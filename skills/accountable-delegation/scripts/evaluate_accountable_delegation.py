#!/usr/bin/env python3
"""Fail-closed evaluator for an Accountable Delegation Contract."""
import argparse,json
from collections import Counter
from pathlib import Path

FORBIDDEN_FLAGS={"auto_assigned","forced_acceptance","expanded_scope","spent_without_approval","access_granted","fake_done","method_overridden"}
FORBIDDEN_STATES={"ASSIGNED","SENT","EXECUTING","DONE","APPROVED","ACCESS_GRANTED"}
TEST_TYPES={"mandate_authority","outcome_dod","delegate_fit_acceptance","authority_boundary","resource_dependency","escalation_rollback","execution_boundary"}
REVIEW_TYPES={"MANDATE_OWNER","DELEGATE_ACCEPTANCE","SECURITY_ACCESS","FINAL_ACTIVATION"}

def load_json(path):
    return json.loads(path.read_text(encoding="utf-8"))

def present(x,*keys):
    return all(k in x and x[k] not in (None,"",[]) for k in keys)

def ids(items,key):
    return {x.get(key) for x in items if x.get(key)}

def scan_forbidden(node,path="root"):
    flags=[];states=[]
    if isinstance(node,dict):
        for k,v in node.items():
            p=f"{path}.{k}"
            if k in FORBIDDEN_FLAGS and v is True: flags.append(p)
            if k in {"status","state"} and v in FORBIDDEN_STATES: states.append(p+f"={v}")
            a,b=scan_forbidden(v,p);flags+=a;states+=b
    elif isinstance(node,list):
        for i,v in enumerate(node):
            a,b=scan_forbidden(v,f"{path}[{i}]");flags+=a;states+=b
    return flags,states

def evaluate(d):
    errors=[];warnings=[]
    c=d.get("contract",{});o=d.get("outcome",{});g=d.get("delegate",{})
    dels=d.get("deliverables",[]);auth=d.get("authority_envelope",[])
    res=d.get("resources",[]);deps=d.get("dependencies",[]);risks=d.get("risks",[])
    checks=d.get("checkpoints",[]);esc=d.get("escalations",[]);record=d.get("record",{})

    contract_bad=0
    if not present(c,"contract_id","principal_id","authority_evidence","authority_locator","classification","valid_until","validity_status","correction_owner","prohibited_actions") or c.get("validity_status")!="ACTIVE":
        errors.append("contract: mandate/authority/validity incomplete");contract_bad+=1
    if not present(o,"business_reason","outcome_statement","success_metric","baseline","target","due_or_trigger","in_scope","non_goals"):
        errors.append("outcome: reason/metric/scope/non-goals/due incomplete");contract_bad+=1
    if o.get("activity_as_outcome") is True:
        errors.append("outcome: activity cannot replace outcome");contract_bad+=1

    delegate_bad=0;acceptance_pending=False
    if not present(g,"delegate_id","delegate_type","competence_status","competence_evidence","capacity_status","availability","conflict_status"):
        errors.append("delegate: identity/fit/capacity/conflict incomplete");delegate_bad+=1
    if g.get("competence_status")!="VERIFIED" or g.get("capacity_status")!="AVAILABLE" or g.get("conflict_status")!="CLEAR":
        errors.append("delegate: competence/capacity/conflict invalid");delegate_bad+=1
    if g.get("delegate_type")=="A.I" and not (present(g,"human_supervisor","runtime_capability") and g.get("runtime_capability")=="VERIFIED"):
        errors.append("delegate: A.I requires human supervisor and verified runtime capability");delegate_bad+=1
    ast=g.get("acceptance_status")
    if ast=="EXPLICIT_ACCEPTED":
        if not present(g,"acceptance_statement","accepted_at","acceptance_locator"):
            errors.append("delegate: explicit acceptance lacks evidence");delegate_bad+=1
    elif ast in {"PENDING","RENEGOTIATE"}:
        acceptance_pending=True;warnings.append(f"delegate acceptance remains {ast}")
    else:
        errors.append("delegate: acceptance invalid or declined");delegate_bad+=1

    deliverable_bad=0
    if not dels: errors.append("deliverables: none");deliverable_bad+=1
    for i,x in enumerate(dels):
        if not present(x,"deliverable_id","deliverable","acceptance_criteria","evidence_required","reviewer","due_or_trigger"):
            errors.append(f"deliverable[{i}]: DoD/evidence/reviewer/due incomplete");deliverable_bad+=1
        if x.get("status") not in {None,"RECORDED","DRAFT"}:
            errors.append(f"deliverable[{i}]: execution status not allowed");deliverable_bad+=1

    authority_bad=0;classes={x.get("class") for x in auth}
    if not {"ALLOWED","APPROVAL_REQUIRED","PROHIBITED"}.issubset(classes):
        errors.append("authority: three classes required");authority_bad+=1
    for i,x in enumerate(auth):
        if not present(x,"authority_id","class","action","limit","evidence","expiry"):
            errors.append(f"authority[{i}]: action/limit/evidence/expiry incomplete");authority_bad+=1

    readiness_bad=0
    for i,x in enumerate(res):
        if not present(x,"resource_id","owner","access_status","evidence","locator") or x.get("access_status")!="AUTHORIZED" or x.get("active") is not True:
            errors.append(f"resource[{i}]: access/readiness invalid");readiness_bad+=1
    for i,x in enumerate(deps):
        if not present(x,"dependency_id","owner","state","evidence","fallback") or x.get("state")!="READY":
            errors.append(f"dependency[{i}]: owner/state/evidence/fallback invalid");readiness_bad+=1
    for i,x in enumerate(risks):
        if not present(x,"risk_id","severity","control","owner","trigger"):
            errors.append(f"risk[{i}]: control/owner/trigger incomplete");readiness_bad+=1

    control_bad=0
    for i,x in enumerate(checks):
        if not present(x,"checkpoint_id","trigger_or_milestone","evidence","reviewer","purpose"):
            errors.append(f"checkpoint[{i}]: trigger/evidence/reviewer/purpose incomplete");control_bad+=1
    for i,x in enumerate(esc):
        if not present(x,"escalation_id","trigger","destination","response_sla","safe_fallback","stop_condition"):
            errors.append(f"escalation[{i}]: destination/SLA/fallback/stop incomplete");control_bad+=1

    coverage_bad=0
    mapping=[("deliverable_ids",ids(dels,"deliverable_id")),("resource_ids",ids(res,"resource_id")),("dependency_ids",ids(deps,"dependency_id")),("risk_ids",ids(risks,"risk_id")),("checkpoint_ids",ids(checks,"checkpoint_id")),("escalation_ids",ids(esc,"escalation_id"))]
    for field,known in mapping:
        actual=set(record.get(field,[])) if isinstance(record.get(field),list) else set()
        if known-actual:
            errors.append(f"record: {field} omitted {', '.join(sorted(known-actual))}");coverage_bad+=1

    flags,states=scan_forbidden(d)
    errors += [f"forbidden flag: {x}" for x in flags]+[f"forbidden state: {x}" for x in states]
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
        if x.get("review_type")!="FINAL_ACTIVATION" and x.get("status")!="PASS":
            errors.append(f"review[{i}]: required review not PASS");review_bad+=1
        if x.get("review_type")=="FINAL_ACTIVATION" and x.get("status") not in {"PENDING","PASS"}:
            errors.append(f"review[{i}]: final activation status invalid");review_bad+=1

    critical=contract_bad+delegate_bad+deliverable_bad+authority_bad+readiness_bad+control_bad+coverage_bad+len(flags)+len(states)+test_bad+review_bad
    state="NOT_READY" if critical else ("READY_FOR_DELEGATE_REVIEW" if acceptance_pending else "READY_FOR_HUMAN_ACTIVATION")
    if state=="READY_FOR_HUMAN_ACTIVATION": warnings.append("human authority must activate; engine does not assign, grant access, spend or execute")
    return {"contract_id":c.get("contract_id"),"state":state,"metrics":{"deliverables":len(dels),"authority_rules":len(auth),"resources":len(res),"dependencies":len(deps),"risks":len(risks),"checkpoints":len(checks),"escalations":len(esc),"delegate_violations":delegate_bad,"deliverable_violations":deliverable_bad,"authority_violations":authority_bad,"readiness_violations":readiness_bad,"control_violations":control_bad,"coverage_violations":coverage_bad,"forbidden_flags":len(flags),"unauthorized_states":len(states),"test_types":len(test_types),"critical_defects":critical},"errors":errors,"warnings":warnings}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",type=Path);p.add_argument("--output",type=Path);a=p.parse_args();r=evaluate(load_json(a.input));s=json.dumps(r,ensure_ascii=False,indent=2);print(s)
    if a.output:a.output.write_text(s+"\n",encoding="utf-8")
    return 0 if r["state"]!="NOT_READY" else 1

if __name__=="__main__": raise SystemExit(main())
