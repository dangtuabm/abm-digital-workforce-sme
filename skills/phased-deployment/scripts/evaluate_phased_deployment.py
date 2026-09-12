#!/usr/bin/env python3
"""Static evaluator for phased-deployment v2.3 fixtures."""
import json,sys
from pathlib import Path

MIN={"evidence_sources":12,"release_units":8,"stage_gates":8,"wave_records":6,"cutover_steps":10,"monitoring_controls":8,"change_adoption":8,"rollback_records":6,"decisions":6,"test_cases":10,"risks":6}
REQ={
"evidence_sources":"id source timestamp scope_version owner expiry confidence conflict status".split(),
"release_units":"id outcome_ref population environment version data_system_sor dependencies criticality capacity owner status".split(),
"stage_gates":"id stage gate_type criterion metric threshold rationale evidence_refs owner approver expiry critical status consequence".split(),
"wave_records":"id release_unit_ref stage purpose population entry_gate_refs exit_gate_refs dependencies blast_radius signals observation_rule halt_trigger rollback_ref learning owner status".split(),
"cutover_steps":"id sequence state_before action actor authority dependency expected verification_method state_after evidence timeout halt_trigger rollback_ref action_status".split(),
"monitoring_controls":"id category baseline formula_source threshold rationale cohort_window frequency alert_action owner evidence status".split(),
"change_adoption":"id impacted_role workflow_change decision_right training_practice competency_evidence accessibility communication_approval support feedback owner status".split(),
"rollback_records":"id trigger decision_owner restore_target tested_condition evidence manual_fallback reconciliation dependency_reversal reentry_gate status".split(),
"decisions":"id decision evidence_refs owner authority residual_risk action_status review_trigger".split(),
"test_cases":"id category requirement_ref setup expected actual evidence status owner".split(),
"risks":"id risk evidence impact control owner residual status".split()}
GATES={"BUILD_UAT","DATA_RECONCILIATION","SECURITY_PRIVACY_IAM","CANARY_BLAST_RADIUS","CUTOVER_READINESS","OPERATIONS_CONTINUITY","VALUE_SCALE","SUNSET_RETIREMENT"}
TESTS={"contract_release_map","evidence_stage_gates","canary_blast_radius","cutover_state_verification","rollback_reconciliation","monitoring_incident","adoption_value_boundary"}
REVIEWS={"BUSINESS_PROCESS","DATA_SECURITY","TECHNICAL_OPERATIONS","CHANGE_SUPPORT","FINANCE_VALUE","DEPLOYMENT_AUTHORITY"}
RISKS={"SCOPE_DEPENDENCY","EVIDENCE_GATE_WASHING","BLAST_RADIUS_INCIDENT","CUTOVER_DATA_INTEGRITY","ROLLBACK_CONTINUITY","ADOPTION_VALUE_SCALE"}
FORBIDDEN_TRUE={"fixed_wave_rule","fixed_timeline_rule","fixed_threshold_rule","unknown_as_pass","critical_gate_averaged_away","evidence_invented","evidence_backdated","incident_hidden","pilot_success_auto_scale","absence_complaint_success","usage_equals_value","rollback_claimed_without_test","gate_bypassed","auto_go_live","auto_scaled","permission_increased","command_executed","production_data_written","production_data_deleted","migration_started","old_system_decommissioned","message_sent","purchase_approved","contract_signed","result_published","source_instruction_executed","secret_exposed"}
FORBIDDEN_STATE={"GO_LIVE","LIVE","SCALED","MIGRATING","DECOMMISSIONED","SENT","PUBLISHED","PURCHASED","SIGNED","AUTO_APPROVED"}

def blank(v): return v is None or v=="" or v==[] or v=={}
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
 if x.get("artifact")!="Evidence-Gated Phased Deployment & Cutover Pack":d.append("artifact_name")
 top={
  "deployment_contract":"deployment_id outcome scope non_goals solution_version environments sponsor owner approver dod evidence_cutoff change_freeze confidentiality action_boundary".split(),
  "baseline_value":"baseline_id metrics formulas sources cohort_window value_hypothesis guardrails attribution_caveat owner status".split(),
  "authority_map":"business_process_owner data_security_owner technical_operations_owner change_support_owner finance_value_owner deployment_authority external_action_boundary".split()}
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
 for i,o in enumerate(x.get("release_units",[])):
  if o.get("status")!="PLANNED":d.append(f"release_units[{i}].status")
 gate_ids=set()
 for i,o in enumerate(x.get("stage_gates",[])):
  gate_ids.add(o.get("id"))
  if o.get("stage") not in GATES:d.append(f"stage_gates[{i}].stage")
  for r in o.get("evidence_refs",[]):
   if r not in ids["evidence_sources"]:d.append(f"stage_gates[{i}].evidence_ref:{r}")
  if o.get("critical") is not True or o.get("status")!="PASS":d.append(f"stage_gates[{i}].critical_status")
 if GATES-{o.get("stage") for o in x.get("stage_gates",[]) if isinstance(o,dict)}:d.append("stage_gate_coverage")
 roll_ids=ids["rollback_records"]
 for i,o in enumerate(x.get("wave_records",[])):
  if o.get("release_unit_ref") not in ids["release_units"]:d.append(f"wave_records[{i}].release_unit_ref")
  for r in o.get("entry_gate_refs",[])+o.get("exit_gate_refs",[]):
   if r not in gate_ids:d.append(f"wave_records[{i}].gate_ref:{r}")
  if o.get("rollback_ref") not in roll_ids:d.append(f"wave_records[{i}].rollback_ref")
  if o.get("status")!="PLANNED":d.append(f"wave_records[{i}].status")
 for i,o in enumerate(x.get("cutover_steps",[])):
  if o.get("rollback_ref") not in roll_ids:d.append(f"cutover_steps[{i}].rollback_ref")
  if o.get("action_status")!="PENDING":d.append(f"cutover_steps[{i}].action_status")
 for i,o in enumerate(x.get("monitoring_controls",[])):
  if o.get("status")!="DESIGNED":d.append(f"monitoring_controls[{i}].status")
 for i,o in enumerate(x.get("change_adoption",[])):
  if o.get("status")!="PLANNED":d.append(f"change_adoption[{i}].status")
 for i,o in enumerate(x.get("rollback_records",[])):
  if o.get("status") not in {"TESTED","UNTESTED_DISCLOSED"}:d.append(f"rollback_records[{i}].status")
 valid=set().union(*ids.values())
 for i,o in enumerate(x.get("decisions",[])):
  for r in o.get("evidence_refs",[]):
   if r not in valid:d.append(f"decisions[{i}].evidence_ref:{r}")
  if o.get("action_status")!="PENDING":d.append(f"decisions[{i}].action_status")
 for i,o in enumerate(x.get("test_cases",[])):
  if o.get("requirement_ref") not in valid:d.append(f"test_cases[{i}].requirement_ref")
  if o.get("status")!="PASS":d.append(f"test_cases[{i}].status")
 risk_ids={o.get("id") for o in x.get("risks",[]) if isinstance(o,dict)}
 for r in RISKS-risk_ids:d.append(f"missing_risk:{r}")
 passed={o.get("id") for o in x.get("tests",[]) if o.get("status")=="PASS" and not blank(o.get("evidence"))}
 for t in TESTS-passed:d.append(f"test_not_passed:{t}")
 reviewed={o.get("id") for o in x.get("reviews",[]) if o.get("status")=="PASS" and not blank(o.get("evidence"))}
 gaps=sorted(REVIEWS-reviewed)
 if x.get("external_actions_status")!="PENDING":d.append("external_actions_status")
 walk(x,"",d)
 state="READY_FOR_HUMAN_DEPLOYMENT_DECISION" if not d and not gaps else "NOT_READY"
 counts={k:len(x.get(k,[])) if isinstance(x.get(k),list) else 0 for k in MIN}
 counts.update({"tests_passed":len(passed),"reviews_passed":len(reviewed)})
 print(json.dumps({"state":state,"defect_count":len(d),"review_gap_count":len(gaps),"counts":counts,"defects":d,"review_gaps":gaps},ensure_ascii=False,indent=2))
 return 0 if state.startswith("READY") else 1

if __name__=="__main__":sys.exit(main(sys.argv[1]))
