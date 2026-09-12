#!/usr/bin/env python3
"""Deterministic structural gate for task-to-asset JSON."""
import json
import sys
from pathlib import Path

RIGHTS_OK = {"granted", "public"}
DECISIONS = {"candidate", "hold", "reject"}
ASSET_TYPES = {"prompt", "template", "checklist", "sop", "playbook", "case", "faq", "skill", "workflow", "agent_component"}

def filled(value):
    return value not in (None, "", [], {})

def evaluate(data):
    errors, warnings = [], []
    contract = data.get("contract", {})
    contract_fields = ["conversion_id", "task_id", "deliverable_ref", "task_status", "objective", "contributor", "rights_status", "attribution", "classification", "intended_users", "reuse_context", "target_asset_type", "owner", "reviewer", "risk_level", "standards"]
    missing_contract = [k for k in contract_fields if not filled(contract.get(k))]
    if missing_contract:
        errors.append("missing_contract:" + ",".join(missing_contract))
    if contract.get("rights_status") not in RIGHTS_OK:
        errors.append("rights_not_granted")

    sources = data.get("source_evidence", [])
    source_ids = set()
    for i, source in enumerate(sources):
        fields = ["id", "source_type", "source_ref", "date_or_version", "observed_result", "acceptance_ref", "rights_status", "classification", "limitations"]
        missing = [k for k in fields if not filled(source.get(k))]
        if missing:
            errors.append(f"source_{i}_missing:" + ",".join(missing))
        if source.get("rights_status") not in RIGHTS_OK:
            errors.append(f"source_{i}_rights_not_granted")
        sid = source.get("id")
        if filled(sid):
            if sid in source_ids:
                errors.append(f"duplicate_source:{sid}")
            source_ids.add(sid)

    worth = data.get("assetworthiness", {})
    worth_fields = ["reuse_problem", "recurrence_evidence", "expected_value_basis", "reusable_kernel", "case_specific_exclusions", "redundancy_check", "maintenance_cost", "decision", "rationale"]
    missing_worth = [k for k in worth_fields if not filled(worth.get(k))]
    if missing_worth:
        errors.append("missing_assetworthiness:" + ",".join(missing_worth))
    decision = worth.get("decision")
    if decision not in DECISIONS:
        errors.append("invalid_assetworthiness_decision")

    candidate = data.get("candidate", {})
    if decision == "candidate":
        candidate_fields = ["candidate_id", "title", "asset_type", "objective", "trigger", "anti_triggers", "inputs", "workflow", "output", "dod", "conditions", "non_applicable_when", "exceptions", "escalation", "evidence_refs", "dependencies", "attribution", "version"]
        missing_candidate = [k for k in candidate_fields if not filled(candidate.get(k))]
        if missing_candidate:
            errors.append("missing_candidate:" + ",".join(missing_candidate))
        allowed = set(contract.get("standards", {}).get("allowed_asset_types", [])) or ASSET_TYPES
        if candidate.get("asset_type") not in allowed:
            errors.append("invalid_asset_type")
        for ref in candidate.get("evidence_refs", []):
            if ref not in source_ids:
                errors.append(f"candidate_broken_ref:{ref}")

    conflict = data.get("conflict_review", {})
    if conflict.get("status") not in {"none", "resolved", "open"}:
        errors.append("invalid_conflict_status")
    if conflict.get("status") == "open":
        warnings.append("open_conflict")

    test = data.get("reuse_test", {})
    test_status = test.get("status", "not_run")
    if test_status not in {"planned", "passed", "failed", "not_run"}:
        errors.append("invalid_reuse_test_status")
    test_plan_ok = all(filled(test.get(k)) for k in ["cases", "rubric_ref", "participants", "baseline_ref", "success_threshold", "owner"])
    if test_status in {"planned", "passed", "failed"} and not test_plan_ok:
        errors.append("incomplete_reuse_test")
    if test_status in {"passed", "failed"} and not filled(test.get("result_source")):
        errors.append("missing_reuse_result_source")

    governance = data.get("governance", {})
    governance_fields = ["access_policy", "storage_destination", "version", "review_cycle", "retirement_rule", "revocation_process", "approval_status", "owner"]
    governance_ok = all(filled(governance.get(k)) for k in governance_fields)
    if decision == "candidate" and not governance_ok:
        errors.append("incomplete_governance")
    if governance.get("approval_status") not in {"draft", "approved", "rejected"}:
        errors.append("invalid_approval_status")

    if missing_contract:
        state = "NOT_READY"
    elif contract.get("task_status") != "completed" or contract.get("rights_status") not in RIGHTS_OK:
        state = "SOURCE_NOT_ELIGIBLE"
    elif decision == "reject" or governance.get("approval_status") == "rejected" or worth.get("redundancy_check") == "duplicate":
        state = "NO_ASSET"
    elif decision == "hold" or not worth.get("actual_result_verified") or not worth.get("reusable_beyond_original"):
        state = "HOLD_FOR_EVIDENCE"
    elif not sources or not candidate:
        state = "DRAFT"
    elif errors:
        state = "REVISE"
    elif contract.get("risk_level") == "high" or conflict.get("status") == "open" or data.get("guardrails") or data.get("expert_review_required"):
        state = "READY_WITH_GUARDRAILS"
    elif test_status == "passed" and governance.get("approval_status") == "approved":
        state = "APPROVED_FOR_KNOWLEDGE_BASE"
    elif test_status == "passed":
        state = "REUSE_VALIDATED"
    else:
        state = "READY_FOR_REUSE_TEST"
        if test_status == "not_run":
            warnings.append("reuse_test_not_planned")

    return {
        "state": state,
        "metrics": {"source_count": len(sources), "candidate_present": bool(candidate), "asset_type": candidate.get("asset_type"), "decision": decision, "reuse_test_status": test_status},
        "errors": sorted(set(errors)),
        "warnings": sorted(set(warnings)),
        "guardrails": data.get("guardrails", []),
        "next_action": {
            "NOT_READY": "complete_conversion_contract_and_rights",
            "SOURCE_NOT_ELIGIBLE": "complete_task_or_obtain_eligible_source",
            "DRAFT": "add_outcome_evidence_and_candidate",
            "NO_ASSET": "record_rejection_or_merge_and_stop",
            "HOLD_FOR_EVIDENCE": "collect_verified_result_or_reuse_basis",
            "REVISE": "fix_schema_refs_dedup_test_or_governance",
            "READY_WITH_GUARDRAILS": "resolve_review_conflict_or_guardrails",
            "READY_FOR_REUSE_TEST": "run_new_case_reuse_test",
            "REUSE_VALIDATED": "obtain_human_approval",
            "APPROVED_FOR_KNOWLEDGE_BASE": "publish_to_authorized_knowledge_base"
        }[state]
    }

def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: evaluate_asset_candidate.py INPUT.json")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(evaluate(data), ensure_ascii=False, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
