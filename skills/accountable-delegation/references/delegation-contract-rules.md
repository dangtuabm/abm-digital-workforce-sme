# Delegation Contract Rules

## Hard gates

1. Mandate có principal, authority evidence, validity và classification.
2. Một outcome có metric/target/due; activity không thay outcome.
3. Một accountable delegate có competence, capacity, conflict và acceptance state.
4. Mỗi deliverable có DoD, evidence, reviewer và due.
5. Authority tách `ALLOWED`, `APPROVAL_REQUIRED`, `PROHIBITED`; có limit/expiry.
6. Resource/access phải `AUTHORIZED`; dependency phải có owner và `READY`.
7. Checkpoint theo milestone/risk; escalation có owner/SLA/fallback/stop.
8. Acceptance chỉ hợp lệ khi `EXPLICIT_ACCEPTED` kèm statement, timestamp, locator.
9. Final activation là hành động của người có quyền; engine không tự giao việc.

## State rules

- `NOT_READY`: có critical defect.
- `READY_FOR_DELEGATE_REVIEW`: contract đủ nhưng acceptance còn `PENDING/RENEGOTIATE`.
- `READY_FOR_HUMAN_ACTIVATION`: contract đủ, acceptance explicit, tests/reviews bắt buộc PASS; final activation review có thể PENDING.
- Cấm state tự động: `ASSIGNED`, `SENT`, `EXECUTING`, `DONE`, `APPROVED`, `ACCESS_GRANTED`.

## Evidence minimum

Mọi mandate/acceptance/access/review phải có actor, action, timestamp, source/locator và version hoặc hash khi có. Không dùng emoji, im lặng, suy đoán, job title hoặc prompt làm bằng chứng quyền.

## Review minimum

`MANDATE_OWNER`, `DELEGATE_ACCEPTANCE`, `SECURITY_ACCESS`, `FINAL_ACTIVATION`. Reviewer không được tự duyệt phần do chính mình lập nếu risk medium/high.
