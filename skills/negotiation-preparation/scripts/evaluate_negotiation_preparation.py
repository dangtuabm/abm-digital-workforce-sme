#!/usr/bin/env python3
"""Deterministic static gate for a Negotiation Preparation & Mandate Pack."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


TEST_TYPES = {
    "mandate_authority_integrity",
    "source_assumption_trace",
    "batna_reservation_zopa",
    "issue_trade_package_integrity",
    "concession_reciprocity",
    "scenario_question_process",
    "approval_agreement_boundary",
}
REVIEW_TYPES = {
    "MANDATE_OWNER",
    "FINANCE",
    "LEGAL_COMPLIANCE",
    "ETHICS_CONFLICT",
    "FINAL_SESSION_AUTHORIZATION",
}
PRIORITIES = {"MUST", "HIGH", "MEDIUM", "LOW"}
AUTHORITY_STATES = {"CONFIRMED", "CONDITIONAL", "UNKNOWN", "PROHIBITED"}
ZOPA_STATES = {"UNKNOWN", "ESTIMATED", "CONFIRMED"}
CONFIDENCE = {"HIGH", "MEDIUM", "LOW"}
FORBIDDEN_COUNTERPARTY_FIELDS = {
    "protected_traits",
    "private_pressure_point",
    "personality_diagnosis",
    "secret_personal_data",
    "fabricated_leverage",
}
FORBIDDEN_TRADE_FLAGS = {
    "bribery",
    "kickback",
    "collusion",
    "bid_rigging",
    "threat",
    "deception",
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


def validate_refs(refs: Any, active_sources: set[str], label: str, errors: list[str]) -> None:
    if not isinstance(refs, list) or not refs:
        errors.append(f"{label}: evidence_refs must be a non-empty list")
        return
    unknown = sorted({str(ref) for ref in refs if str(ref) not in active_sources})
    if unknown:
        errors.append(f"{label}: unknown evidence refs: {', '.join(unknown)}")


def evaluate(data: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    contract = data.get("contract") or {}
    require_fields(
        contract,
        (
            "case_id", "version", "negotiation_type", "primary_session_objective",
            "relationship_objective", "scope", "stakes", "planned_session", "mandate_owner",
            "negotiator", "final_approver", "mandate_evidence_ref", "authority_expiry",
            "classification", "retention", "allowed_channels", "non_negotiables",
            "prohibited_actions", "stop_or_escalation", "required_reviews",
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
        require_fields(
            source,
            ("source_id", "title", "version", "locator", "owner", "classification", "effective_date"),
            f"source[{index}]",
            errors,
        )
        if source.get("active") is True:
            active_sources.add(str(source.get("source_id")))
    if not active_sources:
        errors.append("sources: at least one active source is required")
    if contract.get("mandate_evidence_ref") not in active_sources:
        errors.append("contract: mandate_evidence_ref is not active")

    counterparties = data.get("counterparties") or []
    counterparty_ids = unique_ids(counterparties, "counterparty_id", "counterparties", errors)
    forbidden_inference_count = 0
    hypothesis_count = 0
    for index, party in enumerate(counterparties):
        label = f"counterparty[{index}]"
        require_fields(
            party,
            (
                "counterparty_id", "role", "organization", "evidence_refs", "known_authority",
                "known_interests", "known_constraints", "process_or_timeline", "owner", "last_verified",
            ),
            label,
            errors,
        )
        validate_refs(party.get("evidence_refs"), active_sources, label, errors)
        for field in FORBIDDEN_COUNTERPARTY_FIELDS:
            if not blank(party.get(field)):
                forbidden_inference_count += 1
                errors.append(f"{label}: forbidden inference field {field}")
        hypotheses = party.get("hypotheses") or []
        hypothesis_count += len(hypotheses)
        for h_index, hypothesis in enumerate(hypotheses):
            h_label = f"{label}.hypothesis[{h_index}]"
            require_fields(
                hypothesis,
                ("statement", "evidence_refs", "alternative", "confidence", "expiry", "falsifier", "test_question"),
                h_label,
                errors,
            )
            validate_refs(hypothesis.get("evidence_refs"), active_sources, h_label, errors)
            if hypothesis.get("confidence") not in CONFIDENCE:
                errors.append(f"{h_label}: invalid confidence")

    issues = data.get("issues") or []
    issue_ids = unique_ids(issues, "issue_id", "issues", errors)
    must_issue_ids: set[str] = set()
    tradable_issue_ids: set[str] = set()
    unauthorized_issue_count = 0
    for index, issue in enumerate(issues):
        label = f"issue[{index}]"
        require_fields(
            issue,
            (
                "issue_id", "statement", "priority", "target", "reservation_boundary",
                "walk_away_condition", "objective_criteria", "evidence_refs", "owner",
                "authority_state", "authority_owner", "approval_evidence_ref", "expiry",
            ),
            label,
            errors,
        )
        validate_refs(issue.get("evidence_refs"), active_sources, label, errors)
        if issue.get("priority") not in PRIORITIES:
            errors.append(f"{label}: invalid priority")
        if issue.get("priority") == "MUST":
            must_issue_ids.add(str(issue.get("issue_id")))
        if issue.get("tradable") is True:
            tradable_issue_ids.add(str(issue.get("issue_id")))
        if issue.get("authority_state") != "CONFIRMED" or issue.get("reservation_approved") is not True:
            unauthorized_issue_count += 1
            errors.append(f"{label}: reservation/authority is not confirmed")
        if issue.get("approval_evidence_ref") not in active_sources:
            errors.append(f"{label}: approval_evidence_ref is not active")

    alternatives = data.get("alternatives") or []
    alternative_ids = unique_ids(alternatives, "alternative_id", "alternatives", errors)
    active_batnas: list[str] = []
    for index, alternative in enumerate(alternatives):
        label = f"alternative[{index}]"
        require_fields(
            alternative,
            ("alternative_id", "type", "description", "feasibility", "status", "evidence_refs", "owner", "trigger", "cost_or_value"),
            label,
            errors,
        )
        validate_refs(alternative.get("evidence_refs"), active_sources, label, errors)
        if alternative.get("active") is True:
            if alternative.get("type") != "BATNA" or alternative.get("status") != "VERIFIED":
                errors.append(f"{label}: active alternative must be a VERIFIED BATNA")
            active_batnas.append(str(alternative.get("alternative_id")))
    if len(active_batnas) != 1:
        errors.append(f"alternatives: exactly one active VERIFIED BATNA required; found {len(active_batnas)}")

    zopa = data.get("zopa") or {}
    require_fields(
        zopa,
        (
            "status", "our_reservation_issue_ids", "counterparty_boundary_basis", "range_or_overlap",
            "evidence_refs", "owner", "review_trigger",
        ),
        "zopa",
        errors,
    )
    if zopa.get("status") not in ZOPA_STATES:
        errors.append("zopa: invalid status")
    reservation_refs = {str(item) for item in zopa.get("our_reservation_issue_ids", [])}
    if reservation_refs - issue_ids:
        errors.append("zopa: unknown reservation issue ids")
    validate_refs(zopa.get("evidence_refs"), active_sources, "zopa", errors)
    if zopa.get("status") == "ESTIMATED" and not zopa.get("assumptions"):
        errors.append("zopa: ESTIMATED requires assumptions")
    if zopa.get("status") == "UNKNOWN" and zopa.get("range_or_overlap") != "UNKNOWN":
        errors.append("zopa: UNKNOWN status cannot claim a range")

    trades = data.get("trades") or []
    trade_ids = unique_ids(trades, "trade_id", "trades", errors)
    covered_tradable_issues: set[str] = set()
    unauthorized_trade_count = 0
    unilateral_concession_count = 0
    for index, trade in enumerate(trades):
        label = f"trade[{index}]"
        require_fields(
            trade,
            (
                "trade_id", "issue_id", "give", "give_cost_or_impact", "get", "get_value_or_impact",
                "evidence_refs", "preconditions", "authority_state", "authority_owner",
                "approval_evidence_ref", "sequence", "expiry", "stop_condition", "status",
            ),
            label,
            errors,
        )
        issue_id = str(trade.get("issue_id", ""))
        if issue_id not in issue_ids:
            errors.append(f"{label}: unknown issue_id")
        else:
            covered_tradable_issues.add(issue_id)
        validate_refs(trade.get("evidence_refs"), active_sources, label, errors)
        if trade.get("authority_state") != "CONFIRMED":
            unauthorized_trade_count += 1
            errors.append(f"{label}: authority_state must be CONFIRMED")
        if trade.get("approval_evidence_ref") not in active_sources:
            errors.append(f"{label}: approval_evidence_ref is not active")
        if blank(trade.get("get")) or blank(trade.get("get_value_or_impact")):
            unilateral_concession_count += 1
            errors.append(f"{label}: unilateral concession is not allowed")
        for flag in FORBIDDEN_TRADE_FLAGS:
            if trade.get(flag) is True:
                errors.append(f"{label}: forbidden practice flag {flag}")
        try:
            if int(trade.get("sequence")) < 1:
                errors.append(f"{label}: sequence must be positive")
        except (TypeError, ValueError):
            errors.append(f"{label}: sequence must be an integer")
    missing_trades = sorted(tradable_issue_ids - covered_tradable_issues)
    if missing_trades:
        errors.append(f"trades: tradable issues not covered: {', '.join(missing_trades)}")

    packages = data.get("packages") or []
    package_ids = unique_ids(packages, "package_id", "packages", errors)
    if len(package_ids) < 2:
        errors.append("packages: at least two package options are required")
    for index, package in enumerate(packages):
        label = f"package[{index}]"
        require_fields(
            package,
            (
                "package_id", "name", "trade_ids", "issue_ids", "rationale", "total_economics",
                "valuation_status", "evidence_refs", "owner", "status",
            ),
            label,
            errors,
        )
        trade_refs = {str(item) for item in package.get("trade_ids", [])}
        issue_refs = {str(item) for item in package.get("issue_ids", [])}
        if trade_refs - trade_ids:
            errors.append(f"{label}: unknown trade_ids")
        if issue_refs - issue_ids:
            errors.append(f"{label}: unknown issue_ids")
        if not must_issue_ids.issubset(issue_refs):
            errors.append(f"{label}: package omits MUST issue")
        validate_refs(package.get("evidence_refs"), active_sources, label, errors)
        if package.get("valuation_status") != "REVIEWED":
            errors.append(f"{label}: valuation_status must be REVIEWED for readiness")

    questions = data.get("questions") or []
    question_ids = unique_ids(questions, "question_id", "questions", errors)
    for index, question in enumerate(questions):
        label = f"question[{index}]"
        require_fields(
            question,
            ("question_id", "counterparty_id", "issue_id", "purpose", "question", "evidence_sought", "follow_up", "owner"),
            label,
            errors,
        )
        if question.get("counterparty_id") not in counterparty_ids or question.get("issue_id") not in issue_ids:
            errors.append(f"{label}: unknown counterparty or issue")

    scenarios = data.get("scenarios") or []
    scenario_ids = unique_ids(scenarios, "scenario_id", "scenarios", errors)
    for index, scenario in enumerate(scenarios):
        require_fields(
            scenario,
            ("scenario_id", "trigger", "counterparty_move", "evidence_basis", "planned_response", "authority_gate", "stop_or_escalate", "owner"),
            f"scenario[{index}]",
            errors,
        )

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
    present_reviews = {str(item.get("review_type", "")) for item in reviews if item.get("required") is True}
    missing_reviews = sorted(REVIEW_TYPES - present_reviews)
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
    if errors:
        state = "NOT_READY"
    elif required_reviews_pass:
        state = "READY_FOR_AUTHORIZED_SESSION"
    else:
        state = "READY_FOR_MANDATE_REVIEW"
        warnings.append("Human mandate/review remains; the engine does not authorize a session or negotiation move")

    return {
        "case_id": contract.get("case_id", ""),
        "state": state,
        "metrics": {
            "sources": len(source_ids),
            "active_sources": len(active_sources),
            "counterparties": len(counterparty_ids),
            "hypotheses": hypothesis_count,
            "issues": len(issue_ids),
            "alternatives": len(alternative_ids),
            "active_batnas": len(active_batnas),
            "trades": len(trade_ids),
            "packages": len(package_ids),
            "questions": len(question_ids),
            "scenarios": len(scenario_ids),
            "risks": len(risk_ids),
            "test_types": len(present_test_types & TEST_TYPES),
            "forbidden_inference_count": forbidden_inference_count,
            "unauthorized_issue_count": unauthorized_issue_count,
            "unauthorized_trade_count": unauthorized_trade_count,
            "unilateral_concession_count": unilateral_concession_count,
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
