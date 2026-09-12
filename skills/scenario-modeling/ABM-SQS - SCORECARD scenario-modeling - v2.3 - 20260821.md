---
title: "ABM-SQS Static Pre-score — scenario-modeling"
skill_id: "17"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `scenario-modeling` v2.3

## Kết luận

**Kết quả kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa có baseline execution; Skill là `draft / static-pass`. Safe deterministic engine đã self-test PASS nhưng chưa chứng minh hiệu quả trên models thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description | 594 ký tự — đạt ≤ 600 |
| Thân `SKILL.md` | 7.752 ký tự — đạt ≤ 8.000 |
| Tổng dòng | 140 — đạt ≤ 500 |
| Eval đã thiết kế | 12 |
| Validator ABM / SKILL-CREATOR | PASS / `Skill is valid!` |
| Engine self-test | PASS; downside profit -22.250 kích hoạt `TRG-LOSS`; break-even volume 666,6667 `FOUND` |
| SHA-256 `SKILL.md` | `E1D794CCD0078A12E5A44A1D3C8C0A5F970CBC0A8742714864487D87CCDA8535` |
| SHA-256 engine | `4FA0509D31CE18FB443E95D31486C244CA78F94932A9893F8D8D91A6FD33CCD0` |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Model Register trung gian; 2 rules, JSON input, pack template và safe engine |
| A2 | PASS | Brain First ↔ B1–2; Systems ↔ B2–4; Scenario Planning ↔ B3–5; Sensitivity/Audit ↔ B5–8 |
| A3 | PASS | 0 lỗi "A.I"; human/A.I table; không emoji/sáo ngữ |
| B4 | PASS | Một Scenario Model Pack; đủ bốn khai báo; tách modeling khỏi comparison, challenge, dashboard, allocation |
| B5 | PASS | Name hợp lệ; description 594; body 7.752; 140 dòng; references sâu một tầng |
| B6 | PASS | Trigger/anti-trigger, input 4 cột, artifact/DoD đo integrity, coherence, reproducibility, sensitivity và state |
| C7 | PASS | `MOD/DRV/EQN-ID`, source/version/unit/range/dependency, formulas, configurations, gaps và validation state |
| C8 | PASS | Red Lines hai chiều; dừng trước access/manipulation/fake probability/approve/act; tự chạy local model |
| C9 | PASS | Formula AST chỉ arithmetic/names; không function/file/network; pointer/redaction |
| D10 | NOT PASS | 12 eval, `status = not_run`; chưa baseline/evidence/token/duration/pass^3 |
| D11 | PASS | Frontmatter/metadata/version đủ; name trùng folder |
| D12 | PASS | Asset Candidate có Source Task, model/version, evidence, owner, approval và review trigger |

## Audit trail phiên bản

- **v2.2:** engine/Quick Validator PASS; static gate trượt body 8.350/8.000; sample break-even đúng `NOT_BRACKETED`.
- **v2.3:** cô đọng; mở approved sample range để test `FOUND`; hai validator + engine self-test PASS.

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT:** REJECT vì D10 chưa đạt.
- **OFFICIAL:** REJECT đến khi D10 PASS, reviewer duyệt unit/formula integrity, scenario coherence, model safety, break-even/sensitivity correctness, false probability, trigger usefulness và model drift controls.

## Điều kiện đóng D10

1. Chạy 12 prompt baseline v1.0 và v2.3 trên unit economics, cash, capacity và operating-risk models.
2. Đo trigger precision, false ask, sourced-driver coverage, unit/cycle/injection detection, scenario coherence, formula/result accuracy, false probability, break-even/sensitivity/trigger correctness và reviewer usefulness.
3. Lưu model input/output/expected values, evidence, `total_tokens`, `duration_ms`; chạy pass^3 và engine regression.
4. Sửa systematic error, lưu regression evidence trước đề nghị OFFICIAL.
