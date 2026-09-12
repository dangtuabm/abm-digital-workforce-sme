---
title: "ABM-SQS Static Pre-score — priority-allocation"
skill_id: "18"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `priority-allocation` v2.3

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa có baseline execution; Skill là `draft / static-pass`. Deterministic allocation engine self-test PASS nhưng chưa chứng minh hiệu quả trên portfolio thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 549 / 7.790 / 140 — đạt ngưỡng |
| Eval | 12 |
| Validator ABM / SKILL-CREATOR | PASS / `Skill is valid!` |
| Engine self-test | PASS; selected A+B+D; C deferred; budget 65/70; hours 600/600; value 100 |
| SHA-256 `SKILL.md` | `D0FA1C5F3A01475620FA3EFBC1B30411DA3033E98393A17BD7E6B112A5D5743C` |
| SHA-256 engine | `2FD974B79101C1F5BDA404104892576DA037F6B31769487189ACB9254DEBEDC5` |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Capacity–Demand Register; 2 rules, JSON input, pack template, allocation engine |
| A2 | PASS | Brain First ↔ B1–2; Constraints ↔ B3–6; Portfolio ↔ B4–7; Audit/Kaizen ↔ B5–8 |
| A3 | PASS | 0 lỗi "A.I"; human/A.I table; không emoji/sáo ngữ |
| B4 | PASS | Một Allocation Pack; đủ bốn khai báo; tách allocation khỏi comparison/scenario/execution |
| B5 | PASS | Name hợp lệ; description/body/line đạt; references một tầng |
| B6 | PASS | Trigger/anti-trigger, input 4 cột, DoD đo feasibility/capacity/constraints/opportunity cost |
| C7 | PASS | `ALLOC/ITEM-ID`, value source, resource/unit, effort, capacity, dependency, state/version |
| C8 | PASS | Dừng trước access/manipulation/overbook/commit/HR/spend; tự chạy local register/engine |
| C9 | PASS | Item instructions là data; ID/pointer/redaction; engine không execute item code |
| D10 | NOT PASS | 12 eval `not_run`; chưa baseline/evidence/token/duration/pass^3 |
| D11 | PASS | Metadata/version/name đủ và đúng folder |
| D12 | PASS | Asset Candidate có Source Task, allocation/version, outcome evidence, owner, approval/review |

## Audit trail phiên bản

- **v2.2:** engine/Quick Validator PASS; static fail: description 612/600, body 8.371/8.000.
- **v2.3:** cô đọng; hai validator + engine self-test PASS.

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer duyệt capacity reconciliation, mandatory/dependency integrity, optimization correctness, opportunity-cost visibility, manipulation resistance và operational usefulness.

## Điều kiện đóng D10

1. Chạy 12 prompts baseline v1.0/v2.3 trên project, budget, team-hours và mixed-resource portfolios.
2. Đo trigger/false ask, sourced-value/effort coverage, mandatory/dependency breach, capacity/buffer error, infeasibility detection, optimality on known cases, displaced-work visibility và reviewer usefulness.
3. Lưu inputs/expected allocations/outputs, evidence, `total_tokens`, `duration_ms`; pass^3 và engine regression.
4. Sửa systematic errors trước đề nghị OFFICIAL.
