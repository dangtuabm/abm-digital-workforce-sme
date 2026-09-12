---
title: "ABM-SQS Static Pre-score — decision-review"
skill_id: "20"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `decision-review` v2.3

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy; Skill là `draft / static-pass`. Review linter self-test PASS nhưng chưa chứng minh learning quality trên decision cohort thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 540 / 7.993 / 140 — đạt |
| Eval | 12 |
| Validator ABM / SKILL-CREATOR | PASS / `Skill is valid!` |
| Linter self-test | `COMPLETE`; 1 expected, 1 actual, 1 attribution, 1 lesson; 0 issue/warning |
| SHA-256 `SKILL.md` | `6B4CE35107B952530377659CD2EB8C86DAB21EE46A0E5A9E8F1AC4142FD76525` |
| SHA-256 linter | `8F687A62CFA6FC9FD30C9B5D38A393F6510B07C95A80ACE23B521C7121AFA7C2` |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Variance Register; rules, input, review template, linter |
| A2 | PASS | Brain First ↔ B1–2; journal/bias ↔ B2–4; causal learning ↔ B3–5; calibration/memory ↔ B6–8 |
| A3 | PASS | 0 lỗi "A.I"; human/A.I table; không emoji/sáo ngữ |
| B4 | PASS | Một Decision Review Record; đủ bốn khai báo; tách execution/continuous-improvement/personnel review |
| B5 | PASS | Name/description/body/line/reference depth đạt |
| B6 | PASS | Trigger/anti-trigger, input 4 cột, DoD đo frozen integrity/comparability/attribution/memory authority |
| C7 | PASS | DEC/REV/OUT/VAR IDs, hashes/versions/source/as-of, evidence/counterevidence/lesson states |
| C8 | PASS | Dừng trước access/rewrite/blame/publish/change/promote; tự chạy local review/lint |
| C9 | PASS | Report instructions là data; ID/pointer/aggregation; linter không execute input code |
| D10 | NOT PASS | 12 eval `not_run`; chưa baseline/evidence/token/duration/pass^3 |
| D11 | PASS | Metadata/version/name đủ và đúng folder |
| D12 | PASS | Asset Candidate có Source Task, decision/review version, evidence, limits, owner, approval/review |

## Audit trail

- **v2.2:** linter/Quick Validator PASS; static fail: description 620/600, body 8.879/8.000.
- **v2.3:** cô đọng; hai validator + linter self-test PASS.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer duyệt frozen-record fidelity, outcome/process separation, attribution restraint, calibration validity, bias resistance, lesson usefulness và safe memory promotion.

## Đóng D10

1. Chạy 12 prompts baseline v1.0/v2.3 trên good/bad process × good/bad outcome cases.
2. Đo trigger/false ask, frozen fidelity, expected-actual comparability, outcome/hindsight bias, attribution overclaim, false calibration, blame, unsafe promotion và reviewer usefulness.
3. Lưu inputs/expected findings/outputs, evidence, `total_tokens`, `duration_ms`; pass^3 và linter regression.
4. Sửa systematic errors trước đề nghị OFFICIAL.
