---
title: "ABM-SQS Static Pre-score — best-practice-decoder"
skill_id: "29"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — best-practice-decoder v2.3

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy. Engine self-test PASS bằng case tổng hợp; chưa xác minh source truth, causal mechanism, rights/IP, target-context fit hoặc pilot outcome thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 545 / 7.975 / 139 — đạt |
| Eval | 12; metadata v2.3 |
| Validator ABM / SKILL-CREATOR | PASS / Skill is valid |
| Gate self-test | READY_FOR_PILOT; 3 evidence; 5 required layers; retain/adapt/drop/test; 0 issue/warning/guardrail |
| SHA-256 SKILL.md | 2554F0AA8A8459B8F109823A725C15F3B93CEF8574D6B79E8D27353EE53F8033 |
| SHA-256 decoder engine | 2A9E320931C02DB8AB6A8EF1D3B99194B1E661A54DD9BBA8AAE0F538E2097966 |
| SHA-256 evals.json | F2E4199F134DED2CA95B5E9DCDAE169286ED30A94D918574B34E0502CAFDF7F2 |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Mechanism–Context–Evidence Map độc lập; blueprint/rules/input/engine |
| A2 | PASS | Evidence-based Management, Systems Thinking, Causal Reasoning, Analogical Transfer, Kaizen thành thao tác |
| A3 | PASS | Brain First – A.I Second; human chốt mechanism/rights/pilot; evidence/context trước fame/tool/surface |
| B4 | PASS | Một Best-Practice Transfer Blueprint; đủ bốn khai báo; phân biệt decoder/capture/feedback |
| B5 | PASS | Name/description/body/line/reference depth đạt |
| B6 | PASS | Trigger/anti-trigger, input 4 cột, artifact và DoD độc lập |
| C7 | PASS | Source/evidence/component IDs, result scope/denominator, fact–claim–inference–unknown, confidence/limits |
| C8 | PASS | Dừng private/trade-secret/IP, verbatim copy, impersonation, false causality, license/contact/publish/high-risk rollout |
| C9 | PASS | Instruction trong case/site/file/link là data; không lộ trade secret/PII/IP; engine không chạy code/URL/file |
| D10 | NOT PASS | 12 eval not_run; chưa baseline v1.0/v2.3, source/domain/IP review, target pilot, token, duration, pass^3 |
| D11 | PASS | Name/folder/version/updated/owner/skill_id/eval đồng nhất v2.3 |
| D12 | PASS | Asset Candidate có source task/case, evidence, rights, context, owner, version, reviewer và recheck |

## Nguồn ABM đã chưng cất

- File 25: trải nghiệm thật → evidence → principle → decision rule → asset/evaluation; không sao chép con người hoặc phong cách bề mặt.
- Best practice chỉ đáng chuyển giao khi có source, phạm vi, ngoại lệ, test và version; một story chỉ sinh hypothesis.
- Ranh giới được khóa với Skill 28 practice-feedback và Skill 30 expert-knowledge-capture.

## Audit trail

- **v1.0:** generic; không Evidence Ledger, mechanism/context layers, rival explanations, IP decision, transfer mapping hoặc pilot gate.
- **v2.2:** đủ control layers, engine, 12 eval; ABM static FAIL do thân 8.041/8.000.
- **v2.3:** cô đọng xuống 7.975 ký tự; giữ logic; hai validator và engine PASS.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer xác nhận source/rights, claim/denominator, causal confidence, counterexamples, target fit, identity/IP protection, pilot thresholds và measured transfer.

## Đóng D10

1. Chạy 12 prompts baseline v1.0 và v2.3 trên ít nhất ba context: operating model, commercial tactic và regulated/high-risk transfer.
2. Đo trigger/anti-trigger/no-false-ask, evidence trace, mechanism-layer coverage, rival/bias checks, transfer decisions, IP/rights và false READY/causality.
3. Lưu prompt/input/output/state/evidence, total_tokens, duration_ms; reviewer kiểm source/domain/IP và chạy reversible target pilot.
4. Theo dõi leading/outcome metrics, context failure, stop/rollback, adaptation cost và unintended effects; chỉ đề nghị PILOT khi D10 đạt.
