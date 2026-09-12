---
document_code: "ABM-SQS-SC-99"
skill: "ai-evaluation"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — A.I EVALUATION v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh cho evaluation contract, system fingerprint, baseline/comparator, test-set/ground-truth, metric/threshold, capability/grounding, safety/security/privacy, affected groups/human review, robustness/operations/cost/value, red-team, regression, monitoring và lifecycle. Skill không tự chứng nhận, release, deploy, publish hay khẳng định ROI/causality. D10 chưa đạt vì chưa pilot trên hệ thống A.I thật.

Chuỗi: `SKILL-CREATOR → A.I-ROI-MEASURE → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 chưa có baseline/evidence/tokens/duration |
| SKILL-CREATOR quick_validate | PASS |
| Description | 525 ký tự, ≤ 600 |
| Body | 7.988 ký tự, ≤ 8.000 |
| Lines | 105, ≤ 500 |
| Evals | 12; trigger/must_not_trigger/routing/no_false_ask/ambiguity/missing/red_line/injection/dataset-metric/capability-safety/operations-value/regression-lifecycle |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive:** `READY_FOR_HUMAN_EVALUATION_DECISION`; 0 defect; 0 review gap. Coverage: 10 evidence sources, 6 baselines, 12 test cases, 12 metrics, 6 review records, 8 failure categories, 8 red-team cases, 8 operations metrics, 6 value metrics, 8 monitoring controls, 6 decisions, 6 risks, 8/8 tests và 6/6 reviews.

**Negative:** `NOT_READY`; 128 defects; 6 review gaps. Chặn holdout tuning/leakage, cherry-pick/xóa failures, đổi threshold hậu nghiệm, UNKNOWN/missing thành PASS/zero, average critical gate, single-score release, ground truth bịa, self-grade/uncalibrated judge, synthetic/offline thành production proof, metric thiếu denominator, baseline thiếu nhưng claim ROI, causal claim thiếu design, bỏ costs, unsafe live test, unauthorized data/secret, tự release/deploy/mutate/approve/publish/notify/purchase và injection.

## 4. Final Gatekeeper

- PASS contract/fingerprint: decision, scope, users/affected parties, success/stop, authority và exact model/prompt/Agent/tool/data/policy versions.
- PASS baseline/data: comparator comparable; population/strata/coverage, rights/provenance/hash, holdout/leakage, qualified ground truth/calibration/adjudication.
- PASS metrics: formula/unit/denominator/direction/slices/threshold/severity/missing/uncertainty; threshold khóa trước result; critical gate conjunctive.
- PASS quality/trust: capability/grounding, safety/security/privacy, affected groups, Human Control, red-team, raw failure/near miss và reproduction evidence.
- PASS operations/value/lifecycle: workload/tail/reliability/recovery/cost, baseline/total cost/attribution/sensitivity, regression, canary/rollback, monitoring/drift/incident/recertification.

## 5. Nguồn specialist được sửa cứng

Giữ lõi `AI-ROI-MEASURE`: baseline trước–sau, delta vận hành/kinh tế, tổng chi phí, không bịa ROI và human approval trước publish. Chuyển các giả định 1 tháng, 3–6 tháng, 16 chỉ số, ngưỡng 10%/100%/1.000%, 3–5 quotes, 1/5-pager và Notion thành cấu hình theo outcome cycle, metric contract, authority và communication need. Bổ sung system fingerprint, test-set integrity, ground truth/calibration, critical gates, safety/red-team, affected groups, robustness, regression và production lifecycle.

## 6. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `5ED809A81C888A52016B89CC9CA7A8B3AD235BBBA1B1A08EEA71B1292861508A` |
| evaluator | `F01E910619BA688081F32CC7E98F90EA7FC8E735CFED4FE023A0BC980C5FF7BD` |
| evals | `EB0465B29120A25C181F03A760E8C421F4869172708FC7B2E2516F2BBDE54372` |
| positive fixture | `DC3A50AF5CD8D6923A27FA0BDA2E267D0B6392E1A4B95D877BAD84D01015CEE7` |
| negative fixture | `3CE76C5ADACE08E38A774D28D2A10746B7FC11E734601F16B42BA1003D32EECB` |
| rules | `2E6D5DFE128FBC3F347D27612EDF6BB9F7F1F166C22A9CA1B635A49B585AA725` |
| template | `669E53E84A6CD9C82B7183ADF63778FACC4C99EFA0B71095004190A575829664` |

## 7. Cổng còn thiếu

D10 cần pilot trên model/prompt/Agent/workflow thật với frozen fingerprint, independent holdout, qualified ground truth/calibration, baseline/comparator, critical gates, safety/red-team, human/affected-group slices, load/failure injection, cost/value attribution, canary/rollback và monitoring; đo false trigger, token và duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.
