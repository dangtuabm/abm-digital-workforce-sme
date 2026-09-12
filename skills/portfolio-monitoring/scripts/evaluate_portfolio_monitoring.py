#!/usr/bin/env python3
"""Fail-closed evaluator for a Portfolio Decision Radar."""
import argparse,json
from pathlib import Path

FORBIDDEN_FLAGS={"initiative_hidden","fake_green","fake_actual","fake_forecast","threshold_changed","as_of_changed","baseline_changed","double_counted","risk_hidden","auto_alerted","auto_reprioritized","auto_reallocated","auto_resequenced","auto_approved","auto_paused","auto_stopped"}
FORBIDDEN_STATES={"REPRIORITIZED","REALLOCATED","RESEQUENCED","APPROVED","ALERTED","PAUSED","STOPPED","KILLED"}
TEST_TYPES={"portfolio_census","metric_comparability","source_freshness","dependency_resource","exposure_exception","decision_brief","execution_boundary"}
REVIEW_TYPES={"PORTFOLIO_SPONSOR","METRIC_DATA","FINANCE_RESOURCE_DOMAIN","FINAL_PORTFOLIO_DECISION"}

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
    e=[];w=[];c=d.get("contract",{});src=d.get("sources",[]);cms=d.get("canonical_metrics",[])
    ins=d.get("initiatives",[]);snaps=d.get("snapshots",[]);deps=d.get("dependencies",[])
    pools=d.get("resource_pools",[]);cols=d.get("resource_collisions",[]);risks=d.get("risks",[])
    exs=d.get("exceptions",[]);decs=d.get("decision_requests",[]);record=d.get("record",{});snapshot=d.get("portfolio_snapshot",{})

    contract_bad=0
    if not present(c,"portfolio_id","version","source_hash","sponsor","as_of","cadence","classification","inclusion","exclusion","strategic_objectives","decision_rights","correction_owner","retention","prohibited_actions") or c.get("status")!="ACTIVE":
        e.append("contract: scope/as-of/sponsor/rights incomplete");contract_bad+=1

    source_bad=0;source_ids=ids(src,"source_id")
    for i,x in enumerate(src):
        if not present(x,"source_id","version","hash","locator","owner","captured_at","access_status","freshness_status") or x.get("access_status")!="AUTHORIZED" or x.get("freshness_status")!="CURRENT" or x.get("active") is not True:
            e.append(f"source[{i}]: provenance/access/freshness invalid");source_bad+=1

    metric_bad=0;cm_ids=ids(cms,"metric_id")
    for i,x in enumerate(cms):
        if not present(x,"metric_id","definition","formula","unit","currency","grain","time_horizon","owner","system_of_record","freshness_sla","thresholds","aggregation_rule"):
            e.append(f"canonical_metric[{i}]: definition/unit/threshold/aggregation incomplete");metric_bad+=1

    census_bad=0;initiative_ids=ids(ins,"initiative_id")
    for i,x in enumerate(ins):
        if not present(x,"initiative_id","outcome","owner","sponsor","strategic_theme","authorized_priority","lifecycle","baseline","target","due","source_refs") or not set(x.get("source_refs",[])).issubset(source_ids):
            e.append(f"initiative[{i}]: census/outcome/priority/source incomplete");census_bad+=1

    snapshot_bad=0;snapshot_ids=ids(snaps,"snapshot_id")
    for i,x in enumerate(snaps):
        if not present(x,"snapshot_id","initiative_id","canonical_metric_id","local_metric_id","comparability_status","conversion","actual","actual_at","forecast_low","forecast_high","confidence","source_refs","verification_status"):
            e.append(f"snapshot[{i}]: metric/actual/forecast/source incomplete");snapshot_bad+=1;continue
        if x.get("initiative_id") not in initiative_ids or x.get("canonical_metric_id") not in cm_ids or not set(x.get("source_refs",[])).issubset(source_ids):
            e.append(f"snapshot[{i}]: unknown initiative/metric/source");snapshot_bad+=1
        if x.get("comparability_status")=="COMPARABLE":
            if not (0<x.get("confidence",0)<=1) or x.get("forecast_low")>x.get("forecast_high") or x.get("verification_status")!="VERIFIED":
                e.append(f"snapshot[{i}]: comparable claim/range/confidence invalid");snapshot_bad+=1
        elif x.get("comparability_status")=="NOT_COMPARABLE":
            if not present(x,"non_comparable_reason"): e.append(f"snapshot[{i}]: non-comparable reason missing");snapshot_bad+=1
            else: w.append(f"snapshot[{i}] excluded from aggregation: {x.get('non_comparable_reason')}")
        else: e.append(f"snapshot[{i}]: comparability status invalid");snapshot_bad+=1

    network_bad=0;dep_ids=ids(deps,"dependency_id")
    for i,x in enumerate(deps):
        if not present(x,"dependency_id","predecessor_id","successor_id","interface_owner","state","criticality","impact","fallback","evidence_refs") or x.get("predecessor_id") not in initiative_ids or x.get("successor_id") not in initiative_ids or x.get("state") not in {"READY","CONTROLLED","RESOLVED"} or not set(x.get("evidence_refs",[])).issubset(source_ids):
            e.append(f"dependency[{i}]: network/state/owner/impact/fallback invalid");network_bad+=1
    pool_ids=ids(pools,"resource_id");collision_ids=ids(cols,"collision_id");controlled_resources={x.get("resource_id") for x in cols if x.get("status")=="CONTROLLED"}
    for i,x in enumerate(pools):
        if not present(x,"resource_id","period","capacity","committed_demand","forecast_demand","owner","allocation_evidence","source_refs") or not set(x.get("source_refs",[])).issubset(source_ids):
            e.append(f"resource_pool[{i}]: period/capacity/demand/evidence incomplete");network_bad+=1;continue
        if max(x.get("committed_demand",0),x.get("forecast_demand",0))>x.get("capacity",0) and x.get("resource_id") not in controlled_resources:
            e.append(f"resource_pool[{i}]: overcapacity collision not controlled");network_bad+=1
    for i,x in enumerate(cols):
        if not present(x,"collision_id","resource_id","initiative_ids","demand","capacity","impact","owner","fallback","evidence_refs","status") or x.get("resource_id") not in pool_ids or not set(x.get("initiative_ids",[])).issubset(initiative_ids) or not set(x.get("evidence_refs",[])).issubset(source_ids) or x.get("status")!="CONTROLLED":
            e.append(f"collision[{i}]: resource/initiatives/impact/control invalid");network_bad+=1

    exposure_bad=0;risk_ids=ids(risks,"risk_id")
    for i,x in enumerate(risks):
        if not present(x,"risk_id","initiative_ids","likelihood","impact","correlation_group","concentration","owner","control","trigger","evidence_refs") or not set(x.get("initiative_ids",[])).issubset(initiative_ids) or not set(x.get("evidence_refs",[])).issubset(source_ids):
            e.append(f"risk[{i}]: exposure/correlation/concentration/control invalid");exposure_bad+=1
    exception_bad=0;exception_ids=ids(exs,"exception_id")
    for i,x in enumerate(exs):
        if not present(x,"exception_id","type","initiative_ids","threshold_id","observed_value","breach_direction","severity","impact","urgency","owner","evidence_refs","decision_trigger","status") or not set(x.get("initiative_ids",[])).issubset(initiative_ids) or not set(x.get("evidence_refs",[])).issubset(source_ids) or x.get("status")!="OPEN_CONTROLLED":
            e.append(f"exception[{i}]: threshold/severity/impact/urgency/evidence invalid");exception_bad+=1

    decision_bad=0;decision_ids=ids(decs,"decision_id")
    for i,x in enumerate(decs):
        if not present(x,"decision_id","question","initiative_ids","deadline","options","recommendation","rationale","value_time_cost_resource","risk","prerequisites","reversibility","decision_owner","evidence_refs","status") or not set(x.get("initiative_ids",[])).issubset(initiative_ids) or not set(x.get("evidence_refs",[])).issubset(source_ids) or x.get("status")!="PENDING":
            e.append(f"decision[{i}]: question/options/recommendation/trade-off/owner invalid");decision_bad+=1
        elif len(x.get("options",[]))<2: e.append(f"decision[{i}]: fewer than two options");decision_bad+=1

    coverage_bad=0
    mapping=[("source_ids",source_ids),("metric_ids",cm_ids),("initiative_ids",initiative_ids),("snapshot_ids",snapshot_ids),("dependency_ids",dep_ids),("resource_ids",pool_ids),("collision_ids",collision_ids),("risk_ids",risk_ids),("exception_ids",exception_ids),("decision_ids",decision_ids)]
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
        if x.get("review_type")!="FINAL_PORTFOLIO_DECISION" and x.get("status")!="PASS": e.append(f"review[{i}]: required review not PASS");review_bad+=1
        if x.get("review_type")=="FINAL_PORTFOLIO_DECISION" and x.get("status") not in {"PENDING","PASS"}: e.append(f"review[{i}]: final decision status invalid");review_bad+=1

    critical=contract_bad+source_bad+metric_bad+census_bad+snapshot_bad+network_bad+exposure_bad+exception_bad+decision_bad+coverage_bad+len(flags)+len(states)+test_bad+review_bad
    complete=snapshot.get("status")=="COMPLETE" and set(snapshot.get("initiative_ids",[]))==initiative_ids and set(snapshot.get("decision_ids",[]))==decision_ids
    if critical: state="NOT_READY"
    elif complete: state="READY_FOR_HUMAN_PORTFOLIO_DECISION"
    elif exs or decs: state="READY_FOR_PORTFOLIO_REVIEW"
    else: state="PORTFOLIO_BASELINED"
    if state=="READY_FOR_HUMAN_PORTFOLIO_DECISION": w.append("human portfolio decision remains; engine does not alert, reprioritize, reallocate, resequence, approve, pause or stop")
    return {"portfolio_id":c.get("portfolio_id"),"state":state,"metrics":{"sources":len(src),"canonical_metrics":len(cms),"initiatives":len(ins),"snapshots":len(snaps),"dependencies":len(deps),"resource_pools":len(pools),"collisions":len(cols),"risks":len(risks),"exceptions":len(exs),"decisions":len(decs),"contract_violations":contract_bad,"source_violations":source_bad,"metric_violations":metric_bad,"census_violations":census_bad,"snapshot_violations":snapshot_bad,"network_violations":network_bad,"exposure_violations":exposure_bad,"exception_violations":exception_bad,"decision_violations":decision_bad,"coverage_violations":coverage_bad,"forbidden_flags":len(flags),"unauthorized_states":len(states),"test_types":len(tt),"critical_defects":critical},"errors":e,"warnings":w}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument("input",type=Path);p.add_argument("--output",type=Path);a=p.parse_args();r=evaluate(load_json(a.input));s=json.dumps(r,ensure_ascii=False,indent=2);print(s)
    if a.output:a.output.write_text(s+"\n",encoding="utf-8")
    return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__": raise SystemExit(main())
