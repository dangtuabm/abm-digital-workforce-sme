# Portfolio Monitoring Rules

## Hard gates

1. Portfolio contract có scope/as-of/cadence/sponsor/decision rights và inclusion/exclusion.
2. 100% initiative in-scope có outcome, owner, authorized priority, lifecycle và sources.
3. Metric chỉ so sánh khi definition/formula/unit/currency/grain/period/freshness tương thích; nếu không gắn `NOT_COMPARABLE`.
4. Actual/forecast/threshold/exception có current authorized source và confidence.
5. Cross-dependency, resource collision, cascade/concentration có owner, impact, control/fallback.
6. Không average sai hoặc double count value/cost/risk/resource demand.
7. Decision request có question, affected initiatives, deadline, options, recommendation, trade-offs và decision owner.
8. Engine không alert, reprioritize, reallocate, resequence, đổi budget/status, approve, pause hoặc stop.

## States

- `NOT_READY`: critical defect.
- `PORTFOLIO_BASELINED`: census/metric/source map đủ, chưa đủ current exception snapshot.
- `READY_FOR_PORTFOLIO_REVIEW`: snapshot đủ, reviewer còn xử lý.
- `READY_FOR_HUMAN_PORTFOLIO_DECISION`: reviews bắt buộc PASS, final decision PENDING.

## Review minimum

`PORTFOLIO_SPONSOR`, `METRIC_DATA`, `FINANCE_RESOURCE_DOMAIN`, `FINAL_PORTFOLIO_DECISION`. Mọi human decision lưu actor/action/time/reason/source/version.
