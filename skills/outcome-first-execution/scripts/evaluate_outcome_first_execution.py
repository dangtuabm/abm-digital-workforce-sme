#!/usr/bin/env python3
"""Fail-closed evaluator for an Outcome Execution Control Pack."""
import argparse,json
from pathlib import Path

FORBIDDEN_FLAGS={"orphan_activity_counted","fake_actual","fake_progress","fake_gate_pass","forecast_committed","prerequisite_skipped","baseline_changed","target_changed","scope_changed","due_changed","risk_hidden","auto_reallocated","auto_approved","auto_pivoted","auto_paused","auto_stopped"}
FORBIDDEN_STATES={"APPROVED","RESEQUENCED","REBASELINED","PIVOTED","PAUSED","STOPPED","EXECUTED"}
TEST_TYPES={"outcome_metric","value_trace","milestone_gate","readiness_capacity","forecast_variance","change_stop_control","execution_boundary"}
REVIEW_TYPES={"OUTCOME_OWNER","METRIC_DATA","DOMAIN_RESOURCE","FINAL_EXECUTION_DECISION"}

def load_json(p): return json.loads(p.read_text(encoding="utf-8"))
def present(x,*ks): return all(k in x and x[k] not in (None,"",[]) for k in ks)
def ids(xs,k): return {x.get(k) for x in xs if x.get(k)}
def scan(x,path="root"):
    flags=[];states=[]
    if isinstance(x,dict):
        for k,v in x.items():
            p=f"{path}.{k}"
            if k in FORBIDDEN_FLAGS and v is True: flags.append(p)
            if k in {"status","state"} and v in FORBIDDEN_STATES: states.append(f"{p}={v}")
            a,b=scan(v,p);flags+=a;states+=b
    elif isinstance(x,list):
        for i,v in enumerate(x):
            a,b=scan(v,f"{path}[{i}]");flags+=a;states+=b
    return flags,states

def evaluate(d):
    e=[];w=[];c=d.get("contract",{});o=d.get("outcome",{})
    metrics=d.get("metrics",[]);sources=d.get("sources",[]);wps=d.get("work_packages",[])
    ms=d.get("milestones",[]);criteria=d.get("criteria",[]);deps=d.get("dependencies",[])
    resources=d.get("resources",[]);forecasts=d.get("forecasts",[]);vars=d.get("variances",[])
    risks=d.get("risks",[]);stops=d.get("stop_criteria",[]);opts=d.get("options",[])
    changes=d.get("changes",[]);record=d.get("record",{});snapshot=d.get("execution_snapshot",{})

    contract_bad=0
    if not present(c,"initiative_id","source_id","source_version","source_hash","classification","outcome_owner","decision_owner","review_cadence","correction_owner","retention","prohibited_actions") or c.get("source_status")!="ACTIVE":
        e.append("contract: source/governance/decision rights incomplete");contract_bad+=1
    if not present(o,"business_reason","outcome_statement","beneficiary","value_metric_id","baseline","target","due","in_scope","non_goals","stop_criteria_ids"):
        e.append("outcome: value/baseline/target/due/scope incomplete");contract_bad+=1
    if o.get("activity_as_outcome") is True: e.append("outcome: activity cannot replace outcome");contract_bad+=1

    source_bad=0;source_ids=ids(sources,"source_id")
    for i,x in enumerate(sources):
        if not present(x,"source_id","version","hash","locator","captured_at","access_status","freshness_status") or x.get("access_status")!="AUTHORIZED" or x.get("freshness_status")!="CURRENT" or x.get("active") is not True:
            e.append(f"source[{i}]: provenance/access/freshness invalid");source_bad+=1

    metric_bad=0;metric_ids=ids(metrics,"metric_id")
    for i,x in enumerate(metrics):
        if not present(x,"metric_id","definition","formula","unit","grain","owner","system_of_record","baseline_value","baseline_at","target_value","target_at","actual_value","actual_at","freshness_status","source_refs"):
            e.append(f"metric[{i}]: contract/baseline/target/actual incomplete");metric_bad+=1;continue
        if x.get("freshness_status")!="CURRENT" or not set(x.get("source_refs",[])).issubset(source_ids):
            e.append(f"metric[{i}]: stale or unknown source");metric_bad+=1
    if o.get("value_metric_id") not in metric_ids: e.append("outcome: value metric missing");metric_bad+=1

    trace_bad=0;wp_ids=ids(wps,"work_package_id");milestone_ids=ids(ms,"milestone_id")
    dep_ids=ids(deps,"dependency_id");resource_ids=ids(resources,"resource_id")
    for i,x in enumerate(wps):
        if not present(x,"work_package_id","deliverable","owner","dod","milestone_id","outcome_metric_ids","status"):
            e.append(f"work_package[{i}]: deliverable/owner/DoD/trace incomplete");trace_bad+=1;continue
        if x.get("milestone_id") not in milestone_ids or not set(x.get("outcome_metric_ids",[])).issubset(metric_ids):
            e.append(f"work_package[{i}]: orphan milestone/outcome trace");trace_bad+=1
        if not set(x.get("dependency_ids",[])).issubset(dep_ids) or not set(x.get("resource_ids",[])).issubset(resource_ids):
            e.append(f"work_package[{i}]: unknown dependency/resource");trace_bad+=1

    gate_bad=0;criterion_ids=ids(criteria,"criterion_id")
    by_ms={m.get("milestone_id"):set(m.get("criterion_ids",[])) for m in ms if m.get("milestone_id")}
    for i,x in enumerate(ms):
        if not present(x,"milestone_id","criterion_ids","threshold_authorized","evidence_refs","reviewer","status"):
            e.append(f"milestone[{i}]: threshold/evidence/reviewer incomplete");gate_bad+=1
        if not set(x.get("evidence_refs",[])).issubset(source_ids): e.append(f"milestone[{i}]: unknown evidence");gate_bad+=1
        if not set(x.get("prerequisite_ids",[])).issubset(milestone_ids): e.append(f"milestone[{i}]: unknown prerequisite");gate_bad+=1
    for i,x in enumerate(criteria):
        if not present(x,"criterion_id","milestone_id","critical","result","evidence_refs","reviewer","verification_status") or x.get("milestone_id") not in milestone_ids:
            e.append(f"criterion[{i}]: gate/result/evidence/reviewer incomplete");gate_bad+=1;continue
        if not set(x.get("evidence_refs",[])).issubset(source_ids): e.append(f"criterion[{i}]: unknown evidence");gate_bad+=1
        if x.get("critical") is True and (x.get("result")!="PASS" or x.get("verification_status")!="VERIFIED"):
            e.append(f"criterion[{i}]: critical criterion not verified PASS");gate_bad+=1
    for mid,known in by_ms.items():
        actual={x.get("criterion_id") for x in criteria if x.get("milestone_id")==mid}
        if known-actual: e.append(f"milestone {mid}: criteria omitted {', '.join(sorted(known-actual))}");gate_bad+=1

    ready_bad=0
    for i,x in enumerate(deps):
        if not present(x,"dependency_id","owner","state","critical_path","slack","evidence","fallback") or x.get("state") not in {"READY","RESOLVED"}:
            e.append(f"dependency[{i}]: state/path/slack/evidence/fallback invalid");ready_bad+=1
    for i,x in enumerate(resources):
        if not present(x,"resource_id","owner","capacity_available","wip","wip_limit","access_status","evidence") or x.get("access_status")!="AUTHORIZED" or x.get("capacity_available") is not True or x.get("wip",1)>x.get("wip_limit",0):
            e.append(f"resource[{i}]: capacity/WIP/access invalid");ready_bad+=1

    forecast_bad=0;forecast_ids=ids(forecasts,"forecast_id")
    for i,x in enumerate(forecasts):
        if not present(x,"forecast_id","metric_id","range_low","range_high","confidence","assumptions","evidence_refs","evidence_at","scenario") or x.get("metric_id") not in metric_ids or not set(x.get("evidence_refs",[])).issubset(source_ids):
            e.append(f"forecast[{i}]: range/confidence/assumption/evidence invalid");forecast_bad+=1
        elif x.get("range_low")>x.get("range_high") or not (0<x.get("confidence",0)<=1):
            e.append(f"forecast[{i}]: invalid range/confidence");forecast_bad+=1
    variance_bad=0;variance_ids=ids(vars,"variance_id")
    for i,x in enumerate(vars):
        if not present(x,"variance_id","metric_id","type","baseline","actual_or_forecast","cause","impact","trigger","evidence_refs","status") or x.get("metric_id") not in metric_ids or not set(x.get("evidence_refs",[])).issubset(source_ids):
            e.append(f"variance[{i}]: baseline/cause/impact/evidence incomplete");variance_bad+=1

    control_bad=0;risk_ids=ids(risks,"risk_id");stop_ids=ids(stops,"stop_id");option_ids=ids(opts,"option_id");change_ids=ids(changes,"change_id")
    if not set(o.get("stop_criteria_ids",[])).issubset(stop_ids): e.append("outcome: stop criteria omitted");control_bad+=1
    for i,x in enumerate(risks):
        if not present(x,"risk_id","severity","trigger","impact","control","owner","evidence_refs") or not set(x.get("evidence_refs",[])).issubset(source_ids): e.append(f"risk[{i}]: trigger/control/owner/evidence incomplete");control_bad+=1
    for i,x in enumerate(stops):
        if not present(x,"stop_id","trigger","evidence_refs","owner","response_sla","safe_state") or not set(x.get("evidence_refs",[])).issubset(source_ids): e.append(f"stop[{i}]: trigger/evidence/owner/SLA/safe state incomplete");control_bad+=1
    for i,x in enumerate(opts):
        if not present(x,"option_id","decision","outcome_impact","time_cost_resource","risk","reversibility","prerequisites","rationale","status") or x.get("status")!="PROPOSED": e.append(f"option[{i}]: trade-off/prerequisite/rationale invalid");control_bad+=1
    for i,x in enumerate(changes):
        if not present(x,"change_id","reason","evidence_refs","before","change","after","impact","approver","status","verification","rollback") or not set(x.get("evidence_refs",[])).issubset(source_ids) or x.get("status")!="REVIEWED": e.append(f"change[{i}]: authority/impact/verification/rollback incomplete");control_bad+=1

    coverage_bad=0
    mapping=[("metric_ids",metric_ids),("source_ids",source_ids),("work_package_ids",wp_ids),("milestone_ids",milestone_ids),("criterion_ids",criterion_ids),("dependency_ids",dep_ids),("resource_ids",resource_ids),("forecast_ids",forecast_ids),("variance_ids",variance_ids),("risk_ids",risk_ids),("stop_ids",stop_ids),("option_ids",option_ids),("change_ids",change_ids)]
    for field,known in mapping:
        actual=set(record.get(field,[])) if isinstance(record.get(field),list) else set()
        if known-actual: e.append(f"record: {field} omitted {', '.join(sorted(known-actual))}");coverage_bad+=1

    flags,states=scan(d);e += [f"forbidden flag: {x}" for x in flags]+[f"forbidden state: {x}" for x in states]
    tests=d.get("tests",[]);tt={x.get("test_type") for x in tests};test_bad=0
    if not TEST_TYPES.issubset(tt): e.append("tests: seven required types missing");test_bad+=1
    for i,x in enumerate(tests):
        if x.get("passed") is not True or not present(x,"evidence","reviewer","date"): e.append(f"test[{i}]: failed or evidence incomplete");test_bad+=1
    reviews=d.get("reviews",[]);rt={x.get("review_type") for x in reviews};review_bad=0
    if not REVIEW_TYPES.issubset(rt): e.append("reviews: mandatory types missing");review_bad+=1
    for i,x in enumerate(reviews):
        if not present(x,"review_type","reviewer","status","evidence"): e.append(f"review[{i}]: incomplete");review_bad+=1;continue
        if x.get("review_type")!="FINAL_EXECUTION_DECISION" and x.get("status")!="PASS": e.append(f"review[{i}]: required review not PASS");review_bad+=1
        if x.get("review_type")=="FINAL_EXECUTION_DECISION" and x.get("status") not in {"PENDING","PASS"}: e.append(f"review[{i}]: final decision status invalid");review_bad+=1

    critical=contract_bad+source_bad+metric_bad+trace_bad+gate_bad+ready_bad+forecast_bad+variance_bad+control_bad+coverage_bad+len(flags)+len(states)+test_bad+review_bad
    complete=snapshot.get("status")=="COMPLETE" and set(snapshot.get("metric_ids",[]))==metric_ids and set(snapshot.get("milestone_ids",[]))==milestone_ids
    if critical: state="NOT_READY"
    elif complete: state="READY_FOR_HUMAN_EXECUTION_DECISION"
    elif forecasts and vars: state="READY_FOR_EXECUTION_REVIEW"
    else: state="EXECUTION_BASELINED"
    if state=="READY_FOR_HUMAN_EXECUTION_DECISION": w.append("human decision remains; engine does not mutate, reallocate, approve, rebaseline, pivot, pause or stop")
    return {"initiative_id":c.get("initiative_id"),"state":state,"metrics":{"metrics":len(metrics),"sources":len(sources),"work_packages":len(wps),"milestones":len(ms),"criteria":len(criteria),"dependencies":len(deps),"resources":len(resources),"forecasts":len(forecasts),"variances":len(vars),"options":len(opts),"contract_violations":contract_bad,"source_violations":source_bad,"metric_violations":metric_bad,"trace_violations":trace_bad,"gate_violations":gate_bad,"readiness_violations":ready_bad,"forecast_violations":forecast_bad,"variance_violations":variance_bad,"control_violations":control_bad,"coverage_violations":coverage_bad,"forbidden_flags":len(flags),"unauthorized_states":len(states),"test_types":len(tt),"critical_defects":critical},"errors":e,"warnings":w}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",type=Path);p.add_argument("--output",type=Path);a=p.parse_args();r=evaluate(load_json(a.input));s=json.dumps(r,ensure_ascii=False,indent=2);print(s)
    if a.output:a.output.write_text(s+"\n",encoding="utf-8")
    return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__": raise SystemExit(main())
