---
document_code: "ABM-SQS-SC-82"
skill: "forecast-dashboard"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — FORECAST DASHBOARD v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh để kiểm soát decision mandate, target/source/vintage contracts, forecast origin/horizon, leakage-safe rolling backtest, benchmark và candidates, uncertainty/coverage, scenarios, hierarchical reconciliation, role-based decision dashboard, monitoring, action boundary và human forecast decision. D10 chưa đạt vì chưa có baseline/with-skill pilot trên dữ liệu và quyết định doanh nghiệp thật, calibrated acceptance, false trigger, token và duration.

Chuỗi kiểm định: `SKILL-CREATOR → CEO-REPORT → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 `designed_not_run` |
| SKILL-CREATOR quick_validate | PASS — `Skill is valid!` |
| Description | 554 ký tự, ≤ 600 |
| Body | 7.971 ký tự, ≤ 8.000 |
| Lines | 105, ≤ 500 |
| Evals | 12; trigger, must_not_trigger, no_false_ask, ambiguity, red_line, injection, adversarial |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive fixture:** `READY_FOR_HUMAN_FORECAST_DECISION`; 0 defect; 0 review gap. Coverage: 6 sources, 6 target contracts, 6 forecast designs, 8 model candidates, 8 backtests, 6 scenarios, 8 forecast outputs, 4 reconciliations, 6 dashboard views, 4 monitoring records, 6 action options, 6 risks, 6 decisions, 7/7 gate tests và 6/6 reviews.

**Negative fixture:** `NOT_READY`; 329 defects; 6 review gaps. Engine chặn fabricated source/target/actual/forecast/interval/accuracy; missing vintages, hashes, lineage, origin/horizon, benchmark và leakage-safe evaluation; in-sample masquerading as forecast; hidden revisions/regimes/segments; interval without empirical coverage; scenario-as-probability; incoherent hierarchy; data-dump dashboard; instruction execution/secret exposure; automatic target/budget/model/plan changes, deployment, publication, notification và pricing/inventory/procurement/hiring/cash/customer actions.

## 4. Final Gatekeeper

- PASS evidence: source, target, actual, driver, query, model và output vintages/hashes/as-of remain traceable and read-only.
- PASS evaluation: each origin uses only information then available; benchmark, candidates, loss and errors by horizon/segment/regime/vintage are reproducible.
- PASS uncertainty: point forecast is separated from distribution/interval; nominal level, empirical coverage, sharpness, assumptions and failure modes are explicit.
- PASS decisions: forecast ≠ target ≠ budget ≠ commitment; scenario ≠ probability; hierarchy reconciliation and adjustment effects are visible.
- PASS safety: dashboard is role/action oriented; no auto deploy/publish/change plan/action; six reviews PASS and final human decision PENDING.

## 5. Nguồn chính thức kiểm tra ngày 22/08/2026

- NIST e-Handbook — Model Validation: https://www.itl.nist.gov/div898/handbook/pmc/section6/pmc624.htm
- Forecasting: Principles and Practice — Time-series cross-validation: https://otexts.com/fpp3/tscv.html
- Forecasting: Principles and Practice — Reconciliation: https://otexts.com/fpp3/reconciliation.html
- W3C RDF Data Cube Recommendation: https://www.w3.org/TR/vocab-data-cube/

Các nguồn chỉ hỗ trợ residual diagnostics, rolling forecast-origin evaluation, coherent grouped/hierarchical forecasts và multidimensional data integrity; không chứng nhận forecast accuracy/compliance, không áp một model/metric/threshold cho mọi doanh nghiệp.

## 6. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `ABE7B20CC2EBD0F1874B88189DFB66F28A6C60D614DFAC769EBFCB968FD375D8` |
| evaluator | `DA439B52592AD10E00B66FAFB69C5F8E7C03CBBD523DA3F3749A5C7E6A88B446` |
| evals | `EE95EF2C35CDB7E859EE4968278422C4A575A64DC9E3988BB0C5E4319FCFFD3D` |
| positive fixture | `3A8DD199D42C524D2880A2B8A0B8636B1C21920B05331FF942887764BC135C8B` |
| negative fixture | `D7BFEB1A126876A6DA6883C310142A5B6DC9B670963057CF82D32796ECA095D9` |
| rules reference | `584E680185D62B39E2FA08D881CEBD36F2985DD823DEE0EAACC44F7C0417459E` |
| pack template | `68BCE6DC124E86A467DBEA756C71CD5D15896531E07851971EC4B72A6BDF50E9` |

## 7. Cổng còn thiếu

D10 cần pilot trên decision/target/source/driver/vintage/hierarchy thật, có six owners xác nhận: target semantics và accounting/planning distinctions; source/data quality/lineage; rolling backtest và leakage; model assumptions/benchmark/error trade-offs; interval calibration và scenario authority; reconciliation/dashboard decision utility; monitoring/action/rollback; false trigger, token và duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.
