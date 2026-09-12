#!/usr/bin/env python3
"""Static evaluator for systems-integration v2.3 fixtures."""
from __future__ import annotations
import json, sys
from pathlib import Path

MIN={"systems":6,"interface_contracts":8,"data_mappings":8,"identity_controls":6,"flow_steps":10,"reliability_controls":8,"test_cases":12,"cutover_plans":4,"monitoring":4,"action_options":6,"risks":6,"decisions":6}
REQ={
 "systems":"id name role owner environment provider_version boundary data_class contract_ref capabilities quotas maintenance deprecation".split(),
 "interface_contracts":"id source_system target_system pattern locator version schema methods_events request response errors pagination rate_limit timeout compatibility owner evidence".split(),
 "data_mappings":"id interface_ref object_field source_semantics target_semantics source_type target_type keys unit timezone null_default enum transform validation owner lineage reconciliation".split(),
 "identity_controls":"id interface_ref identity auth_flow environment scopes rights approval sod trust_boundary secret_reference rotation revocation expiry audit owner".split(),
 "flow_steps":"id interface_ref order state_from trigger input actor action output acceptance state_to correlation idempotency delivery_claim evidence failure_route owner".split(),
 "reliability_controls":"id applies_to error_class retryable attempts backoff timeout rate_response circuit_breaker queue_dlq replay manual_fallback compensation reconciliation owner".split(),
 "test_cases":"id category requirement_ref fixture expected actual evidence status owner".split(),
 "cutover_plans":"id environment scope entry success kill freeze_backfill parallel_run support rollback manual_continuity communication lifecycle approver status".split(),
 "monitoring":"id metric formula denominator window threshold_basis owner alert runbook evidence".split(),
 "action_options":"id signal_ref option authority approval rollback verification status".split(),
 "risks":"id risk evidence impact control owner residual status".split(),
 "decisions":"id decision options evidence_refs owner due status".split(),
}
TESTS={"mandate_system_ownership","contracts_semantics","identity_authorization","delivery_consistency","security_audit","tests_reconciliation","cutover_lifecycle"}
REVIEWS={"BUSINESS_PROCESS_OWNER","SYSTEM_DATA_OWNERS","SECURITY_PRIVACY_IAM","INTEGRATION_ENGINEERING_ARCHITECTURE","OPERATIONS_SRE_SUPPORT","RISK_COMPLIANCE_CHANGE"}
RISKS={"BUSINESS_SCOPE_SYSTEM_OWNERSHIP","DATA_SEMANTICS_LINEAGE_QUALITY","IDENTITY_AUTHORIZATION_SECRETS","DELIVERY_RELIABILITY_CONSISTENCY","SECURITY_PRIVACY_COMPLIANCE","CUTOVER_OPERATIONS_CONNECTOR_LIFECYCLE"}
FORBIDDEN_TRUE={"invented_endpoint","invented_schema","invented_event","invented_result","evidence_mutated","secret_exposed","production_data_used","permissions_changed","credential_created","connector_activated","production_connected","integration_deployed","data_migrated","external_published","notification_sent","actions_executed"}
FORBIDDEN_STATE={"AUTO_APPROVED","APPROVED_BY_AI","CONNECTED","ACTIVATED","DEPLOYED","LIVE","MIGRATED","PUBLISHED","ACTIONED","EXECUTED"}

def blank(v): return v is None or v=="" or v==[] or v=={}
def walk(v,path,defects):
    if isinstance(v,dict):
        for k,x in v.items():
            p=f"{path}.{k}" if path else k
            if k in FORBIDDEN_TRUE and x is True: defects.append(f"forbidden_true:{p}")
            if k in {"state","status","release_state"} and str(x).upper() in FORBIDDEN_STATE: defects.append(f"forbidden_state:{p}={x}")
            if any(s in k.lower() for s in ("secret_value","password","api_key","token_value")) and not blank(x): defects.append(f"secret_material:{p}")
            walk(x,p,defects)
    elif isinstance(v,list):
        for i,x in enumerate(v): walk(x,f"{path}[{i}]",defects)

def main(path):
    d=json.loads(Path(path).read_text(encoding="utf-8")); defects=[]
    if d.get("artifact")!="Governed Enterprise Systems Integration & Cutover Readiness Pack": defects.append("artifact_name")
    mandate=d.get("mandate",{})
    for f in "business_flow outcome objects system_owners source_systems target_systems sor_by_object environments baseline_volume slo_basis scope non_goals action_boundary success_criteria kill_criteria".split():
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
    for i,x in enumerate(d.get("interface_contracts",[])):
        if x.get("source_system") not in ids["systems"]: defects.append(f"interface_contracts[{i}].source_system")
        if x.get("target_system") not in ids["systems"]: defects.append(f"interface_contracts[{i}].target_system")
    for i,x in enumerate(d.get("data_mappings",[])):
        if x.get("interface_ref") not in ids["interface_contracts"]: defects.append(f"data_mappings[{i}].interface_ref")
    for i,x in enumerate(d.get("identity_controls",[])):
        if x.get("interface_ref") not in ids["interface_contracts"]: defects.append(f"identity_controls[{i}].interface_ref")
        if str(x.get("secret_reference","")).startswith("ref:") is False: defects.append(f"identity_controls[{i}].secret_reference")
        rights=x.get("rights",{})
        if not isinstance(rights,dict) or not all(k in rights for k in ("read","write","update","delete","send")): defects.append(f"identity_controls[{i}].rights_matrix")
        if str(x.get("scopes","")).lower() in {"*","all","admin"}: defects.append(f"identity_controls[{i}].excess_scope")
    for i,x in enumerate(d.get("flow_steps",[])):
        if x.get("interface_ref") not in ids["interface_contracts"]: defects.append(f"flow_steps[{i}].interface_ref")
        if str(x.get("delivery_claim","")).lower() in {"exactly once","guaranteed exactly once"}: defects.append(f"flow_steps[{i}].delivery_claim")
    valid=set().union(*ids.values())
    for i,x in enumerate(d.get("reliability_controls",[])):
        if x.get("applies_to") not in valid: defects.append(f"reliability_controls[{i}].applies_to")
        if x.get("retryable") is True and (not isinstance(x.get("attempts"),int) or x.get("attempts",0)<1 or x.get("attempts",0)>10): defects.append(f"reliability_controls[{i}].attempts")
    for i,x in enumerate(d.get("test_cases",[])):
        if x.get("requirement_ref") not in valid: defects.append(f"test_cases[{i}].requirement_ref")
        if str(x.get("status","")).upper() not in {"PASS","FAIL"}: defects.append(f"test_cases[{i}].status")
    for i,x in enumerate(d.get("action_options",[])):
        if x.get("signal_ref") not in ids["monitoring"]: defects.append(f"action_options[{i}].signal_ref")
        if str(x.get("status","")).upper()!="PENDING": defects.append(f"action_options[{i}].status")
    risk_ids={x.get("id") for x in d.get("risks",[]) if isinstance(x,dict)}
    for r in RISKS-risk_ids: defects.append(f"missing_risk:{r}")
    for i,x in enumerate(d.get("decisions",[])):
        if str(x.get("status","")).upper()!="PENDING": defects.append(f"decisions[{i}].status")
    tests=d.get("tests",[]); passed={x.get("id") for x in tests if x.get("status")=="PASS" and not blank(x.get("evidence"))}
    for x in TESTS-passed: defects.append(f"test_not_passed:{x}")
    reviews=d.get("reviews",[]); reviewed={x.get("id") for x in reviews if x.get("status")=="PASS" and not blank(x.get("evidence"))}
    gaps=sorted(REVIEWS-reviewed)
    walk(d,"",defects)
    state="READY_FOR_HUMAN_INTEGRATION_DECISION" if not defects and not gaps else "NOT_READY"
    counts={k:len(d.get(k,[])) if isinstance(d.get(k),list) else 0 for k in MIN};counts.update({"tests_passed":len(passed),"reviews_passed":len(reviewed)})
    out={"state":state,"defect_count":len(defects),"review_gap_count":len(gaps),"counts":counts,"defects":defects,"review_gaps":gaps}
    print(json.dumps(out,ensure_ascii=False,indent=2));return 0 if state.startswith("READY") else 1

if __name__=="__main__":
    if len(sys.argv)!=2: print("usage: evaluate_systems_integration.py fixture.json",file=sys.stderr);sys.exit(2)
    sys.exit(main(sys.argv[1]))
