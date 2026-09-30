#!/usr/bin/env python3
"""Deterministic static gate for a Meeting Readiness Pack."""
from __future__ import annotations
import argparse,json
from collections import Counter
from pathlib import Path
from typing import Any,Iterable
TYPES={"DECIDE","ALIGN","SOLVE","REVIEW","CREATE"};MODES={"INFORM","DISCUSS","DECIDE","COMMIT"}
TESTS={"meeting_contract","source_freshness","attendee_quorum","decision_readiness","agenda_timebox","pre_read_accessibility","invitation_execution_boundary"}
REVIEWS={"MEETING_OWNER","DECISION_OWNER","SECURITY_ACCESS","FINAL_INVITE"}
FORBIDDEN={"fabricated_history","hidden_open_commitment","fake_quorum","fake_attendance","fake_pre_read_sent","fake_pre_read_read","auto_invited","auto_rescheduled","false_decision"}
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
def refs(v:Any,valid:set[str],l:str,f:str,e:list[str],empty:bool=False)->set[str]:
    if not isinstance(v,list) or (not v and not empty):e.append(f"{l}: invalid {f}");return set()
    s={str(x) for x in v};u=sorted(s-valid)
    if u:e.append(f"{l}: unknown {f}: {', '.join(u)}")
    return s
def evaluate(d:dict[str,Any])->dict[str,Any]:
    e=[];w=[];c=d.get("contract") or {};req(c,("meeting_id","version","meeting_type","purpose","required_output","start","end","timezone","duration_minutes","owner","facilitator","decider","classification","required_reviews","prohibited_actions"),"contract",e)
    if c.get("meeting_type") not in TYPES:e.append("contract: invalid meeting_type")
    ss=d.get("sources") or [];sids=ids(ss,"source_id","sources",e);active=set();stale=0
    for i,x in enumerate(ss):
        l=f"source[{i}]";req(x,("source_id","title","version","locator","owner","age_hours","freshness_sla_hours","classification","access_status"),l,e)
        if x.get("active") is True:active.add(str(x.get("source_id")))
        if isinstance(x.get("age_hours"),(int,float)) and isinstance(x.get("freshness_sla_hours"),(int,float)) and x.get("age_hours")>x.get("freshness_sla_hours"):stale+=1;e.append(f"{l}: stale")
        if x.get("access_status")!="AUTHORIZED":e.append(f"{l}: access not authorized")
    prs=d.get("pre_reads") or [];prids=ids(prs,"pre_read_id","pre_reads",e);previol=0
    for i,x in enumerate(prs):
        l=f"pre_read[{i}]";req(x,("pre_read_id","title","source_refs","estimated_read_minutes","audience_roles","access_status","status","owner"),l,e);refs(x.get("source_refs"),active,l,"source_refs",e)
        if x.get("access_status")!="AUTHORIZED" or x.get("status") not in {"DRAFT","REVIEWED"}:previol+=1;e.append(f"{l}: access/status invalid")
    ats=d.get("attendees") or [];aids=ids(ats,"attendee_id","attendees",e);required={str(x.get("attendee_id")) for x in ats if x.get("required") is True};available=set()
    for i,x in enumerate(ats):
        l=f"attendee[{i}]";req(x,("attendee_id","role","required","availability_status","access_status","owner"),l,e)
        if x.get("availability_status")=="AVAILABLE" and x.get("access_status")=="AUTHORIZED":available.add(str(x.get("attendee_id")))
    quorum=bool(required) and required<=available and any(x.get("attendee_id")==c.get("decider") and x.get("attendee_id") in available for x in ats)
    if not quorum:e.append("attendees: quorum not met")
    commits=d.get("prior_commitments") or [];coids=ids(commits,"commitment_id","prior_commitments",e);forbidden=0
    for i,x in enumerate(commits):
        req(x,("commitment_id","commitment","owner","due","status","evidence","meeting_relevance"),f"commitment[{i}]",e)
        for f in FORBIDDEN:
            if x.get(f) is True:forbidden+=1;e.append(f"commitment[{i}]: forbidden flag {f}")
    ds=d.get("decision_items") or [];dids=ids(ds,"decision_id","decision_items",e)
    for i,x in enumerate(ds):
        l=f"decision[{i}]";req(x,("decision_id","question","options","recommendation","source_refs","decision_rule","owner","deadline","consequence_of_no_decision"),l,e);refs(x.get("source_refs"),active,l,"source_refs",e)
        if not isinstance(x.get("options"),list) or len(x.get("options",[]))<2:e.append(f"{l}: at least two options required")
    agenda=d.get("agenda") or [];segids=ids(agenda,"segment_id","agenda",e);minutes=0;covered=set()
    for i,x in enumerate(agenda):
        l=f"agenda[{i}]";req(x,("segment_id","objective","mode","owner","duration_minutes","required_inputs","output","stop_rule","parking_route"),l,e)
        if "decision_ids" not in x or not isinstance(x.get("decision_ids"),list):e.append(f"{l}: decision_ids must be a list")
        else:refs(x.get("decision_ids"),dids,l,"decision_ids",e,True)
        if x.get("mode") not in MODES:e.append(f"{l}: invalid mode")
        if isinstance(x.get("duration_minutes"),(int,float)) and x.get("duration_minutes")>=0:minutes+=x.get("duration_minutes")
        else:e.append(f"{l}: invalid duration")
        covered|={str(v) for v in x.get("decision_ids",[])}
    if minutes>c.get("duration_minutes",0):e.append("agenda: duration exceeded")
    missing_dec=sorted(dids-covered)
    if missing_dec:e.append(f"agenda: decisions not covered {', '.join(missing_dec)}")
    plan=d.get("facilitation_plan") or {};req(plan,("opening","norms","dissent_route","parking_rule","accessibility","contingency","recap_owner","status"),"facilitation_plan",e)
    unauthorized=0
    if plan.get("status") in {"INVITED","SENT","RESCHEDULED","ACCEPTED","DECIDED"}:unauthorized+=1;e.append("facilitation_plan: forbidden execution state")
    ts=d.get("tests") or [];present={str(x.get("test_type","")) for x in ts};missing=sorted(TESTS-present)
    if missing:e.append(f"tests: missing {', '.join(missing)}")
    for i,x in enumerate(ts):req(x,("test_type","evidence","reviewer","date"),f"test[{i}]",e);e.append(f"test[{i}]: failed") if x.get("passed") is not True else None
    rs=d.get("reviews") or [];presentr={str(x.get("review_type","")) for x in rs if x.get("required") is True};missingr=sorted(REVIEWS-presentr)
    if missingr:e.append(f"reviews: missing {', '.join(missingr)}")
    for i,x in enumerate(rs):req(x,("review_type","reviewer","status"),f"review[{i}]",e);e.append(f"review[{i}]: PASS needs evidence") if x.get("status")=="PASS" and blank(x.get("evidence_ref")) else None
    final=any(x.get("review_type")=="FINAL_INVITE" and x.get("status")=="PASS" and not blank(x.get("evidence_ref")) for x in rs);nonfinal=all(x.get("status")=="PASS" for x in rs if x.get("required") is True and x.get("review_type")!="FINAL_INVITE")
    if e:state="NOT_READY"
    elif final and nonfinal:state="READY_FOR_AUTHORIZED_INVITE";w.append("Human invite/send remains outside engine")
    elif nonfinal:state="READY_FOR_MEETING_REVIEW";w.append("FINAL_INVITE remains; engine changes no calendar")
    else:state="NOT_READY";e.append("reviews incomplete")
    return {"meeting_id":c.get("meeting_id",""),"state":state,"metrics":{"sources":len(sids),"active_sources":len(active),"stale_sources":stale,"pre_reads":len(prids),"pre_read_violations":previol,"attendees":len(aids),"quorum_met":quorum,"prior_commitments":len(coids),"decision_items":len(dids),"agenda_segments":len(segids),"agenda_minutes":minutes,"meeting_minutes":c.get("duration_minutes"),"uncovered_decisions":len(missing_dec),"forbidden_flags":forbidden,"unauthorized_states":unauthorized,"test_types":len(present&TESTS),"critical_defects":len(e)},"errors":e,"warnings":w}
def main()->int:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",type=Path);p.add_argument("--output",type=Path);a=p.parse_args();r=evaluate(load_json(a.input));s=json.dumps(r,ensure_ascii=False,indent=2);print(s)
    if a.output:a.output.write_text(s+"\n",encoding="utf-8")
    return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__":raise SystemExit(main())
