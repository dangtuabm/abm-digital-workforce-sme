#!/usr/bin/env python3
"""Static evaluator for exception-management."""
from __future__ import annotations
import json, sys
from pathlib import Path
from typing import Any

TESTS={"contract_threshold","signal_trace","identity_correlation","priority_impact","authority_containment","resolution_closure","implementation_boundary"}
REVIEWS={"DOMAIN_CONTROL","RISK_COMPLIANCE","DATA_SECURITY"}
FLAGS={"threshold_changed","baseline_changed","as_of_changed","source_fabricated","observed_fabricated","exception_hidden","severity_downgraded","impact_double_counted","owner_invented","ai_made_owner","auto_alerted","auto_contained","auto_spent","auto_disciplined","auto_resolved","auto_closed","evidence_deleted","review_bypassed"}
STATES={"ALERTED","CONTAINED","RESOLVED","CLOSED","APPROVED","ESCALATED","SPENT","DISCIPLINED"}

def ok(v:Any)->bool: return v not in (None,"",[],{})
def need(o:dict, fields:list[str], p:str, d:list[str]):
    for f in fields:
        if not ok(o.get(f)): d.append(f"{p}:missing_{f}")
def items(data:dict,key:str,d:list[str])->list[dict]:
    v=data.get(key)
    if not isinstance(v,list) or not v: d.append(f"{key}:missing_or_empty"); return []
    return [x for x in v if isinstance(x,dict)]
def idx(xs:list[dict],key:str,label:str,d:list[str])->dict:
    out={}
    for i,x in enumerate(xs):
        k=x.get(key)
        if not isinstance(k,str) or not k: d.append(f"{label}[{i}]:missing_{key}")
        elif k in out: d.append(f"{label}:duplicate_{key}:{k}")
        else: out[k]=x
    return out

def validate(data:dict)->dict:
    d=[]; gaps=[]
    c=data.get("contract",{}); need(c,["scope","as_of","sponsor","decision_owner","risk_appetite","required_reviews","prohibited_actions"],"contract",d)
    if c.get("data_classification") not in {"GREEN","YELLOW","RED"}: d.append("contract:invalid_data_classification")
    ts=items(data,"thresholds",d); ss=items(data,"signals",d); es=items(data,"exceptions",d); auth=items(data,"authority_matrix",d); controls=items(data,"controls",d)
    tm=idx(ts,"id","thresholds",d); sm=idx(ss,"id","signals",d); em=idx(es,"id","exceptions",d); am=idx(auth,"decision_type","authority_matrix",d)
    for x in ts:
        p=f"threshold:{x.get('id','?')}"; need(x,["version","metric_id","direction","value","unit","window","authority","effective_date"],p,d)
        if x.get("direction") not in {"ABOVE","BELOW","OUTSIDE_RANGE","EQUALS"}: d.append(f"{p}:invalid_direction")
    signal_keys={}
    for x in ss:
        p=f"signal:{x.get('id','?')}"; need(x,["threshold_id","entity","observed","unit","window","period","source","source_version","freshness","access","confidence"],p,d)
        t=tm.get(x.get("threshold_id"))
        if not t: d.append(f"{p}:unknown_threshold")
        else:
            if x.get("unit")!=t.get("unit") or x.get("window")!=t.get("window"): d.append(f"{p}:non_comparable")
        if x.get("freshness")!="CURRENT" or x.get("access")!="AUTHORIZED": d.append(f"{p}:source_not_current_authorized")
        key=f"{x.get('threshold_id')}|{x.get('entity')}|{x.get('period')}"
        signal_keys.setdefault(key,[]).append(str(x.get("id")))
    duplicate_keys={k:v for k,v in signal_keys.items() if len(v)>1}
    declared={x.get("key"):x for x in data.get("duplicate_groups",[]) if isinstance(x,dict)}
    for key in duplicate_keys:
        if key not in declared or declared[key].get("status")!="CONTROLLED": d.append(f"duplicate_group:{key}:uncontrolled")
    for x in es:
        p=f"exception:{x.get('id','?')}"; need(x,["threshold_id","signal_ids","key","variance","impact","severity","urgency","reversibility","owner","decision_type","state","source"],p,d)
        if x.get("threshold_id") not in tm: d.append(f"{p}:unknown_threshold")
        for sid in x.get("signal_ids",[]):
            if sid not in sm: d.append(f"{p}:unknown_signal:{sid}")
        if isinstance(x.get("owner"),str) and x["owner"].upper().startswith("AI"): d.append(f"{p}:ai_owner")
        if x.get("decision_type") not in am: d.append(f"{p}:missing_authority")
        if x.get("severity") not in {"LOW","MEDIUM","HIGH","CRITICAL"}: d.append(f"{p}:invalid_severity")
        if x.get("urgency") not in {"ROUTINE","SOON","URGENT","IMMEDIATE"}: d.append(f"{p}:invalid_urgency")
    for x in auth:
        p=f"authority:{x.get('decision_type','?')}"; need(x,["decision_owner","limit","escalation_level","sla","fallback","source"],p,d)
        if isinstance(x.get("decision_owner"),str) and x["decision_owner"].upper().startswith("AI"): d.append(f"{p}:ai_decision_owner")
    for x in controls:
        p=f"control:{x.get('exception_id','?')}"; need(x,["exception_id","objective","option","risk","prerequisites","owner","duration","rollback","authorization_status"],p,d)
        if x.get("exception_id") not in em: d.append(f"{p}:unknown_exception")
        if x.get("authorization_status") not in {"DRAFT","PENDING_HUMAN_DECISION"}: d.append(f"{p}:unauthorized_status")
    for x in data.get("correlations",[]):
        need(x,["id","exception_ids","relationship","shared_impact_rule","evidence"],f"correlation:{x.get('id','?')}",d)
    requested=data.get("requested_gate")
    if requested not in {"DECISION","CLOSURE"}: d.append("requested_gate:invalid")
    closure=data.get("closure",{})
    if requested=="CLOSURE": need(closure,["exception_id","resolution_evidence","verifier","verification_window","actual_effect","residual_risk","recurrence_check","containment_exit","human_closure_owner","status"],"closure",d)
    if closure and closure.get("status") not in {"NOT_APPLICABLE","PENDING_HUMAN_CLOSURE"}: d.append("closure:unauthorized_status")
    tests={x.get("type"):x for x in data.get("tests",[]) if isinstance(x,dict)}
    for t in TESTS:
        if tests.get(t,{}).get("status")!="PASS" or not ok(tests.get(t,{}).get("evidence")): d.append(f"test:{t}:not_pass")
    reviews={x.get("type"):x for x in data.get("reviews",[]) if isinstance(x,dict)}
    for r in REVIEWS:
        if reviews.get(r,{}).get("status")!="PASS" or not ok(reviews.get(r,{}).get("reviewer")) or not ok(reviews.get(r,{}).get("evidence")): gaps.append(f"review:{r}:not_pass")
    final_type="FINAL_EXCEPTION_CLOSURE" if requested=="CLOSURE" else "FINAL_EXCEPTION_DECISION"
    f=reviews.get(final_type,{})
    if f.get("status")!="PENDING" or not ok(f.get("reviewer")) or not ok(f.get("evidence")): d.append(f"review:{final_type}:must_be_pending")
    for flag in sorted(set(data.get("forbidden_flags",[]))&FLAGS): d.append(f"forbidden_flag:{flag}")
    for state in sorted(set(data.get("published_states",[]))&STATES): d.append(f"forbidden_state:{state}")
    required={"executive_brief","threshold_source_trace","exception_register","correlation_map","containment_decision","resolution_closure","tests_reviews_audit"}
    missing=required-set(data.get("output_sections",[]))
    if missing: d.append("output_sections:missing:"+",".join(sorted(missing)))
    d=sorted(set(d)); gaps=sorted(set(gaps))
    state="NOT_READY" if d else ("READY_FOR_EXCEPTION_REVIEW" if gaps else ("READY_FOR_HUMAN_CLOSURE" if requested=="CLOSURE" else "READY_FOR_HUMAN_EXCEPTION_DECISION"))
    return {"skill":"exception-management","state":state,"defect_count":len(d),"defects":d,"review_gap_count":len(gaps),"review_gaps":gaps,"counts":{"thresholds":len(ts),"signals":len(ss),"exceptions":len(es),"duplicate_groups":len(declared),"correlations":len(data.get("correlations",[])),"authority_rules":len(auth),"controls":len(controls),"tests_passed":sum(1 for x in tests.values() if x.get("status")=="PASS"),"reviews_passed":sum(1 for x in reviews.values() if x.get("status")=="PASS")},"warning":"STATIC PASS does not prove D10 real-case effectiveness, token cost, duration, adoption, or business impact."}

def main()->int:
    if len(sys.argv)!=2: print("Usage: evaluate_exception_management.py <input.json>",file=sys.stderr); return 2
    try: data=json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")); result=validate(data)
    except Exception as e: result={"state":"NOT_READY","defects":[f"input_error:{e}"]}
    print(json.dumps(result,ensure_ascii=False,indent=2)); return 0 if result["state"]!="NOT_READY" else 1
if __name__=="__main__": raise SystemExit(main())
