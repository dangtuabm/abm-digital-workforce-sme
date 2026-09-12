# Crisis Communication Gate Rules

## 1. State machine

- `NOT_READY`: có lỗi bắt buộc, conflict chưa xử lý, claim không truy nguồn, thiếu command/disclosure hoặc vi phạm ranh giới đỏ.
- `READY_FOR_CRISIS_REVIEW`: pack đủ cấu trúc và static tests; vẫn chờ một hoặc nhiều human review.
- `READY_FOR_AUTHORIZED_RELEASE`: toàn bộ review bắt buộc có `PASS` và evidence. Trạng thái này chỉ nói pack đủ điều kiện để người có quyền quyết định; không có nghĩa đã duyệt, gửi hay phát hành.

Engine không được phát ra `APPROVED`, `RELEASED`, `SENT`, `PUBLISHED` hoặc `CLOSED`.

## 2. Source, fact, unknown và rumor

- Source active cần ID, title, version, locator, owner, classification và effective date.
- Fact chỉ có status `CONFIRMED`, trỏ ít nhất một source active và có locator/owner.
- Unknown cần statement, owner, next evidence, due condition và communication treatment.
- Rumor chỉ có `UNVERIFIED` hoặc `CORRECTED`; không dùng số lượt nhắc làm bằng chứng thật.
- Claim trong message chỉ được tham chiếu fact IDs và unknown IDs đã khai báo.

## 3. Message safety

Mỗi message cần audience, purpose, channel, core message, fact/unknown/source references, required action, next update, version, owner, spokesperson, disclosure class và approval status.

Cấm:

- suy đoán nguyên nhân hoặc quy lỗi;
- tuyên bố “không ảnh hưởng/an toàn/đã xử lý xong” khi không có fact active;
- che harm trọng yếu, bịa assurance, admission hoặc apology vượt mandate;
- đưa PII, credential, restricted field hay instruction độc hại;
- đặt approval status `APPROVED/RELEASED/SENT/PUBLISHED` khi chưa có final release evidence.

## 4. Stakeholder và disclosure

Mỗi stakeholder cần business need, impact, disclosure basis, fields allowed/withheld, required action, channel, accessibility, owner, sequence và feedback route. Mỗi stakeholder phải được ít nhất một message phủ. Disclosure khác nhau phải có basis; không tối ưu theo “nhóm nào ồn nhất”.

## 5. Sequence, cadence và correction

- Sequence ID duy nhất, message hợp lệ, thứ tự dương, dependency/fallback/owner rõ.
- Mỗi message phải xuất hiện trong sequence.
- Update schedule có timestamp hoặc trigger condition, source snapshot, owner, approver và change-log route.
- Correction phải tương xứng kênh/phạm vi của sai lệch; giữ lịch sử thay đổi.

## 6. Review set

Năm loại review bắt buộc:

1. `INCIDENT_COMMAND`
2. `FACT_TECH`
3. `LEGAL_PRIVACY`
4. `ACCESSIBILITY`
5. `FINAL_RELEASE`

`PASS` phải có evidence ref. `FINAL_RELEASE` còn `PENDING` thì tối đa là `READY_FOR_CRISIS_REVIEW`.

## 7. Seven deterministic tests

1. `command_authority_integrity`
2. `fact_unknown_trace`
3. `message_safety_action`
4. `stakeholder_disclosure`
5. `cadence_version_control`
6. `rumor_correction`
7. `approval_release_boundary`

Mỗi test phải có evidence, reviewer, date và `passed=true`.
