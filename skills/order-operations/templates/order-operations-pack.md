# ORDER-TO-CASH & AFTER-SALES CONTROL PACK

## 1. Document control / mandate

Entity · channels/order types · geography/jurisdiction · purpose · as-of/horizon · SoR per object · policy/master versions · owner/authority/approval limits · SLAs · privacy class · non-goals · version/hash.

## 2. Master, policy và state register

| ID | Type | Source/SoR | Version/effective date | Scope | Owner/authority | States/transitions or rule | Conflict/TBD |
|---|---|---|---|---|---|---|---|

## 3. Canonical order-event ledger

| Event/idempotency key | Object/type/canonical/source ID | Channel | Occurred/received/timezone | Actor/source | From/to state | SKU/UOM/qty | Amount/currency | Evidence/hash | Duplicate/late/conflict |
|---|---|---|---|---|---|---|---|---|---|

## 4. Order–fulfilment–shipment lifecycle

| Order/line/package/shipment IDs | Acceptance/policy | Allocation/backorder/split/substitution | Pick/pack/QC | Handover/carrier/tracking | Delivery milestone/proof | Promise/SLA variance | Owner/exception |
|---|---|---|---|---|---|---|---|

## 5. Payment/COD reconciliation

| Order/invoice/payment/shipment/proof IDs | Gross/discount/tax/shipping/fee | Expected net | Payment/COD statement | Bank/remittance | Ledger handoff | Currency/date/tolerance | Variance/owner/state |
|---|---|---|---|---|---|---|---|

## 6. Return/RMA/refund và exceptions

| ID | Request/reason/source | Eligibility/policy/jurisdiction | Authorization | Item/serial/condition | Receive/inspect/disposition | Refund/replacement/credit option | Authority/limit | Evidence/state |
|---|---|---|---|---|---|---|---|---|

Exception queue: fact/hypothesis · object/event/evidence · severity/urgency · impact · containment · root-cause test · owner/SLA/escalation · decision/rollback · human state.

## 7. Metrics, risks, decisions và reviews

Metric register: grain/formula/numerator/denominator/inclusion/window/timezone/source/freshness/owner/threshold. Ghi đủ six risks, decision queue và six reviews. Final: `FINAL_HUMAN_ORDER_OPERATIONS_DECISION = PENDING`.

## 8. Audit/change log

Version · timestamp · source snapshots/hashes · mapping/state/policy changes · reconciliation runs · reviewer · unresolved TBD/conflicts · prohibited-action check · next authorized action.
