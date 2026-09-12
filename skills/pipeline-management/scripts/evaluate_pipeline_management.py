#!/usr/bin/env python3
import json,sys
from pathlib import Path

TESTS={"mandate_sources","stage_contract_integrity","opportunity_evidence","scoring_fairness","aging_next_action","pipeline_forecast_reconciliation","decision_boundary"}
REVIEWS={"SALES_OPERATIONS","ACCOUNT_OWNER","FINANCE_FORECAST","DELIVERY_CAPACITY","DATA_PRIVACY_FAIRNESS","COMMERCIAL_LEGAL"}
RISK_TYPES={"DATA_QUALITY_LINEAGE","STAGE_PROCESS_INTEGRITY","FORECAST_UNCERTAINTY","CAPACITY_COVERAGE","CUSTOMER_HARM_FAIRNESS","COMMERCIAL_LEGAL_PRIVACY"}
SECTIONS={"document_control","source_stage_contract","opportunity_register","scoring_rationale","aging_next_action","reconciliation_forecast","exceptions_risks","decisions_reviews_audit"}
RECOMMENDATIONS={"KEEP","VERIFY","CORRECT","NURTURE","HOLD","CLOSE_REVIEW"}
FORBIDDEN_FLAGS={"lead_fabricated","opportunity_fabricated","activity_fabricated","amount_fabricated","stage_evidence_fabricated","stakeholder_fabricated","budget_fabricated","decision_authority_fabricated","timing_fabricated","next_action_fabricated","close_date_fabricated","probability_fabricated","forecast_fabricated","loss_reason_fabricated","crm_source_bypassed","duplicate_ignored","stale_data_used","denominator_hidden","currency_mixed","snapshot_mixed","model_unversioned","weight_unapproved","missing_data_scored_zero","sensitive_attribute_used","proxy_discrimination","vulnerability_exploited","consent_bypassed","retention_bypassed","pipeline_inflated","opportunity_split_gamed","activity_gaming","vanity_scoring","override_hidden","manual_override_unlogged","review_bypassed","pressure_tactic","auto_disqualified","auto_deleted","auto_stage_changed","auto_owner_reassigned","auto_task_assigned","auto_followup_sent","auto_forecast_committed","auto_closed"}
FORBIDDEN_STATES={"CRM_UPDATED","STAGE_CHANGED","OPPORTUNITY_DISQUALIFIED","RECORD_DELETED","OWNER_REASSIGNED","TASK_ASSIGNED","FOLLOWUP_SENT","FORECAST_COMMITTED","DEAL_CLOSED"}
RIGHTS={"AUTHORIZED","INTERNAL_AUTHORIZED","CUSTOMER_AUTHORIZED","PUBLIC_TERMS_OK"}

def ok(v): return v not in (None,"",[],{})
def evaluate(d):
 ds=set(); gaps=set(); m=d.get("mandate",{})
 for f in ("portfolio_scope","as_of","horizon","opportunity_unit","sales_process_version","score_model_version","crm_source_of_truth","currency_basis","owner","stage_authority","forecast_authority","decision_authority","confidentiality_retention","required_reviews"):
  if not ok(m.get(f)): ds.add(f"mandate:missing_{f}")

 sources=d.get("sources",[]); sids=set()
 for i,s in enumerate(sources):
  sid=s.get("id",f"index-{i}"); sids.add(sid)
  for f in ("source_type","locator","version","snapshot_at","rights_purpose","coverage","freshness","confidence","subject"):
   if not ok(s.get(f)): ds.add(f"source:{sid}:missing_{f}")
  if s.get("rights_purpose") not in RIGHTS: ds.add(f"source:{sid}:not_authorized")

 stages=d.get("stage_contracts",[]); stageids=set(); orders=[]; stage_map={}
 for i,s in enumerate(stages):
  sid=s.get("stage",f"index-{i}"); stageids.add(sid); stage_map[sid]=s
  for f in ("order","entry_criteria","required_evidence","exit_criteria","owner_role","change_authority","age_limit_source","next_action_sla","allowed_forecast_categories","policy_source_ids"):
   if not ok(s.get(f)): ds.add(f"stage:{sid}:missing_{f}")
  orders.append(s.get("order"))
  for ref in s.get("policy_source_ids",[]):
   if ref not in sids: ds.add(f"stage:{sid}:unknown_source:{ref}")
 if len(stageids)!=len(stages): ds.add("stages:duplicate_stage")
 if len(set(orders))!=len(orders): ds.add("stages:duplicate_order")

 model=d.get("scoring_model",{})
 for f in ("model_id","version","purpose","approved_by","eligible_unit","scale","calibration_reference","limitations","fairness_exclusions","missing_rule","override_rule"):
  if not ok(model.get(f)): ds.add(f"model:missing_{f}")
 dims=model.get("dimensions",[]); dimids=set(); weight=0.0
 for i,x in enumerate(dims):
  did=x.get("id",f"index-{i}"); dimids.add(did)
  for f in ("name","weight","evidence_requirement","missing_rule"):
   if not ok(x.get(f)): ds.add(f"dimension:{did}:missing_{f}")
  try: weight+=float(x.get("weight",0))
  except (TypeError,ValueError): ds.add(f"dimension:{did}:invalid_weight")
 if abs(weight-1.0)>0.0001: ds.add(f"model:weights_not_one:{weight}")
 if len(dimids)!=len(dims): ds.add("model:duplicate_dimension")

 opps=d.get("opportunities",[]); oppids=set(); amounts=0.0; opp_map={}
 for i,o in enumerate(opps):
  oid=o.get("id",f"index-{i}"); oppids.add(oid); opp_map[oid]=o
  for f in ("account_entity","owner","amount","currency","stage","stage_entered_at","source_ids","stage_evidence_ids","fit_status","need_status","decision_process_status","budget_status","timing_status","stakeholder_roles","last_meaningful_activity_at","age_in_stage_days","stage_age_limit_days","close_date_candidate","close_date_basis","forecast_category","forecast_rationale","data_quality_status","scorecard","next_action","exception_ids"):
   if f not in o or not ok(o.get(f)): ds.add(f"opportunity:{oid}:missing_{f}")
  try:
   amount=float(o.get("amount",0)); amounts+=amount
   if amount<=0: ds.add(f"opportunity:{oid}:nonpositive_amount")
  except (TypeError,ValueError): ds.add(f"opportunity:{oid}:invalid_amount")
  stage=o.get("stage")
  if stage not in stageids: ds.add(f"opportunity:{oid}:invalid_stage:{stage}")
  else:
   if o.get("forecast_category") not in stage_map[stage].get("allowed_forecast_categories",[]): ds.add(f"opportunity:{oid}:forecast_not_allowed_for_stage")
  for ref in o.get("source_ids",[])+o.get("stage_evidence_ids",[]):
   if ref not in sids: ds.add(f"opportunity:{oid}:unknown_source:{ref}")
  scs=o.get("scorecard",[]); seen=set()
  for j,sc in enumerate(scs):
   did=sc.get("dimension_id",f"index-{j}"); seen.add(did)
   if did not in dimids: ds.add(f"score:{oid}:unknown_dimension:{did}")
   for f in ("value","evidence_ids","confidence","missing_rule_applied"):
    if f not in sc or not ok(sc.get(f)): ds.add(f"score:{oid}:{did}:missing_{f}")
   for ref in sc.get("evidence_ids",[]):
    if ref not in sids: ds.add(f"score:{oid}:{did}:unknown_source:{ref}")
  for did in dimids-seen: ds.add(f"score:{oid}:missing_dimension:{did}")
  na=o.get("next_action",{})
  for f in ("outcome","owner","due","dependency","expected_evidence","status"):
   if not ok(na.get(f)): ds.add(f"next_action:{oid}:missing_{f}")
 if len(oppids)!=len(opps): ds.add("opportunities:duplicate_id")

 exceptions=d.get("exceptions",[]); exids=set(); ex_by_opp={oid:set() for oid in oppids}
 for i,x in enumerate(exceptions):
  xid=x.get("id",f"index-{i}"); exids.add(xid)
  for f in ("type","affected_ids","evidence_source_ids","severity","owner","due","verification_action","escalation","state"):
   if not ok(x.get(f)): ds.add(f"exception:{xid}:missing_{f}")
  for oid in x.get("affected_ids",[]):
   if oid not in oppids: ds.add(f"exception:{xid}:unknown_opportunity:{oid}")
   else: ex_by_opp[oid].add(xid)
  for ref in x.get("evidence_source_ids",[]):
   if ref not in sids: ds.add(f"exception:{xid}:unknown_source:{ref}")
 for oid,o in opp_map.items():
  declared=set(o.get("exception_ids",[]))
  if declared-exids: ds.add(f"opportunity:{oid}:unknown_exception")
  try:
   if float(o.get("age_in_stage_days",0))>float(o.get("stage_age_limit_days",0)) and not declared: ds.add(f"opportunity:{oid}:age_breach_without_exception")
  except (TypeError,ValueError): ds.add(f"opportunity:{oid}:invalid_age")

 rec=d.get("reconciliation",{})
 for f in ("snapshot_source_id","opportunity_unit","currency_basis","total_records","active_opportunity_ids","included_ids","excluded_ids","duplicate_rule","stale_rule","amount_total","amount_by_stage","record_count_by_stage","variance","unresolved_items","reconciliation_status","coverage_capacity"):
  if f not in rec or not ok(rec.get(f)): ds.add(f"reconciliation:missing_{f}")
 if rec.get("snapshot_source_id") not in sids: ds.add("reconciliation:unknown_snapshot_source")
 if rec.get("total_records")!=len(opps): ds.add("reconciliation:record_count_mismatch")
 if set(rec.get("active_opportunity_ids",[]))!=oppids: ds.add("reconciliation:active_ids_mismatch")
 if set(rec.get("included_ids",[]))!=oppids: ds.add("reconciliation:included_ids_mismatch")
 try:
  if abs(float(rec.get("amount_total",0))-amounts)>0.01: ds.add("reconciliation:amount_total_mismatch")
 except (TypeError,ValueError): ds.add("reconciliation:invalid_amount_total")
 if rec.get("reconciliation_status")!="PASS_WITH_DISCLOSED_EXCEPTIONS": ds.add("reconciliation:not_pass")

 scenarios=d.get("forecast_scenarios",[])
 for i,x in enumerate(scenarios):
  name=x.get("name",f"index-{i}")
  for f in ("opportunity_ids","amount","currency","category_policy","probability_or_range_basis","timing","assumptions","capacity_dependencies","risks_limitations"):
   if not ok(x.get(f)): ds.add(f"scenario:{name}:missing_{f}")
  for oid in x.get("opportunity_ids",[]):
   if oid not in oppids: ds.add(f"scenario:{name}:unknown_opportunity:{oid}")

 risks=d.get("risks",[]); seen_risks=set()
 for i,r in enumerate(risks):
  typ=r.get("risk_type",f"index-{i}"); seen_risks.add(typ)
  for f in ("statement","likelihood","impact","trigger","mitigation","contingency","owner"):
   if not ok(r.get(f)): ds.add(f"risk:{typ}:missing_{f}")
 for typ in RISK_TYPES-seen_risks: ds.add(f"risks:missing_type:{typ}")

 decisions=d.get("decision_queue",[]); decided=set()
 for i,x in enumerate(decisions):
  oid=x.get("opportunity_id",f"index-{i}"); decided.add(oid)
  if oid not in oppids: ds.add(f"decision:unknown_opportunity:{oid}")
  for f in ("recommendation","rationale","evidence_source_ids","decision_owner","needed_by","human_state"):
   if not ok(x.get(f)): ds.add(f"decision:{oid}:missing_{f}")
  if x.get("recommendation") not in RECOMMENDATIONS: ds.add(f"decision:{oid}:invalid_recommendation")
  if x.get("human_state")!="PENDING": ds.add(f"decision:{oid}:human_state_not_pending")
  for ref in x.get("evidence_source_ids",[]):
   if ref not in sids: ds.add(f"decision:{oid}:unknown_source:{ref}")
 for oid in oppids-decided: ds.add(f"decision:missing_opportunity:{oid}")

 missing=SECTIONS-set(d.get("output_sections",[]))
 if missing: ds.add("output_sections:missing:"+",".join(sorted(missing)))
 tests=d.get("tests",{})
 for t in TESTS:
  if tests.get(t)!="PASS": ds.add(f"test:{t}:not_pass")
 reviews=d.get("reviews",{})
 for r in REVIEWS:
  if reviews.get(r)!="PASS": gaps.add(f"review:{r}:not_pass")
 if reviews.get("FINAL_HUMAN_PIPELINE_DECISION")!="PENDING": ds.add("review:FINAL_HUMAN_PIPELINE_DECISION:must_be_pending")
 for f in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS): ds.add(f"forbidden_flag:{f}")
 states=set(d.get("forbidden_states",[])); states.add(d.get("published_state","DRAFT"))
 for s in sorted(states&FORBIDDEN_STATES): ds.add(f"forbidden_state:{s}")
 ready=not ds and not gaps
 return {"skill":"pipeline-management","state":"READY_FOR_HUMAN_PIPELINE_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"stage_contracts":len(stages),"opportunities":len(opps),"score_dimensions":len(dims),"forecast_scenarios":len(scenarios),"exceptions":len(exceptions),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(reviews.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 CRM truth, stage precision, score fairness/calibration, forecast accuracy, customer outcome, token cost, duration or adoption."}

def main():
 if len(sys.argv)!=2: print("usage: evaluate_pipeline_management.py INPUT.json",file=sys.stderr); return 2
 r=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))); print(json.dumps(r,ensure_ascii=False,indent=2)); return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__": raise SystemExit(main())
