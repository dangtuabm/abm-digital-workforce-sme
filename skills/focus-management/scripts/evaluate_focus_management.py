#!/usr/bin/env python3
"""Deterministic static gate for a Focus Commitment Plan."""
from __future__ import annotations
import argparse,json
from collections import Counter
from pathlib import Path
from typing import Any,Iterable

TESTS={"capacity_reconciliation","wip_limit","commitment_dependency","authority_boundary","wellbeing_recovery","interruption_protocol","scheduling_execution_boundary"}
REVIEWS={"FOCUS_OWNER","COMMITMENT_OWNER","DEPENDENCY_OWNER","FINAL_SCHEDULING"}
TIERS={"MUST","WIN","SUPPORT","NOT_NOW"}; STATUSES={"READY","ACTIVE","BLOCKED","DONE","CANCELLED"}; DISPOSITIONS={"DO","DELEGATE","DEFER","DROP","ESCALATE"}
FORBIDDEN={"fabricated_availability","overbooked","sleep_or_recovery_cut","secret_surveillance","auto_rescheduled","auto_declined","auto_delegated","deleted_commitment","fake_done"}
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
def nonneg(v:Any)->bool:return isinstance(v,(int,float)) and not isinstance(v,bool) and v>=0
def evaluate(d:dict[str,Any])->dict[str,Any]:
    e=[];w=[];c=d.get("contract") or {};req(c,("plan_id","version","horizon","timezone","outcomes","owner","final_approver","wip_limit","prohibited_actions","required_reviews"),"contract",e)
    a=d.get("availability") or {};req(a,("working_minutes","fixed_minutes","recovery_minutes","buffer_minutes","source_ref","owner"),"availability",e);vals=[a.get(x) for x in ("working_minutes","fixed_minutes","recovery_minutes","buffer_minutes")]
    cap=0
    if not all(nonneg(x) for x in vals):e.append("availability: minutes must be non-negative")
    else:cap=vals[0]-vals[1]-vals[2]-vals[3];e.append("availability: negative focus capacity") if cap<0 else None
    cs=d.get("commitments") or [];cids=ids(cs,"commitment_id","commitments",e);active=0;forbidden=0
    for i,x in enumerate(cs):
        l=f"commitment[{i}]";req(x,("commitment_id","title","outcome","source","owner","deadline","effort_minutes","tier","status","authority"),l,e)
        if "dependencies" not in x or not isinstance(x.get("dependencies"),list):e.append(f"{l}: dependencies must be a list")
        if x.get("tier") not in TIERS or x.get("status") not in STATUSES:e.append(f"{l}: invalid tier/status")
        if x.get("status")=="ACTIVE":active+=1
        for f in FORBIDDEN:
            if x.get(f) is True:forbidden+=1;e.append(f"{l}: forbidden flag {f}")
    if isinstance(c.get("wip_limit"),int) and active>c.get("wip_limit"):e.append("commitments: WIP limit exceeded")
    ds=d.get("dispositions") or [];dids=ids(ds,"disposition_id","dispositions",e);unauth=0
    for i,x in enumerate(ds):
        l=f"disposition[{i}]";req(x,("disposition_id","commitment_id","decision","rationale","harm_if_wrong","owner","authority_status"),l,e)
        if x.get("commitment_id") not in cids:e.append(f"{l}: unknown commitment")
        if x.get("decision") not in DISPOSITIONS:e.append(f"{l}: invalid decision")
        if x.get("decision")!="DO" and x.get("authority_status")!="APPROVED":unauth+=1;e.append(f"{l}: non-DO decision lacks approval")
    bs=d.get("focus_blocks") or [];bids=ids(bs,"block_id","focus_blocks",e);minutes=0
    for i,x in enumerate(bs):
        l=f"block[{i}]";req(x,("block_id","commitment_id","outcome","duration_minutes","energy_fit","start_condition","stop_rule","buffer_minutes","owner"),l,e)
        if x.get("commitment_id") not in cids:e.append(f"{l}: unknown commitment")
        if not nonneg(x.get("duration_minutes")):e.append(f"{l}: invalid duration")
        else:minutes+=x.get("duration_minutes")
    over=max(0,minutes-cap)
    if over>0:e.append("focus_blocks: over capacity")
    conflicts=d.get("conflicts") or [];critical_open=0
    for i,x in enumerate(conflicts):
        req(x,("conflict_id","type","severity","evidence","resolution","owner","status"),f"conflict[{i}]",e)
        if x.get("severity")=="CRITICAL" and x.get("status")!="RESOLVED":critical_open+=1;e.append(f"conflict[{i}]: critical conflict open")
    ip=d.get("interruption_protocol") or {};req(ip,("classes","capture_queue","escalation_route","return_to_focus","owner"),"interruption_protocol",e)
    ts=d.get("tests") or [];present={str(x.get("test_type","")) for x in ts};missing=sorted(TESTS-present)
    if missing:e.append(f"tests: missing {', '.join(missing)}")
    for i,x in enumerate(ts):req(x,("test_type","evidence","reviewer","date"),f"test[{i}]",e);e.append(f"test[{i}]: failed") if x.get("passed") is not True else None
    rs=d.get("reviews") or [];presentr={str(x.get("review_type","")) for x in rs if x.get("required") is True};missingr=sorted(REVIEWS-presentr)
    if missingr:e.append(f"reviews: missing {', '.join(missingr)}")
    for i,x in enumerate(rs):req(x,("review_type","reviewer","status"),f"review[{i}]",e);e.append(f"review[{i}]: PASS needs evidence") if x.get("status")=="PASS" and blank(x.get("evidence_ref")) else None
    final=any(x.get("review_type")=="FINAL_SCHEDULING" and x.get("status")=="PASS" and not blank(x.get("evidence_ref")) for x in rs);nonfinal=all(x.get("status")=="PASS" for x in rs if x.get("required") is True and x.get("review_type")!="FINAL_SCHEDULING")
    if e:state="NOT_READY"
    elif final and nonfinal:state="READY_FOR_AUTHORIZED_SCHEDULING";w.append("External scheduling remains human-owned")
    elif nonfinal:state="READY_FOR_FOCUS_REVIEW";w.append("FINAL_SCHEDULING remains; engine changes no calendar/task")
    else:state="NOT_READY";e.append("reviews incomplete")
    return {"plan_id":c.get("plan_id",""),"state":state,"metrics":{"focus_capacity":cap,"scheduled_focus_minutes":minutes,"over_capacity_minutes":over,"commitments":len(cids),"active_wip":active,"wip_limit":c.get("wip_limit"),"dispositions":len(dids),"focus_blocks":len(bids),"unauthorized_dispositions":unauth,"forbidden_actions":forbidden,"critical_open_conflicts":critical_open,"test_types":len(present&TESTS),"critical_defects":len(e)},"errors":e,"warnings":w}
def main()->int:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",type=Path);p.add_argument("--output",type=Path);a=p.parse_args();r=evaluate(load_json(a.input));s=json.dumps(r,ensure_ascii=False,indent=2);print(s)
    if a.output:a.output.write_text(s+"\n",encoding="utf-8")
    return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__":raise SystemExit(main())
