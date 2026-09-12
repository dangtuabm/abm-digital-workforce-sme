# PHASED DEPLOYMENT RULES

## 1. Control model

- Wave là release boundary có scope, version, population, dependency, owner, evidence và blast radius; không phải lịch trang trí.
- Lịch chỉ là planning range. Entry/exit criteria và capacity quyết định đủ điều kiện đề xuất chuyển stage.
- `PASS`: evidence hiện hành đáp ứng criterion. `FAIL`: không đáp ứng. `UNKNOWN`: thiếu/expired/conflict. `EXCEPTION`: đúng authority chấp thuận residual risk, scope và expiry; không biến FAIL thành PASS.
- Critical gate FAIL/UNKNOWN dừng đề xuất mở rộng. Aggregate score không được bù critical gate.
- A.I tạo pack và kiểm tính nhất quán; human deployment authority quyết định GO/HOLD/REWORK/ROLLBACK/RETIRE.

## 2. Minimum trace

`outcome → release unit → dependency/SoR → gate criterion → evidence → decision → cutover step → verification → monitoring signal → value/adoption result → next-wave change`.

Evidence cần `id, source, timestamp, scope/version, owner, expiry, confidence/conflict, status`. Không dùng “đã test”, “sẵn sàng”, “an toàn”, “người dùng đồng ý” nếu thiếu artifact và acceptance result.

## 3. Stage menu

`PREP`, `TEST_UAT`, `PILOT`, `CANARY`, `LIMITED`, `SCALE`, `HOLD`, `ROLLBACK`, `RETIRE` là menu; không bắt buộc dùng đủ và không mặc định thứ tự cho mọi case. Mỗi stage có:

- purpose, population/exposure, version/environment;
- entry/exit gates và evidence expiry;
- value/quality/safety/cost/adoption signals;
- dependencies/capacity/support;
- halt/rollback/re-entry/exception owner;
- learning carried to the next stage.

## 4. Canary and blast radius

- Canary phải đủ đại diện cho failure mode quan trọng nhưng giới hạn ảnh hưởng.
- Ghi user/data/system/permission/transaction/geography/time exposure; containment và manual coverage.
- Observation window phải gắn signal/frequency/sample/seasonality, không hardcode số ngày.
- Không có complaint không phải evidence thành công; usage không phải value; average không được che tail/failure cohort.

## 5. Cutover transaction

Mỗi bước: `state_before, action, actor, authority, dependency, expected, verification_method, state_after, evidence, timeout, halt_trigger, rollback_ref, action_status`.

- Pre-flight kiểm version/config/data/IAM/integration/backup/support/communications/change freeze.
- Verification phải end-to-end và đối chiếu System of Record; command success không đủ.
- `action_status=PENDING` trong plan. Skill không chạy command, đổi quyền, ghi/xóa/migrate dữ liệu hoặc gửi thông báo.

## 6. Rollback, continuity, reconciliation

- Rollback record gồm trigger, decision owner, restore target/version/config/data, tested condition/evidence, time/data objectives do tổ chức duyệt, manual fallback, dependency reversal và re-entry.
- Nếu rollback chưa test, ghi `UNTESTED` và consequence; không gọi là available.
- Reconciliation bao phủ count, totals, missing/duplicate/orphan, ordering, partial failure và source-to-target trace. Chỉ owner có thẩm quyền chấp nhận discrepancy.
- Không sunset/decommission old path trước exit gate, retention/deletion authority và recovery evidence.

## 7. Monitoring and value

Tối thiểu xem xét: outcome/value, quality, safety/privacy/security, reliability/SLO, latency/capacity, cost, adoption/competency, incident/support. Mỗi control có baseline, formula/source, threshold rationale, frequency/window, cohort, owner, alert, action và evidence.

Value review tách correlation khỏi attribution; ghi external factors, guardrails/regression và confidence. Completion/training attendance/usage không thay outcome.

## 8. Decision and exception

- Decision ghi evidence refs, authority, options, rationale, residual risk, action status và expiry/review trigger.
- Exception có scope, owner, compensating control, expiry và closure evidence; không open-ended.
- External action luôn `PENDING` cho đến khi người có quyền duyệt và operator xác minh state sau.

## 9. Prohibited shortcuts

Không auto-go-live/scale; không fake/backdate/delete evidence; không coi UNKNOWN là PASS; không hardcode ba Wave, 85%, 30–60 ngày hoặc một thứ tự phòng ban thành rule; không bỏ UAT/security/IAM/rollback/reconciliation; không tăng quyền; không mutate production; không gửi/publish; không mua/ký; không decommission old path để ép tiến độ.

