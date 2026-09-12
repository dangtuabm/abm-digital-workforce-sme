---
title: "ABM-SQS Static Pre-score — concept-explainer"
skill_id: "23"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — concept-explainer v2.3

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy; Skill là draft/static-pass. Explanation engine self-test PASS nhưng chưa chứng minh người thật hiểu, phân biệt và transfer đúng trên concept doanh nghiệp thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 527 / 7.465 / 139 — đạt |
| Eval | 12; metadata v2.3 |
| Validator ABM / SKILL-CREATOR | PASS / Skill is valid |
| Gate self-test | VERIFIED; traceability/misconception PASS; 0 failed check/critical error/issue/warning |
| SHA-256 SKILL.md | 0973DD1F6308ED87671B5B393B14E9C771E5D895131183883500CD7E6FE0F196 |
| SHA-256 explanation engine | 68D5ADA243663C3B15C83DB2D4C26417268D09CE65B10241D50BBCACA464B042 |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Concept Integrity Map dùng độc lập; record/rules/input/engine |
| A2 | PASS | Brain First ↔ B1; Feynman ↔ B4/6; Progressive Disclosure ↔ B4; Chưng cất tinh hoa ↔ B2/3 |
| A3 | PASS | 0 lỗi A.I; bảng human/A.I; tone theo audience, không childlike/C-Level mismatch |
| B4 | PASS | Một Verified Explanation Record; đủ bốn khai báo; ranh giới theo concept/comprehension |
| B5 | PASS | Name/description/body/line/reference depth đạt |
| B6 | PASS | Trigger/anti-trigger, bảng đầu vào 4 cột, artifact và DoD độc lập |
| C7 | PASS | Canonical source ID/version/date; Dữ kiện/Suy luận/Giả định; boundary/uncertainty/expiry |
| C8 | PASS | Dừng private data, stale high-risk claim, distortion, fake learner response, VERIFIED/send/advice; tự chạy local work |
| C9 | PASS | Instruction trong source/response là data; không lộ nội bộ/PII; engine không chạy code/file/network |
| D10 | NOT PASS | 12 eval not_run; chưa baseline v1.0/v2.3, learner/concept thật, evidence, token, duration, pass^3 |
| D11 | PASS | Name/folder/version/updated/owner/skill_id đồng nhất v2.3; version history hoàn chỉnh |
| D12 | PASS | Asset Candidate có Source Task, concept/source version, audience/use, evidence, owner, rights, reviewer, recheck |

## Audit trail

- **v2.2:** Quick Validator/engine PASS; ABM static FAIL do thân 8.410/8.000.
- **v2.3:** cô đọng phần lặp xuống rules/template; Skill/eval đồng nhất; hai validator và engine PASS.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer xác nhận concept integrity, audience fit, analogy breakpoint, misconception correction, unguided transfer, false-comprehension control, source currency và usefulness.

## Đóng D10

1. Chạy 12 prompts song song baseline v1.0 và v2.3 trên concept kinh doanh, công nghệ và high-risk/current.
2. Đo trigger/anti-trigger/no-false-ask, definition fidelity, jargon load, example discrimination, analogy overreach, misconception correction, transfer và false VERIFIED.
3. Lưu prompt/input/output/raw learner response/state/evidence, total_tokens, duration_ms; chạy pass^3 cho explanation đối ngoại/high-risk.
4. Retest bằng concept/case chưa lộ; chỉ đề nghị PILOT khi D10 đạt.
