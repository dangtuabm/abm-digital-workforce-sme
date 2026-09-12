# Best-Practice Decoder Gate Rules

Đọc ở Bước 7. Engine lint trace/coverage; reviewer chịu trách nhiệm về source accuracy, causal validity, IP/rights, domain risk và pilot approval.

## State

- NOT_READY: thiếu contract/standards/owner.
- DRAFT: contract đủ nhưng chưa có evidence/components.
- REVISE: evidence, layers, refs, transfer decisions, rival explanations hoặc pilot lỗi.
- HYPOTHESIS_ONLY: cấu trúc đạt nhưng evidence dưới min_evidence_items.
- READY_WITH_GUARDRAILS: logic đạt nhưng high-risk, expert review/guardrail mở.
- READY_FOR_PILOT: gate tĩnh đạt; chưa chứng minh transfer/effectiveness.

## Gate

1. Evidence: id/source/date-version/type/claim/result/scope/rights/confidence/limitations.
2. Evidence ID duy nhất; rights không được unknown/denied.
3. Component: id/layer/description/evidence refs/causal confidence/context dependency/decision rule/exceptions/copy risk.
4. Component refs phải tồn tại; required layers phải được phủ.
5. High causal confidence cần evidence count đạt contract và không có ref rỗng.
6. Rival explanations phải có ít nhất một giả thuyết cạnh tranh hoặc counterexample gap.
7. Mỗi component có transfer decision retain/adapt/drop/test, target fit, adaptation, owner, validation need.
8. Pilot có hypothesis, baseline, leading/outcome metric, data source, success/stop threshold, review window, owner, rollback.
9. Evidence dưới minimum: HYPOTHESIS_ONLY, không tự fail nếu mọi control khác đạt.
10. Risk cao/expert pending/guardrail mở không vượt READY_WITH_GUARDRAILS.

## Giới hạn

- READY_FOR_PILOT không đồng nghĩa mechanism đúng hay kết quả sẽ lặp lại.
- Engine không xác minh source/web/IP; Evidence Ledger và reviewer phải làm.
- Surface similarity không được dùng thay structural/context fit.
