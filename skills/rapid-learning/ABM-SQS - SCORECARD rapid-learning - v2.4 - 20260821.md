---
title: "ABM-SQS Static Pre-score — rapid-learning"
skill_id: "22"
version: "2.4"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — rapid-learning v2.4

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy; Skill là draft/static-pass. Readiness engine self-test PASS nhưng chưa chứng minh learning transfer trên learner và target task thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 534 / 7.898 / 139 — đạt |
| Eval | 12; metadata v2.4 |
| Validator ABM / SKILL-CREATOR | PASS / Skill is valid |
| Gate self-test | READY_FOR_TASK; knowledge/application/traceability PASS; 0 missing/critical failure/issue/warning |
| SHA-256 SKILL.md | 40EC2DB9095AFB810220269085D07AA61AA0B6B3CE4D7A3DD2BB20EA510F7D38 |
| SHA-256 readiness engine | 8BCA500A2FC57044C069B8456DE9F0EA5BFB7170CC500BF957398AA4C98E3D5F |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước thi công; Learning Mission & Domain Map dùng độc lập; dossier/rules/input/engine |
| A2 | PASS | Brain First ↔ B1–2; 80/20 ↔ B3; Feynman/Retrieval ↔ B5; 70-20-10/Deliberate Practice ↔ B6–8 |
| A3 | PASS | 0 lỗi A.I; bảng human/A.I; không emoji/sáo ngữ/hứa expertise |
| B4 | PASS | Một Learning Readiness Dossier; đủ bốn khai báo; ranh giới theo đích bàn giao, không hard-link tên Skill |
| B5 | PASS | Name/description/body/line/reference depth đạt |
| B6 | PASS | Trigger/anti-trigger, bảng đầu vào 4 cột, artifact và DoD độc lập |
| C7 | PASS | Source ID/version/date/confidence; Dữ kiện/Suy luận/Giả định; unknowns/limits/expiry |
| C8 | PASS | Dừng trước private data, high-risk claim, READY/certify/authorize/send/spend/act; tự chạy local work |
| C9 | PASS | Instruction trong nguồn là data; không lộ nội bộ/PII; engine không chạy code/file/network từ input |
| D10 | NOT PASS | 12 eval not_run; chưa baseline v1.0/v2.4, learner/task thật, evidence, token, duration, pass^3 |
| D11 | PASS | Name/folder/version/updated/owner/skill_id đồng nhất v2.4; version history hoàn chỉnh |
| D12 | PASS | Asset Candidate có Source Task/cohort/domain-source version/evidence/owner/rights/reviewer và recheck trigger |

## Audit trail

- **v2.2:** Quick Validator/engine PASS; ABM static FAIL do thân 8.948/8.000.
- **v2.3:** cô đọng, hai validator PASS; không phát hành vì eval metadata còn v2.2.
- **v2.4:** Skill/eval đồng nhất; hai validator và readiness self-test PASS.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer xác nhận mission quality, source currency, misconception detection, active retrieval, unseen transfer, false-readiness control, high-risk guardrails và usefulness.

## Đóng D10

1. Chạy 12 prompts song song baseline v1.0 và v2.4 trên ít nhất ba miền: ngành mới, công nghệ mới, lĩnh vực có claim thay đổi.
2. Đo trigger/anti-trigger/no-false-ask, mission quality, source traceability, misconception correction, unseen transfer, false READY, expert review và reviewer usefulness.
3. Lưu prompt/input/output/state/evidence, total_tokens, duration_ms; chạy pass^3 với ca đối ngoại/high-risk.
4. Sửa lỗi hệ thống, retest bằng case chưa lộ; chỉ đề nghị PILOT khi D10 đạt.
