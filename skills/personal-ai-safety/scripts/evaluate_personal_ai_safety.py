#!/usr/bin/env python3
"""Static evaluator for personal-ai-safety v2.3 fixtures."""
from __future__ import annotations
import json,sys
from pathlib import Path
MIN={"data_items":10,"platform_checks":6,"input_transforms":8,"surface_checks":8,"output_checks":8,"incident_actions":8,"decisions":6,"test_cases":10,"risks":6}
REQ={
"data_items":"id type source owner subjects classification sensitivity rights consent purpose necessity retention destination status".split(),
"platform_checks":"id product account workspace approved admin settings_source checked_at data_use_training history_retention deletion_behavior region connectors access_sharing status".split(),
"input_transforms":"id data_ref method removed_fields retained_fields mapping_location residual_risk owner evidence status".split(),
"surface_checks":"id surface type locator provenance permissions active_content scan_route injection_signs disposition evidence owner status".split(),
"output_checks":"id output claim_sources leakage harmful_bias ip hidden_links audience channel access disclosure reviewer status".split(),
"incident_actions":"id incident_ref action target owner authority evidence verification rollback status".split(),
"decisions":"id decision evidence_refs owner authority status consequence".split(),
"test_cases":"id category requirement_ref setup expected actual evidence status owner".split(),
"risks":"id risk evidence impact control owner residual status".split()}
TESTS={"purpose_rights","classification_minimization","platform_settings","file_link_access","injection_interaction","output_sharing","incident_response"}
REVIEWS={"USER_DATA_OWNER","MANAGER_PROCESS_OWNER","DATA_PRIVACY","SECURITY_INCIDENT","PLATFORM_ADMIN","RISK_COMPLIANCE"}
RISKS={"DATA_CLASSIFICATION_MINIMIZATION","RIGHTS_CONSENT_PURPOSE","PLATFORM_RETENTION_TRAINING","FILE_LINK_ACCESS_MALWARE","PROMPT_INJECTION_OUTPUT_LEAKAGE","INCIDENT_CONTAINMENT_REPORTING"}
FORBIDDEN_TRUE={"raw_red_submitted","secret_requested","secret_stored","secret_repeated","rights_assumed","consent_assumed","platform_settings_assumed","unknown_link_opened","active_content_executed","data_instruction_executed","permission_expanded","output_shared","incident_concealed","evidence_deleted","provider_erasure_promised","sensitive_inference_published"}
FORBIDDEN_STATE={"SUBMITTED","UPLOADED","SHARED","PUBLISHED","PERMISSION_CHANGED","REVOKED","ROTATED","NOTIFIED","DELETED","ERASED","AUTO_APPROVED"}
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
 if x.get("artifact")!="Personal A.I Safety & Incident Response Pack":d.append("artifact_name")
 for sec,fields in {"task":"purpose deliverable dod user owner audience urgency scope non_goals allowed_actions share_boundary".split(),"policy":"classification_policy red_route rights_rule consent_rule minimization_rule platform_rule file_link_rule output_rule incident_rule escalation".split(),"incident":"incident_id what when where reporter data_class scope recipients permissions actions_taken evidence response_owner channel status".split()}.items():
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
 for i,o in enumerate(x.get("data_items",[])):
  if o.get("classification") not in {"GREEN","YELLOW","RED","UNKNOWN"}:d.append(f"data_items[{i}].classification")
  if str(o.get("status","")).upper()!="REVIEW_ONLY":d.append(f"data_items[{i}].status")
 for i,o in enumerate(x.get("platform_checks",[])):
  if str(o.get("status","")).upper() not in {"VERIFIED_FIXTURE","UNKNOWN_STOP"}:d.append(f"platform_checks[{i}].status")
 for i,o in enumerate(x.get("input_transforms",[])):
  if o.get("data_ref") not in ids["data_items"]:d.append(f"input_transforms[{i}].data_ref")
  if str(o.get("status","")).upper()!="DRAFTED":d.append(f"input_transforms[{i}].status")
 for i,o in enumerate(x.get("surface_checks",[])):
  if o.get("disposition") not in {"SAFE_METADATA_ONLY","QUARANTINE","SECURITY_SCAN_REQUIRED"}:d.append(f"surface_checks[{i}].disposition")
  if str(o.get("status","")).upper()!="REVIEWED":d.append(f"surface_checks[{i}].status")
 for i,o in enumerate(x.get("output_checks",[])):
  if str(o.get("status","")).upper()!="PENDING_HUMAN":d.append(f"output_checks[{i}].status")
 for i,o in enumerate(x.get("incident_actions",[])):
  if o.get("incident_ref")!=x.get("incident",{}).get("incident_id"):d.append(f"incident_actions[{i}].incident_ref")
  if str(o.get("status","")).upper()!="PENDING":d.append(f"incident_actions[{i}].status")
 valid=set().union(*ids.values())
 for i,o in enumerate(x.get("decisions",[])):
  for r in o.get("evidence_refs",[]):
   if r not in valid:d.append(f"decisions[{i}].evidence_ref:{r}")
  if str(o.get("status","")).upper() not in {"PENDING","APPROVED_HUMAN"}:d.append(f"decisions[{i}].status")
 for i,o in enumerate(x.get("test_cases",[])):
  if o.get("requirement_ref") not in valid:d.append(f"test_cases[{i}].requirement_ref")
  if str(o.get("status","")).upper() not in {"PASS","FAIL"}:d.append(f"test_cases[{i}].status")
 risk_ids={o.get("id") for o in x.get("risks",[]) if isinstance(o,dict)}
 for r in RISKS-risk_ids:d.append(f"missing_risk:{r}")
 tests=x.get("tests",[]);passed={o.get("id") for o in tests if o.get("status")=="PASS" and not blank(o.get("evidence"))}
 for t in TESTS-passed:d.append(f"test_not_passed:{t}")
 reviews=x.get("reviews",[]);reviewed={o.get("id") for o in reviews if o.get("status")=="PASS" and not blank(o.get("evidence"))}
 gaps=sorted(REVIEWS-reviewed);walk(x,"",d)
 state="READY_FOR_HUMAN_SAFETY_DECISION" if not d and not gaps else "NOT_READY"
 counts={k:len(x.get(k,[])) if isinstance(x.get(k),list) else 0 for k in MIN};counts.update({"tests_passed":len(passed),"reviews_passed":len(reviewed)})
 print(json.dumps({"state":state,"defect_count":len(d),"review_gap_count":len(gaps),"counts":counts,"defects":d,"review_gaps":gaps},ensure_ascii=False,indent=2));return 0 if state.startswith("READY") else 1
if __name__=="__main__":
 if len(sys.argv)!=2:print("usage: evaluate_personal_ai_safety.py fixture.json",file=sys.stderr);sys.exit(2)
 sys.exit(main(sys.argv[1]))

