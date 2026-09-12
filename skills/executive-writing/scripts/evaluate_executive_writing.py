#!/usr/bin/env python3
"""Deterministic readiness gate for an Executive Communication Operations Pack.

Reads one local JSON file. It does not open attachments, browse, call APIs,
send messages, sign documents, or grant approval.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ALLOWED_MODES = {
    "email",
    "memo_decision_note",
    "directive",
    "announcement",
    "report_message",
    "administrative_letter",
    "public_draft",
}
REQUIRED_TESTS = {
    "bottom_line_5_second",
    "skim_comprehension",
    "claim_trace",
    "actionability",
    "ambiguity_hostile_read",
    "audience_tone",
}


def present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict, tuple, set)):
        return bool(value)
    return True


def require_fields(obj: Any, fields: list[str], path: str, errors: list[str]) -> None:
    if not isinstance(obj, dict):
        errors.append(f"{path} must be an object")
        return
    for field in fields:
        if not present(obj.get(field)):
            errors.append(f"missing {path}.{field}")


def require_list_keys(obj: Any, fields: list[str], path: str, errors: list[str]) -> None:
    if not isinstance(obj, dict):
        return
    for field in fields:
        if field not in obj or not isinstance(obj.get(field), list):
            errors.append(f"missing or invalid {path}.{field}")


def unique_ids(items: list[dict[str, Any]], path: str, errors: list[str]) -> set[str]:
    ids = [str(item.get("id", "")).strip() for item in items]
    if any(not item_id for item_id in ids):
        errors.append(f"{path} contains blank id")
    if len(ids) != len(set(ids)):
        errors.append(f"{path} contains duplicate id")
    return {item_id for item_id in ids if item_id}


def main(input_path: str) -> int:
    payload = json.loads(Path(input_path).read_text(encoding="utf-8"))
    errors: list[str] = []
    warnings: list[str] = []
    guardrails = ["HUMAN_APPROVAL_REQUIRED_BEFORE_SEND_SIGN_PUBLISH_OR_ISSUE"]

    contract = payload.get("contract")
    require_fields(
        contract,
        [
            "id", "mode", "channel", "use", "sender_role", "authority_basis",
            "signature_role", "primary_audience", "purpose", "desired_outcome",
            "decision_or_request", "owner", "reviewer", "approval_route",
            "sensitivity", "status",
        ],
        "contract",
        errors,
    )
    mode = str(contract.get("mode", "")) if isinstance(contract, dict) else ""
    if mode not in ALLOWED_MODES:
        errors.append("contract.mode is not supported")

    sources = payload.get("sources", [])
    if not isinstance(sources, list) or not sources:
        errors.append("sources must be a non-empty list")
        sources = []
    source_ids = unique_ids(sources, "sources", errors)
    active_source_count = 0
    for index, source in enumerate(sources):
        require_fields(
            source,
            ["id", "title", "version", "date", "owner", "authority", "locator", "classification", "status"],
            f"sources[{index}]",
            errors,
        )
        if source.get("authorized") is not True:
            errors.append(f"sources[{index}] is not authorized")
        if source.get("status") == "active":
            active_source_count += 1

    conflicts = payload.get("conflicts", [])
    if not isinstance(conflicts, list):
        errors.append("conflicts must be a list")
        conflicts = []
    unresolved_material_conflicts = 0
    for index, conflict in enumerate(conflicts):
        if conflict.get("material") is True and conflict.get("status") not in {"resolved", "accepted"}:
            unresolved_material_conflicts += 1
            errors.append(f"conflicts[{index}] material conflict is unresolved")

    audiences = payload.get("audiences", [])
    if not isinstance(audiences, list) or not audiences:
        errors.append("audiences must be a non-empty list")
        audiences = []
    audience_ids = unique_ids(audiences, "audiences", errors)
    for index, audience in enumerate(audiences):
        require_fields(
            audience,
            ["id", "role", "name", "power", "knowledge", "concern", "need", "language_accessibility"],
            f"audiences[{index}]",
            errors,
        )
    if audiences and not any(audience.get("role") == "primary" for audience in audiences):
        errors.append("audiences must contain a primary audience")

    authority_statements = payload.get("authority_statements", [])
    if not isinstance(authority_statements, list) or not authority_statements:
        errors.append("authority_statements must be a non-empty list")
        authority_statements = []
    authority_ids = unique_ids(authority_statements, "authority_statements", errors)
    for index, statement in enumerate(authority_statements):
        require_fields(statement, ["id", "text", "basis", "status"], f"authority_statements[{index}]", errors)
        if statement.get("status") not in {"within_authority", "proposal"}:
            errors.append(f"authority_statements[{index}] has invalid status")

    claims = payload.get("claims", [])
    if not isinstance(claims, list) or not claims:
        errors.append("claims must be a non-empty list")
        claims = []
    claim_ids = unique_ids(claims, "claims", errors)
    material_claim_count = 0
    referenced_material_claim_count = 0
    unsupported_material_claim_count = 0
    for index, claim in enumerate(claims):
        require_fields(claim, ["id", "text", "label", "status", "qualifier"], f"claims[{index}]", errors)
        refs = claim.get("source_refs", [])
        bad_refs = sorted(set(refs) - source_ids)
        if bad_refs:
            errors.append(f"claims[{index}] unknown source refs: {', '.join(bad_refs)}")
        if claim.get("material") is True:
            material_claim_count += 1
            if claim.get("status") == "supported" and refs:
                referenced_material_claim_count += 1
            else:
                unsupported_material_claim_count += 1

    actions = payload.get("actions", [])
    if not isinstance(actions, list) or not actions:
        errors.append("actions must be a non-empty list")
        actions = []
    action_ids = unique_ids(actions, "actions", errors)
    for index, action in enumerate(actions):
        require_fields(
            action,
            ["id", "owner", "verb", "deliverable", "deadline", "escalation", "status"],
            f"actions[{index}]",
            errors,
        )

    message_map = payload.get("message_map")
    require_fields(
        message_map,
        ["bottom_line", "decision_or_request", "why_now", "support_blocks", "risk_or_limit", "action_ids", "do_not_say", "approval_route"],
        "message_map",
        errors,
    )
    if isinstance(message_map, dict):
        support_blocks = message_map.get("support_blocks", [])
        if not 1 <= len(support_blocks) <= 3:
            errors.append("message_map.support_blocks must contain 1 to 3 blocks")
        for index, block in enumerate(support_blocks):
            require_fields(block, ["id", "text", "claim_refs"], f"message_map.support_blocks[{index}]", errors)
            bad_claims = sorted(set(block.get("claim_refs", [])) - claim_ids)
            if bad_claims:
                errors.append(f"message_map.support_blocks[{index}] unknown claim refs: {', '.join(bad_claims)}")
        bad_actions = sorted(set(message_map.get("action_ids", [])) - action_ids)
        if bad_actions:
            errors.append("message_map unknown action ids: " + ", ".join(bad_actions))

    document = payload.get("document")
    require_fields(
        document,
        ["mode", "subject_or_title", "status", "opening_bottom_line", "sections", "closing", "signature_role"],
        "document",
        errors,
    )
    if isinstance(document, dict):
        if document.get("mode") != mode:
            errors.append("document.mode must equal contract.mode")
        if document.get("status") not in {"draft_not_approved", "validated_for_review"}:
            errors.append("document.status cannot imply sent or approved")
        if isinstance(message_map, dict) and document.get("opening_bottom_line") != message_map.get("bottom_line"):
            errors.append("document opening must equal message_map.bottom_line")
        for index, section in enumerate(document.get("sections", [])):
            require_fields(section, ["id", "heading", "text"], f"document.sections[{index}]", errors)
            require_list_keys(section, ["claim_refs", "action_refs", "authority_refs"], f"document.sections[{index}]", errors)
            bad_claims = sorted(set(section.get("claim_refs", [])) - claim_ids)
            bad_actions = sorted(set(section.get("action_refs", [])) - action_ids)
            bad_authority = sorted(set(section.get("authority_refs", [])) - authority_ids)
            if bad_claims:
                errors.append(f"document.sections[{index}] unknown claim refs: {', '.join(bad_claims)}")
            if bad_actions:
                errors.append(f"document.sections[{index}] unknown action refs: {', '.join(bad_actions)}")
            if bad_authority:
                errors.append(f"document.sections[{index}] unknown authority refs: {', '.join(bad_authority)}")

    tests = payload.get("tests", [])
    if not isinstance(tests, list):
        errors.append("tests must be a list")
        tests = []
    test_types: set[str] = set()
    test_statuses: list[str] = []
    for index, test in enumerate(tests):
        require_fields(test, ["type", "method", "sample", "threshold", "reviewer", "status"], f"tests[{index}]", errors)
        test_types.add(str(test.get("type", "")))
        test_statuses.append(str(test.get("status", "")))
    missing_tests = sorted(REQUIRED_TESTS - test_types)
    if missing_tests:
        errors.append("missing required tests: " + ", ".join(missing_tests))

    review = payload.get("review")
    require_fields(
        review,
        [
            "source_check", "authority_check", "sensitivity_check", "redactions_complete",
                        "recipient_check", "attachment_check", "validation_state",
        ],
        "review",
        errors,
    )
    require_list_keys(review, ["required_specialist_reviews", "completed_specialist_reviews"], "review", errors)
    review_gaps: list[str] = []
    if isinstance(review, dict):
        for field in ["source_check", "authority_check", "sensitivity_check", "redactions_complete", "recipient_check", "attachment_check"]:
            if review.get(field) is not True:
                review_gaps.append(field)
        required_reviews = set(review.get("required_specialist_reviews", []))
        completed_reviews = set(review.get("completed_specialist_reviews", []))
        missing_specialist_reviews = sorted(required_reviews - completed_reviews)
        if review.get("send_approved") is True:
            guardrails.append("ENGINE_CANNOT_GRANT_OR_VERIFY_SEND_APPROVAL")
    else:
        missing_specialist_reviews = []

    if errors:
        state = "NOT_READY"
        next_action = "resolve_errors_and_rerun"
    elif unsupported_material_claim_count or review_gaps or "failed" in test_statuses:
        state = "DRAFT_READY"
        next_action = "close_claim_review_or_test_gaps"
    elif test_statuses and all(status == "passed" for status in test_statuses) and not missing_specialist_reviews and review.get("validation_state") == "passed":
        state = "VALIDATED_FOR_SEND_REVIEW"
        next_action = "obtain_sender_approval_before_send"
    else:
        state = "READY_FOR_EXECUTIVE_REVIEW"
        next_action = "run_reader_tests_and_required_reviews"

    if missing_specialist_reviews:
        warnings.append("missing specialist reviews: " + ", ".join(missing_specialist_reviews))

    result = {
        "state": state,
        "errors": errors,
        "warnings": warnings,
        "guardrails": guardrails,
        "metrics": {
            "source_count": len(sources),
            "active_source_count": active_source_count,
            "audience_count": len(audience_ids),
            "authority_statement_count": len(authority_ids),
            "material_claim_count": material_claim_count,
            "referenced_material_claim_count": referenced_material_claim_count,
            "unsupported_material_claim_count": unsupported_material_claim_count,
            "action_count": len(action_ids),
            "test_type_coverage": sorted(test_types),
            "unresolved_material_conflict_count": unresolved_material_conflicts,
            "review_gap_count": len(review_gaps),
        },
        "next_action": next_action,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: evaluate_executive_writing.py INPUT.json", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))

