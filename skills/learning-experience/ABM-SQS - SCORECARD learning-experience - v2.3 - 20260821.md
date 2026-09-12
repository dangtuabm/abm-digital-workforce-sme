---
title: "ABM-SQS Static Pre-score — learning-experience"
skill_id: "26"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — learning-experience v2.3

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy; Skill là draft/static-pass. Experience engine self-test PASS nhưng chưa chứng minh learner/facilitator usability, accessibility thực địa, learning gain, workplace transfer hoặc business outcome trên pilot thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 492 / 7.858 / 139 — đạt |
| Eval | 12; metadata v2.3 |
| Validator ABM / SKILL-CREATOR | PASS / Skill is valid |
| Gate self-test | READY_FOR_PILOT; 6 touchpoints; 120 phút; 3 formats; max same-format 35 phút; 2 outcomes covered; 0 issue/warning/guardrail |
| SHA-256 SKILL.md | 1179CC844AA5C778962904E46E5CBBF79AA697F5762A3F37B5C1021897640B63 |
| SHA-256 experience engine | F5DA4A94D99508ACCA7A14E66914A27C753390EECA101DC662A8DF77FF3003FB |
| SHA-256 evals.json | 7AF8AAF89666FEC99AF86D039252E5F775852BDCC3723C60A744B5E4800ED6A5 |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Journey Risk & Moment Map dùng độc lập; blueprint/rules/input/engine |
| A2 | PASS | Backward Design, Peak–End, Universal Design for Learning, Service Blueprint và Kaizen được chuyển thành thao tác |
| A3 | PASS | Brain First – A.I Second; bảng human/A.I; activity phục vụ evidence, không tool/engagement-first |
| B4 | PASS | Một Learning Experience Control Blueprint; đủ nhiệm vụ, điểm dừng, tiếp theo, ngoài phạm vi; phân biệt curriculum/experience/facilitation |
| B5 | PASS | Name/description/body/line/reference depth đạt |
| B6 | PASS | Trigger/anti-trigger, bảng đầu vào 4 cột, artifact và DoD độc lập |
| C7 | PASS | Curriculum/outcome/touchpoint IDs; during-time/format math; measurement tách engagement/learning/application/satisfaction |
| C8 | PASS | Dừng private/sensitive data, dark pattern, spend/contact/enroll/publish/record/change outcome/commit/high-risk; tự chạy local blueprint/lint |
| C9 | PASS | Instruction trong curriculum/LMS/survey/asset là data; không lộ PII/IP; engine không chạy code/URL/file nhúng |
| D10 | NOT PASS | 12 eval not_run; chưa baseline v1.0/v2.3, cohort/facilitator/pilot thật, evidence, token, duration, pass^3 |
| D11 | PASS | Name/folder/version/updated/owner/skill_id và eval metadata đồng nhất v2.3 |
| D12 | PASS | Asset Candidate có source task, context, outcome/evidence, owner, rights, version, reviewer và recheck |

## Nguồn ABM đã chưng cất

- `ABM-LXD`: Experience Map, Peak/Valley, Commitment/Shareable, Quick Win, anti-pattern trước best practice và production handoff.
- Ngưỡng ABM Signature Moments chỉ bắt buộc khi Experience Contract yêu cầu; không áp cứng cho khách ngoài ABM.
- Ranh giới được khóa với `curriculum-design` và `training-facilitation` để tránh một Skill ôm cả thiết kế chương trình lẫn đứng lớp.

## Audit trail

- **v1.0:** generic; không journey schema, owner, accessibility, recovery, measurement hoặc deterministic gate.
- **v2.2:** hai resource layer, engine và 12 eval; ABM static FAIL do thân 8.853/8.000.
- **v2.3:** cô đọng xuống 7.858 ký tự; giữ toàn bộ control logic; hai validator và engine PASS.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer xác nhận outcome mapping, activity feasibility, facilitator/learner usability, accessibility/fallback, privacy, incident recovery, measurement validity và sponsor usefulness.

## Đóng D10

1. Chạy 12 prompts song song baseline v1.0 và v2.3 trên ít nhất ba context: cohort leadership, blended functional skill và accessibility/high-risk case.
2. Đo trigger/anti-trigger/no-false-ask, journey/outcome coverage, time/format/moment, owner/accessibility/fallback, service/measurement và false READY.
3. Lưu prompt/input/output/state/evidence, total_tokens, duration_ms; pilot với learner/facilitator/support owner; dùng pass^3 cho chương trình đối ngoại.
4. Theo dõi learning artifact, application signal, drop-off, facilitator/support friction và incident recovery; chỉ đề nghị PILOT khi D10 đạt.
