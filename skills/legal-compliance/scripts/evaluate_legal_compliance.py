#!/usr/bin/env python3
import json,sys
from pathlib import Path

TESTS={"mandate_authority_sources","applicability_obligation_trace","control_evidence_testing","change_monitoring_transition","exceptions_incidents_remediation","privacy_privilege_security","decision_boundary"}
REVIEWS={"BUSINESS_PROCESS_OWNER","LEGAL_COUNSEL","COMPLIANCE_RISK_OWNER","DATA_PRIVACY_SECURITY","INTERNAL_AUDIT_ASSURANCE","REGULATORY_REPORTING_AUTHORITY"}
RISK_TYPES={"SOURCE_APPLICABILITY_INTERPRETATION","OBLIGATION_DEADLINE_REPORTING","CONTROL_DESIGN_OPERATING_EFFECTIVENESS","EVIDENCE_PRIVILEGE_RECORDS","REGULATORY_CHANGE_LICENSE_CONTINUITY","BREACH_REMEDIATION_ENFORCEMENT_REPUTATION"}
SECTIONS={"document_control","source_legal_register","applicability_obligation_matrix","control_evidence_test","exceptions_incidents_remediation","change_monitoring_transition","risks_decisions_reviews","audit_change_log"}
RIGHTS={"PUBLIC_OFFICIAL","INTERNAL_AUTHORIZED","LEGAL_AUTHORIZED","COMPLIANCE_AUTHORIZED","POLICY_AUTHORIZED","CONTRACT_AUTHORIZED","REGULATOR_AUTHORIZED"}
BINDING={"BINDING_CONFIRMED","BINDING_PENDING_COUNSEL","NON_BINDING_GUIDANCE","VOLUNTARY_STANDARD","INTERNAL_POLICY","CONTRACTUAL","UNKNOWN"}
APP_STATES={"APPLICABLE_CONFIRMED","APPLICABLE_PENDING_COUNSEL","PARTIALLY_APPLICABLE","NOT_APPLICABLE_CONFIRMED","UNKNOWN"}
CONTROL_TYPES={"PREVENTIVE","DETECTIVE","CORRECTIVE","COMBINATION"}
RECOMMENDATIONS={"LEGAL_INTERPRETATION_REVIEW","APPLICABILITY_REVIEW","CONTROL_GAP_REVIEW","INCIDENT_REPORTING_REVIEW","REGULATORY_CHANGE_REVIEW","REMEDIATION_REVIEW","ASSURANCE_REVIEW","REVISE","HOLD"}
FORBIDDEN_FLAGS={
"entity_fabricated","activity_fabricated","jurisdiction_fabricated","geography_fabricated","as_of_fabricated","legal_source_fabricated","legal_citation_fabricated","issuer_fabricated","instrument_fabricated","version_fabricated","publication_date_fabricated","effective_date_fabricated","status_date_fabricated","supersession_hidden","amendment_hidden","translation_claimed_falsely","binding_status_fabricated","guidance_treated_as_law","standard_treated_as_law","policy_treated_as_law","contract_treated_as_law","source_conflict_hidden","source_stale_hidden","applicability_fabricated","subject_fabricated","territorial_scope_fabricated","material_scope_fabricated","temporal_scope_fabricated","trigger_fabricated","threshold_fabricated","exemption_fabricated","exception_fabricated","interpretation_fabricated","counsel_bypassed","obligation_fabricated","prohibition_fabricated","actor_fabricated","deadline_fabricated","frequency_fabricated","retention_fabricated","penalty_fabricated","consequence_fabricated","reporting_trigger_fabricated","reporting_deadline_hidden","license_fabricated","permit_fabricated","regulator_fabricated","process_fabricated","owner_fabricated","authority_fabricated","raci_fabricated","sod_conflict_hidden","system_record_fabricated","control_fabricated","control_objective_fabricated","control_frequency_fabricated","population_fabricated","performer_fabricated","reviewer_fabricated","fallback_fabricated","control_gap_hidden","design_called_effective","operation_called_effective_without_test","evidence_fabricated","evidence_sufficiency_claimed","evidence_integrity_fabricated","evidence_custody_broken","evidence_altered","evidence_deleted","evidence_falsified","audit_log_mutated","sample_fabricated","sample_extrapolated","test_result_fabricated","deviation_hidden","limitation_hidden","reperformance_claimed_falsely","exception_hidden","incident_hidden","allegation_called_fact","breach_claimed_without_authority","root_cause_claimed_without_evidence","regulatory_change_hidden","transition_deadline_hidden","interim_control_fabricated","remediation_fabricated","remediation_approved_without_authority","remediation_executed_without_authority","closure_claimed_without_evidence","issue_closed_without_authority","compliance_certified","non_compliance_certified","legal_opinion_issued","legal_advice_issued","privilege_claimed_falsely","privilege_waived","confidential_data_exposed","reporter_identity_exposed","pii_exposed","credential_exposed","public_llm_unapproved","review_bypassed","auto_regulator_contacted","auto_authority_contacted","auto_third_party_contacted","auto_report_filed","auto_self_reported","auto_license_applied","auto_permit_applied","auto_registration_completed","auto_admission_made","auto_penalty_accepted","auto_investigation_started","auto_person_interviewed","auto_discipline_applied","auto_policy_changed","auto_control_changed","auto_access_changed","auto_system_changed","auto_remediation_executed","retaliation_enabled","evasion_advised","record_duty_bypassed"
}
FORBIDDEN_STATES={"COMPLIANT_CERTIFIED","NON_COMPLIANT_CERTIFIED","LEGAL_OPINION_ISSUED","LEGAL_ADVICE_ISSUED","REPORTED","FILED","SELF_REPORTED","LICENSE_APPLIED","PERMIT_APPLIED","REGISTERED","REGULATOR_CONTACTED","AUTHORITY_CONTACTED","THIRD_PARTY_CONTACTED","BREACH_ADMITTED","LIABILITY_ADMITTED","PENALTY_ACCEPTED","INVESTIGATION_STARTED","PERSON_INTERVIEWED","DISCIPLINE_APPLIED","POLICY_CHANGED","CONTROL_CHANGED","ACCESS_CHANGED","SYSTEM_CHANGED","REMEDIATION_EXECUTED","ISSUE_CLOSED","EVIDENCE_ALTERED","EVIDENCE_DELETED","AUDIT_LOG_MUTATED","PRIVILEGE_WAIVED"}

def ok(v): return v not in (None,"",[],{})
def fields(ds,p,obj,req):
 for f in req:
  if not ok(obj.get(f)): ds.add(f"{p}:missing_{f}")
def refs(ds,p,vals,known):
 for x in vals:
  if x not in known: ds.add(f"{p}:unknown_ref:{x}")

def evaluate(d):
 ds=set(); gaps=set(); m=d.get("mandate",{})
 fields(ds,"mandate",m,("entity_group_scope","activity_product_process","purpose_intended_use","geography_jurisdiction","as_of_horizon","owners_authorities_reviews","privilege_privacy_classification","non_goals"))
 sources=d.get("sources",[]); sids=set()
 for i,x in enumerate(sources):
  xid=x.get("id",f"index-{i}"); sids.add(xid); fields(ds,f"source:{xid}",x,("instrument_type_issuer","official_locator","version_publication_effective_status_dates","jurisdiction_scope","binding_status","language_translation","rights_access","supersession_freshness","confidence_supports"))
  if x.get("rights_access") not in RIGHTS: ds.add(f"source:{xid}:not_authorized")
  if x.get("binding_status") not in BINDING: ds.add(f"source:{xid}:invalid_binding_status")
 if len(sids)!=len(sources): ds.add("sources:duplicate_id")
 apps=d.get("applicability",[]); aids=set()
 for i,x in enumerate(apps):
  xid=x.get("id",f"index-{i}"); aids.add(xid); fields(ds,f"applicability:{xid}",x,("subject_activity_product_data_transaction","territorial_material_temporal_scope","trigger_threshold","exemption_exception_ambiguity","source_ids","interpretation_owner","applicability_state","rationale_as_of")); refs(ds,f"applicability:{xid}:source",x.get("source_ids",[]),sids)
  if x.get("applicability_state") not in APP_STATES: ds.add(f"applicability:{xid}:invalid_state")
 obligations=d.get("obligations",[]); oids=set()
 for i,x in enumerate(obligations):
  xid=x.get("id",f"index-{i}"); oids.add(xid); fields(ds,f"obligation:{xid}",x,("actor_action_prohibition","trigger_frequency_deadline_threshold","exception","process_system_record","evidence_retention","owner_authority","consequence_escalation","source_pinpoint_ids","applicability_ids")); refs(ds,f"obligation:{xid}:source",x.get("source_pinpoint_ids",[]),sids); refs(ds,f"obligation:{xid}:app",x.get("applicability_ids",[]),aids)
 controls=d.get("controls",[]); cids=set()
 for i,x in enumerate(controls):
  xid=x.get("id",f"index-{i}"); cids.add(xid); fields(ds,f"control:{xid}",x,("objective_risk","control_type","frequency_population","performer_reviewer_authority","process_system_record","evidence_expected","exception_fallback","obligation_ids","design_status")); refs(ds,f"control:{xid}:obligation",x.get("obligation_ids",[]),oids)
  if x.get("control_type") not in CONTROL_TYPES: ds.add(f"control:{xid}:invalid_type")
 evid=d.get("evidence_tests",[]); eids=set()
 for i,x in enumerate(evid):
  xid=x.get("id",f"index-{i}"); eids.add(xid); fields(ds,f"evidence_test:{xid}",x,("control_ids","test_period_population","sample_method_basis","evidence_source_custody_integrity_access","result_deviation","limitation_reperformance","tester_reviewer","operation_status")); refs(ds,f"evidence_test:{xid}:control",x.get("control_ids",[]),cids)
 items=d.get("exceptions_incidents",[])
 for i,x in enumerate(items):
  xid=x.get("id",f"index-{i}"); fields(ds,f"exception_incident:{xid}",x,("fact_allegation_status","source_detected_date","affected_obligation_control_ids","impact_urgency_basis","privilege_privacy_security_route","containment_option","reporting_filing_owner_deadline","issue_owner_status")); refs(ds,f"exception_incident:{xid}:affected",x.get("affected_obligation_control_ids",[]),oids|cids)
 changes=d.get("regulatory_changes",[])
 for i,x in enumerate(changes):
  xid=x.get("id",f"index-{i}"); fields(ds,f"change:{xid}",x,("official_source_ids","detected_publication_effective_dates","applicability_impact","affected_obligation_control_ids","affected_policy_contract_training","transition_cutover_interim_control","owner_decision_needed_by","status_evidence")); refs(ds,f"change:{xid}:source",x.get("official_source_ids",[]),sids); refs(ds,f"change:{xid}:affected",x.get("affected_obligation_control_ids",[]),oids|cids)
 rems=d.get("remediations",[])
 for i,x in enumerate(rems):
  xid=x.get("id",f"index-{i}"); fields(ds,f"remediation:{xid}",x,("gap_incident_change_ref","root_cause_hypothesis","severity_urgency_basis","options_recommendation","owner_authority","dependency_needed_by","evidence_needed","success_closure_rollback","human_state"))
  if x.get("human_state")!="PENDING": ds.add(f"remediation:{xid}:human_state_not_pending")
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
 if rev.get("FINAL_HUMAN_LEGAL_COMPLIANCE_DECISION")!="PENDING": ds.add("review:FINAL_HUMAN_LEGAL_COMPLIANCE_DECISION:must_be_pending")
 for x in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS): ds.add(f"forbidden_flag:{x}")
 states=set(d.get("forbidden_states",[])); states.add(d.get("operational_state","DRAFT"))
 for x in sorted(states&FORBIDDEN_STATES): ds.add(f"forbidden_state:{x}")
 ready=not ds and not gaps
 return {"skill":"legal-compliance","state":"READY_FOR_HUMAN_LEGAL_COMPLIANCE_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"applicability":len(apps),"obligations":len(obligations),"controls":len(controls),"evidence_tests":len(evid),"exceptions_incidents":len(items),"regulatory_changes":len(changes),"remediations":len(rems),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(rev.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 legal-source completeness, applicability, legal advice, compliance, control operation, evidence sufficiency, regulator acceptance, remediation outcome, authorization, token cost or duration."}

def main():
 if len(sys.argv)!=2: print("usage: evaluate_legal_compliance.py INPUT.json",file=sys.stderr); return 2
 result=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))); print(json.dumps(result,ensure_ascii=False,indent=2)); return 0 if result["state"]!="NOT_READY" else 1
if __name__=="__main__": raise SystemExit(main())
