# Pipeline Management Rules

## 1. Đơn vị và nguồn sự thật

- Đơn vị là `opportunity record` có ID ổn định; không đồng nhất với contact, account, activity hay invoice.
- Mọi phân tích gắn một CRM snapshot ID/hash/timestamp, sales-process version, scope và as-of.
- Resolve duplicate trước khi tổng hợp. Không cộng hai record cùng opportunity hoặc tách một deal để tăng pipeline.
- Giữ raw amount/currency và basis quy đổi. Không cộng nhiều currency nếu thiếu rate/date/source.
- Unknown giữ `UNKNOWN`; missing không tự biến thành 0, lost hoặc unqualified.

## 2. Stage contract

Mỗi stage cần:

1. Entry criteria có thể kiểm chứng.
2. Required evidence và source class.
3. Exit criteria/gate.
4. Stage owner và authority thay đổi.
5. Age limit cùng policy source/version.
6. Next-action SLA và escalation.
7. Allowed forecast category.

Activity count không phải stage evidence. Email mở, cuộc gọi, cuộc họp hoặc proposal chỉ có nghĩa khi tạo evidence/decision/commitment theo contract.

## 3. Opportunity evidence score

Chỉ score opportunity theo mục đích được duyệt, ví dụ ưu tiên review/capacity; không score giá trị con người hay khả năng dễ bị thuyết phục.

Dimension gợi ý có điều kiện:

- fit/problem evidence;
- need/impact evidence;
- decision process/stakeholder coverage;
- budget/economic path;
- timing/trigger evidence;
- momentum/next-step integrity;
- delivery/commercial risk nếu policy yêu cầu.

Mỗi dimension có weight, scale, evidence requirement, missing rule, confidence và model version. Weight phải được duyệt; score cần calibration và không được dùng để auto-exclude. Manual override phải có old/new, reason, evidence, actor, authority và timestamp.

Protected/sensitive traits và proxy của chúng không được dùng. Cần kiểm fairness theo lawful purpose, sample/coverage và customer-treatment outcome.

## 4. Aging, staleness và next action

- Age-in-stage tính từ stage-entered-at được xác nhận.
- Stale threshold đến từ policy/segment/process, không áp số ngày phổ quát.
- Next action cần outcome, owner, due, dependency, evidence expected và acceptance.
- `No next action`, overdue, single-threaded stakeholder, missing decision process, stage-age breach hoặc source stale → exception, không tự close.
- Lost/nurture reason phải có human evidence và route khôi phục/appeal khi phù hợp.

## 5. Pipeline reconciliation

Reconcile tối thiểu:

- census: source record count, included/excluded IDs và lý do;
- identity: duplicate/merge/split;
- amount: raw/normalized amount, currency/rate/date;
- stage: count/amount by stage;
- owner/capacity: workload and coverage;
- freshness: stale/unknown/late updates;
- variance: expected vs observed and unresolved items.

Không báo coverage ratio, velocity, conversion hoặc weighted value khi thiếu denominator/cohort/window/model source.

## 6. Forecast governance

- Forecast category là policy label, không phải xác suất tự nhiên.
- Nếu dùng probability, phải có model/version/calibration/eligible population và limitation.
- Tách scenario `COMMIT_CANDIDATE|BASE|UPSIDE|DOWNSIDE` theo policy; tên không tạo cam kết pháp lý/tài chính.
- Mỗi forecast line nối opportunity, amount/currency, expected timing, stage evidence, assumption, capacity/dependency và risk.
- So sánh forecast với capacity/delivery constraint và lịch quyết định của khách.
- Không dùng weighted pipeline như revenue certainty; báo range, sensitivity và exclusion.

## 7. Exception và decision queue

Exception có type, affected IDs, source/evidence, severity, owner, due, verification/action, escalation và state. Recommendation hợp lệ: `KEEP|VERIFY|CORRECT|NURTURE|HOLD|CLOSE_REVIEW`; tất cả chờ human authority.

Decision queue không được tự đổi CRM. Sau quyết định, cần before/action/after/authority/timestamp/verification/rollback-or-correction evidence.

## 8. Cổng rủi ro

Sáu nhóm tối thiểu:

- `DATA_QUALITY_LINEAGE`
- `STAGE_PROCESS_INTEGRITY`
- `FORECAST_UNCERTAINTY`
- `CAPACITY_COVERAGE`
- `CUSTOMER_HARM_FAIRNESS`
- `COMMERCIAL_LEGAL_PRIVACY`

Critical defect gồm fabricated record/evidence/amount, mixed currency không kiểm soát, unapproved model, protected-trait/proxy use, hidden override, auto exclusion/deletion/stage/owner/contact/commit/close hoặc source/authority không hợp lệ.

## 9. D10 pilot

Pilot tối thiểu ba pipeline thật có quy mô/mô hình bán khác nhau. So v1.0/v2.3 trên ground truth đã đóng băng; đo stage precision, duplicate/stale detection, amount reconciliation, forecast calibration/error, next-action usefulness, exception closure, customer harm, token và duration. Static self-test không thay thế pilot.
