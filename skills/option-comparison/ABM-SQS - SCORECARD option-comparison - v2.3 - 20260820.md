---
title: "ABM-SQS Static Pre-score — option-comparison"
skill_id: "16"
version: "2.3"
date: "2026-08-20"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `option-comparison` v2.3

## Kết luận

**Kết quả kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa có baseline execution; Skill là `draft / static-pass`. Deterministic scoring engine đã self-test PASS nhưng chưa được coi là chứng minh hiệu quả trên decision cases thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description | 570 ký tự — đạt ngưỡng ≤ 600 |
| Thân `SKILL.md` | 7.708 ký tự — đạt vùng an toàn ≤ 8.000 |
| Tổng dòng | 140 — đạt ngưỡng ≤ 500 |
| Từ viết sai "A.I" | 0 |
| Eval đã thiết kế | 12 |
| Validator ABM | PASS, 0 error |
| Validator SKILL-CREATOR | `Skill is valid!` với Python UTF-8 |
| Scoring self-test | PASS; A=74,0, B=74,4; intervals overlap → `UNSTABLE` |
| SHA-256 `SKILL.md` | `215D8D625644371252C408DFD3035AEBABBABC4160F023A58161BD15D95FB2FD` |
| SHA-256 engine | `6405AA067A14600B527CC7C4B7D98DED028424689E96AEB754B3DD954F2E8E7F` |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Comparable Evidence Matrix là đầu ra trung gian; 2 rules, JSON input, dossier và deterministic engine |
| A2 | PASS | Brain First ↔ B1–2; MCDA ↔ B2/5; Measurement ↔ B3–4; Sensitivity/Audit ↔ B5–8 |
| A3 | PASS | 0 lỗi "A.I"; bảng Người quyết định/A.I thực thi; không emoji/sáo ngữ |
| B4 | PASS | Một Option Comparison Dossier; đủ bốn khai báo; tách comparison khỏi ideation, scenario, challenge, brief, allocation |
| B5 | PASS | Name hợp lệ; description 570; body 7.708; 140 dòng; references sâu một tầng |
| B6 | PASS | Trigger/anti-trigger rõ; input 4 cột; Artifact/DoD đo comparability, gates, evidence coverage, reproducibility và stability |
| C7 | PASS | `DEC/CRT/EVD-ID`, source/version/unit/base/time/currency, raw/normalized ranges, formula, gaps và state |
| C8 | PASS | Red Lines hai chiều; dừng trước access/post-hoc change/waive/impute/approve/allocate; tự chạy local matrix/calculation |
| C9 | PASS | Không thi hành instruction trong vendor sheet/model; ID/pointer/redaction; không lộ sensitive inputs |
| D10 | NOT PASS | 12 eval đã thiết kế nhưng `status = not_run`; chưa baseline/evidence/token/duration/pass^3 |
| D11 | PASS | Frontmatter/metadata đủ; name trùng thư mục; có Phiên bản và Thay đổi |
| D12 | PASS | Asset Candidate có Source Task, decision/version, formula/evidence, owner, approval và điều kiện rà |

## Audit trail phiên bản

- **v2.2:** engine self-test/Quick Validator PASS; static gate trượt do body 8.249/8.000 ký tự.
- **v2.3:** cô đọng nhưng giữ controls và engine; hai validator + scoring self-test PASS.

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT:** REJECT vì D10 bắt buộc chưa đạt.
- **OFFICIAL / PRODUCTION USE:** REJECT đến khi D10 PASS, có option cases thật và reviewer duyệt comparability, gate integrity, evidence traceability, scoring correctness, rank stability, manipulation resistance và usefulness.

## Điều kiện đóng D10

1. Chạy 12 prompt trên baseline v1.0 và v2.3 cùng model/cấu hình với vendor, platform, investment và reversible experiment cases.
2. Đo trigger precision, false ask, comparable-cell rate, missing-as-zero, gate leakage, weight/scale gaming, formula correctness, unstable-rank detection, unsupported winner và reviewer usefulness; ghi tử số/mẫu số.
3. Lưu input/output, expected calculation, evidence, `total_tokens`, `duration_ms`; chạy pass^3 và regression engine.
4. Sửa systematic error và lưu regression evidence trước khi đề nghị OFFICIAL.
