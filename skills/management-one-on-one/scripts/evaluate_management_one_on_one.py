#!/usr/bin/env python3
"""Static evaluator for management-one-on-one."""
from __future__ import annotations
import json, sys
from pathlib import Path
from typing import Any

TESTS={"contract_privacy","evidence_fairness","agenda_balance","feedback_quality","commitment_control","sensitive_boundary","implementation_boundary"}
FLAGS={"evidence_fabricated","quote_fabricated","emotion_inferred","personality_labeled","protected_trait_used","private_note_exposed","covert_recording","surveillance_used","agenda_one_sided","system_blocker_hidden","manager_commitment_omitted","sensitive_route_bypassed","auto_sent","auto_recorded","auto_rated","auto_disciplined","auto_promoted","auto_terminated","hr_file_updated","confirmation_faked"}
STATES={"SENT","RECORDED","RATED","DISCIPLINED","PROMOTED","TERMINATED","HR_FILE_UPDATED","CONFIRMED"}

def ok(v:Any)->bool:return v not in(None,"",[],{})
def need(o:dict,fs:list[str],p:str,d:list[str]):
    for f in fs:
        if not ok(o.get(f)):d.append(f"{p}:missing_{f}")
def rows(x:dict,k:str,d:list[str])->list[dict]:
    v=x.get(k)
    if not isinstance(v,list) or not v:d.append(f"{k}:missing_or_empty");return []
    return [a for a in v if isinstance(a,dict)]
def unique(xs:list[dict],key:str,label:str,d:list[str])->dict:
    z={}
    for i,x in enumerate(xs):
        v=x.get(key)
        if not isinstance(v,str) or not v:d.append(f"{label}[{i}]:missing_{key}")
        elif v in z:d.append(f"{label}:duplicate_{key}:{v}")
        else:z[v]=x
    return z

def validate(x:dict)->dict:
    d=[];g=[]
    c=x.get("session_contract",{});need(c,["pair_id","session_id","purpose","date","cadence","manager_id","participant_id","human_facilitator","consent","notes_rule","recording_rule","access_roles","retention","prohibited_uses","data_classification"],"session_contract",d)
    if c.get("consent")!="CONFIRMED":d.append("session_contract:consent_not_confirmed")
    if c.get("recording_rule") not in {"NO_RECORDING","EXPLICIT_CONSENT_REQUIRED"}:d.append("session_contract:invalid_recording_rule")
    if c.get("data_classification") not in {"GREEN","YELLOW","RED"}:d.append("session_contract:invalid_classification")
    roles={c.get("manager_id"),c.get("participant_id")};fac=c.get("human_facilitator")
    if isinstance(fac,str) and fac.upper().startswith("AI"):d.append("session_contract:ai_facilitator")
    ev=rows(x,"work_evidence",d);pm=rows(x,"prior_commitments",d);ag=rows(x,"agenda",d);fb=rows(x,"feedback_cards",d);qs=rows(x,"questions",d);sp=rows(x,"support_experiments",d);cm=rows(x,"commitments",d)
    unique(ev,"id","work_evidence",d);unique(pm,"id","prior_commitments",d);unique(fb,"id","feedback_cards",d);unique(cm,"id","commitments",d)
    for a in ev:
        p=f"evidence:{a.get('id','?')}";need(a,["type","source","source_version","as_of","access","fact","confidence"],p,d)
        if a.get("access")!="AUTHORIZED":d.append(f"{p}:unauthorized")
        if a.get("contains_protected_trait") is True:d.append(f"{p}:protected_trait")
    for a in pm:
        p=f"prior:{a.get('id','?')}";need(a,["owner","outcome","dod","due","state","evidence_or_blocker","support"],p,d)
        if a.get("owner") not in roles:d.append(f"{p}:unknown_owner")
    agenda_submitters=set()
    for i,a in enumerate(ag):
        p=f"agenda:{i}";need(a,["submitted_by","topic","desired_outcome","priority","minutes","sensitive"],p,d)
        if a.get("submitted_by") not in roles:d.append(f"{p}:unknown_submitter")
        else:agenda_submitters.add(a.get("submitted_by"))
    if not roles.issubset(agenda_submitters):d.append("agenda:not_two_way")
    for a in fb:
        p=f"feedback:{a.get('id','?')}";need(a,["situation","behavior","impact","source","confidence","context_invitation","request"],p,d)
        if a.get("trait_or_intent_label"):d.append(f"{p}:trait_or_intent_label")
    for i,a in enumerate(qs):
        p=f"question:{i}";need(a,["text","open","neutral","purpose"],p,d)
        if a.get("open") is not True or a.get("neutral") is not True:d.append(f"{p}:leading_or_closed")
    for i,a in enumerate(sp):
        p=f"support:{i}";need(a,["goal","owner","manager_support","success_evidence","review_date"],p,d)
        if a.get("owner") not in roles:d.append(f"{p}:unknown_owner")
    manager_commitment=False
    for a in cm:
        p=f"commitment:{a.get('id','?')}";need(a,["owner","outcome","dod","due","dependency","support","evidence","follow_up"],p,d)
        if a.get("owner") not in roles:d.append(f"{p}:unknown_owner")
        if a.get("owner")==c.get("manager_id"):manager_commitment=True
    if not manager_commitment:d.append("commitments:manager_commitment_missing")
    for i,a in enumerate(x.get("sensitive_routes",[])):
        need(a,["topic_type","route","owner","privacy_limit","status"],f"sensitive_route:{i}",d)
        if a.get("status") not in {"NOT_TRIGGERED","PENDING_HUMAN_HANDOFF"}:d.append(f"sensitive_route:{i}:invalid_status")
    gate=x.get("requested_gate")
    if gate not in {"SESSION","CONFIRMATION"}:d.append("requested_gate:invalid")
    summary=x.get("summary",{})
    if gate=="CONFIRMATION":need(summary,["facts","participant_corrections","decisions","open_questions","commitment_ids","status"],"summary",d)
    if summary and summary.get("status") not in {"NOT_APPLICABLE","PENDING_PARTICIPANT_CONFIRMATION"}:d.append("summary:unauthorized_status")
    tests={a.get("type"):a for a in x.get("tests",[]) if isinstance(a,dict)}
    for t in TESTS:
        if tests.get(t,{}).get("status")!="PASS" or not ok(tests.get(t,{}).get("evidence")):d.append(f"test:{t}:not_pass")
    reviews={a.get("type"):a for a in x.get("reviews",[]) if isinstance(a,dict)}
    for r in {"MANAGER_PREP","PEOPLE_POLICY_PRIVACY"}:
        if reviews.get(r,{}).get("status")!="PASS" or not ok(reviews.get(r,{}).get("reviewer")) or not ok(reviews.get(r,{}).get("evidence")):g.append(f"review:{r}:not_pass")
    final="PARTICIPANT_CONFIRMATION" if gate=="CONFIRMATION" else "FINAL_HUMAN_1ON1"
    fr=reviews.get(final,{})
    if fr.get("status")!="PENDING" or not ok(fr.get("reviewer")) or not ok(fr.get("evidence")):d.append(f"review:{final}:must_be_pending")
    for f in sorted(set(x.get("forbidden_flags",[]))&FLAGS):d.append(f"forbidden_flag:{f}")
    for s in sorted(set(x.get("published_states",[]))&STATES):d.append(f"forbidden_state:{s}")
    req={"session_contract","evidence_commitment_brief","two_way_agenda","sbi_questions","support_development","commitment_ledger","confirmation_review_audit"};miss=req-set(x.get("output_sections",[]))
    if miss:d.append("output_sections:missing:"+",".join(sorted(miss)))
    d=sorted(set(d));g=sorted(set(g));state="NOT_READY" if d else("READY_FOR_MANAGER_REVIEW" if g else("READY_FOR_PARTICIPANT_CONFIRMATION" if gate=="CONFIRMATION" else"READY_FOR_HUMAN_1ON1"))
    return{"skill":"management-one-on-one","state":state,"defect_count":len(d),"defects":d,"review_gap_count":len(g),"review_gaps":g,"counts":{"evidence":len(ev),"prior_commitments":len(pm),"agenda_topics":len(ag),"feedback_cards":len(fb),"questions":len(qs),"support_experiments":len(sp),"commitments":len(cm),"tests_passed":sum(1 for a in tests.values() if a.get("status")=="PASS"),"reviews_passed":sum(1 for a in reviews.values() if a.get("status")=="PASS")},"warning":"STATIC PASS does not prove D10 real-case effectiveness, privacy outcome, token cost, duration, adoption, or people impact."}

def main()->int:
    if len(sys.argv)!=2:print("Usage: evaluate_management_one_on_one.py <input.json>",file=sys.stderr);return 2
    try:r=validate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    except Exception as e:r={"state":"NOT_READY","defects":[f"input_error:{e}"]}
    print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__":raise SystemExit(main())
