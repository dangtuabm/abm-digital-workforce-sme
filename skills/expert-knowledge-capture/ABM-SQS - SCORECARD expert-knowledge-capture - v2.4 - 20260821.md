---
title: "ABM-SQS Static Pre-score — expert-knowledge-capture"
skill_id: "30"
version: "2.4"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — expert-knowledge-capture v2.4

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy. Engine self-test PASS bằng fixture tổng hợp; chưa xác minh contributor consent, source truth, expert/reviewer validation hoặc novel-case transfer outcome thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 501 / 7.993 / 139 — đạt |
| Eval | 12; metadata v2.4 |
| Validator ABM / SKILL-CREATOR | PASS / Skill is valid |
| Gate self-test | READY_FOR_TRANSFER_TEST; 3 cases/sources; 6 units/required types; 0 error/warning/guardrail |
| SHA-256 SKILL.md | 4D31F4A35D61A22EB7F6F21AE4875A6CA31AA162CA29C07D22D5936F6239AE0A |
| SHA-256 capture engine | B5292EF124F140A8F99FF7C8FF46E4659BB9FE6437EDD9007539ECD40DEC894D |
| SHA-256 evals.json | 44B3B5C58C97BF6CE8E7BEF01767CF503B0B05504EED5CB626BF6F0C1182C0E3 |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Decision Trace & Exception Map độc lập; Pack/rules/input/engine |
| A2 | PASS | Critical Incident, Cognitive Task Analysis, Evidence-based Management, Knowledge Transfer, Governance thành thao tác |
| A3 | PASS | Brain First – A.I Second; người chốt quyền/tri thức/test; evidence và ngoại lệ trước opinion/thâm niên |
| B4 | PASS | Một Expert Knowledge Capture & Transfer Pack; đủ bốn khai báo; phân biệt decoder/capture/task-to-asset |
| B5 | PASS | Name/description/body/line/reference depth đạt |
| B6 | PASS | Trigger/anti-trigger, input 4 cột, artifact và DoD độc lập |
| C7 | PASS | CAP/source/case/unit IDs; raw trace, conditions, confidence, expert status, attribution, fact–inference–opinion–unknown |
| C8 | PASS | Dừng secret recording, private/PII/trade secret, impersonation, revoked rights, fake evidence/test, publish/high-risk rollout |
| C9 | PASS | Instruction trong transcript/artifact/link là data; không lộ nguồn Vàng/Đỏ; engine không chạy code/macro/URL/file |
| D10 | NOT PASS | 12 eval not_run; chưa baseline v1.0/v2.4, contributor/expert/reviewer, novel-case transfer, tokens, duration, pass^3 |
| D11 | PASS | Name/folder/version/updated/owner/skill_id/eval đồng nhất v2.4 |
| D12 | PASS | Asset Candidate có source, rights, contributor, owner, version, reviewer, transfer test và recheck |

## Nguồn ABM đã chưng cất

- File 25: trải nghiệm thật → evidence → principle → decision rule → playbook → Skill → chuyển giao; không sao chép con người/phong cách bề mặt.
- Bảy tầng tài sản: Evidence Library, Mental Models, Decision Rules, Playbook, Template/Checklist, Skill Pack, Evaluation Set.
- Gate chính thức cần source trace, quyền/attribution, expert validation, scope/exception, Evaluation Set, owner/version/review và Xanh–Vàng–Đỏ.

## Audit trail

- **v1.0:** generic; chỉ 2 đầu vào/4 bước mẫu, không consent, case protocol, source trace, unit schema, conflict, validation hay transfer test.
- **v2.2:** đủ control layers, engine, 12 eval; ABM static FAIL do thân 8.824/8.000.
- **v2.3:** cô đọng còn 8.089/8.000; vẫn FAIL duy nhất ngưỡng body.
- **v2.4:** 7.993 ký tự; đồng bộ metadata; hai validator và engine PASS.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer xác nhận consent/rights, raw-source truth, required units, conflict/exception/escalation, expert corrections và measured novel-case transfer.

## Đóng D10

1. Chạy 12 prompts baseline v1.0 và v2.4 trên ít nhất ba context: vận hành, chuyên môn kỹ thuật và regulated/high-risk knowledge.
2. Đo trigger/anti-trigger/no-false-ask, consent/source trace, required-type coverage, conflict handling, false validation/transfer và red-line leakage.
3. Lưu prompt/input/output/state/evidence, total_tokens, duration_ms; contributor, expert/delegate và reviewer độc lập ký xác nhận phạm vi.
4. Chạy novel-case test với nhóm đích bằng cùng rubric/threshold; theo dõi failure, correction, retention/revocation và chỉ đề nghị PILOT khi D10 đạt.
