#!/usr/bin/env python3
import json,sys
from pathlib import Path
TESTS={"mandate_sources","service_outcome_truth","metric_cohort_integrity","health_risk_hypotheses","intervention_guardrails","customer_choice","decision_boundary"}
REVIEWS={"CUSTOMER_SERVICE","PRODUCT_DELIVERY","FINANCE_RENEWAL","DATA_PRIVACY_FAIRNESS","COMMERCIAL_LEGAL","BRAND_ACCESSIBILITY"}
RISK_TYPES={"SERVICE_DELIVERY_OUTCOME","DATA_METRIC_INTEGRITY","CHURN_CAUSAL_UNCERTAINTY","CUSTOMER_HARM_FAIRNESS","CONSENT_CONTACT_CHOICE","COMMERCIAL_RENEWAL_BILLING"}
SECTIONS={"document_control","source_service_truth","outcome_health_register","metric_cohort_economics","incidents_feedback","risk_interventions","customer_choice_decisions","reviews_audit_version"}
RECOMMENDATIONS={"SUPPORT","RECOVER","IMPROVE","PAUSE","RENEW_REVIEW","EXPAND_REVIEW","EXIT_REVIEW"}
FORBIDDEN_FLAGS={"outcome_fabricated","usage_fabricated","activation_fabricated","adoption_fabricated","satisfaction_fabricated","incident_hidden","complaint_hidden","churn_fabricated","renewal_fabricated","ltv_fabricated","revenue_fabricated","cost_fabricated","cohort_mixed","denominator_hidden","window_mixed","currency_mixed","duplicate_ignored","stale_data_used","missing_scored_zero","model_unversioned","health_score_uncalibrated","sensitive_attribute_used","proxy_discrimination","vulnerability_exploited","consent_bypassed","retention_bypassed","cancel_obstructed","optout_hidden","false_urgency","false_scarcity","forced_continuity","dark_pattern","spam_contact","inactive_called_churn","usage_called_value","complaint_called_churn","review_bypassed","auto_contacted","auto_offered","auto_discounted","auto_renewed","auto_charged","auto_upsold","auto_canceled","auto_closed"}
FORBIDDEN_STATES={"CONTACTED","OFFERED","DISCOUNTED","RENEWED","CHARGED","UPSELL_ACCEPTED","CANCELED","CLOSED","COMPLAINT_SUPPRESSED"}
RIGHTS={"AUTHORIZED","INTERNAL_AUTHORIZED","CUSTOMER_AUTHORIZED","PUBLIC_TERMS_OK"}
def ok(v): return v not in (None,"",[],{})
def evaluate(d):
 ds=set();gaps=set();m=d.get("mandate",{})
 for f in ("service_scope","cohort_scope","account_unit","as_of","horizon","purpose","source_of_truth","owner","consent_retention","decision_authority","renewal_authority","commercial_authority","required_reviews"):
  if not ok(m.get(f)): ds.add(f"mandate:missing_{f}")
 sources=d.get("sources",[]);sids=set()
 for i,s in enumerate(sources):
  sid=s.get("id",f"index-{i}");sids.add(sid)
  for f in ("source_type","locator","version","snapshot_at","rights_purpose","coverage","freshness","confidence","subject"):
   if not ok(s.get(f)): ds.add(f"source:{sid}:missing_{f}")
  if s.get("rights_purpose") not in RIGHTS: ds.add(f"source:{sid}:not_authorized")
 truths=d.get("service_truth",[]);tids=set()
 for i,x in enumerate(truths):
  tid=x.get("id",f"index-{i}");tids.add(tid)
  for f in ("truth_type","statement","source_ids","version","valid_until","conditions_limitations","status"):
   if not ok(x.get(f)): ds.add(f"truth:{tid}:missing_{f}")
  for ref in x.get("source_ids",[]):
   if ref not in sids: ds.add(f"truth:{tid}:unknown_source:{ref}")
  if x.get("status")!="VERIFIED": ds.add(f"truth:{tid}:not_verified")
 metrics=d.get("metrics",[]);mids=set()
 for i,x in enumerate(metrics):
  mid=x.get("id",f"index-{i}");mids.add(mid)
  for f in ("name","purpose","unit_grain","formula","numerator","denominator","cohort","window","source_ids","freshness","missing_late_correction","baseline_target_source","owner","limitations"):
   if not ok(x.get(f)): ds.add(f"metric:{mid}:missing_{f}")
  for ref in x.get("source_ids",[]):
   if ref not in sids: ds.add(f"metric:{mid}:unknown_source:{ref}")
 accounts=d.get("accounts",[]);aids=set()
 for i,a in enumerate(accounts):
  aid=a.get("id",f"index-{i}");aids.add(aid)
  for f in ("contract_id","service_truth_ids","source_ids","lifecycle_stage","outcome_status","activation_status","adoption_status","service_status","complaint_status","renewal_window","renewal_status","contact_consent","data_quality","risk_hypotheses","metric_observations"):
   if not ok(a.get(f)): ds.add(f"account:{aid}:missing_{f}")
  for ref in a.get("service_truth_ids",[]):
   if ref not in tids: ds.add(f"account:{aid}:unknown_truth:{ref}")
  for ref in a.get("source_ids",[]):
   if ref not in sids: ds.add(f"account:{aid}:unknown_source:{ref}")
  seen=set()
  for j,o in enumerate(a.get("metric_observations",[])):
   mid=o.get("metric_id",f"index-{j}");seen.add(mid)
   if mid not in mids: ds.add(f"observation:{aid}:unknown_metric:{mid}")
   for f in ("value","source_ids","confidence","status"):
    if not ok(o.get(f)): ds.add(f"observation:{aid}:{mid}:missing_{f}")
   for ref in o.get("source_ids",[]):
    if ref not in sids: ds.add(f"observation:{aid}:{mid}:unknown_source:{ref}")
 if len(aids)!=len(accounts): ds.add("accounts:duplicate_id")
 incidents=d.get("incidents_feedback",[])
 for i,x in enumerate(incidents):
  iid=x.get("id",f"index-{i}")
  for f in ("account_ids","type","statement","source_ids","timestamp","severity","status","owner","customer_resolution_evidence"):
   if not ok(x.get(f)): ds.add(f"incident:{iid}:missing_{f}")
  for aid in x.get("account_ids",[]):
   if aid not in aids: ds.add(f"incident:{iid}:unknown_account:{aid}")
  for ref in x.get("source_ids",[]):
   if ref not in sids: ds.add(f"incident:{iid}:unknown_source:{ref}")
 cohorts=d.get("cohort_reconciliation",[]);covered=set()
 for i,x in enumerate(cohorts):
  cid=x.get("cohort_id",f"index-{i}")
  for f in ("eligible_ids","active_ids","renewed_ids","churned_ids","excluded_ids","window","metric_basis","revenue_cost_currency","variance","unresolved_items","status"):
   if f not in x or not ok(x.get(f)): ds.add(f"cohort:{cid}:missing_{f}")
  for key in ("eligible_ids","active_ids","renewed_ids","churned_ids"):
   for aid in x.get(key,[]):
    if aid not in aids: ds.add(f"cohort:{cid}:unknown_account:{aid}")
  covered.update(x.get("eligible_ids",[]))
 if covered!=aids: ds.add("cohorts:eligible_coverage_mismatch")
 interventions=d.get("interventions",[]);iids=set()
 for i,x in enumerate(interventions):
  iid=x.get("id",f"index-{i}");iids.add(iid)
  for f in ("account_ids","objective","evidence_source_ids","customer_outcome","consent_channel","owner_capacity","economics","success_criteria","stop_criteria","guardrails","human_state"):
   if not ok(x.get(f)): ds.add(f"intervention:{iid}:missing_{f}")
  for aid in x.get("account_ids",[]):
   if aid not in aids: ds.add(f"intervention:{iid}:unknown_account:{aid}")
  for ref in x.get("evidence_source_ids",[]):
   if ref not in sids: ds.add(f"intervention:{iid}:unknown_source:{ref}")
  if x.get("human_state")!="PENDING": ds.add(f"intervention:{iid}:human_state_not_pending")
 risks=d.get("risks",[]);seenr=set()
 for i,r in enumerate(risks):
  typ=r.get("risk_type",f"index-{i}");seenr.add(typ)
  for f in ("statement","likelihood","impact","trigger","mitigation","contingency","owner"):
   if not ok(r.get(f)): ds.add(f"risk:{typ}:missing_{f}")
 for typ in RISK_TYPES-seenr: ds.add(f"risks:missing_type:{typ}")
 decisions=d.get("decision_queue",[]);decided=set()
 for i,x in enumerate(decisions):
  aid=x.get("account_id",f"index-{i}");decided.add(aid)
  if aid not in aids: ds.add(f"decision:unknown_account:{aid}")
  for f in ("recommendation","alternatives","evidence_source_ids","intervention_ids","decision_owner","needed_by","human_state"):
   if not ok(x.get(f)): ds.add(f"decision:{aid}:missing_{f}")
  if x.get("recommendation") not in RECOMMENDATIONS: ds.add(f"decision:{aid}:invalid_recommendation")
  for iid in x.get("intervention_ids",[]):
   if iid not in iids: ds.add(f"decision:{aid}:unknown_intervention:{iid}")
  for ref in x.get("evidence_source_ids",[]):
   if ref not in sids: ds.add(f"decision:{aid}:unknown_source:{ref}")
  if x.get("human_state")!="PENDING": ds.add(f"decision:{aid}:human_state_not_pending")
 for aid in aids-decided: ds.add(f"decision:missing_account:{aid}")
 missing=SECTIONS-set(d.get("output_sections",[]))
 if missing: ds.add("output_sections:missing:"+",".join(sorted(missing)))
 tests=d.get("tests",{})
 for t in TESTS:
  if tests.get(t)!="PASS": ds.add(f"test:{t}:not_pass")
 reviews=d.get("reviews",{})
 for r in REVIEWS:
  if reviews.get(r)!="PASS": gaps.add(f"review:{r}:not_pass")
 if reviews.get("FINAL_HUMAN_RETENTION_DECISION")!="PENDING": ds.add("review:FINAL_HUMAN_RETENTION_DECISION:must_be_pending")
 for f in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS): ds.add(f"forbidden_flag:{f}")
 states=set(d.get("forbidden_states",[]));states.add(d.get("published_state","DRAFT"))
 for s in sorted(states&FORBIDDEN_STATES): ds.add(f"forbidden_state:{s}")
 ready=not ds and not gaps
 return {"skill":"customer-retention","state":"READY_FOR_HUMAN_RETENTION_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"service_truth_items":len(truths),"metrics":len(metrics),"accounts":len(accounts),"incidents_feedback":len(incidents),"cohorts":len(cohorts),"interventions":len(interventions),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(reviews.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 customer outcome, churn/renewal causality, LTV accuracy, intervention lift/harm, token cost, duration or adoption."}
def main():
 if len(sys.argv)!=2: print("usage: evaluate_customer_retention.py INPUT.json",file=sys.stderr);return 2
 r=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")));print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__":raise SystemExit(main())
