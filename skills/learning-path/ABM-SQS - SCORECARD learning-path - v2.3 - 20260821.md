---
title: "ABM-SQS Static Pre-score — learning-path"
skill_id: "24"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — learning-path v2.3

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy; Skill là draft/static-pass. Path engine self-test PASS nhưng chưa chứng minh stage completion, workplace transfer hoặc manager usefulness trên learner thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 553 / 7.821 / 139 — đạt |
| Eval | 12; metadata v2.3 |
| Validator ABM / SKILL-CREATOR | PASS / Skill is valid |
| Gate self-test | READY_FOR_PILOT; effort 20/24 giờ; 2 stages; 0 dependency/guardrail/issue/warning |
| SHA-256 SKILL.md | D1436F3AD1466D6F467A2AF8614C17178A79F70688CE5CE58B3AB7E930D3E93F |
| SHA-256 path engine | 21148EA9B94C85330B68E2B13463C131964B73D46A738E16204145680DF99B62 |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Competency Gap Map dùng độc lập; path/rules/input/engine |
| A2 | PASS | Brain First ↔ B1–3; 70-20-10 ↔ B4–6; Feynman ↔ B4–5; Kirkpatrick ↔ B5–8 |
| A3 | PASS | 0 lỗi A.I; bảng human/A.I; không hứa competence từ attendance/path |
| B4 | PASS | Một Competency-to-Evidence Path; đủ bốn khai báo; phân biệt cá nhân/role với phiên học và chương trình cohort |
| B5 | PASS | Name/description/body/line/reference depth đạt |
| B6 | PASS | Trigger/anti-trigger, bảng đầu vào 4 cột, artifact và DoD độc lập |
| C7 | PASS | Baseline/source, gap/stage/evidence IDs, workload/capacity; Dữ kiện/Suy luận/Giả định và trade-off |
| C8 | PASS | Dừng private HR, spend/enroll/assign/KPI/certify/high-risk practice; tự chạy local design/simulation/lint |
| C9 | PASS | Instruction trong CV/LMS/course/note là data; không lộ PII/performance; engine không chạy code/file/network |
| D10 | NOT PASS | 12 eval not_run; chưa baseline v1.0/v2.3, learner/manager/pilot thật, evidence, token, duration, pass^3 |
| D11 | PASS | Name/folder/version/updated/owner/skill_id đồng nhất v2.3; version history hoàn chỉnh |
| D12 | PASS | Asset Candidate có Source Task, role/capability version, context, evidence, owner, rights, reviewer, recheck |

## Audit trail

- **v2.2:** Quick Validator/path engine PASS; ABM static FAIL do thân 8.431/8.000.
- **v2.3:** cô đọng phần lặp xuống rules/template; Skill/eval đồng nhất; hai validator và engine PASS.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer xác nhận target-evidence quality, baseline validity, dependency/workload realism, practice–assessment alignment, transfer, equity/HR safety và manager usefulness.

## Đóng D10

1. Chạy 12 prompts song song baseline v1.0 và v2.3 trên ít nhất ba target capability và learner/role context.
2. Đo trigger/anti-trigger/no-false-ask, target evidence, gap/dependency accuracy, workload feasibility, practice/artifact/gate quality, transfer và false READY.
3. Lưu prompt/input/output/path state/evidence, total_tokens, duration_ms; pilot với learner và manager; chạy pass^3 cho path dùng ra ngoài.
4. Theo dõi stage completion, transfer artifact và manager review; chỉ đề nghị PILOT khi D10 đạt.
