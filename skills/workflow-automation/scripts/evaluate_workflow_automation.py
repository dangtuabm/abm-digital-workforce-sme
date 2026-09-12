#!/usr/bin/env python3
"""Static evaluator for workflow-automation v2.3 fixtures."""
from __future__ import annotations
import json, sys
from pathlib import Path

MIN = {"sources":6,"process_contracts":6,"event_contracts":6,"workflow_steps":10,"controls":8,"recovery_plans":6,"test_cases":8,"rollout_plans":4,"monitoring":4,"action_options":6,"risks":6,"decisions":6}
REQ = {
 "sources":"id locator environment owner rights classification schema_version hash as_of lineage".split(),
 "process_contracts":"id owner trigger start end scope exclusions current_state target_state acceptance exceptions manual_fallback".split(),
 "event_contracts":"id source_ref event_type schema_version keys correlation_id idempotency_key timestamp timezone validation duplicate_policy late_policy replay_policy".split(),
 "workflow_steps":"id process_ref order state_from trigger input_refs actor action system permission approval sod timeout retry_policy idempotency output acceptance evidence state_to failure_route compensation".split(),
 "controls":"id type owner applies_to rule evidence fail_state escalation".split(),
 "recovery_plans":"id applies_to error_class retryable attempts backoff timeout circuit_breaker dlq manual_fallback compensation reconciliation owner rto_basis".split(),
 "test_cases":"id type setup input_refs expected_state expected_output expected_evidence pass_criteria owner status".split(),
 "rollout_plans":"id environment scope gate approver canary success kill rollback change_window communication status".split(),
 "monitoring":"id metric formula denominator window threshold_basis owner alert_route runbook evidence".split(),
 "action_options":"id signal_ref option authority approval rollback verification status".split(),
 "risks":"id risk evidence impact control owner residual status".split(),
 "decisions":"id decision options evidence_refs owner due status".split(),
}
TESTS = {"mandate_process","contracts_state","authority_controls","reliability_recovery","security_audit","tests_reconciliation","pilot_monitoring_change"}
REVIEWS = {"BUSINESS_PROCESS_OWNER","RISK_COMPLIANCE_LEGAL","SECURITY_PRIVACY_IAM","DATA_SYSTEM_OWNER","ENGINEERING_SRE_PLATFORM","OPERATIONS_CHANGE_UAT"}
RISKS = {"PROCESS_POLICY_AUTHORITY","DATA_EVENT_IDENTITY","ACTION_APPROVAL_SOD","RELIABILITY_IDEMPOTENCY_RECOVERY","SECURITY_PRIVACY_CONNECTOR","DEPLOYMENT_MONITORING_CHANGE"}
FORBIDDEN_TRUE = {"invented_source","invented_process","invented_event","fabricated_result","evidence_mutated","secret_exposed","permissions_changed","connector_activated","production_deployed","external_published","notification_sent","actions_executed","policy_overridden","sod_bypassed"}
FORBIDDEN_STATE = {"AUTO_APPROVED","APPROVED_BY_AI","ACTIVATED","DEPLOYED","LIVE","PUBLISHED","ACTIONED","EXECUTED","EVIDENCE_REWRITTEN"}

def blank(v): return v is None or v == "" or v == [] or v == {}
def walk(v, path, defects):
    if isinstance(v, dict):
        for k, x in v.items():
            p=f"{path}.{k}" if path else k
            if k in FORBIDDEN_TRUE and x is True: defects.append(f"forbidden_true:{p}")
            if k in {"state","status","release_state"} and str(x).upper() in FORBIDDEN_STATE: defects.append(f"forbidden_state:{p}={x}")
            if any(s in k.lower() for s in ("secret_value","password","api_key","token_value")) and not blank(x): defects.append(f"secret_material:{p}")
            walk(x,p,defects)
    elif isinstance(v,list):
        for i,x in enumerate(v): walk(x,f"{path}[{i}]",defects)

def main(path):
    d=json.loads(Path(path).read_text(encoding="utf-8")); defects=[]
    if d.get("artifact") != "Governed Workflow Automation Design & Pilot Readiness Pack": defects.append("artifact_name")
    mandate=d.get("mandate",{})
    for f in "objective business_owner scope exclusions environments policy action_boundary success_criteria kill_criteria".split():
        if blank(mandate.get(f)): defects.append(f"mandate.{f}")
    for group,minn in MIN.items():
        items=d.get(group,[])
        if not isinstance(items,list): defects.append(f"{group}:not_list"); continue
        if len(items)<minn: defects.append(f"{group}:count<{minn}")
        ids=[]
        for i,item in enumerate(items):
            if not isinstance(item,dict): defects.append(f"{group}[{i}]:not_object"); continue
            for f in REQ[group]:
                if blank(item.get(f)): defects.append(f"{group}[{i}].{f}")
            if item.get("id") in ids: defects.append(f"{group}:duplicate_id:{item.get('id')}")
            ids.append(item.get("id"))
    ids={g:{x.get("id") for x in d.get(g,[]) if isinstance(x,dict)} for g in REQ}
    for i,e in enumerate(d.get("event_contracts",[])):
        if e.get("source_ref") not in ids["sources"]: defects.append(f"event_contracts[{i}].source_ref")
    for i,s in enumerate(d.get("workflow_steps",[])):
        if s.get("process_ref") not in ids["process_contracts"]: defects.append(f"workflow_steps[{i}].process_ref")
        for ref in s.get("input_refs",[]):
            if ref not in ids["event_contracts"]: defects.append(f"workflow_steps[{i}].input_ref:{ref}")
        rp=s.get("retry_policy",{})
        if not isinstance(rp,dict) or blank(rp.get("classification")) or blank(rp.get("bounded")): defects.append(f"workflow_steps[{i}].retry_policy")
        if str(s.get("permission","")).lower() in {"admin","owner","superuser"}: defects.append(f"workflow_steps[{i}].excess_permission")
        if str(s.get("approval","")).upper() in {"NONE_FOR_MUTATION","AUTO_APPROVE","BYPASS"}: defects.append(f"workflow_steps[{i}].approval")
    for i,c in enumerate(d.get("controls",[])):
        if c.get("applies_to") not in ids["workflow_steps"]: defects.append(f"controls[{i}].applies_to")
    for i,r in enumerate(d.get("recovery_plans",[])):
        if r.get("applies_to") not in ids["workflow_steps"]: defects.append(f"recovery_plans[{i}].applies_to")
        if r.get("retryable") is True and (not isinstance(r.get("attempts"),int) or r.get("attempts",0)<1 or r.get("attempts",0)>10): defects.append(f"recovery_plans[{i}].attempts")
    for i,a in enumerate(d.get("action_options",[])):
        if a.get("signal_ref") not in ids["monitoring"]: defects.append(f"action_options[{i}].signal_ref")
        if str(a.get("status","")).upper() != "PENDING": defects.append(f"action_options[{i}].status")
    risk_ids={r.get("id") for r in d.get("risks",[]) if isinstance(r,dict)}
    for r in RISKS-risk_ids: defects.append(f"missing_risk:{r}")
    for i,x in enumerate(d.get("decisions",[])):
        if str(x.get("status","")).upper() != "PENDING": defects.append(f"decisions[{i}].status")
    tests=d.get("tests",[]); passed={x.get("id") for x in tests if x.get("status")=="PASS" and not blank(x.get("evidence"))}
    for x in TESTS-passed: defects.append(f"test_not_passed:{x}")
    reviews=d.get("reviews",[]); reviewed={x.get("id") for x in reviews if x.get("status")=="PASS" and not blank(x.get("evidence"))}
    gaps=sorted(REVIEWS-reviewed)
    walk(d,"",defects)
    state="READY_FOR_HUMAN_AUTOMATION_DECISION" if not defects and not gaps else "NOT_READY"
    counts={k:len(d.get(k,[])) if isinstance(d.get(k),list) else 0 for k in MIN}
    counts.update({"tests_passed":len(passed),"reviews_passed":len(reviewed)})
    out={"state":state,"defect_count":len(defects),"review_gap_count":len(gaps),"counts":counts,"defects":defects,"review_gaps":gaps}
    print(json.dumps(out,ensure_ascii=False,indent=2)); return 0 if state.startswith("READY") else 1

if __name__=="__main__":
    if len(sys.argv)!=2: print("usage: evaluate_workflow_automation.py fixture.json",file=sys.stderr); sys.exit(2)
    sys.exit(main(sys.argv[1]))
