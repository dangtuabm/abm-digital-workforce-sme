#!/usr/bin/env python3
"""Static evaluator for use-case-discovery v2.3 fixtures."""
from __future__ import annotations
import json, sys
from pathlib import Path

MIN = {"evidence_sources":12,"work_moments":10,"opportunities":10,"data_system_maps":8,"basic_screens":10,"coverage_records":8,"validation_items":8,"decisions":6,"test_cases":10,"risks":6}
REQ = {
"evidence_sources":"id source owner rights method evidence_type date coverage quality conflict status".split(),
"work_moments":"id outcome value_stream process_stage unit role user job task_or_decision trigger inputs steps handoffs exceptions output action consumer workload pain evidence_refs owner status".split(),
"opportunities":"id user_ref work_ref problem evidence_refs desired_outcome input data_refs systems output action acceptance value_hypothesis metric capability_pattern alternative human_authority autonomy risk assumptions validation_question status".split(),
"data_system_maps":"id opportunity_ref data_or_system kind system_of_record owner rights classification access quality integration dependency status".split(),
"basic_screens":"id opportunity_ref evidence_sufficiency data_rights output_testability owner_fit workflow_fit human_control harm_security_privacy dependencies disposition reason".split(),
"coverage_records":"id value_stream unit role work_moment source_ref coverage bias gap owner status".split(),
"validation_items":"id opportunity_ref question hypothesis evidence_needed method owner due_trigger consequence status".split(),
"decisions":"id decision evidence_refs owner authority status consequence".split(),
"test_cases":"id category requirement_ref setup expected actual evidence status owner".split(),
"risks":"id risk evidence impact control owner residual status".split()}
TESTS={"discovery_contract","evidence_work_trace","opportunity_contract","data_system_authority","basic_screen_boundary","coverage_dedup","security_injection"}
REVIEWS={"BUSINESS_PROCESS_OWNER","ROLE_USER_REPRESENTATIVE","DATA_SYSTEM_OWNER","RISK_CONTROL_OWNER","PEOPLE_CHANGE_OWNER","VALUE_FINANCE_OWNER"}
RISKS={"SCOPE_COVERAGE_BIAS","PAIN_EVIDENCE_HYPOTHESIS","DATA_RIGHTS_QUALITY","SOLUTION_AUTONOMY_HARM","DUPLICATE_BUNDLE_TRACE","VALUE_METRIC_HANDOFF"}
FORBIDDEN_TRUE={"invented_process","invented_pain","invented_metric","invented_roi","sensitive_inference","employee_surveillance","job_elimination","opportunity_ranked","score_assigned","vendor_selected","architecture_committed","automation_approved","outreach_sent","register_published","data_rights_bypassed","conflict_hidden","evidence_mutated"}
FORBIDDEN_STATE={"RANKED","SELECTED","APPROVED","AUTOMATION_APPROVED","OUTREACH_SENT","PUBLISHED","AUTO_APPROVED"}

def blank(v): return v is None or v=="" or v==[] or v=={}
def walk(v,p,d):
    if isinstance(v,dict):
        for k,x in v.items():
            q=f"{p}.{k}" if p else k
            if k in FORBIDDEN_TRUE and x is True: d.append(f"forbidden_true:{q}")
            if k in {"state","status","release_state"} and str(x).upper() in FORBIDDEN_STATE: d.append(f"forbidden_state:{q}={x}")
            if any(s in k.lower() for s in ("password","api_key","token_value","secret_value")) and not blank(x): d.append(f"secret_material:{q}")
            walk(x,q,d)
    elif isinstance(v,list):
        for i,x in enumerate(v): walk(x,f"{p}[{i}]",d)

def main(path):
    x=json.loads(Path(path).read_text(encoding="utf-8")); d=[]
    if x.get("artifact")!="Evidence-Based A.I Use-Case Opportunity Register": d.append("artifact_name")
    required_top={
      "discovery_contract":"objective scope outcomes value_streams units roles sponsor owner cutoff dod exclusions confidentiality action_boundary".split(),
      "business_context":"strategy outcomes constraints stakeholders processes terminology source_boundary".split(),
      "authority_map":"business_owner process_owner data_owner system_owner risk_owner people_owner value_owner human_checkpoint prohibited_actions".split()}
    for sec,fields in required_top.items():
        obj=x.get(sec,{})
        for f in fields:
            if blank(obj.get(f)): d.append(f"{sec}.{f}")
    for group,n in MIN.items():
        a=x.get(group,[])
        if not isinstance(a,list): d.append(f"{group}:not_list"); continue
        if len(a)<n: d.append(f"{group}:count<{n}")
        seen=[]
        for i,o in enumerate(a):
            if not isinstance(o,dict): d.append(f"{group}[{i}]:not_object"); continue
            for f in REQ[group]:
                if blank(o.get(f)): d.append(f"{group}[{i}].{f}")
            if o.get("id") in seen: d.append(f"{group}:duplicate_id:{o.get('id')}")
            seen.append(o.get("id"))
    ids={g:{o.get("id") for o in x.get(g,[]) if isinstance(o,dict)} for g in REQ}
    evidence_types={"OBSERVED","DOCUMENTED","SYSTEM_DERIVED","SELF_REPORTED","CALCULATED","ESTIMATED","UNVERIFIED"}
    for i,o in enumerate(x.get("evidence_sources",[])):
        if o.get("evidence_type") not in evidence_types: d.append(f"evidence_sources[{i}].evidence_type")
        if str(o.get("status","")).upper()!="REGISTERED": d.append(f"evidence_sources[{i}].status")
    for i,o in enumerate(x.get("work_moments",[])):
        for r in o.get("evidence_refs",[]):
            if r not in ids["evidence_sources"]: d.append(f"work_moments[{i}].evidence_ref:{r}")
        if str(o.get("status","")).upper() not in {"DOCUMENTED","HYPOTHESIS"}: d.append(f"work_moments[{i}].status")
    for i,o in enumerate(x.get("opportunities",[])):
        if o.get("work_ref") not in ids["work_moments"]: d.append(f"opportunities[{i}].work_ref")
        for r in o.get("evidence_refs",[]):
            if r not in ids["evidence_sources"]: d.append(f"opportunities[{i}].evidence_ref:{r}")
        if str(o.get("status","")).upper() not in {"VALIDATE","DEFER","EXCLUDE"}: d.append(f"opportunities[{i}].status")
    for i,o in enumerate(x.get("data_system_maps",[])):
        if o.get("opportunity_ref") not in ids["opportunities"]: d.append(f"data_system_maps[{i}].opportunity_ref")
        if str(o.get("status","")).upper() not in {"MAPPED","TBD"}: d.append(f"data_system_maps[{i}].status")
    for i,o in enumerate(x.get("basic_screens",[])):
        if o.get("opportunity_ref") not in ids["opportunities"]: d.append(f"basic_screens[{i}].opportunity_ref")
        if str(o.get("disposition","")).upper() not in {"VALIDATE","DEFER","EXCLUDE"}: d.append(f"basic_screens[{i}].disposition")
        if any(k in o for k in ("score","rank","weight")): d.append(f"basic_screens[{i}]:prioritization_field")
    for i,o in enumerate(x.get("coverage_records",[])):
        if o.get("source_ref") not in ids["evidence_sources"]: d.append(f"coverage_records[{i}].source_ref")
    for i,o in enumerate(x.get("validation_items",[])):
        if o.get("opportunity_ref") not in ids["opportunities"]: d.append(f"validation_items[{i}].opportunity_ref")
        if str(o.get("status","")).upper() not in {"OPEN","VALIDATED_HUMAN"}: d.append(f"validation_items[{i}].status")
    valid=set().union(*ids.values())
    for i,o in enumerate(x.get("decisions",[])):
        for r in o.get("evidence_refs",[]):
            if r not in valid: d.append(f"decisions[{i}].evidence_ref:{r}")
        if str(o.get("status","")).upper() not in {"PENDING","APPROVED_HUMAN"}: d.append(f"decisions[{i}].status")
    for i,o in enumerate(x.get("test_cases",[])):
        if o.get("requirement_ref") not in valid: d.append(f"test_cases[{i}].requirement_ref")
        if str(o.get("status","")).upper() not in {"PASS","FAIL"}: d.append(f"test_cases[{i}].status")
    risk_ids={o.get("id") for o in x.get("risks",[]) if isinstance(o,dict)}
    for r in RISKS-risk_ids: d.append(f"missing_risk:{r}")
    tests=x.get("tests",[]); passed={o.get("id") for o in tests if o.get("status")=="PASS" and not blank(o.get("evidence"))}
    for t in TESTS-passed: d.append(f"test_not_passed:{t}")
    reviews=x.get("reviews",[]); reviewed={o.get("id") for o in reviews if o.get("status")=="PASS" and not blank(o.get("evidence"))}
    gaps=sorted(REVIEWS-reviewed); walk(x,"",d)
    state="READY_FOR_HUMAN_DISCOVERY_REVIEW" if not d and not gaps else "NOT_READY"
    counts={k:len(x.get(k,[])) if isinstance(x.get(k),list) else 0 for k in MIN}; counts.update({"tests_passed":len(passed),"reviews_passed":len(reviewed)})
    print(json.dumps({"state":state,"defect_count":len(d),"review_gap_count":len(gaps),"counts":counts,"defects":d,"review_gaps":gaps},ensure_ascii=False,indent=2))
    return 0 if state.startswith("READY") else 1

if __name__=="__main__":
    if len(sys.argv)!=2: print("usage: evaluate_use_case_discovery.py fixture.json",file=sys.stderr); sys.exit(2)
    sys.exit(main(sys.argv[1]))
