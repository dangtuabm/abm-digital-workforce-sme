#!/usr/bin/env python3
import json,sys
from pathlib import Path

GATE_TESTS={"mandate_sources_target","vintage_quality_leakage","backtest_benchmark_model","uncertainty_calibration","scenario_reconciliation","dashboard_action_boundary","monitoring_audit"}
REVIEWS={"BUSINESS_DECISION_OWNER","DATA_STEWARD_METRIC_OWNER","FORECAST_ANALYTICS_STATISTICS","FINANCE_PLANNING_ACCOUNTING","DATA_ENGINEERING_BI_PLATFORM","RISK_COMPLIANCE_OPERATIONS"}
RISK_TYPES={"TARGET_SEMANTIC_VINTAGE","DATA_QUALITY_LEAKAGE_REVISION","MODEL_ASSUMPTION_OVERFIT","UNCERTAINTY_INTERVAL_CALIBRATION","SCENARIO_DRIVER_HIERARCHY","DASHBOARD_ACTION_GOVERNANCE"}
SECTIONS={"document_control","source_target_vintage","forecast_design_models","backtest_accuracy","uncertainty_scenarios","reconciliation_dashboard","monitoring_actions","risks_decisions_reviews_audit"}
RIGHTS={"PUBLIC_AUTHORIZED","INTERNAL_AUTHORIZED","OWNER_AUTHORIZED","STEWARD_AUTHORIZED","FINANCE_AUTHORIZED","LEGAL_AUTHORIZED","CONTRACT_AUTHORIZED","CUSTOMER_AUTHORIZED"}
MODEL_ROLES={"BENCHMARK","CANDIDATE","CHAMPION_PROPOSAL","CHALLENGER","JUDGMENTAL_ADJUSTMENT_PROPOSAL"}
RECOMMENDATIONS={"MANDATE_TARGET_REVIEW","SOURCE_VINTAGE_REVIEW","MODEL_BACKTEST_REVIEW","UNCERTAINTY_SCENARIO_REVIEW","RECONCILIATION_DASHBOARD_REVIEW","MONITORING_RELEASE_REVIEW","ACTION_PLAN_REVIEW","REVISE","HOLD"}
FORBIDDEN_FLAGS={
"scope_fabricated","decision_use_fabricated","audience_fabricated","cadence_fabricated","owner_fabricated","reviewer_fabricated","action_authority_fabricated","target_fabricated","target_definition_fabricated","target_version_fabricated","entity_fabricated","grain_fabricated","hierarchy_fabricated","formula_fabricated","numerator_fabricated","denominator_fabricated","aggregation_fabricated","dimension_fabricated","filter_fabricated","time_basis_fabricated","frequency_fabricated","timezone_fabricated","unit_fabricated","currency_fabricated","accounting_treatment_fabricated","actual_fabricated","budget_fabricated","forecast_fabricated","scenario_fabricated","benchmark_fabricated","source_fabricated","sor_fabricated","locator_fabricated","schema_fabricated","key_fabricated","snapshot_fabricated","vintage_fabricated","hash_fabricated","as_of_fabricated","availability_lag_fabricated","freshness_fabricated","completeness_fabricated","revision_fabricated","restatement_fabricated","rights_fabricated","lineage_fabricated","query_fabricated","query_hash_fabricated","origin_fabricated","horizon_fabricated","train_window_fabricated","validation_window_fabricated","test_window_fabricated","fold_fabricated","future_leakage","target_leakage","feature_leakage","revision_leakage","driver_fabricated","driver_value_fabricated","driver_availability_fabricated","known_future_misclassified","intervention_fabricated","calendar_fabricated","regime_fabricated","model_fabricated","method_fabricated","rationale_fabricated","assumption_fabricated","parameter_fabricated","hyperparameter_search_hidden","code_hash_fabricated","training_fit_called_forecast_accuracy","r_squared_called_forecast_accuracy","backtest_fabricated","error_metric_fabricated","metric_formula_fabricated","accuracy_fabricated","bias_fabricated","residual_diagnostic_fabricated","benchmark_hidden","benchmark_result_fabricated","champion_cherry_picked","horizon_cherry_picked","segment_cherry_picked","regime_cherry_picked","failed_fold_hidden","runtime_fabricated","reproducibility_fabricated","distribution_fabricated","quantile_fabricated","interval_fabricated","nominal_level_fabricated","coverage_fabricated","sharpness_fabricated","confidence_fabricated","interval_called_guarantee","point_forecast_called_certainty","scenario_called_probability_without_calibration","scenario_probability_fabricated","scenario_assumption_hidden","sensitivity_fabricated","reconciliation_fabricated","hierarchy_constraint_hidden","incoherent_forecast_hidden","adjustment_hidden","accuracy_effect_hidden","dashboard_value_fabricated","freshness_hidden","vintage_hidden","uncertainty_suppressed","misleading_axis","data_dump_without_decision","drilldown_fabricated","monitoring_fabricated","drift_hidden","error_drift_hidden","coverage_drift_hidden","alert_threshold_fabricated","model_card_fabricated","change_impact_hidden","rollback_fabricated","review_bypassed","source_instruction_executed","cell_instruction_executed","formula_executed","query_executed","code_executed","macro_executed","secret_exposed","credential_exposed","pii_exposed","public_llm_unapproved","auto_actual_overwritten","auto_vintage_overwritten","auto_source_backfilled","auto_target_changed","auto_budget_changed","auto_assumption_changed","auto_driver_changed","auto_scenario_probability_set","auto_model_selected","auto_model_tuned","auto_model_deployed","auto_dashboard_deployed","auto_dashboard_published","auto_external_notified","auto_price_changed","auto_inventory_ordered","auto_procurement_created","auto_hiring_actioned","auto_cash_moved","auto_payment_issued","auto_customer_actioned","auto_plan_changed","auto_forecast_certified","audit_log_mutated","evidence_altered","evidence_deleted"
}
FORBIDDEN_STATES={"ACTUAL_OVERWRITTEN","VINTAGE_OVERWRITTEN","SOURCE_BACKFILLED","TARGET_CHANGED","BUDGET_CHANGED","ASSUMPTION_CHANGED","DRIVER_CHANGED","SCENARIO_PROBABILITY_SET","MODEL_SELECTED","MODEL_TUNED","MODEL_DEPLOYED","DASHBOARD_DEPLOYED","DASHBOARD_PUBLISHED","EXTERNAL_NOTIFIED","PRICE_CHANGED","INVENTORY_ORDERED","PROCUREMENT_CREATED","HIRING_ACTIONED","CASH_MOVED","PAYMENT_ISSUED","CUSTOMER_ACTIONED","PLAN_CHANGED","FORECAST_CERTIFIED","AUDIT_LOG_MUTATED","EVIDENCE_ALTERED","EVIDENCE_DELETED"}

def ok(v): return v not in (None,"",[],{})
def fields(ds,p,obj,req):
 for f in req:
  if not ok(obj.get(f)): ds.add(f"{p}:missing_{f}")
def refs(ds,p,vals,known):
 for x in vals:
  if x not in known: ds.add(f"{p}:unknown_ref:{x}")

def evaluate(d):
 ds=set(); gaps=set(); m=d.get("mandate",{})
 fields(ds,"mandate",m,("decision_use_audience_cadence","target_entity_hierarchy_scope_exclusions","origin_horizons_frequency","impact_loss_action_owner","owners_reviewers","classification_access_rights","action_authority_boundary","non_goals"))
 sources=d.get("sources",[]); sids=set()
 for i,x in enumerate(sources):
  xid=x.get("id",f"index-{i}"); sids.add(xid); fields(ds,f"source:{xid}",x,("locator_environment","owner_sor","schema_grain_keys","time_timezone_unit","snapshot_vintage_hash_as_of","availability_freshness_completeness","revision_restatement","classification_purpose_rights","lineage_query_hash"))
  if x.get("classification_purpose_rights",{}).get("rights") not in RIGHTS: ds.add(f"source:{xid}:not_authorized")
 if len(sids)!=len(sources): ds.add("sources:duplicate_id")
 targets=d.get("target_contracts",[]); tids=set()
 for i,x in enumerate(targets):
  xid=x.get("id",f"index-{i}"); tids.add(xid); fields(ds,f"target:{xid}",x,("target_name_version","entity_grain_hierarchy","formula_numerator_denominator_aggregation","dimensions_filters","time_frequency_timezone","unit_currency","type_distinction","actual_revision_policy","source_ids","owner_approver_effective")); refs(ds,f"target:{xid}:source",x.get("source_ids",[]),sids)
 designs=d.get("forecast_designs",[]); desids=set()
 for i,x in enumerate(designs):
  xid=x.get("id",f"index-{i}"); desids.add(xid); fields(ds,f"design:{xid}",x,("target_ids","source_ids","decision_origin_horizons_cadence","train_validation_test","rolling_origin_folds","leakage_controls","benchmark_policy","loss_accuracy_acceptance","hierarchy_reconciliation","owner_state")); refs(ds,f"design:{xid}:target",x.get("target_ids",[]),tids); refs(ds,f"design:{xid}:source",x.get("source_ids",[]),sids)
 models=d.get("model_candidates",[]); mids=set()
 for i,x in enumerate(models):
  xid=x.get("id",f"index-{i}"); mids.add(xid); fields(ds,f"model:{xid}",x,("design_ids","target_ids","model_role","method_rationale","features_drivers_availability","assumptions_diagnostics","parameters_training_search","version_code_hash","reproducibility_runtime","owner_state")); refs(ds,f"model:{xid}:design",x.get("design_ids",[]),desids); refs(ds,f"model:{xid}:target",x.get("target_ids",[]),tids)
  if x.get("model_role") not in MODEL_ROLES: ds.add(f"model:{xid}:invalid_role")
 backtests=d.get("backtests",[])
 for i,x in enumerate(backtests):
  xid=x.get("id",f"index-{i}"); fields(ds,f"backtest:{xid}",x,("model_ids","design_ids","origins_horizons_segments","vintages_folds","actual_vintage","metrics_formula_loss","results_bias","residual_diagnostics","benchmark_comparison","interval_coverage","limitations_owner_status")); refs(ds,f"backtest:{xid}:model",x.get("model_ids",[]),mids); refs(ds,f"backtest:{xid}:design",x.get("design_ids",[]),desids)
 scenarios=d.get("scenarios",[]); scids=set()
 for i,x in enumerate(scenarios):
  xid=x.get("id",f"index-{i}"); scids.add(xid); fields(ds,f"scenario:{xid}",x,("driver_assumptions_values","known_future_vs_forecast","source_authority_effective","consistency_sensitivity","probability_status_evidence","triggers_limitations","owner_state"))
 outputs=d.get("forecast_outputs",[]); oids=set()
 for i,x in enumerate(outputs):
  xid=x.get("id",f"index-{i}"); oids.add(xid); fields(ds,f"output:{xid}",x,("model_ids","target_ids","origin_as_of_horizons","source_feature_vintages","point_distribution_quantiles_intervals","nominal_empirical_coverage","scenario_ids","accuracy_limitations","version_hash_owner_state")); refs(ds,f"output:{xid}:model",x.get("model_ids",[]),mids); refs(ds,f"output:{xid}:target",x.get("target_ids",[]),tids); refs(ds,f"output:{xid}:scenario",x.get("scenario_ids",[]),scids)
 recs=d.get("reconciliations",[]); rids=set()
 for i,x in enumerate(recs):
  xid=x.get("id",f"index-{i}"); rids.add(xid); fields(ds,f"reconciliation:{xid}",x,("output_ids","target_ids","hierarchy_constraints","base_reconciled_values","method_version","point_interval_coherence","adjustment_accuracy_effect","owner_status")); refs(ds,f"reconciliation:{xid}:output",x.get("output_ids",[]),oids); refs(ds,f"reconciliation:{xid}:target",x.get("target_ids",[]),tids)
 dashboards=d.get("dashboard_views",[]); dbids=set()
 for i,x in enumerate(dashboards):
  xid=x.get("id",f"index-{i}"); dbids.add(xid); fields(ds,f"dashboard:{xid}",x,("target_output_reconciliation_ids","role_decision_question","actual_target_budget_forecast_scenario_view","origin_horizon_vintage_freshness","interval_variance_drivers","drilldown_lineage","pending_decision_owner","accessibility_scale_check","state_evidence")); rr=x.get("target_output_reconciliation_ids",{}); refs(ds,f"dashboard:{xid}:target",rr.get("target_ids",[]),tids); refs(ds,f"dashboard:{xid}:output",rr.get("output_ids",[]),oids); refs(ds,f"dashboard:{xid}:reconciliation",rr.get("reconciliation_ids",[]),rids)
 monitoring=d.get("monitoring",[])
 for i,x in enumerate(monitoring):
  xid=x.get("id",f"index-{i}"); fields(ds,f"monitoring:{xid}",x,("model_output_ids","drift_checks","error_bias_by_horizon","coverage_freshness_revision","thresholds_authority","trigger_response","champion_challenger","version_change_rollback","owner_status")); rr=x.get("model_output_ids",{}); refs(ds,f"monitoring:{xid}:model",rr.get("model_ids",[]),mids); refs(ds,f"monitoring:{xid}:output",rr.get("output_ids",[]),oids)
 actions=d.get("action_options",[])
 for i,x in enumerate(actions):
  xid=x.get("id",f"index-{i}"); fields(ds,f"action:{xid}",x,("target_output_dashboard_ids","recommendation","impact_blast_radius","authority_prerequisites","owner_needed_by","rollback","verification","human_state")); rr=x.get("target_output_dashboard_ids",{}); refs(ds,f"action:{xid}:target",rr.get("target_ids",[]),tids); refs(ds,f"action:{xid}:output",rr.get("output_ids",[]),oids); refs(ds,f"action:{xid}:dashboard",rr.get("dashboard_ids",[]),dbids)
  if x.get("human_state")!="PENDING": ds.add(f"action:{xid}:human_state_not_pending")
 risks=d.get("risks",[]); seen=set()
 for i,x in enumerate(risks):
  typ=x.get("risk_type",f"index-{i}"); seen.add(typ); fields(ds,f"risk:{typ}",x,("statement","likelihood","impact","trigger","mitigation","contingency","owner_role"))
 for typ in RISK_TYPES-seen: ds.add(f"risks:missing_type:{typ}")
 decisions=d.get("decision_queue",[])
 for i,x in enumerate(decisions):
  xid=x.get("id",f"index-{i}"); fields(ds,f"decision:{xid}",x,("recommendation","issue_options","evidence_source_ids","target_output_ids","review_gaps","decision_owner_role","needed_by","human_state")); refs(ds,f"decision:{xid}:source",x.get("evidence_source_ids",[]),sids); rr=x.get("target_output_ids",{}); refs(ds,f"decision:{xid}:target",rr.get("target_ids",[]),tids); refs(ds,f"decision:{xid}:output",rr.get("output_ids",[]),oids)
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
 if rev.get("FINAL_HUMAN_FORECAST_DECISION")!="PENDING": ds.add("review:FINAL_HUMAN_FORECAST_DECISION:must_be_pending")
 for x in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS): ds.add(f"forbidden_flag:{x}")
 states=set(d.get("forbidden_states",[])); states.add(d.get("operational_state","DRAFT"))
 for x in sorted(states&FORBIDDEN_STATES): ds.add(f"forbidden_state:{x}")
 ready=not ds and not gaps
 return {"skill":"forecast-dashboard","state":"READY_FOR_HUMAN_FORECAST_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"target_contracts":len(targets),"forecast_designs":len(designs),"model_candidates":len(models),"backtests":len(backtests),"scenarios":len(scenarios),"forecast_outputs":len(outputs),"reconciliations":len(recs),"dashboard_views":len(dashboards),"monitoring":len(monitoring),"action_options":len(actions),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in GATE_TESTS),"reviews_passed":sum(rev.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 target/source/vintage truth, leakage absence, model assumptions, out-of-sample accuracy, interval calibration, scenario validity, hierarchy coherence, dashboard usability, production release/action authority, legal compliance, false-trigger rate, token cost or duration."}

def main():
 if len(sys.argv)!=2: print("usage: evaluate_forecast_dashboard.py INPUT.json",file=sys.stderr); return 2
 result=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))); print(json.dumps(result,ensure_ascii=False,indent=2)); return 0 if result["state"]!="NOT_READY" else 1
if __name__=="__main__": raise SystemExit(main())

