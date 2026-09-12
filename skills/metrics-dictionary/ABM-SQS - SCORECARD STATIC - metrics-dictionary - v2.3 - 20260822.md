---
document_code: "ABM-SQS-SC-80"
skill: "metrics-dictionary"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — METRICS DICTIONARY v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh cho metric census/conflict, canonical semantic contract, grain/formula/denominator/aggregation, dimensions/time/unit/currency, source-to-consumer lineage, validation/reconciliation, target authority, semantic version/deprecation, adoption và human governance decision. D10 chưa đạt vì chưa có baseline/with-skill pilot trên metric/source/query/dashboard thật, owner xác nhận semantics, production reconciliation, false trigger, token và duration.

Chuỗi kiểm định: `SKILL-CREATOR → AI-ROI-MEASURE → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 `designed_not_run` |
| SKILL-CREATOR quick_validate | PASS — `Skill is valid!` |
| Description | 576 ký tự, ≤ 600 |
| Body | 7.844 ký tự, ≤ 8.000 |
| Lines | 106, ≤ 500 |
| Evals | 12; trigger, must_not_trigger, no_false_ask, ambiguity, red_line, injection, adversarial |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive fixture:** `READY_FOR_HUMAN_METRIC_GOVERNANCE_DECISION`; 0 defect; 0 review gap. Coverage: 8 sources, 8 census items, 10 metric contracts, 6 dimensions, 8 lineage records, 8 validation cases, 4 reconciliations, 5 change records, 8 adoption bindings, 6 risks, 6 decisions, 7/7 gate tests và 6/6 reviews.

**Negative fixture:** `NOT_READY`; 276 defects; 6 review gaps. Engine chặn fabrication của scope/owner/SoR/source/metric/formula/target/SQL/test/reconciliation/version; denominator/filter manipulation; ratio/distinct misaggregation; actual/forecast/target mixing; hidden conflict/delta/change; instruction execution; secret/PII exposure; auto metric/model/dashboard/SQL/backfill/restatement/approval/deprecation/certification/publication và evidence mutation.

## 4. Final Gatekeeper

- PASS semantics: same name/formula không bị auto merge; identity, question, definition, entity/grain/event/state và metric class rõ.
- PASS calculation: numerator/denominator, zero-denominator, aggregation/additivity, dimensions/filters/cohort/time/timezone/unit/currency/FX/null/late/restatement được khóa.
- PASS trace: source snapshot → transform/model/query hash → semantic object → dashboard/report/API/decision; tests và reconciliation cùng scope/grain/time/unit/version.
- PASS lifecycle: target là object riêng có authority; semantic diff, dependencies, acknowledgements, migration, deprecation, sunset và rollback được giữ.
- PASS safety: không invent/redefine/deploy/backfill/restate/publish/certify; six reviews PASS và final human decision PENDING.

## 5. Nguồn chính thức kiểm tra ngày 22/08/2026

- W3C RDF Data Cube Recommendation: https://www.w3.org/TR/vocab-data-cube/
- ISO/IEC 11179-3:2023: https://www.iso.org/standard/78915.html
- ISO 8000-63:2019: https://www.iso.org/standard/65344.html

Các nguồn chỉ hỗ trợ thiết kế dimensions/measures/attributes/integrity, metadata-registry items và measurement stack; không bắt buộc RDF, không thay business/accounting contract và không chứng nhận metric truth/compliance của doanh nghiệp.

## 6. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `32EC0BEBA730F7C7CC25E24656AE79DCE6D7D598E75FC48A9CDA17AE17AB9C6A` |
| evaluator | `4FFD8B8B39F6482BF71EAD0FCC7C714F85AC2A119779B3AA2BA5F2DE2D95E2B3` |
| evals | `E633581CDBF6DF0EADEF9B77CBB757B7134DD18A421FD172D6D9CBF6739AE782` |
| positive fixture | `93F8C4A76680D4D0BBD406A7CC8F827C65CC29949E93D8FE335FC13EBDC4F708` |
| negative fixture | `37981721F1A00EC067FB7F013D49DBE63FE3B63313CF61BBCC2F36D9BA926C49` |
| rules reference | `EAE266A011EB3666219E335F3773155D0FBD0EA7C5DD21F83B66B7B81F4647D6` |
| pack template | `8E9D3590B6920FFA58B485162C1CA6966DDF2F0EF52662972F8FC23002B3495F` |

## 7. Cổng còn thiếu

D10 cần pilot trên metric census, source/model/query/semantic/dashboard snapshots thật, có six owners xác nhận: business meaning/SoR, grain/formula/denominator/aggregation, time/unit/FX/accounting, target authority, lineage/tests/reconciliation, versions/dependencies/adoption/rollback, false trigger, token và duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.

