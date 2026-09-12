#!/usr/bin/env python3
import json,sys
from pathlib import Path
TESTS={"mandate_boundary","data_quality","model_coverage","segment_quality","estimate_fit","score_sensitivity","decision_boundary"}
QUALITY={"MEASURABLE","SUBSTANTIAL","DIFFERENTIABLE","ACCESSIBLE","ACTIONABLE","STABLE"}
RISK_TYPES={"PRIVACY_FAIRNESS","DATA_BIAS","MARKET_MODEL","STRATEGIC_FINANCIAL"}
REVIEWS={"MARKET_CUSTOMER","DATA_ANALYTICS","FINANCE_STRATEGY","LEGAL_PRIVACY"}
SECTIONS={"mandate_boundary","data_quality","model_card","segment_cards_tests","size_economics_fit","score_sensitivity","priority_validation","reviews_audit_refresh"}
STATES={"PRIORITY_CANDIDATE","VALIDATE_CANDIDATE","DEFER_CANDIDATE"}
FORBIDDEN_FLAGS={"population_fabricated","size_fabricated","growth_fabricated","share_fabricated","pain_fabricated","wtp_fabricated","access_fabricated","competition_fabricated","capability_fabricated","sample_called_population","denominator_hidden","coverage_hidden","overlap_hidden","unknown_hidden","missingness_hidden","bias_hidden","sensitivity_hidden","weights_manipulated","segment_forced","segment_merged_to_fit","segment_split_to_fit","protected_trait_used","sensitive_trait_used","proxy_discrimination","tiny_cell_exposed","row_identity_exposed","auto_targeted","auto_excluded","auto_funded","auto_priced","auto_contacted","auto_launched","auto_exited"}
FORBIDDEN_STATES={"TARGETED","EXCLUDED","FUNDED","PRICED","CONTACTED","LAUNCHED","EXITED","APPROVED"}
def ok(v): return v not in (None,"",[],{})
def evaluate(d):
 ds=set(); gaps=set(); m=d.get("mandate",{})
 for f in ("objective","decision","market_boundary","geography","as_of","horizon","unit","decision_owner","prohibited_uses","required_reviews"):
  if not ok(m.get(f)): ds.add(f"mandate:missing_{f}")
 sources=d.get("data_sources",[]); sids=set()
 for i,s in enumerate(sources):
  sid=s.get("id",f"index-{i}"); sids.add(sid)
  for f in ("locator","version","date","rights","frame","denominator","coverage","sample","missingness","bias","metric_definitions"):
   if not ok(s.get(f)): ds.add(f"source:{sid}:missing_{f}")
  if s.get("rights") not in ("AUTHORIZED","PUBLIC_TERMS_OK","INTERNAL_AUTHORIZED"): ds.add(f"source:{sid}:not_authorized")
 model=d.get("model",{})
 for f in ("method","bases","rationale","membership_rule","overlap_policy","unknown_policy","outlier_policy","minimum_cell","privacy_rule","stability_rule","refresh_rule"):
  if not ok(model.get(f)): ds.add(f"model:missing_{f}")
 segs=d.get("segments",[]); segids=set()
 for i,s in enumerate(segs):
  sid=s.get("id",f"index-{i}"); segids.add(sid)
  for f in ("name","definition","membership_rule","inclusion","exclusion","jobs","alternatives","evidence_ids","confidence"):
   if not ok(s.get(f)): ds.add(f"segment:{sid}:missing_{f}")
  for ref in s.get("evidence_ids",[]):
   if ref not in sids: ds.add(f"segment:{sid}:unknown_source:{ref}")
  tests=s.get("quality_tests",{})
  for q in QUALITY:
   if tests.get(q)!="PASS": ds.add(f"segment:{sid}:quality_{q}_not_pass")
 if not segs: ds.add("segments:missing")
 cov=d.get("coverage",{})
 for f in ("population_count_or_range","assigned_pct","overlap_pct","unknown_pct","reconciliation","as_of"):
  if not ok(cov.get(f)): ds.add(f"coverage:missing_{f}")
 if isinstance(cov.get("assigned_pct"),(int,float)) and isinstance(cov.get("unknown_pct"),(int,float)) and cov["assigned_pct"]+cov["unknown_pct"]<99.999: ds.add("coverage:not_reconciled")
 est=d.get("estimates",[])
 for i,e in enumerate(est):
  sid=e.get("segment_id",f"index-{i}")
  if sid not in segids: ds.add(f"estimate:{sid}:unknown_segment")
  for f in ("metric","low","base","high","unit","denominator","method","source_ids","base_year","horizon","confidence"):
   if not ok(e.get(f)) and e.get(f)!=0: ds.add(f"estimate:{sid}:missing_{f}")
  if all(isinstance(e.get(x),(int,float)) for x in ("low","base","high")) and not(e["low"]<=e["base"]<=e["high"]): ds.add(f"estimate:{sid}:invalid_range")
  for ref in e.get("source_ids",[]):
   if ref not in sids: ds.add(f"estimate:{sid}:unknown_source:{ref}")
 assessments=d.get("assessments",[])
 for i,a in enumerate(assessments):
  sid=a.get("segment_id",f"index-{i}")
  if sid not in segids: ds.add(f"assessment:{sid}:unknown_segment")
  for f in ("attractiveness","ability_to_win","evidence_ids","gaps"):
   if not ok(a.get(f)): ds.add(f"assessment:{sid}:missing_{f}")
  for ref in a.get("evidence_ids",[]):
   if ref not in sids: ds.add(f"assessment:{sid}:unknown_source:{ref}")
 score=d.get("scoring",{}); criteria=score.get("criteria",[])
 for f in ("normalization","missing_rule","thresholds","sensitivity_cases","rank_stability"):
  if not ok(score.get(f)): ds.add(f"scoring:missing_{f}")
 total=0
 for i,c in enumerate(criteria):
  for f in ("name","definition","weight","direction","scale"):
   if not ok(c.get(f)) and c.get(f)!=0: ds.add(f"criterion:{i}:missing_{f}")
  if isinstance(c.get("weight"),(int,float)): total+=c["weight"]
 if not criteria: ds.add("scoring:criteria_missing")
 if abs(total-100)>0.001: ds.add(f"scoring:weights_not_100:{total}")
 if len(score.get("sensitivity_cases",[]))<2: ds.add("scoring:insufficient_sensitivity")
 cands=d.get("candidates",[])
 for i,c in enumerate(cands):
  sid=c.get("segment_id",f"index-{i}")
  if sid not in segids: ds.add(f"candidate:{sid}:unknown_segment")
  if c.get("status") not in STATES: ds.add(f"candidate:{sid}:invalid_status")
  for f in ("trade_off","gaps","validation","owner"):
   if not ok(c.get(f)): ds.add(f"candidate:{sid}:missing_{f}")
 risks=d.get("risks",[]); seen=set()
 for i,r in enumerate(risks):
  typ=r.get("risk_type",f"index-{i}"); seen.add(typ)
  for f in ("statement","trigger","mitigation","owner","status"):
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
 if reviews.get("FINAL_HUMAN_SEGMENT_DECISION")!="PENDING": ds.add("review:FINAL_HUMAN_SEGMENT_DECISION:must_be_pending")
 for f in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS): ds.add(f"forbidden_flag:{f}")
 states=set(d.get("forbidden_states",[])); states.add(d.get("published_state","DRAFT"))
 for s in sorted(states&FORBIDDEN_STATES): ds.add(f"forbidden_state:{s}")
 ready=not ds and not gaps
 return {"skill":"market-segmentation","state":"READY_FOR_HUMAN_SEGMENT_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"segments":len(segs),"estimates":len(est),"assessments":len(assessments),"candidates":len(cands),"risks":len(risks),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(reviews.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 population truth, segment stability, estimate accuracy, decision impact, token cost, duration or adoption."}
def main():
 if len(sys.argv)!=2: print("usage: evaluate_market_segmentation.py INPUT.json",file=sys.stderr); return 2
 r=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))); print(json.dumps(r,ensure_ascii=False,indent=2)); return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__": raise SystemExit(main())
