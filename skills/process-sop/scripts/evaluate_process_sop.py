#!/usr/bin/env python3
import json,sys
from pathlib import Path
TESTS={"mandate_sources","process_boundary_sipoc","steps_roles_sod","controls_exceptions","metrics_sla_records","forms_uat_change","decision_boundary"}
REVIEWS={"PROCESS_OWNER","OPERATIONS_USER","RISK_COMPLIANCE","DATA_SECURITY_PRIVACY","QUALITY_CONTINUITY","DOCUMENT_CONTROL_TRAINING"}
RISK_TYPES={"PROCESS_OUTCOME_SCOPE","ROLE_AUTHORITY_SOD","CONTROL_COMPLIANCE","DATA_SECURITY_PRIVACY_RECORDS","QUALITY_CAPACITY_CONTINUITY","DOCUMENT_ADOPTION_CHANGE"}
SECTIONS={"document_control","source_boundary_flow","roles_authority_sod","executable_steps","exceptions_controls_metrics","assets_uat_adoption","risks_decisions_change","audit_log"}
RIGHTS={"AUTHORIZED","INTERNAL_AUTHORIZED","OWNER_AUTHORIZED","POLICY_AUTHORIZED","SYSTEM_AUTHORIZED","RESEARCH_CONSENTED"}
RECOMMENDATIONS={"ACTIVATE_REVIEW","PILOT_REVIEW","REVISE","HOLD","RETIRE_REVIEW"}
FORBIDDEN_FLAGS={"process_fabricated","step_fabricated","role_fabricated","authority_fabricated","sla_fabricated","kpi_fabricated","target_fabricated","control_fabricated","record_fabricated","exception_fabricated","source_fabricated","policy_fabricated","system_state_fabricated","tribal_knowledge_called_fact","current_target_mixed","broken_process_automated","control_removed_for_speed","sod_bypassed","incompatible_duties_combined","access_assumed","named_person_dependency","approval_self_assigned","unsafe_shortcut","exception_hidden","deviation_hidden","escalation_bypassed","critical_control_averaged","control_evidence_missing","acceptance_missing","output_missing","record_missing","dependency_hidden","handoff_hidden","continuity_ignored","manual_fallback_missing","metric_denominator_hidden","cohort_mixed","window_mixed","activity_called_outcome","speed_called_quality","policy_copied_without_rights","restricted_content_exposed","credential_exposed","pii_exposed","retention_bypassed","privacy_bypassed","security_bypassed","uat_bypassed","exception_test_bypassed","failed_test_called_pass","walkthrough_called_effective","training_fabricated","competence_fabricated","adoption_fabricated","review_bypassed","version_overwritten","effective_date_fabricated","rollback_missing","old_version_uncontrolled","auto_sop_published","auto_sop_activated","auto_workflow_changed","auto_system_changed","auto_permission_changed","auto_task_executed","auto_record_mutated","auto_policy_approved","auto_training_certified","auto_old_version_retired"}
FORBIDDEN_STATES={"SOP_PUBLISHED","SOP_ACTIVATED","WORKFLOW_CHANGED","SYSTEM_CHANGED","PERMISSION_CHANGED","TASK_EXECUTED","RECORD_MUTATED","POLICY_APPROVED","TRAINING_CERTIFIED","OLD_VERSION_RETIRED"}
def ok(v):return v not in(None,"",[],{})
def fields(ds,p,obj,req):
 for f in req:
  if not ok(obj.get(f)):ds.add(f"{p}:missing_{f}")
def refs(ds,p,vals,known):
 for x in vals:
  if x not in known:ds.add(f"{p}:unknown_ref:{x}")
def evaluate(d):
 ds=set();gaps=set();m=d.get("mandate",{})
 fields(ds,"mandate",m,("objective_outcome","process_document_type","audience","trigger_start_end","scope_volume_criticality","as_of_horizon","owner","approver","activation_authority","required_reviews"))
 sources=d.get("sources",[]);sids=set()
 for i,x in enumerate(sources):
  xid=x.get("id",f"index-{i}");sids.add(xid)
  fields(ds,f"source:{xid}",x,("source_type","locator","version","date","rights_purpose","freshness","confidence","supports"))
  if x.get("rights_purpose") not in RIGHTS:ds.add(f"source:{xid}:not_authorized")
 if len(sids)!=len(sources):ds.add("sources:duplicate_id")
 boundary=d.get("process_boundary",{})
 fields(ds,"boundary",boundary,("suppliers","inputs_preconditions","trigger","current_stages","target_stages","outputs_acceptance","customers","upstream_downstream_interfaces","system_of_record","current_target_gaps","non_goals"))
 roles=d.get("roles",[]);rids=set()
 for i,x in enumerate(roles):
  xid=x.get("id",f"index-{i}");rids.add(xid)
  fields(ds,f"role:{xid}",x,("accountability_tasks","decision_approval_authority","competence_access","backup_handoff","sod_conflicts_controls"))
 if len(rids)!=len(roles):ds.add("roles:duplicate_id")
 steps=d.get("process_steps",[]);stepids=set()
 for i,x in enumerate(steps):
  xid=x.get("id",f"index-{i}");stepids.add(xid)
  fields(ds,f"step:{xid}",x,("trigger_input","performer_roles","accountable_role","action_decision_rule","output_acceptance","sla_basis","system_record_evidence","control_ids","dependencies","next_state"))
  refs(ds,f"step:{xid}:performer",x.get("performer_roles",[]),rids);refs(ds,f"step:{xid}:accountable",[x.get("accountable_role")],rids)
 if len(stepids)!=len(steps):ds.add("steps:duplicate_id")
 exceptions=d.get("exceptions",[]);exids=set()
 for i,x in enumerate(exceptions):
  xid=x.get("id",f"index-{i}");exids.add(xid)
  fields(ds,f"exception:{xid}",x,("condition_detection","containment_allowed_deviation","escalation_threshold_route_sla","decision_authority_role","evidence","recovery_rollback","closure"))
  refs(ds,f"exception:{xid}",[x.get("decision_authority_role")],rids)
 controls=d.get("controls",[]);cids=set()
 for i,x in enumerate(controls):
  xid=x.get("id",f"index-{i}");cids.add(xid)
  fields(ds,f"control:{xid}",x,("objective_type","owner_role","event_frequency","evidence","pass_fail","failure_action","residual_risk"))
  refs(ds,f"control:{xid}",[x.get("owner_role")],rids)
 for x in steps:
  refs(ds,f"step:{x.get('id','unknown')}:control",x.get("control_ids",[]),cids)
 metrics=d.get("metrics",[]);mids=set()
 for i,x in enumerate(metrics):
  xid=x.get("id",f"index-{i}");mids.add(xid)
  fields(ds,f"metric:{xid}",x,("purpose_formula_grain","denominator_cohort_window","source_freshness","target_sla_basis","owner_role","action"))
  refs(ds,f"metric:{xid}",[x.get("owner_role")],rids)
 assets=d.get("assets",[]);aids=set()
 for i,x in enumerate(assets):
  xid=x.get("id",f"index-{i}");aids.add(xid)
  fields(ds,f"asset:{xid}",x,("asset_type_purpose","step_ids","version_access_retention","record_fields_or_content","completion_evidence","owner_role"))
  refs(ds,f"asset:{xid}:step",x.get("step_ids",[]),stepids);refs(ds,f"asset:{xid}:owner",[x.get("owner_role")],rids)
 testsuites=d.get("uat_cases",[])
 for i,x in enumerate(testsuites):
  xid=x.get("id",f"index-{i}")
  fields(ds,f"uat:{xid}",x,("case_type","preconditions_action","expected_result_evidence","related_step_exception_control_ids","defect_retest_state","test_owner_role"))
  refs(ds,f"uat:{xid}:owner",[x.get("test_owner_role")],rids)
 adoption=d.get("adoption_change",{})
 fields(ds,"adoption_change",adoption,("walkthrough_training_competence","adoption_feedback","version_hash_effective_date_proposal","change_communication","rollback","old_version_treatment","change_authority","record_source"))
 risks=d.get("risks",[]);seenr=set()
 for i,x in enumerate(risks):
  typ=x.get("risk_type",f"index-{i}");seenr.add(typ)
  fields(ds,f"risk:{typ}",x,("statement","likelihood","impact","trigger","mitigation","contingency","owner_role"));refs(ds,f"risk:{typ}",[x.get("owner_role")],rids)
 for typ in RISK_TYPES-seenr:ds.add(f"risks:missing_type:{typ}")
 decisions=d.get("decision_queue",[])
 for i,x in enumerate(decisions):
  xid=x.get("id",f"index-{i}")
  fields(ds,f"decision:{xid}",x,("recommendation","alternatives","evidence_source_ids","review_gaps","decision_owner_role","needed_by","human_state"))
  if x.get("recommendation") not in RECOMMENDATIONS:ds.add(f"decision:{xid}:invalid_recommendation")
  refs(ds,f"decision:{xid}:source",x.get("evidence_source_ids",[]),sids);refs(ds,f"decision:{xid}:owner",[x.get("decision_owner_role")],rids)
  if x.get("human_state")!="PENDING":ds.add(f"decision:{xid}:human_state_not_pending")
 missing=SECTIONS-set(d.get("output_sections",[]))
 if missing:ds.add("output_sections:missing:"+",".join(sorted(missing)))
 tests=d.get("tests",{})
 for x in TESTS:
  if tests.get(x)!="PASS":ds.add(f"test:{x}:not_pass")
 rev=d.get("reviews",{})
 for x in REVIEWS:
  if rev.get(x)!="PASS":gaps.add(f"review:{x}:not_pass")
 if rev.get("FINAL_HUMAN_SOP_ACTIVATION")!="PENDING":ds.add("review:FINAL_HUMAN_SOP_ACTIVATION:must_be_pending")
 for x in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS):ds.add(f"forbidden_flag:{x}")
 states=set(d.get("forbidden_states",[]));states.add(d.get("operational_state","DRAFT"))
 for x in sorted(states&FORBIDDEN_STATES):ds.add(f"forbidden_state:{x}")
 ready=not ds and not gaps
 return {"skill":"process-sop","state":"READY_FOR_HUMAN_SOP_ACTIVATION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"roles":len(roles),"steps":len(steps),"exceptions":len(exceptions),"controls":len(controls),"metrics":len(metrics),"assets":len(assets),"uat_cases":len(testsuites),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(rev.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 process truth, operational effectiveness, control compliance, user competence/adoption, token cost or duration."}
def main():
 if len(sys.argv)!=2:print("usage: evaluate_process_sop.py INPUT.json",file=sys.stderr);return 2
 r=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")));print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__":raise SystemExit(main())
