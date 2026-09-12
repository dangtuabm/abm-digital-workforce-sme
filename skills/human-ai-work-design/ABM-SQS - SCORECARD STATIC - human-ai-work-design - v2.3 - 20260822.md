---
document_code: "ABM-SQS-SC-92"
skill: "human-ai-work-design"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — HUMAN–A.I WORK DESIGN v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh để phân rã task/decision, gán bảy disposition, khóa human authority/SoD, autonomy envelope, exception–recovery, workload/capability change và test/UAT. Skill dừng trước production permission, staffing, policy và rollout. D10 chưa đạt vì chưa pilot trên use case, workflow, roles, authority, systems, data và workload thật.

Chuỗi: `SKILL-CREATOR → AGENT-ORCHESTRATION → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 `designed_not_run` |
| SKILL-CREATOR quick_validate | PASS — `Skill is valid!` |
| Description | 596 ký tự, ≤ 600 |
| Body | 7.977 ký tự, ≤ 8.000 |
| Lines | 109, ≤ 500 |
| Evals | 12; trigger, must_not_trigger, no_false_ask, ambiguity, missing, red_line, injection, adversarial, failure, change/capability |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive:** `READY_FOR_HUMAN_WORK_DESIGN_DECISION`; 0 defect; 0 review gap. Coverage: 12 evidence, 10 work units, 10 allocations, đủ 7 dispositions, 8 autonomy contracts, 8 exception routes, 8 capability changes, 6 decisions, 10 test cases, 6 risks, 7/7 tests và 6/6 reviews.

**Negative:** `NOT_READY`; 199 defects; 6 review gaps. Chặn whole-job automation, surveillance, sensitive inference/proxy/discrimination, high-impact auto decision, A.I accountable/self-review, bypass approval, production permission, policy/staffing/termination/deployment/send/publish, evidence mutation, injection và secret.

## 4. Final Gatekeeper

- PASS task-level boundary; `ELIMINATE` loại waste/task, không loại người.
- PASS seven dispositions và high-impact/external-effect human authority.
- PASS maker/checker, SoD và independent review.
- PASS autonomy envelope: data/system/action/threshold/abstain/rate/time/expiry/log/retry/fallback/escalation/kill/rollback/reconciliation.
- PASS people impact: workload, cognitive load, exception burden, deskilling, training, accessibility/fairness và feedback.
- PASS handoff: chỉ là design proposal; production, staffing, policy và rollout vẫn PENDING human authority.

## 5. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `DA0DFD38AB7718AB4F04AA9CBB02B4B4F23965FF8E2712E77C57601F8BEAD207` |
| evaluator | `444F07F20A23C7D0FC9B0ED9E652A96C72ADBAB074FD8002BF2C763771D211B9` |
| evals | `BE82D1D82EF76A1EB35DFB9920E5C3F51775661918F7FA6BE4CB6ACFD815653A` |
| positive fixture | `CCF12399ACDC4B0E4E247C17C5D241F7F0FAF4DC56ABD075377C6A881877F7A7` |
| negative fixture | `095617F6DBEF201FBDCBBFEAE18D5EF818178840060E0CEEC4CF2153828D309E` |
| rules | `233C3F9EF19B92C0DF7A034993FBF5E518108D5C406A3D1481E66034B160C753` |
| template | `E44132B452D3654C694E81EAE919F9D6E8B07E7EC1182EC27AE57C8A11C935FA` |

## 6. Cổng còn thiếu

D10 cần pilot trên selected use case, current-work evidence, roles/decision rights, data/system permission, task allocation, autonomy/failure controls, workload/capability changes và UAT thật; đo false trigger, token, duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.

