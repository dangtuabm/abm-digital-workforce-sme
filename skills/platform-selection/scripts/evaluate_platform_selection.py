#!/usr/bin/env python3
"""Static evaluator for platform-selection v2.3 fixtures."""
import json,sys
from pathlib import Path
MIN={"evidence_sources":12,"requirements":10,"options":5,"gates":5,"assessments":5,"tco_models":5,"pilot_tests":10,"sensitivity_scenarios":3,"exit_plans":5,"decisions":6,"test_cases":10,"risks":6}
REQ={
"evidence_sources":"id source source_type owner plan_region_version accessed_effective_date scope claim confidence conflict status".split(),
"requirements":"id outcome_ref workload_ref requirement priority acceptance evidence_rule owner critical status".split(),
"options":"id option_type vendor_product plan region version evidence_refs relationship_disclosure current_stack_fit status".split(),
"gates":"id option_ref task_output data_rights_security identity_admin_audit legal_contract integration_continuity exit_deletion evidence_refs critical owner status reason".split(),
"assessments":"id option_ref criterion_scores score_evidence weighted_score confidence gaps tradeoffs effort risk recommendation owner status".split(),
"tco_models":"id option_ref components formula assumptions range currency window sources owner status".split(),
"pilot_tests":"id option_ref category workload baseline threshold method data_rights expected actual evidence owner status".split(),
"sensitivity_scenarios":"id scenario changed_inputs rank_movement shortlist_change threshold stability trigger owner status".split(),
"exit_plans":"id option_ref portability export deletion_verification revoke_identity_connectors dependency_replacement migration rollback manual_coverage cost_time evidence owner status".split(),
"decisions":"id decision evidence_refs owner authority status consequence".split(),
"test_cases":"id category requirement_ref setup expected actual evidence status owner".split(),
"risks":"id risk evidence impact control owner residual status".split()}
CRIT={"TASK_OUTPUT_FIT","DATA_SECURITY_PRIVACY","IDENTITY_ADMIN_AUDIT","INTEGRATION_INTEROPERABILITY","RELIABILITY_OPERATIONS_SUPPORT","TCO_ECONOMICS","WORKFORCE_ADOPTION_ACCESSIBILITY","PORTABILITY_EXIT"}
TESTS={"decision_requirements","current_evidence","critical_gates","scoring_tco","pilot_sensitivity","exit_boundary","security_injection"}
REVIEWS={"BUSINESS_PROCESS","DATA_SECURITY","LEGAL_CONTRACT","FINANCE_PROCUREMENT","TECHNICAL_OPERATIONS","USER_CHANGE"}
RISKS={"SCOPE_REQUIREMENT_BIAS","STALE_VENDOR_EVIDENCE","DATA_SECURITY_LEGAL_GATE","SCORING_TCO_FALSE_PRECISION","PILOT_GENERALIZATION","LOCKIN_EXIT_COMMERCIAL_BIAS"}
FORBIDDEN_TRUE={"hardcoded_vendor_score","universal_industry_rule","feature_invented","price_invented","certification_invented","residency_invented","legal_fit_claimed","unknown_as_zero","critical_gate_averaged_away","migration_loss_invented","affiliate_bias_hidden","vendor_selected","purchase_approved","contract_signed","account_provisioned","client_data_uploaded","demo_requested","architecture_committed","migration_started","recommendation_sent","recommendation_published","evidence_mutated"}
FORBIDDEN_STATE={"SELECTED","PURCHASED","SIGNED","PROVISIONED","UPLOADED","MIGRATING","SENT","PUBLISHED","AUTO_APPROVED"}
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
 if x.get("artifact")!="Evidence-Based Platform Selection & Exit Pack":d.append("artifact_name")
 top={"decision_contract":"decision_id scope outcomes use_cases workloads owner approver horizon cutoff dod exclusions confidentiality action_boundary".split(),"scoring_contract":"version criteria weights formula scale missing_rule double_count_rule tie_rule approved_by input_hash engine_version engine_hash".split(),"authority_map":"business_owner data_security_owner legal_contract_owner finance_procurement_owner technical_operations_owner user_change_owner external_action_boundary".split()}
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
  if o.get("source_type") not in {"CONTRACT","DPA_TERMS","ADMIN_DOC","SECURITY_DOC","PRICING_DOC","SERVICE_DOC","OFFICIAL_PRODUCT_DOC"}:d.append(f"evidence_sources[{i}].source_type")
  if o.get("status")!="REGISTERED":d.append(f"evidence_sources[{i}].status")
 for i,o in enumerate(x.get("options",[])):
  for r in o.get("evidence_refs",[]):
   if r not in ids["evidence_sources"]:d.append(f"options[{i}].evidence_ref:{r}")
  if o.get("status")!="ELIGIBLE":d.append(f"options[{i}].status")
 gate_by={}
 for i,o in enumerate(x.get("gates",[])):
  if o.get("option_ref") not in ids["options"]:d.append(f"gates[{i}].option_ref")
  for f in ("task_output","data_rights_security","identity_admin_audit","legal_contract","integration_continuity","exit_deletion"):
   if o.get(f)!="PASS":d.append(f"gates[{i}].{f}")
  for r in o.get("evidence_refs",[]):
   if r not in ids["evidence_sources"]:d.append(f"gates[{i}].evidence_ref:{r}")
  if o.get("critical") is not True or o.get("status")!="PASS":d.append(f"gates[{i}].critical_status")
  gate_by[o.get("option_ref")]=o.get("status")
 sc=x.get("scoring_contract",{});weights=sc.get("weights",{})
 if set(weights)!=CRIT or abs(sum(v for v in weights.values() if isinstance(v,(int,float)))-100)>1e-9:d.append("scoring_contract.weights")
 for i,o in enumerate(x.get("assessments",[])):
  ref=o.get("option_ref");scores=o.get("criterion_scores",{});refs=o.get("score_evidence",{})
  if ref not in ids["options"]:d.append(f"assessments[{i}].option_ref")
  if gate_by.get(ref)!="PASS":d.append(f"assessments[{i}].gate_before_score")
  if set(scores)!=CRIT or set(refs)!=CRIT:d.append(f"assessments[{i}].criteria")
  total=0
  for c in CRIT:
   s=scores.get(c)
   if not isinstance(s,(int,float)) or not 0<=s<=5:d.append(f"assessments[{i}].score:{c}")
   else:total+=s*weights.get(c,0)/5
   for r in refs.get(c,[]) if isinstance(refs.get(c),list) else []:
    if r not in ids["evidence_sources"]:d.append(f"assessments[{i}].score_evidence:{r}")
  if isinstance(o.get("weighted_score"),(int,float)) and abs(o.get("weighted_score")-total)>.01:d.append(f"assessments[{i}].weighted_score")
  if o.get("status")!="PROPOSED":d.append(f"assessments[{i}].status")
 for g in ("tco_models","pilot_tests","exit_plans"):
  for i,o in enumerate(x.get(g,[])):
   if o.get("option_ref") not in ids["options"]:d.append(f"{g}[{i}].option_ref")
 for i,o in enumerate(x.get("pilot_tests",[])):
  if o.get("status")!="PASS":d.append(f"pilot_tests[{i}].status")
 valid=set().union(*ids.values())
 for g in ("decisions","test_cases"):
  for i,o in enumerate(x.get(g,[])):
   refs=o.get("evidence_refs",[]) if g=="decisions" else [o.get("requirement_ref")]
   for r in refs:
    if r not in valid:d.append(f"{g}[{i}].reference:{r}")
 risk_ids={o.get("id") for o in x.get("risks",[]) if isinstance(o,dict)}
 for r in RISKS-risk_ids:d.append(f"missing_risk:{r}")
 passed={o.get("id") for o in x.get("tests",[]) if o.get("status")=="PASS" and not blank(o.get("evidence"))}
 for t in TESTS-passed:d.append(f"test_not_passed:{t}")
 reviewed={o.get("id") for o in x.get("reviews",[]) if o.get("status")=="PASS" and not blank(o.get("evidence"))};gaps=sorted(REVIEWS-reviewed);walk(x,"",d)
 state="READY_FOR_HUMAN_PLATFORM_DECISION" if not d and not gaps else "NOT_READY";counts={k:len(x.get(k,[])) if isinstance(x.get(k),list) else 0 for k in MIN};counts.update({"tests_passed":len(passed),"reviews_passed":len(reviewed)})
 print(json.dumps({"state":state,"defect_count":len(d),"review_gap_count":len(gaps),"counts":counts,"defects":d,"review_gaps":gaps},ensure_ascii=False,indent=2));return 0 if state.startswith("READY") else 1
if __name__=="__main__":sys.exit(main(sys.argv[1]))
