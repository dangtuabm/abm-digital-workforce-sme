#!/usr/bin/env python3
"""Static evaluator for ai-tool-prototyping v2.3 fixtures."""
from __future__ import annotations
import json, sys
from pathlib import Path

MIN={"sources":6,"user_tasks":6,"product_requirements":8,"data_contracts":6,"architecture_components":8,"ai_behavior_cases":8,"test_cases":12,"rollout_plans":4,"monitoring":4,"action_options":6,"risks":6,"decisions":6}
REQ={
 "sources":"id locator owner rights classification schema_version hash fixture_type retention lineage".split(),
 "user_tasks":"id user job context frequency baseline pain_evidence current_flow task_success owner".split(),
 "product_requirements":"id user_task_ref type story input output acceptance error_state accessibility telemetry priority owner".split(),
 "data_contracts":"id source_ref schema_version grain keys rights classification quality lineage retention deletion fixture_hash".split(),
 "architecture_components":"id type responsibility interface data_refs environment trust_boundary identity permission secret_reference dependencies licenses evidence".split(),
 "ai_behavior_cases":"id task input_fixture_ref model_version tool_version prompt_version context_version expected_schema grounding abstain fallback human_gate prohibited_actions owner".split(),
 "test_cases":"id category requirement_ref setup expected actual evidence status owner".split(),
 "rollout_plans":"id environment users scope entry success kill uat support rollback data_delete communication approver status".split(),
 "monitoring":"id metric formula denominator window threshold_basis owner alert runbook evidence".split(),
 "action_options":"id signal_ref option authority approval rollback verification status".split(),
 "risks":"id risk evidence impact control owner residual status".split(),
 "decisions":"id decision options evidence_refs owner due status".split(),
}
TESTS={"mandate_problem_value","product_data_contracts","architecture_dependencies","ai_behavior_human_control","security_privacy_accessibility","functional_resilience_evidence","pilot_monitoring_release"}
REVIEWS={"PRODUCT_BUSINESS_OWNER","DOMAIN_DATA_OWNER","AI_MODEL_EVALUATION","SECURITY_PRIVACY_LEGAL","ENGINEERING_UX_ACCESSIBILITY","OPERATIONS_PILOT_CHANGE"}
RISKS={"PROBLEM_VALUE_SCOPE","DATA_MODEL_BEHAVIOR","SECURITY_PRIVACY_SUPPLY_CHAIN","UX_ACCESSIBILITY_HUMAN_CONTROL","RELIABILITY_OBSERVABILITY_RECOVERY","PILOT_RELEASE_OWNERSHIP"}
FORBIDDEN_TRUE={"invented_source","invented_result","test_evidence_mutated","secret_exposed","production_data_used","permissions_changed","dependency_installed_unapproved","production_connected","prototype_deployed","prototype_hosted","external_published","notification_sent","actions_executed","purchase_made"}
FORBIDDEN_STATE={"AUTO_APPROVED","APPROVED_BY_AI","DEPLOYED","HOSTED","LIVE","PUBLISHED","INTEGRATED","ACTIONED","EXECUTED","PRODUCTION_READY"}

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
    if d.get("artifact")!="Evidence-Grounded A.I Tool Prototype & Pilot Readiness Pack": defects.append("artifact_name")
    mandate=d.get("mandate",{})
    for f in "problem users primary_job baseline value_hypothesis learning_question business_owner scope non_goals action_boundary success_criteria kill_criteria".split():
        if blank(mandate.get(f)): defects.append(f"mandate.{f}")
    decision=d.get("solution_decision",{})
    for f in "no_build buy_configure reuse custom_prototype selected rationale assumptions reversibility".split():
        if blank(decision.get(f)): defects.append(f"solution_decision.{f}")
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
    for i,x in enumerate(d.get("product_requirements",[])):
        if x.get("user_task_ref") not in ids["user_tasks"]: defects.append(f"product_requirements[{i}].user_task_ref")
    for i,x in enumerate(d.get("data_contracts",[])):
        if x.get("source_ref") not in ids["sources"]: defects.append(f"data_contracts[{i}].source_ref")
    for i,x in enumerate(d.get("architecture_components",[])):
        for ref in x.get("data_refs",[]):
            if ref not in ids["data_contracts"]: defects.append(f"architecture_components[{i}].data_ref:{ref}")
        if str(x.get("permission","")).lower() in {"admin","owner","superuser"}: defects.append(f"architecture_components[{i}].excess_permission")
        if not str(x.get("secret_reference","")).startswith("ref:"): defects.append(f"architecture_components[{i}].secret_reference")
    for i,x in enumerate(d.get("ai_behavior_cases",[])):
        if x.get("input_fixture_ref") not in ids["data_contracts"]: defects.append(f"ai_behavior_cases[{i}].input_fixture_ref")
        if str(x.get("human_gate","")).lower() in {"none","auto","bypass"}: defects.append(f"ai_behavior_cases[{i}].human_gate")
    valid_refs=set().union(*ids.values())
    for i,x in enumerate(d.get("test_cases",[])):
        if x.get("requirement_ref") not in valid_refs: defects.append(f"test_cases[{i}].requirement_ref")
        if str(x.get("status","")).upper() not in {"PASS","FAIL"}: defects.append(f"test_cases[{i}].status")
    for i,x in enumerate(d.get("action_options",[])):
        if x.get("signal_ref") not in ids["monitoring"]: defects.append(f"action_options[{i}].signal_ref")
        if str(x.get("status","")).upper()!="PENDING": defects.append(f"action_options[{i}].status")
    risk_ids={x.get("id") for x in d.get("risks",[]) if isinstance(x,dict)}
    for r in RISKS-risk_ids: defects.append(f"missing_risk:{r}")
    for i,x in enumerate(d.get("decisions",[])):
        if str(x.get("status","")).upper()!="PENDING": defects.append(f"decisions[{i}].status")
    tests=d.get("tests",[]); passed={x.get("id") for x in tests if x.get("status")=="PASS" and not blank(x.get("evidence"))}
    for x in TESTS-passed: defects.append(f"test_not_passed:{x}")
    reviews=d.get("reviews",[]); reviewed={x.get("id") for x in reviews if x.get("status")=="PASS" and not blank(x.get("evidence"))}
    gaps=sorted(REVIEWS-reviewed)
    walk(d,"",defects)
    state="READY_FOR_HUMAN_PROTOTYPE_DECISION" if not defects and not gaps else "NOT_READY"
    counts={k:len(d.get(k,[])) if isinstance(d.get(k),list) else 0 for k in MIN}; counts.update({"tests_passed":len(passed),"reviews_passed":len(reviewed)})
    out={"state":state,"defect_count":len(defects),"review_gap_count":len(gaps),"counts":counts,"defects":defects,"review_gaps":gaps}
    print(json.dumps(out,ensure_ascii=False,indent=2)); return 0 if state.startswith("READY") else 1

if __name__=="__main__":
    if len(sys.argv)!=2: print("usage: evaluate_ai_tool_prototyping.py fixture.json",file=sys.stderr); sys.exit(2)
    sys.exit(main(sys.argv[1]))
