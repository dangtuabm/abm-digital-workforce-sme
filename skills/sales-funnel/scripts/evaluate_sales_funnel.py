#!/usr/bin/env python3
import json,sys
from pathlib import Path
TESTS={"mandate_journey","stage_contract","event_identity","metric_cohort","reconciliation_economics","diagnosis_experiment","decision_boundary"}
REVIEWS={"CUSTOMER_JOURNEY","DATA_ANALYTICS","PRIVACY_LEGAL","MARKETING_SALES","FINANCE_REVENUE_OPS"}
RISK_TYPES={"PRIVACY_CONSENT","MEASUREMENT_ATTRIBUTION","COMMERCIAL_CUSTOMER_HARM","OPERATIONS_CAPACITY"}
SECTIONS={"mandate_journey","stage_transitions","event_identity_consent","metric_baseline","reconciliation_leakage","economics_attribution","experiments_guardrails","reviews_audit_activation"}
FORBIDDEN_FLAGS={"traffic_fabricated","lead_fabricated","account_fabricated","conversion_fabricated","cost_fabricated","revenue_fabricated","attribution_fabricated","benchmark_fabricated","sample_fabricated","experiment_result_fabricated","unit_mixed","cohort_mixed","window_mixed","denominator_changed","loss_deleted","duplicate_deleted_to_improve","activity_called_intent","last_touch_called_causal","spam","illegal_tracking","consent_bypassed","retention_bypassed","unsubscribe_bypassed","dark_pattern","fake_urgency","fake_social_proof","protected_trait_targeting","sensitive_trait_inference","discriminatory_targeting","metric_gaming","criteria_changed","guardrail_hidden","auto_published","auto_sent","auto_enrolled","auto_routed","auto_scored","auto_advanced","auto_closed_won","auto_activated"}
FORBIDDEN_STATES={"PUBLISHED","SENT","ENROLLED","ROUTED","SCORED","ADVANCED","CLOSED_WON","ACTIVATED"}
def ok(v): return v not in (None,"",[],{})
def evaluate(d):
 ds=set(); gaps=set(); m=d.get("mandate",{})
 for f in ("objective","decision","product","segment","geography","journey_start","journey_end","as_of","horizon","funnel_owner","activation_authority","constraints","prohibited_actions","required_reviews"):
  if not ok(m.get(f)): ds.add(f"mandate:missing_{f}")
 sources=d.get("sources",[]); sids=set()
 for i,s in enumerate(sources):
  sid=s.get("id",f"index-{i}"); sids.add(sid)
  for f in ("system","locator","version","as_of","freshness","rights","unit","confidence"):
   if not ok(s.get(f)): ds.add(f"source:{sid}:missing_{f}")
  if s.get("rights") not in ("AUTHORIZED","INTERNAL_AUTHORIZED","PUBLIC_TERMS_OK"): ds.add(f"source:{sid}:not_authorized")
 journey=d.get("journey",[])
 for i,j in enumerate(journey):
  jid=j.get("id",f"index-{i}")
  for f in ("customer_job_question","touchpoint","channel","offer_or_content","expected_action","friction","handoff","accessibility","evidence_ids"):
   if not ok(j.get(f)): ds.add(f"journey:{jid}:missing_{f}")
  for ref in j.get("evidence_ids",[]):
   if ref not in sids: ds.add(f"journey:{jid}:unknown_source:{ref}")
 stages=d.get("stages",[]); stageids=set()
 for i,s in enumerate(stages):
  sid=s.get("id",f"index-{i}"); stageids.add(sid)
  for f in ("name","unit","entry_rule","exit_rule","valid_transitions","owner","sla","required_evidence","loss_rule","recycle_rule","system_of_record"):
   if not ok(s.get(f)): ds.add(f"stage:{sid}:missing_{f}")
 events=d.get("events",[]); eventids=set()
 for i,e in enumerate(events):
  eid=e.get("id",f"index-{i}"); eventids.add(eid)
  for f in ("event_name","entity_unit","timestamp_rule","source_id","schema_version","required_properties","identity_rule","consent_rule","retention_rule","dedup_rule","late_correction_deletion_rule"):
   if not ok(e.get(f)): ds.add(f"event:{eid}:missing_{f}")
  if e.get("source_id") not in sids: ds.add(f"event:{eid}:unknown_source")
 metrics=d.get("metrics",[])
 for i,x in enumerate(metrics):
  mid=x.get("id",f"index-{i}")
  for f in ("name","formula","unit","grain","numerator","denominator","cohort","window","source_ids","owner","target_threshold","confidence"):
   if not ok(x.get(f)) and x.get(f)!=0: ds.add(f"metric:{mid}:missing_{f}")
  for ref in x.get("source_ids",[]):
   if ref not in sids: ds.add(f"metric:{mid}:unknown_source:{ref}")
 cohorts=d.get("cohorts",[])
 for i,c in enumerate(cohorts):
  cid=c.get("id",f"index-{i}")
  for f in ("definition","unit","start","end","timezone","source_ids","missingness","bias"):
   if not ok(c.get(f)): ds.add(f"cohort:{cid}:missing_{f}")
  for ref in c.get("source_ids",[]):
   if ref not in sids: ds.add(f"cohort:{cid}:unknown_source:{ref}")
 baselines=d.get("baselines",[])
 for i,b in enumerate(baselines):
  bid=b.get("id",f"index-{i}")
  if b.get("stage_id") not in stageids: ds.add(f"baseline:{bid}:unknown_stage")
  for f in ("cohort_id","eligible_entries","valid_exits","in_stage","loss_recycle","conversion","velocity","window","source_ids","confidence"):
   if not ok(b.get(f)) and b.get(f)!=0: ds.add(f"baseline:{bid}:missing_{f}")
  vals=[b.get(x) for x in ("eligible_entries","valid_exits","in_stage","loss_recycle")]
  if all(isinstance(z,(int,float)) for z in vals) and abs(vals[0]-sum(vals[1:]))>0.0001: ds.add(f"baseline:{bid}:not_reconciled")
  for ref in b.get("source_ids",[]):
   if ref not in sids: ds.add(f"baseline:{bid}:unknown_source:{ref}")
 economics=d.get("economics",[])
 for i,e in enumerate(economics):
  eid=e.get("id",f"index-{i}")
  for f in ("channel_segment","spend_cost","capacity","value_revenue_definition","cac_or_cost_per_progression","payback_or_contribution","attribution_method","attribution_limits","currency","base_year","horizon","source_ids","sensitivity"):
   if not ok(e.get(f)) and e.get(f)!=0: ds.add(f"economics:{eid}:missing_{f}")
  for ref in e.get("source_ids",[]):
   if ref not in sids: ds.add(f"economics:{eid}:unknown_source:{ref}")
 leaks=d.get("leakages",[])
 for i,l in enumerate(leaks):
  lid=l.get("id",f"index-{i}")
  for f in ("stage_transition","eligible_volume","rate_gap","value_per_progression","impact_formula","impact_range","root_cause_hypotheses","evidence_for","evidence_against","owner","confidence"):
   if not ok(l.get(f)) and l.get(f)!=0: ds.add(f"leakage:{lid}:missing_{f}")
 exps=d.get("experiments",[])
 for i,x in enumerate(exps):
  xid=x.get("id",f"index-{i}")
  for f in ("hypothesis","audience","assignment","control","change","sample_rationale","primary_metric","baseline","success","kill","guardrails","duration","max_budget","consent_fairness","owner","status"):
   if not ok(x.get(f)) and x.get(f)!=0: ds.add(f"experiment:{xid}:missing_{f}")
  if x.get("status") not in ("PROPOSED","PENDING_HUMAN_APPROVAL"): ds.add(f"experiment:{xid}:unauthorized_status")
 risks=d.get("risks",[]); seen=set()
 for i,r in enumerate(risks):
  typ=r.get("risk_type",f"index-{i}"); seen.add(typ)
  for f in ("statement","trigger","mitigation","contingency","owner","status"):
   if not ok(r.get(f)): ds.add(f"risk:{typ}:missing_{f}")
 for typ in RISK_TYPES-seen: ds.add(f"risks:missing_type:{typ}")
 miss=SECTIONS-set(d.get("output_sections",[]))
 if miss: ds.add("output_sections:missing:"+",".join(sorted(miss)))
 tests=d.get("tests",{})
 for t in TESTS:
  if tests.get(t)!="PASS": ds.add(f"test:{t}:not_pass")
 reviews=d.get("reviews",{})
 for r in REVIEWS:
  if reviews.get(r)!="PASS": gaps.add(f"review:{r}:not_pass")
 if reviews.get("FINAL_HUMAN_FUNNEL_ACTIVATION")!="PENDING": ds.add("review:FINAL_HUMAN_FUNNEL_ACTIVATION:must_be_pending")
 for f in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS): ds.add(f"forbidden_flag:{f}")
 states=set(d.get("forbidden_states",[])); states.add(d.get("published_state","DRAFT"))
 for s in sorted(states&FORBIDDEN_STATES): ds.add(f"forbidden_state:{s}")
 ready=not ds and not gaps
 return {"skill":"sales-funnel","state":"READY_FOR_HUMAN_FUNNEL_ACTIVATION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"journey_steps":len(journey),"stages":len(stages),"events":len(events),"metrics":len(metrics),"cohorts":len(cohorts),"baselines":len(baselines),"economics":len(economics),"leakages":len(leaks),"experiments":len(exps),"risks":len(risks),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(reviews.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 funnel truth, causal lift, customer impact, economics, legal compliance, token cost, duration or adoption."}
def main():
 if len(sys.argv)!=2: print("usage: evaluate_sales_funnel.py INPUT.json",file=sys.stderr); return 2
 r=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")));print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__": raise SystemExit(main())
