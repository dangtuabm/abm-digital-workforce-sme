#!/usr/bin/env python3
import json,sys
from pathlib import Path
TESTS={"mandate_sources","campaign_taxonomy_funnel","measurement_reconciliation","audience_creative_compliance","experiment_causal","budget_pacing_risk","decision_boundary"}
REVIEWS={"STRATEGY_CUSTOMER","MEDIA_OPERATIONS","CREATIVE_BRAND_LANDING","DATA_MEASUREMENT","FINANCE_REVENUE","LEGAL_PRIVACY_POLICY"}
RISK_TYPES={"STRATEGY_OFFER_CUSTOMER","MEASUREMENT_ATTRIBUTION","AUDIENCE_PRIVACY_POLICY","CREATIVE_LANDING_BRAND","BUDGET_ECONOMICS_CAPACITY","FRAUD_PLATFORM_OPERATION"}
SECTIONS={"document_control","source_snapshot_ledger","campaign_funnel_contracts","audience_creative_landing","baseline_reconciliation_diagnosis","experiments_budget_scenarios","risks_decisions_reviews","audit_rollback"}
RIGHTS={"AUTHORIZED","INTERNAL_AUTHORIZED","PLATFORM_AUTHORIZED","CUSTOMER_AUTHORIZED","LICENSED","PUBLIC_TERMS_OK"}
RECOMMENDATIONS={"HOLD","VALIDATE","TEST_REVIEW","REALLOCATE_REVIEW","SCALE_REVIEW","REDUCE_REVIEW","STOP_REVIEW"}
FORBIDDEN_FLAGS={"performance_fabricated","conversion_fabricated","revenue_fabricated","cost_fabricated","benchmark_fabricated","audience_fabricated","attribution_fabricated","tracking_event_fabricated","sample_fabricated","source_fabricated","customer_list_uploaded_unlawfully","sensitive_attribute_targeting","proxy_discrimination","vulnerable_targeting","minors_targeted","consent_bypassed","unlawful_tracking","cookie_bypassed","platform_policy_bypassed","regulated_claim_unapproved","claim_fabricated","case_fabricated","creative_rights_bypassed","brand_bypassed","landing_mismatch_hidden","dark_pattern","false_urgency","false_scarcity","fake_social_proof","competitor_trademark_misused","account_access_bypassed","credential_exposed","fraud_hidden","invalid_traffic_ignored","bot_traffic_counted","duplicate_conversion_counted","refund_chargeback_hidden","tax_fee_hidden","currency_mixed","denominator_hidden","cohort_mixed","window_mixed","attribution_called_causality","incrementality_claimed_without_test","significance_fabricated","experiment_assignment_hidden","peeking_stopped_early","budget_authority_bypassed","kill_switch_bypassed","metric_gaming","review_bypassed","auto_create","auto_edit","auto_publish","auto_launch","auto_pause","auto_stop","auto_budget_change","auto_bid_change","auto_targeting_change","auto_tracking_change","auto_audience_upload","auto_spend"}
FORBIDDEN_STATES={"CREATED","EDITED","PUBLISHED","LAUNCHED","PAUSED","STOPPED","BUDGET_CHANGED","BID_CHANGED","TARGETING_CHANGED","TRACKING_CHANGED","AUDIENCE_UPLOADED","SPEND_COMMITTED"}
def ok(v):return v not in(None,"",[],{})
def fields(ds,p,obj,req):
 for f in req:
  if not ok(obj.get(f)):ds.add(f"{p}:missing_{f}")
def refs(ds,p,vals,known):
 for x in vals:
  if x not in known:ds.add(f"{p}:unknown_ref:{x}")
def evaluate(d):
 ds=set();gaps=set();m=d.get("mandate",{})
 fields(ds,"mandate",m,("objective_outcome","product_offer","audience_geography_channel","as_of_window_timezone_currency","budget_risk_capacity","owner","account_authority","budget_authority","release_authority","required_reviews"))
 sources=d.get("sources",[]);sids=set()
 for i,x in enumerate(sources):
  xid=x.get("id",f"index-{i}");sids.add(xid)
  fields(ds,f"source:{xid}",x,("source_type","locator","version_hash","date","rights_access","freshness","confidence","supports"))
  if x.get("rights_access") not in RIGHTS:ds.add(f"source:{xid}:not_authorized")
 if len(sids)!=len(sources):ds.add("sources:duplicate_id")
 campaigns=d.get("campaigns",[]);cids=set()
 for i,x in enumerate(campaigns):
  xid=x.get("id",f"index-{i}");cids.add(xid)
  fields(ds,f"campaign:{xid}",x,("account_id","campaign_adset_ad_ids","creative_landing_ids","objective_status","audience_placement","budget_bid_schedule","change_history","source_ids"))
  refs(ds,f"campaign:{xid}",x.get("source_ids",[]),sids)
 if len(cids)!=len(campaigns):ds.add("campaigns:duplicate_id")
 contracts=d.get("measurement_contracts",[]);mids=set()
 for i,x in enumerate(contracts):
  xid=x.get("id",f"index-{i}");mids.add(xid)
  fields(ds,f"measurement:{xid}",x,("funnel_stage_event_meaning","formula_grain","numerator_denominator","cohort_window","identity_dedup_consent","source_freshness","attribution_limits","owner"))
 if len(mids)!=len(contracts):ds.add("measurement:duplicate_id")
 reviews=d.get("experience_reviews",[]);reviewed=set()
 for i,x in enumerate(reviews):
  xid=x.get("campaign_id",f"index-{i}");reviewed.add(xid)
  if xid not in cids:ds.add(f"experience:{xid}:unknown_campaign")
  fields(ds,f"experience:{xid}",x,("targeting_minimization","claim_rights_brand","accessibility_disclosure","creative_landing_offer_consistency","policy_source_ids","defects_state"))
  refs(ds,f"experience:{xid}",x.get("policy_source_ids",[]),sids)
 for xid in cids-reviewed:ds.add(f"experience:missing_campaign:{xid}")
 baselines=d.get("baseline_reconciliation",[]);based=set()
 for i,x in enumerate(baselines):
  xid=x.get("campaign_id",f"index-{i}");based.add(xid)
  if xid not in cids:ds.add(f"baseline:{xid}:unknown_campaign")
  fields(ds,f"baseline:{xid}",x,("metric_ids","delivery_attention_click","conversion_value_quality_harm","platform_total","analytics_total","crm_total","finance_total","currency_tax_fees_refunds","gap_explanation_confidence"))
  refs(ds,f"baseline:{xid}",x.get("metric_ids",[]),mids)
 for xid in cids-based:ds.add(f"baseline:missing_campaign:{xid}")
 diagnoses=d.get("diagnoses",[]);diagnosed=set()
 for i,x in enumerate(diagnoses):
  xid=x.get("campaign_id",f"index-{i}");diagnosed.add(xid)
  if xid not in cids:ds.add(f"diagnosis:{xid}:unknown_campaign")
  fields(ds,f"diagnosis:{xid}",x,("observed_signal","tracking_data_checks","fraud_anomaly_checks","fatigue_saturation_learning","landing_funnel_offer_capacity","external_factors","primary_alternative_causes","evidence_source_ids","confidence"))
  refs(ds,f"diagnosis:{xid}",x.get("evidence_source_ids",[]),sids)
 for xid in cids-diagnosed:ds.add(f"diagnosis:missing_campaign:{xid}")
 experiments=d.get("experiments",[]);eids=set()
 for i,x in enumerate(experiments):
  xid=x.get("id",f"index-{i}");eids.add(xid)
  fields(ds,f"experiment:{xid}",x,("campaign_ids","hypothesis_unit","variant_control_assignment","sample_window_decision_rule","success_stop_harm","metric_ids","causal_boundary","rollback","human_state"))
  refs(ds,f"experiment:{xid}:campaign",x.get("campaign_ids",[]),cids);refs(ds,f"experiment:{xid}:metric",x.get("metric_ids",[]),mids)
  if x.get("human_state")!="PENDING":ds.add(f"experiment:{xid}:human_state_not_pending")
 scenarios=d.get("budget_scenarios",[]);bids=set()
 for i,x in enumerate(scenarios):
  xid=x.get("id",f"index-{i}");bids.add(xid)
  fields(ds,f"budget:{xid}",x,("campaign_ids","action_range","pacing_marginal_economics","capacity_downside","trigger_kill_switch","rollback","authority","human_state"))
  refs(ds,f"budget:{xid}",x.get("campaign_ids",[]),cids)
  if x.get("human_state")!="PENDING":ds.add(f"budget:{xid}:human_state_not_pending")
 risks=d.get("risks",[]);seenr=set()
 for i,x in enumerate(risks):
  typ=x.get("risk_type",f"index-{i}");seenr.add(typ)
  fields(ds,f"risk:{typ}",x,("statement","likelihood","impact","trigger","mitigation","contingency","owner"))
 for typ in RISK_TYPES-seenr:ds.add(f"risks:missing_type:{typ}")
 decisions=d.get("decision_queue",[]);decided=set()
 for i,x in enumerate(decisions):
  xid=x.get("campaign_id",f"index-{i}");decided.add(xid)
  if xid not in cids:ds.add(f"decision:{xid}:unknown_campaign")
  fields(ds,f"decision:{xid}",x,("recommendation","alternatives","evidence_source_ids","experiment_ids","budget_scenario_ids","uncertainty_prerequisites","decision_owner_needed_by","authorized_operator","before_action_after_verification","human_state"))
  if x.get("recommendation") not in RECOMMENDATIONS:ds.add(f"decision:{xid}:invalid_recommendation")
  refs(ds,f"decision:{xid}:source",x.get("evidence_source_ids",[]),sids);refs(ds,f"decision:{xid}:experiment",x.get("experiment_ids",[]),eids);refs(ds,f"decision:{xid}:budget",x.get("budget_scenario_ids",[]),bids)
  if x.get("human_state")!="PENDING":ds.add(f"decision:{xid}:human_state_not_pending")
 for xid in cids-decided:ds.add(f"decision:missing_campaign:{xid}")
 missing=SECTIONS-set(d.get("output_sections",[]))
 if missing:ds.add("output_sections:missing:"+",".join(sorted(missing)))
 tests=d.get("tests",{})
 for x in TESTS:
  if tests.get(x)!="PASS":ds.add(f"test:{x}:not_pass")
 rev=d.get("reviews",{})
 for x in REVIEWS:
  if rev.get(x)!="PASS":gaps.add(f"review:{x}:not_pass")
 if rev.get("FINAL_HUMAN_ADVERTISING_DECISION")!="PENDING":ds.add("review:FINAL_HUMAN_ADVERTISING_DECISION:must_be_pending")
 for x in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS):ds.add(f"forbidden_flag:{x}")
 states=set(d.get("forbidden_states",[]));states.add(d.get("platform_state","DRAFT"))
 for x in sorted(states&FORBIDDEN_STATES):ds.add(f"forbidden_state:{x}")
 ready=not ds and not gaps
 return {"skill":"advertising-optimization","state":"READY_FOR_HUMAN_ADVERTISING_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"campaigns":len(campaigns),"measurement_contracts":len(contracts),"experience_reviews":len(reviews),"baselines":len(baselines),"diagnoses":len(diagnoses),"experiments":len(experiments),"budget_scenarios":len(scenarios),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(rev.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 advertising lift, incrementality, platform policy accuracy, campaign economics, operator adoption, token cost or duration."}
def main():
 if len(sys.argv)!=2:print("usage: evaluate_advertising_optimization.py INPUT.json",file=sys.stderr);return 2
 r=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")));print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__":raise SystemExit(main())
