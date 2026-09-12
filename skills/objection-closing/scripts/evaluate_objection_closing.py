#!/usr/bin/env python3
import json,sys
from pathlib import Path

TESTS={"mandate_sources","objection_verbatim","diagnosis_alternatives","response_evidence","commercial_options","customer_choice","decision_boundary"}
REVIEWS={"CUSTOMER_CONTEXT","SALES_MANAGER","FINANCE_COMMERCIAL","DELIVERY_PRODUCT","LEGAL_PRIVACY_FAIRNESS","BRAND_ACCESSIBILITY"}
RISK_TYPES={"CUSTOMER_INTENT_MISREAD","CLAIM_PROOF_INTEGRITY","COMMERCIAL_AUTHORITY","PRESSURE_FAIRNESS","PRIVACY_CONTACT_CONSENT","RELATIONSHIP_REPUTATION"}
SECTIONS={"document_control","objection_source_ledger","diagnosis_hypotheses","fact_claim_gap_map","response_options","commercial_customer_choice","risks_scenarios","decisions_reviews_audit"}
STATEMENT_TYPES={"QUESTION","CONSTRAINT","CONDITION","RISK","MISUNDERSTANDING","PREFERENCE","DECLINE","NO_RESPONSE","UNKNOWN"}
OBJECTIVES={"CLARIFY","ANSWER","PROVIDE_EVIDENCE","OFFER_APPROVED_OPTIONS","PAUSE","RESPECT_DECLINE"}
FORBIDDEN_FLAGS={"verbatim_fabricated","customer_intent_fabricated","pain_fabricated","budget_fabricated","authority_fabricated","need_fabricated","urgency_fabricated","roi_fabricated","price_fabricated","discount_fabricated","term_fabricated","guarantee_fabricated","capability_fabricated","case_fabricated","result_fabricated","credential_fabricated","testimonial_fabricated","benchmark_fabricated","competitor_claim_fabricated","competitor_defamed","consent_bypassed","stop_ignored","repeated_contact","false_urgency","false_scarcity","fear_exploited","shame_used","vulnerability_exploited","sensitive_attribute_used","proxy_discrimination","hidden_term","forced_choice","optout_hidden","misleading_empathy","question_called_acceptance","silence_called_consent","review_bypassed","auto_sent","auto_followed_up","auto_discounted","auto_terms_changed","auto_committed","auto_negotiated","auto_closed","auto_accepted"}
FORBIDDEN_STATES={"RESPONSE_SENT","FOLLOWUP_SCHEDULED","PRICE_CHANGED","DISCOUNT_GRANTED","TERMS_CHANGED","COMMITMENT_MADE","NEGOTIATED","DEAL_CLOSED","CONTRACT_ACCEPTED"}
RIGHTS={"AUTHORIZED","INTERNAL_AUTHORIZED","CUSTOMER_AUTHORIZED","PUBLIC_TERMS_OK"}

def ok(v): return v not in (None,"",[],{})
def evaluate(d):
 ds=set(); gaps=set(); m=d.get("mandate",{})
 for f in ("customer_entity","purpose","opportunity_stage","channel","as_of","owner","response_authority","commercial_authority","consent_contact_rule","confidentiality_retention","required_reviews"):
  if not ok(m.get(f)): ds.add(f"mandate:missing_{f}")
 sources=d.get("sources",[]); sids=set()
 for i,s in enumerate(sources):
  sid=s.get("id",f"index-{i}"); sids.add(sid)
  for f in ("source_type","locator","version","date","rights_consent","confidence","subject"):
   if not ok(s.get(f)): ds.add(f"source:{sid}:missing_{f}")
  if s.get("rights_consent") not in RIGHTS: ds.add(f"source:{sid}:not_authorized")

 records=d.get("objection_records",[]); rids=set()
 for i,r in enumerate(records):
  rid=r.get("id",f"index-{i}"); rids.add(rid)
  for f in ("verbatim","speaker_role","timestamp","channel","sequence_context","prior_response","source_ids","rights_consent","confidence"):
   if not ok(r.get(f)): ds.add(f"record:{rid}:missing_{f}")
  for ref in r.get("source_ids",[]):
   if ref not in sids: ds.add(f"record:{rid}:unknown_source:{ref}")
  if r.get("rights_consent") not in RIGHTS: ds.add(f"record:{rid}:not_authorized")
 if len(rids)!=len(records): ds.add("records:duplicate_id")

 diagnoses=d.get("diagnoses",[]); diagnosed=set()
 for i,x in enumerate(diagnoses):
  rid=x.get("record_id",f"index-{i}"); diagnosed.add(rid)
  if rid not in rids: ds.add(f"diagnosis:unknown_record:{rid}")
  for f in ("statement_type","candidate_classes","evidence_source_ids","confidence","alternative_hypotheses","clarification_question","inferred_intent_status"):
   if not ok(x.get(f)): ds.add(f"diagnosis:{rid}:missing_{f}")
  if x.get("statement_type") not in STATEMENT_TYPES: ds.add(f"diagnosis:{rid}:invalid_statement_type")
  if x.get("inferred_intent_status")!="HYPOTHESIS_NOT_FACT": ds.add(f"diagnosis:{rid}:intent_asserted")
  for ref in x.get("evidence_source_ids",[]):
   if ref not in sids: ds.add(f"diagnosis:{rid}:unknown_source:{ref}")
 for rid in rids-diagnosed: ds.add(f"diagnosis:missing_record:{rid}")

 truths=d.get("truth_items",[]); tids=set()
 for i,x in enumerate(truths):
  tid=x.get("id",f"index-{i}"); tids.add(tid)
  for f in ("item_type","statement","source_ids","version","valid_until","rights_consent","conditions_limitations","status"):
   if not ok(x.get(f)): ds.add(f"truth:{tid}:missing_{f}")
  for ref in x.get("source_ids",[]):
   if ref not in sids: ds.add(f"truth:{tid}:unknown_source:{ref}")
  if x.get("rights_consent") not in RIGHTS: ds.add(f"truth:{tid}:not_authorized")
  if x.get("status")!="VERIFIED_FOR_DRAFT": ds.add(f"truth:{tid}:not_verified")

 options=d.get("response_options",[]); oids=set(); covered=set()
 for i,x in enumerate(options):
  oid=x.get("id",f"index-{i}"); oids.add(oid)
  for f in ("record_ids","objective","acknowledgement","clarification_question","evidence_item_ids","factual_answer","limitations_unknowns","approved_choices","permission_next_or_exit","prohibited_claims","risk_notes"):
   if not ok(x.get(f)): ds.add(f"response:{oid}:missing_{f}")
  if x.get("objective") not in OBJECTIVES: ds.add(f"response:{oid}:invalid_objective")
  for rid in x.get("record_ids",[]):
   if rid not in rids: ds.add(f"response:{oid}:unknown_record:{rid}")
   else: covered.add(rid)
  for tid in x.get("evidence_item_ids",[]):
   if tid not in tids: ds.add(f"response:{oid}:unknown_truth:{tid}")
 for rid in rids-covered: ds.add(f"response:uncovered_record:{rid}")

 cb=d.get("commercial_boundary",{})
 for f in ("approved_offer_scope","price_reference","terms_reference","version_validity","discount_exception_rule","change_authority","binding_boundary","open_requests"):
  if not ok(cb.get(f)): ds.add(f"commercial:missing_{f}")
 cc=d.get("customer_choice",{})
 for f in ("consent_status","contact_channel_frequency","stop_no_hold_rule","accessibility","correction_appeal","retention","next_step_permission","exit_options"):
  if not ok(cc.get(f)): ds.add(f"customer_choice:missing_{f}")

 risks=d.get("risks",[]); seen=set()
 for i,r in enumerate(risks):
  typ=r.get("risk_type",f"index-{i}"); seen.add(typ)
  for f in ("statement","likelihood","impact","trigger","mitigation","contingency","owner"):
   if not ok(r.get(f)): ds.add(f"risk:{typ}:missing_{f}")
 for typ in RISK_TYPES-seen: ds.add(f"risks:missing_type:{typ}")

 decisions=d.get("decision_queue",[]); decided=set()
 for i,x in enumerate(decisions):
  rid=x.get("record_id",f"index-{i}"); decided.add(rid)
  if rid not in rids: ds.add(f"decision:unknown_record:{rid}")
  for f in ("recommended_option_id","alternatives","evidence_item_ids","decision_owner","needed_by","human_state"):
   if not ok(x.get(f)): ds.add(f"decision:{rid}:missing_{f}")
  if x.get("recommended_option_id") not in oids: ds.add(f"decision:{rid}:unknown_option")
  for tid in x.get("evidence_item_ids",[]):
   if tid not in tids: ds.add(f"decision:{rid}:unknown_truth:{tid}")
  if x.get("human_state")!="PENDING": ds.add(f"decision:{rid}:human_state_not_pending")
 for rid in rids-decided: ds.add(f"decision:missing_record:{rid}")

 missing=SECTIONS-set(d.get("output_sections",[]))
 if missing: ds.add("output_sections:missing:"+",".join(sorted(missing)))
 tests=d.get("tests",{})
 for t in TESTS:
  if tests.get(t)!="PASS": ds.add(f"test:{t}:not_pass")
 reviews=d.get("reviews",{})
 for r in REVIEWS:
  if reviews.get(r)!="PASS": gaps.add(f"review:{r}:not_pass")
 if reviews.get("FINAL_HUMAN_RESPONSE_RELEASE")!="PENDING": ds.add("review:FINAL_HUMAN_RESPONSE_RELEASE:must_be_pending")
 for f in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS): ds.add(f"forbidden_flag:{f}")
 states=set(d.get("forbidden_states",[])); states.add(d.get("published_state","DRAFT"))
 for s in sorted(states&FORBIDDEN_STATES): ds.add(f"forbidden_state:{s}")
 ready=not ds and not gaps
 return {"skill":"objection-closing","state":"READY_FOR_HUMAN_RESPONSE_RELEASE" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"objection_records":len(records),"diagnoses":len(diagnoses),"truth_items":len(truths),"response_options":len(options),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(reviews.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 customer intent, response quality, commercial accuracy, customer choice/outcome, token cost, duration or adoption."}

def main():
 if len(sys.argv)!=2: print("usage: evaluate_objection_closing.py INPUT.json",file=sys.stderr); return 2
 r=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))); print(json.dumps(r,ensure_ascii=False,indent=2)); return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__": raise SystemExit(main())
