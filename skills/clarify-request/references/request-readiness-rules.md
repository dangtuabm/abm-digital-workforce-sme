# REQUEST READINESS RULES

## Field tối thiểu

Outcome/value; deliverable; audience/use; scope in/out; inputs/source of truth/version; constraints; acceptance/Definition of Done; format/destination; timing/priority; dependencies; authority/red lines; decision owner.

Không phải mọi field đều cần user trả lời. Dùng `NOT_APPLICABLE`, evidence hoặc reversible default khi phù hợp.

## Materiality

- `BLOCKING`: câu trả lời có thể đổi outcome/scope/source, tạo hành động không đảo ngược, external impact, sensitive-data exposure, legal/commercial commitment hoặc acceptance không thể kiểm.
- `MATERIAL_NONBLOCKING`: có thể làm phần reversible nhưng phải chốt trước stage/action cụ thể.
- `OPTIONAL`: không đổi outcome/risk đáng kể; dùng default minh bạch và cho phép sửa.

## Readiness

- `READY`: material fields confirmed/evidenced; không còn conflict ảnh hưởng execution.
- `READY_WITH_ASSUMPTIONS`: chỉ còn assumptions reversible, low-risk, disclosed; có rollback/change trigger.
- `BLOCKED_PENDING_ANSWER`: còn blocking branch/approval; nêu chính xác phần dừng, owner và work vẫn tiếp tục được.

## Source conflict

Ghi từng source/version, claim khác nhau, field bị ảnh hưởng, consequence và authority owner. Không chọn “mới nhất” nếu chưa có evidence; timestamp không đồng nghĩa authoritative.

## Assumption record

Mỗi assumption cần ID, statement, evidence/default basis, impact, reversibility, expiry/change trigger, affected outputs và owner. Business assumption material không được tự duyệt.

