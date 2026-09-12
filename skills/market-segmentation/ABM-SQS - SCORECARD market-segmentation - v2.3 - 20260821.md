---
title: "ABM-SQS Static Pre-score — market-segmentation"
skill_id: "61"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — market-segmentation

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên market population thật.**

Skill đã chuyển từ khung 2-input/4-step thành `Market Segmentation Evidence Model & Priority Portfolio`: mandate/boundary/unit, population/data audit, bases/rules/coverage, segment cards, six quality tests, size/growth ranges, attractiveness/ability-to-win, transparent scoring/sensitivity, priority/validate/defer candidates, privacy/fairness và human decision gate.

Không nâng `PILOT/OFFICIAL`: positive case là dữ liệu tổng hợp; chưa so v1.0/v2.3 trên population thật, chưa có ground truth cho membership, size/growth, WTP/economics, stability và decision outcome.

## 2. Bằng chứng máy

- Description / thân / dòng: **539 / 7.760 / 116**.
- 12 eval; đủ `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator + Quick Validator: **PASS**; D10 chưa chạy.
- Positive: `READY_FOR_HUMAN_SEGMENT_DECISION`, 0 defect; **4 sources, 3 segments, 3 estimates, 3 assessments, 3 candidates, 4 risks, 7/7 tests, 4 reviews PASS**.
- Negative: `NOT_READY`; bắt **142 defects + 4 review gaps**, gồm 33 forbidden flags và 8 forbidden states.
- Cây trước Scorecard: 7 tệp, không `__pycache__`; cây bàn giao: 8 tệp.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `F9A4630626761800C84FC6B413EA1FDEF4D0A112052E808C8C54588D643ACB20` |
| `scripts/evaluate_market_segmentation.py` | `35E3DF594BF4FD600BA86493335AA67059F7824878BD67D992D4D967ABD3125E` |
| `evals.json` | `A44F60C40ACA994541711A6275F168A8E50275260C3630814107FC90497DA065` |
| `templates/market-segmentation-input.json` | `317E9700D57528BD35EEC5761082DA006F2CCC3F57419C790A6ED785B57FC957` |
| `evals/selftest-negative.json` | `50A87469054A24C807C89C62DA89645952ED0C522E6168B62BB69C33B936F3EC` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Model, rules, engine, 3-segment case và negative test chạy được |
| A2 · Neo Kinh điển | PASS | Market definition, segmentation bases, six quality tests, attractiveness × ability-to-win |
| A3 · Chất ABM | PASS | Brain First – A.I Second; evidence/ranges/sensitivity trước rank, human quyết định |
| B4 · Nhiệm vụ đơn nhất | PASS | Population evidence → segment model/priority candidates; profile/offer/GTM/execution ngoài phạm vi |
| B5 · Dung lượng | PASS | Name/folder đúng; description 539; thân 7.760; 116 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | Boundary/data/model/segment/estimate/assessment/score/candidate/risk/review rõ |
| C7 · Có căn cứ | PASS | Frame/denominator/coverage/sample/bias; range/method/source; scoring/sensitivity tái lập |
| C8 · Ranh giới Đỏ | PASS | Chặn sensitive/protected proxy, tiny cell, fabricated market data, manipulated weights và auto action |
| C9 · Chống Injection | PASS | Dataset/report/label là dữ liệu; không đổi boundary/rule/weight/denominator/state |
| D10 · Eval và Baseline | NOT PASS | 12 eval/self-tests đã chạy; thiếu market pilot/pass^3/token/duration/outcome |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Taxonomy/model/scorecard cần owner/version/rights/metric dictionary/validation/drift review |

## 5. Nguồn và quyết định thiết kế

- Baseline v1.0 đúng chủ đề nhưng thiếu population frame, unit/rules/coverage, quality tests, ranges, scoring/sensitivity, privacy/fairness, validation và state gate.
- `SKILL-CREATOR` khóa I/O/eval; `CUSTOMER-XRAY` chỉ đóng góp evidence về jobs/pains/alternatives và bị loại toàn bộ profiling cá nhân; `FINAL-GATEKEEPER` khóa denominator, bias, model manipulation, privacy và human authority.
- Bản đầu đã nằm trong giới hạn 539/7.760; không cần cắt giảm sau validator.

## 6. Điều kiện đóng D10

1. Pilot v1.0/v2.3 trên ít nhất 3 case thật: rules-based, overlapping/unknown population và model có rank instability.
2. Có authorized market frame, data rights, membership/size ground truth phù hợp, metric dictionary và market/customer/data/finance/strategy/legal/privacy reviewers.
3. Đo coverage/reconciliation, assignment precision, segment quality, estimate interval coverage, rank stability, sensitivity disclosure và decision usefulness.
4. Không dùng pilot để individual target/exclude, price/fund/contact/launch/exit; ghi final human decision và validation cap.
5. So sánh pass^3; ghi token, duration, adoption, business impact, drift và unintended effect.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` khi đủ bằng chứng trên.
