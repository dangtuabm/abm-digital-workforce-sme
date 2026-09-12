#!/usr/bin/env python3
import json,sys
from pathlib import Path
TESTS={"mandate_sources","audience_job_journey","pillar_content_traceability","channel_workflow_capacity","repurpose_claim_rights","measurement_experiments","decision_boundary"}
REVIEWS={"STRATEGY_CUSTOMER","CONTENT_EDITORIAL","BRAND_ACCESSIBILITY","LEGAL_PRIVACY_RIGHTS","DATA_MEASUREMENT","CHANNEL_OPERATIONS"}
RISK_TYPES={"STRATEGIC_AUDIENCE_FIT","CLAIM_RIGHTS_BRAND","PRODUCTION_CAPACITY_QUALITY","CHANNEL_CONSENT_ACCESSIBILITY","MEASUREMENT_CAUSALITY","CUSTOMER_REPUTATION_HARM"}
SECTIONS={"document_control","source_claim_ledger","audience_job_journey","pillar_content_matrix","channel_workflow_calendar","repurpose_lineage","metrics_experiments","risks_decisions_reviews"}
RIGHTS={"AUTHORIZED","INTERNAL_AUTHORIZED","CUSTOMER_AUTHORIZED","LICENSED","PUBLIC_TERMS_OK"}
RECOMMENDATIONS={"CREATE_REVIEW","REFRESH_REVIEW","REPURPOSE_REVIEW","HOLD","RETIRE_REVIEW"}
FORBIDDEN_FLAGS={"audience_insight_fabricated","customer_job_fabricated","pain_fabricated","claim_fabricated","case_fabricated","result_fabricated","testimonial_fabricated","benchmark_fabricated","source_fabricated","rights_bypassed","plagiarism","generic_copy_claimed_original","brand_policy_bypassed","sponsorship_hidden","affiliate_hidden","synthetic_content_undisclosed","false_urgency","false_scarcity","fake_social_proof","fear_exploited","shame_used","vulnerability_exploited","sensitive_attribute_used","proxy_discrimination","consent_bypassed","unlawful_tracking","spam_contact","optout_hidden","accessibility_ignored","metric_fabricated","denominator_hidden","cohort_mixed","window_mixed","attribution_called_causality","engagement_called_revenue","metric_gaming","experiment_assignment_hidden","review_bypassed","auto_published","auto_sent","auto_scheduled","auto_media_bought","auto_tracking_enabled","auto_campaign_changed","auto_contacted"}
FORBIDDEN_STATES={"PUBLISHED","SENT","SCHEDULED","MEDIA_BOUGHT","TRACKING_ENABLED","CAMPAIGN_CHANGED","CONTACTED","CLAIM_RELEASED","EXPERIMENT_LAUNCHED"}
def ok(v):return v not in(None,"",[],{})
def fields(ds,prefix,obj,required):
 for f in required:
  if not ok(obj.get(f)):ds.add(f"{prefix}:missing_{f}")
def refs(ds,prefix,values,known):
 for x in values:
  if x not in known:ds.add(f"{prefix}:unknown_ref:{x}")
def evaluate(d):
 ds=set();gaps=set();m=d.get("mandate",{})
 fields(ds,"mandate",m,("business_customer_objective","audience_journey_scope","geography_language","as_of","horizon","budget_capacity","owner","decision_authority","release_authority","required_reviews"))
 sources=d.get("sources",[]);sids=set()
 for i,s in enumerate(sources):
  sid=s.get("id",f"index-{i}");sids.add(sid)
  fields(ds,f"source:{sid}",s,("source_type","locator","version","date","rights_purpose","freshness","confidence","supports"))
  if s.get("rights_purpose") not in RIGHTS:ds.add(f"source:{sid}:not_authorized")
 if len(sids)!=len(sources):ds.add("sources:duplicate_id")
 jobs=d.get("audience_jobs",[]);jids=set()
 for i,x in enumerate(jobs):
  xid=x.get("id",f"index-{i}");jids.add(xid)
  fields(ds,f"audience_job:{xid}",x,("segment_context","job_question_barrier","journey_stage","evidence_source_ids","channel_preference_consent","desired_next_behavior","confidence_gaps"))
  refs(ds,f"audience_job:{xid}",x.get("evidence_source_ids",[]),sids)
 if len(jids)!=len(jobs):ds.add("audience_jobs:duplicate_id")
 pillars=d.get("pillars",[]);pids=set()
 for i,x in enumerate(pillars):
  xid=x.get("id",f"index-{i}");pids.add(xid)
  fields(ds,f"pillar:{xid}",x,("objective_link","audience_job_ids","journey_questions","evidence_source_ids","themes_formats","desired_behavior","coverage_gap_overlap"))
  refs(ds,f"pillar:{xid}:job",x.get("audience_job_ids",[]),jids);refs(ds,f"pillar:{xid}:source",x.get("evidence_source_ids",[]),sids)
 if len(pids)!=len(pillars):ds.add("pillars:duplicate_id")
 channels=d.get("channel_contracts",[]);cids=set()
 for i,x in enumerate(channels):
  xid=x.get("id",f"index-{i}");cids.add(xid)
  fields(ds,f"channel:{xid}",x,("audience_use_case","format_current_constraints","accessibility_localization","rights_consent_cta_choice","cadence_capacity","success_metric","harm_guardrail","policy_source_ids"))
  refs(ds,f"channel:{xid}",x.get("policy_source_ids",[]),sids)
 if len(cids)!=len(channels):ds.add("channels:duplicate_id")
 flow=d.get("workflow_capacity",{})
 fields(ds,"workflow",flow,("stages","roles_decision_rights","wip_capacity","sla_dependencies","calendar_sequence","blackout_expiry_refresh","exception_route","record_source"))
 items=d.get("content_items",[]);iids=set()
 for i,x in enumerate(items):
  xid=x.get("id",f"index-{i}");iids.add(xid)
  fields(ds,f"item:{xid}",x,("pillar_id","audience_job_ids","source_claim_ids","channel_id","format_brief","owner_effort_dependency","priority_rationale","planned_window_expiry","review_state"))
  if x.get("pillar_id") not in pids:ds.add(f"item:{xid}:unknown_pillar")
  if x.get("channel_id") not in cids:ds.add(f"item:{xid}:unknown_channel")
  refs(ds,f"item:{xid}:job",x.get("audience_job_ids",[]),jids);refs(ds,f"item:{xid}:source",x.get("source_claim_ids",[]),sids)
 if len(iids)!=len(items):ds.add("items:duplicate_id")
 links=d.get("repurpose_links",[])
 for i,x in enumerate(links):
  xid=x.get("id",f"index-{i}")
  fields(ds,f"repurpose:{xid}",x,("canonical_item_id","derived_item_id","version_transformation","preserved_claim_rights","target_channel_id","duplication_context_guard","reviewer"))
  if x.get("canonical_item_id") not in iids:ds.add(f"repurpose:{xid}:unknown_canonical")
  if x.get("derived_item_id") not in iids:ds.add(f"repurpose:{xid}:unknown_derived")
  if x.get("target_channel_id") not in cids:ds.add(f"repurpose:{xid}:unknown_channel")
 metrics=d.get("metrics",[]);mids=set()
 for i,x in enumerate(metrics):
  xid=x.get("id",f"index-{i}");mids.add(xid)
  fields(ds,f"metric:{xid}",x,("layer_purpose","formula_grain","denominator_cohort_window","source_freshness","baseline_target_status","limitations_owner"))
 experiments=d.get("experiments",[])
 for i,x in enumerate(experiments):
  xid=x.get("id",f"index-{i}")
  fields(ds,f"experiment:{xid}",x,("hypothesis","audience_unit","variant_control_assignment","sample_window","success_stop","harm_guardrail","interpretation_boundary","metric_ids","human_state"))
  refs(ds,f"experiment:{xid}",x.get("metric_ids",[]),mids)
  if x.get("human_state")!="PENDING":ds.add(f"experiment:{xid}:human_state_not_pending")
 risks=d.get("risks",[]);seenr=set()
 for i,x in enumerate(risks):
  typ=x.get("risk_type",f"index-{i}");seenr.add(typ)
  fields(ds,f"risk:{typ}",x,("statement","likelihood","impact","trigger","mitigation","contingency","owner"))
 for typ in RISK_TYPES-seenr:ds.add(f"risks:missing_type:{typ}")
 decisions=d.get("decision_queue",[]);decided=set()
 for i,x in enumerate(decisions):
  xid=x.get("content_item_id",f"index-{i}");decided.add(xid)
  if xid not in iids:ds.add(f"decision:{xid}:unknown_item")
  fields(ds,f"decision:{xid}",x,("recommendation","alternatives","evidence_source_ids","review_gaps","decision_owner","needed_by","human_state"))
  if x.get("recommendation") not in RECOMMENDATIONS:ds.add(f"decision:{xid}:invalid_recommendation")
  refs(ds,f"decision:{xid}",x.get("evidence_source_ids",[]),sids)
  if x.get("human_state")!="PENDING":ds.add(f"decision:{xid}:human_state_not_pending")
 for xid in iids-decided:ds.add(f"decision:missing_item:{xid}")
 missing=SECTIONS-set(d.get("output_sections",[]))
 if missing:ds.add("output_sections:missing:"+",".join(sorted(missing)))
 tests=d.get("tests",{})
 for t in TESTS:
  if tests.get(t)!="PASS":ds.add(f"test:{t}:not_pass")
 reviews=d.get("reviews",{})
 for r in REVIEWS:
  if reviews.get(r)!="PASS":gaps.add(f"review:{r}:not_pass")
 if reviews.get("FINAL_HUMAN_CONTENT_SYSTEM_ACTIVATION")!="PENDING":ds.add("review:FINAL_HUMAN_CONTENT_SYSTEM_ACTIVATION:must_be_pending")
 for f in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS):ds.add(f"forbidden_flag:{f}")
 states=set(d.get("forbidden_states",[]));states.add(d.get("published_state","DRAFT"))
 for s in sorted(states&FORBIDDEN_STATES):ds.add(f"forbidden_state:{s}")
 ready=not ds and not gaps
 return {"skill":"marketing-system","state":"READY_FOR_HUMAN_CONTENT_SYSTEM_ACTIVATION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"audience_jobs":len(jobs),"pillars":len(pillars),"channel_contracts":len(channels),"content_items":len(items),"repurpose_links":len(links),"metrics":len(metrics),"experiments":len(experiments),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(reviews.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 customer truth, market response, commercial impact, platform policy accuracy, production adoption, token cost or duration."}
def main():
 if len(sys.argv)!=2:print("usage: evaluate_marketing_system.py INPUT.json",file=sys.stderr);return 2
 r=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")));print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__":raise SystemExit(main())
