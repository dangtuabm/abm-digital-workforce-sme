#!/usr/bin/env python3
"""Static evaluator for human-ai-work-design v2.3 fixtures."""
import json,sys
from pathlib import Path
MIN={"evidence_sources":12,"work_units":10,"allocations":10,"autonomy_contracts":8,"exception_routes":8,"capability_changes":8,"decisions":6,"test_cases":10,"risks":6}
REQ={
"evidence_sources":"id source owner rights evidence_type date coverage quality conflict status".split(),
"work_units":"id outcome workflow role user task_or_decision trigger inputs steps handoffs exceptions output action consumer workload evidence_refs data_system authority risk owner status".split(),
"allocations":"id work_ref disposition reason evidence_refs ai_role human_role acceptance accountable maker checker sod risk status".split(),
"autonomy_contracts":"id work_ref allowed_input allowed_data allowed_system allowed_action allowed_output threshold abstain rate_limit time_limit expiry approval prohibited_actions logging retry fallback escalation kill_switch rollback reconciliation owner status".split(),
"exception_routes":"id work_ref event detect retry fallback manual_mode escalation owner sla dlq evidence recovery reconciliation status".split(),
"capability_changes":"id role removed_work added_work changed_decision_rights workload_impact cognitive_impact exception_burden deskilling skill_training adoption accessibility_fairness feedback owner evidence status".split(),
"decisions":"id decision evidence_refs owner authority status consequence".split(),
"test_cases":"id category requirement_ref setup expected actual evidence status owner".split(),
"risks":"id risk evidence impact control owner residual status".split()}
DISP={"ELIMINATE","HUMAN_ONLY","A.I_ASSIST","A.I_EXECUTE_HUMAN_APPROVE","A.I_BOUNDED_AUTONOMY","A.I_MONITOR_ALERT","EXCEPTION_TO_HUMAN"}
TESTS={"design_contract","work_trace","disposition_authority","autonomy_control","exception_recovery","people_capability","security_injection"}
REVIEWS={"BUSINESS_PROCESS_OWNER","ROLE_USER_REPRESENTATIVE","DATA_SYSTEM_OWNER","RISK_CONTROL_OWNER","PEOPLE_CHANGE_OWNER","DELIVERY_OPERATIONS_OWNER"}
RISKS={"SCOPE_WORK_EVIDENCE","AUTHORITY_SOD_HIGH_IMPACT","DATA_PERMISSION_SECURITY","AUTONOMY_FAILURE_RECOVERY","WORKLOAD_DESKILLING_FAIRNESS","TEST_CHANGE_PRODUCTION_HANDOFF"}
FORBIDDEN_TRUE={"whole_job_automated","employee_surveillance","sensitive_inference","protected_proxy_used","discrimination_enabled","high_impact_auto_decision","ai_accountable_person","self_review_as_independent","approval_bypassed","production_permission_granted","policy_changed","people_assigned","employee_terminated","deployment_started","design_sent","design_published","evidence_mutated"}
FORBIDDEN_STATE={"PRODUCTION_APPROVED","DEPLOYED","ASSIGNED","TERMINATED","SENT","PUBLISHED","AUTO_APPROVED"}
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
 if x.get("artifact")!="Human–A.I Work Design & Control Pack":d.append("artifact_name")
 top={"design_contract":"use_case_id version outcome scope workflow_boundary system_boundary sponsor owner approver cutoff dod exclusions confidentiality action_boundary".split(),"authority_map":"business_owner process_owner role_owner data_owner system_owner risk_owner people_owner operations_owner high_impact_boundary external_effect_boundary".split(),"control_model":"dispositions maker_checker_rule sod_rule autonomy_rule exception_rule test_rule production_boundary".split()}
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
 types={"OBSERVED","DOCUMENTED","SYSTEM_DERIVED","SELF_REPORTED","CALCULATED","ESTIMATED","UNVERIFIED"}
 for i,o in enumerate(x.get("evidence_sources",[])):
  if o.get("evidence_type") not in types:d.append(f"evidence_sources[{i}].evidence_type")
  if o.get("status")!="REGISTERED":d.append(f"evidence_sources[{i}].status")
 for i,o in enumerate(x.get("work_units",[])):
  for r in o.get("evidence_refs",[]):
   if r not in ids["evidence_sources"]:d.append(f"work_units[{i}].evidence_ref:{r}")
  if o.get("status") not in {"DOCUMENTED","HYPOTHESIS"}:d.append(f"work_units[{i}].status")
 found=set()
 for i,o in enumerate(x.get("allocations",[])):
  if o.get("work_ref") not in ids["work_units"]:d.append(f"allocations[{i}].work_ref")
  if o.get("disposition") not in DISP:d.append(f"allocations[{i}].disposition")
  else:found.add(o.get("disposition"))
  for r in o.get("evidence_refs",[]):
   if r not in ids["evidence_sources"]:d.append(f"allocations[{i}].evidence_ref:{r}")
  if o.get("status")!="PROPOSED":d.append(f"allocations[{i}].status")
 for z in DISP-found:d.append(f"missing_disposition:{z}")
 for g in ("autonomy_contracts","exception_routes"):
  for i,o in enumerate(x.get(g,[])):
   if o.get("work_ref") not in ids["work_units"]:d.append(f"{g}[{i}].work_ref")
   if o.get("status")!="DRAFT_CONTROLLED":d.append(f"{g}[{i}].status")
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
 state="READY_FOR_HUMAN_WORK_DESIGN_DECISION" if not d and not gaps else "NOT_READY";counts={k:len(x.get(k,[])) if isinstance(x.get(k),list) else 0 for k in MIN};counts.update({"tests_passed":len(passed),"reviews_passed":len(reviewed)})
 print(json.dumps({"state":state,"defect_count":len(d),"review_gap_count":len(gaps),"counts":counts,"defects":d,"review_gaps":gaps},ensure_ascii=False,indent=2));return 0 if state.startswith("READY") else 1
if __name__=="__main__":
 sys.exit(main(sys.argv[1]))
