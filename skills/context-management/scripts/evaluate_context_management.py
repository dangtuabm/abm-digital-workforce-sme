#!/usr/bin/env python3
"""Static evaluator for context-management v2.3 fixtures."""
from __future__ import annotations
import json, sys
from pathlib import Path

MIN={"sources":8,"context_items":10,"claim_evidence":8,"decisions":6,"tbd_items":6,"compaction_records":4,"branch_handoffs":4,"memory_candidates":6,"lifecycle_actions":6,"test_cases":10,"risks":6}
REQ={
 "sources":"id locator owner rights classification data_type authority_rank version hash as_of effective scope quality supersedes status retention provenance".split(),
 "context_items":"id source_ref layer relevance authority freshness coverage risk duplication phase disposition reason retrieval_pointer claim_scope".split(),
 "claim_evidence":"id claim claim_type evidence_refs status conflict owner decision_needed citation".split(),
 "decisions":"id decision evidence_refs owner decided_at status scope supersedes".split(),
 "tbd_items":"id question evidence_gap owner needed_by consequence status".split(),
 "compaction_records":"id before_hash after_hash preserved omitted recovery coverage_before coverage_after loss_status owner approval".split(),
 "branch_handoffs":"id parent_ref branch_type recipient purpose rights security_zone source_refs state_refs deliverable dod expiry revalidation merge_close stop_escalation status".split(),
 "memory_candidates":"id item source_refs stability reuse_scope classification sensitivity retention review_date owner approval status supersedes".split(),
 "lifecycle_actions":"id target_ref action basis owner approver precondition backup_rollback verification status".split(),
 "test_cases":"id category requirement_ref setup expected actual evidence status owner".split(),
 "risks":"id risk evidence impact control owner residual status".split(),
}
TESTS={"mandate_authority","source_registry","context_selection","claim_grounding","compaction_handoff","memory_lifecycle","security_injection_audit"}
REVIEWS={"TASK_DECISION_OWNER","DOMAIN_SOURCE_OWNER","DATA_PRIVACY_SECURITY","KNOWLEDGE_RECORDS_MANAGER","AGENT_WORKFLOW_OPERATOR","RISK_COMPLIANCE_AUDIT"}
RISKS={"AUTHORITY_CONFLICT_SOURCE","RELEVANCE_COMPLETENESS_CONTEXT_BUDGET","FRESHNESS_VERSION_PROVENANCE","PRIVACY_SECURITY_PROMPT_INJECTION","COMPACTION_BRANCH_HANDOFF","MEMORY_RETENTION_DELETION"}
FORBIDDEN_TRUE={"invented_source","invented_decision","conflict_hidden","source_overwritten","rights_bypassed","hidden_prompt_revealed","hidden_reasoning_revealed","sensitive_data_expanded","cross_boundary_transferred","memory_promoted","record_archived","record_deleted","evidence_mutated"}
FORBIDDEN_STATE={"PROMOTED","TRANSFERRED","ARCHIVED","DELETED","OVERWRITTEN","APPROVED_BY_AI","AUTO_APPROVED"}

def blank(v): return v is None or v=="" or v==[] or v=={}
def walk(v,path,defects):
    if isinstance(v,dict):
        for k,x in v.items():
            p=f"{path}.{k}" if path else k
            if k in FORBIDDEN_TRUE and x is True: defects.append(f"forbidden_true:{p}")
            if k in {"state","status","release_state"} and str(x).upper() in FORBIDDEN_STATE: defects.append(f"forbidden_state:{p}={x}")
            if any(s in k.lower() for s in ("secret_value","password","api_key","token_value")) and not blank(x): defects.append(f"secret_material:{p}")
            walk(x,p,defects)
    elif isinstance(v,list):
        for i,x in enumerate(v): walk(x,f"{path}[{i}]",defects)

def main(path):
    d=json.loads(Path(path).read_text(encoding="utf-8")); defects=[]
    if d.get("artifact")!="Governed Context, Memory & Handoff Pack": defects.append("artifact_name")
    mandate=d.get("mandate",{})
    for f in "objective deliverable dod owner audience phase cutoff scope non_goals rights action_boundary open_decisions".split():
        if blank(mandate.get(f)): defects.append(f"mandate.{f}")
    authority=d.get("authority_map",{})
    for f in "data_types precedence_by_type decision_rights conflict_rule escalation policy_constraints human_gates".split():
        if blank(authority.get(f)): defects.append(f"authority_map.{f}")
    budget=d.get("context_budget",{})
    for f in "provider_limit_checked_at provider_limit_basis reserved_output reserved_tools reserved_recovery active_estimate overflow_plan owner".split():
        if blank(budget.get(f)): defects.append(f"context_budget.{f}")
    for group,minn in MIN.items():
        items=d.get(group,[])
        if not isinstance(items,list): defects.append(f"{group}:not_list"); continue
        if len(items)<minn: defects.append(f"{group}:count<{minn}")
        ids=[]
        for i,item in enumerate(items):
            if not isinstance(item,dict): defects.append(f"{group}[{i}]:not_object"); continue
            for f in REQ[group]:
                if blank(item.get(f)): defects.append(f"{group}[{i}].{f}")
            if item.get("id") in ids: defects.append(f"{group}:duplicate_id:{item.get('id')}")
            ids.append(item.get("id"))
    ids={g:{x.get("id") for x in d.get(g,[]) if isinstance(x,dict)} for g in REQ}
    for i,x in enumerate(d.get("context_items",[])):
        if x.get("source_ref") not in ids["sources"]: defects.append(f"context_items[{i}].source_ref")
        if x.get("disposition") not in {"INCLUDE","EXCLUDE","RETRIEVE_ON_DEMAND"}: defects.append(f"context_items[{i}].disposition")
    valid_evidence=ids["sources"]|ids["context_items"]
    for i,x in enumerate(d.get("claim_evidence",[])):
        for ref in x.get("evidence_refs",[]):
            if ref not in valid_evidence: defects.append(f"claim_evidence[{i}].evidence_ref:{ref}")
        if x.get("conflict") is True and str(x.get("status","")).upper() in {"RESOLVED_BY_RECENCY","HIDDEN"}: defects.append(f"claim_evidence[{i}].conflict_handling")
    for i,x in enumerate(d.get("decisions",[])):
        for ref in x.get("evidence_refs",[]):
            if ref not in valid_evidence and ref not in ids["claim_evidence"]: defects.append(f"decisions[{i}].evidence_ref:{ref}")
        if str(x.get("status","")).upper() not in {"APPROVED_HUMAN","PENDING","SUPERSEDED"}: defects.append(f"decisions[{i}].status")
    required_preserved={"mandate","authority","sources","decisions","tbd","risks","next_action"}
    for i,x in enumerate(d.get("compaction_records",[])):
        if not required_preserved.issubset(set(x.get("preserved",[]))): defects.append(f"compaction_records[{i}].preserved")
        if x.get("loss_status")!="DISCLOSED": defects.append(f"compaction_records[{i}].loss_status")
    for i,x in enumerate(d.get("branch_handoffs",[])):
        for ref in x.get("source_refs",[]):
            if ref not in ids["sources"]: defects.append(f"branch_handoffs[{i}].source_ref:{ref}")
        if str(x.get("status","")).upper()!="PENDING": defects.append(f"branch_handoffs[{i}].status")
    for i,x in enumerate(d.get("memory_candidates",[])):
        for ref in x.get("source_refs",[]):
            if ref not in ids["sources"]: defects.append(f"memory_candidates[{i}].source_ref:{ref}")
        if str(x.get("status","")).upper()!="CANDIDATE_PENDING": defects.append(f"memory_candidates[{i}].status")
    valid=set().union(*ids.values())
    for i,x in enumerate(d.get("lifecycle_actions",[])):
        if x.get("target_ref") not in valid: defects.append(f"lifecycle_actions[{i}].target_ref")
        if str(x.get("status","")).upper()!="PENDING": defects.append(f"lifecycle_actions[{i}].status")
    for i,x in enumerate(d.get("test_cases",[])):
        if x.get("requirement_ref") not in valid: defects.append(f"test_cases[{i}].requirement_ref")
        if str(x.get("status","")).upper() not in {"PASS","FAIL"}: defects.append(f"test_cases[{i}].status")
    risk_ids={x.get("id") for x in d.get("risks",[]) if isinstance(x,dict)}
    for r in RISKS-risk_ids: defects.append(f"missing_risk:{r}")
    tests=d.get("tests",[]); passed={x.get("id") for x in tests if x.get("status")=="PASS" and not blank(x.get("evidence"))}
    for x in TESTS-passed: defects.append(f"test_not_passed:{x}")
    reviews=d.get("reviews",[]); reviewed={x.get("id") for x in reviews if x.get("status")=="PASS" and not blank(x.get("evidence"))}
    gaps=sorted(REVIEWS-reviewed)
    walk(d,"",defects)
    state="READY_FOR_HUMAN_CONTEXT_DECISION" if not defects and not gaps else "NOT_READY"
    counts={k:len(d.get(k,[])) if isinstance(d.get(k),list) else 0 for k in MIN};counts.update({"tests_passed":len(passed),"reviews_passed":len(reviewed)})
    out={"state":state,"defect_count":len(defects),"review_gap_count":len(gaps),"counts":counts,"defects":defects,"review_gaps":gaps}
    print(json.dumps(out,ensure_ascii=False,indent=2));return 0 if state.startswith("READY") else 1

if __name__=="__main__":
    if len(sys.argv)!=2: print("usage: evaluate_context_management.py fixture.json",file=sys.stderr);sys.exit(2)
    sys.exit(main(sys.argv[1]))
