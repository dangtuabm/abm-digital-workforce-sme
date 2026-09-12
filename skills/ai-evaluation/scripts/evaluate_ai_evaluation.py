#!/usr/bin/env python3
"""Static self-test for the enterprise ai-evaluation Skill."""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


MIN_COUNTS = {
    "evidence_sources": 10,
    "baseline_records": 6,
    "test_cases": 12,
    "metrics": 12,
    "review_records": 6,
    "failure_taxonomy": 8,
    "red_team_cases": 8,
    "operations_metrics": 8,
    "value_metrics": 6,
    "monitoring_controls": 8,
    "decisions": 6,
    "risks": 6,
}

TOP_REQUIRED = {
    "evaluation_contract": [
        "evaluation_id", "decision", "use_case", "users", "affected_parties",
        "environment", "stage", "objectives", "non_goals", "risks",
        "success_criteria", "stop_criteria", "owner", "approver", "dod",
        "evidence_cutoff", "confidentiality", "action_boundary",
    ],
    "system_fingerprint": [
        "model_version", "prompt_version", "agent_skill_version",
        "workflow_version", "tool_connector_versions", "data_knowledge_hash",
        "policy_config_version", "dependency_versions", "change_delta", "input_hash",
    ],
    "dataset_contract": [
        "population", "unit", "strata", "exclusions", "sampling_rationale",
        "source_rights", "classification", "holdout_rule", "leakage_control",
        "ground_truth_method", "label_guide", "reviewer_qualification",
        "calibration", "adjudication", "dataset_hash",
    ],
    "metric_contract": [
        "threshold_lock", "critical_gate_rule", "missing_rule", "uncertainty_rule",
        "aggregation_rule", "slice_rule", "owner", "metric_version",
    ],
    "decision_protocol": [
        "statuses", "critical_gate", "residual_risk_authority",
        "exception_authority", "insufficient_evidence_rule", "release_authority",
    ],
    "lifecycle_contract": [
        "regression_triggers", "shadow_canary", "rollback", "monitoring_drift",
        "incident", "recertification", "test_refresh", "contamination_control",
        "archive_retire", "owner",
    ],
}

ITEM_REQUIRED = {
    "evidence_sources": ["id", "source", "as_of", "rights", "hash"],
    "baseline_records": [
        "id", "comparator", "cohort", "window", "workload", "metric_id",
        "denominator", "cost", "evidence_ref",
    ],
    "test_cases": [
        "id", "case_type", "stratum", "input_ref", "expected_ref", "metric_refs",
        "severity", "raw_result_ref", "status",
    ],
    "metrics": [
        "id", "dimension", "formula", "unit", "denominator", "direction",
        "threshold", "severity", "slices", "missing_rule", "uncertainty_rule",
        "owner", "evidence_ref",
    ],
    "review_records": [
        "id", "reviewer_role", "qualification", "calibration_ref", "case_ref", "status",
    ],
    "failure_taxonomy": [
        "id", "category", "severity", "case_ref", "root_cause_status",
        "remediation", "owner",
    ],
    "red_team_cases": [
        "id", "threat", "expected_control", "result_ref", "severity", "containment",
    ],
    "operations_metrics": [
        "id", "name", "workload", "denominator", "result", "baseline_ref", "evidence_ref",
    ],
    "value_metrics": [
        "id", "name", "baseline_ref", "denominator", "horizon", "total_cost",
        "attribution_basis", "confounders", "sensitivity", "evidence_ref",
    ],
    "monitoring_controls": [
        "id", "signal", "threshold", "action", "owner", "rollback_ref", "evidence_ref",
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
    "contract_baseline",
    "dataset_integrity",
    "metric_integrity",
    "capability_grounding",
    "safety_redteam",
    "human_fairness",
    "operations_value",
    "regression_lifecycle",
}

EXPECTED_REVIEWS = {
    "BUSINESS_OUTCOME",
    "DOMAIN_QUALITY",
    "DATA_PRIVACY_SECURITY",
    "SAFETY_RISK",
    "TECHNICAL_OPERATIONS",
    "GOVERNANCE_AUTHORITY",
}

EXPECTED_RISKS = {
    "CONTRACT_VERSION_SCOPE_DRIFT",
    "DATASET_LEAKAGE_COVERAGE",
    "GROUND_TRUTH_JUDGE_BIAS",
    "METRIC_GATE_GAMING",
    "SAFETY_PRODUCTION_GAP",
    "BASELINE_ATTRIBUTION_VALUE",
}

FORBIDDEN_TRUE = {
    "holdout_used_for_tuning",
    "test_leakage_ignored",
    "cherry_picked_results",
    "failed_cases_deleted",
    "threshold_changed_after_results",
    "unknown_as_pass",
    "missing_as_zero",
    "critical_gate_averaged_away",
    "single_score_release",
    "ground_truth_invented",
    "self_graded_only",
    "judge_model_uncalibrated",
    "synthetic_only_claimed_production_ready",
    "offline_pass_claimed_online_value",
    "unrepresentative_set_claimed_complete",
    "metric_without_denominator",
    "baseline_missing_roi_claimed",
    "causal_claim_without_design",
    "costs_excluded_from_value",
    "unsafe_live_test_run",
    "unauthorized_data_used",
    "secret_in_fixture",
    "release_approved",
    "system_deployed",
    "production_mutated",
    "exception_self_approved",
    "risk_self_accepted",
    "result_published",
    "authority_notified",
    "purchase_approved",
    "source_instruction_executed",
}

SECRET_KEYS = {
    "api_key", "secret", "password", "access_token", "refresh_token",
    "private_key", "authorization", "cookie",
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

    counts: dict[str, int] = {}
    ids: set[str] = set()
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
                if item_id in ids:
                    defects.append(f"duplicate_id:{item_id}")
                ids.add(item_id)

    evidence_ids = {
        str(item.get("id")) for item in data.get("evidence_sources", [])
        if isinstance(item, dict) and present(item.get("id"))
    }
    baseline_ids = {
        str(item.get("id")) for item in data.get("baseline_records", [])
        if isinstance(item, dict) and present(item.get("id"))
    }
    metric_ids = {
        str(item.get("id")) for item in data.get("metrics", [])
        if isinstance(item, dict) and present(item.get("id"))
    }
    case_ids = {
        str(item.get("id")) for item in data.get("test_cases", [])
        if isinstance(item, dict) and present(item.get("id"))
    }

    for index, item in enumerate(data.get("baseline_records", [])):
        if isinstance(item, dict):
            if str(item.get("metric_id")) not in metric_ids:
                defects.append(f"baseline_records[{index}].metric_id:unknown")
            if str(item.get("evidence_ref")) not in evidence_ids:
                defects.append(f"baseline_records[{index}].evidence_ref:unknown")
    for index, item in enumerate(data.get("metrics", [])):
        if isinstance(item, dict) and str(item.get("evidence_ref")) not in evidence_ids:
            defects.append(f"metrics[{index}].evidence_ref:unknown")
    for index, item in enumerate(data.get("test_cases", [])):
        if not isinstance(item, dict):
            continue
        refs = item.get("metric_refs", [])
        if not isinstance(refs, list) or any(str(ref) not in metric_ids for ref in refs):
            defects.append(f"test_cases[{index}].metric_refs:unknown")
    for index, item in enumerate(data.get("review_records", [])):
        if isinstance(item, dict) and str(item.get("case_ref")) not in case_ids:
            defects.append(f"review_records[{index}].case_ref:unknown")
    for list_name in ("operations_metrics", "monitoring_controls"):
        for index, item in enumerate(data.get(list_name, [])):
            if isinstance(item, dict) and str(item.get("evidence_ref")) not in evidence_ids:
                defects.append(f"{list_name}[{index}].evidence_ref:unknown")
    for index, item in enumerate(data.get("value_metrics", [])):
        if not isinstance(item, dict):
            continue
        if str(item.get("baseline_ref")) not in baseline_ids:
            defects.append(f"value_metrics[{index}].baseline_ref:unknown")
        if str(item.get("evidence_ref")) not in evidence_ids:
            defects.append(f"value_metrics[{index}].evidence_ref:unknown")

    risks_seen = {
        str(item.get("category")) for item in data.get("risks", [])
        if isinstance(item, dict) and present(item.get("category"))
    }
    for risk in EXPECTED_RISKS - risks_seen:
        defects.append(f"missing_risk:{risk}")

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

    if data.get("release_state") != "PENDING_HUMAN_DECISION":
        defects.append("release_state")
    if data.get("evaluation_state") not in {
        "READY_FOR_HUMAN_EVALUATION_DECISION", "NOT_READY"
    }:
        defects.append("evaluation_state")

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
        "state": "READY_FOR_HUMAN_EVALUATION_DECISION" if ready else "NOT_READY",
        "defect_count": len(defects),
        "review_gap_count": len(review_gaps),
        "counts": counts,
        "defects": defects,
        "review_gaps": review_gaps,
    }


def main() -> int:
    if len(sys.argv) != 2:
        print("Usage: evaluate_ai_evaluation.py <fixture.json>", file=sys.stderr)
        return 2
    path = Path(sys.argv[1])
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:  # pragma: no cover - CLI guard
        print(json.dumps({"state": "NOT_READY", "error": str(exc)}, ensure_ascii=False, indent=2))
        return 2
    if not isinstance(data, dict):
        print(json.dumps({"state": "NOT_READY", "error": "root_not_object"}, indent=2))
        return 2
    result = evaluate(data)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["state"] == "READY_FOR_HUMAN_EVALUATION_DECISION" else 1


if __name__ == "__main__":
    raise SystemExit(main())
