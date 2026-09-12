# FORECAST DASHBOARD RULES

## 1. Target, source và vintage

Mỗi forecast khóa target metric/version, entity/grain/hierarchy, formula/denominator/aggregation, dimensions/filters, time/frequency/timezone, unit/currency, actual revision/restatement and owner. Tách `ACTUAL`, `TARGET`, `BUDGET`, `FORECAST`, `SCENARIO`, `BENCHMARK`.

Mỗi run ghi forecast ID, origin/as-of, horizons, source/feature vintages/hashes, data availability lag, query/model/code version/hash and authorized rights. Không backtest bằng data/driver chưa tồn tại tại origin. Revised actuals không ghi đè vintage used; đánh giá initial-vs-final actual nếu quyết định cần.

## 2. Design, benchmark và backtest

Define train/validation/test hoặc rolling-origin folds theo cadence/horizon. Benchmark tối thiểu là owner-approved simple method phù hợp như naive/seasonal naive; không hardcode nếu target khác cấu trúc. Candidate ghi rationale, assumptions, features/drivers availability, hyperparameter search boundary and reproducibility.

Evaluate genuine forecasts by horizon/segment/regime/vintage. Metrics may include MAE, RMSE, MASE, WAPE, pinball loss, interval score and coverage; state formula/denominator/zero behavior and decision loss. Training fit/R² không thay out-of-sample evidence; không cherry-pick one metric/horizon.

## 3. Uncertainty, scenario và reconciliation

Point forecast đi cùng distribution/quantiles/intervals when decision risk requires. Ghi nominal level, construction method, empirical coverage, sharpness/width, calibration period and assumptions. Interval không phải guaranteed range.

Scenario ghi driver values/ranges, source, owner, effective period, internal consistency, sensitivities and triggers. Chỉ gắn probability khi có calibrated method/evidence/authority. Known-future and forecast drivers are separate.

Hierarchical/grouped/time reconciliation records base forecasts, aggregation constraints, method/version, point/distribution coherence, adjustments, accuracy/coverage impact and owner.

## 4. Dashboard, release và monitoring

Role view: decision/question, actual/target/budget/forecast/scenario, interval, variance and drivers, origin/horizon/vintage/freshness, confidence/limitations, drill-down/lineage, pending decision/owner/needed-by. Avoid data dump and misleading axes/scales.

Release records champion/challenger, model card, approvals, freeze cadence, change impact, compatibility, rollback. Monitor data/feature/target drift, error by horizon/segment, bias, coverage, freshness, revision and business cost. Tuning/deploy/plan/action require human authority.

## 5. Risks, reviews và decision boundary

Six risks: `TARGET_SEMANTIC_VINTAGE`, `DATA_QUALITY_LEAKAGE_REVISION`, `MODEL_ASSUMPTION_OVERFIT`, `UNCERTAINTY_INTERVAL_CALIBRATION`, `SCENARIO_DRIVER_HIERARCHY`, `DASHBOARD_ACTION_GOVERNANCE`.

Six reviews: `BUSINESS_DECISION_OWNER`, `DATA_STEWARD_METRIC_OWNER`, `FORECAST_ANALYTICS_STATISTICS`, `FINANCE_PLANNING_ACCOUNTING`, `DATA_ENGINEERING_BI_PLATFORM`, `RISK_COMPLIANCE_OPERATIONS`.

Recommendations: `MANDATE_TARGET_REVIEW`, `SOURCE_VINTAGE_REVIEW`, `MODEL_BACKTEST_REVIEW`, `UNCERTAINTY_SCENARIO_REVIEW`, `RECONCILIATION_DASHBOARD_REVIEW`, `MONITORING_RELEASE_REVIEW`, `ACTION_PLAN_REVIEW`, `REVISE`, `HOLD`. Human state luôn `PENDING`.

## 6. Nguồn nguyên tắc — kiểm tra 22/08/2026

- NIST e-Handbook — Model Validation: https://www.itl.nist.gov/div898/handbook/pmc/section6/pmc624.htm — residual/model diagnostic principles.
- Forecasting: Principles and Practice — Time-series cross-validation: https://otexts.com/fpp3/tscv.html — rolling forecast origin and horizon-aware evaluation.
- Forecasting: Principles and Practice — Reconciliation: https://otexts.com/fpp3/reconciliation.html — coherent grouped/hierarchical forecasts.
- W3C RDF Data Cube Recommendation: https://www.w3.org/TR/vocab-data-cube/ — dimensions/measures/attributes and integrity; không bắt buộc RDF.

Luôn kiểm current target/data contracts, accounting policy, law and authorized owner decisions. Các nguồn không chứng nhận accuracy, outcome, budget or action.

