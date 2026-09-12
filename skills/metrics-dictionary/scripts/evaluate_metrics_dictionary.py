#!/usr/bin/env python3
import json,sys
from pathlib import Path

GATE_TESTS={"mandate_sources_owners","metric_contract_semantics","grain_formula_denominator","dimensions_time_unit","lineage_validation_reconciliation","version_target_adoption","decision_boundary"}
REVIEWS={"BUSINESS_DOMAIN_OWNER","DATA_STEWARD_ANALYTICS","FINANCE_ACCOUNTING_OWNER","DATA_ENGINEERING_SEMANTIC_LAYER","RISK_LEGAL_COMPLIANCE","DASHBOARD_REPORTING_CONSUMER_OWNER"}
RISK_TYPES={"SEMANTIC_DEFINITION_SCOPE","GRAIN_DENOMINATOR_DOUBLE_COUNT","SOURCE_LINEAGE_DATA_QUALITY","TIME_CURRENCY_UNIT_RESTATEMENT","TARGET_THRESHOLD_GAMING","VERSION_ADOPTION_RECONCILIATION"}
SECTIONS={"document_control","metric_census_glossary","metric_contracts","dimensions_time_units","source_lineage_implementation","tests_reconciliation","targets_versions_adoption","risks_decisions_reviews_audit"}
RIGHTS={"PUBLIC_AUTHORIZED","INTERNAL_AUTHORIZED","OWNER_AUTHORIZED","STEWARD_AUTHORIZED","FINANCE_AUTHORIZED","LEGAL_AUTHORIZED","CONTRACT_AUTHORIZED","CUSTOMER_AUTHORIZED"}
METRIC_TYPES={"RAW_MEASURE","DERIVED_METRIC","KPI","LEADING","LAGGING","GUARDRAIL","TARGET","BENCHMARK","DIAGNOSTIC"}
TEST_TYPES={"CONTRACT_SCHEMA","POSITIVE","NEGATIVE","BOUNDARY_DENOMINATOR_ZERO","AGGREGATION_GRAIN","TIME_COHORT_TIMEZONE","NULL_DUPLICATE_LATE_RESTATEMENT","LINEAGE_RECONCILIATION_ACCESS"}
RECOMMENDATIONS={"MANDATE_SCOPE_REVIEW","METRIC_CONTRACT_REVIEW","FORMULA_GRAIN_REVIEW","LINEAGE_TEST_REVIEW","TARGET_AUTHORITY_REVIEW","VERSION_ADOPTION_REVIEW","RECONCILIATION_RELEASE_REVIEW","REVISE","HOLD"}
FORBIDDEN_FLAGS={
"scope_fabricated","owner_fabricated","steward_fabricated","approver_fabricated","system_of_record_fabricated","rights_fabricated","source_fabricated","locator_fabricated","snapshot_fabricated","hash_fabricated","schema_fabricated","table_fabricated","field_fabricated","event_fabricated","key_fabricated","grain_fabricated","metric_id_fabricated","metric_name_fabricated","alias_fabricated","business_question_fabricated","definition_fabricated","classification_fabricated","numerator_fabricated","denominator_fabricated","formula_fabricated","aggregation_fabricated","dimension_fabricated","hierarchy_fabricated","code_list_fabricated","filter_fabricated","inclusion_fabricated","exclusion_fabricated","cohort_fabricated","time_basis_fabricated","window_fabricated","timezone_fabricated","unit_fabricated","currency_fabricated","fx_source_fabricated","rounding_fabricated","null_rule_fabricated","zero_rule_fabricated","duplicate_rule_fabricated","late_rule_fabricated","restatement_rule_fabricated","target_fabricated","baseline_fabricated","benchmark_fabricated","status_band_fabricated","threshold_fabricated","tolerance_fabricated","sql_fabricated","query_hash_fabricated","model_hash_fabricated","lineage_fabricated","test_fabricated","fixture_fabricated","expected_fabricated","actual_fabricated","reconciliation_fabricated","delta_hidden","version_fabricated","effective_date_fabricated","sunset_date_fabricated","semantic_diff_hidden","breaking_change_hidden","dependency_hidden","consumer_hidden","adoption_fabricated","acknowledgement_fabricated","rollback_fabricated","deprecation_fabricated","actual_forecast_mixed","actual_target_mixed","missing_called_zero","average_ratio_misaggregated","distinct_count_additivity_assumed","denominator_zero_hidden","denominator_manipulated","filter_manipulated","cohort_leakage_hidden","double_count_hidden","late_data_hidden","restatement_hidden","provisional_called_final","dashboard_called_truth","conflict_suppressed","duplicate_auto_merged","metric_history_deleted","review_bypassed","finance_review_bypassed","legal_review_bypassed","source_instruction_executed","comment_instruction_executed","macro_executed","formula_executed","sql_executed","code_executed","secret_exposed","credential_exposed","pii_exposed","public_llm_unapproved","auto_metric_created","auto_metric_renamed","auto_metric_redefined","auto_formula_changed","auto_denominator_changed","auto_grain_changed","auto_filter_changed","auto_target_changed","auto_threshold_changed","auto_sor_selected","auto_owner_changed","auto_accounting_treatment_changed","auto_fx_rule_changed","auto_model_changed","auto_semantic_layer_changed","auto_dashboard_changed","auto_sql_deployed","auto_history_backfilled","auto_data_restated","auto_metric_approved","auto_metric_deprecated","auto_report_certified","auto_report_published","auto_external_sent","audit_log_mutated","evidence_altered","evidence_deleted"
}
FORBIDDEN_STATES={"METRIC_CREATED","METRIC_RENAMED","METRIC_REDEFINED","FORMULA_CHANGED","DENOMINATOR_CHANGED","GRAIN_CHANGED","FILTER_CHANGED","TARGET_CHANGED","THRESHOLD_CHANGED","SOR_SELECTED","OWNER_CHANGED","ACCOUNTING_TREATMENT_CHANGED","FX_RULE_CHANGED","MODEL_CHANGED","SEMANTIC_LAYER_CHANGED","DASHBOARD_CHANGED","SQL_DEPLOYED","HISTORY_BACKFILLED","DATA_RESTATED","METRIC_APPROVED","METRIC_DEPRECATED","REPORT_CERTIFIED","REPORT_PUBLISHED","EXTERNAL_SENT","AUDIT_LOG_MUTATED","EVIDENCE_ALTERED","EVIDENCE_DELETED"}

def ok(v): return v not in (None,"",[],{})
def fields(ds,p,obj,req):
 for f in req:
  if not ok(obj.get(f)): ds.add(f"{p}:missing_{f}")
def refs(ds,p,vals,known):
 for x in vals:
  if x not in known: ds.add(f"{p}:unknown_ref:{x}")

def evaluate(d):
 ds=set(); gaps=set(); m=d.get("mandate",{})
 fields(ds,"mandate",m,("business_decisions_use_cases","domain_entity_scope_exclusions","audience_reporting_consumers","as_of_horizon","owners_stewards_approvers_reviewers","systems_of_record","classification_access_rights","non_goals"))
 sources=d.get("sources",[]); sids=set()
 for i,x in enumerate(sources):
  xid=x.get("id",f"index-{i}"); sids.add(xid); fields(ds,f"source:{xid}",x,("locator_environment","owner_sor","schema_table_field_event","grain_keys","freshness_as_of","classification_purpose_rights","snapshot_version_hash","dependencies_consumers"))
  if x.get("classification_purpose_rights",{}).get("rights") not in RIGHTS: ds.add(f"source:{xid}:not_authorized")
 if len(sids)!=len(sources): ds.add("sources:duplicate_id")
 census=d.get("metric_census",[]); census_ids=set()
 for i,x in enumerate(census):
  xid=x.get("id",f"index-{i}"); census_ids.add(xid); fields(ds,f"census:{xid}",x,("original_name_formula","artifact_consumer_version_hash","candidate_canonical_id","alias_duplicate_conflict","semantic_difference","owner_state_evidence"))
 contracts=d.get("metric_contracts",[]); mids=set()
 for i,x in enumerate(contracts):
  xid=x.get("canonical_metric_id",f"index-{i}"); mids.add(xid); fields(ds,f"metric:{xid}",x,("canonical_name_aliases","business_question_definition","metric_type","entity_grain_event_state","numerator_denominator_formula","aggregation_behavior","dimensions_filters_inclusions_exclusions","time_window_timezone_cohort","unit_currency_fx_rounding","null_zero_duplicate_late_restatement","source_lineage_ids","owner_steward_approver","implementation_test_refs","version_effective_status","human_state")); refs(ds,f"metric:{xid}:source",x.get("source_lineage_ids",[]),sids)
  if x.get("metric_type") not in METRIC_TYPES: ds.add(f"metric:{xid}:invalid_type")
  if x.get("human_state")!="PENDING": ds.add(f"metric:{xid}:human_state_not_pending")
 if len(mids)!=len(contracts): ds.add("metrics:duplicate_canonical_id")
 dimensions=d.get("dimensions",[]); dids=set()
 for i,x in enumerate(dimensions):
  xid=x.get("id",f"index-{i}"); dids.add(xid); fields(ds,f"dimension:{xid}",x,("name_business_meaning","type_domain_code_list","hierarchy_rollup","grain_compatibility","time_validity_scd","owner_version_effective","source_ids","metric_ids")); refs(ds,f"dimension:{xid}:source",x.get("source_ids",[]),sids); refs(ds,f"dimension:{xid}:metric",x.get("metric_ids",[]),mids)
 lineage=d.get("lineage",[]); lids=set()
 for i,x in enumerate(lineage):
  xid=x.get("id",f"index-{i}"); lids.add(xid); fields(ds,f"lineage:{xid}",x,("metric_ids","source_ids","source_event_table_fields_snapshot","transform_model_query_version_hash","semantic_object","dashboard_report_api_decision","environment_as_of_freshness","rights_owner_evidence")); refs(ds,f"lineage:{xid}:metric",x.get("metric_ids",[]),mids); refs(ds,f"lineage:{xid}:source",x.get("source_ids",[]),sids)
 validations=d.get("validation_cases",[]); test_types=set()
 for i,x in enumerate(validations):
  xid=x.get("id",f"index-{i}"); typ=x.get("test_type"); test_types.add(typ); fields(ds,f"validation:{xid}",x,("test_type","metric_ids_versions","fixture_source","expected_actual","coverage_limitations","evidence_hash","owner_status")); refs(ds,f"validation:{xid}:metric",x.get("metric_ids_versions",{}).get("metric_ids",[]),mids)
 for typ in TEST_TYPES-test_types: ds.add(f"validation:missing_type:{typ}")
 reconciliations=d.get("reconciliations",[])
 for i,x in enumerate(reconciliations):
  xid=x.get("id",f"index-{i}"); fields(ds,f"reconciliation:{xid}",x,("metric_ids_versions","systems_compared","same_scope_grain_time_unit","tolerance_authority","values_delta","delta_explanation","evidence_hash","owner_status")); refs(ds,f"reconciliation:{xid}:metric",x.get("metric_ids_versions",{}).get("metric_ids",[]),mids)
 changes=d.get("change_records",[])
 for i,x in enumerate(changes):
  xid=x.get("id",f"index-{i}"); fields(ds,f"change:{xid}",x,("metric_ids_versions","old_new_semantic_diff_reason","breaking_level","dependencies_consumers","compatibility_migration","acknowledgement","rollback_deprecation_sunset","owner_human_state")); refs(ds,f"change:{xid}:metric",x.get("metric_ids_versions",{}).get("metric_ids",[]),mids)
  if x.get("owner_human_state",{}).get("human_state")!="PENDING": ds.add(f"change:{xid}:human_state_not_pending")
 adoption=d.get("adoption_bindings",[])
 for i,x in enumerate(adoption):
  xid=x.get("id",f"index-{i}"); fields(ds,f"adoption:{xid}",x,("metric_ids_versions","consumer_artifact_locator","binding_query_semantic_object","owner_acknowledgement","freshness_reconciliation","migration_rollback","state_evidence")); refs(ds,f"adoption:{xid}:metric",x.get("metric_ids_versions",{}).get("metric_ids",[]),mids)
 risks=d.get("risks",[]); seen=set()
 for i,x in enumerate(risks):
  typ=x.get("risk_type",f"index-{i}"); seen.add(typ); fields(ds,f"risk:{typ}",x,("statement","likelihood","impact","trigger","mitigation","contingency","owner_role"))
 for typ in RISK_TYPES-seen: ds.add(f"risks:missing_type:{typ}")
 decisions=d.get("decision_queue",[])
 for i,x in enumerate(decisions):
  xid=x.get("id",f"index-{i}"); fields(ds,f"decision:{xid}",x,("recommendation","issue_options","evidence_source_ids","metric_ids","review_gaps","decision_owner_role","needed_by","human_state")); refs(ds,f"decision:{xid}:source",x.get("evidence_source_ids",[]),sids); refs(ds,f"decision:{xid}:metric",x.get("metric_ids",[]),mids)
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
 if rev.get("FINAL_HUMAN_METRIC_GOVERNANCE_DECISION")!="PENDING": ds.add("review:FINAL_HUMAN_METRIC_GOVERNANCE_DECISION:must_be_pending")
 for x in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS): ds.add(f"forbidden_flag:{x}")
 states=set(d.get("forbidden_states",[])); states.add(d.get("operational_state","DRAFT"))
 for x in sorted(states&FORBIDDEN_STATES): ds.add(f"forbidden_state:{x}")
 ready=not ds and not gaps
 return {"skill":"metrics-dictionary","state":"READY_FOR_HUMAN_METRIC_GOVERNANCE_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"census_items":len(census),"metric_contracts":len(contracts),"dimensions":len(dimensions),"lineage":len(lineage),"validation_cases":len(validations),"reconciliations":len(reconciliations),"change_records":len(changes),"adoption_bindings":len(adoption),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in GATE_TESTS),"reviews_passed":sum(rev.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 business-semantic truth, source/query correctness, finance/accounting treatment, target authority, production reconciliation, consumer adoption, legal compliance, false-trigger rate, token cost or duration."}

def main():
 if len(sys.argv)!=2: print("usage: evaluate_metrics_dictionary.py INPUT.json",file=sys.stderr); return 2
 result=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))); print(json.dumps(result,ensure_ascii=False,indent=2)); return 0 if result["state"]!="NOT_READY" else 1
if __name__=="__main__": raise SystemExit(main())

