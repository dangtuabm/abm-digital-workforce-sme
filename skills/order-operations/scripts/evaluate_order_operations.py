#!/usr/bin/env python3
import json,sys
from pathlib import Path

TESTS={"mandate_master_policy_sources","identity_dedup_idempotency","lifecycle_inventory_fulfilment","shipment_delivery_sla","payment_cod_reconciliation","return_refund_exception","decision_boundary"}
REVIEWS={"ORDER_MANAGEMENT_OWNER","FULFILLMENT_INVENTORY_OWNER","LOGISTICS_CARRIER_OWNER","CUSTOMER_SERVICE_RETURNS_OWNER","FINANCE_TAX_PAYMENT_OWNER","DATA_SECURITY_COMPLIANCE"}
RISK_TYPES={"ORDER_IDENTITY_DUPLICATE_SUSPICIOUS","PRICE_TAX_PAYMENT_AUTHORIZATION","INVENTORY_ALLOCATION_FULFILMENT","CARRIER_DELIVERY_PROOF_COD","RETURN_REFUND_COMPENSATION","DATA_PRIVACY_SECURITY_CONTINUITY"}
SECTIONS={"document_control","master_policy_state_register","canonical_order_event_ledger","order_fulfilment_shipment_lifecycle","payment_cod_reconciliation","return_refund_exceptions","metrics_risks_decisions_reviews","audit_change_log"}
RIGHTS={"PUBLIC_OFFICIAL","INTERNAL_AUTHORIZED","OWNER_AUTHORIZED","POLICY_AUTHORIZED","CONTRACT_AUTHORIZED","FINANCE_AUTHORIZED","CUSTOMER_AUTHORIZED"}
OBJECTS={"ORDER","ORDER_LINE","PACKAGE","SHIPMENT","PAYMENT","COD_SETTLEMENT","RETURN","RETURN_LINE","REFUND","EXCEPTION"}
RECOMMENDATIONS={"ORDER_EXCEPTION_REVIEW","INVENTORY_FULFILMENT_REVIEW","DELIVERY_CARRIER_REVIEW","PAYMENT_COD_RECONCILIATION_REVIEW","RETURN_REFUND_REVIEW","CUSTOMER_RECOVERY_REVIEW","DATA_CONTROL_REVIEW","REVISE","HOLD"}
FORBIDDEN_FLAGS={
"entity_fabricated","channel_fabricated","order_type_fabricated","jurisdiction_fabricated","source_fabricated","policy_fabricated","policy_version_fabricated","master_fabricated","master_version_fabricated","system_of_record_fabricated","canonical_id_fabricated","source_id_fabricated","customer_id_fabricated","order_id_fabricated","order_line_id_fabricated","sku_fabricated","uom_fabricated","package_id_fabricated","shipment_id_fabricated","tracking_id_fabricated","payment_id_fabricated","cod_id_fabricated","return_id_fabricated","refund_id_fabricated","event_fabricated","event_time_fabricated","actor_fabricated","state_fabricated","state_transition_fabricated","idempotency_key_fabricated","duplicate_silently_merged","collision_hidden","late_event_overwritten","out_of_order_event_hidden","grain_mixed","order_state_applied_to_lines","source_priority_fabricated","customer_fabricated","address_fabricated","recipient_fabricated","phone_exposed","pii_exposed","credential_exposed","payment_data_exposed","public_llm_unapproved","price_fabricated","discount_fabricated","tax_fabricated","currency_fabricated","fx_fabricated","fee_fabricated","rounding_fabricated","quantity_fabricated","stock_fabricated","stock_promise_fabricated","inventory_adjustment_fabricated","fraud_verdict_fabricated","suspicious_called_fraud","acceptance_fabricated","allocation_fabricated","substitution_fabricated","backorder_fabricated","split_merge_link_missing","quantity_mismatch_hidden","pick_fabricated","pack_fabricated","qc_fabricated","weight_fabricated","label_fabricated","handover_fabricated","carrier_fabricated","service_level_fabricated","milestone_fabricated","tracking_fabricated","delivery_attempt_fabricated","delivery_proof_fabricated","delivered_fabricated","lost_damaged_fabricated","rto_fabricated","sla_fabricated","sla_pause_fabricated","promise_variance_hidden","payment_state_fabricated","payment_capture_fabricated","cod_collected_fabricated","cod_statement_fabricated","bank_receipt_fabricated","settlement_fabricated","ledger_posting_fabricated","reconciliation_fabricated","tolerance_fabricated","variance_hidden","refund_fabricated","credit_note_fabricated","compensation_fabricated","return_request_fabricated","return_eligibility_fabricated","rma_authorization_fabricated","return_received_fabricated","inspection_fabricated","condition_fabricated","disposition_fabricated","return_reason_fabricated","complaint_hidden","exception_hidden","root_cause_claimed_without_test","metric_formula_fabricated","denominator_mixed","review_bypassed","auto_order_created","auto_order_updated","auto_order_deleted","auto_order_accepted","auto_order_cancelled","auto_order_held","auto_order_released","auto_address_changed","auto_price_changed","auto_discount_changed","auto_tax_changed","auto_sku_changed","auto_quantity_changed","auto_stock_reserved","auto_stock_released","auto_inventory_adjusted","auto_substitution_chosen","auto_carrier_booked","auto_carrier_cancelled","auto_label_issued","auto_payment_captured","auto_payment_voided","auto_refund_issued","auto_credit_issued","auto_compensation_issued","auto_cod_moved","auto_ledger_posted","auto_customer_contacted","auto_carrier_contacted","auto_return_approved","auto_exception_closed","auto_dispute_closed","audit_log_mutated","evidence_altered","evidence_deleted"
}
FORBIDDEN_STATES={"ORDER_CREATED","ORDER_UPDATED","ORDER_DELETED","ORDER_ACCEPTED","ORDER_CANCELLED","ORDER_HELD","ORDER_RELEASED","ADDRESS_CHANGED","PRICE_CHANGED","DISCOUNT_CHANGED","TAX_CHANGED","SKU_CHANGED","QUANTITY_CHANGED","STOCK_RESERVED","STOCK_RELEASED","INVENTORY_ADJUSTED","SUBSTITUTION_CHOSEN","CARRIER_BOOKED","CARRIER_CANCELLED","LABEL_ISSUED","PAYMENT_CAPTURED","PAYMENT_VOIDED","REFUND_ISSUED","CREDIT_ISSUED","COMPENSATION_ISSUED","COD_MOVED","LEDGER_POSTED","CUSTOMER_CONTACTED","CARRIER_CONTACTED","RETURN_APPROVED","EXCEPTION_CLOSED","DISPUTE_CLOSED","AUDIT_LOG_MUTATED","EVIDENCE_ALTERED","EVIDENCE_DELETED"}

def ok(v): return v not in (None,"",[],{})
def fields(ds,p,obj,req):
 for f in req:
  if not ok(obj.get(f)): ds.add(f"{p}:missing_{f}")
def refs(ds,p,vals,known):
 for x in vals:
  if x not in known: ds.add(f"{p}:unknown_ref:{x}")

def evaluate(d):
 ds=set(); gaps=set(); m=d.get("mandate",{})
 fields(ds,"mandate",m,("entity_channels_order_types","geography_jurisdiction","purpose_as_of_horizon","systems_of_record","owners_authorities_limits_slas","privacy_retention","non_goals"))
 sources=d.get("sources",[]); sids=set()
 for i,x in enumerate(sources):
  xid=x.get("id",f"index-{i}"); sids.add(xid); fields(ds,f"source:{xid}",x,("source_type","locator","version_effective_as_of","rights_access","status_scope","owner_authority","supports"))
  if x.get("rights_access") not in RIGHTS: ds.add(f"source:{xid}:not_authorized")
 if len(sids)!=len(sources): ds.add("sources:duplicate_id")
 contracts=d.get("object_contracts",[]); cids=set()
 for i,x in enumerate(contracts):
  xid=x.get("id",f"index-{i}"); cids.add(xid); fields(ds,f"contract:{xid}",x,("object_type","canonical_source_id_rules","system_of_record","grain_identity_keys","state_transition_contract","occurred_received_timezone_rule","idempotency_retry_rule","late_conflict_rule","source_ids","owner_role")); refs(ds,f"contract:{xid}:source",x.get("source_ids",[]),sids)
  if x.get("object_type") not in OBJECTS: ds.add(f"contract:{xid}:invalid_object_type")
 if len(cids)!=len(contracts): ds.add("object_contracts:duplicate_id")
 events=d.get("events",[]); eids=set()
 for i,x in enumerate(events):
  xid=x.get("id",f"index-{i}"); eids.add(xid); fields(ds,f"event:{xid}",x,("event_idempotency_key","object_contract_ids","object_canonical_source_ids","source_id","occurred_received_timezone","actor_source","from_to_state","sku_uom_quantity","amount_currency","evidence_hash","duplicate_late_conflict_status")); refs(ds,f"event:{xid}:contract",x.get("object_contract_ids",[]),cids); refs(ds,f"event:{xid}:source",[x.get("source_id")],sids)
 if len(eids)!=len(events): ds.add("events:duplicate_id")
 life=d.get("lifecycle_items",[]); lids=set()
 for i,x in enumerate(life):
  xid=x.get("id",f"index-{i}"); lids.add(xid); fields(ds,f"lifecycle:{xid}",x,("order_line_package_shipment_ids","acceptance_policy_source_ids","allocation_backorder_split_substitution","ordered_cancelled_open_fulfilled_quantities","pick_pack_qc","handover_carrier_tracking","delivery_milestone_proof","promise_sla_variance","event_ids","owner_exception_state")); refs(ds,f"lifecycle:{xid}:source",x.get("acceptance_policy_source_ids",[]),sids); refs(ds,f"lifecycle:{xid}:event",x.get("event_ids",[]),eids)
 recs=d.get("reconciliations",[]); rids=set()
 for i,x in enumerate(recs):
  xid=x.get("id",f"index-{i}"); rids.add(xid); fields(ds,f"reconciliation:{xid}",x,("order_invoice_payment_shipment_proof_ids","gross_discount_tax_shipping_fee_refund","expected_actual_net","payment_cod_statement","bank_remittance","ledger_handoff","currency_dates_tolerance_basis","variance_owner_state","source_ids")); refs(ds,f"reconciliation:{xid}:source",x.get("source_ids",[]),sids)
 returns=d.get("returns",[]); rtids=set()
 for i,x in enumerate(returns):
  xid=x.get("id",f"index-{i}"); rtids.add(xid); fields(ds,f"return:{xid}",x,("request_reason_source","eligibility_policy_jurisdiction","authorization_state","item_serial_condition","receive_inspect_disposition","refund_replacement_credit_compensation_options","authority_limit","evidence_state","source_ids")); refs(ds,f"return:{xid}:source",x.get("source_ids",[]),sids)
 exc=d.get("exceptions",[])
 for i,x in enumerate(exc):
  xid=x.get("id",f"index-{i}"); fields(ds,f"exception:{xid}",x,("fact_hypothesis","object_event_evidence_refs","severity_urgency_basis","impact","containment_option","root_cause_test","owner_sla_escalation","decision_rollback","human_state"))
  if x.get("human_state")!="PENDING": ds.add(f"exception:{xid}:human_state_not_pending")
 metrics=d.get("metrics",[])
 for i,x in enumerate(metrics):
  xid=x.get("id",f"index-{i}"); fields(ds,f"metric:{xid}",x,("name_grain","formula","numerator_denominator","inclusion_exclusion","cohort_window_timezone","source_ids","freshness","owner_threshold_basis")); refs(ds,f"metric:{xid}:source",x.get("source_ids",[]),sids)
 risks=d.get("risks",[]); seen=set()
 for i,x in enumerate(risks):
  typ=x.get("risk_type",f"index-{i}"); seen.add(typ); fields(ds,f"risk:{typ}",x,("statement","likelihood","impact","trigger","mitigation","contingency","owner_role"))
 for typ in RISK_TYPES-seen: ds.add(f"risks:missing_type:{typ}")
 decisions=d.get("decision_queue",[])
 for i,x in enumerate(decisions):
  xid=x.get("id",f"index-{i}"); fields(ds,f"decision:{xid}",x,("recommendation","issue_options","evidence_source_ids","review_gaps","decision_owner_role","needed_by","human_state")); refs(ds,f"decision:{xid}:source",x.get("evidence_source_ids",[]),sids)
  if x.get("recommendation") not in RECOMMENDATIONS: ds.add(f"decision:{xid}:invalid_recommendation")
  if x.get("human_state")!="PENDING": ds.add(f"decision:{xid}:human_state_not_pending")
 missing=SECTIONS-set(d.get("output_sections",[]))
 if missing: ds.add("output_sections:missing:"+",".join(sorted(missing)))
 tests=d.get("tests",{})
 for x in TESTS:
  if tests.get(x)!="PASS": ds.add(f"test:{x}:not_pass")
 rev=d.get("reviews",{})
 for x in REVIEWS:
  if rev.get(x)!="PASS": gaps.add(f"review:{x}:not_pass")
 if rev.get("FINAL_HUMAN_ORDER_OPERATIONS_DECISION")!="PENDING": ds.add("review:FINAL_HUMAN_ORDER_OPERATIONS_DECISION:must_be_pending")
 for x in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS): ds.add(f"forbidden_flag:{x}")
 states=set(d.get("forbidden_states",[])); states.add(d.get("operational_state","DRAFT"))
 for x in sorted(states&FORBIDDEN_STATES): ds.add(f"forbidden_state:{x}")
 ready=not ds and not gaps
 return {"skill":"order-operations","state":"READY_FOR_HUMAN_ORDER_OPERATIONS_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"object_contracts":len(contracts),"events":len(events),"lifecycle_items":len(life),"reconciliations":len(recs),"returns":len(returns),"exceptions":len(exc),"metrics":len(metrics),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(rev.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 source/master/event truth, production SoR state, inventory/payment/COD/ledger truth, policy/law applicability, customer/carrier outcome, authorization, token cost or duration."}

def main():
 if len(sys.argv)!=2: print("usage: evaluate_order_operations.py INPUT.json",file=sys.stderr); return 2
 result=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))); print(json.dumps(result,ensure_ascii=False,indent=2)); return 0 if result["state"]!="NOT_READY" else 1
if __name__=="__main__": raise SystemExit(main())
