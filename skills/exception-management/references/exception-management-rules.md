# Exception Management Control Rules

## Threshold and signal

- Threshold phải có ID/version/authority/effective date; không đổi hồi tố sau khi thấy observed value.
- Metric, unit, direction, aggregation window và scope phải khớp rule.
- Signal phải có source/version/hash hoặc locator, freshness, access và confidence.
- Missing/stale/denied/non-comparable không được chuyển thành “không có ngoại lệ”.

## Identity, priority and correlation

- Exception key = scope + rule + entity + window; retry/replay phải deduplicate.
- Severity dựa trên impact; urgency dựa trên time-to-harm/decision SLA; không dùng người báo to.
- Related exceptions phải link parent/child/common-cause; shared impact không double count.

## Authority and lifecycle

- Exception owner, decision owner, verifier và closure owner phải là vai trò người hợp lệ.
- Containment/action chỉ được phản chiếu là executed khi có authorization + evidence.
- Engine chỉ phát hành `READY_FOR_HUMAN_EXCEPTION_DECISION` hoặc `READY_FOR_HUMAN_CLOSURE`.
- Forbidden states: `ALERTED`, `CONTAINED`, `RESOLVED`, `CLOSED`, `APPROVED`, `ESCALATED`, `SPENT`, `DISCIPLINED` nếu không có authorized evidence.

## Closure

- Resolution output khác closure: phải verify trong window, kiểm residual risk, recurrence, containment exit và human acceptance.
- Reopen khi threshold tái vượt, evidence sai/stale hoặc residual risk vượt appetite.
- Learning candidate không tự sửa threshold, rule, control hoặc lịch sử.

## Forbidden flags

`threshold_changed`, `baseline_changed`, `as_of_changed`, `source_fabricated`, `observed_fabricated`, `exception_hidden`, `severity_downgraded`, `impact_double_counted`, `owner_invented`, `ai_made_owner`, `auto_alerted`, `auto_contained`, `auto_spent`, `auto_disciplined`, `auto_resolved`, `auto_closed`, `evidence_deleted`, `review_bypassed`.

## Reviews

`DOMAIN_CONTROL`, `RISK_COMPLIANCE`, `DATA_SECURITY` phải PASS. `FINAL_EXCEPTION_DECISION` hoặc `FINAL_EXCEPTION_CLOSURE` tồn tại với `PENDING`; người có authority quyết định ngoài engine.
