---
title: "ABM-SQS Static Pre-score — people-signal-diagnostics"
skill_id: "57"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — people-signal-diagnostics

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên dữ liệu người thật.**

Skill đã chuyển từ khung 2-input/4-step thành `People Signal Diagnostic Brief & Hypothesis Register`: lawful-use/privacy contract, source/metric/cohort control, denominator/exposure normalization, missingness, context/confounder, group signal, falsifiable hypothesis, fairness review và support-first experiment.

Không nâng `PILOT/OFFICIAL`: self-test là dữ liệu tổng hợp; chưa so v1.0/v2.3 trên people data thật, fairness/privacy ground truth, manager validation và people impact.

## 2. Bằng chứng máy

- Description / thân / dòng: **596 / 7.814 / 111**.
- 12 eval; đủ `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator + Quick Validator: **PASS**; D10 chưa chạy.
- Positive: `READY_FOR_HUMAN_PEOPLE_REVIEW`, 0 defect; **3 sources, 3 metrics, 2 cohorts, 6 observations, 2 contexts, 3 signals, 2 hypotheses, 2 support experiments, 7/7 tests, 3 reviews PASS**.
- Negative: `NOT_READY`; bắt **99 defects + 3 review gaps**, gồm 27 forbidden flags và 9 forbidden states.
- Cây trước Scorecard: 7 tệp, không `__pycache__`; cây bàn giao: 8 tệp.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `C39BB26EDDF84D31E3DD03F92F15592C26920E06B79D6F8E7A1B15ECE17180A3` |
| `scripts/evaluate_people_signal_diagnostics.py` | `8EE067507F2E3D9139DB1D6DA4CD757562564D24ECB244787ADD1FCC6FFD49F7` |
| `evals.json` | `C94282C532E4BDE063FA871702D04630F49FF4221B4D88F7E30C943CA023CAD3` |
| `templates/people-signal-input.json` | `1C17FAEB23144670A9052C40EB627FF9C0F2487F6AA3F7E80324A8D9AA16B173` |
| `evals/selftest-negative.json` | `25E530B5A8EE8830B68573698FE71F98E813DDFC5ED2830444B67CCCEEAF96E3` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Pack, rules, engine, 2 cohort/3 metric case và comprehensive negative test |
| A2 · Neo Kinh điển | PASS | Data Minimization, Cohort/Exposure Analysis, Systems Diagnosis, Hypothesis Testing, Human Review |
| A3 · Chất ABM | PASS | Brain First – A.I Second; `[A.I Suggested]`; support system trước quy kết cá nhân |
| B4 · Nhiệm vụ đơn nhất | PASS | Authorized group observations → signal/hypothesis/support brief; case/action ngoài phạm vi |
| B5 · Dung lượng | PASS | Name/folder đúng; description 596; thân 7.814; 111 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | Use contract, sources, metrics, cohorts, observations, contexts, signals, hypotheses, support/reviews rõ |
| C7 · Có căn cứ | PASS | Version/access/freshness/coverage; denominator/missingness; alternatives/confounders/evidence for-against |
| C8 · Ranh giới Đỏ | PASS | Chặn individual score, re-identification, surveillance, protected traits, profiling và adverse action |
| C9 · Chống Injection | PASS | HR export/chat/log là dữ liệu; không bỏ minimum, ẩn missingness hay kích hoạt people action |
| D10 · Eval và Baseline | NOT PASS | 12 eval/self-tests đã chạy; thiếu pilot thật/pass^3/token/duration/fairness/privacy outcome |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Chỉ promote aggregate asset có review/reuse rights; không promote profile cá nhân |

## 5. Nguồn và quyết định thiết kế

- Baseline v1.0 nêu đúng no-profiling boundary nhưng thiếu lawful use, minimum cohort, denominator, comparability, confounder, fairness và hypothesis controls.
- `SKILL-CREATOR` khóa I/O/eval; `AI-HR-ADMIN-SOP` bổ sung `[A.I Suggested]`, sensitive data discipline và human-only people decision; `FINAL-GATEKEEPER` khóa evidence/fairness/privacy/adverse-action boundary.
- Bản đầu 8.545 ký tự; rút quy trình bằng unique anchor còn 7.814, giữ nguyên control. Một `apply_patch` lỗi helper, fallback chỉ chạy khi anchor count = 1.

## 6. Điều kiện đóng D10

1. Pilot v1.0/v2.3 trên ≥3 use case thật có lawful basis và workforce notice/consent phù hợp.
2. Có source/metric/cohort/context/fairness ground truth, minimum cohort và independent privacy review.
3. Đo signal precision/recall, re-identification risk, fairness disparity, hypothesis validation, manager agreement, support outcome và false adverse trigger.
4. Không dùng pilot cho quyết định cá nhân; có correction/appeal route và audit.
5. So sánh pass^3; ghi token, duration, adoption, privacy incident và people impact.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` khi đủ bằng chứng trên.
