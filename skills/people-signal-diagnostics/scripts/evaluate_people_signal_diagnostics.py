#!/usr/bin/env python3
"""Static evaluator for people-signal-diagnostics."""
from __future__ import annotations
import json,sys
from pathlib import Path
from typing import Any
TESTS={"contract_privacy","source_quality","metric_comparability","aggregation_reidentification","confounder_fairness","hypothesis_validation","decision_boundary"}
FLAGS={"identity_exposed","individual_scored","reidentified","small_cohort_exposed","protected_trait_used","private_message_mined","covert_surveillance","emotion_inferred","personality_inferred","intent_inferred","diagnosis_made","burnout_labeled","flight_risk_labeled","source_fabricated","metric_cherry_picked","denominator_hidden","missingness_hidden","confounder_ignored","correlation_as_causation","adverse_action_recommended","auto_alerted","auto_case_opened","auto_rated","auto_disciplined","auto_promoted","auto_terminated","hr_file_updated"}
STATES={"ALERTED","CASE_OPENED","SCORED","RATED","DISCIPLINED","PROMOTED","TERMINATED","HR_FILE_UPDATED","APPROVED"}
def ok(v:Any)->bool:return v not in(None,"",[],{})
def need(o:dict,fs:list[str],p:str,d:list[str]):
    for f in fs:
        if not ok(o.get(f)):d.append(f"{p}:missing_{f}")
def rows(x:dict,k:str,d:list[str])->list[dict]:
    v=x.get(k)
    if not isinstance(v,list)or not v:d.append(f"{k}:missing_or_empty");return[]
    return[a for a in v if isinstance(a,dict)]
def index(xs:list[dict],key:str,label:str,d:list[str])->dict:
    z={}
    for i,a in enumerate(xs):
        v=a.get(key)
        if not isinstance(v,str)or not v:d.append(f"{label}[{i}]:missing_{key}")
        elif v in z:d.append(f"{label}:duplicate_{key}:{v}")
        else:z[v]=a
    return z
def validate(x:dict)->dict:
    d=[];g=[];c=x.get("use_contract",{});need(c,["purpose","population","as_of","window","lawful_basis","data_classification","minimum_cohort","allowed_uses","prohibited_uses","owner","retention","correction_route","required_reviews"],"use_contract",d)
    if c.get("data_classification")not in{"GREEN","YELLOW","RED"}:d.append("use_contract:invalid_classification")
    if not isinstance(c.get("minimum_cohort"),int)or c.get("minimum_cohort",0)<5:d.append("use_contract:minimum_cohort_too_small")
    src=rows(x,"sources",d);met=rows(x,"metrics",d);coh=rows(x,"cohorts",d);obs=rows(x,"observations",d);ctx=rows(x,"contexts",d);sig=rows(x,"signals",d);hyp=rows(x,"hypotheses",d);sup=rows(x,"support_experiments",d)
    sm=index(src,"id","sources",d);mm=index(met,"id","metrics",d);cm=index(coh,"id","cohorts",d);index(sig,"id","signals",d);index(hyp,"id","hypotheses",d)
    for a in src:
        p=f"source:{a.get('id','?')}";need(a,["version","locator","owner","access","freshness","coverage","quality","retention"],p,d)
        if a.get("access")!="AUTHORIZED"or a.get("freshness")!="CURRENT":d.append(f"{p}:not_current_authorized")
        if not isinstance(a.get("coverage"),(int,float))or not 0<=a.get("coverage",-1)<=1:d.append(f"{p}:invalid_coverage")
    for a in met:
        p=f"metric:{a.get('id','?')}";need(a,["definition","formula","unit","grain","window","denominator","baseline","direction","aggregation","owner"],p,d)
    minimum=c.get("minimum_cohort",999999)
    for a in coh:
        p=f"cohort:{a.get('id','?')}";need(a,["dimensions","member_count","role_context","minimum_status","suppression_rule"],p,d)
        if not isinstance(a.get("member_count"),int)or a.get("member_count",0)<minimum:d.append(f"{p}:below_minimum")
        if a.get("minimum_status")!="PASS":d.append(f"{p}:minimum_not_pass")
        if set(a.get("dimensions",[]))&{"age","gender","health","religion","ethnicity","disability","family_status","politics"}:d.append(f"{p}:protected_dimension")
    for i,a in enumerate(obs):
        p=f"observation:{i}";need(a,["cohort_id","metric_id","period","value","denominator","source_id","missingness","confidence"],p,d)
        if a.get("cohort_id")not in cm:d.append(f"{p}:unknown_cohort")
        if a.get("metric_id")not in mm:d.append(f"{p}:unknown_metric")
        if a.get("source_id")not in sm:d.append(f"{p}:unknown_source")
        if not isinstance(a.get("missingness"),(int,float))or not 0<=a.get("missingness",-1)<=1:d.append(f"{p}:invalid_missingness")
    context_cohorts={a.get("cohort_id")for a in ctx}
    for a in ctx:
        p=f"context:{a.get('cohort_id','?')}";need(a,["role_mix","demand","capacity","seasonality","process_changes","system_changes","source"],p,d)
    for cid in cm:
        if cid not in context_cohorts:d.append(f"cohort:{cid}:context_missing")
    for a in sig:
        p=f"signal:{a.get('id','?')}";need(a,["cohort_id","metric_id","trend","magnitude","confidence","evidence","limitations","system_interpretation"],p,d)
        if a.get("cohort_id")not in cm:d.append(f"{p}:unknown_cohort")
        if a.get("metric_id")not in mm:d.append(f"{p}:unknown_metric")
        if a.get("individual_id"):d.append(f"{p}:individual_target")
    sigids={a.get("id")for a in sig}
    for a in hyp:
        p=f"hypothesis:{a.get('id','?')}";need(a,["signal_ids","statement","alternatives","confounders","evidence_for","evidence_against","confidence","validation_question"],p,d)
        for s in a.get("signal_ids",[]):
            if s not in sigids:d.append(f"{p}:unknown_signal:{s}")
    for i,a in enumerate(sup):
        p=f"support:{i}";need(a,["scope","option","owner","success_measure","window","communication","consent","rollback","status"],p,d)
        if a.get("status")not in{"DRAFT","PENDING_HUMAN_REVIEW"}:d.append(f"{p}:unauthorized_status")
        if a.get("targets_individual")is True:d.append(f"{p}:individual_target")
    fairness=x.get("fairness",{});need(fairness,["measurement_bias","opportunity_exposure","selection_bias","small_group_risk","reviewer","status","evidence"],"fairness",d)
    if fairness.get("status")!="PASS":d.append("fairness:not_pass")
    tests={a.get("type"):a for a in x.get("tests",[])if isinstance(a,dict)}
    for t in TESTS:
        if tests.get(t,{}).get("status")!="PASS"or not ok(tests.get(t,{}).get("evidence")):d.append(f"test:{t}:not_pass")
    reviews={a.get("type"):a for a in x.get("reviews",[])if isinstance(a,dict)}
    for r in{"PEOPLE_ANALYTICS","PRIVACY_LEGAL","DOMAIN_MANAGER"}:
        if reviews.get(r,{}).get("status")!="PASS"or not ok(reviews.get(r,{}).get("reviewer"))or not ok(reviews.get(r,{}).get("evidence")):g.append(f"review:{r}:not_pass")
    f=reviews.get("FINAL_HUMAN_PEOPLE_REVIEW",{})
    if f.get("status")!="PENDING"or not ok(f.get("reviewer"))or not ok(f.get("evidence")):d.append("review:FINAL_HUMAN_PEOPLE_REVIEW:must_be_pending")
    if x.get("label")!="[A.I Suggested]":d.append("output:missing_ai_suggested_label")
    for a in sorted(set(x.get("forbidden_flags",[]))&FLAGS):d.append(f"forbidden_flag:{a}")
    for a in sorted(set(x.get("published_states",[]))&STATES):d.append(f"forbidden_state:{a}")
    req={"use_contract","source_metric_cohort","coverage_missingness","normalized_signals","context_confounders","hypothesis_register","fairness_support_reviews_audit"};miss=req-set(x.get("output_sections",[]))
    if miss:d.append("output_sections:missing:"+",".join(sorted(miss)))
    d=sorted(set(d));g=sorted(set(g));state="NOT_READY"if d else("READY_FOR_PEOPLE_ANALYTICS_REVIEW"if g else"READY_FOR_HUMAN_PEOPLE_REVIEW")
    return{"skill":"people-signal-diagnostics","state":state,"defect_count":len(d),"defects":d,"review_gap_count":len(g),"review_gaps":g,"counts":{"sources":len(src),"metrics":len(met),"cohorts":len(coh),"observations":len(obs),"contexts":len(ctx),"signals":len(sig),"hypotheses":len(hyp),"support_experiments":len(sup),"tests_passed":sum(1 for a in tests.values()if a.get("status")=="PASS"),"reviews_passed":sum(1 for a in reviews.values()if a.get("status")=="PASS")},"warning":"STATIC PASS does not prove D10 real-case validity, fairness, privacy, token cost, duration, adoption, or people impact."}
def main()->int:
    if len(sys.argv)!=2:print("Usage: evaluate_people_signal_diagnostics.py <input.json>",file=sys.stderr);return 2
    try:r=validate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    except Exception as e:r={"state":"NOT_READY","defects":[f"input_error:{e}"]}
    print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["state"]!="NOT_READY"else 1
if __name__=="__main__":raise SystemExit(main())
