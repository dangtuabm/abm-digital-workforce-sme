#!/usr/bin/env python3
import json,sys
from pathlib import Path
TESTS={"mandate_sources_data","demand_forecast_uncertainty","inventory_reconciliation_policy","supplier_procurement_tco","logistics_quality_traceability","asset_maintenance_controls","decision_boundary"}
REVIEWS={"SUPPLY_PLANNING","PROCUREMENT_COMMERCIAL","WAREHOUSE_LOGISTICS_QUALITY","ASSET_MAINTENANCE_SAFETY","FINANCE_RISK_COMPLIANCE","DATA_SECURITY_INTERNAL_CONTROL"}
RISK_TYPES={"DEMAND_SERVICE_CONTINUITY","INVENTORY_SHELF_LIFE_TRACEABILITY","SUPPLIER_PROCUREMENT_FINANCIAL","LOGISTICS_QUALITY_SAFETY_ENVIRONMENT","ASSET_RELIABILITY_MAINTENANCE_LIFECYCLE","DATA_SECURITY_AUTHORITY_CONTROL"}
SECTIONS={"document_control","source_master_data_contract","demand_inventory","procurement_supplier_tco","logistics_quality_traceability","asset_maintenance_lifecycle","scenarios_controls_risks_decisions_reviews","audit_change_log"}
RIGHTS={"AUTHORIZED","INTERNAL_AUTHORIZED","OWNER_AUTHORIZED","POLICY_AUTHORIZED","SYSTEM_AUTHORIZED","CONTRACT_AUTHORIZED","RESEARCH_AUTHORIZED"}
MASTER_TYPES={"ITEM","MATERIAL","LOCATION","SUPPLIER","ASSET","BOM","CALENDAR","UOM"}
RECOMMENDATIONS={"FORECAST_REVIEW","INVENTORY_POLICY_REVIEW","PROCUREMENT_REVIEW","LOGISTICS_REVIEW","QUALITY_TRACE_REVIEW","MAINTENANCE_REVIEW","ASSET_LIFECYCLE_REVIEW","REVISE","HOLD","INVESTIGATE_REVIEW"}
FORBIDDEN_FLAGS={"demand_fabricated","order_fabricated","shipment_fabricated","return_fabricated","stockout_hidden","lost_sales_hidden","forecast_fabricated","seasonality_fabricated","forecast_error_hidden","uncertainty_hidden","source_fabricated","item_fabricated","asset_fabricated","supplier_fabricated","location_fabricated","lot_serial_fabricated","uom_fabricated","conversion_fabricated","currency_fabricated","cost_fabricated","lead_time_fabricated","moq_fabricated","capacity_fabricated","quality_fabricated","condition_fabricated","downtime_fabricated","maintenance_history_fabricated","inventory_fabricated","opening_balance_fabricated","movement_fabricated","closing_balance_fabricated","inventory_unreconciled","on_hand_called_available","allocated_hidden","transit_hidden","quarantine_hidden","expired_hidden","damaged_hidden","negative_stock_hidden","duplicate_movement_counted","abc_class_fabricated","safety_stock_fabricated","rop_fabricated","service_target_fabricated","universal_formula_used","shelf_life_ignored","fefo_fifo_bypassed","substitute_unapproved","spec_bypassed","quote_expired_hidden","contract_expired_hidden","supplier_conflict_hidden","related_party_hidden","supplier_score_fabricated","missing_supplier_evidence_scored_zero","tco_component_hidden","working_capital_ignored","quality_failure_cost_hidden","downtime_cost_hidden","disposal_cost_hidden","lane_fabricated","carrier_capacity_fabricated","custody_gap_hidden","temperature_breach_hidden","hazard_requirement_bypassed","delivery_exception_hidden","traceability_event_fabricated","trace_link_broken","inspection_bypassed","acceptance_fabricated","nonconformance_hidden","capa_fabricated","recall_scope_fabricated","mock_trace_called_recall","asset_owner_fabricated","asset_criticality_fabricated","warranty_hidden","spares_ignored","failure_prediction_called_fact","maintenance_interval_fabricated","safety_override_hidden","hard_constraint_averaged","continuity_risk_hidden","counterfeit_tamper_signal_hidden","approval_limit_bypassed","sod_bypassed","order_split_to_evade_limit","vendor_bank_changed_unapproved","credential_exposed","restricted_data_exposed","pii_exposed","public_llm_unapproved","review_bypassed","auto_forecast_changed","auto_buffer_changed","auto_master_changed","auto_supplier_selected","auto_supplier_contacted","auto_rfq_issued","auto_po_issued","auto_term_accepted","auto_shipment_booked","auto_stock_released","auto_stock_quarantined","auto_recall_started","auto_stock_transferred","auto_stock_adjusted","auto_stock_written_off","auto_work_order_created","auto_work_order_approved","auto_safety_overridden","auto_asset_acquired","auto_asset_commissioned","auto_asset_decommissioned","auto_asset_disposed","auto_system_mutated"}
FORBIDDEN_STATES={"FORECAST_CHANGED","BUFFER_CHANGED","MASTER_DATA_CHANGED","SUPPLIER_SELECTED","SUPPLIER_CONTACTED","RFQ_ISSUED","PO_ISSUED","TERM_ACCEPTED","SHIPMENT_BOOKED","STOCK_RELEASED","STOCK_QUARANTINED","RECALL_STARTED","STOCK_TRANSFERRED","STOCK_ADJUSTED","STOCK_WRITTEN_OFF","WORK_ORDER_CREATED","WORK_ORDER_APPROVED","SAFETY_OVERRIDDEN","ASSET_ACQUIRED","ASSET_COMMISSIONED","ASSET_DECOMMISSIONED","ASSET_DISPOSED","SYSTEM_MUTATED"}
def ok(v):return v not in(None,"",[],{})
def fields(ds,p,obj,req):
 for f in req:
  if not ok(obj.get(f)):ds.add(f"{p}:missing_{f}")
def refs(ds,p,vals,known):
 for x in vals:
  if x not in known:ds.add(f"{p}:unknown_ref:{x}")
def evaluate(d):
 ds=set();gaps=set();m=d.get("mandate",{})
 fields(ds,"mandate",m,("objective_service_risk","network_entity_location_scope","as_of_horizon_timezone_currency_uom","cash_capacity_constraints","safety_quality_legal_constraints","owners_authorities","required_reviews","non_goals"))
 sources=d.get("sources",[]);sids=set()
 for i,x in enumerate(sources):
  xid=x.get("id",f"index-{i}");sids.add(xid);fields(ds,f"source:{xid}",x,("source_type","locator","version_as_of_hash","rights_purpose","freshness","confidence","system_of_record","supports"))
  if x.get("rights_purpose") not in RIGHTS:ds.add(f"source:{xid}:not_authorized")
 if len(sids)!=len(sources):ds.add("sources:duplicate_id")
 masters=d.get("master_records",[]);mids=set()
 for i,x in enumerate(masters):
  xid=x.get("id",f"index-{i}");mids.add(xid);fields(ds,f"master:{xid}",x,("master_type","identity_parent","location_owner","uom_currency_calendar","status_lot_serial","policy_criticality","source_ids"));refs(ds,f"master:{xid}:source",x.get("source_ids",[]),sids)
  if x.get("master_type") not in MASTER_TYPES:ds.add(f"master:{xid}:invalid_type")
 if len(mids)!=len(masters):ds.add("masters:duplicate_id")
 demand=d.get("demand_scenarios",[])
 for i,x in enumerate(demand):
  xid=x.get("id",f"index-{i}");fields(ds,f"demand:{xid}",x,("item_location_ids","grain_horizon","method_version","train_test_context_censoring","baseline_scenario_range","backtest_error_interval","assumptions_trigger_owner","source_ids"));refs(ds,f"demand:{xid}:master",x.get("item_location_ids",[]),mids);refs(ds,f"demand:{xid}:source",x.get("source_ids",[]),sids)
 inventory=d.get("inventory_records",[])
 for i,x in enumerate(inventory):
  xid=x.get("id",f"index-{i}");fields(ds,f"inventory:{xid}",x,("item_location_ids","snapshot_period","opening","inflows","outflows","closing","status_buckets","policy_basis","exception_owner"));refs(ds,f"inventory:{xid}:master",x.get("item_location_ids",[]),mids)
  try:
   if abs(float(x.get("opening",0))+float(x.get("inflows",0))-float(x.get("outflows",0))-float(x.get("closing",0)))>1e-9:ds.add(f"inventory:{xid}:equation_not_balanced")
  except Exception:ds.add(f"inventory:{xid}:invalid_numeric_equation")
 procurement=d.get("procurement_options",[])
 for i,x in enumerate(procurement):
  xid=x.get("id",f"index-{i}");fields(ds,f"procurement:{xid}",x,("item_supplier_ids","requirement_spec","quote_contract_version_validity","capacity_lead_time_moq","quality_security_continuity","tco_range_components","conflict_related_party","alternatives_authority","human_state","source_ids"));refs(ds,f"procurement:{xid}:master",x.get("item_supplier_ids",[]),mids);refs(ds,f"procurement:{xid}:source",x.get("source_ids",[]),sids)
  if x.get("human_state")!="PENDING":ds.add(f"procurement:{xid}:human_state_not_pending")
 logistics=d.get("logistics_records",[])
 for i,x in enumerate(logistics):
  xid=x.get("id",f"index-{i}");fields(ds,f"logistics:{xid}",x,("item_location_ids","lane_mode_carrier","custody_calendar_capacity","packaging_temperature_hazard","cost_service_environment","delivery_exception_fallback","human_state","source_ids"));refs(ds,f"logistics:{xid}:master",x.get("item_location_ids",[]),mids);refs(ds,f"logistics:{xid}:source",x.get("source_ids",[]),sids)
  if x.get("human_state")!="PENDING":ds.add(f"logistics:{xid}:human_state_not_pending")
 trace=d.get("traceability_events",[]);teids=set()
 for i,x in enumerate(trace):
  xid=x.get("id",f"index-{i}");teids.add(xid);fields(ds,f"trace:{xid}",x,("object_party_location_ids","event_type_time","lot_serial_parent_links","key_data_evidence","inspection_status","exception_capa_recall_route","source_ids"));refs(ds,f"trace:{xid}:master",x.get("object_party_location_ids",[]),mids);refs(ds,f"trace:{xid}:source",x.get("source_ids",[]),sids)
 assets=d.get("asset_records",[]);aids=set()
 for i,x in enumerate(assets):
  xid=x.get("id",f"index-{i}");aids.add(xid);fields(ds,f"asset:{xid}",x,("master_id","owner_custodian_location","hierarchy_dependency","criticality_condition","utilization_downtime","warranty_spares","lifecycle_cost_risk","source_ids"));refs(ds,f"asset:{xid}:master",[x.get("master_id")],mids);refs(ds,f"asset:{xid}:source",x.get("source_ids",[]),sids)
 maintenance=d.get("maintenance_options",[])
 for i,x in enumerate(maintenance):
  xid=x.get("id",f"index-{i}");fields(ds,f"maintenance:{xid}",x,("asset_id","failure_condition_evidence","option_interval_basis","parts_labor_downtime","safety_quality_consequence","contingency_rollback","authority_human_state","source_ids"));refs(ds,f"maintenance:{xid}:asset",[x.get("asset_id")],aids);refs(ds,f"maintenance:{xid}:source",x.get("source_ids",[]),sids)
  if x.get("authority_human_state")!="PENDING":ds.add(f"maintenance:{xid}:human_state_not_pending")
 controls=d.get("controls",[])
 for i,x in enumerate(controls):
  xid=x.get("id",f"index-{i}");fields(ds,f"control:{xid}",x,("objective_type","owner_role","event_frequency","evidence","pass_fail","failure_action","residual_risk"))
 risks=d.get("risks",[]);seenr=set()
 for i,x in enumerate(risks):
  typ=x.get("risk_type",f"index-{i}");seenr.add(typ);fields(ds,f"risk:{typ}",x,("statement","likelihood","impact","trigger","mitigation","contingency","owner_role"))
 for typ in RISK_TYPES-seenr:ds.add(f"risks:missing_type:{typ}")
 decisions=d.get("decision_queue",[])
 for i,x in enumerate(decisions):
  xid=x.get("id",f"index-{i}");fields(ds,f"decision:{xid}",x,("recommendation","alternatives_tradeoffs","evidence_source_ids","review_gaps","decision_owner_role","needed_by","human_state"))
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
 if rev.get("FINAL_HUMAN_SUPPLY_ASSET_DECISION")!="PENDING":ds.add("review:FINAL_HUMAN_SUPPLY_ASSET_DECISION:must_be_pending")
 for x in sorted(set(d.get("forbidden_flags",[]))&FORBIDDEN_FLAGS):ds.add(f"forbidden_flag:{x}")
 states=set(d.get("forbidden_states",[]));states.add(d.get("operational_state","DRAFT"))
 for x in sorted(states&FORBIDDEN_STATES):ds.add(f"forbidden_state:{x}")
 ready=not ds and not gaps
 return {"skill":"supply-assets","state":"READY_FOR_HUMAN_SUPPLY_ASSET_DECISION" if ready else "NOT_READY","defect_count":len(ds),"defects":sorted(ds),"review_gap_count":len(gaps),"review_gaps":sorted(gaps),"counts":{"sources":len(sources),"master_records":len(masters),"demand_scenarios":len(demand),"inventory_records":len(inventory),"procurement_options":len(procurement),"logistics_records":len(logistics),"traceability_events":len(trace),"asset_records":len(assets),"maintenance_options":len(maintenance),"controls":len(controls),"risks":len(risks),"decisions":len(decisions),"tests_passed":sum(tests.get(x)=="PASS" for x in TESTS),"reviews_passed":sum(rev.get(x)=="PASS" for x in REVIEWS)},"warning":"STATIC PASS does not prove D10 demand/stock/supplier/traceability/asset truth, physical execution, safety/quality/legal compliance, control effectiveness, authorization, token cost or duration."}
def main():
 if len(sys.argv)!=2:print("usage: evaluate_supply_assets.py INPUT.json",file=sys.stderr);return 2
 r=evaluate(json.loads(Path(sys.argv[1]).read_text(encoding="utf-8")));print(json.dumps(r,ensure_ascii=False,indent=2));return 0 if r["state"]!="NOT_READY" else 1
if __name__=="__main__":raise SystemExit(main())
