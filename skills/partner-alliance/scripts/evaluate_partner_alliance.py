#!/usr/bin/env python3
import json,sys
from pathlib import Path
TESTS={"mandate_sources","counterparty_fit","due_diligence_red_flags","value_operating_economics","data_ip_brand_ethics","pilot_governance_exit","decision_boundary"}
REVIEWS={"STRATEGY_CUSTOMER","FINANCE_COMMERCIAL","LEGAL_COMPETITION_ETHICS","DATA_SECURITY_PRIVACY","IP_BRAND_REPUTATION","DELIVERY_OPERATIONS"}
DD_DOMAINS={"STRATEGY_CUSTOMER_FIT","FINANCE_SOLVENCY_TAX","LEGAL_COMPLIANCE_COMPETITION_ANTI_BRIBERY","DATA_SECURITY_PRIVACY","IP_BRAND_REPUTATION","DELIVERY_QUALITY_CAPACITY"}
RISK_TYPES={"STRATEGIC_VALUE","COUNTERPARTY_DUE_DILIGENCE","DELIVERY_CUSTOMER_HARM","FINANCIAL_COMMERCIAL","LEGAL_COMPETITION_ETHICS","DATA_IP_BRAND_SECURITY"}
SECTIONS={"document_control","counterparty_source_ledger","fit_value_contribution","due_diligence_red_flags","options_operating_economics","data_ip_brand_pilot","governance_conflict_exit","decisions_reviews_audit"}
RECOMMENDATIONS={"SCREEN","VALIDATE","PILOT_REVIEW","NEGOTIATE_REVIEW","SCALE_REVIEW","HOLD","EXIT_REVIEW"}
FORBIDDEN_FLAGS={"partner_identity_fabricated","ownership_fabricated","authority_fabricated","capability_fabricated","customer_list_fabricated","audience_fabricated","track_record_fabricated","contribution_fabricated","customer_value_fabricated","economics_fabricated","commission_fabricated","revenue_share_fabricated","cost_fabricated","margin_fabricated","due_diligence_bypassed","critical_red_flag_averaged","conflict_hidden","bribery_kickback","price_fixing","market_allocation","customer_allocation","bid_rigging","coordinated_exclusion","sanctions_evasion","confidential_competitor_info_used","customer_data_shared_unlawfully","consent_bypassed","retention_bypassed","security_bypassed","ip_misused","brand_misused","misleading_endorsement","exclusivity_fabricated","attribution_gamed","dispute_hidden","pilot_result_fabricated","review_bypassed","auto_outreach","auto_data_shared","auto_offered","auto_exclusivity_promised","auto_negotiated","auto_paid","auto_signed","auto_activated","auto_announced"}
FORBIDDEN_STATES={"OUTREACH_SENT","DATA_SHARED","OFFER_MADE","EXCLUSIVITY_PROMISED","NEGOTIATED","PAYMENT_MADE","AGREEMENT_SIGNED","ALLIANCE_ACTIVATED","PUBLICLY_ANNOUNCED"}
RIGHTS={"AUTHORIZED","INTERNAL_AUTHORIZED","COUNTERPARTY_AUTHORIZED","CUSTOMER_AUTHORIZED","PUBLIC_TERMS_OK"}
def ok(v):return v not in(None,"",[],{})
def evaluate(d):
 ds=set();gaps=set();m=d.get("mandate",{})
 for f in("alliance_type_scope","purpose","strategy_customer_outcome","geography_segment","as_of","horizon","owner","budget_capacity","decision_authority","commercial_authority","legal_authority","confidentiality","required_reviews"):
  if not ok(m.get(f)):ds.add(f"mandate:missing_{f}")
 sources=d.get("sources",[]);sids=set()
 for i,s in enumerate(sources):
  sid=s.get("id",f"index-{i}");sids.add(sid)
  for f in("source_type","locator","version","date","rights_purpose","freshness","confidence","subject"):
   if not ok(s.get(f)):ds.add(f"source:{sid}:missing_{f}")
  if s.get("rights_purpose") not in RIGHTS:ds.add(f"source:{sid}:not_authorized")
 partners=d.get("partners",[]);pids=set()
 for i,p in enumerate(partners):
  pid=p.get("id",f"index-{i}");pids.add(pid)
  for f in("legal_entity","ownership_control","authorized_contacts","capabilities_assets_channels","customer_fit","track_record","contribution","source_ids","confidence","gaps","status"):
   if not ok(p.get(f)):ds.add(f"partner:{pid}:missing_{f}")
  for ref in p.get("source_ids",[]):
   if ref not in sids:ds.add(f"partner:{pid}:unknown_source:{ref}")
 if len(pids)!=len(partners):ds.add("partners:duplicate_id")
 dd=d.get("due_diligence",[]);seen=set()
 for i,x in enumerate(dd):
  dom=x.get("domain",f"index-{i}");seen.add(dom)
  for f in("partner_ids","finding","source_ids","severity","confidence","gap","mitigation","owner","gate"):
   if not ok(x.get(f)):ds.add(f"diligence:{dom}:missing_{f}")
  for pid in x.get("partner_ids",[]):
   if pid not in pids:ds.add(f"diligence:{dom}:unknown_partner:{pid}")
  for ref in x.get("source_ids",[]):
   if ref not in sids:ds.add(f"diligence:{dom}:unknown_source:{ref}")
 for dom in DD_DOMAINS-seen:ds.add(f"diligence:missing_domain:{dom}")
 options=d.get("alliance_options",[]);oids=set()
 for i,x in enumerate(options):
  oid=x.get("id",f"index-{i}");oids.add(oid)
  for f in("partner_ids","model","reciprocal_value","customer_public_value","contributions","scope_tradeoffs","control_cost_liability","data_ip_brand_exposure","channel_conflict","reversibility_prerequisites","recommendation_status"):
   if not ok(x.get(f)):ds.add(f"option:{oid}:missing_{f}")
  for pid in x.get("partner_ids",[]):
   if pid not in pids:ds.add(f"option:{oid}:unknown_partner:{pid}")
 op=d.get("operating_model",{})
 for f in("in_scope","out_of_scope","roles_decision_rights","service_quality_acceptance","customer_lead_ownership","attribution_dispute","support_records","change_escalation","audit_continuity_exit"):
  if not ok(op.get(f)):ds.add(f"operating:missing_{f}")
 eco=d.get("economics",{})
 for f in("approved_rate_reference","currency_tax_basis","eligible_event","attribution_window","refund_clawback","cost_to_serve","contribution_margin_sensitivity","cash_timing","liability","decision_authority"):
  if not ok(eco.get(f)):ds.add(f"economics:missing_{f}")
 dib=d.get("data_ip_brand_ethics",{})
 for f in("data_purpose_consent","minimum_fields_access","security_incident","retention_deletion","preexisting_new_ip","license_exit","brand_publicity","competition_anti_bribery_conflicts"):
  if not ok(dib.get(f)):ds.add(f"data_ip_brand:missing_{f}")
 pilots=d.get("pilots",[]);pilotids=set()
 for i,x in enumerate(pilots):
  xid=x.get("id",f"index-{i}");pilotids.add(xid)
  for f in("partner_ids","hypothesis","bounded_scope_baseline","contribution_owner_capacity","success_criteria","stop_criteria","guardrails","evidence_review","rollback","human_state"):
   if not ok(x.get(f)):ds.add(f"pilot:{xid}:missing_{f}")
  for pid in x.get("partner_ids",[]):
   if pid not in pids:ds.add(f"pilot:{xid}:unknown_partner:{pid}")
  if x.get("human_state")!="PENDING":ds.add(f"pilot:{xid}:human_state_not_pending")
 gov=d.get("governance",{})
 for f in("kpi_contracts","decision_cadence","issue_conflict_register","renewal_change_triggers","exit_transition_customer_continuity","record_source"):
  if not ok(gov.get(f)):ds.add(f"governance:missing_{f}")
 risks=d.get("risks",[]);seenr=set()
 for i,r in enumerate(risks):
  typ=r.get("risk_type",f"index-{i}");seenr.add(typ)
  for f in("statement","likelihood","impact","trigger","mitigation","contingency","owner"):
   if not ok(r.get(f)):ds.add(f"risk:{typ}:missing_{f}")
 for typ in RISK_TYPES-seenr:ds.add(f"risks:missing_type:{typ}")
 decisions=d.get("decision_queue",[]);decided=set()
 for i,x in enumerate(decisions):
  pid=x.get("partner_id",f"index-{i}");decided.add(pid)
  if pid not in pids:ds.add(f"decision:unknown_partner:{pid}")
  for f in("recommendation","alternatives","evidence_source_ids","option_ids","pilot_ids","red_flags","decision_owner","needed_by","human_state"):
   if not ok(x.get(f)):ds.add(f"decision:{pid}:missing_{f}")
  if x.get("recommendation") not in RECOMMENDATIONS:ds.add(f"decision:{pid}:invalid_recommendation")
  for oid in x.get("option_ids",[]):
   if oid not in oids:ds.add(f"decision:{pid}:unknown_option:{oid}")
  for xid in x.get("pilot_ids",[]):
   if xid not in pilotids:ds.add(f"decision:{pid}:unknown_pilot:{xid}")
  for ref in x.get("evidence_source_ids",[]):
   if ref not in sids:ds.add(f"decision:{pid}:unknown_source:{ref}")
  if x.get("human_state")!="PENDING":ds.add(f"decision:{pid}:human_state_not_pending")
 for pid in pids-decided:ds.add(f"decision:missing_partner:{pid}")
 missing=SECTIONS-set(d.get("output_sections",[]))
 if missing:ds.add("output_sections:missing:"+",".join(sorted(missing)))
 tests=d.get("tests",{})
 for t in TESTS:
  if tests.get(t)!="PASS":ds.add(f"test:{t}:not_pass")
 reviews=d.get("reviews",{})
 for r in REVIEWS:
  if reviews.get(r)!="PASS":gaps.add(f"review:{r}:not_pass")
 if reviews.get("FINAL_HUMAN_ALLIANCE_DECISION")!="PENDING":ds.add("review:FINAL_HUMAN_ALLIANCE_DECISION:must_be_pending")
 for f in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS):ds.add(f"forbidden_flag:{f}")
 states=set(d.get("forbidden_states",[]));states.add(d.get("published_state","DRAFT"))
 for s in sorted(states&FORBIDDEN_STATES):ds.add(f"forbidden_state:{s}")
 ready=not ds and not gaps
 return {"skill":"partner-alliance","state":"READY_FOR_HUMAN_ALLIANCE_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"partners":len(partners),"diligence_domains":len(dd),"alliance_options":len(options),"pilots":len(pilots),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(reviews.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 counterparty truth, alliance value, diligence/legal/economics accuracy, pilot/customer outcome, token cost, duration or adoption."}
def main():
 if len(sys.argv)!=2:print("usage: evaluate_partner_alliance.py INPUT.json",file=sys.stderr);return 2
 r=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")));print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__":raise SystemExit(main())
