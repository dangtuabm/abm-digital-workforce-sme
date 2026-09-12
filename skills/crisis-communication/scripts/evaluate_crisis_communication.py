#!/usr/bin/env python3
"""Deterministic static gate for a Crisis Communication Command Pack."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


TEST_TYPES = {
    "command_authority_integrity",
    "fact_unknown_trace",
    "message_safety_action",
    "stakeholder_disclosure",
    "cadence_version_control",
    "rumor_correction",
    "approval_release_boundary",
}
REVIEW_TYPES = {
    "INCIDENT_COMMAND",
    "FACT_TECH",
    "LEGAL_PRIVACY",
    "ACCESSIBILITY",
    "FINAL_RELEASE",
}
RUMOR_STATES = {"UNVERIFIED", "CORRECTED"}
MESSAGE_DRAFT_STATES = {"DRAFT", "REVIEW_PENDING", "REVIEWED"}
FORBIDDEN_MESSAGE_STATES = {"APPROVED", "RELEASED", "SENT", "PUBLISHED", "CLOSED"}
FORBIDDEN_INCIDENT_FIELDS = {
    "fabricated_cause",
    "blame_target",
    "liability_conclusion",
    "unauthorized_compensation",
}
FORBIDDEN_MESSAGE_FLAGS = {
    "false_reassurance",
    "conceal_material_harm",
    "speculative_cause",
    "speculative_blame",
    "contains_restricted_data",
    "unauthorized_admission",
    "unauthorized_commitment",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("Root JSON must be an object")
    return data


def blank(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def require_fields(obj: dict[str, Any], fields: Iterable[str], label: str, errors: list[str]) -> None:
    for field in fields:
        if field not in obj or blank(obj[field]):
            errors.append(f"{label}: missing {field}")


def unique_ids(items: list[dict[str, Any]], field: str, label: str, errors: list[str]) -> set[str]:
    values = [str(item.get(field, "")).strip() for item in items]
    if any(not value for value in values):
        errors.append(f"{label}: blank {field}")
    duplicates = [value for value, count in Counter(values).items() if value and count > 1]
    if duplicates:
        errors.append(f"{label}: duplicate {field}: {', '.join(sorted(duplicates))}")
    return {value for value in values if value}


def validate_refs(refs: Any, valid: set[str], label: str, field: str, errors: list[str]) -> set[str]:
    if not isinstance(refs, list) or not refs:
        errors.append(f"{label}: {field} must be a non-empty list")
        return set()
    normalized = {str(ref) for ref in refs}
    unknown = sorted(normalized - valid)
    if unknown:
        errors.append(f"{label}: unknown {field}: {', '.join(unknown)}")
    return normalized


def evaluate(data: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    contract = data.get("contract") or {}
    require_fields(
        contract,
        (
            "case_id", "version", "outcome", "scope", "incident_command", "communication_lead",
            "spokesperson", "final_approver", "command_evidence_ref", "classification", "retention",
            "allowed_channels", "emergency_stop_owner", "prohibited_actions", "stop_or_escalation",
            "required_reviews",
        ),
        "contract",
        errors,
    )
    if contract.get("data_authorized") is not True:
        errors.append("contract: data_authorized must be true")

    sources = data.get("sources") or []
    source_ids = unique_ids(sources, "source_id", "sources", errors)
    active_sources: set[str] = set()
    for index, source in enumerate(sources):
        label = f"source[{index}]"
        require_fields(
            source,
            ("source_id", "title", "version", "locator", "owner", "classification", "effective_date"),
            label,
            errors,
        )
        if source.get("active") is True:
            active_sources.add(str(source.get("source_id")))
    if not active_sources:
        errors.append("sources: at least one active source is required")
    if contract.get("command_evidence_ref") not in active_sources:
        errors.append("contract: command_evidence_ref is not active")

    incident = data.get("incident") or {}
    require_fields(
        incident,
        (
            "incident_id", "title", "status", "severity", "severity_owner", "affected_scope",
            "started_at", "last_verified", "source_refs", "data_impact_status", "incident_owner",
        ),
        "incident",
        errors,
    )
    validate_refs(incident.get("source_refs"), active_sources, "incident", "source_refs", errors)
    forbidden_incident_count = 0
    for field in FORBIDDEN_INCIDENT_FIELDS:
        if not blank(incident.get(field)):
            forbidden_incident_count += 1
            errors.append(f"incident: forbidden field {field}")
    if incident.get("closed_by_ai") is True:
        errors.append("incident: A.I cannot close an incident")

    facts = data.get("facts") or []
    fact_ids = unique_ids(facts, "fact_id", "facts", errors)
    for index, fact in enumerate(facts):
        label = f"fact[{index}]"
        require_fields(
            fact,
            ("fact_id", "statement", "status", "source_refs", "locator", "owner", "last_verified"),
            label,
            errors,
        )
        if fact.get("status") != "CONFIRMED":
            errors.append(f"{label}: status must be CONFIRMED")
        validate_refs(fact.get("source_refs"), active_sources, label, "source_refs", errors)

    unknowns = data.get("unknowns") or []
    unknown_ids = unique_ids(unknowns, "unknown_id", "unknowns", errors)
    for index, unknown in enumerate(unknowns):
        require_fields(
            unknown,
            ("unknown_id", "statement", "owner", "next_evidence", "due_condition", "communication_treatment"),
            f"unknown[{index}]",
            errors,
        )

    stakeholders = data.get("stakeholders") or []
    stakeholder_ids = unique_ids(stakeholders, "stakeholder_id", "stakeholders", errors)
    for index, stakeholder in enumerate(stakeholders):
        label = f"stakeholder[{index}]"
        require_fields(
            stakeholder,
            (
                "stakeholder_id", "group", "need", "impact", "disclosure_basis", "allowed_fields",
                "withheld_fields", "required_action", "channel", "accessibility", "owner", "sequence",
                "feedback_route", "evidence_refs",
            ),
            label,
            errors,
        )
        validate_refs(stakeholder.get("evidence_refs"), active_sources, label, "evidence_refs", errors)
        try:
            if int(stakeholder.get("sequence")) < 1:
                errors.append(f"{label}: sequence must be positive")
        except (TypeError, ValueError):
            errors.append(f"{label}: sequence must be an integer")

    messages = data.get("messages") or []
    message_ids = unique_ids(messages, "message_id", "messages", errors)
    covered_stakeholders: set[str] = set()
    forbidden_message_count = 0
    untraced_claim_count = 0
    unauthorized_release_count = 0
    for index, message in enumerate(messages):
        label = f"message[{index}]"
        require_fields(
            message,
            (
                "message_id", "message_type", "stakeholder_ids", "purpose", "channel", "core_message",
                "fact_ids", "unknown_ids", "source_refs", "required_action", "next_update", "version",
                "owner", "spokesperson", "disclosure_class", "approval_status",
            ),
            label,
            errors,
        )
        stakeholder_refs = validate_refs(
            message.get("stakeholder_ids"), stakeholder_ids, label, "stakeholder_ids", errors
        )
        covered_stakeholders |= stakeholder_refs & stakeholder_ids
        fact_refs = validate_refs(message.get("fact_ids"), fact_ids, label, "fact_ids", errors)
        unknown_refs_raw = message.get("unknown_ids")
        if not isinstance(unknown_refs_raw, list):
            errors.append(f"{label}: unknown_ids must be a list")
            unknown_refs: set[str] = set()
        else:
            unknown_refs = {str(item) for item in unknown_refs_raw}
            invalid_unknowns = sorted(unknown_refs - unknown_ids)
            if invalid_unknowns:
                errors.append(f"{label}: unknown unknown_ids: {', '.join(invalid_unknowns)}")
        validate_refs(message.get("source_refs"), active_sources, label, "source_refs", errors)
        claim_refs = {str(item) for item in message.get("claim_refs", [])}
        invalid_claims = claim_refs - fact_ids - unknown_ids
        if invalid_claims or not claim_refs or not claim_refs.issubset(fact_refs | unknown_refs):
            untraced_claim_count += 1
            errors.append(f"{label}: claim_refs are missing or not fully traced")
        approval = str(message.get("approval_status", ""))
        if approval in FORBIDDEN_MESSAGE_STATES:
            unauthorized_release_count += 1
            errors.append(f"{label}: forbidden approval/release state {approval}")
        elif approval not in MESSAGE_DRAFT_STATES:
            errors.append(f"{label}: invalid approval_status")
        for flag in FORBIDDEN_MESSAGE_FLAGS:
            if message.get(flag) is True:
                forbidden_message_count += 1
                errors.append(f"{label}: forbidden message flag {flag}")
    missing_stakeholders = sorted(stakeholder_ids - covered_stakeholders)
    if missing_stakeholders:
        errors.append(f"messages: stakeholders not covered: {', '.join(missing_stakeholders)}")

    sequence = data.get("sequence") or []
    sequence_ids = unique_ids(sequence, "sequence_id", "sequence", errors)
    sequenced_messages: set[str] = set()
    for index, item in enumerate(sequence):
        label = f"sequence[{index}]"
        require_fields(
            item,
            ("sequence_id", "order", "message_id", "stakeholder_id", "dependency", "fallback", "owner"),
            label,
            errors,
        )
        if item.get("message_id") not in message_ids or item.get("stakeholder_id") not in stakeholder_ids:
            errors.append(f"{label}: unknown message_id or stakeholder_id")
        else:
            sequenced_messages.add(str(item.get("message_id")))
        try:
            if int(item.get("order")) < 1:
                errors.append(f"{label}: order must be positive")
        except (TypeError, ValueError):
            errors.append(f"{label}: order must be an integer")
    missing_sequence = sorted(message_ids - sequenced_messages)
    if missing_sequence:
        errors.append(f"sequence: messages not sequenced: {', '.join(missing_sequence)}")

    rumors = data.get("rumors") or []
    rumor_ids = unique_ids(rumors, "rumor_id", "rumors", errors)
    for index, rumor in enumerate(rumors):
        label = f"rumor[{index}]"
        require_fields(
            rumor,
            ("rumor_id", "claim", "status", "evidence_refs", "response", "owner", "last_checked"),
            label,
            errors,
        )
        if rumor.get("status") not in RUMOR_STATES:
            errors.append(f"{label}: invalid status")
        validate_refs(rumor.get("evidence_refs"), active_sources, label, "evidence_refs", errors)

    updates = data.get("update_schedule") or []
    update_ids = unique_ids(updates, "update_id", "update_schedule", errors)
    for index, update in enumerate(updates):
        label = f"update[{index}]"
        require_fields(
            update,
            ("update_id", "message_ids", "timestamp_or_trigger", "source_snapshot", "owner", "approver", "change_log_route"),
            label,
            errors,
        )
        validate_refs(update.get("message_ids"), message_ids, label, "message_ids", errors)
        validate_refs(update.get("source_snapshot"), active_sources, label, "source_snapshot", errors)

    risks = data.get("risks") or []
    risk_ids = unique_ids(risks, "risk_id", "risks", errors)
    for index, risk in enumerate(risks):
        label = f"risk[{index}]"
        require_fields(
            risk,
            ("risk_id", "type", "trigger", "harm", "prevention", "stop_or_rollback", "escalation_owner", "evidence_refs"),
            label,
            errors,
        )
        validate_refs(risk.get("evidence_refs"), active_sources, label, "evidence_refs", errors)

    tests = data.get("tests") or []
    present_test_types = {str(item.get("test_type", "")) for item in tests}
    missing_tests = sorted(TEST_TYPES - present_test_types)
    if missing_tests:
        errors.append(f"tests: missing types: {', '.join(missing_tests)}")
    for index, test in enumerate(tests):
        require_fields(test, ("test_type", "evidence", "reviewer", "date"), f"test[{index}]", errors)
        if test.get("passed") is not True:
            errors.append(f"test[{index}]: passed must be true")

    reviews = data.get("reviews") or []
    present_reviews = {str(item.get("review_type", "")) for item in reviews if item.get("required") is True}
    missing_reviews = sorted(REVIEW_TYPES - present_reviews)
    if missing_reviews:
        errors.append(f"reviews: missing required types: {', '.join(missing_reviews)}")
    for index, review in enumerate(reviews):
        label = f"review[{index}]"
        require_fields(review, ("review_type", "reviewer", "status"), label, errors)
        if review.get("required") is True and review.get("status") not in {"PASS", "PENDING"}:
            errors.append(f"{label}: invalid required review status")
        if review.get("status") == "PASS" and blank(review.get("evidence_ref")):
            errors.append(f"{label}: PASS requires evidence_ref")

    final_release_pass = any(
        review.get("review_type") == "FINAL_RELEASE"
        and review.get("required") is True
        and review.get("status") == "PASS"
        and not blank(review.get("evidence_ref"))
        for review in reviews
    )
    required_reviews_pass = bool(reviews) and all(
        review.get("status") == "PASS" for review in reviews if review.get("required") is True
    )

    if errors:
        state = "NOT_READY"
    elif required_reviews_pass and final_release_pass:
        state = "READY_FOR_AUTHORIZED_RELEASE"
        warnings.append("Human release decision and channel execution remain outside the engine")
    else:
        state = "READY_FOR_CRISIS_REVIEW"
        warnings.append("Required human reviews remain; the engine does not approve, send, publish, or close")

    return {
        "case_id": contract.get("case_id", ""),
        "state": state,
        "metrics": {
            "sources": len(source_ids),
            "active_sources": len(active_sources),
            "facts": len(fact_ids),
            "unknowns": len(unknown_ids),
            "stakeholders": len(stakeholder_ids),
            "messages": len(message_ids),
            "sequence_steps": len(sequence_ids),
            "rumors": len(rumor_ids),
            "updates": len(update_ids),
            "risks": len(risk_ids),
            "test_types": len(present_test_types & TEST_TYPES),
            "forbidden_incident_count": forbidden_incident_count,
            "forbidden_message_count": forbidden_message_count,
            "untraced_claim_count": untraced_claim_count,
            "unauthorized_release_count": unauthorized_release_count,
            "critical_defects": len(errors),
        },
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate(load_json(args.input))
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if result["state"] != "NOT_READY" else 1


if __name__ == "__main__":
    raise SystemExit(main())
