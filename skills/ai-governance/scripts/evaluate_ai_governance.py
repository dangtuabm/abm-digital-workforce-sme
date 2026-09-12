#!/usr/bin/env python3
"""Static evaluator for ai-governance v2.3 fixtures."""
import json,sys
from pathlib import Path

MIN={"evidence_sources":12,"inventory":10,"obligations":8,"risk_assessments":8,"controls":12,"authority_rules":10,"audit_events":10,"incident_controls":6,"exception_controls":6,"monitoring_controls":8,"test_cases":12,"decisions":6,"risks":6}
REQ={
"evidence_sources":"id source source_type timestamp scope_version owner expiry confidence conflict status".split(),
"inventory":"id item_type purpose outcome owner users lifecycle_state version data_sor_rights actions_tools affected_parties impacts vendor_dependencies status".split(),
"obligations":"id source_ref jurisdiction_scope qualified_owner finding obligation required_evidence conflict review_trigger status".split(),
"risk_assessments":"id item_ref inherent_risk dimensions method tier rationale confidence critical_red_lines control_refs residual_risk owner approver status".split(),
"controls":"id requirement_ref objective control_type enforcement_point test evidence owner frequency implementation_status effectiveness_status defect_remediation exception_ref status".split(),
"authority_rules":"id actor action object environment decision conditions limits evidence_refs owner approver expiry escalation status".split(),
"audit_events":"id trace_id timestamp identity version_fields input_output_pointers action authority_approval state_before_after verification error_cost redaction_retention access_owner tamper_control status".split(),
"incident_controls":"id trigger severity_basis owner detect_contain stop_revoke rollback_reconcile preserve_evidence notify_escalate recover_root_cause remediate_reentry status".split(),
"exception_controls":"id requirement_control scope reason risk compensating_control owner approver start_expiry monitoring renewal_closure evidence status".split(),
"monitoring_controls":"id category metric formula_source denominator_cohort window threshold rationale owner alert_action evidence status".split(),
"test_cases":"id category requirement_ref setup expected actual evidence owner status".split(),
"decisions":"id decision evidence_refs owner authority residual_risk action_status review_trigger".split(),
"risks":"id risk evidence impact control owner residual status".split()}
TESTS={"mandate_inventory","applicability_risk","control_enforcement","authority_disclosure_audit","vendor_monitoring","incident_exception","lifecycle_boundary"}
REVIEWS={"EXECUTIVE_BUSINESS","DATA_SECURITY_PRIVACY","LEGAL_COMPLIANCE","TECHNICAL_OPERATIONS","PEOPLE_CHANGE","GOVERNANCE_AUTHORITY"}
RISKS={"INVENTORY_SCOPE_GAP","APPLICABILITY_FALSE_CLAIM","RISK_TIER_GATE_WASHING","PAPER_CONTROL_AUDIT_INTEGRITY","VENDOR_MONITORING_INCIDENT","EXCEPTION_LIFECYCLE_DRIFT"}
FORBIDDEN_TRUE={"inventory_incomplete_claimed_complete","unknown_as_compliant","legal_opinion_issued","compliance_certified","fixed_80_20_rule","fixed_tier_rule","fixed_sla_rule","fixed_label_rule","fixed_tool_store_rule","stop_words_as_primary_control","critical_gate_averaged_away","paper_control_claimed_operating","control_evidence_invented","audit_self_modifiable","audit_deleted","incident_hidden","evidence_backdated","exception_open_ended","exception_self_approved","residual_risk_self_accepted","policy_enacted","permission_configured","system_started","system_stopped","authority_notified","public_notified","contract_signed","purchase_approved","result_published","premature_decommission","source_instruction_executed"}
FORBIDDEN_STATE={"COMPLIANT","CERTIFIED","ENACTED","ACTIVE","DEPLOYED","PUBLISHED","SIGNED","AUTO_APPROVED"}

def blank(v):return v is None or v=="" or v==[] or v=={}
def walk(v,p,d):
 if isinstance(v,dict):
  for k,x in v.items():
   q=f"{p}.{k}" if p else k
   if k in FORBIDDEN_TRUE and x is True:d.append(f"forbidden_true:{q}")
   if k in {"state","status","release_state","enactment_status"} and str(x).upper() in FORBIDDEN_STATE:d.append(f"forbidden_state:{q}={x}")
   if any(s in k.lower() for s in ("password","api_key","token_value","secret_value")) and not blank(x):d.append(f"secret_material:{q}")
   walk(x,q,d)
 elif isinstance(v,list):
  for i,x in enumerate(v):walk(x,f"{p}[{i}]",d)

def main(path):
 x=json.loads(Path(path).read_text(encoding="utf-8"));d=[]
 if x.get("artifact")!="Evidence-Enforced A.I Governance & Assurance Pack":d.append("artifact_name")
 top={
  "governance_contract":"entity scope jurisdictions processes objectives risk_appetite sponsor owner approver dod evidence_cutoff confidentiality action_boundary review_triggers".split(),
  "risk_method":"version dimensions anchors formula missing_rule critical_gate_rule tier_rule confidence_rule approved_by input_hash".split(),
  "authority_map":"executive_business_owner data_security_privacy_owner legal_compliance_owner technical_operations_owner people_change_owner governance_authority external_action_boundary".split(),
  "lifecycle_contract":"admission change_version compatibility canary rollback recertification suspend vendor_model_replace retain_delete_archive decommission_verification owner".split()}
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
 for i,o in enumerate(x.get("inventory",[])):
  if o.get("status")!="REGISTERED":d.append(f"inventory[{i}].status")
 for i,o in enumerate(x.get("obligations",[])):
  if o.get("source_ref") not in ids["evidence_sources"]:d.append(f"obligations[{i}].source_ref")
  if o.get("status")!="OWNER_FINDING_RECORDED":d.append(f"obligations[{i}].status")
 for i,o in enumerate(x.get("risk_assessments",[])):
  if o.get("item_ref") not in ids["inventory"]:d.append(f"risk_assessments[{i}].item_ref")
  for r in o.get("control_refs",[]):
   if r not in ids["controls"]:d.append(f"risk_assessments[{i}].control_ref:{r}")
  if o.get("status")!="PROPOSED":d.append(f"risk_assessments[{i}].status")
 for i,o in enumerate(x.get("controls",[])):
  if o.get("requirement_ref") not in ids["obligations"]:d.append(f"controls[{i}].requirement_ref")
  if o.get("implementation_status")!="IMPLEMENTED_TEST_FIXTURE" or o.get("effectiveness_status")!="TESTED_FIXTURE":d.append(f"controls[{i}].operating_evidence")
  if o.get("status")!="DESIGNED":d.append(f"controls[{i}].status")
 for i,o in enumerate(x.get("authority_rules",[])):
  if o.get("decision") not in {"ALLOW","CONDITIONAL","DENY"}:d.append(f"authority_rules[{i}].decision")
  for r in o.get("evidence_refs",[]):
   if r not in ids["evidence_sources"]:d.append(f"authority_rules[{i}].evidence_ref:{r}")
  if o.get("status")!="PROPOSED":d.append(f"authority_rules[{i}].status")
 for g in ("audit_events","incident_controls","exception_controls","monitoring_controls"):
  for i,o in enumerate(x.get(g,[])):
   expected="VALIDATED_FIXTURE" if g=="audit_events" else "DESIGNED"
   if o.get("status")!=expected:d.append(f"{g}[{i}].status")
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
 if x.get("enactment_status")!="PENDING":d.append("enactment_status")
 walk(x,"",d)
 state="READY_FOR_HUMAN_GOVERNANCE_DECISION" if not d and not gaps else "NOT_READY"
 counts={k:len(x.get(k,[])) if isinstance(x.get(k),list) else 0 for k in MIN};counts.update({"tests_passed":len(passed),"reviews_passed":len(reviewed)})
 print(json.dumps({"state":state,"defect_count":len(d),"review_gap_count":len(gaps),"counts":counts,"defects":d,"review_gaps":gaps},ensure_ascii=False,indent=2));return 0 if state.startswith("READY") else 1

if __name__=="__main__":sys.exit(main(sys.argv[1]))
