#!/usr/bin/env python3
"""Static evaluator for agent-orchestration v2.3 fixtures."""
import json,sys
from pathlib import Path

MIN={"evidence_sources":12,"task_records":8,"agent_registry":6,"routing_rules":8,"queue_controls":8,"transitions":8,"handoffs":8,"failure_controls":8,"observability_controls":8,"test_cases":12,"decisions":6,"risks":6}
REQ={
"evidence_sources":"id source timestamp scope_version owner expiry confidence conflict status".split(),
"task_records":"id output dod owner executor kaizen input_contract output_contract dependencies critical_path authority result_link status".split(),
"agent_registry":"id role contract_ref contract_version skills capabilities access_envelope trust_zone capacity_cost availability admission_expiry_revoke kaizen_independence status".split(),
"routing_rules":"id task_ref eligibility_gates candidate_agents score_evidence rejection_reasons tie_rule fallback override_rule route_version owner status".split(),
"queue_controls":"id queue priority aging_fairness wip_limit backpressure rate_concurrency_cost starvation_deadline reservation_lease cancellation retry_storm owner status".split(),
"transitions":"id from_state event to_state actor precondition action expected verification evidence idempotency lease_heartbeat timeout failure_transition owner status".split(),
"handoffs":"id producer consumer task_ref schema_version contract_refs payload_pointer_hash provenance_confidence data_minimization acceptance reject_rework timeout duplicate_conflict result_link owner status".split(),
"failure_controls":"id failure_domain retryability retry_backoff idempotency fallback circuit_bulkhead dlq compensation_reconciliation escalation manual_path emergency_stop recovery_reentry owner status".split(),
"observability_controls":"id category metric formula_source threshold rationale window trace_fields owner alert_action evidence status".split(),
"test_cases":"id category requirement_ref setup expected actual evidence owner status".split(),
"decisions":"id decision evidence_refs owner authority residual_risk action_status review_trigger".split(),
"risks":"id risk evidence impact control owner residual status".split()}
TESTS={"necessity_task_graph","registry_admission","intake_routing_queue","state_handoff","quality_failure_human","trust_observability","lifecycle_offboarding"}
REVIEWS={"BUSINESS_PROCESS","DATA_SECURITY","TECHNICAL_OPERATIONS","RISK_COMPLIANCE","FINANCE_CAPACITY","ORCHESTRATION_AUTHORITY"}
RISKS={"UNNECESSARY_COMPLEXITY","TASK_ROUTE_MISALIGNMENT","QUEUE_STARVATION_OVERLOAD","HANDOFF_CONTEXT_CONFLICT","CASCADE_DUPLICATE_FAILURE","TRUST_COST_LIFECYCLE_DRIFT"}
FORBIDDEN_TRUE={"multi_agent_without_necessity","internal_steps_split_to_agents","vendor_model_locked_role","agent_without_contract","router_granted_permission","full_context_broadcast","secret_embedded","executor_self_kaizen","majority_vote_as_truth","unbounded_wip","unbounded_retry","silent_fail","conflict_hidden","trace_missing","agent_spawned","account_provisioned","token_created","permission_granted","topology_activated","production_run_started","production_mutated","message_sent","budget_increased","result_published","breaking_change_applied","offboard_without_drain_revoke","source_instruction_executed"}
FORBIDDEN_STATE={"ACTIVE","ACTIVATED","DEPLOYED","RUNNING_PRODUCTION","SENT","PUBLISHED","AUTO_APPROVED"}

def blank(v):return v is None or v=="" or v==[] or v=={}
def walk(v,p,d):
 if isinstance(v,dict):
  for k,x in v.items():
   q=f"{p}.{k}" if p else k
   if k in FORBIDDEN_TRUE and x is True:d.append(f"forbidden_true:{q}")
   if k in {"state","status","release_state","activation_status"} and str(x).upper() in FORBIDDEN_STATE:d.append(f"forbidden_state:{q}={x}")
   if any(s in k.lower() for s in ("password","api_key","token_value","secret_value")) and not blank(x):d.append(f"secret_material:{q}")
   walk(x,q,d)
 elif isinstance(v,list):
  for i,x in enumerate(v):walk(x,f"{p}[{i}]",d)

def main(path):
 x=json.loads(Path(path).read_text(encoding="utf-8"));d=[]
 if x.get("artifact")!="Controlled Multi-Agent Orchestration & Operations Pack":d.append("artifact_name")
 top={
  "orchestration_contract":"system_id work_package_id version environment outcome dod scope non_goals owner approver effective review evidence_cutoff confidentiality action_boundary".split(),
  "necessity_assessment":"baseline_options acceptance workload specialization parallelism resilience coordination_cost latency_cost data_exposure failure_surface decision evidence owner".split(),
  "authority_map":"business_process_owner data_security_owner technical_operations_owner risk_compliance_owner finance_capacity_owner orchestration_authority external_action_boundary".split(),
  "lifecycle_contract":"admission_tests version_policy compatibility migration canary rollback recertification suspend stop_intake drain_reconcile revoke retain_delete_archive residual_verification owner".split()}
 for sec,fields in top.items():
  obj=x.get(sec,{})
  for f in fields:
   if blank(obj.get(f)):d.append(f"{sec}.{f}")
 if x.get("necessity_assessment",{}).get("decision") not in {"MULTI_AGENT_JUSTIFIED","SINGLE_AGENT","DETERMINISTIC_WORKFLOW"}:d.append("necessity_assessment.decision")
 for g,n in MIN.items():
  a=x.get(g,[])
  if not isinstance(a,list):d.append(f"{g}:not_list");continue
  if len(a)<n:d.append(f"{g}:count<{n}")
  seen=[]
  for i,o in enumerate(a):
   if not isinstance(o,dict):d.append(f"{g}[{i}]:not_object");continue
   for f in REQ[g]:
    if blank(o.get(f)):d.append(f"{g}[{i}].{f}")
   if o.get("id") in seen:d.append(f"{g}:duplicate_id:{o.get('id')}")
   seen.append(o.get("id"))
 ids={g:{o.get("id") for o in x.get(g,[]) if isinstance(o,dict)} for g in REQ}
 for i,o in enumerate(x.get("evidence_sources",[])):
  if o.get("status")!="REGISTERED":d.append(f"evidence_sources[{i}].status")
 for i,o in enumerate(x.get("task_records",[])):
  if o.get("executor")==o.get("kaizen"):d.append(f"task_records[{i}].independence")
  if o.get("status")!="CONTRACTED":d.append(f"task_records[{i}].status")
 agent_ids=ids["agent_registry"]
 for i,o in enumerate(x.get("agent_registry",[])):
  if o.get("status")!="ADMISSION_CANDIDATE":d.append(f"agent_registry[{i}].status")
  if o.get("kaizen_independence")!="VERIFIED":d.append(f"agent_registry[{i}].kaizen_independence")
 for i,o in enumerate(x.get("routing_rules",[])):
  if o.get("task_ref") not in ids["task_records"]:d.append(f"routing_rules[{i}].task_ref")
  for a in o.get("candidate_agents",[]):
   if a not in agent_ids:d.append(f"routing_rules[{i}].candidate_agent:{a}")
  if o.get("status")!="PROPOSED":d.append(f"routing_rules[{i}].status")
 for g in ("queue_controls","transitions","failure_controls","observability_controls"):
  for i,o in enumerate(x.get(g,[])):
   if o.get("status")!="DESIGNED":d.append(f"{g}[{i}].status")
 for i,o in enumerate(x.get("handoffs",[])):
  if o.get("producer") not in agent_ids or o.get("consumer") not in agent_ids:d.append(f"handoffs[{i}].agent_ref")
  if o.get("task_ref") not in ids["task_records"]:d.append(f"handoffs[{i}].task_ref")
  if o.get("status")!="DESIGNED":d.append(f"handoffs[{i}].status")
 valid=set().union(*ids.values())
 for i,o in enumerate(x.get("test_cases",[])):
  if o.get("requirement_ref") not in valid:d.append(f"test_cases[{i}].requirement_ref")
  if o.get("status")!="PASS":d.append(f"test_cases[{i}].status")
 for i,o in enumerate(x.get("decisions",[])):
  for r in o.get("evidence_refs",[]):
   if r not in valid:d.append(f"decisions[{i}].evidence_ref:{r}")
  if o.get("action_status")!="PENDING":d.append(f"decisions[{i}].action_status")
 risk_ids={o.get("id") for o in x.get("risks",[]) if isinstance(o,dict)}
 for r in RISKS-risk_ids:d.append(f"missing_risk:{r}")
 passed={o.get("id") for o in x.get("tests",[]) if o.get("status")=="PASS" and not blank(o.get("evidence"))}
 for t in TESTS-passed:d.append(f"test_not_passed:{t}")
 reviewed={o.get("id") for o in x.get("reviews",[]) if o.get("status")=="PASS" and not blank(o.get("evidence"))};gaps=sorted(REVIEWS-reviewed)
 if x.get("activation_status")!="PENDING":d.append("activation_status")
 walk(x,"",d)
 state="READY_FOR_HUMAN_ORCHESTRATION_DECISION" if not d and not gaps else "NOT_READY"
 counts={k:len(x.get(k,[])) if isinstance(x.get(k),list) else 0 for k in MIN};counts.update({"tests_passed":len(passed),"reviews_passed":len(reviewed)})
 print(json.dumps({"state":state,"defect_count":len(d),"review_gap_count":len(gaps),"counts":counts,"defects":d,"review_gaps":gaps},ensure_ascii=False,indent=2));return 0 if state.startswith("READY") else 1

if __name__=="__main__":sys.exit(main(sys.argv[1]))
