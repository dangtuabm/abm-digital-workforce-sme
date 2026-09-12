# Action Closure Rules

## Hard gates

1. Action set có source/version/hash/scope/classification và correction owner.
2. Mỗi action có outcome, một accepted owner, due, DoD, reviewer và authority evidence.
3. Progress event chỉ là `REPORTED` cho đến khi evidence được verify.
4. Evidence có version/hash/locator/access/captured-at/owner và còn active.
5. Dependency/blocker/exception có owner, impact, control và escalation rule.
6. Mỗi DoD criterion có `PASS/FAIL/NOT_TESTED`, evidence refs và reviewer.
7. Late/partial/reject/waive/cancel/reopen không xóa lịch sử và cần authority evidence.
8. Engine không gửi nhắc, escalate, mutate task, đổi owner/due/scope/DoD hay đóng action.

## States

- `NOT_READY`: critical defect.
- `MONITORING_READY`: contract đủ, chưa đủ closure evidence.
- `READY_FOR_CLOSURE_REVIEW`: candidate đủ để reviewer kiểm.
- `READY_FOR_HUMAN_CLOSURE`: review bắt buộc PASS, final closure PENDING.
- Trạng thái closed chỉ phản chiếu human decision có evidence.

## Review minimum

`ACTION_OWNER`, `DOD_REVIEWER`, `DOMAIN_SECURITY`, `FINAL_CLOSURE`. Medium/high risk không tự review. Mọi decision lưu actor/action/time/reason/source/version.
