# ORDER OPERATIONS RULES

## 1. Object, grain và System of Record

- Tách object: `order`, `order_line`, `package`, `shipment`, `payment`, `cod_settlement`, `return`, `return_line`, `refund`, `exception`.
- Mỗi object có canonical ID, source ID, channel, SoR, version, occurred/received timestamp + timezone, actor/source và evidence/hash.
- Không dùng order-level state để suy state của mọi line/package/payment/return. Split/merge/replacement/RTO phải có parent-child link và quantity conservation.
- Event key phải idempotent. Retry giữ cùng business event; collision hoặc late/out-of-order event vào exception, không silent overwrite.

## 2. State contracts gợi ý

Tên state phải map về state thật của doanh nghiệp; không tự cập nhật production:

- Order: `RECEIVED`, `VALIDATION_HOLD`, `ACCEPTED`, `PARTIAL`, `FULFILLED`, `CANCEL_PENDING`, `CANCELLED`, `CLOSED`.
- Line: `OPEN`, `RESERVED`, `BACKORDERED`, `PICKED`, `PACKED`, `SHIPPED`, `DELIVERED`, `RETURNED`, `CANCELLED`.
- Shipment: `PLANNED`, `HANDED_OVER`, `IN_TRANSIT`, `DELIVERY_EXCEPTION`, `DELIVERED`, `LOST_DAMAGED`, `RTO`.
- Payment/COD: `PENDING`, `AUTHORIZED`, `CAPTURED`, `COD_PENDING`, `COD_COLLECTED`, `SETTLEMENT_PENDING`, `RECONCILED`, `VARIANCE`, `REFUND_PENDING`, `REFUNDED`.
- Return: `REQUESTED`, `ELIGIBILITY_REVIEW`, `AUTHORIZED`, `IN_TRANSIT`, `RECEIVED`, `INSPECTED`, `DISPOSITION_PENDING`, `CLOSED`.

## 3. Trace và reconciliation

Trace bắt buộc: channel order → canonical order/line → acceptance/policy → allocation → pick/pack/package → handover/shipment/milestone/proof → invoice/payment/COD statement/bank/ledger → return/inspection/refund → exception/decision.

- Quantity: ordered = cancelled + backordered/open + fulfilled, theo rule/source; packed/shipped/delivered/returned phải reconcile theo line/package.
- Value: gross − approved discount + tax + shipping/fee − refund/credit = expected net theo policy/source. Không bịa formula, rounding, tolerance hay FX.
- COD: delivered/COD-collected evidence → carrier statement → remittance/bank receipt → fee/tax → ledger handoff. `DELIVERED` không tự tạo `COD_COLLECTED` hay `RECONCILED`.
- Return/refund: eligibility ≠ authorization; received ≠ inspected; inspected ≠ refund approved; refund instructed ≠ refunded/settled.

## 4. Metrics

Mỗi metric cần name, grain, formula, numerator/denominator, inclusion/exclusion, cohort/window/timezone, source, freshness, owner and threshold basis. Không trộn order/line/package/shipment denominators.

Ví dụ chỉ dùng khi data contract xác nhận: fill rate; order/fulfilment/delivery cycle time; on-time/in-full; first-attempt delivery; cancellation/RTO/return/refund rates; stuck-order and COD ageing; settlement/refund variance.

## 5. Quyền, risks và decision boundary

Six reviews: `ORDER_MANAGEMENT_OWNER`, `FULFILLMENT_INVENTORY_OWNER`, `LOGISTICS_CARRIER_OWNER`, `CUSTOMER_SERVICE_RETURNS_OWNER`, `FINANCE_TAX_PAYMENT_OWNER`, `DATA_SECURITY_COMPLIANCE`.

Six risks: `ORDER_IDENTITY_DUPLICATE_SUSPICIOUS`, `PRICE_TAX_PAYMENT_AUTHORIZATION`, `INVENTORY_ALLOCATION_FULFILMENT`, `CARRIER_DELIVERY_PROOF_COD`, `RETURN_REFUND_COMPENSATION`, `DATA_PRIVACY_SECURITY_CONTINUITY`.

Decision recommendation chỉ: `ORDER_EXCEPTION_REVIEW`, `INVENTORY_FULFILMENT_REVIEW`, `DELIVERY_CARRIER_REVIEW`, `PAYMENT_COD_RECONCILIATION_REVIEW`, `RETURN_REFUND_REVIEW`, `CUSTOMER_RECOVERY_REVIEW`, `DATA_CONTROL_REVIEW`, `REVISE`, `HOLD`. Human state luôn `PENDING`.

## 6. Nguồn nguyên tắc — kiểm tra 22/08/2026

- GS1 EDI Order to Cash: https://www.gs1.org/standards/edi/solutions — reference cho ordering, delivering, invoice/settlement/remittance messages; không áp message set nếu doanh nghiệp chưa phê duyệt.
- GS1 Global Traceability Standard: https://www.gs1.org/standards/gs1-global-traceability-standard/current-standard — reference cho identify/capture/share và traceable events; không tự chứng nhận.
- ISO 10002:2018: https://www.iso.org/standard/71580.html — guideline cho complaints handling; không thay consumer law, return/refund policy hoặc dispute resolution ngoài tổ chức.

Luôn kiểm current contract, channel/carrier/payment terms, policy, tax/consumer law và authorized master tại thời điểm chạy.
