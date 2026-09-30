#!/usr/bin/env python3
"""Deterministic static gate for a Meeting Evidence & Commitment Record."""
from __future__ import annotations
import argparse,json
from collections import Counter
from pathlib import Path
from typing import Any,Iterable
TESTS={"source_provenance","speaker_identity","decision_authority","action_acceptance","dissent_unknown_coverage","privacy_correction","distribution_execution_boundary"}
REVIEWS={"MEETING_OWNER","DECISION_AUTHORITY","ACTION_OWNERS","PRIVACY_SECURITY","FINAL_RECORD"}
FORBIDDEN={"fabricated_source","altered_quote","inferred_as_decided","unauthorized_decider","forced_commitment","hidden_dissent","silent_correction","fake_signed","fake_sent","fake_done"}
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
    e=[];w=[];c=d.get("contract") or {};req(c,("record_id","meeting_id","version","start","end","timezone","purpose","participant_ids","classification","retention","distribution","correction_owner","required_reviews","prohibited_actions"),"contract",e)
    ss=d.get("sources") or [];sids=ids(ss,"source_id","sources",e);active=set();sourceviol=0
    for i,x in enumerate(ss):
        l=f"source[{i}]";req(x,("source_id","source_type","version","hash","locator","owner","capture_method","time_span","classification","access_status","consent_status"),l,e)
        if x.get("active") is True:active.add(str(x.get("source_id")))
        if x.get("access_status")!="AUTHORIZED" or x.get("consent_status")!="APPROVED":sourceviol+=1;e.append(f"{l}: access/consent invalid")
    sp=d.get("speakers") or [];spids=ids(sp,"speaker_id","speakers",e);verified=set();deciders=set()
    for i,x in enumerate(sp):
        l=f"speaker[{i}]";req(x,("speaker_id","canonical_name","role","identity_confidence","verification_evidence","authority_scope"),l,e)
        if x.get("identity_confidence") in {"VERIFIED","HIGH"}:verified.add(str(x.get("speaker_id")))
        if x.get("role")=="DECIDER" and str(x.get("speaker_id")) in verified:deciders.add(str(x.get("speaker_id")))
    dissent=d.get("dissents") or [];disids=ids(dissent,"dissent_id","dissents",e)
    for i,x in enumerate(dissent):
        l=f"dissent[{i}]";req(x,("dissent_id","speaker_id","statement","source_refs","locator","status","owner"),l,e);refs(x.get("source_refs"),active,l,"source_refs",e)
        if x.get("speaker_id") not in spids:e.append(f"{l}: unknown speaker")
    decisions=d.get("decisions") or [];deids=ids(decisions,"decision_id","decisions",e);decisionviol=0;forbidden=0
    for i,x in enumerate(decisions):
        l=f"decision[{i}]";req(x,("decision_id","decision","decider_id","authority_evidence","source_refs","locator","rationale","scope","confirmation_status"),l,e);refs(x.get("source_refs"),active,l,"source_refs",e)
        if "dissent_ids" not in x or not isinstance(x.get("dissent_ids"),list):e.append(f"{l}: dissent_ids must be a list")
        else:refs(x.get("dissent_ids"),disids,l,"dissent_ids",e,True)
        if x.get("decider_id") not in deciders or x.get("confirmation_status")!="CONFIRMED":decisionviol+=1;e.append(f"{l}: authority/confirmation invalid")
        for f in FORBIDDEN:
            if x.get(f) is True:forbidden+=1;e.append(f"{l}: forbidden flag {f}")
    actions=d.get("actions") or [];aids=ids(actions,"action_id","actions",e);actionviol=0
    for i,x in enumerate(actions):
        l=f"action[{i}]";req(x,("action_id","deliverable","owner_id","acceptance_status","source_refs","locator","due_or_trigger","acceptance_criteria","report_to","status"),l,e);refs(x.get("source_refs"),active,l,"source_refs",e)
        if "dependencies" not in x or not isinstance(x.get("dependencies"),list):e.append(f"{l}: dependencies must be a list")
        if x.get("owner_id") not in verified or x.get("acceptance_status")!="EXPLICIT" or x.get("status") not in {"RECORDED","PENDING_CONFIRMATION"}:actionviol+=1;e.append(f"{l}: owner/acceptance/status invalid")
        for f in FORBIDDEN:
            if x.get(f) is True:forbidden+=1;e.append(f"{l}: forbidden flag {f}")
    unknowns=d.get("unknowns") or [];uids=ids(unknowns,"unknown_id","unknowns",e)
    for i,x in enumerate(unknowns):req(x,("unknown_id","question","owner","due_or_trigger","impact","source_refs","status"),f"unknown[{i}]",e);refs(x.get("source_refs"),active,f"unknown[{i}]","source_refs",e)
    corrections=d.get("corrections") or [];cids=ids(corrections,"correction_id","corrections",e)
    for i,x in enumerate(corrections):
        l=f"correction[{i}]";req(x,("correction_id","before","after","reason","requester","approver","evidence_ref","date"),l,e)
        if x.get("evidence_ref") not in active:e.append(f"{l}: evidence not active")
    record=d.get("record") or {};req(record,("summary","decision_ids","action_ids","dissent_ids","unknown_ids","source_refs","owner","status"),"record",e)
    rde=refs(record.get("decision_ids"),deids,"record","decision_ids",e,True);rac=refs(record.get("action_ids"),aids,"record","action_ids",e,True);rdi=refs(record.get("dissent_ids"),disids,"record","dissent_ids",e,True);run=refs(record.get("unknown_ids"),uids,"record","unknown_ids",e,True);refs(record.get("source_refs"),active,"record","source_refs",e)
    if deids-rde:e.append(f"record: decisions omitted {', '.join(sorted(deids-rde))}")
    if aids-rac:e.append(f"record: actions omitted {', '.join(sorted(aids-rac))}")
    if disids-rdi:e.append(f"record: dissents omitted {', '.join(sorted(disids-rdi))}")
    if uids-run:e.append(f"record: unknowns omitted {', '.join(sorted(uids-run))}")
    unauthorized=0
    if record.get("status") in {"SIGNED","SENT","DISTRIBUTED","ACKNOWLEDGED","DONE"}:unauthorized+=1;e.append("record: forbidden execution state")
    ts=d.get("tests") or [];present={str(x.get("test_type","")) for x in ts};missing=sorted(TESTS-present)
    if missing:e.append(f"tests: missing {', '.join(missing)}")
    for i,x in enumerate(ts):req(x,("test_type","evidence","reviewer","date"),f"test[{i}]",e);e.append(f"test[{i}]: failed") if x.get("passed") is not True else None
    rs=d.get("reviews") or [];presentr={str(x.get("review_type","")) for x in rs if x.get("required") is True};missingr=sorted(REVIEWS-presentr)
    if missingr:e.append(f"reviews: missing {', '.join(missingr)}")
    for i,x in enumerate(rs):req(x,("review_type","reviewer","status"),f"review[{i}]",e);e.append(f"review[{i}]: PASS needs evidence") if x.get("status")=="PASS" and blank(x.get("evidence_ref")) else None
    final=any(x.get("review_type")=="FINAL_RECORD" and x.get("status")=="PASS" and not blank(x.get("evidence_ref")) for x in rs);nonfinal=all(x.get("status")=="PASS" for x in rs if x.get("required") is True and x.get("review_type")!="FINAL_RECORD")
    if e:state="NOT_READY"
    elif final and nonfinal:state="READY_FOR_AUTHORIZED_DISTRIBUTION";w.append("Human distribution/task creation remains outside engine")
    elif nonfinal:state="READY_FOR_RECORD_REVIEW";w.append("FINAL_RECORD remains; engine does not send or create tasks")
    else:state="NOT_READY";e.append("reviews incomplete")
    return {"record_id":c.get("record_id",""),"state":state,"metrics":{"sources":len(sids),"active_sources":len(active),"source_violations":sourceviol,"speakers":len(spids),"verified_speakers":len(verified),"decisions":len(deids),"decision_violations":decisionviol,"actions":len(aids),"action_violations":actionviol,"dissents":len(disids),"unknowns":len(uids),"corrections":len(cids),"forbidden_flags":forbidden,"unauthorized_states":unauthorized,"test_types":len(present&TESTS),"critical_defects":len(e)},"errors":e,"warnings":w}
def main()->int:
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",type=Path);p.add_argument("--output",type=Path);a=p.parse_args();r=evaluate(load_json(a.input));s=json.dumps(r,ensure_ascii=False,indent=2);print(s)
    if a.output:a.output.write_text(s+"\n",encoding="utf-8")
    return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__":raise SystemExit(main())
