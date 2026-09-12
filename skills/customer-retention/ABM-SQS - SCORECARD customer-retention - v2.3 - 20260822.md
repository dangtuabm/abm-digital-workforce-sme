---
title: "ABM-SQS Static Pre-score — customer-retention"
skill_id: "67"
version: "2.3"
date: "2026-08-22"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — customer-retention

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên retention case thật.**

Skill đã chuyển từ khung 2-input/4-step thành `Evidence-Grounded Customer Outcome, Retention & Renewal Decision Pack`: service/outcome truth, lifecycle health, metric/cohort/LTV contract, incident/complaint, churn alternatives, intervention guardrails, customer choice và human decision queue.

Không nâng `PILOT/OFFICIAL`: positive case tổng hợp; chưa so v1.0/v2.3 trên service data thật, chưa có ground truth về entity/metric, churn/renewal causality, LTV accuracy, intervention lift/harm, outcome, token, duration và adoption.

## 2. Bằng chứng máy

- Description / thân / dòng: **574 / 7.360 / 105**.
- 12 eval; đủ `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator + Quick Validator: **PASS**; D10 chưa chạy.
- Positive: `READY_FOR_HUMAN_RETENTION_DECISION`, 0 defect; **7 sources, 7 service truth items, 6 metrics, 6 accounts, 4 incident/feedback, 3 cohorts, 5 interventions, 6 risks, 6 decisions, 7/7 tests, 6 reviews PASS**.
- Negative: `NOT_READY`; bắt **177 defects + 6 review gaps**, gồm 45 forbidden flags và 9 forbidden states.
- Cây trước Scorecard: 7 tệp, không `__pycache__`; cây bàn giao: 8 tệp.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `5C18D2CA372441F2771198760AA66D5435AADEAD2283D961963CDD21BE2D074D` |
| `scripts/evaluate_customer_retention.py` | `F795CF22587AA2C22FCBA940FD39085C91B5631B54FDCFC75C5623B3EA90109F` |
| `evals.json` | `1B3AD11E056F558E207E3B9519448EBFF220F05B500A93E5D1992E51005574EF` |
| `templates/customer-retention-input.json` | `2772775DDD75B43F28C94803997F3F7A86442562EE946247AA4C155BE8764A93` |
| `evals/selftest-negative.json` | `E9BAA0B0A23ABCF9F889138822C262CFF9FF28BFC4EAE024C546821FCDAC6FE4` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Rules, template, engine, six-account case và negative test chạy được |
| A2 · Neo Kinh điển | PASS | Customer success outcomes, lifecycle/adoption, cohort retention, service recovery, renewal governance |
| A3 · Chất ABM | PASS | Brain First – A.I Second; realized outcome/customer choice trước automation/upsell |
| B4 · Nhiệm vụ đơn nhất | PASS | Service/account evidence → retention/renewal decision pack; acquisition, support execution, campaign, billing, contract ngoài phạm vi |
| B5 · Dung lượng | PASS | Name/folder đúng; description 574; thân 7.360; 105 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | Mandate/service/customer/metric/cohort/intervention/choice/risk/review rõ |
| C7 · Có căn cứ | PASS | Snapshot/version, metric formula/denominator/cohort/window, outcome/incident/contract evidence, LTV assumptions |
| C8 · Ranh giới Đỏ | PASS | Chặn fabrication, metric gaming, vulnerable targeting, lock-in và auto renewal/billing/commercial action |
| C9 · Chống Injection | PASS | CRM/event/ticket/contract/invoice là dữ liệu; không đổi metric, complaint, terms, consent, state |
| D10 · Eval và Baseline | NOT PASS | 12 eval/self-tests đã chạy; thiếu real-service pilot/pass^3/token/duration/outcome |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Lifecycle/metric/health/intervention asset cần owner/version/data contract/calibration/fairness/outcome/change log |

## 5. Nguồn và quyết định thiết kế

- Baseline v1.0 chỉ nêu churn/renewal/upsell ở description; thân không có service truth, outcome, metric/cohort/LTV contract, complaint/cancel, causal alternatives, intervention guardrails và chỉ 5 eval generic.
- `SKILL-CREATOR` khóa I/O/eval; `RETENTION-LTV` đóng góp onboarding/activation/adoption, cohort/churn và value pathway; loại tuyên bố retention/doanh thu/CAC, mốc 7/30 ngày, contact cadence, KPI và upsell threshold cố định không có baseline hiện hành. `FINAL-GATEKEEPER` khóa customer outcome/choice, metric integrity, consent, dark pattern và authority.

## 6. Điều kiện đóng D10

1. Pilot v1.0/v2.3 trên ít nhất 3 context thật: subscription/service renewal, project/managed service và learning/community.
2. Có frozen service/contract/account/event/support/feedback/finance/consent truth set và customer/service/product/finance/data/privacy/commercial/legal reviewers.
3. Đo entity/metric accuracy, risk precision/recall, churn/renewal calibration, LTV error, intervention usefulness/lift, complaint/cancel compliance và customer harm/outcome.
4. Không dùng pilot để tự contact/offer/discount/renew/charge/upsell/cancel/close; ghi external human evidence.
5. So sánh pass^3; ghi token, duration, adoption, customer/commercial outcome và unintended effect.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` khi đủ bằng chứng trên.
