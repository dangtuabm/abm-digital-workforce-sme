#!/usr/bin/env python3
import json, sys
from pathlib import Path

TESTS = {"mandate_entity","source_claim","organization_job","buying_context","signal_hypothesis","privacy_fairness","decision_boundary"}
CLAIM_TYPES = {"FACT","ESTIMATE","HYPOTHESIS","UNKNOWN"}
AUTHORITY = {"VERIFIED","HYPOTHESIS","UNKNOWN"}
RISK_TYPES = {"PRIVACY_SENSITIVITY","FAIRNESS_HIGH_IMPACT","LEGAL_TERMS","SECURITY_REPUTATION"}
REVIEWERS = {"DOMAIN_ENTITY","DATA_PRIVACY","COMMERCIAL_USE"}
SECTIONS = {"entity_card","source_claim_ledger","organization_snapshot","jobs_alternatives","buying_group_process","signals_hypotheses_gaps","privacy_reviews_audit","refresh_human_use_decision"}
FORBIDDEN_FLAGS = {
    "entity_merged_without_evidence","source_fabricated","claim_fabricated","revenue_fabricated","headcount_fabricated",
    "market_share_fabricated","kpi_fabricated","pain_fabricated","intent_fabricated","budget_fabricated","timeline_fabricated",
    "authority_fabricated","relationship_fabricated","public_equals_consent","rights_bypassed","private_contact_enriched",
    "protected_trait_inferred","sensitive_trait_inferred","psychology_inferred","disc_inferred","personal_life_profiled",
    "vulnerability_manipulated","discriminatory_eligibility","illegal_surveillance","contradiction_hidden","stale_source_hidden",
    "auto_scored","auto_targeted","auto_personalized","auto_contacted","auto_enriched","auto_disqualified"
}
FORBIDDEN_STATES = {"SCORED","TARGETED","PERSONALIZED","CONTACTED","ENRICHED","DISQUALIFIED","APPROVED"}

def present(v): return v not in (None,"",[],{})
def add(ds,msg): ds.add(msg)

def evaluate(d):
    defects=set(); gaps=set()
    m=d.get("mandate",{})
    for f in ("purpose","target","as_of","users","decision_owner","prohibited_uses","retention","required_reviews"):
        if not present(m.get(f)): add(defects,f"mandate:missing_{f}")

    entities=d.get("entities",[]); entity_ids=set()
    for i,e in enumerate(entities):
        eid=e.get("id",f"index-{i}"); entity_ids.add(eid)
        if not present(e.get("name")): add(defects,f"entity:{eid}:missing_name")
        if len(e.get("stable_keys",[]))<2: add(defects,f"entity:{eid}:insufficient_stable_keys")
        for f in ("geography","confidence","ambiguity_status"):
            if not present(e.get(f)): add(defects,f"entity:{eid}:missing_{f}")
    if not entities: add(defects,"entities:missing")

    sources=d.get("sources",[]); source_ids=set()
    for i,s in enumerate(sources):
        sid=s.get("id",f"index-{i}"); source_ids.add(sid)
        for f in ("locator","version","date","rights","freshness","source_type","confidence","subject"):
            if not present(s.get(f)): add(defects,f"source:{sid}:missing_{f}")
        if s.get("rights") not in ("AUTHORIZED","PUBLIC_TERMS_OK","INTERNAL_AUTHORIZED"):
            add(defects,f"source:{sid}:not_authorized")
    if not sources: add(defects,"sources:missing")

    claims=d.get("claims",[])
    for i,c in enumerate(claims):
        cid=c.get("id",f"index-{i}"); ctype=c.get("claim_type")
        if c.get("entity_id") not in entity_ids: add(defects,f"claim:{cid}:unknown_entity")
        if ctype not in CLAIM_TYPES: add(defects,f"claim:{cid}:invalid_type")
        for f in ("statement","confidence","as_of"):
            if not present(c.get(f)): add(defects,f"claim:{cid}:missing_{f}")
        refs=c.get("source_ids",[])
        if ctype in ("FACT","ESTIMATE") and not refs: add(defects,f"claim:{cid}:missing_source")
        for ref in refs:
            if ref not in source_ids: add(defects,f"claim:{cid}:unknown_source:{ref}")
        if ctype=="ESTIMATE" and (not present(c.get("method")) or not present(c.get("range"))):
            add(defects,f"claim:{cid}:estimate_missing_method_range")
        if c.get("conflict") and not present(c.get("conflict_note")): add(defects,f"claim:{cid}:hidden_conflict")
    if not claims: add(defects,"claims:missing")

    for i,o in enumerate(d.get("organization_context",[])):
        oid=o.get("entity_id",f"index-{i}")
        if oid not in entity_ids: add(defects,f"organization:{oid}:unknown_entity")
        for f in ("business_model","offerings","geography","scale_range","lifecycle","evidence_ids"):
            if not present(o.get(f)): add(defects,f"organization:{oid}:missing_{f}")
        for ref in o.get("evidence_ids",[]):
            if ref not in source_ids: add(defects,f"organization:{oid}:unknown_source:{ref}")

    jobs=d.get("jobs",[])
    for i,j in enumerate(jobs):
        jid=j.get("id",f"index-{i}")
        if j.get("entity_id") not in entity_ids: add(defects,f"job:{jid}:unknown_entity")
        for f in ("statement","desired_outcome","current_alternative","evidence_ids","confidence","status"):
            if not present(j.get(f)): add(defects,f"job:{jid}:missing_{f}")
        for ref in j.get("evidence_ids",[]):
            if ref not in source_ids: add(defects,f"job:{jid}:unknown_source:{ref}")
        if j.get("status") not in ("VERIFIED","HYPOTHESIS","UNKNOWN"): add(defects,f"job:{jid}:invalid_status")
    if not jobs: add(defects,"jobs:missing")

    roles=d.get("buying_roles",[])
    for i,r in enumerate(roles):
        rid=r.get("role",f"index-{i}")
        for f in ("responsibility","authority_status","evidence_ids","unknown_question"):
            if not present(r.get(f)): add(defects,f"role:{rid}:missing_{f}")
        if r.get("authority_status") not in AUTHORITY: add(defects,f"role:{rid}:invalid_authority")
        for ref in r.get("evidence_ids",[]):
            if ref not in source_ids: add(defects,f"role:{rid}:unknown_source:{ref}")
    if not roles: add(defects,"buying_roles:missing")

    process=d.get("buying_process",{})
    for f in ("trigger_status","stage_status","criteria","approval_path","procurement_path","security_legal_path","budget_status","timeline_status","evidence_gaps"):
        if not present(process.get(f)): add(defects,f"buying_process:missing_{f}")

    signals=d.get("signals",[])
    for i,s in enumerate(signals):
        sid=s.get("id",f"index-{i}")
        for f in ("observed_event","date","source_ids","alternative_explanations","confidence"):
            if not present(s.get(f)): add(defects,f"signal:{sid}:missing_{f}")
        for ref in s.get("source_ids",[]):
            if ref not in source_ids: add(defects,f"signal:{sid}:unknown_source:{ref}")
    hypotheses=d.get("hypotheses",[])
    for i,h in enumerate(hypotheses):
        hid=h.get("id",f"index-{i}")
        for f in ("claim","evidence_for","evidence_against","confidence","impact","question_test","owner","expiry"):
            if not present(h.get(f)): add(defects,f"hypothesis:{hid}:missing_{f}")
    if not hypotheses: add(defects,"hypotheses:missing")

    risks=d.get("risks",[]); seen=set()
    for i,r in enumerate(risks):
        typ=r.get("risk_type",f"index-{i}"); seen.add(typ)
        for f in ("statement","trigger","mitigation","owner","status"):
            if not present(r.get(f)): add(defects,f"risk:{typ}:missing_{f}")
    for typ in RISK_TYPES-seen: add(defects,f"risks:missing_type:{typ}")

    missing=SECTIONS-set(d.get("output_sections",[]))
    if missing: add(defects,"output_sections:missing:"+",".join(sorted(missing)))
    tests=d.get("tests",{})
    for t in TESTS:
        if tests.get(t)!="PASS": add(defects,f"test:{t}:not_pass")
    reviews=d.get("reviews",{})
    for r in REVIEWERS:
        if reviews.get(r)!="PASS": gaps.add(f"review:{r}:not_pass")
    if reviews.get("FINAL_HUMAN_CUSTOMER_USE_DECISION")!="PENDING": add(defects,"review:FINAL_HUMAN_CUSTOMER_USE_DECISION:must_be_pending")
    for flag in sorted(set(d.get("forbidden_flags",[])) & FORBIDDEN_FLAGS): add(defects,f"forbidden_flag:{flag}")
    states=set(d.get("forbidden_states",[])); states.add(d.get("published_state","DRAFT"))
    for state in sorted(states & FORBIDDEN_STATES): add(defects,f"forbidden_state:{state}")
    ready=not defects and not gaps
    return {
      "skill":"customer-profile","state":"READY_FOR_HUMAN_CUSTOMER_USE_DECISION" if ready else "NOT_READY",
      "defect_count":len(defects),"defects":sorted(defects),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),
      "counts":{"entities":len(entities),"sources":len(sources),"claims":len(claims),"jobs":len(jobs),"roles":len(roles),"signals":len(signals),"hypotheses":len(hypotheses),"risks":len(risks),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(reviews.get(x)=="PASS" for x in REVIEWERS)},
      "warning":"STATIC PASS does not prove D10 entity accuracy, customer truth, privacy compliance, profile usefulness, token cost, duration, adoption, or business impact."
    }

def main():
    if len(sys.argv)!=2:
        print("usage: evaluate_customer_profile.py INPUT.json",file=sys.stderr); return 2
    result=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")))
    print(json.dumps(result,ensure_ascii=False,indent=2)); return 0 if result["state"]!="NOT_READY" else 1

if __name__=="__main__": raise SystemExit(main())
