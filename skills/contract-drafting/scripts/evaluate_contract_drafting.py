#!/usr/bin/env python3
import json,sys
from pathlib import Path
TESTS={"mandate_parties_law_sources","commercial_scope_acceptance_payment","obligation_clause_trace","ip_data_risk_allocation","term_exit_dispute_formality","annex_consistency_tbd","decision_boundary"}
REVIEWS={"BUSINESS_OWNER","COMMERCIAL_FINANCE_TAX","LEGAL_COUNSEL","DATA_SECURITY_PRIVACY_IP","DELIVERY_OPERATIONS","SIGNING_AUTHORITY_GOVERNANCE"}
RISK_TYPES={"PARTY_AUTHORITY_FORMALITY","SCOPE_ACCEPTANCE_CHANGE","COMMERCIAL_PAYMENT_TAX","IP_DATA_CONFIDENTIALITY_SECURITY","LIABILITY_INDEMNITY_INSURANCE_COMPLIANCE","TERM_TERMINATION_DISPUTE_ENFORCEABILITY"}
SECTIONS={"document_control","source_term_ledger","party_authority_jurisdiction","commercial_obligation_matrix","risk_clause_matrix","draft_annexes_consistency","negotiation_issues_decisions_reviews","audit_change_log"}
RIGHTS={"AUTHORIZED","INTERNAL_AUTHORIZED","OWNER_AUTHORIZED","POLICY_AUTHORIZED","COUNSEL_AUTHORIZED","CONTRACT_AUTHORIZED","PUBLIC_LEGAL_SOURCE"}
TERM_STATES={"PROPOSED","APPROVED_INTERNAL","NEGOTIATED_PENDING","REJECTED","SUPERSEDED","EXECUTED_REFERENCE","TBD"}
POSITIONS={"PREFERRED","ACCEPTABLE","FALLBACK","REDLINE","TBD"}
RECOMMENDATIONS={"DRAFT_REVIEW","COMMERCIAL_TERM_REVIEW","RISK_CLAUSE_REVIEW","LEGAL_FORMALITY_REVIEW","NEGOTIATION_POSITION_REVIEW","SIGNING_READINESS_REVIEW","REVISE","HOLD"}
FORBIDDEN_FLAGS={"party_fabricated","legal_entity_fabricated","representative_fabricated","authority_fabricated","address_fabricated","tax_id_fabricated","notice_detail_fabricated","signature_block_fabricated","jurisdiction_fabricated","governing_law_fabricated","dispute_forum_fabricated","mandatory_law_fabricated","formality_fabricated","effective_date_fabricated","term_fabricated","language_priority_fabricated","legal_source_fabricated","legal_citation_fabricated","clause_source_fabricated","commercial_term_fabricated","scope_fabricated","deliverable_fabricated","exclusion_fabricated","dependency_fabricated","milestone_fabricated","acceptance_fabricated","sla_fabricated","service_credit_fabricated","price_fabricated","currency_fabricated","tax_fabricated","payment_fabricated","expense_fabricated","refund_fabricated","warranty_fabricated","notice_period_fabricated","cure_period_fabricated","renewal_fabricated","termination_right_fabricated","transition_fabricated","obligation_fabricated","right_fabricated","ip_ownership_fabricated","license_fabricated","third_party_rights_hidden","data_role_fabricated","privacy_commitment_fabricated","security_commitment_fabricated","incident_term_fabricated","confidentiality_term_fabricated","confidentiality_exception_hidden","indemnity_fabricated","liability_cap_fabricated","insurance_fabricated","force_majeure_fabricated","compliance_certified","audit_right_fabricated","assignment_fabricated","subcontract_right_fabricated","e_sign_validity_claimed","enforceability_claimed","legal_advice_claimed","privilege_claimed_falsely","one_sided_risk_hidden","commercial_conflict_hidden","law_conflict_hidden","date_conflict_hidden","currency_conflict_hidden","tax_conflict_hidden","scope_conflict_hidden","acceptance_conflict_hidden","payment_conflict_hidden","termination_conflict_hidden","definition_inconsistent","party_name_inconsistent","crossref_broken","annex_missing","precedence_missing","survival_conflict_hidden","placeholder_hidden","unresolved_tbd_removed","template_copied_without_rights","prior_agreement_mixed","negotiated_change_omitted","redline_hidden","fallback_invented","counsel_review_bypassed","signature_authority_bypassed","confidential_data_exposed","privileged_data_exposed","credential_exposed","pii_exposed","public_llm_unapproved","review_bypassed","auto_contract_sent","auto_contract_published","auto_offer_made","auto_acceptance_sent","auto_term_accepted","auto_negotiation_conducted","auto_redline_accepted","auto_contract_approved","auto_contract_signed","auto_e_signature_applied","auto_counterpart_executed","auto_payment_committed","auto_obligation_activated","auto_legal_advice_issued","auto_enforceability_certified","auto_government_filed","auto_registration_completed","auto_external_party_contacted","auto_executed_record_mutated"}
FORBIDDEN_STATES={"CONTRACT_SENT","CONTRACT_PUBLISHED","OFFER_MADE","ACCEPTANCE_SENT","TERM_ACCEPTED","NEGOTIATION_CONDUCTED","REDLINE_ACCEPTED","CONTRACT_APPROVED","CONTRACT_SIGNED","E_SIGNATURE_APPLIED","COUNTERPART_EXECUTED","PAYMENT_COMMITTED","OBLIGATION_ACTIVATED","LEGAL_ADVICE_ISSUED","ENFORCEABILITY_CERTIFIED","GOVERNMENT_FILED","REGISTRATION_COMPLETED","EXTERNAL_PARTY_CONTACTED","EXECUTED_RECORD_MUTATED"}
def ok(v):return v not in(None,"",[],{})
def fields(ds,p,obj,req):
 for f in req:
  if not ok(obj.get(f)):ds.add(f"{p}:missing_{f}")
def refs(ds,p,vals,known):
 for x in vals:
  if x not in known:ds.add(f"{p}:unknown_ref:{x}")
def evaluate(d):
 ds=set();gaps=set();m=d.get("mandate",{})
 fields(ds,"mandate",m,("document_deal_type_purpose_stage","audience_language_intended_use","as_of_effective_term","owner_legal_signing_authorities","required_approvals_reviews","risk_position","non_goals"))
 sources=d.get("sources",[]);sids=set()
 for i,x in enumerate(sources):
  xid=x.get("id",f"index-{i}");sids.add(xid);fields(ds,f"source:{xid}",x,("source_type","locator","version_date_as_of","rights_purpose","confidentiality_access","priority_status","confidence","supports"))
  if x.get("rights_purpose") not in RIGHTS:ds.add(f"source:{xid}:not_authorized")
 if len(sids)!=len(sources):ds.add("sources:duplicate_id")
 parties=d.get("parties",[]);pids=set()
 for i,x in enumerate(parties):
  xid=x.get("id",f"index-{i}");pids.add(xid);fields(ds,f"party:{xid}",x,("legal_identity_role","address_ids","representative_capacity","authority_source_ids","notice_signature_details","verification_status"));refs(ds,f"party:{xid}:authority",x.get("authority_source_ids",[]),sids)
 if len(pids)!=len(parties):ds.add("parties:duplicate_id")
 law=d.get("legal_context",{})
 fields(ds,"legal_context",law,("jurisdiction_transaction_scope","governing_law_source_ids","dispute_forum_source_ids","mandatory_law_formality","e_sign_notarization_registration","language_priority","counsel_owner_status"));refs(ds,"legal_context:law",law.get("governing_law_source_ids",[]),sids);refs(ds,"legal_context:forum",law.get("dispute_forum_source_ids",[]),sids)
 terms=d.get("term_items",[]);tids=set()
 for i,x in enumerate(terms):
  xid=x.get("id",f"index-{i}");tids.add(xid);fields(ds,f"term:{xid}",x,("topic_current_position","source_ids","term_state","priority_contradiction","owner_needed_by_consequence"));refs(ds,f"term:{xid}:source",x.get("source_ids",[]),sids)
  if x.get("term_state") not in TERM_STATES:ds.add(f"term:{xid}:invalid_state")
 commercial=d.get("commercial_items",[]);cids=set()
 for i,x in enumerate(commercial):
  xid=x.get("id",f"index-{i}");cids.add(xid);fields(ds,f"commercial:{xid}",x,("topic","parties_roles","scope_term","trigger_timing_dependency","evidence_acceptance","price_currency_tax_payment","change_exception_remedy","source_term_ids"));refs(ds,f"commercial:{xid}:party",x.get("parties_roles",[]),pids);refs(ds,f"commercial:{xid}:term",x.get("source_term_ids",[]),tids)
 obligations=d.get("obligations",[]);oids=set()
 for i,x in enumerate(obligations):
  xid=x.get("id",f"index-{i}");oids.add(xid);fields(ds,f"obligation:{xid}",x,("actor_party_id","action_standard","trigger_due_window","dependency","evidence_acceptance","exception_remedy","survival","source_term_ids"));refs(ds,f"obligation:{xid}:party",[x.get("actor_party_id")],pids);refs(ds,f"obligation:{xid}:term",x.get("source_term_ids",[]),tids)
 clauses=d.get("clause_positions",[]);clids=set()
 for i,x in enumerate(clauses):
  xid=x.get("id",f"index-{i}");clids.add(xid);fields(ds,f"clause:{xid}",x,("topic_draft_summary","source_term_ids","preferred","acceptable","fallback","redline","rationale_risk","owner_approval_state"));refs(ds,f"clause:{xid}:term",x.get("source_term_ids",[]),tids)
 for x in clauses:
  for k in ("preferred","acceptable","fallback","redline"):
   if x.get(k) in(None,""):ds.add(f"clause:{x.get('id','unknown')}:missing_{k}")
 annexes=d.get("annexes",[]);aids=set()
 for i,x in enumerate(annexes):
  xid=x.get("id",f"index-{i}");aids.add(xid);fields(ds,f"annex:{xid}",x,("purpose_version","inputs_defined_terms","precedence_linkage","source_term_ids","reviewer_status"));refs(ds,f"annex:{xid}:term",x.get("source_term_ids",[]),tids)
 checks=d.get("consistency_checks",[])
 for i,x in enumerate(checks):
  xid=x.get("id",f"index-{i}");fields(ds,f"check:{xid}",x,("check_type","affected_ids","finding","owner_needed_by_consequence","blocking_status","evidence"))
 risks=d.get("risks",[]);seenr=set()
 for i,x in enumerate(risks):
  typ=x.get("risk_type",f"index-{i}");seenr.add(typ);fields(ds,f"risk:{typ}",x,("statement","likelihood","impact","trigger","mitigation","contingency","owner_role"))
 for typ in RISK_TYPES-seenr:ds.add(f"risks:missing_type:{typ}")
 decisions=d.get("decision_queue",[])
 for i,x in enumerate(decisions):
  xid=x.get("id",f"index-{i}");fields(ds,f"decision:{xid}",x,("recommendation","issue_options_position","evidence_source_ids","review_gaps","decision_owner_role","needed_by","human_state"))
  if x.get("recommendation") not in RECOMMENDATIONS:ds.add(f"decision:{xid}:invalid_recommendation")
  refs(ds,f"decision:{xid}:source",x.get("evidence_source_ids",[]),sids)
  if x.get("human_state")!="PENDING":ds.add(f"decision:{xid}:human_state_not_pending")
 missing=SECTIONS-set(d.get("output_sections",[]))
 if missing:ds.add("output_sections:missing:"+",".join(sorted(missing)))
 tests=d.get("tests",{})
 for x in TESTS:
  if tests.get(x)!="PASS":ds.add(f"test:{x}:not_pass")
 rev=d.get("reviews",{})
 for x in REVIEWS:
  if rev.get(x)!="PASS":gaps.add(f"review:{x}:not_pass")
 if rev.get("FINAL_HUMAN_LEGAL_CONTRACT_DECISION")!="PENDING":ds.add("review:FINAL_HUMAN_LEGAL_CONTRACT_DECISION:must_be_pending")
 for x in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS):ds.add(f"forbidden_flag:{x}")
 states=set(d.get("forbidden_states",[]));states.add(d.get("operational_state","DRAFT"))
 for x in sorted(states&FORBIDDEN_STATES):ds.add(f"forbidden_state:{x}")
 ready=not ds and not gaps
 return {"skill":"contract-drafting","state":"READY_FOR_HUMAN_LEGAL_CONTRACT_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"parties":len(parties),"term_items":len(terms),"commercial_items":len(commercial),"obligations":len(obligations),"clause_positions":len(clauses),"annexes":len(annexes),"consistency_checks":len(checks),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(rev.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 party/authority/legal/commercial truth, legal advice, enforceability, negotiation outcome, execution, compliance, authorization, token cost or duration."}
def main():
 if len(sys.argv)!=2:print("usage: evaluate_contract_drafting.py INPUT.json",file=sys.stderr);return 2
 r=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")));print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__":raise SystemExit(main())
