#!/usr/bin/env python3
import json,sys
from pathlib import Path
TESTS={"mandate_evidence","value_offer","metric_economics","wtp_corridor","commercial_controls","scenario_experiment","decision_boundary"}
REVIEWS={"PRODUCT_CUSTOMER","FINANCE_PRICING","DELIVERY_OPERATIONS","LEGAL_TAX_COMPETITION","COMMERCIAL_GOVERNANCE"}
RISK_TYPES={"FINANCE_ECONOMICS","CUSTOMER_VALUE","LEGAL_TAX_COMPETITION","DELIVERY_CHANNEL_FAIRNESS"}
SECTIONS={"mandate_authority","value_evidence","offer_packages","metric_economics","wtp_corridor","commercial_controls","scenario_validation","risks_reviews_audit"}
FORBIDDEN_FLAGS={"value_fabricated","price_fabricated","cost_fabricated","margin_fabricated","wtp_fabricated","competitor_price_fabricated","demand_fabricated","conversion_fabricated","churn_fabricated","capacity_fabricated","bonus_value_fabricated","guarantee_result_fabricated","fake_anchor","fake_discount","fake_scarcity","fake_deadline","hidden_fee","hidden_term","unsafe_guarantee","dark_pattern","collusion","price_fixing","resale_price_coercion","confidential_competitor_data_used","protected_trait_pricing","sensitive_trait_pricing","vulnerability_exploited","floor_bypassed","approval_bypassed","criteria_changed","auto_published","auto_quoted","auto_discounted","auto_contracted","auto_invoiced","auto_charged","auto_promoted"}
FORBIDDEN_STATES={"PUBLISHED","QUOTED","DISCOUNTED","CONTRACTED","INVOICED","CHARGED","PROMOTED","APPROVED"}
def ok(v): return v not in (None,"",[],{})
def evaluate(d):
 ds=set(); gaps=set(); m=d.get("mandate",{})
 for f in ("objective","product","segment","geography","currency","as_of","horizon","price_authority","constraints","prohibited_actions","required_reviews"):
  if not ok(m.get(f)): ds.add(f"mandate:missing_{f}")
 sources=d.get("sources",[]); sids=set()
 for i,s in enumerate(sources):
  sid=s.get("id",f"index-{i}"); sids.add(sid)
  for f in ("locator","version","date","rights","evidence_type","confidence","subject"):
   if not ok(s.get(f)): ds.add(f"source:{sid}:missing_{f}")
  if s.get("rights") not in ("AUTHORIZED","PUBLIC_TERMS_OK","INTERNAL_AUTHORIZED"): ds.add(f"source:{sid}:not_authorized")
 values=d.get("value_cases",[])
 for i,v in enumerate(values):
  vid=v.get("id",f"index-{i}")
  for f in ("job","outcome","alternative","value_driver","low","base","high","unit","method","source_ids","confidence"):
   if not ok(v.get(f)) and v.get(f)!=0: ds.add(f"value:{vid}:missing_{f}")
  if all(isinstance(v.get(x),(int,float)) for x in ("low","base","high")) and not(v["low"]<=v["base"]<=v["high"]): ds.add(f"value:{vid}:invalid_range")
  for ref in v.get("source_ids",[]):
   if ref not in sids: ds.add(f"value:{vid}:unknown_source:{ref}")
 packages=d.get("packages",[]); pids=set()
 for i,p in enumerate(packages):
  pid=p.get("id",f"index-{i}"); pids.add(pid)
  for f in ("name","core_outcome","scope","entitlements","limits","deliverables","service_level","dependencies","exclusions","capacity","bonus_value_cost"):
   if not ok(p.get(f)): ds.add(f"package:{pid}:missing_{f}")
 metrics=d.get("price_metrics",[])
 for i,x in enumerate(metrics):
  mid=x.get("id",f"index-{i}")
  for f in ("metric","structure","alignment","predictability","measurability","gaming_risk","billing_feasibility","recommendation"):
   if not ok(x.get(f)): ds.add(f"metric:{mid}:missing_{f}")
 economics=d.get("economics",[])
 for i,e in enumerate(economics):
  pid=e.get("package_id",f"index-{i}")
  if pid not in pids: ds.add(f"economics:{pid}:unknown_package")
  for f in ("formula","inputs","source_ids","currency","base_year","horizon","price_low","price_base","price_high","variable_cost","incremental_cost","fixed_allocation","contribution_margin_low","contribution_margin_base","contribution_margin_high","break_even","cash_timing","capacity_exposure","sensitivity"):
   if not ok(e.get(f)) and e.get(f)!=0: ds.add(f"economics:{pid}:missing_{f}")
  for lo,ba,hi,label in [(e.get("price_low"),e.get("price_base"),e.get("price_high"),"price"),(e.get("contribution_margin_low"),e.get("contribution_margin_base"),e.get("contribution_margin_high"),"margin")]:
   if all(isinstance(z,(int,float)) for z in (lo,ba,hi)) and not(lo<=ba<=hi): ds.add(f"economics:{pid}:invalid_{label}_range")
  for ref in e.get("source_ids",[]):
   if ref not in sids: ds.add(f"economics:{pid}:unknown_source:{ref}")
 wtp=d.get("market_wtp",[])
 for i,w in enumerate(wtp):
  wid=w.get("id",f"index-{i}")
  for f in ("method","finding","range","currency","date","source_ids","bias_limit","confidence"):
   if not ok(w.get(f)): ds.add(f"wtp:{wid}:missing_{f}")
  for ref in w.get("source_ids",[]):
   if ref not in sids: ds.add(f"wtp:{wid}:unknown_source:{ref}")
 corridors=d.get("corridors",[])
 for i,c in enumerate(corridors):
  pid=c.get("package_id",f"index-{i}")
  if pid not in pids: ds.add(f"corridor:{pid}:unknown_package")
  for f in ("economic_floor","validation_floor","target","ceiling_hypothesis","currency","tax_treatment","term","volume","valid_until","evidence_ids","confidence","below_floor_rule"):
   if not ok(c.get(f)) and c.get(f)!=0: ds.add(f"corridor:{pid}:missing_{f}")
  vals=[c.get(x) for x in ("economic_floor","validation_floor","target","ceiling_hypothesis")]
  if all(isinstance(z,(int,float)) for z in vals) and vals!=sorted(vals): ds.add(f"corridor:{pid}:invalid_order")
  for ref in c.get("evidence_ids",[]):
   if ref not in sids: ds.add(f"corridor:{pid}:unknown_source:{ref}")
 for i,r in enumerate(d.get("discount_rules",[])):
  rid=r.get("id",f"index-{i}")
  for f in ("reason_code","eligible_fence","max_rate","approver","floor_check","expiry","audit"):
   if not ok(r.get(f)) and r.get(f)!=0: ds.add(f"discount:{rid}:missing_{f}")
 for i,g in enumerate(d.get("guarantees",[])):
  gid=g.get("id",f"index-{i}")
  for f in ("claim","evidence","conditions","liability_cap","capacity_check","legal_status","owner"):
   if not ok(g.get(f)): ds.add(f"guarantee:{gid}:missing_{f}")
 scenarios=d.get("scenarios",[])
 for i,s in enumerate(scenarios):
  sid=s.get("id",f"index-{i}")
  for f in ("assumptions","demand","conversion","churn_or_refund","usage_support","discount","tax_channel","margin_cash","capacity","break_even","downside"):
   if not ok(s.get(f)) and s.get(f)!=0: ds.add(f"scenario:{sid}:missing_{f}")
 experiments=d.get("experiments",[])
 for i,x in enumerate(experiments):
  xid=x.get("id",f"index-{i}")
  for f in ("assumption","method","sample","rights_fairness","metric","baseline","success","kill","max_time","max_budget","owner","status"):
   if not ok(x.get(f)) and x.get(f)!=0: ds.add(f"experiment:{xid}:missing_{f}")
  if x.get("status") not in ("PROPOSED","PENDING_HUMAN_APPROVAL"): ds.add(f"experiment:{xid}:unauthorized_status")
 risks=d.get("risks",[]); seen=set()
 for i,r in enumerate(risks):
  typ=r.get("risk_type",f"index-{i}"); seen.add(typ)
  for f in ("statement","trigger","mitigation","contingency","owner","status"):
   if not ok(r.get(f)): ds.add(f"risk:{typ}:missing_{f}")
 for typ in RISK_TYPES-seen: ds.add(f"risks:missing_type:{typ}")
 miss=SECTIONS-set(d.get("output_sections",[]))
 if miss: ds.add("output_sections:missing:"+",".join(sorted(miss)))
 tests=d.get("tests",{})
 for t in TESTS:
  if tests.get(t)!="PASS": ds.add(f"test:{t}:not_pass")
 reviews=d.get("reviews",{})
 for r in REVIEWS:
  if reviews.get(r)!="PASS": gaps.add(f"review:{r}:not_pass")
 if reviews.get("FINAL_HUMAN_PRICE_DECISION")!="PENDING": ds.add("review:FINAL_HUMAN_PRICE_DECISION:must_be_pending")
 for f in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS): ds.add(f"forbidden_flag:{f}")
 states=set(d.get("forbidden_states",[])); states.add(d.get("published_state","DRAFT"))
 for s in sorted(states&FORBIDDEN_STATES): ds.add(f"forbidden_state:{s}")
 ready=not ds and not gaps
 return {"skill":"offer-pricing","state":"READY_FOR_HUMAN_PRICE_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"value_cases":len(values),"packages":len(packages),"price_metrics":len(metrics),"economics":len(economics),"market_wtp":len(wtp),"corridors":len(corridors),"scenarios":len(scenarios),"experiments":len(experiments),"risks":len(risks),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(reviews.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 value/WTP truth, cost accuracy, realized margin, legal compliance, customer outcome, token cost, duration or adoption."}
def main():
 if len(sys.argv)!=2: print("usage: evaluate_offer_pricing.py INPUT.json",file=sys.stderr); return 2
 r=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))); print(json.dumps(r,ensure_ascii=False,indent=2)); return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__": raise SystemExit(main())
