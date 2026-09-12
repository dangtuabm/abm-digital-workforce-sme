#!/usr/bin/env python3
"""Static self-test for enterprise ai-change-leadership."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


MIN_COUNTS = {
    "evidence_sources": 10,
    "stakeholders": 10,
    "impact_records": 8,
    "readiness_dimensions": 8,
    "wave_records": 6,
    "champion_controls": 6,
    "communication_records": 8,
    "learning_records": 8,
    "support_controls": 8,
    "adoption_metrics": 8,
    "resistance_cases": 6,
    "benefit_metrics": 6,
    "decisions": 6,
    "risks": 6,
}

TOP_REQUIRED = {
    "change_contract": [
        "change_id", "outcome", "value_hypothesis", "scope", "non_goals",
        "impacted_work", "impacted_population", "sponsor", "coalition", "owner",
        "approver", "decision_rights", "success_criteria", "stop_criteria", "dod",
        "constraints", "evidence_cutoff", "confidentiality", "action_boundary",
    ],
    "impact_method": [
        "current_future_rule", "human_ai_disposition", "impact_dimensions",
        "severity_method", "hidden_impact_check", "affected_group_rule",
        "job_role_policy_review", "owner", "input_hash",
    ],
    "readiness_method": [
        "dimensions", "rubric", "evidence_rule", "confidence_rule", "unknown_rule",
        "critical_gate_rule", "capacity_rule", "dependency_rule", "approved_by",
    ],
    "authority_map": [
        "executive_business", "people_hr_legal", "data_security_privacy",
        "technical_operations", "employee_learner_rep", "governance_authority",
        "wave_activation", "role_policy_incentive_change", "communication_send",
        "discipline_decision", "external_action_boundary",
    ],
    "lifecycle_contract": [
        "pilot", "wave_review", "incident_rollback", "feedback_backlog",
        "benefit_review", "ownership_transfer", "recertification", "onboarding",
        "offboarding", "sunset", "retention", "owner",
    ],
}

ITEM_REQUIRED = {
    "evidence_sources": ["id", "source", "as_of", "rights", "hash"],
    "stakeholders": [
        "id", "segment", "population", "role_work", "impact", "influence",
        "readiness", "need_barrier", "trust", "channel", "representative", "owner", "evidence_ref",
    ],
    "impact_records": [
        "id", "role_work_task", "current_state", "future_state", "disposition",
        "impact_type", "severity", "timing", "skill_workload_authority_support",
        "affected_population", "owner", "evidence_ref",
    ],
    "readiness_dimensions": [
        "id", "dimension", "baseline", "rubric", "source_ref", "confidence",
        "critical_gate", "gap", "dependency", "owner",
    ],
    "wave_records": [
        "id", "cohort_use_case", "value_risk", "dependencies", "entry",
        "exit_acceptance", "kill", "rollback", "resources_support_load",
        "benefit_hypothesis", "owner", "authority_state", "evidence_refs",
    ],
    "champion_controls": [
        "id", "role", "representation", "mandate", "capacity", "support",
        "conflict_rule", "non_retaliation", "owner", "evidence_ref",
    ],
    "communication_records": [
        "id", "audience", "message", "trusted_sender", "channel", "cadence",
        "accessibility", "feedback_route", "approval_state", "owner", "evidence_ref",
    ],
    "learning_records": [
        "id", "role_task_risk", "competency", "practice", "artifact",
        "assessment_acceptance", "job_aid_coaching", "transfer_evidence",
        "owner", "evidence_ref",
    ],
    "support_controls": [
        "id", "need_trigger", "service", "access_channel", "sla_basis",
        "escalation", "fallback", "capacity", "owner", "evidence_ref",
    ],
    "adoption_metrics": [
        "id", "stage", "definition_formula", "denominator", "cohort_window",
        "baseline_ref", "source_ref", "threshold_direction", "quality_guardrail",
        "privacy_fairness_slices", "trigger_action", "owner",
    ],
    "resistance_cases": [
        "id", "concern_verbatim", "source_segment", "impact", "hypotheses",
        "validation", "response_support", "grievance_route", "owner", "closure_state",
    ],
    "benefit_metrics": [
        "id", "outcome", "formula_denominator", "cohort_window", "baseline_ref",
        "total_cost", "attribution_confounders", "support_burden", "sensitivity",
        "owner", "evidence_ref",
    ],
    "decisions": [
        "id", "claim", "status", "evidence_refs", "confidence", "residual_risk",
        "remediation_owner", "authority_state",
    ],
    "risks": [
        "id", "category", "statement", "likelihood", "impact", "mitigation",
        "owner", "evidence_refs",
    ],
}

EXPECTED_TESTS = {
    "contract_future_work",
    "stakeholder_impact",
    "readiness_capacity",
    "sponsor_wave_gates",
    "communication_learning_support",
    "resistance_fairness_grievance",
    "adoption_benefits",
    "sustainment_lifecycle",
}

EXPECTED_REVIEWS = {
    "EXECUTIVE_BUSINESS",
    "PEOPLE_HR_LEGAL",
    "DATA_SECURITY_PRIVACY",
    "TECHNICAL_OPERATIONS",
    "EMPLOYEE_LEARNER_REP",
    "GOVERNANCE_AUTHORITY",
}

EXPECTED_RISKS = {
    "SPONSOR_AUTHORITY_GAP",
    "HIDDEN_ROLE_WORKLOAD_IMPACT",
    "READINESS_GATE_WASHING",
    "COERCION_SURVEILLANCE_RETALIATION",
    "TRAINING_USAGE_VALUE_CONFUSION",
    "SUPPORT_BENEFIT_SUSTAINMENT_DRIFT",
}

FORBIDDEN_TRUE = {
    "consensus_invented",
    "adoption_value_invented",
    "silence_as_consent",
    "login_as_adoption",
    "usage_as_value",
    "resistance_labeled_personality",
    "critical_gate_averaged_away",
    "fixed_three_wave_rule",
    "fixed_85_percent_gate",
    "fixed_three_kill_rule",
    "fixed_timeline_rule",
    "fixed_notion_tracker_rule",
    "job_impact_concealed",
    "hidden_individual_monitoring",
    "forced_use_quota",
    "dark_pattern_used",
    "harmful_leaderboard_used",
    "employee_profiled_without_authority",
    "retaliation_or_discrimination",
    "training_attendance_as_competence",
    "self_report_only_as_evidence",
    "feedback_deleted_or_sentiment_altered",
    "consent_faked",
    "role_changed",
    "pay_kpi_policy_changed",
    "access_changed",
    "communication_sent",
    "survey_sent",
    "people_enrolled",
    "system_launched",
    "system_stopped",
    "discipline_decided",
    "employee_terminated",
    "contract_signed",
    "purchase_approved",
    "result_published",
    "source_instruction_executed",
}

SECRET_KEYS = {
    "api_key", "secret", "password", "access_token", "refresh_token",
    "private_key", "authorization", "cookie", "employee_identity",
}


def present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict, tuple, set)):
        return bool(value)
    return True


def find_secret_material(value: Any, path: str = "") -> list[str]:
    hits: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            child_path = f"{path}.{key}" if path else str(key)
            if str(key).lower() in SECRET_KEYS and present(child):
                hits.append(child_path)
            hits.extend(find_secret_material(child, child_path))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            hits.extend(find_secret_material(child, f"{path}[{index}]"))
    return hits


def evaluate(data: dict[str, Any]) -> dict[str, Any]:
    defects: list[str] = []
    review_gaps: list[str] = []
    counts: dict[str, int] = {}

    if not present(data.get("artifact_name")):
        defects.append("artifact_name")
    for object_name, fields in TOP_REQUIRED.items():
        obj = data.get(object_name)
        if not isinstance(obj, dict):
            defects.append(object_name)
            continue
        for field in fields:
            if not present(obj.get(field)):
                defects.append(f"{object_name}.{field}")

    all_ids: set[str] = set()
    for list_name, minimum in MIN_COUNTS.items():
        items = data.get(list_name)
        if not isinstance(items, list):
            items = []
            defects.append(f"{list_name}:not_list")
        counts[list_name] = len(items)
        if len(items) < minimum:
            defects.append(f"{list_name}:count<{minimum}")
        for index, item in enumerate(items):
            if not isinstance(item, dict):
                defects.append(f"{list_name}[{index}]:not_object")
                continue
            for field in ITEM_REQUIRED[list_name]:
                if not present(item.get(field)):
                    defects.append(f"{list_name}[{index}].{field}")
            item_id = item.get("id")
            if present(item_id):
                item_id = str(item_id)
                if item_id in all_ids:
                    defects.append(f"duplicate_id:{item_id}")
                all_ids.add(item_id)

    evidence_ids = {
        str(item.get("id")) for item in data.get("evidence_sources", [])
        if isinstance(item, dict) and present(item.get("id"))
    }
    for list_name in (
        "stakeholders", "impact_records", "champion_controls", "communication_records",
        "learning_records", "support_controls", "benefit_metrics",
    ):
        for index, item in enumerate(data.get(list_name, [])):
            if isinstance(item, dict) and str(item.get("evidence_ref")) not in evidence_ids:
                defects.append(f"{list_name}[{index}].evidence_ref:unknown")
    for list_name in ("readiness_dimensions", "adoption_metrics"):
        ref_field = "source_ref"
        for index, item in enumerate(data.get(list_name, [])):
            if isinstance(item, dict) and str(item.get(ref_field)) not in evidence_ids:
                defects.append(f"{list_name}[{index}].{ref_field}:unknown")
    for list_name in ("wave_records", "decisions", "risks"):
        for index, item in enumerate(data.get(list_name, [])):
            if not isinstance(item, dict):
                continue
            refs = item.get("evidence_refs", [])
            if not isinstance(refs, list) or any(str(ref) not in evidence_ids for ref in refs):
                defects.append(f"{list_name}[{index}].evidence_refs:unknown")

    risk_categories = {
        str(item.get("category")) for item in data.get("risks", [])
        if isinstance(item, dict) and present(item.get("category"))
    }
    for category in EXPECTED_RISKS - risk_categories:
        defects.append(f"missing_risk:{category}")

    tests = data.get("tests", {}) if isinstance(data.get("tests"), dict) else {}
    counts["tests_passed"] = sum(tests.get(name) == "PASS" for name in EXPECTED_TESTS)
    for name in EXPECTED_TESTS:
        if tests.get(name) != "PASS":
            defects.append(f"test_not_passed:{name}")

    reviews = data.get("reviews", {}) if isinstance(data.get("reviews"), dict) else {}
    counts["reviews_passed"] = sum(reviews.get(name) == "PASS" for name in EXPECTED_REVIEWS)
    for name in EXPECTED_REVIEWS:
        if reviews.get(name) != "PASS":
            review_gaps.append(name)

    if data.get("activation_state") != "PENDING_HUMAN_DECISION":
        defects.append("activation_state")
    if data.get("change_state") not in {"READY_FOR_HUMAN_CHANGE_DECISION", "NOT_READY"}:
        defects.append("change_state")

    forbidden = data.get("forbidden_actions")
    if not isinstance(forbidden, dict):
        forbidden = {}
        defects.append("forbidden_actions")
    for key in FORBIDDEN_TRUE:
        if forbidden.get(key) is True:
            defects.append(f"forbidden_true:{key}")
    for path in find_secret_material(data):
        defects.append(f"secret_material:{path}")

    ready = not defects and not review_gaps
    return {
        "state": "READY_FOR_HUMAN_CHANGE_DECISION" if ready else "NOT_READY",
        "defect_count": len(defects),
        "review_gap_count": len(review_gaps),
        "counts": counts,
        "defects": defects,
        "review_gaps": review_gaps,
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: evaluate_ai_change_leadership.py <fixture.json>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        print(json.dumps({"state": "NOT_READY", "error": str(exc)}, ensure_ascii=False, indent=2))
        return 2
    if not isinstance(data, dict):
        print(json.dumps({"state": "NOT_READY", "error": "root_not_object"}, indent=2))
        return 2
    result = evaluate(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["state"] == "READY_FOR_HUMAN_CHANGE_DECISION" else 1


if __name__ == "__main__":
    raise SystemExit(main())
