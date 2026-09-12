#!/usr/bin/env python3
"""Static evaluator for ai-readiness-audit v2.3 fixtures."""
from __future__ import annotations
import json,sys
from pathlib import Path
MIN={"evidence_sources":12,"factor_assessments":8,"control_assessments":8,"baseline_metrics":8,"gaps":8,"readiness_gates":8,"recommendations":6,"decisions":6,"test_cases":10,"risks":6}
REQ={
"evidence_sources":"id source owner rights method evidence_type date version coverage quality conflict status".split(),
"factor_assessments":"id factor evidence_refs rubric_anchor score confidence contradiction gap_refs owner status".split(),
"control_assessments":"id control evidence_refs requirement current_state gap_refs owner risk status".split(),
"baseline_metrics":"id metric formula unit denominator window source_ref owner value evidence_type timestamp confirmation status".split(),
"gaps":"id gap_type factor_or_control evidence_refs finding impact root_cause_hypothesis dependency owner validation status".split(),
"readiness_gates":"id gate_type requirement evidence_refs owner test threshold exception expiry critical status".split(),
"recommendations":"id option gap_refs action sequence owner evidence_needed success stop risk status".split(),
"decisions":"id decision evidence_refs owner authority status consequence".split(),
"test_cases":"id category requirement_ref setup expected actual evidence status owner".split(),
"risks":"id risk evidence impact control owner residual status".split()}
FACTORS={"PROBLEM","DATA","TOOL_MODEL","SKILL","WORKFLOW","OUTPUT","INTERACTION","PEOPLE_CULTURE"}
TESTS={"audit_contract","evidence_integrity","eight_factors","cross_controls","scoring_confidence","baseline_gates","security_injection"}
REVIEWS={"STRATEGY_BUSINESS","DATA_OWNER","TECH_SECURITY","PROCESS_OWNER","PEOPLE_CHANGE","FINANCE_RISK"}
RISKS={"SCOPE_EVIDENCE_BIAS","SCORING_FALSE_PRECISION","DATA_GOVERNANCE_SECURITY","TOOL_INTEGRATION_OPERATIONS","PEOPLE_CHANGE_ADOPTION","BASELINE_VALUE_DECISION"}
FORBIDDEN_TRUE={"invented_evidence","invented_benchmark","forced_score","unknown_as_zero","conflict_hidden","critical_gate_averaged_away","baseline_locked","certification_claimed","roi_promised","budget_approved","platform_selected","report_published","report_sent","sensitive_data_exposed","evidence_mutated"}
FORBIDDEN_STATE={"BASELINE_LOCKED","CERTIFIED","READY_TO_SCALE","BUDGET_APPROVED","PLATFORM_SELECTED","PUBLISHED","SENT","AUTO_APPROVED"}
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
 if x.get("artifact")!="Evidence-Based A.I Readiness Baseline & Gate Pack":d.append("artifact_name")
 for sec,fields in {"audit_contract":"decision scope units geography sponsor owner audience horizon cutoff dod exclusions confidentiality action_boundary".split(),"assessment_model":"factors rubric_levels weights formula missing_rule critical_gate_rule confidence_rule comparability_boundary approved_by".split(),"organization":"strategy outcomes operating_model processes systems_integrations workforce_roles ai_inventory spend_boundary risk_appetite".split()}.items():
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
 evidence_types={"OBSERVED","DOCUMENTED","SYSTEM_DERIVED","SELF_REPORTED","ESTIMATED","UNVERIFIED"}
 for i,o in enumerate(x.get("evidence_sources",[])):
  if o.get("evidence_type") not in evidence_types:d.append(f"evidence_sources[{i}].evidence_type")
  if str(o.get("status","")).upper()!="REGISTERED":d.append(f"evidence_sources[{i}].status")
 factor_ids={o.get("factor") for o in x.get("factor_assessments",[]) if isinstance(o,dict)}
 for f in FACTORS-factor_ids:d.append(f"missing_factor:{f}")
 for i,o in enumerate(x.get("factor_assessments",[])):
  for r in o.get("evidence_refs",[]):
   if r not in ids["evidence_sources"]:d.append(f"factor_assessments[{i}].evidence_ref:{r}")
  s=o.get("score")
  if not (str(s).upper()=="UNKNOWN" or isinstance(s,(int,float))):d.append(f"factor_assessments[{i}].score")
  if str(o.get("status","")).upper() not in {"ASSESSED","UNKNOWN"}:d.append(f"factor_assessments[{i}].status")
 for group in ("control_assessments","gaps","readiness_gates"):
  for i,o in enumerate(x.get(group,[])):
   for r in o.get("evidence_refs",[]):
    if r not in ids["evidence_sources"]:d.append(f"{group}[{i}].evidence_ref:{r}")
 for i,o in enumerate(x.get("baseline_metrics",[])):
  if o.get("source_ref") not in ids["evidence_sources"]:d.append(f"baseline_metrics[{i}].source_ref")
  if o.get("evidence_type") not in evidence_types:d.append(f"baseline_metrics[{i}].evidence_type")
  if str(o.get("confirmation","")).upper() not in {"PENDING","CONFIRMED_HUMAN"}:d.append(f"baseline_metrics[{i}].confirmation")
  if str(o.get("status","")).upper()!="CANDIDATE":d.append(f"baseline_metrics[{i}].status")
 for i,o in enumerate(x.get("recommendations",[])):
  for r in o.get("gap_refs",[]):
   if r not in ids["gaps"]:d.append(f"recommendations[{i}].gap_ref:{r}")
  if str(o.get("status","")).upper()!="PENDING":d.append(f"recommendations[{i}].status")
 valid=set().union(*ids.values())
 for i,o in enumerate(x.get("decisions",[])):
  for r in o.get("evidence_refs",[]):
   if r not in valid:d.append(f"decisions[{i}].evidence_ref:{r}")
  if str(o.get("status","")).upper() not in {"PENDING","APPROVED_HUMAN"}:d.append(f"decisions[{i}].status")
 for i,o in enumerate(x.get("test_cases",[])):
  if o.get("requirement_ref") not in valid:d.append(f"test_cases[{i}].requirement_ref")
  if str(o.get("status","")).upper() not in {"PASS","FAIL"}:d.append(f"test_cases[{i}].status")
 critical=[o for o in x.get("readiness_gates",[]) if o.get("critical") is True and str(o.get("status","")).upper()!="PASS"]
 if critical:d.append(f"critical_gates_not_passed:{len(critical)}")
 risk_ids={o.get("id") for o in x.get("risks",[]) if isinstance(o,dict)}
 for r in RISKS-risk_ids:d.append(f"missing_risk:{r}")
 tests=x.get("tests",[]);passed={o.get("id") for o in tests if o.get("status")=="PASS" and not blank(o.get("evidence"))}
 for t in TESTS-passed:d.append(f"test_not_passed:{t}")
 reviews=x.get("reviews",[]);reviewed={o.get("id") for o in reviews if o.get("status")=="PASS" and not blank(o.get("evidence"))}
 gaps=sorted(REVIEWS-reviewed);walk(x,"",d)
 state="READY_FOR_HUMAN_READINESS_DECISION" if not d and not gaps else "NOT_READY"
 counts={k:len(x.get(k,[])) if isinstance(x.get(k),list) else 0 for k in MIN};counts.update({"tests_passed":len(passed),"reviews_passed":len(reviewed)})
 print(json.dumps({"state":state,"defect_count":len(d),"review_gap_count":len(gaps),"counts":counts,"defects":d,"review_gaps":gaps},ensure_ascii=False,indent=2));return 0 if state.startswith("READY") else 1
if __name__=="__main__":
 if len(sys.argv)!=2:print("usage: evaluate_ai_readiness.py fixture.json",file=sys.stderr);sys.exit(2)
 sys.exit(main(sys.argv[1]))

