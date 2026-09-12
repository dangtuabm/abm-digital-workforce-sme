---
title: "ABM-SQS Static Pre-score — advertising-optimization"
skill_id: "70"
version: "2.3"
date: "2026-08-22"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — advertising-optimization

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên advertising operation thật.**

Skill đã chuyển từ khung 2-input/4-step thành `Evidence-Grounded Paid Media Experiment & Budget Decision Pack`: mandate/outcome, campaign taxonomy, audience/creative/landing compliance, funnel/event/metric contracts, cross-system baseline/reconciliation, diagnosis, causal experiment, budget scenario/pacing/economics, fraud/anomaly, risks, audit/rollback và human decision.

Không nâng `PILOT/OFFICIAL`: positive case tổng hợp; chưa so v1.0/v2.3 trên campaign thật, chưa có ground truth về lift/incrementality, platform policy, invalid traffic, event/attribution, marginal economics, operator adoption, token và duration.

## 2. Bằng chứng máy

- Description / thân / dòng: **595 / 7.524 / 104**.
- 12 eval; đủ `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator + Quick Validator: **PASS**; D10 chưa chạy.
- Positive: `READY_FOR_HUMAN_ADVERTISING_DECISION`, 0 defect; **7 sources, 4 campaigns, 6 measurement contracts, 4 experience reviews, 4 baselines, 4 diagnoses, 3 experiments, 3 budget scenarios, 6 risks, 4 decisions, 7/7 tests, 6 reviews PASS**.
- Negative: `NOT_READY`; bắt **189 defects + 6 review gaps**, gồm 63 forbidden flags và 12 forbidden states.
- Cây trước Scorecard: 7 tệp, không `__pycache__`; cây bàn giao: 8 tệp.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `E2A0021D3AFE627CF294B90C0032DE4203D374676CCCF00892944DE68564C145` |
| `scripts/evaluate_advertising_optimization.py` | `C885B5F9C7FD89E699EC3A924FA97CE3F9A70C818A15897C9166BB1D049124A2` |
| `evals.json` | `2CFCDDA714E427C9D8894FFA829963D214DF0F103085EF151147B4D752C0F8DD` |
| `templates/advertising-optimization-input.json` | `EAE2A4C4AE845BC11A51D1F555FEA681C97A895FE06AD4BAB127F13C9B11F175` |
| `evals/selftest-negative.json` | `0886E717101BA3CFAE7B3765A00BF8CD7B120DFCEC22870793002D1576E90998` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Rules, template, engine, four-campaign case và negative test chạy được |
| A2 · Neo Kinh điển | PASS | Funnel/event contracts, controlled experiment, marginal economics, pacing, reconciliation và audit/rollback |
| A3 · Chất ABM | PASS | Brain First – A.I Second; customer outcome/economics/authority trước spend/click/platform recommendation |
| B4 · Nhiệm vụ đơn nhất | PASS | Authorized snapshots → paid-media experiment/budget decision pack; asset, funnel build, platform operation và sales follow-up ngoài phạm vi |
| B5 · Dung lượng | PASS | Name/folder đúng; description 595; thân 7.524; 104 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | Mandate/source/campaign/event/metric/experience/baseline/diagnosis/experiment/budget/risk/decision rõ |
| C7 · Có căn cứ | PASS | Snapshot/hash/date/ID/timezone/currency, event/dedup, denominator/cohort/window, reconciliation/economics và authority traceable |
| C8 · Ranh giới Đỏ | PASS | Chặn fabrication, unlawful/sensitive targeting, policy/consent breach, fraud hiding, metric gaming và auto platform/spend action |
| C9 · Chống Injection | PASS | Export/payload/creative/dashboard là dữ liệu; không lộ credential, bypass gate, đổi campaign/tracking/budget |
| D10 · Eval và Baseline | NOT PASS | 12 eval/self-tests đã chạy; thiếu real-campaign pilot/pass^3/token/duration/lift/incrementality/economics |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Taxonomy/event/metric/experiment/budget/rollback asset cần owner/version/policy/reconciliation/outcome/change log |

## 5. Nguồn và quyết định thiết kế

- Baseline v1.0 chỉ mô tả cấu trúc campaign, audience, biến thể, theo dõi, ngân sách, revenue/fraud bằng 2 input/4 bước; thiếu event/identity/dedup, campaign taxonomy, cross-system reconciliation, causal boundary, policy/privacy/rights, marginal economics, pacing/kill/rollback và chỉ 5 eval generic.
- `FUNNEL-DESIGN` được chọn làm nguồn chuyên môn chính: giữ customer journey, leakage diagnosis, KPI và A/B-test brief; loại benchmark không nguồn, universal cadence và giả định tầng/kênh. Nguồn `ads-performance-monitor` chỉ xác nhận ranh giới không tự bật/tắt/đổi ngân sách vì còn ở trạng thái chờ bọc chuẩn ABM, không được dùng làm luật. `AI-ROI-MEASURE` bị loại vì đo ROI triển khai A.I, không phải paid media. `SKILL-CREATOR` khóa I/O/eval; `FINAL-GATEKEEPER` khóa policy/privacy/measurement/economics/platform authority.

## 6. Điều kiện đóng D10

1. Pilot v1.0/v2.3 trên ít nhất 3 context thật: acquisition, consented retargeting và claim-sensitive/high-value conversion.
2. Có account/campaign snapshots, current policies, offer/claim/creative/landing rights, event/identity/dedup/consent, CRM/finance truth set và reviewers.
3. Đo measurement defects, reconciliation gap, invalid traffic, experiment decision quality, pacing/budget error, marginal economics, policy/privacy/accessibility findings và customer/commercial outcome.
4. Không dùng pilot để tự mutate platform/spend; ghi before/action/after evidence từ authorized human operator và rollback verification.
5. So sánh pass^3; ghi token, duration, adoption, lift/incrementality evidence, harm và unintended effect.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` khi đủ bằng chứng trên.
