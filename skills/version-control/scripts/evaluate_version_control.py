#!/usr/bin/env python3
"""Static evaluator for version-control v2.3 fixtures."""
from __future__ import annotations
import json, sys
from pathlib import Path

MIN={"assets":8,"versions":10,"change_requests":6,"dependency_impacts":8,"approvals":6,"release_candidates":4,"rollback_plans":4,"audit_events":10,"test_cases":10,"risks":6}
REQ={
"assets":"id type title system_of_record locator owner authority classification rights consumers retention aliases status".split(),
"versions":"id asset_ref version scheme parent_ref locator hash snapshot created_at effective_at status supersedes provenance approval_ref immutable".split(),
"change_requests":"id asset_ref baseline_ref candidate_ref source rationale owner structured_diff affected_scope alternatives compatibility migration status".split(),
"dependency_impacts":"id change_ref consumer dependency constraint impact compatibility migration owner evidence status".split(),
"approvals":"id candidate_ref reviewer role authority sod_check decision decided_at scope hash evidence status".split(),
"release_candidates":"id version_ref change_refs hash build_evidence test_refs release_notes window channels audience monitoring stop_trigger rollback_ref status".split(),
"rollback_plans":"id candidate_ref trigger authority target_version_ref backup recovery_steps consumer_restore reconciliation verification owner status".split(),
"audit_events":"id timestamp actor action target_ref before_ref after_ref evidence result correlation append_only".split(),
"test_cases":"id category requirement_ref setup expected actual evidence status owner".split(),
"risks":"id risk evidence impact control owner residual status".split()}
TESTS={"scope_registry","version_policy","change_traceability","dependency_impact","release_approval","rollback_recovery","security_audit"}
REVIEWS={"ASSET_OWNER","DOMAIN_OWNER","CHANGE_AUTHORITY","DATA_SECURITY_RECORDS","DEPENDENCY_CONSUMER","RISK_AUDIT"}
RISKS={"CANONICAL_ID_DUPLICATE","AUTHORITY_EFFECTIVITY_CONFLICT","IMMUTABILITY_PROVENANCE","DEPENDENCY_COMPATIBILITY","RELEASE_ROLLBACK_RECOVERY","ACCESS_RETENTION_AUDIT"}
FORBIDDEN_TRUE={"invented_asset","invented_version","invented_approval","hash_mismatch_ignored","conflict_hidden","released_artifact_mutated","audit_mutated","rights_bypassed","secret_revealed","private_prompt_revealed","auto_merged","auto_released","auto_effective","auto_rollback","auto_archived","auto_deleted","source_overwritten"}
FORBIDDEN_STATE={"MERGED","RELEASED","EFFECTIVE","ROLLED_BACK","ARCHIVED","DISPOSED","DELETED","OVERWRITTEN","APPROVED_BY_AI","AUTO_APPROVED"}

def blank(v): return v is None or v=="" or v==[] or v=={}
def walk(v,path,defects):
    if isinstance(v,dict):
        for k,x in v.items():
            p=f"{path}.{k}" if path else k
            if k in FORBIDDEN_TRUE and x is True: defects.append(f"forbidden_true:{p}")
            if k in {"state","status","release_state","decision"} and str(x).upper() in FORBIDDEN_STATE: defects.append(f"forbidden_state:{p}={x}")
            if any(s in k.lower() for s in ("secret_value","password","api_key","token_value")) and not blank(x): defects.append(f"secret_material:{p}")
            walk(x,p,defects)
    elif isinstance(v,list):
        for i,x in enumerate(v): walk(x,f"{path}[{i}]",defects)

def main(path):
    d=json.loads(Path(path).read_text(encoding="utf-8")); defects=[]
    if d.get("artifact")!="Controlled Version, Release & Rollback Pack": defects.append("artifact_name")
    for section,fields in {
      "mandate":"purpose deliverable dod owner audience cutoff scope non_goals rights action_boundary open_decisions".split(),
      "authority_map":"asset_types propose_rights review_rights approve_rights release_rights effective_rights rollback_rights archive_dispose_rights sod_rule conflict_rule escalation".split(),
      "version_policy":"scheme_by_type version_meaning states branch_merge immutable_release naming_tagging compatibility_rule deprecation_rule retention_rule".split()
    }.items():
        obj=d.get(section,{})
        for f in fields:
            if blank(obj.get(f)): defects.append(f"{section}.{f}")
    for group,minn in MIN.items():
        items=d.get(group,[])
        if not isinstance(items,list): defects.append(f"{group}:not_list"); continue
        if len(items)<minn: defects.append(f"{group}:count<{minn}")
        seen=[]
        for i,item in enumerate(items):
            if not isinstance(item,dict): defects.append(f"{group}[{i}]:not_object"); continue
            for f in REQ[group]:
                if blank(item.get(f)): defects.append(f"{group}[{i}].{f}")
            if item.get("id") in seen: defects.append(f"{group}:duplicate_id:{item.get('id')}")
            seen.append(item.get("id"))
    ids={g:{x.get("id") for x in d.get(g,[]) if isinstance(x,dict)} for g in REQ}
    for i,x in enumerate(d.get("versions",[])):
        if x.get("asset_ref") not in ids["assets"]: defects.append(f"versions[{i}].asset_ref")
        if x.get("parent_ref")!="ROOT" and x.get("parent_ref") not in ids["versions"]: defects.append(f"versions[{i}].parent_ref")
        if x.get("immutable") is not True: defects.append(f"versions[{i}].immutable")
        if str(x.get("status","")).upper() not in {"DRAFT","IN_REVIEW","APPROVED_HUMAN","RELEASE_CANDIDATE","SUPERSEDED","DEPRECATED"}: defects.append(f"versions[{i}].status")
    for i,x in enumerate(d.get("change_requests",[])):
        if x.get("asset_ref") not in ids["assets"]: defects.append(f"change_requests[{i}].asset_ref")
        for f in ("baseline_ref","candidate_ref"):
            if x.get(f) not in ids["versions"]: defects.append(f"change_requests[{i}].{f}")
        if str(x.get("status","")).upper() not in {"OPEN","IN_REVIEW","PENDING"}: defects.append(f"change_requests[{i}].status")
    for i,x in enumerate(d.get("dependency_impacts",[])):
        if x.get("change_ref") not in ids["change_requests"]: defects.append(f"dependency_impacts[{i}].change_ref")
    for i,x in enumerate(d.get("approvals",[])):
        if x.get("candidate_ref") not in ids["release_candidates"]: defects.append(f"approvals[{i}].candidate_ref")
        if str(x.get("decision","")).upper() not in {"APPROVED_HUMAN","PENDING","REJECTED_HUMAN"}: defects.append(f"approvals[{i}].decision")
        if str(x.get("status","")).upper()!="EVIDENCED": defects.append(f"approvals[{i}].status")
    for i,x in enumerate(d.get("release_candidates",[])):
        if x.get("version_ref") not in ids["versions"]: defects.append(f"release_candidates[{i}].version_ref")
        for ref in x.get("change_refs",[]):
            if ref not in ids["change_requests"]: defects.append(f"release_candidates[{i}].change_ref:{ref}")
        for ref in x.get("test_refs",[]):
            if ref not in ids["test_cases"]: defects.append(f"release_candidates[{i}].test_ref:{ref}")
        if x.get("rollback_ref") not in ids["rollback_plans"]: defects.append(f"release_candidates[{i}].rollback_ref")
        if str(x.get("status","")).upper()!="PENDING": defects.append(f"release_candidates[{i}].status")
    for i,x in enumerate(d.get("rollback_plans",[])):
        if x.get("candidate_ref") not in ids["release_candidates"]: defects.append(f"rollback_plans[{i}].candidate_ref")
        if x.get("target_version_ref") not in ids["versions"]: defects.append(f"rollback_plans[{i}].target_version_ref")
        if str(x.get("status","")).upper()!="PENDING": defects.append(f"rollback_plans[{i}].status")
    valid=set().union(*ids.values())
    for i,x in enumerate(d.get("audit_events",[])):
        if x.get("target_ref") not in valid: defects.append(f"audit_events[{i}].target_ref")
        if x.get("append_only") is not True: defects.append(f"audit_events[{i}].append_only")
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
    state="READY_FOR_HUMAN_VERSION_DECISION" if not defects and not gaps else "NOT_READY"
    counts={k:len(d.get(k,[])) if isinstance(d.get(k),list) else 0 for k in MIN}
    counts.update({"tests_passed":len(passed),"reviews_passed":len(reviewed)})
    out={"state":state,"defect_count":len(defects),"review_gap_count":len(gaps),"counts":counts,"defects":defects,"review_gaps":gaps}
    print(json.dumps(out,ensure_ascii=False,indent=2)); return 0 if state.startswith("READY") else 1

if __name__=="__main__":
    if len(sys.argv)!=2: print("usage: evaluate_version_control.py fixture.json",file=sys.stderr);sys.exit(2)
    sys.exit(main(sys.argv[1]))

