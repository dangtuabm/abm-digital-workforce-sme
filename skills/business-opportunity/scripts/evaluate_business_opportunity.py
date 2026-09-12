#!/usr/bin/env python3
"""Static evaluator for business-opportunity."""
from __future__ import annotations
import json,sys
from pathlib import Path
from typing import Any
TESTS={"mandate_evidence","thesis_fit","assumption_priority","economics_risk","experiment_gate","rights_compliance","decision_boundary"}
CATS={"DESIRABILITY","FEASIBILITY","VIABILITY","DEFENSIBILITY","COMPLIANCE"}
FLAGS={"evidence_fabricated","demand_fabricated","pain_fabricated","wtp_fabricated","market_size_fabricated","price_fabricated","cost_fabricated","margin_fabricated","capability_fabricated","partner_interest_fabricated","validation_result_fabricated","rights_bypassed","ip_misused","sensitive_data_misused","confirmation_bias","contradiction_hidden","cannibalization_hidden","dependency_hidden","risk_hidden","sunk_cost_escalated","criteria_changed","failed_evidence_deleted","deceptive_test","auto_funded","auto_contacted","auto_built","auto_priced","auto_contracted","auto_launched","auto_scaled"}
STATES={"FUNDED","CONTACTED","BUILT","PRICED","CONTRACTED","LAUNCHED","SCALED","APPROVED"}
def ok(v:Any)->bool:return v not in(None,"",[],{})
def need(o:dict,fs:list[str],p:str,d:list[str]):
    for f in fs:
        if not ok(o.get(f)):d.append(f"{p}:missing_{f}")
def rows(x:dict,k:str,d:list[str])->list[dict]:
    v=x.get(k)
    if not isinstance(v,list)or not v:d.append(f"{k}:missing_or_empty");return[]
    return[a for a in v if isinstance(a,dict)]
def idx(xs:list[dict],key:str,label:str,d:list[str])->dict:
    z={}
    for i,a in enumerate(xs):
        v=a.get(key)
        if not isinstance(v,str)or not v:d.append(f"{label}[{i}]:missing_{key}")
        elif v in z:d.append(f"{label}:duplicate_{key}:{v}")
        else:z[v]=a
    return z
def validate(x:dict)->dict:
    d=[];g=[];m=x.get("mandate",{});need(m,["scope","as_of","strategy_objectives","decision_question","decision_owner","risk_limit","capital_limit","confidentiality","prohibited_actions","required_reviews"],"mandate",d)
    ev=rows(x,"evidence",d);th=rows(x,"theses",d);ass=rows(x,"assumptions",d);eco=rows(x,"economics",d);risk=rows(x,"risks",d);opt=rows(x,"options",d);exp=rows(x,"experiments",d);stg=rows(x,"stages",d)
    em=idx(ev,"id","evidence",d);tm=idx(th,"id","theses",d);am=idx(ass,"id","assumptions",d);idx(exp,"id","experiments",d)
    for a in ev:
        p=f"evidence:{a.get('id','?')}";need(a,["source","version","date","rights","freshness","evidence_type","statement","confidence","contradiction_status"],p,d)
        if a.get("rights")!="AUTHORIZED"or a.get("freshness")!="CURRENT":d.append(f"{p}:not_authorized_current")
        if a.get("evidence_type")not in{"FACT","ESTIMATE","HYPOTHESIS"}:d.append(f"{p}:invalid_type")
    for a in th:
        p=f"thesis:{a.get('id','?')}";need(a,["opportunity_type","target_customer","job_problem","frequency_severity","current_alternative","current_cost","value_hypothesis","differentiation","right_to_win","revenue_logic","cost_logic","strategic_fit","evidence_ids"],p,d)
        for e in a.get("evidence_ids",[]):
            if e not in em:d.append(f"{p}:unknown_evidence:{e}")
    cats_by={k:set()for k in tm}
    for a in ass:
        p=f"assumption:{a.get('id','?')}";need(a,["opportunity_id","category","statement","evidence_for","evidence_against","confidence","consequence","testability","owner"],p,d)
        if a.get("opportunity_id")not in tm:d.append(f"{p}:unknown_opportunity")
        elif a.get("category")in CATS:cats_by[a["opportunity_id"]].add(a["category"])
        else:d.append(f"{p}:invalid_category")
    for oid,cats in cats_by.items():
        if cats!=CATS:d.append(f"thesis:{oid}:assumption_categories_incomplete")
    for i,a in enumerate(eco):
        p=f"economics:{i}";need(a,["opportunity_id","formula","inputs","source_ids","low","base","high","currency","base_year","horizon","sensitivity","downside","capital_exposure","capacity_exposure"],p,d)
        if a.get("opportunity_id")not in tm:d.append(f"{p}:unknown_opportunity")
        if all(isinstance(a.get(k),(int,float))for k in("low","base","high"))and not a["low"]<=a["base"]<=a["high"]:d.append(f"{p}:invalid_range")
    risk_types=set()
    for i,a in enumerate(risk):
        p=f"risk:{i}";need(a,["opportunity_id","risk_type","statement","likelihood","impact","trigger","mitigation","contingency","owner","evidence"],p,d);risk_types.add(a.get("risk_type"))
    for required in{"MARKET_CUSTOMER","CAPABILITY_DELIVERY","FINANCE","LEGAL_DATA_IP","CANNIBALIZATION_DEPENDENCY"}:
        if required not in risk_types:d.append(f"risks:missing_type:{required}")
    for i,a in enumerate(opt):need(a,["opportunity_id","option","trade_off","prerequisites","reversibility","risk","status"],f"option:{i}",d)
    for a in exp:
        p=f"experiment:{a.get('id','?')}";need(a,["opportunity_id","assumption_id","method","sample","consent_rights","metric","baseline","success_criteria","kill_criteria","max_time","max_budget","owner","evidence_capture","stop_rule","status"],p,d)
        if a.get("opportunity_id")not in tm:d.append(f"{p}:unknown_opportunity")
        if a.get("assumption_id")not in am:d.append(f"{p}:unknown_assumption")
        if a.get("status")not in{"DRAFT","PENDING_HUMAN_APPROVAL"}:d.append(f"{p}:unauthorized_status")
    for a in stg:
        p=f"stage:{a.get('opportunity_id','?')}";need(a,["opportunity_id","stage","evidence_achieved","evidence_gaps","capital_exposure","options","recommendation","decision_owner","deadline","status"],p,d)
        if a.get("opportunity_id")not in tm:d.append(f"{p}:unknown_opportunity")
        if a.get("status")not in{"DRAFT","PENDING_HUMAN_DECISION"}:d.append(f"{p}:unauthorized_status")
    tests={a.get("type"):a for a in x.get("tests",[])if isinstance(a,dict)}
    for t in TESTS:
        if tests.get(t,{}).get("status")!="PASS"or not ok(tests.get(t,{}).get("evidence")):d.append(f"test:{t}:not_pass")
    reviews={a.get("type"):a for a in x.get("reviews",[])if isinstance(a,dict)}
    for r in{"STRATEGY_PORTFOLIO","CUSTOMER_MARKET","FINANCE_ECONOMICS","DELIVERY_CAPABILITY","LEGAL_DATA_IP"}:
        if reviews.get(r,{}).get("status")!="PASS"or not ok(reviews.get(r,{}).get("reviewer"))or not ok(reviews.get(r,{}).get("evidence")):g.append(f"review:{r}:not_pass")
    f=reviews.get("FINAL_HUMAN_OPPORTUNITY_DECISION",{})
    if f.get("status")!="PENDING"or not ok(f.get("reviewer"))or not ok(f.get("evidence")):d.append("review:FINAL_HUMAN_OPPORTUNITY_DECISION:must_be_pending")
    for a in sorted(set(x.get("forbidden_flags",[]))&FLAGS):d.append(f"forbidden_flag:{a}")
    for a in sorted(set(x.get("published_states",[]))&STATES):d.append(f"forbidden_state:{a}")
    req={"mandate_evidence","opportunity_theses","fit_assumption_map","economics_risk","options_experiments","stage_decision","reviews_audit"};miss=req-set(x.get("output_sections",[]))
    if miss:d.append("output_sections:missing:"+",".join(sorted(miss)))
    d=sorted(set(d));g=sorted(set(g));state="NOT_READY"if d else("READY_FOR_OPPORTUNITY_REVIEW"if g else"READY_FOR_HUMAN_OPPORTUNITY_DECISION")
    return{"skill":"business-opportunity","state":state,"defect_count":len(d),"defects":d,"review_gap_count":len(g),"review_gaps":g,"counts":{"evidence":len(ev),"theses":len(th),"assumptions":len(ass),"economics":len(eco),"risks":len(risk),"options":len(opt),"experiments":len(exp),"stages":len(stg),"tests_passed":sum(1 for a in tests.values()if a.get("status")=="PASS"),"reviews_passed":sum(1 for a in reviews.values()if a.get("status")=="PASS")},"warning":"STATIC PASS does not prove D10 real-opportunity validity, economics accuracy, token cost, duration, adoption, or business impact."}
def main()->int:
    if len(sys.argv)!=2:print("Usage: evaluate_business_opportunity.py <input.json>",file=sys.stderr);return 2
    try:r=validate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    except Exception as e:r={"state":"NOT_READY","defects":[f"input_error:{e}"]}
    print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["state"]!="NOT_READY"else 1
if __name__=="__main__":raise SystemExit(main())
