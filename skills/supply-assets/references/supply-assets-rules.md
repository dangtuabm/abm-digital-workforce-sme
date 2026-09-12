# Supply & Asset Rules — v2.3

## 1. Thứ tự sự thật

1. Applicable safety, quality, product, environmental, trade, customs and asset requirements current for item/location/jurisdiction.
2. Approved business policy, contracts/specifications, service goals, risk appetite, asset strategy and authority matrix.
3. Reconciled ERP/WMS/TMS/EAM, physical-count/inspection/IoT and immutable transaction snapshots.
4. Versioned supplier/carrier/maintenance evidence and authorized market data.
5. Model output, manual assertion and unverified document extraction — labelled, never promoted without review.

ISO 55000, GS1 traceability and NIST supply-chain-risk guidance are principle references only; local requirements and approved operational truth prevail.

## 2. Data and identity contract

- Scope: entity, network, location, item/material/SKU, lot/batch/serial, asset, supplier and time horizon.
- Measures: UOM conversion, transaction/base currency, calendar/timezone, quantity/status, cost and service metric.
- Evidence: source/version/as-of/hash/rights/freshness/confidence, system of record and transformation lineage.
- Authority: planner, buyer, approver, receiver, inspector, inventory controller, maintainer, custodian, disposer and reviewer SOD.

Unknown identity, conversion, status or freshness stays UNKNOWN and blocks material recommendation.

## 3. Demand and inventory rules

- Preserve orders, shipments, lost sales/stockouts, returns, promotions, one-offs, substitutions and censoring separately.
- Forecast declares grain/horizon/method/version/train-test windows/error/interval/assumptions and comparison baseline.
- Inventory reconciles opening, all movement types and closing; do not net quarantine, expired, damaged or unknown into available.
- Safety stock, ROP, review cycle, ABC/XYZ, FIFO/FEFO and substitution depend on approved service, variability, shelf life, capacity and policy.
- Every recommendation has scenario/sensitivity, trigger, owner and rollback; no automatic master-data or buffer change.

## 4. Procurement and supplier rules

- Requirement/specification, quantity/UOM, delivery, acceptance, warranty/service, data/security and applicable compliance criteria precede comparison.
- Preserve quote/contract version, validity, capacity, lead-time distribution, MOQ, quality, continuity, concentration, conflict and related-party evidence.
- TCO separates price, freight, duty/tax basis, storage, working capital, quality failure, downtime, integration, maintenance and disposal as applicable.
- Supplier score/weight is approved and sensitivity-tested; missing evidence is not zero.
- Draft RFQ/PO/award options remain PENDING; no contact, acceptance, bank-master change or purchase commitment.

## 5. Logistics, quality and traceability rules

- Lane/mode/carrier/custody/calendar/capacity, packaging/temperature/hazard, delivery window and fallback are contextual.
- Trace objects, parties, locations and critical events with key data; keep lot/serial and transformation/aggregation links.
- Receipt is not acceptance; inspection, quarantine, release, nonconformance, CAPA and recall require authorized states/evidence.
- Mock trace tests completeness, speed and affected-scope accuracy without executing recall.

## 6. Asset and maintenance rules

- Asset register contains identity, hierarchy, owner/custodian/location, criticality, condition, utilization, downtime, warranty, spares, cost and dependencies.
- Lifecycle covers need/acquire/receive/commission/operate/maintain/renew/decommission/dispose with authority and evidence.
- Maintenance option states failure mode/condition evidence, safety consequence, interval basis, parts/labor/downtime, contingency and work authority.
- Forecasted failure is not fact; no work order, safety override, commissioning or disposal without qualified approval.

## 7. Control and scenario rules

- Keep requisition, sourcing, approval, receipt, inspection, inventory adjustment, invoice, payment, custody, maintenance and disposal duties separated.
- Detect duplicate/order split, master/bank change, conflict, counterfeit/tamper, unauthorized substitute, stock adjustment/write-off and unsafe override.
- Optimize across cost/cash/service/quality/safety/capacity/environment/continuity; hard constraints cannot be averaged away.
- Each scenario has baseline, assumptions, uncertainty, sensitivity, trigger, guardrail, owner and stop/rollback rule.

## 8. Stop conditions

Stop at NOT_READY for missing identity/UOM/source/authority, unreconciled material stock, unvalidated forecast, hidden quarantine/expiry/defect, unsupported supplier/asset claim, safety/quality conflict or execution request.

Final state is READY_FOR_HUMAN_SUPPLY_ASSET_DECISION; procurement, physical, maintenance and system actions remain outside.
