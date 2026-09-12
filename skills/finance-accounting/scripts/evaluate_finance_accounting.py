#!/usr/bin/env python3
import json,sys
from pathlib import Path
TESTS={"mandate_sources","document_transaction_traceability","classification_journal_balance","period_cutoff_reconciliation","ar_ap_cash_budget","controls_sod_security","decision_boundary"}
REVIEWS={"ACCOUNTING_CONTROLLER","FINANCE_MANAGEMENT","TREASURY_PAYMENT_CONTROL","TAX_LEGAL_COMPLIANCE","DATA_SECURITY_PRIVACY","INTERNAL_CONTROL_AUDIT"}
RISK_TYPES={"FINANCIAL_STATEMENT_ACCURACY","PERIOD_CUTOFF_LOCK","CASH_LIQUIDITY_PAYMENT","TAX_LEGAL_COMPLIANCE","FRAUD_SOD_AUTHORITY","DATA_SECURITY_PRIVACY_CONTINUITY"}
SECTIONS={"document_control","source_document_transaction_ledger","classification_draft_journals","period_cutoff_reconciliations","ar_ap_cash_budget","controls_exceptions_risks","management_decisions_reviews","audit_change_log"}
RIGHTS={"AUTHORIZED","INTERNAL_AUTHORIZED","OWNER_AUTHORIZED","POLICY_AUTHORIZED","SYSTEM_AUTHORIZED","LEGAL_AUTHORIZED","CONSENTED"}
RECOMMENDATIONS={"POST_REVIEW","ADJUST_REVIEW","PAYMENT_REVIEW","BUDGET_REVIEW","TAX_REVIEW","REVISE","HOLD","INVESTIGATE_REVIEW"}
FORBIDDEN_FLAGS={"invoice_fabricated","receipt_fabricated","transaction_fabricated","vendor_fabricated","customer_fabricated","amount_fabricated","currency_fabricated","tax_fabricated","exchange_rate_fabricated","account_code_fabricated","journal_fabricated","balance_fabricated","bank_balance_fabricated","cash_balance_fabricated","revenue_fabricated","expense_fabricated","asset_fabricated","liability_fabricated","forecast_fabricated","budget_fabricated","source_fabricated","ocr_uncertainty_hidden","duplicate_document_counted","duplicate_transaction_counted","entity_mixed","currency_mixed","period_mixed","cutoff_bypassed","locked_period_modified","closed_period_reopened","debit_credit_unbalanced","coa_policy_bypassed","materiality_hidden","unsupported_reclass","unsupported_accrual","unsupported_tax_treatment","bank_reconciliation_bypassed","subledger_reconciliation_bypassed","unreconciled_difference_hidden","aging_bucket_manipulated","overdue_hidden","refund_chargeback_hidden","restricted_data_exposed","credential_exposed","pii_exposed","public_llm_unapproved","retention_bypassed","sod_bypassed","approval_limit_bypassed","payment_split_to_evade_limit","fraud_signal_hidden","management_override_hidden","going_concern_claim_fabricated","official_statement_claimed","audit_opinion_fabricated","review_bypassed","auto_journal_posted","auto_reclassified","auto_period_opened","auto_period_closed","auto_payment_approved","auto_payment_sent","auto_transfer_sent","auto_budget_changed","auto_tax_filed","auto_statement_published","auto_report_certified","auto_vendor_contacted","auto_customer_contacted"}
FORBIDDEN_STATES={"JOURNAL_POSTED","RECLASSIFIED","PERIOD_OPENED","PERIOD_CLOSED","PAYMENT_APPROVED","PAYMENT_SENT","TRANSFER_SENT","BUDGET_CHANGED","TAX_FILED","STATEMENT_PUBLISHED","REPORT_CERTIFIED","EXTERNAL_PARTY_CONTACTED"}
def ok(v):return v not in(None,"",[],{})
def fields(ds,p,obj,req):
 for f in req:
  if not ok(obj.get(f)):ds.add(f"{p}:missing_{f}")
def refs(ds,p,vals,known):
 for x in vals:
  if x not in known:ds.add(f"{p}:unknown_ref:{x}")
def evaluate(d):
 ds=set();gaps=set();m=d.get("mandate",{})
 fields(ds,"mandate",m,("purpose_audience_decision","entity_legal_reporting_scope","period_cutoff_timezone_currency","accounting_tax_basis","coa_policy_materiality","owner_controller_authorities","required_reviews","non_goals"))
 sources=d.get("sources",[]);sids=set()
 for i,x in enumerate(sources):
  xid=x.get("id",f"index-{i}");sids.add(xid)
  fields(ds,f"source:{xid}",x,("source_type","locator","version_as_of_hash","rights_purpose","freshness","confidence","system_of_record","supports"))
  if x.get("rights_purpose") not in RIGHTS:ds.add(f"source:{xid}:not_authorized")
 if len(sids)!=len(sources):ds.add("sources:duplicate_id")
 docs=d.get("documents",[]);dids=set()
 for i,x in enumerate(docs):
  xid=x.get("id",f"index-{i}");dids.add(xid)
  fields(ds,f"document:{xid}",x,("source_ids","entity_counterparty","document_date_period","currency_amount_tax","ocr_confidence","integrity_duplicate_status","transaction_links"));refs(ds,f"document:{xid}:source",x.get("source_ids",[]),sids)
 if len(dids)!=len(docs):ds.add("documents:duplicate_id")
 txs=d.get("transactions",[]);tids=set()
 for i,x in enumerate(txs):
  xid=x.get("id",f"index-{i}");tids.add(xid)
  fields(ds,f"transaction:{xid}",x,("document_ids","system_record","entity_counterparty","dates_period","currency_amount_tax","classification_status","evidence_uncertainty"));refs(ds,f"transaction:{xid}:document",x.get("document_ids",[]),dids)
 if len(tids)!=len(txs):ds.add("transactions:duplicate_id")
 journals=d.get("draft_journals",[]);jids=set()
 for i,x in enumerate(journals):
  xid=x.get("id",f"index-{i}");jids.add(xid)
  fields(ds,f"journal:{xid}",x,("transaction_ids","source_policy_ids","rationale","period_currency","debit_total","credit_total","account_tax_cost_lines","reviewer_role","human_state"));refs(ds,f"journal:{xid}:transaction",x.get("transaction_ids",[]),tids);refs(ds,f"journal:{xid}:source",x.get("source_policy_ids",[]),sids)
  if x.get("debit_total")!=x.get("credit_total"):ds.add(f"journal:{xid}:unbalanced")
  if x.get("human_state")!="PENDING":ds.add(f"journal:{xid}:human_state_not_pending")
 recs=d.get("reconciliations",[]);recids=set()
 for i,x in enumerate(recs):
  xid=x.get("id",f"index-{i}");recids.add(xid)
  fields(ds,f"reconciliation:{xid}",x,("area_populations","snapshot_dates","equation","tolerance_basis","matched_amount","unmatched_items","owner_role","resolution_evidence_state"))
 aging=d.get("aging_items",[])
 for i,x in enumerate(aging):fields(ds,f"aging:{x.get('id',i)}",x,("ar_ap","counterparty_document","due_age_bucket_basis","amount_currency","dispute_credit_refund_state","option_owner"))
 cash=d.get("cash_scenarios",[])
 for i,x in enumerate(cash):fields(ds,f"cash:{x.get('id',i)}",x,("scenario_type","actual_opening_source","horizon","inflows_outflows","closing_range","assumptions_sources_uncertainty","trigger_action_owner"))
 variances=d.get("budget_variances",[])
 for i,x in enumerate(variances):fields(ds,f"variance:{x.get('id',i)}",x,("entity_metric_period_currency","actual_source","budget_forecast_source","absolute_percent_denominator","driver_evidence_hypothesis","owner_action"))
 controls=d.get("controls",[]);cids=set()
 for i,x in enumerate(controls):
  xid=x.get("id",f"index-{i}");cids.add(xid);fields(ds,f"control:{xid}",x,("objective_type","owner_role","event_frequency","evidence","pass_fail","failure_action","residual_risk"))
 period=d.get("period_cutoff",{})
 fields(ds,"period_cutoff",period,("open_locked_closed_state","cutoff_basis","accrual_prepayment","fx_basis","intercompany_basis","exceptions_proposed_treatment","period_authority"))
 risks=d.get("risks",[]);seenr=set()
 for i,x in enumerate(risks):
  typ=x.get("risk_type",f"index-{i}");seenr.add(typ);fields(ds,f"risk:{typ}",x,("statement","likelihood","impact","trigger","mitigation","contingency","owner_role"))
 for typ in RISK_TYPES-seenr:ds.add(f"risks:missing_type:{typ}")
 decisions=d.get("decision_queue",[])
 for i,x in enumerate(decisions):
  xid=x.get("id",f"index-{i}");fields(ds,f"decision:{xid}",x,("recommendation","alternatives","evidence_source_ids","review_gaps","decision_owner_role","needed_by","human_state"))
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
 if rev.get("FINAL_HUMAN_FINANCE_ACCOUNTING_DECISION")!="PENDING":ds.add("review:FINAL_HUMAN_FINANCE_ACCOUNTING_DECISION:must_be_pending")
 for x in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS):ds.add(f"forbidden_flag:{x}")
 states=set(d.get("forbidden_states",[]));states.add(d.get("operational_state","DRAFT"))
 for x in sorted(states&FORBIDDEN_STATES):ds.add(f"forbidden_state:{x}")
 ready=not ds and not gaps
 return {"skill":"finance-accounting","state":"READY_FOR_HUMAN_FINANCE_ACCOUNTING_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"documents":len(docs),"transactions":len(txs),"draft_journals":len(journals),"reconciliations":len(recs),"aging_items":len(aging),"cash_scenarios":len(cash),"budget_variances":len(variances),"controls":len(controls),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(rev.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 accounting truth, financial accuracy, tax/legal compliance, control effectiveness, audit assurance, authorization, token cost or duration."}
def main():
 if len(sys.argv)!=2:print("usage: evaluate_finance_accounting.py INPUT.json",file=sys.stderr);return 2
 r=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")));print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__":raise SystemExit(main())
