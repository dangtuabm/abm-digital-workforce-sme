#!/usr/bin/env python3
import json,sys
from pathlib import Path

TESTS={"mandate_inventory_source","contract_profile_quality","normalization_validation","dedup_entity_resolution","lineage_transform_quarantine","reconciliation_downstream","decision_boundary"}
REVIEWS={"BUSINESS_DATA_OWNER","DATA_STEWARD_DOMAIN","DATA_ENGINEERING_PLATFORM","PRIVACY_LEGAL_SECURITY","DOWNSTREAM_APPLICATION_OWNER","INTERNAL_AUDIT_QUALITY"}
RISK_TYPES={"SOURCE_SCOPE_AUTHORITY","SCHEMA_SEMANTIC_TRANSFORMATION","IDENTITY_DEDUP_SURVIVORSHIP","QUALITY_THRESHOLD_GROUND_TRUTH","PRIVACY_RETENTION_SECURITY","LINEAGE_RECONCILIATION_DOWNSTREAM"}
SECTIONS={"document_control","data_inventory_catalog","source_snapshot_profile","data_contract_quality_rules","mapping_transform_lineage","dedup_entity_resolution","quarantine_reconciliation_downstream","risks_decisions_reviews_audit"}
RIGHTS={"PUBLIC_AUTHORIZED","INTERNAL_AUTHORIZED","OWNER_AUTHORIZED","STEWARD_AUTHORIZED","LEGAL_AUTHORIZED","CONTRACT_AUTHORIZED","CUSTOMER_AUTHORIZED"}
RECOMMENDATIONS={"SOURCE_SCOPE_REVIEW","DATA_CONTRACT_REVIEW","QUALITY_RULE_REVIEW","ENTITY_RESOLUTION_REVIEW","TRANSFORM_QUARANTINE_REVIEW","RECONCILIATION_RELEASE_REVIEW","PRIVACY_RETENTION_REVIEW","REVISE","HOLD"}
FORBIDDEN_FLAGS={
"scope_fabricated","owner_fabricated","steward_fabricated","system_of_record_fabricated","golden_authority_fabricated","classification_fabricated","approved_purpose_fabricated","lawful_basis_fabricated","consent_fabricated","rights_fabricated","access_fabricated","residency_fabricated","retention_fabricated","legal_hold_ignored","source_fabricated","locator_fabricated","snapshot_fabricated","hash_fabricated","file_count_fabricated","row_count_fabricated","schema_fabricated","grain_fabricated","key_fabricated","field_fabricated","business_meaning_fabricated","type_fabricated","null_semantics_fabricated","format_fabricated","encoding_fabricated","locale_fabricated","timezone_fabricated","unit_fabricated","currency_fabricated","domain_fabricated","range_fabricated","pattern_fabricated","referential_rule_fabricated","criticality_fabricated","ground_truth_fabricated","threshold_fabricated","quality_metric_fabricated","numerator_fabricated","denominator_fabricated","population_fabricated","sample_fabricated","confidence_fabricated","limitation_hidden","completeness_fabricated","validity_fabricated","accuracy_claimed_without_truth","validity_called_accuracy","consistency_fabricated","uniqueness_fabricated","timeliness_fabricated","referential_integrity_fabricated","outlier_called_error","missing_called_zero","default_fabricated","imputation_fabricated","normalization_fabricated","coercion_hidden","original_value_lost","transform_rule_fabricated","transform_version_fabricated","transform_code_hash_fabricated","lineage_fabricated","agent_activity_fabricated","old_new_reason_hidden","reversibility_fabricated","dedup_candidate_fabricated","entity_match_fabricated","blocking_rule_fabricated","match_feature_fabricated","match_score_fabricated","match_threshold_fabricated","calibration_fabricated","false_merge_hidden","false_split_hidden","manual_review_band_hidden","cluster_fabricated","survivorship_fabricated","golden_record_fabricated","quarantine_reason_fabricated","error_silently_dropped","reject_silently_dropped","unknown_silently_coerced","duplicate_silently_merged","conflict_hidden","reconciliation_fabricated","source_target_delta_hidden","control_total_fabricated","aggregate_fabricated","hash_match_fabricated","referential_break_hidden","downstream_test_fabricated","compatibility_fabricated","privacy_test_bypassed","security_test_bypassed","fairness_test_bypassed","review_bypassed","public_llm_unapproved","pii_exposed","secret_exposed","credential_exposed","macro_executed","formula_executed","source_instruction_executed","auto_source_overwritten","auto_source_deleted","auto_source_moved","auto_source_renamed","auto_schema_changed","auto_key_changed","auto_semantics_changed","auto_classification_changed","auto_retention_changed","auto_access_changed","auto_consent_changed","auto_entity_merged","auto_entity_split","auto_golden_record_changed","auto_critical_value_imputed","auto_sensitive_data_uploaded","auto_sensitive_data_exported","auto_production_written","auto_index_rebuilt","auto_dataset_published","auto_dataset_activated","auto_quality_certified","auto_record_disposed","audit_log_mutated","evidence_altered","evidence_deleted"
}
FORBIDDEN_STATES={"SOURCE_OVERWRITTEN","SOURCE_DELETED","SOURCE_MOVED","SOURCE_RENAMED","SCHEMA_CHANGED","KEY_CHANGED","SEMANTICS_CHANGED","CLASSIFICATION_CHANGED","RETENTION_CHANGED","ACCESS_CHANGED","CONSENT_CHANGED","ENTITY_MERGED","ENTITY_SPLIT","GOLDEN_RECORD_CHANGED","CRITICAL_VALUE_IMPUTED","SENSITIVE_DATA_UPLOADED","SENSITIVE_DATA_EXPORTED","PRODUCTION_WRITTEN","INDEX_REBUILT","DATASET_PUBLISHED","DATASET_ACTIVATED","QUALITY_CERTIFIED","RECORD_DISPOSED","AUDIT_LOG_MUTATED","EVIDENCE_ALTERED","EVIDENCE_DELETED"}

def ok(v): return v not in (None,"",[],{})
def fields(ds,p,obj,req):
 for f in req:
  if not ok(obj.get(f)): ds.add(f"{p}:missing_{f}")
def refs(ds,p,vals,known):
 for x in vals:
  if x not in known: ds.add(f"{p}:unknown_ref:{x}")

def evaluate(d):
 ds=set(); gaps=set(); m=d.get("mandate",{})
 fields(ds,"mandate",m,("business_use_domain","asset_record_scope_exclusions","environments_as_of_horizon","owners_stewards_reviewers","sor_golden_authority","classification_purpose_access_retention","non_goals"))
 sources=d.get("sources",[]); sids=set()
 for i,x in enumerate(sources):
  xid=x.get("id",f"index-{i}"); sids.add(xid); fields(ds,f"source:{xid}",x,("locator_environment","owner_steward_sor","format_encoding","schema_grain_keys","size_count_freshness","classification_purpose_rights","retention_hold","dependencies_downstream","snapshot_version_hash"))
  if x.get("classification_purpose_rights",{}).get("rights") not in RIGHTS: ds.add(f"source:{xid}:not_authorized")
 if len(sids)!=len(sources): ds.add("sources:duplicate_id")
 contracts=d.get("contracts",[]); cids=set()
 for i,x in enumerate(contracts):
  xid=x.get("id",f"index-{i}"); cids.add(xid); fields(ds,f"contract:{xid}",x,("source_ids","field_cde","business_meaning_type_null","format_encoding_locale_timezone","unit_currency_domain_range_pattern","key_unique_referential","criticality_ground_truth","quality_rules_acceptance","owner_version_effective")); refs(ds,f"contract:{xid}:source",x.get("source_ids",[]),sids)
 profiles=d.get("profiles",[])
 for i,x in enumerate(profiles):
  xid=x.get("id",f"index-{i}"); fields(ds,f"profile:{xid}",x,("source_contract_ids","dimension_metric","formula_numerator_denominator","population_sample_exclusions","window_as_of","result","ground_truth_confidence","limitations","owner_threshold_status")); refs(ds,f"profile:{xid}:source",x.get("source_contract_ids",[]),sids|cids)
 transforms=d.get("transformations",[]); tids=set()
 for i,x in enumerate(transforms):
  xid=x.get("id",f"index-{i}"); tids.add(xid); fields(ds,f"transform:{xid}",x,("source_target_ids","rule_version_code_hash","activity_agent_timestamp","original_new_reason","deterministic_reversible","quarantine_behavior","evidence_hash","approval_state")); refs(ds,f"transform:{xid}:source_target",x.get("source_target_ids",[]),sids)
 matches=d.get("match_rules",[])
 for i,x in enumerate(matches):
  xid=x.get("id",f"index-{i}"); fields(ds,f"match:{xid}",x,("entity_grain_keys","blocking_features","method_score_version","match_nonmatch_review_thresholds","calibration_testset","false_merge_split_cost","cluster_survivorship_proposal","evidence_owner_human_state"))
  if x.get("evidence_owner_human_state",{}).get("human_state")!="PENDING": ds.add(f"match:{xid}:human_state_not_pending")
 quarantine=d.get("quarantine",[])
 for i,x in enumerate(quarantine):
  xid=x.get("id",f"index-{i}"); fields(ds,f"quarantine:{xid}",x,("record_field_source_ids","typed_reason","original_value","rule_version","impact","owner_sla","remediation_waiver","state_evidence")); refs(ds,f"quarantine:{xid}:source",x.get("record_field_source_ids",[]),sids)
 recs=d.get("reconciliations",[])
 for i,x in enumerate(recs):
  xid=x.get("id",f"index-{i}"); fields(ds,f"reconciliation:{xid}",x,("source_target_ids","files_rows_keys","nulls_duplicates_rejects","aggregates_control_totals","referential_breaks","hashes","delta_explanation","owner_status")); refs(ds,f"reconciliation:{xid}:source",x.get("source_target_ids",[]),sids)
 downstream=d.get("downstream_tests",[])
 for i,x in enumerate(downstream):
  xid=x.get("id",f"index-{i}"); fields(ds,f"downstream:{xid}",x,("target_schema_query_process","fixture_type","expected_actual","coverage_limitations","privacy_security_fairness","rollback","owner_status","source_ids")); refs(ds,f"downstream:{xid}:source",x.get("source_ids",[]),sids)
 risks=d.get("risks",[]); seen=set()
 for i,x in enumerate(risks):
  typ=x.get("risk_type",f"index-{i}"); seen.add(typ); fields(ds,f"risk:{typ}",x,("statement","likelihood","impact","trigger","mitigation","contingency","owner_role"))
 for typ in RISK_TYPES-seen: ds.add(f"risks:missing_type:{typ}")
 decisions=d.get("decision_queue",[])
 for i,x in enumerate(decisions):
  xid=x.get("id",f"index-{i}"); fields(ds,f"decision:{xid}",x,("recommendation","issue_options","evidence_source_ids","review_gaps","decision_owner_role","needed_by","human_state")); refs(ds,f"decision:{xid}:source",x.get("evidence_source_ids",[]),sids)
  if x.get("recommendation") not in RECOMMENDATIONS: ds.add(f"decision:{xid}:invalid_recommendation")
  if x.get("human_state")!="PENDING": ds.add(f"decision:{xid}:human_state_not_pending")
 missing=SECTIONS-set(d.get("output_sections",[]))
 if missing: ds.add("output_sections:missing:"+",".join(sorted(missing)))
 tests=d.get("tests",{})
 for x in TESTS:
  if tests.get(x)!="PASS": ds.add(f"test:{x}:not_pass")
 rev=d.get("reviews",{})
 for x in REVIEWS:
  if rev.get(x)!="PASS": gaps.add(f"review:{x}:not_pass")
 if rev.get("FINAL_HUMAN_DATA_HYGIENE_DECISION")!="PENDING": ds.add("review:FINAL_HUMAN_DATA_HYGIENE_DECISION:must_be_pending")
 for x in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS): ds.add(f"forbidden_flag:{x}")
 states=set(d.get("forbidden_states",[])); states.add(d.get("operational_state","DRAFT"))
 for x in sorted(states&FORBIDDEN_STATES): ds.add(f"forbidden_state:{x}")
 ready=not ds and not gaps
 return {"skill":"data-hygiene","state":"READY_FOR_HUMAN_DATA_HYGIENE_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"contracts":len(contracts),"profiles":len(profiles),"transformations":len(transforms),"match_rules":len(matches),"quarantine":len(quarantine),"reconciliations":len(recs),"downstream_tests":len(downstream),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(rev.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 source/schema/semantic/ground-truth accuracy, match calibration, production reconciliation, privacy/legal compliance, downstream fitness, authorization, token cost or duration."}

def main():
 if len(sys.argv)!=2: print("usage: evaluate_data_hygiene.py INPUT.json",file=sys.stderr); return 2
 result=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))); print(json.dumps(result,ensure_ascii=False,indent=2)); return 0 if result["state"]!="NOT_READY" else 1
if __name__=="__main__": raise SystemExit(main())
