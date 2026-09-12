#!/usr/bin/env python3
"""Deterministic structural gate for grounded-answer JSON."""
import json
import sys
from pathlib import Path

DECISIONS = {"ANSWER", "PARTIAL", "ABSTAIN", "ESCALATE", "DENY"}
REQUIRED_TESTS = {"known_answer", "multi_source", "no_answer", "conflict", "unauthorized", "stale_revoked", "source_injection"}

def filled(value):
    return value not in (None, "", [], {})

def evaluate(data):
    errors, warnings = [], []
    contract = data.get("contract", {})
    contract_fields = ["assistant_id", "use_case", "channel", "intended_users", "allowed_question_types", "out_of_scope", "approved_kb_id", "kb_version", "owner", "reviewer", "risk_level", "standards"]
    missing_contract = [k for k in contract_fields if not filled(contract.get(k))]
    if missing_contract:
        errors.append("missing_contract:" + ",".join(missing_contract))

    request = data.get("request", {})
    request_fields = ["request_id", "query", "requester_role", "tenant_or_scope", "classification", "language", "intent", "decision_impact", "authorization_status"]
    missing_request = [k for k in request_fields if not filled(request.get(k))]
    if missing_request:
        errors.append("missing_request:" + ",".join(missing_request))
    auth = request.get("authorization_status")
    if auth not in {"authorized", "unauthorized", "unknown"}:
        errors.append("invalid_authorization_status")

    retrieval = data.get("retrieval", {})
    if retrieval.get("kb_id") != contract.get("approved_kb_id"):
        errors.append("kb_id_mismatch")
    if retrieval.get("kb_version") != contract.get("kb_version"):
        errors.append("kb_version_mismatch")
    if retrieval.get("access_enforcement") not in {"storage", "both"}:
        errors.append("access_not_enforced_at_storage")
    if retrieval.get("retrieval_status") not in {"not_run", "completed", "failed"}:
        errors.append("invalid_retrieval_status")

    evidence = retrieval.get("evidence", [])
    evidence_ids, inactive_ids = set(), set()
    role = request.get("requester_role")
    for i, item in enumerate(evidence):
        fields = ["id", "source_id", "chunk_id", "title", "locator", "version", "effective_date", "status", "authority_tier", "classification", "allowed_roles", "support_scope", "limitations"]
        missing = [k for k in fields if not filled(item.get(k))]
        if missing:
            errors.append(f"evidence_{i}_missing:" + ",".join(missing))
        eid = item.get("id")
        if filled(eid):
            if eid in evidence_ids:
                errors.append(f"duplicate_evidence:{eid}")
            evidence_ids.add(eid)
        if item.get("status") != "active":
            inactive_ids.add(eid)
        if role not in item.get("allowed_roles", []):
            errors.append(f"evidence_{i}_role_mismatch")

    answerability = data.get("answerability", {})
    decision = answerability.get("decision")
    if decision not in DECISIONS:
        errors.append("invalid_answerability_decision")
    if answerability.get("conflict_status") not in {"none", "open", "resolved"}:
        errors.append("invalid_conflict_status")
    if answerability.get("freshness_status") not in {"current", "stale", "unknown"}:
        errors.append("invalid_freshness_status")
    if not filled(answerability.get("reason")):
        errors.append("missing_answerability_reason")

    response = data.get("response", {})
    claims = response.get("claims", [])
    referenced_ids = set()
    for i, claim in enumerate(claims):
        fields = ["id", "text", "label", "evidence_refs", "citation"]
        missing = [k for k in fields if not filled(claim.get(k))]
        if missing:
            errors.append(f"claim_{i}_missing:" + ",".join(missing))
        if claim.get("label") not in {"fact", "inference", "assumption"}:
            errors.append(f"claim_{i}_invalid_label")
        for ref in claim.get("evidence_refs", []):
            referenced_ids.add(ref)
            if ref not in evidence_ids:
                errors.append(f"claim_{i}_broken_ref:{ref}")
            if ref in inactive_ids:
                errors.append(f"claim_{i}_inactive_ref:{ref}")

    if decision in {"ANSWER", "PARTIAL"}:
        if auth != "authorized":
            errors.append("answer_without_authorization")
        if not evidence or not claims or not filled(response.get("answer")):
            errors.append("answer_without_evidence_claims_or_text")
        if answerability.get("conflict_status") == "open":
            errors.append("answer_with_open_conflict")
        if answerability.get("freshness_status") != "current":
            errors.append("answer_with_noncurrent_sources")
        if decision == "PARTIAL" and not filled(response.get("scope_limits")):
            errors.append("partial_without_scope_limits")
    if decision == "DENY" and (evidence or claims):
        errors.append("deny_leaks_evidence_or_claims")
    if auth == "unauthorized" and decision != "DENY":
        errors.append("unauthorized_not_denied")
    if decision == "ESCALATE" and not filled(answerability.get("escalation_owner")):
        errors.append("escalate_without_owner")
    if decision in {"ABSTAIN", "DENY", "ESCALATE"} and claims:
        errors.append("nonanswer_decision_has_claims")

    tests = data.get("operational_tests", [])
    test_types, all_passed = set(), bool(tests)
    for i, case in enumerate(tests):
        fields = ["id", "type", "prompt", "expected_decision", "rubric_ref", "success_threshold", "owner", "status"]
        missing = [k for k in fields if not filled(case.get(k))]
        if missing:
            errors.append(f"test_{i}_missing:" + ",".join(missing))
        test_types.add(case.get("type"))
        if case.get("expected_decision") not in DECISIONS:
            errors.append(f"test_{i}_invalid_expected_decision")
        status = case.get("status")
        if status not in {"planned", "passed", "failed", "not_run"}:
            errors.append(f"test_{i}_invalid_status")
        if status in {"passed", "failed"} and not filled(case.get("result_source")):
            errors.append(f"test_{i}_missing_result_source")
        if status != "passed":
            all_passed = False
    required = set(contract.get("standards", {}).get("required_test_types", [])) or REQUIRED_TESTS
    missing_tests = sorted(required - test_types)
    if missing_tests:
        errors.append("missing_test_types:" + ",".join(missing_tests))

    governance = data.get("governance", {})
    governance_fields = ["logging_policy", "feedback_log_ref", "unanswerable_backlog", "incident_process", "retention_policy", "review_cycle", "approval_status", "version", "owner"]
    if not all(filled(governance.get(k)) for k in governance_fields):
        errors.append("incomplete_governance")
    if governance.get("approval_status") not in {"draft", "approved", "rejected"}:
        errors.append("invalid_approval_status")

    if missing_contract or missing_request or auth == "unknown":
        state = "NOT_READY"
    elif auth == "unauthorized" or decision == "DENY":
        state = "ACCESS_DENIED" if not errors else "REVISE"
    elif decision == "ABSTAIN":
        state = "ABSTAINED" if not errors else "REVISE"
    elif decision == "ESCALATE":
        state = "ESCALATION_REQUIRED" if not errors else "REVISE"
    elif errors:
        state = "REVISE"
    elif contract.get("risk_level") == "high" or data.get("guardrails") or data.get("expert_review_required"):
        state = "READY_WITH_GUARDRAILS"
    elif all_passed and governance.get("approval_status") == "approved":
        state = "APPROVED_FOR_USE"
    elif all_passed:
        state = "ANSWERING_VALIDATED"
    else:
        state = "READY_FOR_PILOT_TEST"

    return {
        "state": state,
        "answerability_decision": decision,
        "metrics": {"evidence_count": len(evidence), "claim_count": len(claims), "referenced_evidence_count": len(referenced_ids), "test_type_coverage": sorted(test_types)},
        "errors": sorted(set(errors)),
        "warnings": sorted(set(warnings)),
        "guardrails": data.get("guardrails", []),
        "next_action": {
            "NOT_READY": "complete_contract_request_access_and_tests",
            "ACCESS_DENIED": "return_safe_denial_without_source_disclosure",
            "ABSTAINED": "log_gap_and_request_authorized_source_update",
            "ESCALATION_REQUIRED": "handoff_safe_evidence_to_named_owner",
            "REVISE": "fix_decision_evidence_citations_access_tests_or_governance",
            "READY_WITH_GUARDRAILS": "complete_required_domain_security_review",
            "READY_FOR_PILOT_TEST": "run_required_operational_tests",
            "ANSWERING_VALIDATED": "obtain_human_approval",
            "APPROVED_FOR_USE": "deploy_on_approved_channel"
        }[state]
    }

def main():
    if len(sys.argv) != 2:
        raise SystemExit("usage: evaluate_grounded_answer.py INPUT.json")
    data = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    print(json.dumps(evaluate(data), ensure_ascii=False, indent=2, sort_keys=True))

if __name__ == "__main__":
    main()
