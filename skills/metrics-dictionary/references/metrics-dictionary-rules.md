# METRICS DICTIONARY RULES

## 1. Identity, classification và census

Mỗi metric có immutable canonical ID, canonical name, aliases/original labels, domain, business question, definition, type (`RAW_MEASURE`, `DERIVED_METRIC`, `KPI`, `LEADING`, `LAGGING`, `GUARDRAIL`, `TARGET`, `BENCHMARK`, `DIAGNOSTIC`), owner/steward/approver, status, version và effective/sunset dates. Census giữ source artifact, locator/version/hash, consumer và conflict; same label/formula không đủ để merge.

## 2. Observation và semantic contract

Khóa entity, grain, event/state, numerator, denominator, formula, aggregation behavior, allowed roll-up, distinctness and denominator-zero rule. Khóa dimensions, hierarchies/code lists, filters/inclusion/exclusion, cohort, valid/event/processing time, window, timezone, unit, currency/FX source/effective date, rounding, null/zero, duplicates, late arrivals, corrections/restatement and provisional/final status.

Formula phải machine-readable hoặc có deterministic pseudocode; mọi input field có meaning/type/source. Ratio ghi rõ `ratio of sums`, `average of ratios` hay phương thức được owner duyệt. Không cộng distinct counts xuyên slice nếu chưa chứng minh additivity.

## 3. Lineage, test và reconciliation

Trace: authorized source/event/table/field/snapshot → transform/model/query/version/hash → semantic object → dashboard/report/API/decision. Ghi environment, owner, run/as-of, freshness and rights.

Test tối thiểu: contract/schema; positive; negative; boundary/denominator-zero; aggregation/grain; time/cohort/timezone; null/duplicate/late/restatement; lineage/reconciliation/access. Mỗi test có fixture, expected, actual, evidence and owner.

Reconcile source, model, semantic layer, dashboard and finance/control total theo cùng scope/grain/time/unit/version. Tolerance phải có authority. Unexplained delta = FAIL/NOT_READY; không “làm tròn cho khớp”.

## 4. Target, change và adoption

Target/baseline/benchmark/status band là objects riêng với authority, evidence, effective period, scope and version; không nhúng mặc định vào definition. Semantic change ghi old/new/diff/reason, breaking level, impacted metrics/consumers, compatibility, migration, acknowledgement, rollback and deprecation/sunset. Không xóa lịch sử.

## 5. Risks, reviews và decision boundary

Six risks: `SEMANTIC_DEFINITION_SCOPE`, `GRAIN_DENOMINATOR_DOUBLE_COUNT`, `SOURCE_LINEAGE_DATA_QUALITY`, `TIME_CURRENCY_UNIT_RESTATEMENT`, `TARGET_THRESHOLD_GAMING`, `VERSION_ADOPTION_RECONCILIATION`.

Six reviews: `BUSINESS_DOMAIN_OWNER`, `DATA_STEWARD_ANALYTICS`, `FINANCE_ACCOUNTING_OWNER`, `DATA_ENGINEERING_SEMANTIC_LAYER`, `RISK_LEGAL_COMPLIANCE`, `DASHBOARD_REPORTING_CONSUMER_OWNER`.

Recommendations: `MANDATE_SCOPE_REVIEW`, `METRIC_CONTRACT_REVIEW`, `FORMULA_GRAIN_REVIEW`, `LINEAGE_TEST_REVIEW`, `TARGET_AUTHORITY_REVIEW`, `VERSION_ADOPTION_REVIEW`, `RECONCILIATION_RELEASE_REVIEW`, `REVISE`, `HOLD`. Human state luôn `PENDING`.

## 6. Nguồn nguyên tắc — kiểm tra 22/08/2026

- W3C RDF Data Cube Recommendation: https://www.w3.org/TR/vocab-data-cube/ — dimensions, measures, attributes, structures and integrity constraints; không bắt buộc doanh nghiệp dùng RDF.
- ISO/IEC 11179-3:2023: https://www.iso.org/standard/78915.html — identification, designation/definition, registration, classification and mapping principles for metadata registries.
- ISO 8000-63:2019: https://www.iso.org/standard/65344.html — goal/sub-goal/question/indicator/metric process-measurement stack; được ISO xác nhận lại năm 2025.

Luôn kiểm current business contract, accounting policy, law, source system and authorized owner decision tại thời điểm chạy. Các nguồn trên chỉ là design references, không chứng nhận metric truth, accounting treatment hay compliance.

