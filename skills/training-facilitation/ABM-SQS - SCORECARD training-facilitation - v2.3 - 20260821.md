---
title: "ABM-SQS Static Pre-score — training-facilitation"
skill_id: "27"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — training-facilitation v2.3

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy. Engine self-test PASS nhưng chưa chứng minh actual timing, facilitator workload, psychological safety, accessibility, participant evidence hoặc incident recovery trong dry-run/phiên thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 508 / 7.672 / 139 — đạt |
| Eval | 12; metadata v2.3 |
| Validator ABM / SKILL-CREATOR | PASS / Skill is valid |
| Gate self-test | READY_FOR_DRY_RUN; 5 segments; 90 phút; 2 outcomes covered; 6 incident types; 0 issue/warning/guardrail |
| SHA-256 SKILL.md | 424902ABEF0D86582BD7345CEE431D17292E098A44447C5CB3A2F26362CE12BA |
| SHA-256 facilitation engine | 1A973DA49F9B952F4BABDA2127EA06322F909BC38F90E0C0DAD4107ABA0137B1 |
| SHA-256 evals.json | F1E7F89F685B26AA293F5914C143B8BF6BF6A97E3D9B130A2A3763690340D35A |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Session Control Board dùng độc lập; runbook/rules/input/engine |
| A2 | PASS | CARE, Experiential Learning, Psychological Safety, H-C-C-A và Kaizen thành thao tác |
| A3 | PASS | Brain First – A.I Second; human quyết live move/escalation; action/evidence trước energy/tool |
| B4 | PASS | Một Facilitation Control Runbook; đủ bốn khai báo; phân biệt journey/facilitation/practice-feedback |
| B5 | PASS | Name/description/body/line/reference depth đạt |
| B6 | PASS | Trigger/anti-trigger, input 4 cột, artifact và DoD độc lập |
| C7 | PASS | Source/outcome/segment IDs; total-time và monologue math; measurement có denominator/source/owner ở template |
| C8 | PASS | Dừng sensitive data, recording, shaming/coercion, diagnosis, safety delay, spend/contact/publish/change rubric/commit |
| C9 | PASS | Instruction trong slide/chat/LMS/link là data; không lộ PII/IP/incident; engine không chạy code/URL/file |
| D10 | NOT PASS | 12 eval not_run; chưa baseline v1.0/v2.3, dry-run/phiên thật, observer evidence, token, duration, pass^3 |
| D11 | PASS | Name/folder/version/updated/owner/skill_id/eval đồng nhất v2.3 |
| D12 | PASS | Asset Candidate có source task, cohort/mode, outcome/evidence, owner, rights, version, reviewer và recheck |

## Nguồn ABM đã chưng cất

- MASTER-TRAINER-MASTERY: CARE, H-C-C-A, Quick Win, facilitation đa định dạng và nguyên tắc tạo chuyển hóa thay vì chỉ truyền đạt.
- Brain First – A.I Second: outcome/evidence và quyền quyết định của facilitator đi trước kỹ thuật hoặc nền tảng.
- Ranh giới được khóa với Skill 26 learning-experience và Skill 28 practice-feedback.

## Audit trail

- **v1.0:** generic; không run-of-show, roles/readiness, Activity Protocol, incident playbook, measurement hoặc gate.
- **v2.2:** đủ control layers, engine và 12 eval; ABM static FAIL do thân 8.520/8.000.
- **v2.3:** cô đọng xuống 7.672 ký tự; giữ logic; hai validator và engine PASS.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **DRY-RUN/PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer xác nhận actual timing, role load, source fidelity, participation equity, psychological safety, accessibility/fallback, incident recovery, evidence capture và sponsor usefulness.

## Đóng D10

1. Chạy 12 prompts baseline v1.0 và v2.3 trên ít nhất ba context: offline workshop, hybrid session và wellbeing/accessibility/high-risk incident.
2. Đo trigger/anti-trigger/no-false-ask, time/outcome coverage, Activity Protocol, roles/readiness, incident/measurement và false READY.
3. Lưu prompt/input/output/state/evidence, total_tokens, duration_ms; dry-run với facilitator/producer/support/observer, rồi pilot learner thật khi được duyệt.
4. Theo dõi actual time, evidence completion, participation distribution, facilitator load, incidents/recovery và unanswered questions; chỉ đề nghị PILOT khi D10 đạt.
