# Outcome Execution Rules

## Hard gates

1. Một initiative có outcome invariant, beneficiary, baseline/target/due, non-goals và decision rights.
2. Metric có definition/formula/unit/grain/owner/system-of-record/freshness.
3. Mọi work package trace tới milestone và outcome metric; orphan activity không tính progress.
4. Milestone chỉ pass khi prerequisites và mọi critical criterion PASS bằng current evidence; threshold phải được phê duyệt.
5. Dependency/critical path/capacity/WIP/access có owner, state, evidence và fallback.
6. Forecast có range/confidence/assumptions/evidence date; variance giữ nguyên baseline.
7. Scope/budget/target/deadline/resource change cần before/change/after/impact/approver/verification/rollback.
8. Engine không mutate, reallocate, approve, rebaseline, pivot, pause, stop hoặc gửi cảnh báo.

## States

- `NOT_READY`: critical defect.
- `EXECUTION_BASELINED`: contract/trace/readiness đủ, chưa đủ current evidence/forecast.
- `READY_FOR_EXECUTION_REVIEW`: snapshot đủ, reviewer còn xử lý.
- `READY_FOR_HUMAN_EXECUTION_DECISION`: reviews bắt buộc PASS, final decision PENDING.
- Execution decision chỉ phản chiếu human evidence.

## Review minimum

`OUTCOME_OWNER`, `METRIC_DATA`, `DOMAIN_RESOURCE`, `FINAL_EXECUTION_DECISION`. Medium/high risk không tự review. Mọi decision lưu actor/action/time/reason/source/version.
