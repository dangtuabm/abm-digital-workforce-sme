---
document_code: "ABM-SQS-SC-79"
skill: "data-hygiene"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — DATA HYGIENE v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh cho inventory/SoR/classification, raw snapshot, data contract/profile, staging normalization/validation, entity resolution, transform lineage, typed quarantine, reconciliation và downstream release review. D10 chưa đạt vì chưa có baseline/with-skill pilot trên dữ liệu thật, owner ground truth, production reconciliation, token và duration.

Chuỗi kiểm định: `SKILL-CREATOR → DATA-HYGIENE-RAG → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 `designed_not_run` |
| SKILL-CREATOR quick_validate | PASS — `Skill is valid!` |
| Description | 553 ký tự, ≤ 600 |
| Body | 7.684 ký tự, ≤ 8.000 |
| Lines | 103, ≤ 500 |
| Evals | 12; trigger, must_not_trigger, no_false_ask, ambiguity, red_line, injection, adversarial |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive fixture:** `READY_FOR_HUMAN_DATA_HYGIENE_DECISION`; 0 defect; 0 review gap. Coverage: 8 sources, 8 contracts, 8 profiles, 7 transformations, 5 match rules, 5 quarantine items, 6 reconciliations, 6 downstream tests, 6 risks, 6 decisions, 7/7 tests và 6/6 reviews.

**Negative fixture:** `NOT_READY`; 181 defects; 6 review gaps. Engine chặn source/schema/metric/ground-truth fabrication, false accuracy, silent coercion/drop/merge, missing lineage/delta, macro/formula execution, PII/secret exposure, source mutation, golden merge, sensitive export, production write, publish và disposal.

## 4. Final Gatekeeper

- PASS logic: completeness/validity/consistency/uniqueness/timeliness/integrity tách accuracy; sample không đại diện population nếu chưa có basis.
- PASS trace: asset/snapshot → contract/profile → rule/activity/agent → staging/target/quarantine → reconciliation/downstream/decision.
- PASS identity: candidates, scores, calibration, false merge/split, manual-review band and survivorship proposal visible; no auto merge.
- PASS safety: raw read-only; original value retained; staging/output/quarantine separate; no silent drop, source/production mutation or sensitive export.
- PASS release: every delta explained, rollback defined, six reviews PASS and final release PENDING.

## 5. Nguồn chính thức kiểm tra ngày 22/08/2026

- ISO 8000-63:2019: https://www.iso.org/standard/65344.html
- W3C PROV-O Recommendation: https://www.w3.org/TR/prov-o/
- NIST Privacy Framework: https://www.nist.gov/privacy-framework

Các nguồn chỉ hỗ trợ process measurement, provenance và privacy-risk principles; không thay data contract, law/policy hay chứng nhận doanh nghiệp cụ thể.

## 6. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `F4D35515BFB6E7242AB39D59C2BB23F84487FE4C16DFA83DE800A477807C2E35` |
| evaluator | `01660F0FF361CA37E80A60BB8DAA17966DEDAFE882289BF53D1C267078E3AA05` |
| evals | `F9931D981104FEB4658E9CBFDD4D0B98BFAD6ED14C014799C32BA6DB24A5C6F2` |
| positive fixture | `9084AEC221F5883CC950780006B672D504C8FF6A50763220CE6F206703A0434B` |
| negative fixture | `3C49F635C178E689E77DEA39FB71FA71A0B183CCAE13F420C381BCB0E930570E` |
| rules reference | `819BDE21816E579DE073C755B37D4D1A1A480C77F669DF8F80646CD2AB6122AF` |
| pack template | `8E8F5BD00B4EC2DA6C5728EA6D25A5E9560AD096ADE1D7E8B88A232330E9FE3D` |

## 7. Cổng còn thiếu

D10 cần pilot trên raw/staging/quarantine/target snapshots thật, có six owners xác nhận: scope/SoR/semantics/ground truth, metrics, match calibration, false merge/split, lineage, source-target reconciliation, downstream/privacy/security fitness, rollback, false trigger, token và duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.
