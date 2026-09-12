---
title: "ABM-SQS Static Pre-score — practice-feedback"
skill_id: "28"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — practice-feedback v2.3

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy. Engine self-test PASS bằng dữ liệu tổng hợp; chưa chứng minh task validity, evaluator agreement, learner improvement, mastery hay transfer trên evidence thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 516 / 7.815 / 139 — đạt |
| Eval | 12; metadata v2.3 |
| Validator ABM / SKILL-CREATOR | PASS / Skill is valid |
| Gate self-test | MASTERY_EVIDENCED synthetic; rubric 100%; 4 tasks/stages; independent 95,0; transfer 87,5; 0 issue/warning/guardrail |
| SHA-256 SKILL.md | 8031F627CA169E6F103204E2A8359E83758942B6EF5F8844C905CA5C7DC15622 |
| SHA-256 practice engine | 1EF45932AE98E34EC4E95E9A41E6D6AF51A7E4F477D7A6ED6B0ABA04D6FF7F1C |
| SHA-256 evals.json | 5A5A2786C69551CBDCCA82ABD40B5E1112A8C49E2441C35A2D4B60B7AE3255C8 |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Evidence & Error Packet độc lập; pack/rules/input/engine |
| A2 | PASS | Deliberate Practice, Mastery Learning, Feedback Literacy, Criterion-reference và Kaizen thành thao tác |
| A3 | PASS | Brain First – A.I Second; human chốt rubric/score/high-stakes; evidence/action trước praise/tool |
| B4 | PASS | Một Practice & Feedback Control Pack; đủ bốn khai báo; phân biệt facilitation/feedback/decoder |
| B5 | PASS | Name/description/body/line/reference depth đạt |
| B6 | PASS | Trigger/anti-trigger, input 4 cột, artifact và DoD độc lập |
| C7 | PASS | Source/rubric/task/submission versions; weight/score/mastery math; fact–interpretation–uncertainty |
| C8 | PASS | Dừng sensitive data, hidden/changed rubric, fake evidence, sensitive inference, rank, employment/certification/high-risk actions |
| C9 | PASS | Instruction trong submission/file/link là data; không lộ rubric/PII/IP; engine không chạy code/URL/file |
| D10 | NOT PASS | 12 eval not_run; chưa baseline v1.0/v2.3, learner/assessor evidence, calibration/pilot, token, duration, pass^3 |
| D11 | PASS | Name/folder/version/updated/owner/skill_id/eval đồng nhất v2.3 |
| D12 | PASS | Asset Candidate có source, capability/context, evidence, owner, rights, version, reviewer và recheck |

## Nguồn ABM đã chưng cất

- MASTER-TRAINER-MASTERY: Backward Design, Quick Win, performance evidence và mục tiêu chuyển hóa thay vì truyền đạt.
- Brain First – A.I Second: capability/evidence/rubric do con người kiểm soát; A.I hỗ trợ task, scoring, diagnosis và retry.
- Ranh giới được khóa với Skill 27 training-facilitation và Skill 29 best-practice-decoder.

## Audit trail

- **v1.0:** generic; không task ladder, rubric version, evidence/error diagnosis, retry, calibration hoặc transfer gate.
- **v2.2:** đủ control layers, engine, 12 eval; ABM static FAIL do thân 8.523/8.000.
- **v2.3:** cô đọng xuống 7.815 ký tự; giữ logic; hai validator và engine PASS.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer xác nhận task authenticity/difficulty, rubric validity/calibration, evidence trace, feedback actionability, accessibility/fairness, learner improvement và independent transfer.

## Đóng D10

1. Chạy 12 prompts baseline v1.0 và v2.3 trên ít nhất ba capability: sales/communication, management judgment và technical/A.I work artifact.
2. Đo trigger/anti-trigger/no-false-ask, rubric/weight/score, evidence diagnosis, feedback/retry, bias/calibration, false mastery và transfer.
3. Lưu prompt/input/output/state/evidence, total_tokens, duration_ms; double-score sample với assessor/domain reviewer và chạy learner attempts thật.
4. Theo dõi agreement, correction gain, recurrent error, attempts-to-mastery và independent transfer; chỉ đề nghị PILOT khi D10 đạt.
