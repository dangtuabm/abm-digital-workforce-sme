#!/usr/bin/env python3
import json,sys
from pathlib import Path

GATE_TESTS={"mandate_sources_contracts","data_quality_precheck","baseline_method_assumptions","detection_reproducibility","signal_triage_hypothesis","impact_action_boundary","feedback_audit"}
REVIEWS={"BUSINESS_METRIC_OWNER","DATA_STEWARD_QUALITY","ANALYTICS_STATISTICS","DATA_ENGINEERING_OBSERVABILITY","RISK_SECURITY_COMPLIANCE","OPERATIONS_INCIDENT_OWNER"}
RISK_TYPES={"BASELINE_COMPARABILITY_DRIFT","DATA_QUALITY_PIPELINE_LINEAGE","METHOD_ASSUMPTION_THRESHOLD_MULTIPLICITY","SEASONALITY_SEGMENT_DENOMINATOR","CAUSALITY_ROOT_CAUSE_OVERCLAIM","ALERT_FATIGUE_ACTION_AUTHORITY"}
SECTIONS={"document_control","source_contract_baseline","detector_registry","signal_register","triage_investigation","cause_evidence_tests","impact_actions_monitoring","risks_decisions_reviews_audit"}
RIGHTS={"PUBLIC_AUTHORIZED","INTERNAL_AUTHORIZED","OWNER_AUTHORIZED","STEWARD_AUTHORIZED","FINANCE_AUTHORIZED","LEGAL_AUTHORIZED","CONTRACT_AUTHORIZED","CUSTOMER_AUTHORIZED"}
METHODS={"RULE_CONSTRAINT","ABSOLUTE_RELATIVE_DELTA","ROBUST_IQR_MAD","SHEWHART_CONTROL_CHART","TIME_SERIES_RESIDUAL","CHANGE_POINT","MULTIVARIATE","ENSEMBLE_APPROVED"}
TRIAGE_TYPES={"DATA_QUALITY","PIPELINE","METRIC_SEMANTIC","EXPECTED_EVENT","BUSINESS_PROCESS","EXTERNAL","SECURITY_RISK","UNRESOLVED"}
CAUSE_STATES={"SUPPORTED","DISPROVED","UNRESOLVED"}
RECOMMENDATIONS={"MANDATE_IMPACT_REVIEW","SOURCE_CONTRACT_REVIEW","BASELINE_METHOD_REVIEW","SIGNAL_TRIAGE_REVIEW","HYPOTHESIS_CAUSE_REVIEW","ACTION_AUTHORITY_REVIEW","DETECTOR_FEEDBACK_REVIEW","REVISE","HOLD"}
FORBIDDEN_FLAGS={
"scope_fabricated","impact_fabricated","severity_fabricated","owner_fabricated","reviewer_fabricated","action_authority_fabricated","source_fabricated","sor_fabricated","locator_fabricated","snapshot_fabricated","hash_fabricated","schema_fabricated","grain_fabricated","key_fabricated","time_basis_fabricated","timezone_fabricated","unit_fabricated","freshness_fabricated","completeness_fabricated","rights_fabricated","lineage_fabricated","query_fabricated","query_hash_fabricated","model_fabricated","model_hash_fabricated","change_log_fabricated","contract_fabricated","metric_definition_fabricated","formula_fabricated","numerator_fabricated","denominator_fabricated","aggregation_fabricated","dimension_fabricated","filter_fabricated","null_rule_fabricated","late_rule_fabricated","restatement_rule_fabricated","baseline_fabricated","baseline_window_fabricated","reference_population_fabricated","regime_fabricated","stability_fabricated","trend_fabricated","seasonality_fabricated","distribution_fabricated","sample_size_fabricated","missingness_fabricated","known_event_fabricated","comparability_fabricated","detector_fabricated","method_fabricated","assumption_fabricated","parameter_fabricated","threshold_fabricated","threshold_authority_fabricated","calibration_fabricated","false_positive_cost_fabricated","false_negative_cost_fabricated","multiplicity_hidden","uncertainty_hidden","score_fabricated","control_limit_fabricated","p_value_fabricated","p_value_without_assumptions","expected_fabricated","actual_fabricated","delta_fabricated","signal_fabricated","evidence_fabricated","quality_issue_hidden","schema_break_hidden","pipeline_change_hidden","denominator_effect_hidden","segment_effect_hidden","seasonality_hidden","known_event_hidden","late_data_hidden","revision_hidden","non_comparable_baseline_hidden","small_sample_hidden","normality_assumed","stationarity_assumed","multiple_testing_ignored","alert_called_anomaly","anomaly_called_incident","correlation_called_cause","temporal_order_called_cause","score_called_impact","outlier_called_error","outlier_silently_deleted","record_silently_corrected","missing_called_zero","hypothesis_fabricated","mechanism_fabricated","supporting_evidence_fabricated","disconfirming_test_hidden","alternative_cause_hidden","confounder_hidden","root_cause_fabricated","root_cause_overclaimed","fraud_declared_without_authority","security_breach_declared_without_authority","impact_overclaimed","action_fabricated","rollback_fabricated","verification_fabricated","feedback_label_fabricated","detector_drift_hidden","review_bypassed","source_instruction_executed","log_instruction_executed","sql_executed","code_executed","macro_executed","secret_exposed","credential_exposed","pii_exposed","public_llm_unapproved","auto_data_deleted","auto_data_corrected","auto_data_imputed","auto_data_quarantined","auto_metric_changed","auto_formula_changed","auto_baseline_changed","auto_threshold_changed","auto_detector_changed","auto_alert_suppressed","auto_alert_closed","auto_incident_declared","auto_root_cause_accepted","auto_fraud_label_applied","auto_account_locked","auto_process_stopped","auto_refund_issued","auto_charge_applied","auto_customer_contacted","auto_employee_actioned","auto_external_notified","auto_fix_deployed","auto_incident_published","auto_detector_tuned","audit_log_mutated","evidence_altered","evidence_deleted"
}
FORBIDDEN_STATES={"DATA_DELETED","DATA_CORRECTED","DATA_IMPUTED","DATA_QUARANTINED","METRIC_CHANGED","FORMULA_CHANGED","BASELINE_CHANGED","THRESHOLD_CHANGED","DETECTOR_CHANGED","ALERT_SUPPRESSED","ALERT_CLOSED","INCIDENT_DECLARED","ROOT_CAUSE_ACCEPTED","FRAUD_LABEL_APPLIED","ACCOUNT_LOCKED","PROCESS_STOPPED","REFUND_ISSUED","CHARGE_APPLIED","CUSTOMER_CONTACTED","EMPLOYEE_ACTIONED","EXTERNAL_NOTIFIED","FIX_DEPLOYED","INCIDENT_PUBLISHED","DETECTOR_TUNED","AUDIT_LOG_MUTATED","EVIDENCE_ALTERED","EVIDENCE_DELETED"}

def ok(v): return v not in (None,"",[],{})
def fields(ds,p,obj,req):
 for f in req:
  if not ok(obj.get(f)): ds.add(f"{p}:missing_{f}")
def refs(ds,p,vals,known):
 for x in vals:
  if x not in known: ds.add(f"{p}:unknown_ref:{x}")

def evaluate(d):
 ds=set(); gaps=set(); m=d.get("mandate",{})
 fields(ds,"mandate",m,("decision_use","metric_process_entity_scope_exclusions","impact_severity_rubric","as_of_horizon","owners_reviewers","action_authority_boundary","classification_access_rights","non_goals"))
 sources=d.get("sources",[]); sids=set()
 for i,x in enumerate(sources):
  xid=x.get("id",f"index-{i}"); sids.add(xid); fields(ds,f"source:{xid}",x,("locator_environment","owner_sor","snapshot_version_hash","schema_grain_keys","time_timezone_unit","freshness_completeness","classification_purpose_rights","lineage_query_model_hash","change_revision_log"))
  if x.get("classification_purpose_rights",{}).get("rights") not in RIGHTS: ds.add(f"source:{xid}:not_authorized")
 if len(sids)!=len(sources): ds.add("sources:duplicate_id")
 contracts=d.get("contracts",[]); cids=set()
 for i,x in enumerate(contracts):
  xid=x.get("id",f"index-{i}"); cids.add(xid); fields(ds,f"contract:{xid}",x,("metric_event_definition","formula_numerator_denominator","aggregation_grain","dimensions_filters","time_window_timezone_unit","null_duplicate_late_restatement","source_ids","owner_version_effective")); refs(ds,f"contract:{xid}:source",x.get("source_ids",[]),sids)
 baselines=d.get("baselines",[]); bids=set()
 for i,x in enumerate(baselines):
  xid=x.get("id",f"index-{i}"); bids.add(xid); fields(ds,f"baseline:{xid}",x,("contract_ids","source_ids","reference_population_window","regime_version","stability_trend_seasonality","distribution_sample_missingness","known_events","comparability","owner_evidence")); refs(ds,f"baseline:{xid}:contract",x.get("contract_ids",[]),cids); refs(ds,f"baseline:{xid}:source",x.get("source_ids",[]),sids)
 detectors=d.get("detectors",[]); dids=set()
 for i,x in enumerate(detectors):
  xid=x.get("id",f"index-{i}"); dids.add(xid); fields(ds,f"detector:{xid}",x,("baseline_ids","contract_ids","method","rationale","assumptions_tests","parameters_version_code_hash","threshold_authority","calibration_fp_fn_cost","multiplicity_uncertainty","owner_state")); refs(ds,f"detector:{xid}:baseline",x.get("baseline_ids",[]),bids); refs(ds,f"detector:{xid}:contract",x.get("contract_ids",[]),cids)
  if x.get("method") not in METHODS: ds.add(f"detector:{xid}:invalid_method")
 signals=d.get("signals",[]); sigids=set()
 for i,x in enumerate(signals):
  xid=x.get("id",f"index-{i}"); sigids.add(xid); fields(ds,f"signal:{xid}",x,("detector_id","source_ids","contract_ids","expected_actual_delta_score","window_slice","evidence_hash","quality_checks","segment_denominator_time_checks","impact_confidence_rubric","state_limitations")); refs(ds,f"signal:{xid}:detector",[x.get("detector_id")],dids); refs(ds,f"signal:{xid}:source",x.get("source_ids",[]),sids); refs(ds,f"signal:{xid}:contract",x.get("contract_ids",[]),cids)
 investigations=d.get("investigations",[]); iids=set()
 for i,x in enumerate(investigations):
  xid=x.get("id",f"index-{i}"); iids.add(xid); fields(ds,f"investigation:{xid}",x,("signal_ids","triage_type","raw_aggregate_adjacent_control","lineage_pipeline_revision","metric_semantic_checks","known_event_external_checks","owner_sla","status_evidence")); refs(ds,f"investigation:{xid}:signal",x.get("signal_ids",[]),sigids)
  if x.get("triage_type") not in TRIAGE_TYPES: ds.add(f"investigation:{xid}:invalid_triage_type")
 hypotheses=d.get("hypotheses",[]); hids=set()
 for i,x in enumerate(hypotheses):
  xid=x.get("id",f"index-{i}"); hids.add(xid); fields(ds,f"hypothesis:{xid}",x,("investigation_ids","mechanism","predicted_observations","supporting_evidence","disconfirming_test_result","alternatives_confounders","cause_state","owner_reviewer_limitations")); refs(ds,f"hypothesis:{xid}:investigation",x.get("investigation_ids",[]),iids)
  if x.get("cause_state") not in CAUSE_STATES: ds.add(f"hypothesis:{xid}:invalid_cause_state")
 actions=d.get("action_options",[])
 for i,x in enumerate(actions):
  xid=x.get("id",f"index-{i}"); fields(ds,f"action:{xid}",x,("signal_investigation_hypothesis_ids","recommendation","impact_blast_radius","authority_prerequisites","owner_sla","rollback","verification","human_state")); rr=x.get("signal_investigation_hypothesis_ids",{}); refs(ds,f"action:{xid}:signal",rr.get("signal_ids",[]),sigids); refs(ds,f"action:{xid}:investigation",rr.get("investigation_ids",[]),iids); refs(ds,f"action:{xid}:hypothesis",rr.get("hypothesis_ids",[]),hids)
  if x.get("human_state")!="PENDING": ds.add(f"action:{xid}:human_state_not_pending")
 feedback=d.get("monitoring_feedback",[])
 for i,x in enumerate(feedback):
  xid=x.get("id",f"index-{i}"); fields(ds,f"feedback:{xid}",x,("detector_ids","labels_coverage","recurrence_misses_false_positives","performance_cost_metric","drift_monitor","proposed_tuning_version_diff","approval_rollback_human_state")); refs(ds,f"feedback:{xid}:detector",x.get("detector_ids",[]),dids)
  if x.get("approval_rollback_human_state",{}).get("human_state")!="PENDING": ds.add(f"feedback:{xid}:human_state_not_pending")
 risks=d.get("risks",[]); seen=set()
 for i,x in enumerate(risks):
  typ=x.get("risk_type",f"index-{i}"); seen.add(typ); fields(ds,f"risk:{typ}",x,("statement","likelihood","impact","trigger","mitigation","contingency","owner_role"))
 for typ in RISK_TYPES-seen: ds.add(f"risks:missing_type:{typ}")
 decisions=d.get("decision_queue",[])
 for i,x in enumerate(decisions):
  xid=x.get("id",f"index-{i}"); fields(ds,f"decision:{xid}",x,("recommendation","issue_options","evidence_source_ids","signal_ids","review_gaps","decision_owner_role","needed_by","human_state")); refs(ds,f"decision:{xid}:source",x.get("evidence_source_ids",[]),sids); refs(ds,f"decision:{xid}:signal",x.get("signal_ids",[]),sigids)
  if x.get("recommendation") not in RECOMMENDATIONS: ds.add(f"decision:{xid}:invalid_recommendation")
  if x.get("human_state")!="PENDING": ds.add(f"decision:{xid}:human_state_not_pending")
 missing=SECTIONS-set(d.get("output_sections",[]))
 if missing: ds.add("output_sections:missing:"+",".join(sorted(missing)))
 tests=d.get("gate_tests",{})
 for x in GATE_TESTS:
  if tests.get(x)!="PASS": ds.add(f"test:{x}:not_pass")
 rev=d.get("reviews",{})
 for x in REVIEWS:
  if rev.get(x)!="PASS": gaps.add(f"review:{x}:not_pass")
 if rev.get("FINAL_HUMAN_ANOMALY_DECISION")!="PENDING": ds.add("review:FINAL_HUMAN_ANOMALY_DECISION:must_be_pending")
 for x in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS): ds.add(f"forbidden_flag:{x}")
 states=set(d.get("forbidden_states",[])); states.add(d.get("operational_state","DRAFT"))
 for x in sorted(states&FORBIDDEN_STATES): ds.add(f"forbidden_state:{x}")
 ready=not ds and not gaps
 return {"skill":"data-anomaly","state":"READY_FOR_HUMAN_ANOMALY_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"contracts":len(contracts),"baselines":len(baselines),"detectors":len(detectors),"signals":len(signals),"investigations":len(investigations),"hypotheses":len(hypotheses),"action_options":len(actions),"monitoring_feedback":len(feedback),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in GATE_TESTS),"reviews_passed":sum(rev.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 source/metric truth, baseline comparability, method assumptions, threshold calibration, signal precision/recall, causal/root-cause validity, incident severity, production action authority, legal compliance, false-trigger rate, token cost or duration."}

def main():
 if len(sys.argv)!=2: print("usage: evaluate_data_anomaly.py INPUT.json",file=sys.stderr); return 2
 result=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))); print(json.dumps(result,ensure_ascii=False,indent=2)); return 0 if result["state"]!="NOT_READY" else 1
if __name__=="__main__": raise SystemExit(main())

