#!/usr/bin/env python3
"""Deterministic structural gate for second-brain knowledge-base JSON."""
import json
import sys
from pathlib import Path

RIGHTS_OK = {"granted", "public"}
SOURCE_STATUS = {"active", "draft", "superseded", "revoked", "quarantined"}
REQUIRED_TEST_TYPES = {"known_answer", "multi_source", "no_answer", "conflict", "unauthorized", "stale_revoked"}

def filled(value):
    return value not in (None, "", [], {})

def evaluate(data):
    errors, warnings = [], []
    contract = data.get("contract", {})
    contract_fields = ["brain_id", "objective", "use_cases", "intended_users", "decision_impact", "scope", "exclusions", "owner", "reviewer", "risk_level", "platform_constraints", "standards"]
    missing_contract = [k for k in contract_fields if not filled(contract.get(k))]
    if missing_contract:
        errors.append("missing_contract:" + ",".join(missing_contract))

    sources = data.get("sources", [])
    source_ids, active_ids = set(), set()
    source_by_id = {}
    for i, source in enumerate(sources):
        fields = ["id", "title", "source_ref", "source_type", "domain", "authority_tier", "owner", "version", "effective_date", "status", "rights_status", "classification", "allowed_roles", "hash", "limitations"]
        missing = [k for k in fields if not filled(source.get(k))]
        if missing:
            errors.append(f"source_{i}_missing:" + ",".join(missing))
        if source.get("rights_status") not in RIGHTS_OK:
            errors.append(f"source_{i}_rights_not_granted")
        if source.get("status") not in SOURCE_STATUS:
            errors.append(f"source_{i}_invalid_status")
        sid = source.get("id")
        if filled(sid):
            if sid in source_ids:
                errors.append(f"duplicate_source:{sid}")
            source_ids.add(sid)
            source_by_id[sid] = source
            if source.get("status") == "active":
                active_ids.add(sid)

    canonical = data.get("canonical_map", [])
    topic_ids, open_conflicts = set(), 0
    for i, entry in enumerate(canonical):
        fields = ["topic_id", "topic", "canonical_source_id", "authority_rule", "decision_status", "owner"]
        missing = [k for k in fields if not filled(entry.get(k))]
        if missing:
            errors.append(f"canonical_{i}_missing:" + ",".join(missing))
        tid = entry.get("topic_id")
        if filled(tid):
            if tid in topic_ids:
                errors.append(f"duplicate_topic:{tid}")
            topic_ids.add(tid)
        canonical_id = entry.get("canonical_source_id")
        if canonical_id not in source_ids:
            errors.append(f"canonical_{i}_broken_ref:{canonical_id}")
        elif source_by_id[canonical_id].get("status") != "active":
            errors.append(f"canonical_{i}_not_active:{canonical_id}")
        for ref in entry.get("competing_source_ids", []):
            if ref not in source_ids:
                errors.append(f"canonical_{i}_broken_competing_ref:{ref}")
        if entry.get("decision_status") not in {"confirmed", "open", "quarantined"}:
            errors.append(f"canonical_{i}_invalid_decision")
        if entry.get("decision_status") in {"open", "quarantined"}:
            open_conflicts += 1

    normalization = data.get("normalization", {})
    derivatives = normalization.get("derivatives", [])
    derivative_source_ids = set()
    for i, item in enumerate(derivatives):
        fields = ["source_id", "derivative_ref", "chunk_ids", "citation_locator", "parse_status", "limitations"]
        missing = [k for k in fields if not filled(item.get(k))]
        if missing:
            errors.append(f"derivative_{i}_missing:" + ",".join(missing))
        sid = item.get("source_id")
        if sid not in source_ids:
            errors.append(f"derivative_{i}_broken_ref:{sid}")
        else:
            derivative_source_ids.add(sid)
    uncovered_active = sorted(active_ids - derivative_source_ids)

    taxonomy = data.get("taxonomy", {})
    taxonomy_ok = all(filled(taxonomy.get(k)) for k in ["fields", "entities", "synonyms", "relationships", "version", "owner"])
    if sources and not taxonomy_ok:
        errors.append("incomplete_taxonomy")

    access = data.get("access_control", {})
    access_ok = all(filled(access.get(k)) for k in ["enforcement_layer", "roles", "classification_rules", "unauthorized_test_cases", "audit_log_ref", "owner"])
    if access.get("enforcement_layer") not in {"storage", "both"}:
        errors.append("access_not_enforced_at_storage")
    if sources and not access_ok:
        errors.append("incomplete_access_control")

    tests = data.get("retrieval_tests", [])
    test_types, all_passed = set(), bool(tests)
    for i, case in enumerate(tests):
        fields = ["id", "type", "query", "expected_behavior", "rubric_ref", "success_threshold", "owner", "status"]
        missing = [k for k in fields if not filled(case.get(k))]
        if missing:
            errors.append(f"test_{i}_missing:" + ",".join(missing))
        ctype = case.get("type")
        test_types.add(ctype)
        for ref in case.get("expected_source_ids", []):
            if ref not in source_ids:
                errors.append(f"test_{i}_broken_ref:{ref}")
        status = case.get("status")
        if status not in {"planned", "passed", "failed", "not_run"}:
            errors.append(f"test_{i}_invalid_status")
        if status in {"passed", "failed"} and not filled(case.get("result_source")):
            errors.append(f"test_{i}_missing_result_source")
        if status != "passed":
            all_passed = False
    required_types = set(contract.get("standards", {}).get("required_test_types", [])) or REQUIRED_TEST_TYPES
    missing_test_types = sorted(required_types - test_types)
    if missing_test_types:
        errors.append("missing_test_types:" + ",".join(missing_test_types))

    operations = data.get("operations", {})
    operation_fields = ["ingestion_log_ref", "freshness_policy", "review_cycle", "change_impact_process", "supersede_archive_revoke", "unanswerable_backlog", "audit_process", "approval_status", "version", "owner"]
    operations_ok = all(filled(operations.get(k)) for k in operation_fields)
    if sources and not operations_ok:
        errors.append("incomplete_operations")
    if operations.get("approval_status") not in {"draft", "approved", "rejected"}:
        errors.append("invalid_approval_status")

    if missing_contract:
        state = "NOT_READY"
    elif any(s.get("rights_status") not in RIGHTS_OK for s in sources):
        state = "SOURCE_NOT_ELIGIBLE"
    elif not sources or not canonical:
        state = "DRAFT"
    elif not normalization.get("raw_preserved") or uncovered_active:
        state = "READY_FOR_NORMALIZATION"
    elif errors:
        state = "REVISE"
    elif open_conflicts:
        state = "QUARANTINE_CONFLICT"
    elif contract.get("risk_level") == "high" or data.get("guardrails") or data.get("expert_review_required"):
        state = "READY_WITH_GUARDRAILS"
    elif all_passed and operations.get("approval_status") == "approved":
        state = "APPROVED_FOR_USE"
    elif all_passed:
        state = "KNOWLEDGE_BASE_VALIDATED"
    else:
        state = "READY_FOR_RETRIEVAL_TEST"

    return {
        "state": state,
        "metrics": {"source_count": len(sources), "active_source_count": len(active_ids), "topic_count": len(canonical), "derivative_count": len(derivatives), "test_type_coverage": sorted(test_types), "open_conflicts": open_conflicts},
        "errors": sorted(set(errors)),
        "warnings": sorted(set(warnings)),
        "guardrails": data.get("guardrails", []),
        "next_action": {
            "NOT_READY": "complete_contract_authority_access_and_tests",
            "SOURCE_NOT_ELIGIBLE": "remove_or_authorize_ineligible_sources",
            "DRAFT": "build_source_inventory_and_canonical_map",
            "READY_FOR_NORMALIZATION": "normalize_active_sources_with_trace",
            "REVISE": "fix_refs_metadata_access_tests_or_operations",
            "QUARANTINE_CONFLICT": "resolve_or_keep_conflicting_topics_quarantined",
            "READY_WITH_GUARDRAILS": "complete_required_security_or_domain_review",
            "READY_FOR_RETRIEVAL_TEST": "run_required_retrieval_tests",
            "KNOWLEDGE_BASE_VALIDATED": "obtain_human_approval",
            "APPROVED_FOR_USE": "handoff_to_authorized_answering_layer"
        }[state]
    }

def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: evaluate_knowledge_base.py INPUT.json")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(evaluate(data), ensure_ascii=False, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
