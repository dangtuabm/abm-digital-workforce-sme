#!/usr/bin/env python3
"""Static evaluator for use-case-prioritization v2.3 fixtures."""
from __future__ import annotations
import json, sys
from pathlib import Path

MIN={"evidence_sources":12,"criteria":8,"candidates":10,"gates":10,"priority_results":10,"sensitivity_scenarios":3,"portfolio_views":5,"decisions":6,"test_cases":10,"risks":6}
REQ={
"evidence_sources":"id source owner rights evidence_type date version coverage quality conflict status".split(),
"criteria":"id definition direction weight anchors evidence_rule missing_rule double_count_rule owner approved_by status".split(),
"candidates":"id opportunity_ref work_ref evidence_refs outcome value_hypothesis baseline_candidate effort_range cost_range risk dependencies capacity_need alternative criterion_scores score_evidence confidence status".split(),
"gates":"id candidate_ref checks evidence_refs owner critical status reason".split(),
"priority_results":"id candidate_ref gate_state weighted_score rank tier stability why_now why_not opportunity_cost disposition owner status".split(),
"sensitivity_scenarios":"id scenario changed_inputs rank_movements shortlist_change threshold stability trigger owner status".split(),
"portfolio_views":"id view criteria evidence insight constraint owner status".split(),
"decisions":"id decision evidence_refs owner authority status consequence".split(),
"test_cases":"id category requirement_ref setup expected actual evidence status owner".split(),
"risks":"id risk evidence impact control owner residual status".split()}
CRITERIA={"STRATEGIC_FIT","PROBLEM_EVIDENCE","WORKLOAD","VALUE_HYPOTHESIS","DATA_WORKFLOW_READINESS","MEASURABILITY","TIME_TO_LEARNING_REVERSIBILITY","SCALABILITY_REUSE"}
GATE_CHECKS={"SCOPE_OWNER","EVIDENCE_SUFFICIENCY","DATA_RIGHTS","OUTPUT_TESTABILITY","HUMAN_CONTROL","HARM_SECURITY_PRIVACY"}
TESTS={"priority_contract","candidate_trace","gate_before_score","rubric_weight_formula","value_double_count","ranking_recompute","sensitivity_injection"}
REVIEWS={"BUSINESS_PROCESS_OWNER","DATA_SYSTEM_OWNER","RISK_CONTROL_OWNER","VALUE_FINANCE_OWNER","DELIVERY_PEOPLE_OWNER","PORTFOLIO_AUTHORITY"}
RISKS={"SCOPE_SPONSOR_BIAS","EVIDENCE_SCORE_PRECISION","VALUE_ROI_DOUBLE_COUNT","DATA_HUMAN_HARM_GATE","EFFORT_CAPACITY_DEPENDENCY","SENSITIVITY_COMMITMENT_HANDOFF"}
FORBIDDEN_TRUE={"invented_pain","invented_baseline","invented_metric","invented_roi","realized_roi_claimed","unknown_as_zero","gate_averaged_away","weight_changed_without_approval","score_changed_for_sponsor","double_count_hidden","protected_attribute_used","vendor_selected","architecture_committed","budget_approved","people_assigned","work_stopped","ranking_published","ranking_sent","evidence_mutated"}
FORBIDDEN_STATE={"SELECTED","APPROVED","BUDGET_APPROVED","ASSIGNED","WORK_STOPPED","PUBLISHED","SENT","AUTO_APPROVED"}

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
    if x.get("artifact")!="Evidence-Based A.I Use-Case Priority Portfolio Pack": d.append("artifact_name")
    top={
      "priority_contract":"portfolio_id version outcome window scope exclusions sponsor owner approver candidate_register_version candidate_register_hash dod confidentiality action_boundary".split(),
      "scoring_contract":"version formula score_scale weight_total missing_rule tie_rule sensitivity_threshold approved_by input_hash engine_version engine_hash".split(),
      "authority_map":"business_process_owner data_system_owner risk_control_owner value_finance_owner delivery_people_owner portfolio_authority exception_authority selected_set_boundary".split()}
    for sec,fields in top.items():
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
    criterion_ids={o.get("id") for o in x.get("criteria",[]) if isinstance(o,dict)}
    for c in CRITERIA-criterion_ids: d.append(f"missing_criterion:{c}")
    weights={}
    for i,o in enumerate(x.get("criteria",[])):
        w=o.get("weight")
        if not isinstance(w,(int,float)) or w<=0: d.append(f"criteria[{i}].weight")
        else: weights[o.get("id")]=w
        if str(o.get("status","")).upper()!="APPROVED_HUMAN": d.append(f"criteria[{i}].status")
    if abs(sum(weights.values())-100)>1e-9: d.append(f"criteria:weight_sum={sum(weights.values())}")
    computed={}
    for i,o in enumerate(x.get("candidates",[])):
        for r in o.get("evidence_refs",[]):
            if r not in ids["evidence_sources"]: d.append(f"candidates[{i}].evidence_ref:{r}")
        scores=o.get("criterion_scores",{}); refs=o.get("score_evidence",{})
        if set(scores)!=CRITERIA: d.append(f"candidates[{i}].criterion_scores")
        if set(refs)!=CRITERIA: d.append(f"candidates[{i}].score_evidence")
        total=0; numeric=True
        for c in CRITERIA:
            s=scores.get(c)
            if not isinstance(s,(int,float)) or not 0<=s<=5: d.append(f"candidates[{i}].score:{c}"); numeric=False
            elif c in weights: total+=s*weights[c]/5
            for r in refs.get(c,[]) if isinstance(refs.get(c),list) else []:
                if r not in ids["evidence_sources"]: d.append(f"candidates[{i}].score_evidence:{c}:{r}")
        if numeric: computed[o.get("id")]=round(total,4)
        if str(o.get("status","")).upper()!="ELIGIBLE": d.append(f"candidates[{i}].status")
    gate_by={}
    for i,o in enumerate(x.get("gates",[])):
        if o.get("candidate_ref") not in ids["candidates"]: d.append(f"gates[{i}].candidate_ref")
        checks=o.get("checks",[])
        passed={c.get("type") for c in checks if isinstance(c,dict) and c.get("status")=="PASS" and not blank(c.get("evidence"))}
        for g in GATE_CHECKS-passed: d.append(f"gates[{i}].missing_or_fail:{g}")
        for r in o.get("evidence_refs",[]):
            if r not in ids["evidence_sources"]: d.append(f"gates[{i}].evidence_ref:{r}")
        if o.get("critical") is not True or str(o.get("status","")).upper()!="PASS": d.append(f"gates[{i}].critical_status")
        gate_by[o.get("candidate_ref")]=o.get("status")
    ranks=[]
    for i,o in enumerate(x.get("priority_results",[])):
        cid=o.get("candidate_ref")
        if cid not in ids["candidates"]: d.append(f"priority_results[{i}].candidate_ref")
        if str(o.get("gate_state","")).upper()!="PASS" or gate_by.get(cid)!="PASS": d.append(f"priority_results[{i}].gate_state")
        if cid in computed and isinstance(o.get("weighted_score"),(int,float)) and abs(o.get("weighted_score")-computed[cid])>0.01: d.append(f"priority_results[{i}].weighted_score")
        if not isinstance(o.get("rank"),int) or o.get("rank")<1: d.append(f"priority_results[{i}].rank")
        else: ranks.append(o.get("rank"))
        if str(o.get("disposition","")).upper() not in {"SHORTLIST","BACKLOG","DEFER","EXCLUDE"}: d.append(f"priority_results[{i}].disposition")
        if str(o.get("status","")).upper()!="PROPOSED": d.append(f"priority_results[{i}].status")
    if len(ranks)!=len(set(ranks)): d.append("priority_results:duplicate_rank_without_tie")
    for i,o in enumerate(x.get("sensitivity_scenarios",[])):
        if str(o.get("stability","")).upper() not in {"STABLE","CONDITIONAL","UNSTABLE"}: d.append(f"sensitivity_scenarios[{i}].stability")
        if str(o.get("status","")).upper()!="TESTED": d.append(f"sensitivity_scenarios[{i}].status")
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
    state="READY_FOR_HUMAN_PRIORITY_DECISION" if not d and not gaps else "NOT_READY"
    counts={k:len(x.get(k,[])) if isinstance(x.get(k),list) else 0 for k in MIN}; counts.update({"tests_passed":len(passed),"reviews_passed":len(reviewed)})
    print(json.dumps({"state":state,"defect_count":len(d),"review_gap_count":len(gaps),"counts":counts,"defects":d,"review_gaps":gaps},ensure_ascii=False,indent=2))
    return 0 if state.startswith("READY") else 1

if __name__=="__main__":
    if len(sys.argv)!=2: print("usage: evaluate_use_case_prioritization.py fixture.json",file=sys.stderr); sys.exit(2)
    sys.exit(main(sys.argv[1]))
