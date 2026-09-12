#!/usr/bin/env python3
"""Static control engine for the organization-design Skill."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_REVIEWS = {
    "ORG_SPONSOR",
    "PEOPLE_LEGAL_COMPLIANCE",
    "DATA_SECURITY",
    "FINAL_ORG_DECISION",
}
SPECIALIST_REVIEWS = REQUIRED_REVIEWS - {"FINAL_ORG_DECISION"}
REQUIRED_TESTS = {
    "strategy_capability_trace",
    "role_accountability",
    "decision_rights",
    "interface_sod",
    "span_layer_capacity",
    "human_ai_boundary",
    "implementation_boundary",
}
REQUIRED_SECTIONS = {
    "executive_decision_brief",
    "strategy_capability_trace",
    "current_state_diagnosis",
    "target_unit_and_role_charters",
    "decision_rights",
    "interface_and_sod",
    "human_ai_allocation",
    "option_comparison",
    "transition_control",
    "tests_reviews_audit",
}
AI_MODES = {"ANALYZE", "DRAFT", "CHECK", "ALERT", "NONE"}
FORBIDDEN_FLAGS = {
    "role_invented",
    "accountability_duplicated",
    "decision_owner_duplicated",
    "gap_hidden",
    "overlap_hidden",
    "span_assumed",
    "fte_fabricated",
    "ai_made_accountable",
    "sod_bypassed",
    "auto_hired",
    "auto_fired",
    "auto_promoted",
    "auto_demoted",
    "pay_changed",
    "reporting_changed",
    "permission_changed",
    "auto_reorganized",
}
FORBIDDEN_STATES = {
    "HIRED",
    "FIRED",
    "PROMOTED",
    "DEMOTED",
    "APPOINTED",
    "REASSIGNED",
    "REORGANIZED",
    "APPROVED",
    "IMPLEMENTED",
}


def nonempty(value: Any) -> bool:
    return value is not None and value != "" and value != [] and value != {}


def rows(data: dict[str, Any], key: str, defects: list[str]) -> list[dict[str, Any]]:
    value = data.get(key)
    if not isinstance(value, list) or not value:
        defects.append(f"{key}:missing_or_empty")
        return []
    if any(not isinstance(item, dict) for item in value):
        defects.append(f"{key}:contains_non_object")
        return [item for item in value if isinstance(item, dict)]
    return value


def index_unique(items: list[dict[str, Any]], key: str, label: str, defects: list[str]) -> dict[str, dict[str, Any]]:
    result: dict[str, dict[str, Any]] = {}
    for pos, item in enumerate(items):
        item_id = item.get(key)
        if not nonempty(item_id):
            defects.append(f"{label}[{pos}]:missing_{key}")
        elif not isinstance(item_id, str):
            defects.append(f"{label}[{pos}]:invalid_{key}")
        elif item_id in result:
            defects.append(f"{label}:{key}_duplicate:{item_id}")
        else:
            result[item_id] = item
    return result


def require_fields(item: dict[str, Any], fields: list[str], prefix: str, defects: list[str]) -> None:
    for field in fields:
        if not nonempty(item.get(field)):
            defects.append(f"{prefix}:missing_{field}")


def references_exist(values: Any, valid: set[str], prefix: str, defects: list[str]) -> None:
    if not isinstance(values, list) or not values:
        defects.append(f"{prefix}:missing_references")
        return
    unknown = sorted({str(value) for value in values if value not in valid})
    if unknown:
        defects.append(f"{prefix}:unknown_references:{','.join(unknown)}")


def validate(data: dict[str, Any]) -> dict[str, Any]:
    defects: list[str] = []
    review_gaps: list[str] = []

    contract = data.get("design_contract")
    if not isinstance(contract, dict):
        defects.append("design_contract:missing")
        contract = {}
    require_fields(
        contract,
        ["organization_scope", "as_of", "strategy_source", "data_classification", "sponsor", "final_decision_owner", "required_reviews", "prohibited_actions"],
        "design_contract",
        defects,
    )
    if contract.get("data_classification") not in {"GREEN", "YELLOW", "RED"}:
        defects.append("design_contract:invalid_data_classification")
    required_review_values = contract.get("required_reviews", [])
    if not isinstance(required_review_values, list) or not REQUIRED_REVIEWS.issubset(set(required_review_values)):
        defects.append("design_contract:required_reviews_incomplete")

    objectives = rows(data, "strategy_objectives", defects)
    value_streams = rows(data, "value_streams", defects)
    capabilities = rows(data, "capabilities", defects)
    current_units = rows(data, "current_units", defects)
    target_units = rows(data, "target_units", defects)
    roles = rows(data, "roles", defects)
    decisions = rows(data, "decisions", defects)
    interfaces = rows(data, "interfaces", defects)
    sod_rules = rows(data, "sod_rules", defects)
    allocations = rows(data, "human_ai_allocations", defects)
    options = rows(data, "design_options", defects)

    objective_map = index_unique(objectives, "id", "strategy_objectives", defects)
    stream_map = index_unique(value_streams, "id", "value_streams", defects)
    capability_map = index_unique(capabilities, "id", "capabilities", defects)
    current_unit_map = index_unique(current_units, "id", "current_units", defects)
    target_unit_map = index_unique(target_units, "id", "target_units", defects)
    role_map = index_unique(roles, "id", "roles", defects)
    index_unique(decisions, "id", "decisions", defects)
    index_unique(interfaces, "id", "interfaces", defects)
    index_unique(sod_rules, "id", "sod_rules", defects)
    index_unique(options, "id", "design_options", defects)

    for item in objectives:
        item_id = item.get("id", "?")
        require_fields(item, ["outcome", "measure", "source"], f"objective:{item_id}", defects)

    for item in value_streams:
        item_id = item.get("id", "?")
        require_fields(item, ["name", "customer_outcome", "source"], f"value_stream:{item_id}", defects)
        references_exist(item.get("objective_ids"), set(objective_map), f"value_stream:{item_id}:objective_ids", defects)

    for item in capabilities:
        item_id = item.get("id", "?")
        require_fields(item, ["name", "maturity", "criticality", "source"], f"capability:{item_id}", defects)
        references_exist(item.get("value_stream_ids"), set(stream_map), f"capability:{item_id}:value_stream_ids", defects)

    for item in current_units:
        item_id = item.get("id", "?")
        require_fields(item, ["purpose", "source"], f"current_unit:{item_id}", defects)
        references_exist(item.get("capability_ids"), set(capability_map), f"current_unit:{item_id}:capability_ids", defects)

    target_capability_owners: dict[str, list[str]] = {}
    for item in target_units:
        item_id = item.get("id", "?")
        require_fields(item, ["purpose", "outcomes", "accountabilities", "system_of_record", "source"], f"target_unit:{item_id}", defects)
        references_exist(item.get("capability_ids"), set(capability_map), f"target_unit:{item_id}:capability_ids", defects)
        for capability_id in item.get("capability_ids", []):
            target_capability_owners.setdefault(str(capability_id), []).append(str(item_id))
    for capability_id, capability in capability_map.items():
        if capability.get("criticality") == "CRITICAL":
            owners = target_capability_owners.get(capability_id, [])
            if len(owners) != 1:
                defects.append(f"capability:{capability_id}:critical_owner_count:{len(owners)}")

    accountability_owners: dict[str, list[str]] = {}
    valid_units = set(current_unit_map) | set(target_unit_map)
    for item in roles:
        item_id = item.get("id", "?")
        require_fields(item, ["unit_id", "purpose", "outcomes", "accountabilities", "skills", "capacity", "source"], f"role:{item_id}", defects)
        if item.get("unit_id") not in valid_units:
            defects.append(f"role:{item_id}:unknown_unit")
        capacity = item.get("capacity")
        if not isinstance(capacity, dict):
            defects.append(f"role:{item_id}:capacity_not_evidenced")
        else:
            require_fields(capacity, ["workload_evidence", "complexity", "manager_capacity", "standardization"], f"role:{item_id}:capacity", defects)
        for accountability in item.get("accountabilities", []) if isinstance(item.get("accountabilities"), list) else []:
            accountability_owners.setdefault(str(accountability), []).append(str(item_id))
    for accountability, owners in accountability_owners.items():
        if len(owners) > 1:
            defects.append(f"accountability:{accountability}:duplicated_owners:{','.join(owners)}")

    for item in decisions:
        item_id = item.get("id", "?")
        require_fields(item, ["decision", "decision_owner", "executors", "source"], f"decision:{item_id}", defects)
        owner = item.get("decision_owner")
        if not isinstance(owner, str):
            defects.append(f"decision:{item_id}:owner_must_be_single_role")
        elif owner not in role_map:
            defects.append(f"decision:{item_id}:owner_unknown")
        if isinstance(owner, str) and owner.upper().startswith("AI"):
            defects.append(f"decision:{item_id}:ai_cannot_own_decision")

    for item in interfaces:
        item_id = item.get("id", "?")
        require_fields(item, ["provider", "consumer", "input", "output", "service_level", "quality_rule", "escalation", "source"], f"interface:{item_id}", defects)
        for party in ("provider", "consumer"):
            if item.get(party) not in valid_units and item.get(party) not in role_map:
                defects.append(f"interface:{item_id}:unknown_{party}")

    for item in sod_rules:
        item_id = item.get("id", "?")
        require_fields(item, ["incompatible_duties", "control_owner", "source", "status"], f"sod:{item_id}", defects)
        if item.get("control_owner") not in role_map:
            defects.append(f"sod:{item_id}:unknown_control_owner")
        if item.get("status") != "PASS":
            defects.append(f"sod:{item_id}:not_pass")

    for pos, item in enumerate(allocations):
        prefix = f"human_ai_allocation:{item.get('work_id', pos)}"
        require_fields(item, ["work_id", "human_supervisor", "ai_mode", "allowed_actions", "prohibited_actions", "audit", "rollback"], prefix, defects)
        if item.get("human_supervisor") not in role_map:
            defects.append(f"{prefix}:unknown_human_supervisor")
        if item.get("ai_mode") not in AI_MODES:
            defects.append(f"{prefix}:invalid_ai_mode")
        if item.get("accountable_party") and item.get("accountable_party") not in role_map:
            defects.append(f"{prefix}:ai_or_unknown_accountable_party")

    if len(options) < 2:
        defects.append("design_options:minimum_two_required")
    for item in options:
        item_id = item.get("id", "?")
        require_fields(item, ["pattern", "rationale", "assumptions", "impacts"], f"design_option:{item_id}", defects)

    transition = data.get("transition")
    if not isinstance(transition, dict):
        defects.append("transition:missing")
    else:
        require_fields(transition, ["dependencies", "milestones", "people_impacts", "change_risks", "readiness_evidence", "rollback_points"], "transition", defects)
        for request in transition.get("change_requests", []):
            if request.get("status") not in {"DRAFT", "PENDING_HUMAN_APPROVAL"}:
                defects.append(f"change_request:{request.get('id', '?')}:unauthorized_status")

    test_rows = data.get("tests", [])
    tests = {item.get("test_type"): item for item in test_rows if isinstance(item, dict)} if isinstance(test_rows, list) else {}
    for test_type in REQUIRED_TESTS:
        if tests.get(test_type, {}).get("status") != "PASS" or not nonempty(tests.get(test_type, {}).get("evidence")):
            defects.append(f"test:{test_type}:not_pass_or_missing_evidence")

    review_rows = data.get("reviews", [])
    reviews = {item.get("review_type"): item for item in review_rows if isinstance(item, dict)} if isinstance(review_rows, list) else {}
    for review_type in REQUIRED_REVIEWS:
        row = reviews.get(review_type)
        if not row or not nonempty(row.get("reviewer")) or not nonempty(row.get("evidence")):
            defects.append(f"review:{review_type}:missing_reviewer_or_evidence")
        elif review_type in SPECIALIST_REVIEWS and row.get("status") != "PASS":
            review_gaps.append(f"review:{review_type}:not_pass")
        elif review_type == "FINAL_ORG_DECISION" and row.get("status") != "PENDING":
            defects.append("review:FINAL_ORG_DECISION:must_be_pending")

    final_decision = data.get("final_human_decision")
    if not isinstance(final_decision, dict):
        defects.append("final_human_decision:missing")
    else:
        require_fields(final_decision, ["owner", "status", "evidence"], "final_human_decision", defects)
        if final_decision.get("owner") != contract.get("final_decision_owner"):
            defects.append("final_human_decision:owner_mismatch")
        if final_decision.get("status") != "PENDING":
            defects.append("final_human_decision:must_be_pending")

    active_flags = sorted(set(data.get("forbidden_flags", [])) & FORBIDDEN_FLAGS)
    for flag in active_flags:
        defects.append(f"forbidden_flag:{flag}")
    active_states = sorted(set(data.get("published_states", [])) & FORBIDDEN_STATES)
    for state in active_states:
        defects.append(f"forbidden_state:{state}")

    sections = set(data.get("output_sections", [])) if isinstance(data.get("output_sections"), list) else set()
    missing_sections = sorted(REQUIRED_SECTIONS - sections)
    if missing_sections:
        defects.append(f"output_sections:missing:{','.join(missing_sections)}")

    defects = sorted(set(defects))
    review_gaps = sorted(set(review_gaps))
    if defects:
        state = "NOT_READY"
    elif review_gaps:
        state = "READY_FOR_ORG_REVIEW"
    else:
        state = "READY_FOR_HUMAN_ORG_DECISION"

    return {
        "skill": "organization-design",
        "state": state,
        "defect_count": len(defects),
        "defects": defects,
        "review_gap_count": len(review_gaps),
        "review_gaps": review_gaps,
        "counts": {
            "objectives": len(objectives),
            "value_streams": len(value_streams),
            "capabilities": len(capabilities),
            "current_units": len(current_units),
            "target_units": len(target_units),
            "roles": len(roles),
            "decisions": len(decisions),
            "interfaces": len(interfaces),
            "sod_rules": len(sod_rules),
            "human_ai_allocations": len(allocations),
            "design_options": len(options),
            "tests_passed": sum(1 for row in tests.values() if row.get("status") == "PASS"),
            "reviews_passed": sum(1 for row in reviews.values() if row.get("status") == "PASS"),
        },
        "warning": "STATIC PASS does not prove D10 real-case effectiveness, duration, token cost, adoption, or business impact.",
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: organization_design_engine.py <input.json>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(json.dumps({"state": "NOT_READY", "defects": [f"input_error:{exc}"]}, ensure_ascii=False, indent=2))
        return 1
    result = validate(payload)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["state"] != "NOT_READY" else 1


if __name__ == "__main__":
    raise SystemExit(main())
