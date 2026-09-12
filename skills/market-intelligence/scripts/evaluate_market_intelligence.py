#!/usr/bin/env python3
"""Static evaluator for market-intelligence."""
from __future__ import annotations
import json,sys
from pathlib import Path
from typing import Any
TESTS={"mandate_boundary","source_claim_trace","sizing_reconciliation","entity_event_price","signal_scenario","legal_rights","decision_boundary"}
FLAGS={"boundary_changed","as_of_changed","source_fabricated","source_omitted","rights_bypassed","paywall_bypassed","confidential_data_used","personal_profiled","rumor_as_fact","company_claim_verified","contradiction_hidden","entity_misresolved","market_share_fabricated","growth_fabricated","price_misnormalized","currency_mixed","base_year_mixed","denominator_hidden","double_counted","sample_overgeneralized","certainty_inflated","collusion_enabled","price_fixing_enabled","auto_published","auto_priced","auto_invested","auto_entered","auto_exited","auto_acquired","competitor_contacted"}
STATES={"PUBLISHED","PRICED","INVESTED","ENTERED","EXITED","ACQUIRED","CONTACTED_COMPETITOR","APPROVED"}
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
    d=[];g=[];m=x.get("mandate",{});need(m,["scope","as_of","decision_questions","decision_owner","users","confidentiality","prohibited_actions","required_reviews"],"mandate",d)
    b=x.get("market_definition",{});need(b,["customer_job","category","substitutes","geography","channels","period","currency","base_year","inclusions","exclusions"],"market_definition",d)
    tax=rows(x,"taxonomy",d);src=rows(x,"sources",d);cl=rows(x,"claims",d);est=rows(x,"estimates",d);comp=rows(x,"competitors",d);ev=rows(x,"events",d);sig=rows(x,"signals",d);scn=rows(x,"scenarios",d);dec=rows(x,"decision_implications",d)
    sm=idx(src,"id","sources",d);cm=idx(comp,"id","competitors",d);idx(cl,"id","claims",d);idx(est,"id","estimates",d);idx(ev,"id","events",d);idx(sig,"id","signals",d);idx(scn,"id","scenarios",d)
    for i,a in enumerate(tax):need(a,["type","canonical_id","name","aliases","definition"],f"taxonomy:{i}",d)
    for a in src:
        p=f"source:{a.get('id','?')}";need(a,["locator","publisher","type","tier","published_date","observed_date","access","rights","freshness","independence","version_hash"],p,d)
        if a.get("access")!="AUTHORIZED"or a.get("rights")!="PERMITTED"or a.get("freshness")!="CURRENT":d.append(f"{p}:not_current_permitted")
    for a in cl:
        p=f"claim:{a.get('id','?')}";need(a,["text","claim_type","entity_id","period","geography","source_ids","confidence","contradiction_status"],p,d)
        if a.get("claim_type")not in{"FACT","ESTIMATE","HYPOTHESIS","COMPANY_CLAIM"}:d.append(f"{p}:invalid_type")
        for s in a.get("source_ids",[]):
            if s not in sm:d.append(f"{p}:unknown_source:{s}")
    if len(est)<2:d.append("estimates:two_methods_required")
    methods=set()
    for a in est:
        p=f"estimate:{a.get('id','?')}";need(a,["method","formula","inputs","source_ids","low","base","high","currency","base_year","denominator","sensitivity","reconciliation"],p,d);methods.add(a.get("method"))
        if not(a.get("currency")==b.get("currency")and a.get("base_year")==b.get("base_year")):d.append(f"{p}:currency_or_base_year_mismatch")
        if all(isinstance(a.get(k),(int,float))for k in("low","base","high"))and not a["low"]<=a["base"]<=a["high"]:d.append(f"{p}:invalid_range")
        for s in a.get("source_ids",[]):
            if s not in sm:d.append(f"{p}:unknown_source:{s}")
    if not{"TOP_DOWN","BOTTOM_UP"}.issubset(methods):d.append("estimates:top_down_bottom_up_missing")
    for a in comp:
        p=f"competitor:{a.get('id','?')}";need(a,["canonical_name","aliases","parent","offers","price_basis","channels","capabilities","source_ids","claimed_vs_verified"],p,d)
    for a in ev:
        p=f"event:{a.get('id','?')}";need(a,["entity_id","event_type","event_date","published_date","source_ids","syndication_group","claimed_vs_verified","implication"],p,d)
        if a.get("entity_id")not in cm:d.append(f"{p}:unknown_entity")
    for a in sig:
        p=f"signal:{a.get('id','?')}";need(a,["observation","direction","strength","persistence","breadth","indicator_type","alternatives","source_ids","confidence"],p,d)
    for a in scn:
        p=f"scenario:{a.get('id','?')}";need(a,["name","drivers","assumptions","low","base","high","trigger","indicator","cadence","owner"],p,d)
    for i,a in enumerate(dec):need(a,["decision_question","implication","validation_action","no_regret_move","owner","status"],f"decision:{i}",d)
    for i,a in enumerate(dec):
        if a.get("status")not in{"DRAFT","PENDING_HUMAN_DECISION"}:d.append(f"decision:{i}:unauthorized_status")
    tests={a.get("type"):a for a in x.get("tests",[])if isinstance(a,dict)}
    for t in TESTS:
        if tests.get(t,{}).get("status")!="PASS"or not ok(tests.get(t,{}).get("evidence")):d.append(f"test:{t}:not_pass")
    reviews={a.get("type"):a for a in x.get("reviews",[])if isinstance(a,dict)}
    for r in{"MARKET_DOMAIN","RESEARCH_DATA","FINANCE_SIZING","LEGAL_COMPETITION"}:
        if reviews.get(r,{}).get("status")!="PASS"or not ok(reviews.get(r,{}).get("reviewer"))or not ok(reviews.get(r,{}).get("evidence")):g.append(f"review:{r}:not_pass")
    f=reviews.get("FINAL_HUMAN_MARKET_DECISION",{})
    if f.get("status")!="PENDING"or not ok(f.get("reviewer"))or not ok(f.get("evidence")):d.append("review:FINAL_HUMAN_MARKET_DECISION:must_be_pending")
    for a in sorted(set(x.get("forbidden_flags",[]))&FLAGS):d.append(f"forbidden_flag:{a}")
    for a in sorted(set(x.get("published_states",[]))&STATES):d.append(f"forbidden_state:{a}")
    req={"executive_decision_brief","market_boundary_taxonomy","source_claim_ledger","market_size_reconciliation","segment_competitor_event","signal_scenario_watch","limitations_reviews_audit"};miss=req-set(x.get("output_sections",[]))
    if miss:d.append("output_sections:missing:"+",".join(sorted(miss)))
    d=sorted(set(d));g=sorted(set(g));state="NOT_READY"if d else("READY_FOR_INTELLIGENCE_REVIEW"if g else"READY_FOR_HUMAN_MARKET_DECISION")
    return{"skill":"market-intelligence","state":state,"defect_count":len(d),"defects":d,"review_gap_count":len(g),"review_gaps":g,"counts":{"taxonomy":len(tax),"sources":len(src),"claims":len(cl),"estimates":len(est),"competitors":len(comp),"events":len(ev),"signals":len(sig),"scenarios":len(scn),"decisions":len(dec),"tests_passed":sum(1 for a in tests.values()if a.get("status")=="PASS"),"reviews_passed":sum(1 for a in reviews.values()if a.get("status")=="PASS")},"warning":"STATIC PASS does not prove D10 real-market accuracy, forecast calibration, token cost, duration, adoption, or business impact."}
def main()->int:
    if len(sys.argv)!=2:print("Usage: evaluate_market_intelligence.py <input.json>",file=sys.stderr);return 2
    try:r=validate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    except Exception as e:r={"state":"NOT_READY","defects":[f"input_error:{e}"]}
    print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["state"]!="NOT_READY"else 1
if __name__=="__main__":raise SystemExit(main())
