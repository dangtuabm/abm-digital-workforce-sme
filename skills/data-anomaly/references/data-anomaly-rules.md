# DATA ANOMALY RULES

## 1. Evidence, contract và baseline

Mỗi run khóa source locator/environment/snapshot/version/hash, schema/grain/keys, event/processing time, timezone/unit, metric contract/formula/denominator/filters, query/model/code hash, rights and lineage. Raw evidence read-only.

Baseline ghi reference population/window, regime/version, stability, trend/seasonality/calendar, segments, distribution/sample/missingness, known events and comparability. Không trộn pre/post regime, actual/forecast/target hoặc populations khác grain. Non-comparable baseline phải fail closed hoặc có limitation/owner decision.

## 2. Detector selection và signal record

- Rule/constraint cho contract/range/referential violations.
- Absolute/relative delta cho owner-approved comparison; denominator và near-zero behavior bắt buộc.
- IQR/MAD/robust score cho skew/outliers khi phù hợp; không mặc định normality.
- Shewhart/control chart cho monitored process có baseline/stability và chart phù hợp data type.
- Residual/time-series cho trend/seasonality; change-point cho regime shift; multivariate detector khi features/scaling/dependence/calibration rõ.

Signal ghi detector/version/parameters/code hash, assumptions/tests, threshold/authority, score/limit, expected/actual/delta, window/slice, uncertainty, multiplicity, supporting source and state. Statistical significance không thay business impact.

## 3. Triage, hypothesis và cause

Triage types: `DATA_QUALITY`, `PIPELINE`, `METRIC_SEMANTIC`, `EXPECTED_EVENT`, `BUSINESS_PROCESS`, `EXTERNAL`, `SECURITY_RISK`, `UNRESOLVED`. Kiểm raw-vs-aggregate, adjacent windows, control/peer segments, numerator/denominator, unit/timezone, ingestion/revision and known events.

Mỗi hypothesis ghi mechanism, predicted observations, supporting evidence, disconfirming evidence/test, confounders/alternatives, owner and state. Cause chỉ `SUPPORTED` khi converging evidence, temporal/mechanistic consistency, alternatives addressed and reviewer acceptance; còn lại `DISPROVED` hoặc `UNRESOLVED`.

## 4. Action, monitoring và feedback

Action option ghi observe/investigate/contain/recompute/fix/communicate, impact/blast radius, prerequisites/authority, owner/SLA, rollback, verification and human state PENDING. Detector tuning dùng human labels, recurrence, precision/recall hoặc supplied cost metric, drift and versioned change; không auto activate/close.

## 5. Risks, reviews và decision boundary

Six risks: `BASELINE_COMPARABILITY_DRIFT`, `DATA_QUALITY_PIPELINE_LINEAGE`, `METHOD_ASSUMPTION_THRESHOLD_MULTIPLICITY`, `SEASONALITY_SEGMENT_DENOMINATOR`, `CAUSALITY_ROOT_CAUSE_OVERCLAIM`, `ALERT_FATIGUE_ACTION_AUTHORITY`.

Six reviews: `BUSINESS_METRIC_OWNER`, `DATA_STEWARD_QUALITY`, `ANALYTICS_STATISTICS`, `DATA_ENGINEERING_OBSERVABILITY`, `RISK_SECURITY_COMPLIANCE`, `OPERATIONS_INCIDENT_OWNER`.

Recommendations: `MANDATE_IMPACT_REVIEW`, `SOURCE_CONTRACT_REVIEW`, `BASELINE_METHOD_REVIEW`, `SIGNAL_TRIAGE_REVIEW`, `HYPOTHESIS_CAUSE_REVIEW`, `ACTION_AUTHORITY_REVIEW`, `DETECTOR_FEEDBACK_REVIEW`, `REVISE`, `HOLD`. Human state luôn `PENDING`.

## 6. Nguồn nguyên tắc — kiểm tra 22/08/2026

- NIST/SEMATECH e-Handbook — Process Monitoring: https://www.itl.nist.gov/div898/handbook/pmc/pmc.htm — monitoring, control charts and time-series methods; method selection remains context-specific.
- ISO 7870-2:2023: https://www.iso.org/standard/78859.html — Shewhart control-chart use/understanding; không áp một chart cho mọi data/process.
- W3C PROV-O Recommendation: https://www.w3.org/TR/prov-o/ — source/activity/agent provenance chains; không bắt buộc RDF/OWL.

Luôn kiểm current metric/data contract, baseline regime, law/policy and authorized owner decisions. Các nguồn không chứng nhận một signal là cause, incident, fraud hay compliance breach.

