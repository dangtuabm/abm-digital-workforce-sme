# Organization Design Control Rules

## 1. Evidence hierarchy

1. Chiến lược, chính sách, sơ đồ quyền hạn và dữ liệu vận hành đã được chủ nguồn phê duyệt.
2. Dữ liệu workload, capacity, service level và risk có System of Record cùng mốc `as_of`.
3. Phỏng vấn/workshop có người xác nhận và biên bản.
4. Giả định thiết kế được gắn nhãn, owner và hạn xác minh.

Nguồn cấp thấp không được ghi đè nguồn cấp cao. Xung đột phải được đưa vào decision brief.

## 2. Trace rules

- Mỗi target unit phải nối đến ít nhất một capability có nguồn.
- Mỗi capability trọng yếu phải có đúng một accountability owner cuối, dù nhiều đơn vị có thể đóng góp.
- Mỗi capability phải nối đến value stream; mỗi value stream nối đến objective.
- Vai trò không có purpose/outcome/capacity/source là chưa hợp lệ.

## 3. Decision-right rules

- Mỗi `decision.id` là duy nhất và có đúng một `decision_owner`.
- `decision_owner` không được rỗng, không được là A.I và phải thuộc role register.
- Approver theo ngưỡng không thay thế owner; executor không tự nâng thành owner.
- Quyết định có rủi ro xung đột phải qua SOD/control review.

## 4. Span/layer rules

- Không hard-code “span lý tưởng”.
- Chỉ kết luận khi có workload, complexity, manager capacity và standardization evidence.
- Nếu thiếu dữ liệu, ghi `INSUFFICIENT_EVIDENCE`; không tạo FTE hoặc headcount giả.
- Layer chỉ bị xem là thừa khi có bằng chứng về value add, decision latency và accountability duplication.

## 5. Interface and SOD rules

- Interface trọng yếu phải đủ provider, consumer, input, output, service level, quality rule, escalation và source.
- Duty incompatibility phải được kiểm tra trên role/accountability/decision assignment.
- Không một vai trò vừa khởi tạo, phê duyệt và tự xác minh giao dịch kiểm soát nếu policy cấm.

## 6. Human–A.I rules

- `ai_mode` chỉ nhận `ANALYZE`, `DRAFT`, `CHECK`, `ALERT` hoặc `NONE`.
- Mỗi allocation dùng A.I phải có human supervisor, audit và rollback.
- A.I không là final decision owner, accountable legal person hoặc approver nhân sự.
- Dữ liệu RED chỉ được xử lý trong môi trường và quyền đã phê duyệt.

## 7. Implementation boundary

Engine chỉ kiểm định pack. Mọi thay đổi thật phải là change request do người có thẩm quyền duyệt và hệ thống được ủy quyền thực thi. Forbidden flags gồm:

`role_invented`, `accountability_duplicated`, `decision_owner_duplicated`, `gap_hidden`, `overlap_hidden`, `span_assumed`, `fte_fabricated`, `ai_made_accountable`, `sod_bypassed`, `auto_hired`, `auto_fired`, `auto_promoted`, `auto_demoted`, `pay_changed`, `reporting_changed`, `permission_changed`, `auto_reorganized`.

Forbidden states gồm: `HIRED`, `FIRED`, `PROMOTED`, `DEMOTED`, `APPOINTED`, `REASSIGNED`, `REORGANIZED`, `APPROVED`, `IMPLEMENTED`.

## 8. Review gates

- `ORG_SPONSOR`: fit với chiến lược, phạm vi và investment intent.
- `PEOPLE_LEGAL_COMPLIANCE`: lao động, SOD, role impact và nghĩa vụ tham vấn.
- `DATA_SECURITY`: dữ liệu, quyền, A.I và system boundary.
- `FINAL_ORG_DECISION`: người được ủy quyền quyết định sau khi pack hoàn chỉnh.

Ba review chuyên môn đầu phải `PASS`; review cuối phải tồn tại với `PENDING` để engine phát hành `READY_FOR_HUMAN_ORG_DECISION`.
