#!/usr/bin/env python3
"""Deterministic static gate for an Executive Operating Brief."""
from __future__ import annotations
import argparse,json
from collections import Counter
from pathlib import Path
from typing import Any,Iterable

TESTS={"source_freshness","metric_exception","critical_front_page_coverage","decision_recommendation","bad_news_unknown_integrity","privacy_distribution","approval_delivery_boundary"}
REVIEWS={"SOURCE_OWNER","OPERATING_OWNER","EDITORIAL","FINAL_BRIEF"}
SEVERITY={"LOW":1,"MEDIUM":2,"HIGH":3,"CRITICAL":4}; TIERS={"NOW","TODAY","MONITOR","APPENDIX"}
FORBIDDEN={"fabricated_signal","hidden_bad_news","downgraded_severity","stale_as_current","vanity_metric","false_approval","false_decision","false_delivery"}
def load_json(p:Path)->dict[str,Any]:
    with p.open("r",encoding="utf-8-sig") as f:d=json.load(f)
    if not isinstance(d,dict):raise ValueError("Root JSON must be object")
    return d
def blank(v:Any)->bool:return v is None or v=="" or v==[] or v=={}
def req(o:dict[str,Any],fs:Iterable[str],l:str,e:list[str])->None:
    for f in fs:
        if f not in o or blank(o[f]):e.append(f"{l}: missing {f}")
def ids(xs:list[dict[str,Any]],f:str,l:str,e:list[str])->set[str]:
    vs=[str(x.get(f,"")).strip() for x in xs];ds=[v for v,n in Counter(vs).items() if v and n>1]
    if any(not v for v in vs):e.append(f"{l}: blank {f}")
    if ds:e.append(f"{l}: duplicate {f}: {', '.join(ds)}")
    return {v for v in vs if v}
def refs(v:Any,valid:set[str],l:str,f:str,e:list[str])->set[str]:
    if not isinstance(v,list) or not v:e.append(f"{l}: invalid {f}");return set()
    s={str(x) for x in v};u=sorted(s-valid)
    if u:e.append(f"{l}: unknown {f}: {', '.join(u)}")
    return s
def number(v:Any)->float|None:
    return float(v) if isinstance(v,(int,float)) and not isinstance(v,bool) else None
def evaluate(d:dict[str,Any])->dict[str,Any]:
    e=[];w=[];c=d.get("contract") or {};req(c,("brief_id","version","as_of","snapshot_hash","timezone","horizon_hours","audiences","owner","final_approver","max_front_page_items","freshness_sla_hours","classification","required_reviews","prohibited_actions"),"contract",e)
    ss=d.get("sources") or [];sids=ids(ss,"source_id","sources",e);active=set();stale=set()
    for i,x in enumerate(ss):
        l=f"source[{i}]";req(x,("source_id","title","version","locator","owner","observed_at","age_hours","classification"),l,e)
        if x.get("active") is True:active.add(str(x.get("source_id")))
        age=number(x.get("age_hours"));sla=number(x.get("freshness_sla_hours",c.get("freshness_sla_hours")))
        if age is None or sla is None:e.append(f"{l}: age/SLA must be numeric")
        elif age>sla:stale.add(str(x.get("source_id")))
    sigs=d.get("signals") or [];sigids=ids(sigs,"signal_id","signals",e);critical=set();forbidden=0
    for i,x in enumerate(sigs):
        l=f"signal[{i}]";req(x,("signal_id","signal_type","statement","severity","tier","impact","owner","due_at","status","source_refs","confidence"),l,e);r=refs(x.get("source_refs"),active,l,"source_refs",e)
        if x.get("severity") not in SEVERITY or x.get("tier") not in TIERS:e.append(f"{l}: invalid severity/tier")
        if x.get("severity")=="CRITICAL":critical.add(str(x.get("signal_id")))
        if r&stale and x.get("status")=="CURRENT":e.append(f"{l}: stale source used as current")
        for f in FORBIDDEN:
            if x.get(f) is True:forbidden+=1;e.append(f"{l}: forbidden flag {f}")
    metrics=d.get("metric_exceptions") or [];mids=ids(metrics,"exception_id","metric_exceptions",e);metric_defects=0
    for i,x in enumerate(metrics):
        l=f"metric[{i}]";req(x,("exception_id","metric","definition","actual","threshold","direction","denominator","window","source_refs","owner","reported_breach"),l,e);refs(x.get("source_refs"),active,l,"source_refs",e)
        a,t=number(x.get("actual")),number(x.get("threshold"));direction=x.get("direction")
        if a is None or t is None or direction not in {"ABOVE","BELOW"}:metric_defects+=1;e.append(f"{l}: invalid actual/threshold/direction");continue
        breach=a>t if direction=="ABOVE" else a<t
        if breach is not x.get("reported_breach"):metric_defects+=1;e.append(f"{l}: reported_breach mismatch")
    decisions=d.get("decision_requests") or [];dids=ids(decisions,"decision_id","decision_requests",e);unauthorized=0
    for i,x in enumerate(decisions):
        l=f"decision[{i}]";req(x,("decision_id","question","options","recommendation","evidence_refs","deadline","owner","consequence_of_delay","reversible","approval_status"),l,e);refs(x.get("evidence_refs"),active,l,"evidence_refs",e)
        if not isinstance(x.get("options"),list) or len(x.get("options",[]))<2:e.append(f"{l}: at least two options required")
        if x.get("approval_status") in {"APPROVED","DECIDED","SENT","DELIVERED"}:unauthorized+=1;e.append(f"{l}: forbidden approval/delivery state")
    fp=d.get("front_page") or {};req(fp,("headline","signal_ids","decision_ids","unknowns","owner","status"),"front_page",e);fps=set(str(x) for x in fp.get("signal_ids",[]));fpd=set(str(x) for x in fp.get("decision_ids",[]));unknown_sig=sorted(fps-sigids);unknown_dec=sorted(fpd-dids)
    if unknown_sig:e.append(f"front_page: unknown signals {', '.join(unknown_sig)}")
    if unknown_dec:e.append(f"front_page: unknown decisions {', '.join(unknown_dec)}")
    omitted=sorted(critical-fps)
    if omitted:e.append(f"front_page: critical signals omitted {', '.join(omitted)}")
    if len(fps)+len(fpd)>c.get("max_front_page_items",0):e.append("front_page: max items exceeded")
    if fp.get("status") in {"APPROVED","SENT","DELIVERED","PUBLISHED"}:unauthorized+=1;e.append("front_page: forbidden status")
    actions=d.get("actions") or [];aids=ids(actions,"action_id","actions",e)
    for i,x in enumerate(actions):req(x,("action_id","action","owner","due_or_trigger","dependency","approval_needed","source_refs"),f"action[{i}]",e);refs(x.get("source_refs"),active,f"action[{i}]","source_refs",e)
    ts=d.get("tests") or [];present={str(x.get("test_type","")) for x in ts};missing=sorted(TESTS-present)
    if missing:e.append(f"tests: missing {', '.join(missing)}")
    for i,x in enumerate(ts):req(x,("test_type","evidence","reviewer","date"),f"test[{i}]",e);e.append(f"test[{i}]: failed") if x.get("passed") is not True else None
    rs=d.get("reviews") or [];presentr={str(x.get("review_type","")) for x in rs if x.get("required") is True};missingr=sorted(REVIEWS-presentr)
    if missingr:e.append(f"reviews: missing {', '.join(missingr)}")
    for i,x in enumerate(rs):req(x,("review_type","reviewer","status"),f"review[{i}]",e);e.append(f"review[{i}]: PASS needs evidence") if x.get("status")=="PASS" and blank(x.get("evidence_ref")) else None
    final=any(x.get("review_type")=="FINAL_BRIEF" and x.get("status")=="PASS" and not blank(x.get("evidence_ref")) for x in rs);nonfinal=all(x.get("status")=="PASS" for x in rs if x.get("required") is True and x.get("review_type")!="FINAL_BRIEF")
    if e:state="NOT_READY"
    elif final and nonfinal:state="READY_FOR_AUTHORIZED_DELIVERY";w.append("Human delivery remains outside engine")
    elif nonfinal:state="READY_FOR_EXECUTIVE_REVIEW";w.append("FINAL_BRIEF remains; engine does not decide or send")
    else:state="NOT_READY";e.append("reviews incomplete")
    return {"brief_id":c.get("brief_id",""),"state":state,"metrics":{"sources":len(sids),"active_sources":len(active),"stale_sources":len(stale),"signals":len(sigids),"critical_signals":len(critical),"critical_omissions":len(omitted),"metric_exceptions":len(mids),"metric_defects":metric_defects,"decision_requests":len(dids),"front_page_items":len(fps)+len(fpd),"actions":len(aids),"forbidden_flags":forbidden,"unauthorized_states":unauthorized,"test_types":len(present&TESTS),"critical_defects":len(e)},"errors":e,"warnings":w}
def main()->int:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",type=Path);p.add_argument("--output",type=Path);a=p.parse_args();r=evaluate(load_json(a.input));s=json.dumps(r,ensure_ascii=False,indent=2);print(s)
    if a.output:a.output.write_text(s+"\n",encoding="utf-8")
    return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__":raise SystemExit(main())
