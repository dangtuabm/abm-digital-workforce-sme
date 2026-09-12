---
document_code: "ABM-SQS-SC-96"
skill: "agent-contract"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — AGENT CONTRACT v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh để tạo Agent Contract có identity/task, I-O/DoD, authority/access, state/idempotency, failure/SLO, Human Control/SoD, audit/evidence, conformance và lifecycle/offboarding. Skill tách capability khỏi permission và dừng trước grant, activation, deploy hoặc external action. D10 chưa đạt vì chưa admission/pilot một Agent thật.

Chuỗi: `SKILL-CREATOR → AGENT-ORCHESTRATION → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 `designed_not_run` |
| SKILL-CREATOR quick_validate | PASS |
| Description | 526 ký tự, ≤ 600 |
| Body | 7.796 ký tự, ≤ 8.000 |
| Lines | 108, ≤ 500 |
| Evals | 12; trigger/routing/no_false_ask/ambiguity/missing/red_line/injection/permission/failure/audit/lifecycle |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive:** `READY_FOR_HUMAN_AGENT_CONTRACT_DECISION`; 0 defect; 0 review gap. Coverage: 12 evidence sources, 10 requirements, 12 I-O fields, 10 authority rules, 10 access rules, 8 transitions, 8 failure controls, 8 service controls, 12 test cases, 6 decisions, 6 risks, 7/7 tests và 6/6 reviews.

**Negative:** `NOT_READY`; 117 defects; 6 review gaps. Chặn prompt-only contract, capability=permission, UNKNOWN→ALLOW, invented grant/evidence, embedded/shared secret, unbounded retry, silent fail, Executor tự làm Kaizen, tự duyệt exception, scope creep, account/token/grant/activate/deploy/action/write/delete/send/purchase/sign/publish, breaking change, offboard không revoke và injection.

## 4. Final Gatekeeper

- PASS contract identity, one-Task/one-Executor/independent-Kaizen và acceptance evidence.
- PASS input/output schema: SoR, rights, validation, conflict/quarantine, uncertainty, abstain, result link và retention.
- PASS authority/access: ALLOW/CONDITIONAL/DENY; tool capability không thành grant; least privilege, secret ref, expiry/revoke.
- PASS state/failure: legal transitions, idempotency, bounded retry, fallback, compensation, reconciliation, DLQ, escalation và recovery.
- PASS SLO/budget/capacity, Human Control/SoD, audit/redaction và six-owner review.
- PASS lifecycle: version, compatibility, migration, canary, rollback, suspend, drain, revoke và residual-access verification.

## 5. Nguồn specialist được sửa cứng

Giữ nguyên nguyên tắc `AGENT-ORCHESTRATION`: một Task–một Executor đầu-cuối, Kaizen độc lập, Human Control đúng điểm, retry/fallback/escalation/DLQ và không khóa model/platform. Bổ sung contract schema, capability-versus-permission semantics, I-O/SoR/rights, idempotency, SLO/budget, audit/redaction, conformance, compatibility và offboarding; không dùng “bảy trạng thái chuẩn” như universal state machine.

## 6. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `36AEC56FC981E1717739416192B2848CB470E2351FCBEB93419C11E0E754991C` |
| evaluator | `6AC3E1521369CB8FD26C86375030067D6F33F7DB920502BE44A430AD34A046A9` |
| evals | `18D3465973CCF74118FD059027E38246E15B9CA2815D5753595BA1325C26E65F` |
| positive fixture | `2EF47AF9546230FEEB22C9D7553B915753CC7DC5D4CB7965FBA33B79F994656F` |
| negative fixture | `869231E45B9C4149247D74A624D561AB3FD43891B7536445317BCCCF4E0C846E` |
| rules | `D079B170D7324863A85AA105FD53211EA4C067B38B208044DCA4A9DF0912C74A` |
| template | `2147195140F27543122D94C99F6C9B9376EA63B3D5FDB858C381252398C2DD34` |

## 7. Cổng còn thiếu

D10 cần pilot trên một Agent/Task thật với contract/grant enforcement, I-O/DoD, failures, SLO/budget, audit, human approval, version change và offboarding; đo false trigger, token và duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.

