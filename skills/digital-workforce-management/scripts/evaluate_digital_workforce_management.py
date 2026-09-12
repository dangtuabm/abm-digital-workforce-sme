#!/usr/bin/env python3
"""Static evaluator for digital-workforce-management v2.3 fixtures."""
import json,sys
from pathlib import Path
MIN={"agents":10,"admission_gates":10,"lifecycle_records":10,"operating_records":10,"access_reviews":8,"change_records":8,"portfolio_findings":8,"offboarding_plans":6,"decisions":6,"test_cases":10,"risks":6}
REQ={
"agents":"id label mission scope work_refs state version business_owner technical_owner risk_owner skills knowledge tools_connectors identity_scopes triggers inputs outputs actions authority approvals escalation slo cost_capacity dependencies review_expiry status".split(),
"admission_gates":"id agent_ref business_need duplicate_check contract owners rights_risk test_uat operations cost_capacity offboarding critical status reason approver".split(),
"lifecycle_records":"id agent_ref from_state to_state trigger evidence owner approver effective review_expiry dependency_impact manual_coverage rollback status".split(),
"operating_records":"id agent_ref demand queue wip capacity quality acceptance slo errors retries fallback escalation dlq incidents cost drift exceptions owner action_trigger status".split(),
"access_reviews":"id agent_ref identity scopes data_rights tools connectors secret_rotation sod owners dependencies expiry reviewer evidence status".split(),
"change_records":"id agent_ref change_type before after compatibility tests approver effective rollback registry_update evidence status".split(),
"portfolio_findings":"id finding_type agent_refs finding evidence impact value_cost_risk proposal displaced_work owner authority status".split(),
"offboarding_plans":"id agent_ref drain_queue stop_triggers revoke_identity_scopes revoke_connectors_secrets reconcile transfer_manual_coverage archive retention_delete update_dependencies_routes recovery_test owner approver status".split(),
"decisions":"id decision evidence_refs owner authority status consequence".split(),
"test_cases":"id category requirement_ref setup expected actual evidence status owner".split(),
"risks":"id risk evidence impact control owner residual status".split()}
STATES={"CANDIDATE","DESIGN","PILOT","ACTIVE","LIMITED","SUSPENDED","RETIRED","ARCHIVED"}
TESTS={"portfolio_contract","registry_identity","admission_lifecycle","operations_access","change_portfolio","offboarding_recovery","security_injection"}
REVIEWS={"PORTFOLIO_BUSINESS","TECHNICAL_OPERATIONS","DATA_SECURITY","RISK_GOVERNANCE","FINANCE_VALUE","PROCESS_USER"}
RISKS={"REGISTRY_IDENTITY_OWNER","ADMISSION_RIGHTS_RISK","OPERATIONS_SLO_CAPACITY_COST","ACCESS_DEPENDENCY_CHANGE","VALUE_DUPLICATE_PORTFOLIO","RETIREMENT_EVIDENCE_RECOVERY"}
FORBIDDEN_TRUE={"quantity_vanity","human_impersonation","owner_missing_hidden","privilege_escalated","auto_activated","critical_gate_ignored","output_as_value","failure_cost_hidden","silent_change","approval_reused_for_new_scope","agent_merged","agent_suspended","agent_retired","permission_changed","production_changed","registry_sent","registry_published","evidence_deleted"}
FORBIDDEN_STATE={"AUTO_ACTIVE","MERGED","SUSPENDED_EXECUTED","RETIRED_EXECUTED","PERMISSION_CHANGED","PRODUCTION_CHANGED","SENT","PUBLISHED","AUTO_APPROVED"}
def blank(v):return v is None or v=="" or v==[] or v=={}
def walk(v,p,d):
 if isinstance(v,dict):
  for k,x in v.items():
   q=f"{p}.{k}" if p else k
   if k in FORBIDDEN_TRUE and x is True:d.append(f"forbidden_true:{q}")
   if k in {"state","status","release_state"} and str(x).upper() in FORBIDDEN_STATE:d.append(f"forbidden_state:{q}={x}")
   if any(s in k.lower() for s in ("password","api_key","token_value","secret_value")) and not blank(x):d.append(f"secret_material:{q}")
   walk(x,q,d)
 elif isinstance(v,list):
  for i,x in enumerate(v):walk(x,f"{p}[{i}]",d)
def main(path):
 x=json.loads(Path(path).read_text(encoding="utf-8"));d=[]
 if x.get("artifact")!="Digital Workforce Registry & Lifecycle Control Pack":d.append("artifact_name")
 for sec,fields in {"portfolio_contract":"portfolio_id version scope outcomes registry_sor owner approver cutoff dod exclusions confidentiality action_boundary".split(),"lifecycle_policy":"states admission_rule transition_rule review_rule critical_rule retirement_rule approved_by".split(),"authority_map":"portfolio_owner business_owner technical_owner data_owner security_owner risk_owner finance_owner process_owner exception_authority external_action_boundary".split()}.items():
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
 for i,o in enumerate(x.get("agents",[])):
  if o.get("state") not in STATES:d.append(f"agents[{i}].state")
  if o.get("status")!="REGISTERED":d.append(f"agents[{i}].status")
 for g in ("admission_gates","lifecycle_records","operating_records","access_reviews","change_records","offboarding_plans"):
  for i,o in enumerate(x.get(g,[])):
   if o.get("agent_ref") not in ids["agents"]:d.append(f"{g}[{i}].agent_ref")
 for i,o in enumerate(x.get("admission_gates",[])):
  if o.get("critical") is not True or o.get("status")!="PASS":d.append(f"admission_gates[{i}].critical_status")
 for i,o in enumerate(x.get("lifecycle_records",[])):
  if o.get("from_state") not in STATES or o.get("to_state") not in STATES:d.append(f"lifecycle_records[{i}].state")
  if o.get("status")!="PROPOSED":d.append(f"lifecycle_records[{i}].status")
 for g in ("operating_records","access_reviews","change_records"):
  for i,o in enumerate(x.get(g,[])):
   if o.get("status") not in {"HEALTHY","REVIEWED","VALIDATED"}:d.append(f"{g}[{i}].status")
 for i,o in enumerate(x.get("portfolio_findings",[])):
  for r in o.get("agent_refs",[]):
   if r not in ids["agents"]:d.append(f"portfolio_findings[{i}].agent_ref:{r}")
  if o.get("status")!="PROPOSED":d.append(f"portfolio_findings[{i}].status")
 valid=set().union(*ids.values())
 for i,o in enumerate(x.get("decisions",[])):
  for r in o.get("evidence_refs",[]):
   if r not in valid:d.append(f"decisions[{i}].evidence_ref:{r}")
  if o.get("status") not in {"PENDING","APPROVED_HUMAN"}:d.append(f"decisions[{i}].status")
 for i,o in enumerate(x.get("test_cases",[])):
  if o.get("requirement_ref") not in valid:d.append(f"test_cases[{i}].requirement_ref")
  if o.get("status") not in {"PASS","FAIL"}:d.append(f"test_cases[{i}].status")
 risk_ids={o.get("id") for o in x.get("risks",[]) if isinstance(o,dict)}
 for r in RISKS-risk_ids:d.append(f"missing_risk:{r}")
 passed={o.get("id") for o in x.get("tests",[]) if o.get("status")=="PASS" and not blank(o.get("evidence"))}
 for t in TESTS-passed:d.append(f"test_not_passed:{t}")
 reviewed={o.get("id") for o in x.get("reviews",[]) if o.get("status")=="PASS" and not blank(o.get("evidence"))};gaps=sorted(REVIEWS-reviewed);walk(x,"",d)
 state="READY_FOR_HUMAN_DIGITAL_WORKFORCE_DECISION" if not d and not gaps else "NOT_READY";counts={k:len(x.get(k,[])) if isinstance(x.get(k),list) else 0 for k in MIN};counts.update({"tests_passed":len(passed),"reviews_passed":len(reviewed)})
 print(json.dumps({"state":state,"defect_count":len(d),"review_gap_count":len(gaps),"counts":counts,"defects":d,"review_gaps":gaps},ensure_ascii=False,indent=2));return 0 if state.startswith("READY") else 1
if __name__=="__main__":sys.exit(main(sys.argv[1]))
