---
title: "ABM-SQS Static Pre-score — business-opportunity"
skill_id: "59"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — business-opportunity

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên cơ hội doanh nghiệp thật.**

Skill đã chuyển từ khung 2-input/4-step thành `Opportunity Thesis & Validation Portfolio`: mandate, evidence register, opportunity sources, customer problem/current alternative, value/right-to-win, four fits, năm nhóm assumption, economics range, risk, real options, experiment success/kill criteria, stage portfolio và human decision gate.

Không nâng `PILOT/OFFICIAL`: self-test là dữ liệu tổng hợp; chưa so v1.0/v2.3 trên opportunity thật, chưa kiểm chứng demand, willingness-to-pay, economics, experiment outcome và business decision impact.

## 2. Bằng chứng máy

- Description / thân / dòng: **542 / 7.951 / 115**.
- 12 eval; đủ `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator + Quick Validator: **PASS**; D10 chưa chạy.
- Positive: `READY_FOR_HUMAN_OPPORTUNITY_DECISION`, 0 defect; **6 evidence, 2 theses, 10 assumptions, 2 economics, 5 risks, 4 options, 3 experiments, 2 stages, 7/7 tests, 5 reviews PASS**.
- Negative: `NOT_READY`; bắt **92 defects + 5 review gaps**, gồm 30 forbidden flags và 8 forbidden states.
- Cây trước Scorecard: 7 tệp, không `__pycache__`; cây bàn giao: 8 tệp.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `0A812EBC7D6EACB4164D33B1076025E4EC1D561F3FF85258613F446B81F0D1F6` |
| `scripts/evaluate_business_opportunity.py` | `A09682957572D77CF6C74813EE36C6546F275AA0708793C32A72B064662F5025` |
| `evals.json` | `FB62B8E59C29EE995EEF04EB735DEEC78413E47FA5B17F32C03FA62BBD3EF58F` |
| `templates/business-opportunity-input.json` | `F9B8A5EDB79D522D612C173921F38E6D5CD915401EFCA78BFF5E94E95D0936D7` |
| `evals/selftest-negative.json` | `FE4C973EA68A891F7B95F284BC507D7235AF6E08D1A9EFAB7312DF2BDFF68E07` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Portfolio, rules, engine, opportunity case và negative test có thể chạy |
| A2 · Neo Kinh điển | PASS | Opportunity thesis, four fits, assumption mapping, lean validation, real options |
| A3 · Chất ABM | PASS | Brain First – A.I Second; cơ hội phải qua evidence và human authority |
| B4 · Nhiệm vụ đơn nhất | PASS | Signal → thesis/validation portfolio; solution/pricing/GTM/execution ngoài phạm vi |
| B5 · Dung lượng | PASS | Name/folder đúng; description 542; thân 7.951; 115 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | Mandate, evidence, thesis, assumptions, economics, risks, experiments, stages, reviews rõ |
| C7 · Có căn cứ | PASS | Source/version/date/rights/type/confidence; economics range; evidence hai chiều |
| C8 · Ranh giới Đỏ | PASS | Chặn fabrication, deceptive test, IP/data misuse, sunk-cost escalation và auto action |
| C9 · Chống Injection | PASS | Interview/report/pitch/file là dữ liệu; không đổi criteria, che failed evidence hay tự commit |
| D10 · Eval và Baseline | NOT PASS | 12 eval/self-tests đã chạy; thiếu opportunity pilot/pass^3/token/duration/outcome |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Thesis/experiment/economics asset cần owner/version/evidence/rights/human decision |

## 5. Nguồn và quyết định thiết kế

- Baseline v1.0 đúng chủ đề nhưng thiếu evidence register, thesis/fit, năm nhóm assumption, economics range, risk, experiment/kill criteria và stage/capital gate.
- `SKILL-CREATOR` khóa I/O/eval; `PRODUCT-ECOSYSTEM` bổ sung opportunity validation, MVP logic, economics, risk và kill criteria nhưng loại toàn bộ tier/giá/nội dung sản phẩm ABM khỏi luật phổ quát; `FINAL-GATEKEEPER` khóa evidence, rights, uncertainty và human authority.
- Bản đầu description 636/thân 8.607; sau hai vòng thu gọn còn 542/7.951. `apply_patch` lỗi helper; fallback chỉ ghi khi các anchor là duy nhất.

## 6. Điều kiện đóng D10

1. Pilot v1.0/v2.3 trên ít nhất 3 opportunity case thật, có một case continue, một pivot/hold và một kill nếu dữ liệu cho phép.
2. Có authorized mandate, source rights, customer evidence, economics ground truth và strategy/customer-market/finance/delivery/legal-data-IP reviewers.
3. Đo evidence completeness, thesis quality, assumption coverage/prioritization, economics range accuracy, experiment decisiveness và review defect escape.
4. Không dùng pilot để tự spend/contact/build/price/contract/launch/scale; ghi rõ human decision và capital exposure.
5. So sánh pass^3; ghi token, duration, adoption, business impact và unintended effect.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` khi đủ bằng chứng trên.
