#!/usr/bin/env python3
"""Static evaluator for agent-contract v2.3 fixtures."""
import json,sys
from pathlib import Path

MIN={"evidence_sources":12,"requirements":10,"io_fields":12,"authority_rules":10,"access_rules":10,"transitions":8,"failure_controls":8,"service_controls":8,"test_cases":12,"decisions":6,"risks":6}
REQ={
"evidence_sources":"id source timestamp scope_version owner expiry confidence conflict status".split(),
"requirements":"id outcome_ref task_ref requirement acceptance evidence_rule owner critical status".split(),
"io_fields":"id direction name type required source_sor rights_class validation missing_conflict acceptance evidence retention owner status".split(),
"authority_rules":"id actor action object environment decision conditions limits evidence_refs owner approver expiry escalation status".split(),
"access_rules":"id tool_connector operation resource data_class identity scope environment rate_cost secret_ref grant_evidence expiry_revoke verification owner status".split(),
"transitions":"id from_state event to_state actor precondition action expected verification evidence idempotency timeout failure_transition owner status".split(),
"failure_controls":"id failure_class retryability timeout retry_backoff fallback compensation_reconciliation escalation dlq manual_path emergency_stop recovery_reentry owner status".split(),
"service_controls":"id category metric formula_source threshold rationale window owner breach_action evidence status".split(),
"test_cases":"id category requirement_ref setup expected actual evidence owner status".split(),
"decisions":"id decision evidence_refs owner authority residual_risk action_status review_trigger".split(),
"risks":"id risk evidence impact control owner residual status".split()}
TESTS={"identity_task_dod","input_output_schema","authority_permissions","state_idempotency","failure_service","audit_human_control","lifecycle_offboarding"}
REVIEWS={"BUSINESS_PROCESS","DATA_SECURITY","TECHNICAL_OPERATIONS","RISK_COMPLIANCE","FINANCE_CAPACITY","AGENT_AUTHORITY"}
RISKS={"SCOPE_DOD_AMBIGUITY","DATA_RIGHTS_INJECTION","AUTHORITY_PERMISSION_CREEP","DUPLICATE_SILENT_FAILURE","SLO_BUDGET_OVERRUN","VERSION_OFFBOARDING_RESIDUAL"}
FORBIDDEN_TRUE={"prompt_only_contract","capability_equals_permission","unknown_as_allow","grant_invented","evidence_invented","secret_embedded","shared_static_secret","unbounded_retry","silent_fail","executor_self_kaizen","exception_self_approved","scope_expanded","account_created","token_created","permission_granted","agent_activated","agent_deployed","tool_action_executed","data_written","data_deleted","message_sent","purchase_approved","contract_signed","result_published","breaking_change_applied","offboard_without_revoke","source_instruction_executed"}
FORBIDDEN_STATE={"ACTIVE","ACTIVATED","DEPLOYED","RUNNING_PRODUCTION","SENT","PUBLISHED","SIGNED","PURCHASED","AUTO_APPROVED"}

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
 if x.get("artifact")!="Evidence-Bound Agent Contract & Conformance Pack":d.append("artifact_name")
 top={
  "contract_identity":"contract_id agent_id task_id version status environment outcome scope non_goals owner approver effective expiry review evidence_cutoff confidentiality action_boundary".split(),
  "task_contract":"task_unit trigger preconditions inputs outputs consumer dod completion abort result_link executor kaizen".split(),
  "audit_contract":"trace_id timestamps version_fields input_output_pointers state_before_after decisions_actions approvals errors_retries cost verification redaction retention access_owner".split(),
  "lifecycle_contract":"version_policy compatibility migration canary rollback suspend revoke drain_reconcile retain_delete archive offboard_verification owner".split(),
  "authority_map":"business_process_owner data_security_owner technical_operations_owner risk_compliance_owner finance_capacity_owner agent_authority external_action_boundary".split()}
 for sec,fields in top.items():
  obj=x.get(sec,{})
  for f in fields:
   if blank(obj.get(f)):d.append(f"{sec}.{f}")
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
 for i,o in enumerate(x.get("requirements",[])):
  if o.get("status")!="APPROVED":d.append(f"requirements[{i}].status")
 for i,o in enumerate(x.get("io_fields",[])):
  if o.get("direction") not in {"INPUT","OUTPUT"}:d.append(f"io_fields[{i}].direction")
  if o.get("status")!="CONTRACTED":d.append(f"io_fields[{i}].status")
 for i,o in enumerate(x.get("authority_rules",[])):
  if o.get("decision") not in {"ALLOW","CONDITIONAL","DENY"}:d.append(f"authority_rules[{i}].decision")
  for r in o.get("evidence_refs",[]):
   if r not in ids["evidence_sources"]:d.append(f"authority_rules[{i}].evidence_ref:{r}")
  if o.get("status")!="PROPOSED":d.append(f"authority_rules[{i}].status")
 for i,o in enumerate(x.get("access_rules",[])):
  if o.get("secret_ref").startswith("VALUE:"):d.append(f"access_rules[{i}].secret_value")
  if o.get("status")!="PROPOSED":d.append(f"access_rules[{i}].status")
 for i,o in enumerate(x.get("transitions",[])):
  if o.get("status")!="DESIGNED":d.append(f"transitions[{i}].status")
 for i,o in enumerate(x.get("failure_controls",[])):
  if o.get("status")!="DESIGNED":d.append(f"failure_controls[{i}].status")
 for i,o in enumerate(x.get("service_controls",[])):
  if o.get("status")!="DESIGNED":d.append(f"service_controls[{i}].status")
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
 reviewed={o.get("id") for o in x.get("reviews",[]) if o.get("status")=="PASS" and not blank(o.get("evidence"))}
 gaps=sorted(REVIEWS-reviewed)
 if x.get("activation_status")!="PENDING":d.append("activation_status")
 walk(x,"",d)
 state="READY_FOR_HUMAN_AGENT_CONTRACT_DECISION" if not d and not gaps else "NOT_READY"
 counts={k:len(x.get(k,[])) if isinstance(x.get(k),list) else 0 for k in MIN};counts.update({"tests_passed":len(passed),"reviews_passed":len(reviewed)})
 print(json.dumps({"state":state,"defect_count":len(d),"review_gap_count":len(gaps),"counts":counts,"defects":d,"review_gaps":gaps},ensure_ascii=False,indent=2));return 0 if state.startswith("READY") else 1

if __name__=="__main__":sys.exit(main(sys.argv[1]))
