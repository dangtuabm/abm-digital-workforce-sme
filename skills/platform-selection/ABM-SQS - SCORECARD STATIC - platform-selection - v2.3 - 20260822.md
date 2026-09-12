---
document_code: "ABM-SQS-SC-94"
skill: "platform-selection"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — PLATFORM SELECTION v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh cho requirements trace, dated official/contract evidence, critical gates, fit-gap-risk, anchored scoring, lifecycle TCO, representative pilot, sensitivity và portability/exit. Skill dừng trước procurement, sign, provision, upload, architecture commitment và migration. D10 chưa đạt vì chưa pilot workload, vendor plan/region, contract, security, price, integration và exit thật.

Chuỗi: `SKILL-CREATOR → PLATFORM-SELECTION → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 `designed_not_run` |
| SKILL-CREATOR quick_validate | PASS |
| Description | 576 ký tự, ≤ 600 |
| Body | 7.962 ký tự, ≤ 8.000 |
| Lines | 110, ≤ 500 |
| Evals | 12; trigger/routing/no_false_ask/ambiguity/missing/red_line/injection/adversarial/pilot/exit-lock-in |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive:** `READY_FOR_HUMAN_PLATFORM_DECISION`; 0 defect; 0 review gap. Coverage: 12 sources, 10 requirements, 5 options/gates/assessments/TCO/exit plans, 10 pilot tests, 3 sensitivity scenarios, 6 decisions, 10 test cases, 6 risks, 7/7 tests và 6/6 reviews.

**Negative:** `NOT_READY`; 209 defects; 6 review gaps. Chặn hardcoded vendor score, universal industry rule, invented feature/price/certification/residency/legal fit, UNKNOWN thành 0, gate washing, invented migration loss, affiliate bias, auto select/purchase/sign/provision/upload/demo/architecture/migrate/send/publish, evidence mutation, injection và secret.

## 4. Final Gatekeeper

- PASS requirements-first; không bắt đầu từ brand/vendor list.
- PASS current evidence: plan/region/version/date/scope; marketing không ghi đè contract/DPA/terms/admin evidence.
- PASS critical gates: task/output, data/security, identity/audit, legal/contract, integration/continuity, exit/deletion.
- PASS scoring/TCO: criteria và weights human-approved; fit/risk/TCO/effort tách rõ; không hardcode ABM/vendor preference.
- PASS pilot: representative workload, quality/latency/reliability/cost/security/integration/UAT/failure/exit.
- PASS exit: portability, export/deletion, revoke, replacement, migration/rollback/manual coverage.

## 5. Nguồn specialist được sửa cứng

Không đưa các điểm vendor cố định, quy tắc “ngành nhạy cảm bắt buộc Local LLM” hoặc con số thất thoát chuyển đổi 30–40% từ specialist vào bản enterprise vì thiếu evidence/scope pháp lý. Bản mới yêu cầu current official/contract sources và qualified legal/security owner theo từng case.

## 6. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `AF0563B6F46DFF56854C3017F4E55D4285D6020DA4F379F45B56003F4E79655C` |
| evaluator | `5B79FDA758F731E9280F4FC90ED3863F609013B5B859821E57F8B463B5DFA582` |
| evals | `356B64890370D9E02E1899109DDD427F906826663F06E94EDC00191EDBE75E64` |
| positive fixture | `7ABC1873D7DC9F942C4F265D0AA82896ACD0EBE2452F5EE5F863F714D7049F0C` |
| negative fixture | `7203ED36251CAA22FDBFD8D15FEB485C3F91DD852582B881A0DC8C3678DA7BFC` |
| rules | `9F193D738F50490C3B4253FC6758A4B717309AD2B52E2ACDD942D1F5DD11EB83` |
| template | `5B0B6AB7F16252862997ED85F003A1D7C2F5ABCB982C34FD9EC682D87B6BA8AA` |

## 7. Cổng còn thiếu

D10 cần pilot trên decision/use cases/workloads, current official/contract evidence, critical gates, scoring/TCO inputs, representative tests và exit/migration thật; đo false trigger, token, duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.

