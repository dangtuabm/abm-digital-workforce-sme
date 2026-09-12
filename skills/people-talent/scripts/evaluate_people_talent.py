#!/usr/bin/env python3
import json,sys
from pathlib import Path
TESTS={"mandate_sources","job_relatedness_evidence","people_lifecycle_cases","competency_performance_context","succession_retention","fairness_privacy_due_process","decision_boundary"}
REVIEWS={"PEOPLE_TALENT_OWNER","WORKFORCE_DOMAIN_MANAGER","EMPLOYEE_CANDIDATE_EXPERIENCE","LEGAL_LABOR_FAIRNESS","DATA_PRIVACY_SECURITY","INTERNAL_CONTROL_AUDIT"}
RISK_TYPES={"JOB_RELATEDNESS_VALIDITY","DISCRIMINATION_FAIRNESS","PRIVACY_CONFIDENTIALITY_SECURITY","DECISION_AUTHORITY_DUE_PROCESS","PERFORMANCE_DEVELOPMENT_WELLBEING","SUCCESSION_RETENTION_CONTINUITY"}
SECTIONS={"document_control","source_job_evidence_ledger","people_lifecycle_cases","competency_development","performance_succession_retention","fairness_privacy_controls","risks_decisions_reviews","audit_change_log"}
RIGHTS={"AUTHORIZED","INTERNAL_AUTHORIZED","OWNER_AUTHORIZED","POLICY_AUTHORIZED","SYSTEM_AUTHORIZED","CONSENTED","FAIRNESS_AUDIT_AUTHORIZED"}
STAGES={"JOB_DESIGN","RECRUITMENT","ONBOARDING","PERFORMANCE","DEVELOPMENT","SUCCESSION","RETENTION_OFFBOARDING"}
RECOMMENDATIONS={"JOB_REVIEW","ASSESSMENT_REVIEW","ONBOARDING_REVIEW","PERFORMANCE_REVIEW","DEVELOPMENT_REVIEW","SUCCESSION_REVIEW","RETENTION_REVIEW","REVISE","HOLD","INVESTIGATE_REVIEW"}
FORBIDDEN_FLAGS={"protected_trait_inferred","health_inferred","pregnancy_inferred","disability_inferred","religion_inferred","ethnicity_inferred","sexual_orientation_inferred","union_status_inferred","political_view_inferred","biometric_used","face_emotion_scored","voice_emotion_scored","personality_diagnosed","mental_health_diagnosed","candidate_fabricated","employee_fabricated","credential_fabricated","performance_fabricated","skill_fabricated","experience_fabricated","reference_fabricated","salary_fabricated","source_fabricated","consent_fabricated","protected_data_in_decision","proxy_feature_used","job_requirement_unrelated","requirement_fabricated","inaccessible_assessment","accommodation_denied","candidate_deceived","employee_surveillance_hidden","secret_scoring","model_version_hidden","threshold_fabricated","ranking_fabricated","cohort_denominator_hidden","subgroup_suppressed","sample_too_small_exposed","missingness_hidden","adverse_impact_hidden","fairness_test_bypassed","validity_claim_fabricated","score_called_truth","activity_called_performance","outcome_without_context","opportunity_ignored","manager_opinion_called_fact","rating_fabricated","feedback_fabricated","appeal_bypassed","correction_bypassed","due_process_bypassed","training_forced","successor_declared","attrition_prediction_called_fact","individual_attrition_used_for_adverse_action","retaliation_risk_hidden","confidential_data_exposed","credential_exposed","pii_exposed","salary_data_exposed","public_llm_unapproved","retention_bypassed","deletion_bypassed","access_bypassed","review_bypassed","auto_job_published","auto_candidate_sourced","auto_candidate_contacted","auto_candidate_shortlisted","auto_candidate_rejected","auto_candidate_hired","auto_offer_sent","auto_compensation_set","auto_rating_finalized","auto_promotion_decided","auto_demotion_decided","auto_discipline_decided","auto_termination_decided","auto_training_enrolled","auto_successor_named","auto_employee_record_changed","auto_access_changed","auto_government_filed","auto_decision_communicated"}
FORBIDDEN_STATES={"JOB_PUBLISHED","CANDIDATE_CONTACTED","CANDIDATE_SHORTLISTED","CANDIDATE_REJECTED","CANDIDATE_HIRED","OFFER_SENT","COMPENSATION_SET","PERFORMANCE_RATING_FINALIZED","PROMOTION_DECIDED","DEMOTION_DECIDED","DISCIPLINE_DECIDED","TERMINATION_DECIDED","TRAINING_ENROLLED","SUCCESSOR_NAMED","EMPLOYEE_RECORD_CHANGED","ACCESS_CHANGED","GOVERNMENT_FILED","EXTERNAL_DECISION_COMMUNICATED"}
def ok(v):return v not in(None,"",[],{})
def fields(ds,p,obj,req):
 for f in req:
  if not ok(obj.get(f)):ds.add(f"{p}:missing_{f}")
def refs(ds,p,vals,known):
 for x in vals:
  if x not in known:ds.add(f"{p}:unknown_ref:{x}")
def evaluate(d):
 ds=set();gaps=set();m=d.get("mandate",{})
 fields(ds,"mandate",m,("use_case_stage_purpose_decision_audience","entity_jurisdiction_population","as_of_horizon","owner_decision_authority","lawful_basis_notice_consent","reviews","appeal_correction_accommodation","data_access_retention_deletion","non_goals"))
 sources=d.get("sources",[]);sids=set()
 for i,x in enumerate(sources):
  xid=x.get("id",f"index-{i}");sids.add(xid);fields(ds,f"source:{xid}",x,("source_type","locator","version_as_of","rights_purpose","retention_access","confidence","system_of_record","supports"))
  if x.get("rights_purpose") not in RIGHTS:ds.add(f"source:{xid}:not_authorized")
 if len(sids)!=len(sources):ds.add("sources:duplicate_id")
 jobs=d.get("job_profiles",[]);jids=set()
 for i,x in enumerate(jobs):
  xid=x.get("id",f"index-{i}");jids.add(xid);fields(ds,f"job:{xid}",x,("purpose_outcomes","essential_duties","requirements","competency_anchors","assessment_evidence_methods","context_resources","job_relatedness_validity","accessibility_accommodation"))
 if len(jids)!=len(jobs):ds.add("jobs:duplicate_id")
 people=d.get("people_records",[]);pids=set()
 for i,x in enumerate(people):
  xid=x.get("id",f"index-{i}");pids.add(xid);fields(ds,f"person:{xid}",x,("pseudonymous_id","job_id","lifecycle_stage","eligibility_evidence_ids","opportunity_context","accommodation_state","correction_appeal_state","sensitive_data_segregation"));refs(ds,f"person:{xid}:job",[x.get("job_id")],jids)
 if len(pids)!=len(people):ds.add("people:duplicate_id")
 evidence=d.get("evidence_items",[]);eids=set()
 for i,x in enumerate(evidence):
  xid=x.get("id",f"index-{i}");eids.add(xid);fields(ds,f"evidence:{xid}",x,("source_ids","person_id","job_id","evidence_type","period_context","claim_result","confidence_limitations","correction_reviewer"));refs(ds,f"evidence:{xid}:source",x.get("source_ids",[]),sids);refs(ds,f"evidence:{xid}:person",[x.get("person_id")],pids);refs(ds,f"evidence:{xid}:job",[x.get("job_id")],jids)
 competencies=d.get("competency_items",[])
 for i,x in enumerate(competencies):
  xid=x.get("id",f"index-{i}");fields(ds,f"competency:{xid}",x,("job_id","anchor_proficiency","required_current_evidence_ids","gap_confidence_opportunity","development_option_consent","success_reassessment"));refs(ds,f"competency:{xid}:job",[x.get("job_id")],jids);refs(ds,f"competency:{xid}:evidence",x.get("required_current_evidence_ids",[]),eids)
 development=d.get("development_plans",[])
 for i,x in enumerate(development):
  xid=x.get("id",f"index-{i}");fields(ds,f"development:{xid}",x,("person_id","gap_evidence_ids","option_access","consent_authority","success_measure","reassessment_owner","human_state"));refs(ds,f"development:{xid}:person",[x.get("person_id")],pids);refs(ds,f"development:{xid}:evidence",x.get("gap_evidence_ids",[]),eids)
  if x.get("human_state")!="PENDING":ds.add(f"development:{xid}:human_state_not_pending")
 cases=d.get("lifecycle_cases",[]);seenst=set()
 for i,x in enumerate(cases):
  xid=x.get("id",f"index-{i}");st=x.get("stage");seenst.add(st);fields(ds,f"case:{xid}",x,("stage","job_person_ids","criteria_evidence_ids","context_alternatives","options","owner_role","human_state"));refs(ds,f"case:{xid}:evidence",x.get("criteria_evidence_ids",[]),eids)
  if st not in STAGES:ds.add(f"case:{xid}:invalid_stage")
  if x.get("human_state")!="PENDING":ds.add(f"case:{xid}:human_state_not_pending")
 for st in STAGES-seenst:ds.add(f"cases:missing_stage:{st}")
 fairness=d.get("fairness_checks",[])
 for i,x in enumerate(fairness):
  xid=x.get("id",f"index-{i}");fields(ds,f"fairness:{xid}",x,("tool_model_version","intended_use_population","job_relatedness_validity","accessibility_accommodation","cohort_denominator_sample_missingness","result_uncertainty","alternative_remediation_owner","protected_data_handling"))
 controls=d.get("controls",[])
 for i,x in enumerate(controls):
  xid=x.get("id",f"index-{i}");fields(ds,f"control:{xid}",x,("objective_type","owner_role","event_frequency","evidence","pass_fail","failure_action","residual_risk"))
 risks=d.get("risks",[]);seenr=set()
 for i,x in enumerate(risks):
  typ=x.get("risk_type",f"index-{i}");seenr.add(typ);fields(ds,f"risk:{typ}",x,("statement","likelihood","impact","trigger","mitigation","contingency","owner_role"))
 for typ in RISK_TYPES-seenr:ds.add(f"risks:missing_type:{typ}")
 decisions=d.get("decision_queue",[])
 for i,x in enumerate(decisions):
  xid=x.get("id",f"index-{i}");fields(ds,f"decision:{xid}",x,("recommendation","alternatives","evidence_source_ids","review_gaps","decision_owner_role","needed_by","human_state"))
  if x.get("recommendation") not in RECOMMENDATIONS:ds.add(f"decision:{xid}:invalid_recommendation")
  refs(ds,f"decision:{xid}:source",x.get("evidence_source_ids",[]),sids)
  if x.get("human_state")!="PENDING":ds.add(f"decision:{xid}:human_state_not_pending")
 missing=SECTIONS-set(d.get("output_sections",[]))
 if missing:ds.add("output_sections:missing:"+",".join(sorted(missing)))
 tests=d.get("tests",{})
 for x in TESTS:
  if tests.get(x)!="PASS":ds.add(f"test:{x}:not_pass")
 rev=d.get("reviews",{})
 for x in REVIEWS:
  if rev.get(x)!="PASS":gaps.add(f"review:{x}:not_pass")
 if rev.get("FINAL_HUMAN_PEOPLE_TALENT_DECISION")!="PENDING":ds.add("review:FINAL_HUMAN_PEOPLE_TALENT_DECISION:must_be_pending")
 for x in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS):ds.add(f"forbidden_flag:{x}")
 states=set(d.get("forbidden_states",[]));states.add(d.get("operational_state","DRAFT"))
 for x in sorted(states&FORBIDDEN_STATES):ds.add(f"forbidden_state:{x}")
 ready=not ds and not gaps
 return {"skill":"people-talent","state":"READY_FOR_HUMAN_PEOPLE_TALENT_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"job_profiles":len(jobs),"people_records":len(people),"evidence_items":len(evidence),"competency_items":len(competencies),"development_plans":len(development),"lifecycle_cases":len(cases),"fairness_checks":len(fairness),"controls":len(controls),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(rev.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 job truth, assessment validity, legal compliance, fairness, employee/candidate experience, decision quality, authorization, token cost or duration."}
def main():
 if len(sys.argv)!=2:print("usage: evaluate_people_talent.py INPUT.json",file=sys.stderr);return 2
 r=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")));print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__":raise SystemExit(main())
