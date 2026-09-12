#!/usr/bin/env python3
"""Fail-closed evaluator for an Action Closure Evidence Pack."""
import argparse,json
from pathlib import Path

FORBIDDEN_FLAGS={"fake_progress","fake_done","auto_reminded","auto_escalated","owner_changed","due_changed","scope_changed","dod_changed","backdated_evidence","exception_hidden","auto_closed"}
FORBIDDEN_STATES={"SENT","REMINDED","ESCALATED","DONE","CLOSED","WAIVED","CANCELLED","REOPENED"}
TEST_TYPES={"action_contract","evidence_provenance","progress_verification","dependency_blocker","dod_closure","exception_change_control","execution_boundary"}
REVIEW_TYPES={"ACTION_OWNER","DOD_REVIEWER","DOMAIN_SECURITY","FINAL_CLOSURE"}

def load_json(path): return json.loads(path.read_text(encoding="utf-8"))
def present(x,*keys): return all(k in x and x[k] not in (None,"",[]) for k in keys)
def ids(items,key): return {x.get(key) for x in items if x.get(key)}

def scan(node,path="root"):
    flags=[];states=[]
    if isinstance(node,dict):
        for k,v in node.items():
            p=f"{path}.{k}"
            if k in FORBIDDEN_FLAGS and v is True: flags.append(p)
            if k in {"status","state"} and v in FORBIDDEN_STATES: states.append(f"{p}={v}")
            a,b=scan(v,p);flags+=a;states+=b
    elif isinstance(node,list):
        for i,v in enumerate(node):
            a,b=scan(v,f"{path}[{i}]");flags+=a;states+=b
    return flags,states

def evaluate(d):
    errors=[];warnings=[]
    c=d.get("contract",{});actions=d.get("actions",[]);sources=d.get("sources",[])
    events=d.get("progress_events",[]);deps=d.get("dependencies",[]);blocks=d.get("blockers",[])
    criteria=d.get("criteria",[]);exceptions=d.get("exceptions",[]);escalations=d.get("escalations",[])
    candidate=d.get("closure_candidate",{});record=d.get("record",{})

    contract_bad=0
    if not present(c,"closure_set_id","source_id","source_version","source_hash","scope","classification","owner","correction_owner","retention","prohibited_actions") or c.get("source_status")!="ACTIVE":
        errors.append("contract: source/scope/governance incomplete");contract_bad+=1

    action_bad=0;action_ids=ids(actions,"action_id")
    if not actions: errors.append("actions: none");action_bad+=1
    for i,x in enumerate(actions):
        if not present(x,"action_id","outcome","owner_id","owner_acceptance_status","owner_acceptance_evidence","due_or_trigger","dod_criteria_ids","reviewer","authority_evidence"):
            errors.append(f"action[{i}]: contract/owner/due/DoD/reviewer incomplete");action_bad+=1
        if x.get("owner_acceptance_status")!="EXPLICIT_ACCEPTED":
            errors.append(f"action[{i}]: owner acceptance invalid");action_bad+=1
        if x.get("status") not in {None,"RECORDED","OPEN","AT_RISK","BLOCKED"}:
            errors.append(f"action[{i}]: execution/closure status not allowed");action_bad+=1

    source_bad=0;source_ids=ids(sources,"source_id")
    for i,x in enumerate(sources):
        if not present(x,"source_id","version","hash","locator","owner","captured_at","access_status","freshness_status") or x.get("access_status")!="AUTHORIZED" or x.get("freshness_status")!="CURRENT" or x.get("active") is not True:
            errors.append(f"source[{i}]: provenance/access/freshness invalid");source_bad+=1

    event_bad=0;event_ids=ids(events,"event_id")
    for i,x in enumerate(events):
        if not present(x,"event_id","action_id","actor","timestamp","reported_state","forecast","verification_state") or x.get("action_id") not in action_ids:
            errors.append(f"event[{i}]: actor/time/action/forecast incomplete");event_bad+=1;continue
        refs=x.get("evidence_refs",[])
        if x.get("verification_state")=="VERIFIED" and (not refs or not set(refs).issubset(source_ids)):
            errors.append(f"event[{i}]: VERIFIED without valid evidence");event_bad+=1
        if x.get("reported_state") in {"COMPLETE","100%"} and x.get("verification_state")!="VERIFIED":
            errors.append(f"event[{i}]: completion only reported");event_bad+=1

    readiness_bad=0;dep_ids=ids(deps,"dependency_id");block_ids=ids(blocks,"blocker_id")
    for i,x in enumerate(deps):
        if not present(x,"dependency_id","owner","state","evidence","fallback") or x.get("state") not in {"READY","RESOLVED"}:
            errors.append(f"dependency[{i}]: owner/state/evidence/fallback invalid");readiness_bad+=1
    for i,x in enumerate(blocks):
        if not present(x,"blocker_id","owner","state","impact","control","escalation_id") or x.get("state") not in {"CONTROLLED","RESOLVED"}:
            errors.append(f"blocker[{i}]: owner/state/impact/control/escalation invalid");readiness_bad+=1
    for i,x in enumerate(escalations):
        if not present(x,"escalation_id","trigger","destination","response_sla","safe_fallback","stop_condition"):
            errors.append(f"escalation[{i}]: trigger/destination/SLA/fallback/stop incomplete");readiness_bad+=1

    criterion_bad=0;criterion_ids=ids(criteria,"criterion_id")
    by_action={a.get("action_id"):set(a.get("dod_criteria_ids",[])) for a in actions if a.get("action_id")}
    for i,x in enumerate(criteria):
        if not present(x,"criterion_id","action_id","criterion","result","evidence_refs","reviewer","review_status") or x.get("action_id") not in action_ids:
            errors.append(f"criterion[{i}]: action/result/evidence/reviewer incomplete");criterion_bad+=1;continue
        if not set(x.get("evidence_refs",[])).issubset(source_ids):
            errors.append(f"criterion[{i}]: unknown evidence ref");criterion_bad+=1
        if x.get("result")=="PASS" and x.get("review_status")!="VERIFIED":
            errors.append(f"criterion[{i}]: PASS not verified");criterion_bad+=1
    for aid,known in by_action.items():
        actual={x.get("criterion_id") for x in criteria if x.get("action_id")==aid}
        if known-actual:
            errors.append(f"action {aid}: criteria omitted {', '.join(sorted(known-actual))}");criterion_bad+=1

    exception_bad=0;exception_ids=ids(exceptions,"exception_id")
    for i,x in enumerate(exceptions):
        if not present(x,"exception_id","action_id","type","reason","impact","authority_evidence","source_locator","status") or x.get("status")!="REVIEWED":
            errors.append(f"exception[{i}]: reason/impact/authority/history incomplete");exception_bad+=1

    coverage_bad=0
    mapping=[("action_ids",action_ids),("source_ids",source_ids),("event_ids",event_ids),("dependency_ids",dep_ids),("blocker_ids",block_ids),("criterion_ids",criterion_ids),("exception_ids",exception_ids)]
    for field,known in mapping:
        actual=set(record.get(field,[])) if isinstance(record.get(field),list) else set()
        if known-actual:
            errors.append(f"record: {field} omitted {', '.join(sorted(known-actual))}");coverage_bad+=1

    flags,states=scan(d);errors += [f"forbidden flag: {x}" for x in flags]+[f"forbidden state: {x}" for x in states]
    tests=d.get("tests",[]);test_types={x.get("test_type") for x in tests};test_bad=0
    if not TEST_TYPES.issubset(test_types): errors.append("tests: seven required types missing");test_bad+=1
    for i,x in enumerate(tests):
        if x.get("passed") is not True or not present(x,"evidence","reviewer","date"):
            errors.append(f"test[{i}]: failed or evidence incomplete");test_bad+=1
    reviews=d.get("reviews",[]);review_types={x.get("review_type") for x in reviews};review_bad=0
    if not REVIEW_TYPES.issubset(review_types): errors.append("reviews: mandatory types missing");review_bad+=1
    for i,x in enumerate(reviews):
        if not present(x,"review_type","reviewer","status","evidence"):
            errors.append(f"review[{i}]: incomplete");review_bad+=1;continue
        if x.get("review_type")!="FINAL_CLOSURE" and x.get("status")!="PASS":
            errors.append(f"review[{i}]: required review not PASS");review_bad+=1
        if x.get("review_type")=="FINAL_CLOSURE" and x.get("status") not in {"PENDING","PASS"}:
            errors.append(f"review[{i}]: final closure status invalid");review_bad+=1

    critical=contract_bad+action_bad+source_bad+event_bad+readiness_bad+criterion_bad+exception_bad+coverage_bad+len(flags)+len(states)+test_bad+review_bad
    all_pass=bool(criteria) and all(x.get("result")=="PASS" and x.get("review_status")=="VERIFIED" for x in criteria)
    complete=candidate.get("status")=="COMPLETE" and set(candidate.get("action_ids",[]))==action_ids and all_pass
    if critical: state="NOT_READY"
    elif complete: state="READY_FOR_HUMAN_CLOSURE"
    elif candidate.get("status") in {"DRAFT","COMPLETE"}: state="READY_FOR_CLOSURE_REVIEW"
    else: state="MONITORING_READY"
    if state=="READY_FOR_HUMAN_CLOSURE": warnings.append("final human closure remains; engine does not remind, escalate, mutate, waive or close")
    return {"closure_set_id":c.get("closure_set_id"),"state":state,"metrics":{"actions":len(actions),"sources":len(sources),"events":len(events),"dependencies":len(deps),"blockers":len(blocks),"criteria":len(criteria),"exceptions":len(exceptions),"action_violations":action_bad,"source_violations":source_bad,"event_violations":event_bad,"readiness_violations":readiness_bad,"criterion_violations":criterion_bad,"exception_violations":exception_bad,"coverage_violations":coverage_bad,"forbidden_flags":len(flags),"unauthorized_states":len(states),"test_types":len(test_types),"critical_defects":critical},"errors":errors,"warnings":warnings}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",type=Path);p.add_argument("--output",type=Path);a=p.parse_args();r=evaluate(load_json(a.input));s=json.dumps(r,ensure_ascii=False,indent=2);print(s)
    if a.output:a.output.write_text(s+"\n",encoding="utf-8")
    return 0 if r["state"]!="NOT_READY" else 1

if __name__=="__main__": raise SystemExit(main())
