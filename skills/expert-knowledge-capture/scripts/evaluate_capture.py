#!/usr/bin/env python3
"""Deterministic structural gate for expert-knowledge-capture JSON."""
import json
import sys
from pathlib import Path

REQUIRED_TYPES = {"signal", "mental_model", "decision_rule", "exception", "failure_mode", "escalation"}
RIGHTS_OK = {"granted", "public"}

def filled(v):
    return v not in (None, "", [], {})

def evaluate(data):
    errors, warnings = [], []
    contract = data.get("contract", {})
    required_contract = ["capture_id", "capability_scope", "intended_users", "use_case", "expert_contributors", "rights_status", "attribution", "confidentiality_class", "target_artifacts", "owner", "reviewer", "risk_level", "standards"]
    missing_contract = [k for k in required_contract if not filled(contract.get(k))]
    if missing_contract:
        errors.append("missing_contract:" + ",".join(missing_contract))
    if contract.get("rights_status") not in RIGHTS_OK:
        errors.append("rights_not_granted")

    sources = data.get("sources", [])
    source_ids, case_ids = set(), set()
    for i, source in enumerate(sources):
        required = ["id", "case_id", "source_type", "raw_source_ref", "date_or_version", "rights_status", "classification", "evidence_scope", "limitations"]
        missing = [k for k in required if not filled(source.get(k))]
        if missing:
            errors.append(f"source_{i}_missing:" + ",".join(missing))
        if source.get("rights_status") not in RIGHTS_OK:
            errors.append(f"source_{i}_rights_not_granted")
        if filled(source.get("id")):
            if source["id"] in source_ids:
                errors.append(f"duplicate_source:{source['id']}")
            source_ids.add(source["id"])
        if filled(source.get("case_id")):
            case_ids.add(source["case_id"])

    units = data.get("knowledge_units", [])
    unit_ids, types, pending = set(), set(), 0
    for i, unit in enumerate(units):
        required = ["id", "type", "statement", "evidence_refs", "conditions", "non_applicable_when", "confidence", "expert_status", "attribution"]
        missing = [k for k in required if not filled(unit.get(k))]
        if missing:
            errors.append(f"unit_{i}_missing:" + ",".join(missing))
        uid = unit.get("id")
        if filled(uid):
            if uid in unit_ids:
                errors.append(f"duplicate_unit:{uid}")
            unit_ids.add(uid)
        types.add(unit.get("type"))
        for ref in unit.get("evidence_refs", []):
            if ref not in source_ids:
                errors.append(f"unit_{i}_broken_ref:{ref}")
        if unit.get("expert_status") != "validated":
            pending += 1

    standards = contract.get("standards", {})
    required_types = set(standards.get("required_knowledge_types", [])) or REQUIRED_TYPES
    missing_types = sorted(required_types - types)
    if missing_types:
        errors.append("missing_types:" + ",".join(missing_types))

    conflict = data.get("conflict_review", {})
    if conflict.get("status") not in {"none", "resolved", "open"}:
        errors.append("invalid_conflict_status")
    if conflict.get("status") == "open":
        warnings.append("open_conflict")

    validation = data.get("expert_validation", {})
    validation_ok = all(validation.get(k) is True for k in ["scope_confirmed", "accuracy_confirmed", "exceptions_confirmed", "rights_confirmed"])
    validation_ok = validation_ok and all(filled(validation.get(k)) for k in ["allowed_audiences", "expert_or_delegate", "date_or_version"])

    transfer = data.get("transfer_test", {})
    transfer_status = transfer.get("status", "not_run")
    if transfer_status not in {"planned", "passed", "failed", "not_run"}:
        errors.append("invalid_transfer_status")
    transfer_plan_ok = all(filled(transfer.get(k)) for k in ["scenarios", "rubric_ref", "participants", "success_threshold", "owner"])
    if transfer_status in {"planned", "passed", "failed"} and not transfer_plan_ok:
        errors.append("incomplete_transfer_plan")
    if transfer_status in {"passed", "failed"} and not filled(transfer.get("result_source")):
        errors.append("missing_transfer_result_source")

    packaging = data.get("packaging", {})
    packaging_ok = all(filled(packaging.get(k)) for k in ["assets", "access_policy", "version", "review_cycle", "revocation_process", "owner"])
    if sources and units and not packaging_ok:
        errors.append("incomplete_packaging")

    min_cases = standards.get("min_cases", 2)
    if missing_contract:
        state = "NOT_READY"
    elif not sources or not units:
        state = "DRAFT"
    elif errors:
        state = "REVISE"
    elif len(case_ids) < min_cases:
        state = "HYPOTHESIS_ONLY"
    elif pending or not validation_ok:
        state = "READY_FOR_EXPERT_REVIEW"
    elif contract.get("risk_level") == "high" or conflict.get("status") == "open" or data.get("guardrails") or data.get("expert_review_required"):
        state = "READY_WITH_GUARDRAILS"
    elif transfer_status == "passed":
        state = "TRANSFER_VALIDATED"
    elif transfer_status == "planned":
        state = "READY_FOR_TRANSFER_TEST"
    else:
        state = "READY_FOR_TRANSFER_TEST"
        warnings.append("transfer_test_not_planned")

    return {
        "state": state,
        "metrics": {"source_count": len(sources), "case_count": len(case_ids), "unit_count": len(units), "type_coverage": sorted(types - {None}), "pending_units": pending},
        "errors": sorted(set(errors)),
        "warnings": sorted(set(warnings)),
        "guardrails": data.get("guardrails", []),
        "next_action": {
            "NOT_READY": "complete_capture_contract_and_rights",
            "DRAFT": "capture_real_cases_and_extract_units",
            "REVISE": "fix_schema_evidence_or_packaging",
            "HYPOTHESIS_ONLY": "add_distinct_cases",
            "READY_FOR_EXPERT_REVIEW": "obtain_expert_validation",
            "READY_WITH_GUARDRAILS": "resolve_conflict_or_required_review",
            "READY_FOR_TRANSFER_TEST": "run_novel_case_transfer_test",
            "TRANSFER_VALIDATED": "handoff_to_task_to_asset"
        }[state]
    }

def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: evaluate_capture.py INPUT.json")
    path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8"))
    print(json.dumps(evaluate(data), ensure_ascii=False, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
