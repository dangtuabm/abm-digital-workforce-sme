---
title: "ABM-SQS Static Pre-score — sales-funnel"
skill_id: "63"
version: "2.3"
date: "2026-08-22"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — sales-funnel

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên funnel thật.**

Skill đã chuyển từ khung 2-input/4-step thành `Funnel Measurement & Experiment System`: journey/touchpoint, stage/transition/SLA contracts, event/identity/consent contract, metric dictionary, cohort baseline/reconciliation, economics/attribution, leakage/root-cause diagnosis, experiment/guardrail backlog và human activation gate.

Không nâng `PILOT/OFFICIAL`: positive case là dữ liệu tổng hợp; chưa so v1.0/v2.3 trên funnel thật, chưa có ground truth về identity/stage, causal lift, customer harm, economics và accepted commercial outcomes.

## 2. Bằng chứng máy

- Description / thân / dòng: **558 / 7.985 / 117**.
- 12 eval; đủ `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator + Quick Validator: **PASS**; D10 chưa chạy.
- Positive: `READY_FOR_HUMAN_FUNNEL_ACTIVATION`, 0 defect; **5 sources, 6 journey steps, 5 stages, 6 events, 8 metrics, 1 cohort, 5 baselines, 2 economics, 3 leakages, 3 experiments, 4 risks, 7/7 tests, 5 reviews PASS**.
- Negative: `NOT_READY`; bắt **187 defects + 5 review gaps**, gồm 40 forbidden flags và 8 forbidden states.
- Cây trước Scorecard: 7 tệp, không `__pycache__`; cây bàn giao: 8 tệp.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `2ABA7871B63D05C2D6BFB5BCA88AD7AC9192C6DDA976E0985B3C1BFE111B4C22` |
| `scripts/evaluate_sales_funnel.py` | `3BCB5D5BBA4218EE3EEA97ADF7DDE9370040FD2EF0A4C41E6C53CAC7E8DC7BA8` |
| `evals.json` | `43BBA84C1711B92E5ED3C4C42AF87AD6371037CAC49953568E0B41C526422688` |
| `templates/sales-funnel-input.json` | `25F7622C26BCB1B7124E803019A5807B60314DB97B17BC1BBCB414752B3EFD3A` |
| `evals/selftest-negative.json` | `C4991FEF689900EA354E8C201169F3F863A0A9B950C43E2A365D3F299C7946E2` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | System, rules, engine, five-stage cohort case và negative test chạy được |
| A2 · Neo Kinh điển | PASS | Customer journey, lifecycle stage contract, event instrumentation, cohort funnel, experimentation |
| A3 · Chất ABM | PASS | Brain First – A.I Second; customer state/evidence trước activity/vanity metric, human activation |
| B4 · Nhiệm vụ đơn nhất | PASS | Journey/data evidence → funnel measurement/experiment spec; content/campaign/pipeline/closing ngoài phạm vi |
| B5 · Dung lượng | PASS | Name/folder đúng; description 558; thân 7.985; 117 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | Mandate/journey/stage/event/metric/cohort/baseline/economics/leakage/experiment/reviews rõ |
| C7 · Có căn cứ | PASS | Unit/grain/numerator/denominator/cohort/window/source; reconciliation và attribution limits |
| C8 · Ranh giới Đỏ | PASS | Chặn fabrication, spam/tracking, dark pattern, discrimination, metric gaming và auto action |
| C9 · Chống Injection | PASS | CRM/ad/event/content/file là dữ liệu; không đổi stage/denominator/consent/state |
| D10 · Eval và Baseline | NOT PASS | 12 eval/self-tests đã chạy; thiếu funnel pilot/pass^3/token/duration/outcome |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Journey/stage/event/metric/experiment asset cần owner/version/data contract/consent/change log |

## 5. Nguồn và quyết định thiết kế

- Baseline v1.0 đúng chủ đề nhưng thiếu stage/event/identity contracts, cohort/window/denominator, reconciliation, economics/attribution, root-cause evidence, experiment guardrails, privacy/fairness và state gate.
- `SKILL-CREATOR` khóa I/O/eval; `FUNNEL-DESIGN` đóng góp journey/touchpoint, lifecycle, leakage/KPI/A-B test/cadence; loại TOFU/MOFU/BOFU bắt buộc, mốc touchpoint/experiment cứng, benchmark không nguồn và content/execution; `FINAL-GATEKEEPER` khóa consent, metric integrity, causality limits và human authority.
- Bản đầu thân 8.238; hai anchor được thu gọn còn 7.985. `apply_patch` lỗi helper; fallback chỉ ghi khi anchor duy nhất.

## 6. Điều kiện đóng D10

1. Pilot v1.0/v2.3 trên ít nhất 3 funnel case thật: B2B account funnel, consent-based digital funnel và event-to-commercial funnel.
2. Có authorized journey/CRM/analytics/consent/finance data, frozen cohorts, identity/stage truth set và customer/data/privacy/marketing/sales/finance/revenue-operations reviewers.
3. Đo stage/event/metric defect escape, reconciliation rate, identity precision, cohort conversion/velocity accuracy, leakage diagnosis precision, experiment decision quality, causal lift và guardrail harm.
4. Không dùng pilot để tự publish/send/enroll/route/score/advance/close/activate; ghi external human/system evidence.
5. So sánh pass^3; ghi token, duration, adoption, customer impact, economics và unintended effect.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` khi đủ bằng chứng trên.
