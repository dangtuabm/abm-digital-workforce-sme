#!/usr/bin/env python3
"""Deterministic static gate for a Data Story Decision Pack."""
from __future__ import annotations
import argparse, json, math
from collections import Counter
from pathlib import Path
from typing import Any, Iterable

TEST_TYPES={"source_data_contract","metric_reconciliation","insight_claim_lineage","chart_encoding_integrity","narrative_consistency","accessibility_medium","approval_render_boundary"}
REVIEW_TYPES={"DATA_OWNER","DOMAIN_OWNER","EDITORIAL","ACCESSIBILITY","FINAL_STORY"}
LAYERS={"OBSERVATION":1,"INTERPRETATION":2,"IMPLICATION":3,"RECOMMENDATION":4}
FORBIDDEN={"fabricated_data","denominator_changed","cherry_picked_window","causal_overclaim","hidden_missing_data","hidden_uncertainty","truncated_bar_axis","unjustified_dual_axis","misleading_area","fake_render_or_publish"}

def load_json(p:Path)->dict[str,Any]:
    with p.open("r",encoding="utf-8-sig") as f:d=json.load(f)
    if not isinstance(d,dict):raise ValueError("Root JSON must be object")
    return d
def blank(v:Any)->bool:return v is None or v=="" or v==[] or v=={}
def req(o:dict[str,Any],fs:Iterable[str],label:str,e:list[str])->None:
    for f in fs:
        if f not in o or blank(o[f]):e.append(f"{label}: missing {f}")
def ids(xs:list[dict[str,Any]],f:str,label:str,e:list[str])->set[str]:
    vs=[str(x.get(f,"")).strip() for x in xs]; ds=[v for v,n in Counter(vs).items() if v and n>1]
    if any(not v for v in vs):e.append(f"{label}: blank {f}")
    if ds:e.append(f"{label}: duplicate {f}: {', '.join(ds)}")
    return {v for v in vs if v}
def refs(v:Any,valid:set[str],label:str,f:str,e:list[str],empty:bool=False)->set[str]:
    if not isinstance(v,list) or (not v and not empty):e.append(f"{label}: invalid {f}");return set()
    s={str(x) for x in v}; u=sorted(s-valid)
    if u:e.append(f"{label}: unknown {f}: {', '.join(u)}")
    return s
def num(v:Any)->float|None:
    try:x=float(v)
    except (TypeError,ValueError):return None
    return x if not isinstance(v,bool) and math.isfinite(x) else None

def evaluate(d:dict[str,Any])->dict[str,Any]:
    e=[];w=[]; c=d.get("contract") or {}
    req(c,("story_id","version","data_snapshot_hash","decision","question","audiences","medium","owner","final_approver","classification","required_reviews","prohibited_actions"),"contract",e)
    if c.get("data_authorized") is not True:e.append("contract: data_authorized must be true")
    ss=d.get("sources") or []; sids=ids(ss,"source_id","sources",e); active=set()
    for i,s in enumerate(ss):
        req(s,("source_id","title","version","locator","owner","effective_date","classification"),f"source[{i}]",e)
        if s.get("active") is True:active.add(str(s.get("source_id")))
    if not active:e.append("sources: active source required")
    dc=d.get("data_contract") or {}; req(dc,("grain","dimensions","timezone","currency","units","baseline_window","outcome_window","sample_rule","exclusions","missing_data_rule","attribution_level","source_refs","owner"),"data_contract",e); refs(dc.get("source_refs"),active,"data_contract","source_refs",e)
    ms=d.get("metrics") or []; mids=ids(ms,"metric_id","metrics",e); calc=0
    for i,m in enumerate(ms):
        label=f"metric[{i}]"; req(m,("metric_id","name","formula","unit","delta_type","baseline_value","outcome_value","reported_delta","denominator","baseline_window","outcome_window","sample_size","exclusions","source_refs","validation_status"),label,e); refs(m.get("source_refs"),active,label,"source_refs",e)
        b,o,r=num(m.get("baseline_value")),num(m.get("outcome_value")),num(m.get("reported_delta"))
        if None in (b,o,r):calc+=1;e.append(f"{label}: values must be finite");continue
        if m.get("delta_type")=="ABSOLUTE":x=o-b
        elif m.get("delta_type")=="RELATIVE" and b!=0:x=(o-b)/b
        else:calc+=1;e.append(f"{label}: invalid delta");continue
        if not math.isclose(x,r,rel_tol=1e-9,abs_tol=1e-9):calc+=1;e.append(f"{label}: reported_delta mismatch")
        if m.get("baseline_window")!=dc.get("baseline_window") or m.get("outcome_window")!=dc.get("outcome_window"):e.append(f"{label}: window mismatch")
        if m.get("validation_status")!="VALIDATED":e.append(f"{label}: not validated")
    ins=d.get("insights") or []; iids=ids(ins,"insight_id","insights",e); over=0; forbidden=0
    rank=LAYERS.get(str(dc.get("attribution_level")),2)
    for i,x in enumerate(ins):
        label=f"insight[{i}]";req(x,("insight_id","statement","layer","metric_ids","source_refs","confidence","limitations","counter_reading","owner"),label,e);refs(x.get("metric_ids"),mids,label,"metric_ids",e);refs(x.get("source_refs"),active,label,"source_refs",e)
        if LAYERS.get(str(x.get("layer")),99)>rank and x.get("evidence_design_approved") is not True:over+=1;e.append(f"{label}: layer exceeds evidence")
        for f in FORBIDDEN:
            if x.get(f) is True:forbidden+=1;e.append(f"{label}: forbidden flag {f}")
    cs=d.get("charts") or []; cids=ids(cs,"chart_id","charts",e); deceptive=0
    for i,x in enumerate(cs):
        label=f"chart[{i}]";req(x,("chart_id","question","chart_type","fields","encoding","scale","sort","metric_ids","source_refs","source_note","alt_text","owner","review_status"),label,e);refs(x.get("metric_ids"),mids,label,"metric_ids",e);refs(x.get("source_refs"),active,label,"source_refs",e)
        if x.get("chart_type")=="BAR" and x.get("zero_baseline") is not True:deceptive+=1;e.append(f"{label}: bar requires zero baseline")
        for f in FORBIDDEN:
            if x.get(f) is True:deceptive+=1;e.append(f"{label}: forbidden flag {f}")
        if x.get("review_status") in {"RENDERED","APPROVED","PUBLISHED","SENT"}:e.append(f"{label}: forbidden status {x.get('review_status')}")
    nar=d.get("narrative") or {};req(nar,("headline","context","change","evidence","limitations","implication","actions","insight_ids","metric_ids","owner","status"),"narrative",e);refs(nar.get("insight_ids"),iids,"narrative","insight_ids",e);refs(nar.get("metric_ids"),mids,"narrative","metric_ids",e)
    unauthorized=0
    if nar.get("status") in {"RENDERED","APPROVED","PUBLISHED","SENT"}:unauthorized+=1;e.append(f"narrative: forbidden status {nar.get('status')}")
    ts=d.get("tests") or []; present={str(x.get("test_type","")) for x in ts}; missing=sorted(TEST_TYPES-present)
    if missing:e.append(f"tests: missing {', '.join(missing)}")
    for i,x in enumerate(ts):req(x,("test_type","evidence","reviewer","date"),f"test[{i}]",e);e.append(f"test[{i}]: failed") if x.get("passed") is not True else None
    rs=d.get("reviews") or []; presentr={str(x.get("review_type","")) for x in rs if x.get("required") is True}; missingr=sorted(REVIEW_TYPES-presentr)
    if missingr:e.append(f"reviews: missing {', '.join(missingr)}")
    for i,x in enumerate(rs):
        req(x,("review_type","reviewer","status"),f"review[{i}]",e)
        if x.get("status")=="PASS" and blank(x.get("evidence_ref")):e.append(f"review[{i}]: PASS needs evidence")
    final=any(x.get("review_type")=="FINAL_STORY" and x.get("status")=="PASS" and not blank(x.get("evidence_ref")) for x in rs); nonfinal=all(x.get("status")=="PASS" for x in rs if x.get("required") is True and x.get("review_type")!="FINAL_STORY")
    if e:state="NOT_READY"
    elif final and nonfinal:state="READY_FOR_AUTHORIZED_RENDER";w.append("Human render/publication remains outside engine")
    elif nonfinal:state="READY_FOR_STORY_REVIEW";w.append("FINAL_STORY remains; engine does not render or publish")
    else:state="NOT_READY";e.append("reviews incomplete")
    return {"story_id":c.get("story_id",""),"state":state,"metrics":{"sources":len(sids),"active_sources":len(active),"metrics":len(mids),"insights":len(iids),"charts":len(cids),"calculation_defects":calc,"attribution_overclaims":over,"forbidden_insights":forbidden,"deceptive_charts":deceptive,"test_types":len(present&TEST_TYPES),"unauthorized_render_publish":unauthorized,"critical_defects":len(e)},"errors":e,"warnings":w}

def main()->int:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",type=Path);p.add_argument("--output",type=Path);a=p.parse_args();r=evaluate(load_json(a.input));s=json.dumps(r,ensure_ascii=False,indent=2);print(s)
    if a.output:a.output.write_text(s+"\n",encoding="utf-8")
    return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__":raise SystemExit(main())
