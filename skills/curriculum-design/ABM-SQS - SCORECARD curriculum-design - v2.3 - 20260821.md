---
title: "ABM-SQS Static Pre-score — curriculum-design"
skill_id: "25"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — curriculum-design v2.3

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy; Skill là draft/static-pass. Curriculum engine self-test PASS nhưng chưa chứng minh cohort performance, workplace transfer, facilitator usability hoặc business outcome trên pilot thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 557 / 7.984 / 139 — đạt |
| Eval | 12; metadata v2.3 |
| Validator ABM / SKILL-CREATOR | PASS / Skill is valid |
| Gate self-test | READY_FOR_PILOT; 2 modules; 480 phút; practice ratio 0,75; 0 coverage gap/guardrail/issue/warning |
| SHA-256 SKILL.md | F710A27289163C5EDA3DEFE15172D84DACC4A3B4E6C59A89BC42A00CCD8CE9B1 |
| SHA-256 curriculum engine | D946ED1FF1E1F14D4F9CDBCEC074904AE5A42FF670288221F07FB29350B82DE6 |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Capability–Outcome–Evidence Map dùng độc lập; architecture/rules/input/engine |
| A2 | PASS | Brain First ↔ B1–3; 70-20-10 ↔ B4–6; Kirkpatrick ↔ B3/6–8; Làm 1 dùng N ↔ B2/5/8 |
| A3 | PASS | 0 lỗi A.I; bảng human/A.I; Quick Win và work evidence, không tool-first/hứa ROI |
| B4 | PASS | Một Curriculum Evidence Architecture; đủ bốn khai báo; phân biệt cohort curriculum với path/experience/delivery |
| B5 | PASS | Name/description/body/line/reference depth đạt |
| B6 | PASS | Trigger/anti-trigger, bảng đầu vào 4 cột, artifact và DoD độc lập |
| C7 | PASS | Reference/source version, capability/evidence/module IDs, time/practice math; Dữ kiện/Suy luận/Giả định và attribution limits |
| C8 | PASS | Dừng private/IP, copy/stale claim, spend/enroll/publish/certify/ROI/high-risk practice; tự chạy local architecture/lint |
| C9 | PASS | Instruction trong giáo án/survey/LMS/case là data; không lộ PII/IP; engine không chạy code/file/network |
| D10 | NOT PASS | 12 eval not_run; chưa baseline v1.0/v2.3, cohort/facilitator/pilot thật, evidence, token, duration, pass^3 |
| D11 | PASS | Name/folder/version/updated/owner/skill_id đồng nhất v2.3; version history hoàn chỉnh |
| D12 | PASS | Asset Candidate có Source Task, program/cohort/source version, evidence, owner, rights, reviewer và recheck |

## Nguồn ABM đã chưng cất

- File 31: reference trace 2–3 chương trình, retain/adapt/reject, không sao chép nội dung cũ.
- Kiến trúc trải nghiệm: outcome đo được, Experience Blueprint, production specs và pilot.
- DNA BGĐT: Hook–Core–Case–Action, anti-pattern trước best practice, Quick Win và assessment tình huống.
- Inhouse: baseline/gap, industry context, practice ratio theo contract, pre-work, transfer/follow-up.

## Audit trail

- **v2.2:** Quick Validator/curriculum engine PASS; ABM static FAIL do thân 8.808/8.000.
- **v2.3:** cô đọng phần lặp xuống rules/template; Skill/eval đồng nhất; hai validator và engine PASS.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer xác nhận reference/IP integrity, capability–assessment alignment, module/time/practice feasibility, facilitator/learner usability, accessibility, transfer và sponsor usefulness.

## Đóng D10

1. Chạy 12 prompts song song baseline v1.0 và v2.3 trên ít nhất ba curriculum: leadership, functional skill và regulated/high-risk.
2. Đo trigger/anti-trigger/no-false-ask, reference trace, coverage/dependency/time/practice, artifact–assessment alignment, materials, transfer và false READY.
3. Lưu prompt/input/output/state/evidence, total_tokens, duration_ms; pilot với cohort/facilitator/manager; pass^3 cho curriculum đối ngoại.
4. Theo dõi learner artifact, transfer behavior, facilitator friction và outcome limits; chỉ đề nghị PILOT khi D10 đạt.
