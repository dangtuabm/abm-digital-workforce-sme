#!/usr/bin/env python3
import json,sys
from pathlib import Path
TESTS={"mandate_sources","customer_requirements","option_traceability","scope_acceptance","delivery_economics","claims_risks","decision_boundary"}
REVIEWS={"CUSTOMER_FACT","SOLUTION_DOMAIN","DELIVERY_OPERATIONS","FINANCE_COMMERCIAL","LEGAL_PRIVACY_IP","BRAND_ACCESSIBILITY"}
RISK_TYPES={"SCOPE_CHANGE","DELIVERY_CAPACITY","DATA_SECURITY_PRIVACY","VALUE_ADOPTION","LEGAL_IP_COMMERCIAL","CUSTOMER_DEPENDENCY"}
SECTIONS={"document_mandate","executive_decision","customer_requirements","options_traceability","scope_acceptance","delivery_roles","economics_terms","risks_claims_rights","decision_reviews_release"}
FORBIDDEN_FLAGS={"customer_pain_fabricated","customer_impact_fabricated","requirement_fabricated","capability_fabricated","case_fabricated","result_fabricated","credential_fabricated","benchmark_fabricated","price_fabricated","discount_fabricated","tax_fabricated","timeline_fabricated","capacity_fabricated","acceptance_fabricated","legal_claim_fabricated","social_proof_fabricated","customer_logo_misused","confidential_evidence_misused","generic_copy_claimed_personalized","estimate_called_commitment","scope_hidden","exclusion_hidden","fee_hidden","term_hidden","risk_hidden","false_urgency","pressure_tactic","discriminatory_personalization","vulnerability_exploited","review_bypassed","auto_sent","auto_quoted","auto_negotiated","auto_discounted","auto_committed","auto_contracted","auto_signed","auto_published","auto_accepted"}
FORBIDDEN_STATES={"SENT","QUOTED","NEGOTIATED","DISCOUNTED","COMMITTED","CONTRACTED","SIGNED","PUBLISHED","ACCEPTED"}
def ok(v): return v not in (None,"",[],{})
def evaluate(d):
 ds=set(); gaps=set(); m=d.get("mandate",{})
 for f in ("customer_entity","purpose","audience","opportunity_stage","proposal_scope","as_of","valid_until","owner","release_authority","confidentiality","constraints","required_reviews"):
  if not ok(m.get(f)): ds.add(f"mandate:missing_{f}")
 sources=d.get("sources",[]); sids=set()
 for i,s in enumerate(sources):
  sid=s.get("id",f"index-{i}"); sids.add(sid)
  for f in ("source_type","locator","version","date","rights_consent","claim_class","confidence","subject"):
   if not ok(s.get(f)): ds.add(f"source:{sid}:missing_{f}")
  if s.get("rights_consent") not in ("AUTHORIZED","INTERNAL_AUTHORIZED","CUSTOMER_AUTHORIZED","PUBLIC_TERMS_OK"): ds.add(f"source:{sid}:not_authorized")
 probs=d.get("problems",[]); probids=set()
 for i,p in enumerate(probs):
  pid=p.get("id",f"index-{i}"); probids.add(pid)
  for f in ("statement","impact","current_alternative","source_ids","confidence","status"):
   if not ok(p.get(f)): ds.add(f"problem:{pid}:missing_{f}")
  for ref in p.get("source_ids",[]):
   if ref not in sids: ds.add(f"problem:{pid}:unknown_source:{ref}")
 reqs=d.get("requirements",[]); reqids=set()
 for i,r in enumerate(reqs):
  rid=r.get("id",f"index-{i}"); reqids.add(rid)
  for f in ("statement","priority","source_ids","acceptance_need","owner"):
   if not ok(r.get(f)): ds.add(f"requirement:{rid}:missing_{f}")
  for ref in r.get("source_ids",[]):
   if ref not in sids: ds.add(f"requirement:{rid}:unknown_source:{ref}")
 opts=d.get("options",[]); optids=set()
 for i,o in enumerate(opts):
  oid=o.get("id",f"index-{i}"); optids.add(oid)
  for f in ("name","rationale","outcome_value_hypothesis","capability_evidence_ids","limitations","prerequisites","trade_offs","feasibility","recommendation_status"):
   if not ok(o.get(f)): ds.add(f"option:{oid}:missing_{f}")
  for ref in o.get("capability_evidence_ids",[]):
   if ref not in sids: ds.add(f"option:{oid}:unknown_source:{ref}")
 dels=d.get("deliverables",[]); delids=set()
 for i,x in enumerate(dels):
  did=x.get("id",f"index-{i}"); delids.add(did)
  for f in ("name","scope","acceptance_criteria","acceptance_evidence","acceptance_approver","service_level","dependencies","exclusions"):
   if not ok(x.get(f)): ds.add(f"deliverable:{did}:missing_{f}")
 links=d.get("traceability",[])
 linked_p=set();linked_r=set();linked_o=set();linked_d=set()
 for i,l in enumerate(links):
  lid=l.get("id",f"index-{i}")
  for f,valid,target in (("problem_id",probids,linked_p),("requirement_id",reqids,linked_r),("option_id",optids,linked_o),("deliverable_id",delids,linked_d)):
   val=l.get(f)
   if val not in valid: ds.add(f"trace:{lid}:invalid_{f}")
   else: target.add(val)
  if not ok(l.get("acceptance_link")): ds.add(f"trace:{lid}:missing_acceptance_link")
 for pid in probids-linked_p: ds.add(f"trace:unlinked_problem:{pid}")
 for rid in reqids-linked_r: ds.add(f"trace:unlinked_requirement:{rid}")
 for oid in optids-linked_o: ds.add(f"trace:unlinked_option:{oid}")
 for did in delids-linked_d: ds.add(f"trace:unlinked_deliverable:{did}")
 scope=d.get("scope_control",{})
 for f in ("in_scope","out_of_scope","optional_future","assumptions","dependencies","customer_roles","provider_roles","change_request_rule"):
  if not ok(scope.get(f)): ds.add(f"scope:missing_{f}")
 milestones=d.get("milestones",[])
 for i,x in enumerate(milestones):
  mid=x.get("id",f"index-{i}")
  for f in ("phase","entry","activities","exit","evidence","approver","resources_capacity","data_security","support_handoff"):
   if not ok(x.get(f)): ds.add(f"milestone:{mid}:missing_{f}")
 eco=d.get("economics",{})
 for f in ("approved_price_reference","version","currency","tax_treatment","term","valid_until","payment_candidates","milestone_links","optional_items","exclusions","value_driver_range","measurement_method","conditions"):
  if not ok(eco.get(f)): ds.add(f"economics:missing_{f}")
 risks=d.get("risks",[]); seen=set()
 for i,r in enumerate(risks):
  typ=r.get("risk_type",f"index-{i}");seen.add(typ)
  for f in ("statement","likelihood","impact","trigger","mitigation","contingency","owner"):
   if not ok(r.get(f)): ds.add(f"risk:{typ}:missing_{f}")
 for typ in RISK_TYPES-seen: ds.add(f"risks:missing_type:{typ}")
 claims=d.get("claims",[])
 for i,c in enumerate(claims):
  cid=c.get("id",f"index-{i}")
  for f in ("statement","claim_type","source_ids","version","rights_consent","conditions_limitations","status"):
   if not ok(c.get(f)): ds.add(f"claim:{cid}:missing_{f}")
  for ref in c.get("source_ids",[]):
   if ref not in sids: ds.add(f"claim:{cid}:unknown_source:{ref}")
  if c.get("status")!="VERIFIED_FOR_DRAFT": ds.add(f"claim:{cid}:not_verified_for_draft")
 dec=d.get("decision_path",{})
 for f in ("options","open_questions","decision_roles","review_roles","next_steps","valid_until","change_route","contract_boundary"):
  if not ok(dec.get(f)): ds.add(f"decision:missing_{f}")
 miss=SECTIONS-set(d.get("output_sections",[]))
 if miss: ds.add("output_sections:missing:"+",".join(sorted(miss)))
 tests=d.get("tests",{})
 for t in TESTS:
  if tests.get(t)!="PASS": ds.add(f"test:{t}:not_pass")
 reviews=d.get("reviews",{})
 for r in REVIEWS:
  if reviews.get(r)!="PASS": gaps.add(f"review:{r}:not_pass")
 if reviews.get("FINAL_HUMAN_PROPOSAL_RELEASE")!="PENDING": ds.add("review:FINAL_HUMAN_PROPOSAL_RELEASE:must_be_pending")
 for f in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS): ds.add(f"forbidden_flag:{f}")
 states=set(d.get("forbidden_states",[]));states.add(d.get("published_state","DRAFT"))
 for s in sorted(states&FORBIDDEN_STATES): ds.add(f"forbidden_state:{s}")
 ready=not ds and not gaps
 return {"skill":"sales-proposal","state":"READY_FOR_HUMAN_PROPOSAL_RELEASE" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"problems":len(probs),"requirements":len(reqs),"options":len(opts),"deliverables":len(dels),"trace_links":len(links),"milestones":len(milestones),"risks":len(risks),"claims":len(claims),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(reviews.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 customer truth, proposal decision quality, commercial/legal accuracy, acceptance outcome, token cost, duration or adoption."}
def main():
 if len(sys.argv)!=2: print("usage: evaluate_sales_proposal.py INPUT.json",file=sys.stderr); return 2
 r=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")));print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__": raise SystemExit(main())
