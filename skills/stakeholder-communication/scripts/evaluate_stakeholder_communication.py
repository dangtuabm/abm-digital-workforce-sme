#!/usr/bin/env python3
"""Deterministic static gate for a Stakeholder Communication Control Pack."""

from __future__ import annotations

import argparse
import json
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any, Iterable


TEST_TYPES = {
    "stakeholder_evidence_trace",
    "decision_rights_integrity",
    "message_truth_action",
    "sequence_no_surprise",
    "disclosure_accessibility_fairness",
    "feedback_commitment_closure",
    "approval_state_boundary",
}
REVIEW_TYPES = {
    "FACT_SOURCE",
    "STAKEHOLDER_OPERATIONS",
    "ACCESSIBILITY",
    "RELEASE_APPROVAL",
}
RATING = {"HIGH", "MEDIUM", "LOW", "UNKNOWN"}
STANCE = {"SUPPORTIVE", "CONDITIONAL", "NEUTRAL", "CONCERNED", "OPPOSED", "UNKNOWN"}
RIGHTS = {"PROPOSE", "DECIDE", "APPROVE", "CONSULT", "VETO_OR_ESCALATE", "EXECUTE", "INFORMED"}
FORBIDDEN_STAKEHOLDER_FIELDS = {
    "protected_traits",
    "personality_identity",
    "mental_state",
    "deep_motive",
    "secret_influence",
    "private_profile",
}
FORBIDDEN_MESSAGE_FLAGS = {
    "deception",
    "coercion",
    "hidden_sponsorship",
    "fabricated_endorsement",
    "retaliation",
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


def validate_refs(refs: Any, allowed: set[str], label: str, errors: list[str]) -> None:
    if not isinstance(refs, list) or not refs:
        errors.append(f"{label}: evidence_refs must be a non-empty list")
        return
    unknown = sorted({str(ref) for ref in refs if str(ref) not in allowed})
    if unknown:
        errors.append(f"{label}: unknown evidence refs: {', '.join(unknown)}")


def has_dependency_cycle(entries: list[dict[str, Any]], valid_ids: set[str]) -> bool:
    graph = {str(entry.get("sequence_id")): [str(x) for x in entry.get("dependencies", [])] for entry in entries}
    state: dict[str, int] = {node: 0 for node in valid_ids}

    def visit(node: str) -> bool:
        if state[node] == 1:
            return True
        if state[node] == 2:
            return False
        state[node] = 1
        for dependency in graph.get(node, []):
            if dependency in state and visit(dependency):
                return True
        state[node] = 2
        return False

    return any(visit(node) for node in valid_ids if state[node] == 0)


def evaluate(data: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    contract = data.get("contract") or {}
    require_fields(
        contract,
        (
            "case_id", "version", "outcome", "issue_or_decision", "scope", "stakes",
            "current_state", "desired_state", "source_canon_id", "classification",
            "authority_owner", "communication_owner", "approver", "sender",
            "allowed_channels", "prohibited_actions", "non_negotiables", "retention",
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
        require_fields(source, ("source_id", "title", "version", "locator", "owner", "classification"), f"source[{index}]", errors)
        if source.get("active") is True:
            active_sources.add(str(source.get("source_id")))
    if not active_sources:
        errors.append("sources: at least one active source is required")
    if contract.get("source_canon_id") not in active_sources:
        errors.append("contract: source_canon_id is not active")

    stakeholders = data.get("stakeholders") or []
    stakeholder_ids = unique_ids(stakeholders, "stakeholder_id", "stakeholders", errors)
    banned_inference_count = 0
    high_impact_ids: set[str] = set()
    for index, stakeholder in enumerate(stakeholders):
        label = f"stakeholder[{index}]"
        require_fields(
            stakeholder,
            (
                "stakeholder_id", "role", "organization", "evidence_refs", "power", "interest",
                "impact", "legitimacy", "urgency", "stance", "influence_path", "decision_rights",
                "communication_needs", "disclosure_level", "relationship_owner", "review_owner",
                "confidence", "last_verified",
            ),
            label,
            errors,
        )
        validate_refs(stakeholder.get("evidence_refs"), active_sources, label, errors)
        for field in ("power", "interest", "impact", "legitimacy", "urgency", "confidence"):
            if stakeholder.get(field) not in RATING:
                errors.append(f"{label}: invalid {field}")
        if stakeholder.get("stance") not in STANCE:
            errors.append(f"{label}: invalid stance")
        if stakeholder.get("impact") == "HIGH":
            high_impact_ids.add(str(stakeholder.get("stakeholder_id")))
        for field in FORBIDDEN_STAKEHOLDER_FIELDS:
            if not blank(stakeholder.get(field)):
                banned_inference_count += 1
                errors.append(f"{label}: forbidden inference field {field}")

    issues = data.get("issues") or []
    issue_ids = unique_ids(issues, "issue_id", "issues", errors)
    for index, issue in enumerate(issues):
        label = f"issue[{index}]"
        require_fields(
            issue,
            ("issue_id", "statement", "evidence_refs", "facts", "decision_needed", "non_negotiables", "sensitivity", "owner"),
            label,
            errors,
        )
        validate_refs(issue.get("evidence_refs"), active_sources, label, errors)

    rights = data.get("decision_rights") or []
    final_owners: dict[str, list[str]] = defaultdict(list)
    for index, item in enumerate(rights):
        label = f"decision_right[{index}]"
        require_fields(item, ("issue_id", "stakeholder_id", "right", "evidence_ref"), label, errors)
        issue_id = str(item.get("issue_id", ""))
        stakeholder_id = str(item.get("stakeholder_id", ""))
        right = str(item.get("right", ""))
        if issue_id not in issue_ids:
            errors.append(f"{label}: unknown issue_id")
        if stakeholder_id not in stakeholder_ids:
            errors.append(f"{label}: unknown stakeholder_id")
        if right not in RIGHTS:
            errors.append(f"{label}: invalid right")
        if item.get("evidence_ref") not in active_sources:
            errors.append(f"{label}: evidence_ref is not active")
        if item.get("owner_confirmed") is not True:
            errors.append(f"{label}: owner_confirmed must be true")
        if right in {"DECIDE", "APPROVE"}:
            final_owners[issue_id].append(stakeholder_id)
    for issue_id in issue_ids:
        owners = final_owners.get(issue_id, [])
        if len(owners) != 1:
            errors.append(f"issue {issue_id}: requires exactly one DECIDE/APPROVE owner; found {len(owners)}")

    messages = data.get("messages") or []
    message_ids = unique_ids(messages, "message_id", "messages", errors)
    message_defects = 0
    covered_high_impact: set[str] = set()
    for index, message in enumerate(messages):
        label = f"message[{index}]"
        before = len(errors)
        require_fields(
            message,
            (
                "message_id", "issue_id", "stakeholder_ids", "purpose", "state_now", "must_know",
                "core_message", "evidence_refs", "qualifiers", "impact", "unchanged", "ask",
                "sender", "owner", "channel", "timing", "disclosure_level", "fallback",
                "approval_status",
            ),
            label,
            errors,
        )
        if message.get("issue_id") not in issue_ids:
            errors.append(f"{label}: unknown issue_id")
        recipients = {str(item) for item in message.get("stakeholder_ids", [])}
        unknown_recipients = sorted(recipients - stakeholder_ids)
        if unknown_recipients:
            errors.append(f"{label}: unknown stakeholder_ids: {', '.join(unknown_recipients)}")
        covered_high_impact.update(recipients & high_impact_ids)
        validate_refs(message.get("evidence_refs"), active_sources, label, errors)
        ask = message.get("ask") or {}
        require_fields(ask, ("action", "owner", "due"), f"{label}.ask", errors)
        for flag in FORBIDDEN_MESSAGE_FLAGS:
            if message.get(flag) is True:
                errors.append(f"{label}: forbidden practice flag {flag}")
        if len(errors) > before:
            message_defects += 1
    missing_high_impact = sorted(high_impact_ids - covered_high_impact)
    if missing_high_impact:
        errors.append(f"messages: high-impact stakeholders not covered: {', '.join(missing_high_impact)}")

    sequence = data.get("sequence") or []
    sequence_ids = unique_ids(sequence, "sequence_id", "sequence", errors)
    orders: list[int] = []
    sequence_message_refs: set[str] = set()
    for index, entry in enumerate(sequence):
        label = f"sequence[{index}]"
        require_fields(
            entry,
            ("sequence_id", "order", "message_ids", "stakeholder_ids", "precondition", "reason", "owner", "approval_status", "status"),
            label,
            errors,
        )
        try:
            order = int(entry.get("order"))
            orders.append(order)
            if order < 1:
                errors.append(f"{label}: order must be positive")
        except (TypeError, ValueError):
            errors.append(f"{label}: order must be an integer")
        refs = {str(item) for item in entry.get("message_ids", [])}
        sequence_message_refs.update(refs)
        if refs - message_ids:
            errors.append(f"{label}: unknown message_ids")
        recipients = {str(item) for item in entry.get("stakeholder_ids", [])}
        if recipients - stakeholder_ids:
            errors.append(f"{label}: unknown stakeholder_ids")
        dependencies = {str(item) for item in entry.get("dependencies", [])}
        if dependencies - sequence_ids:
            errors.append(f"{label}: unknown dependencies")
        if entry.get("no_surprise") is not True:
            errors.append(f"{label}: no_surprise must be true")
    if len(orders) != len(set(orders)):
        errors.append("sequence: duplicate order")
    if message_ids - sequence_message_refs:
        errors.append("sequence: not all messages are scheduled")
    if has_dependency_cycle(sequence, sequence_ids):
        errors.append("sequence: dependency cycle detected")

    feedback_items = data.get("feedback_items") or []
    unique_ids(feedback_items, "item_id", "feedback_items", errors)
    for index, item in enumerate(feedback_items):
        label = f"feedback[{index}]"
        require_fields(item, ("item_id", "stakeholder_id", "issue_id", "question_or_objection", "source_ref", "owner", "due", "status"), label, errors)
        if item.get("stakeholder_id") not in stakeholder_ids or item.get("issue_id") not in issue_ids:
            errors.append(f"{label}: unknown stakeholder or issue")
        if item.get("source_ref") not in active_sources:
            errors.append(f"{label}: source_ref is not active")

    commitments = data.get("commitments") or []
    unique_ids(commitments, "commitment_id", "commitments", errors)
    for index, item in enumerate(commitments):
        label = f"commitment[{index}]"
        require_fields(item, ("commitment_id", "stakeholder_id", "issue_id", "commitment", "source_ref", "owner", "due", "approver", "status"), label, errors)
        if item.get("stakeholder_id") not in stakeholder_ids or item.get("issue_id") not in issue_ids:
            errors.append(f"{label}: unknown stakeholder or issue")
        if item.get("source_ref") not in active_sources:
            errors.append(f"{label}: source_ref is not active")

    risks = data.get("risks") or []
    unique_ids(risks, "risk_id", "risks", errors)
    for index, risk in enumerate(risks):
        label = f"risk[{index}]"
        require_fields(
            risk,
            ("risk_id", "type", "trigger", "affected_party", "harm", "prevention", "stop_or_rollback", "escalation_owner", "evidence_refs"),
            label,
            errors,
        )
        validate_refs(risk.get("evidence_refs"), active_sources, label, errors)

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
    present_review_types = {str(item.get("review_type", "")) for item in reviews if item.get("required") is True}
    missing_reviews = sorted(REVIEW_TYPES - present_review_types)
    if missing_reviews:
        errors.append(f"reviews: missing required types: {', '.join(missing_reviews)}")
    for index, review in enumerate(reviews):
        require_fields(review, ("review_type", "reviewer", "status"), f"review[{index}]", errors)
        if review.get("required") is True and review.get("status") not in {"PASS", "PENDING"}:
            errors.append(f"review[{index}]: invalid required review status")
        if review.get("status") == "PASS" and blank(review.get("evidence_ref")):
            errors.append(f"review[{index}]: PASS requires evidence_ref")

    required_reviews_pass = bool(reviews) and all(
        review.get("status") == "PASS" for review in reviews if review.get("required") is True
    )
    message_approvals_pass = bool(messages) and all(
        (not message.get("approval_required")) or message.get("approval_status") == "APPROVED"
        for message in messages
    )
    sequence_approvals_pass = bool(sequence) and all(
        entry.get("approval_status") == "APPROVED" for entry in sequence
    )

    if errors:
        state = "NOT_READY"
    elif required_reviews_pass and message_approvals_pass and sequence_approvals_pass:
        state = "READY_FOR_AUTHORIZED_RELEASE"
    else:
        state = "READY_FOR_STAKEHOLDER_REVIEW"
        warnings.append("Human review/approval remains; the engine does not authorize or release communication")

    return {
        "case_id": contract.get("case_id", ""),
        "state": state,
        "metrics": {
            "sources": len(source_ids),
            "active_sources": len(active_sources),
            "stakeholders": len(stakeholder_ids),
            "high_impact_stakeholders": len(high_impact_ids),
            "issues": len(issue_ids),
            "decision_rights": len(rights),
            "messages": len(message_ids),
            "sequence_steps": len(sequence_ids),
            "feedback_items": len(feedback_items),
            "commitments": len(commitments),
            "risks": len(risks),
            "test_types": len(present_test_types & TEST_TYPES),
            "banned_inference_count": banned_inference_count,
            "message_defects": message_defects,
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
