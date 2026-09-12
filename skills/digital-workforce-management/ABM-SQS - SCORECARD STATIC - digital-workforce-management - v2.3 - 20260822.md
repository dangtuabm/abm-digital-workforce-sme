---
document_code: "ABM-SQS-SC-93"
skill: "digital-workforce-management"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — DIGITAL WORKFORCE MANAGEMENT v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh cho Agent Registry, admission/lifecycle gates, operations/SLO/capacity/cost, access recertification, change/version, portfolio duplicate–overlap–gap/value review và controlled offboarding. Skill chỉ đề xuất BUILD/MERGE/LIMIT/SUSPEND/REMEDIATE/RETIRE; không tự tác động production/quyền/dữ liệu. D10 chưa đạt vì chưa pilot trên portfolio, telemetry, identities, connectors, dependencies, incidents và value thật.

Chuỗi: `SKILL-CREATOR → AGENT-ORCHESTRATION → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 `designed_not_run` |
| SKILL-CREATOR quick_validate | PASS |
| Description | 575 ký tự, ≤ 600 |
| Body | 7.999 ký tự, ≤ 8.000 |
| Lines | 108, ≤ 500 |
| Evals | 12; trigger, routing, no_false_ask, ambiguity, missing, red_line, injection, adversarial, operations, change control |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive:** `READY_FOR_HUMAN_DIGITAL_WORKFORCE_DECISION`; 0 defect; 0 review gap. Coverage: 10 Agents, 10 admission gates, 10 lifecycle, 10 operating, 8 access, 8 change, 8 portfolio findings, 6 offboarding plans, 6 decisions, 10 test cases, 6 risks, 7/7 tests và 6/6 reviews.

**Negative:** `NOT_READY`; 224 defects; 6 review gaps. Chặn quantity vanity, human impersonation, ownerless Agent, privilege escalation, auto-activation, ignored critical gate, output-as-value, hidden failure/cost, silent change, reused approval, auto merge/suspend/retire, permission/production change, send/publish, evidence deletion, injection và secret.

## 4. Final Gatekeeper

- PASS scope: portfolio/lifecycle management khác Agent contract, orchestration runtime và governance framework.
- PASS identity/ownership: immutable ID, non-impersonation, business/technical/risk owners.
- PASS admission/lifecycle: critical evidence trước PILOT/ACTIVE; transition có approver, expiry, dependencies, manual coverage và rollback.
- PASS operations: quality/SLO/queue/WIP/capacity/incidents/cost/drift/value tách rõ; breach không bị average che.
- PASS access/change: least privilege, recertification, compatibility/tests/version/rollback; không silent change.
- PASS offboarding: drain, revoke, reconcile, transfer, archive/retention, update routes/dependencies và recovery test.

## 5. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `C48DC444D77D5511014C21133C87647EB84A17D9D923CE4D5B7F09D114B9ED2B` |
| evaluator | `FEAD9FBC24354A7B8C37F5E05AAE446F71A4F0999F7B79D6B9E7236B7EF88034` |
| evals | `B9AE03B2E4DD6334E6CF084A89AE8FBFF39E7EEDCE0D9DCC2735932FA6068403` |
| positive fixture | `1F2A5A75D9A6FFD418CD64C72ADF3B074547901A7784B7E771276CEB24150C2A` |
| negative fixture | `1ABECD22511AD15620714DB557BE6885DDA5B8647D16A4131CD10665AA6879D7` |
| rules | `6F7277855BAAF06355204E7C213116923143E94203EFD92FD173600FD3BE5009` |
| template | `66D0BD03786ADFFE5A88CAC39DA23643694EE66DE6C77804F9C50FA8DC3F04F6` |

## 6. Cổng còn thiếu

D10 cần pilot trên registry SoR, Agents/owners/rights, lifecycle transitions, SLO/capacity/cost/incidents, access/change review, portfolio findings và offboarding thật; đo false trigger, token, duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.

