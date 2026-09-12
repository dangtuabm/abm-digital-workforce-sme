#!/usr/bin/env python3
import json,sys
from pathlib import Path
TESTS={"mandate_sources","intake_need_traceability","opportunity_concept_spec","experiments_validation","prioritization_sensitivity","roadmap_capacity_dependencies","decision_boundary"}
REVIEWS={"STRATEGY_CUSTOMER","PRODUCT_DISCOVERY","DESIGN_RESEARCH","ENGINEERING_OPERATIONS","FINANCE_COMMERCIAL","LEGAL_DATA_SECURITY"}
RISK_TYPES={"STRATEGY_PORTFOLIO","CUSTOMER_NEED_OUTCOME","DISCOVERY_EXPERIMENT","DELIVERY_CAPACITY_DEPENDENCY","FINANCE_COMMERCIAL","LEGAL_DATA_SECURITY_LIFECYCLE"}
SECTIONS={"document_control","source_intake_ledger","need_opportunity_map","concept_specs_experiments","prioritization_sensitivity","roadmap_capacity_lifecycle","risks_decisions_reviews","audit_change_log"}
RIGHTS={"AUTHORIZED","INTERNAL_AUTHORIZED","CUSTOMER_AUTHORIZED","RESEARCH_CONSENTED","LICENSED","PUBLIC_TERMS_OK"}
ACTIONS={"VALIDATE","INVEST_REVIEW","MAINTAIN","PACKAGE_REVIEW","DEFER","STOP_REVIEW","DEPRECATE_REVIEW"}
FORBIDDEN_FLAGS={"feedback_fabricated","customer_need_fabricated","pain_fabricated","interview_fabricated","demand_fabricated","market_size_fabricated","competitor_fabricated","revenue_fabricated","cost_fabricated","effort_fabricated","capacity_fabricated","dependency_fabricated","confidence_fabricated","source_fabricated","feedback_volume_called_priority","executive_request_auto_priority","sales_request_auto_priority","loudest_voice_priority","duplicate_demand_counted","segment_mixed","cohort_mixed","time_window_mixed","score_weight_hidden","missing_value_zeroed","score_gamed","sensitivity_hidden","strategic_fit_fabricated","cannibalization_hidden","legal_risk_hidden","data_risk_hidden","security_risk_hidden","accessibility_ignored","customer_harm_hidden","dark_pattern","vulnerable_user_exploited","experiment_result_fabricated","test_assignment_hidden","invalid_sample_accepted","inconclusive_called_validated","vanity_metric_used","success_criteria_changed","kill_criteria_bypassed","discovery_bypassed","concept_bypassed","review_bypassed","roadmap_committed_date_fabricated","release_date_promised","scope_creep_hidden","wip_ignored","capacity_overloaded","dependency_ignored","unauthorized_spec_change","auto_ticket_created","auto_backlog_changed","auto_priority_changed","auto_roadmap_committed","auto_funding_approved","auto_build_started","auto_release_scheduled","auto_product_released","auto_product_deprecated","auto_customer_contacted"}
FORBIDDEN_STATES={"TICKET_CREATED","BACKLOG_CHANGED","PRIORITY_CHANGED","ROADMAP_COMMITTED","FUNDING_APPROVED","BUILD_STARTED","RELEASE_SCHEDULED","PRODUCT_RELEASED","PRODUCT_DEPRECATED","CUSTOMER_CONTACTED"}
def ok(v):return v not in(None,"",[],{})
def fields(ds,p,obj,req):
 for f in req:
  if not ok(obj.get(f)):ds.add(f"{p}:missing_{f}")
def refs(ds,p,vals,known):
 for x in vals:
  if x not in known:ds.add(f"{p}:unknown_ref:{x}")
def evaluate(d):
 ds=set();gaps=set();m=d.get("mandate",{})
 fields(ds,"mandate",m,("strategy_outcome","product_portfolio_scope","customer_market_scope","as_of_horizon","budget_capacity_risk","owner","investment_authority","roadmap_authority","release_authority","required_reviews"))
 sources=d.get("sources",[]);sids=set()
 for i,x in enumerate(sources):
  xid=x.get("id",f"index-{i}");sids.add(xid)
  fields(ds,f"source:{xid}",x,("source_type","locator","version","date","rights_purpose","freshness","confidence","supports"))
  if x.get("rights_purpose") not in RIGHTS:ds.add(f"source:{xid}:not_authorized")
 if len(sids)!=len(sources):ds.add("sources:duplicate_id")
 intake=d.get("intake",[]);iids=set()
 for i,x in enumerate(intake):
  xid=x.get("id",f"index-{i}");iids.add(xid)
  fields(ds,f"intake:{xid}",x,("intake_type","source_id","entity_segment_context_date","verbatim","interpretation","duplicate_cluster","rights","confidence_gaps"))
  refs(ds,f"intake:{xid}",[x.get("source_id")],sids)
 if len(iids)!=len(intake):ds.add("intake:duplicate_id")
 needs=d.get("needs",[]);nids=set()
 for i,x in enumerate(needs):
  xid=x.get("id",f"index-{i}");nids.add(xid)
  fields(ds,f"need:{xid}",x,("job_problem_alternative_outcome","intake_ids","evidence_source_ids","pattern_frequency_reach","denominator_sample_bias","severity_value","confidence_gaps"))
  refs(ds,f"need:{xid}:intake",x.get("intake_ids",[]),iids);refs(ds,f"need:{xid}:source",x.get("evidence_source_ids",[]),sids)
 if len(nids)!=len(needs):ds.add("needs:duplicate_id")
 opps=d.get("opportunities",[]);oids=set()
 for i,x in enumerate(opps):
  xid=x.get("id",f"index-{i}");oids.add(xid)
  fields(ds,f"opportunity:{xid}",x,("outcome_link","need_ids","opportunity_statement","assumptions","solution_alternatives","evidence_source_ids","confidence_gaps"))
  refs(ds,f"opportunity:{xid}:need",x.get("need_ids",[]),nids);refs(ds,f"opportunity:{xid}:source",x.get("evidence_source_ids",[]),sids)
 concepts=d.get("concepts",[]);cids=set()
 for i,x in enumerate(concepts):
  xid=x.get("id",f"index-{i}");cids.add(xid)
  fields(ds,f"concept:{xid}",x,("opportunity_ids","need_ids","target_user_job","value_hypothesis","in_scope","out_scope","acceptance","nonfunctional","accessibility_data_security_privacy","dependencies_lifecycle"))
  refs(ds,f"concept:{xid}:opportunity",x.get("opportunity_ids",[]),oids);refs(ds,f"concept:{xid}:need",x.get("need_ids",[]),nids)
 if len(cids)!=len(concepts):ds.add("concepts:duplicate_id")
 experiments=d.get("experiments",[]);eids=set()
 for i,x in enumerate(experiments):
  xid=x.get("id",f"index-{i}");eids.add(xid)
  fields(ds,f"experiment:{xid}",x,("concept_ids","assumption_method_unit","baseline_sample_window","success_criteria","kill_criteria","harm_guardrails","evidence_owner","interpretation_next_decision","human_state"))
  refs(ds,f"experiment:{xid}",x.get("concept_ids",[]),cids)
  if x.get("human_state")!="PENDING":ds.add(f"experiment:{xid}:human_state_not_pending")
 model=d.get("prioritization_model",{})
 fields(ds,"prioritization_model",model,("criteria_weights","scale_direction","missing_rule","confidence_rule","normalization","sensitivity_method","red_flag_rule"))
 priorities=d.get("priorities",[]);prioritized=set()
 for i,x in enumerate(priorities):
  xid=x.get("concept_id",f"index-{i}");prioritized.add(xid)
  if xid not in cids:ds.add(f"priority:{xid}:unknown_concept")
  fields(ds,f"priority:{xid}",x,("evidence_source_ids","score_range","sensitivity_rank_stability","effort_range","capacity_dependencies","strategic_value_risk","red_flags","recommendation"))
  refs(ds,f"priority:{xid}",x.get("evidence_source_ids",[]),sids)
  if x.get("recommendation") not in ACTIONS:ds.add(f"priority:{xid}:invalid_recommendation")
 for xid in cids-prioritized:ds.add(f"priority:missing_concept:{xid}")
 options=d.get("roadmap_options",[]);rids=set()
 for i,x in enumerate(options):
  xid=x.get("id",f"index-{i}");rids.add(xid)
  fields(ds,f"roadmap:{xid}",x,("concept_ids","outcome_horizon","action","capacity_wip","dependencies_tradeoffs","trigger_uncertainty","portfolio_cannibalization","lifecycle_migration_continuity","reversibility"))
  refs(ds,f"roadmap:{xid}",x.get("concept_ids",[]),cids)
  if x.get("action") not in ACTIONS:ds.add(f"roadmap:{xid}:invalid_action")
 risks=d.get("risks",[]);seenr=set()
 for i,x in enumerate(risks):
  typ=x.get("risk_type",f"index-{i}");seenr.add(typ)
  fields(ds,f"risk:{typ}",x,("statement","likelihood","impact","trigger","mitigation","contingency","owner"))
 for typ in RISK_TYPES-seenr:ds.add(f"risks:missing_type:{typ}")
 decisions=d.get("decision_queue",[]);decided=set()
 for i,x in enumerate(decisions):
  xid=x.get("concept_id",f"index-{i}");decided.add(xid)
  if xid not in cids:ds.add(f"decision:{xid}:unknown_concept")
  fields(ds,f"decision:{xid}",x,("recommendation","alternatives","evidence_source_ids","experiment_ids","roadmap_option_ids","score_sensitivity","funding_capacity_request","decision_owner_needed_by","human_state"))
  if x.get("recommendation") not in ACTIONS:ds.add(f"decision:{xid}:invalid_recommendation")
  refs(ds,f"decision:{xid}:source",x.get("evidence_source_ids",[]),sids);refs(ds,f"decision:{xid}:experiment",x.get("experiment_ids",[]),eids);refs(ds,f"decision:{xid}:roadmap",x.get("roadmap_option_ids",[]),rids)
  if x.get("human_state")!="PENDING":ds.add(f"decision:{xid}:human_state_not_pending")
 for xid in cids-decided:ds.add(f"decision:missing_concept:{xid}")
 missing=SECTIONS-set(d.get("output_sections",[]))
 if missing:ds.add("output_sections:missing:"+",".join(sorted(missing)))
 tests=d.get("tests",{})
 for x in TESTS:
  if tests.get(x)!="PASS":ds.add(f"test:{x}:not_pass")
 rev=d.get("reviews",{})
 for x in REVIEWS:
  if rev.get(x)!="PASS":gaps.add(f"review:{x}:not_pass")
 if rev.get("FINAL_HUMAN_ROADMAP_DECISION")!="PENDING":ds.add("review:FINAL_HUMAN_ROADMAP_DECISION:must_be_pending")
 for x in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS):ds.add(f"forbidden_flag:{x}")
 states=set(d.get("forbidden_states",[]));states.add(d.get("delivery_state","DRAFT"))
 for x in sorted(states&FORBIDDEN_STATES):ds.add(f"forbidden_state:{x}")
 ready=not ds and not gaps
 return {"skill":"product-roadmap","state":"READY_FOR_HUMAN_ROADMAP_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"intake":len(intake),"needs":len(needs),"opportunities":len(opps),"concepts":len(concepts),"experiments":len(experiments),"priorities":len(priorities),"roadmap_options":len(options),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(rev.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 customer need, product-market fit, effort/capacity accuracy, experiment outcome, roadmap adoption, token cost or duration."}
def main():
 if len(sys.argv)!=2:print("usage: evaluate_product_roadmap.py INPUT.json",file=sys.stderr);return 2
 r=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")));print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__":raise SystemExit(main())
