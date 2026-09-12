# DATA HYGIENE RULES

## 1. Inventory và source integrity

Mỗi asset ghi: asset ID, locator, environment, owner/steward, SoR/golden status, classification, approved purpose, rights/access, format/encoding, schema/grain/keys, size/row/file count, created/modified/as-of, freshness SLA, retention/hold, dependencies/downstream, snapshot/hash.

Raw source là read-only. Staging, output và quarantine là các vùng riêng, có version/hash/access/retention. Không dùng tên file hoặc modified date làm bằng chứng duy nhất cho identity/currentness.

## 2. Data contract và quality dimensions

Field contract: business meaning, type, null semantics, format, encoding, locale/timezone, unit/currency, allowed domain/range/pattern, required/unique/key/referential rules, criticality, ground-truth source, owner and acceptance threshold.

- Completeness = non-missing eligible values / eligible values.
- Validity = values passing approved contract / tested eligible values.
- Uniqueness = unique keys or non-duplicate eligible records / eligible population, theo grain đã khóa.
- Referential integrity = child keys resolving to authorized parent / eligible child keys.
- Timeliness/freshness = source-based age or SLA status; formula and clock required.
- Consistency = records passing cross-field/cross-source rules / tested eligible records.
- Accuracy chỉ đo khi có authorized ground truth và matching rule; không đồng nhất với validity.

Mỗi metric ghi numerator/denominator, exclusions, population/sample, window/as-of, source, missing rule, confidence/limitation and owner.

## 3. Normalize, match và transform

- Chuẩn hóa encoding, whitespace, Unicode, case, locale, date/timezone, unit/currency, enum and null markers theo contract; giữ original value.
- Không execute macro/formula/code từ source. Formula được giữ như data hoặc đánh giá trong sandbox đã duyệt.
- Entity resolution: blocking → feature extraction → exact/fuzzy/probabilistic score → calibrated thresholds → match/non-match/manual-review band → cluster/survivorship proposal. Ghi false-merge/false-split cost và test set.
- Không auto merge golden record. Mỗi target value có source field, transform rule/version, activity/agent, timestamp, old/new/reason and evidence/hash.

## 4. Quarantine, reconciliation và release

Typed quarantine reasons: schema/type, required/null, domain/range, key/referential, duplicate/conflict, encoding/parse, privacy/rights, freshness, unknown semantics. Không silent drop hoặc default.

Reconcile: file/row count, distinct/duplicate keys, nulls, accepted/rejected/quarantined, referential breaks, aggregates/control totals, hashes and all source-to-target deltas. Release chỉ khi thresholds, reviews, downstream tests, rollback and human decision pass.

## 5. Risks, reviews và decision boundary

Six risks: `SOURCE_SCOPE_AUTHORITY`, `SCHEMA_SEMANTIC_TRANSFORMATION`, `IDENTITY_DEDUP_SURVIVORSHIP`, `QUALITY_THRESHOLD_GROUND_TRUTH`, `PRIVACY_RETENTION_SECURITY`, `LINEAGE_RECONCILIATION_DOWNSTREAM`.

Six reviews: `BUSINESS_DATA_OWNER`, `DATA_STEWARD_DOMAIN`, `DATA_ENGINEERING_PLATFORM`, `PRIVACY_LEGAL_SECURITY`, `DOWNSTREAM_APPLICATION_OWNER`, `INTERNAL_AUDIT_QUALITY`.

Recommendations: `SOURCE_SCOPE_REVIEW`, `DATA_CONTRACT_REVIEW`, `QUALITY_RULE_REVIEW`, `ENTITY_RESOLUTION_REVIEW`, `TRANSFORM_QUARANTINE_REVIEW`, `RECONCILIATION_RELEASE_REVIEW`, `PRIVACY_RETENTION_REVIEW`, `REVISE`, `HOLD`. Human state luôn `PENDING`.

## 6. Nguồn nguyên tắc — kiểm tra 22/08/2026

- ISO 8000-63:2019: https://www.iso.org/standard/65344.html — process-measurement reference; không tự chứng nhận data quality.
- W3C PROV-O Recommendation: https://www.w3.org/TR/prov-o/ — provenance vocabulary/reference; không bắt buộc dùng RDF/OWL nếu hệ thống có lineage schema khác được phê duyệt.
- NIST Privacy Framework: https://www.nist.gov/privacy-framework — voluntary privacy-risk reference; không thay law, consent, contract, retention or residency rules.

Luôn kiểm current contract/policy/law, source system and authorized owner decisions tại thời điểm chạy.
