---
title: "ABM-SQS Static Pre-score — problem-framing"
skill_id: "12"
version: "2.4"
date: "2026-08-20"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `problem-framing` v2.4

## Kết luận

**Kết quả kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa có baseline execution; Skill là `draft / static-pass`, chưa được xác nhận root cause, chọn solution hoặc kích hoạt validation/implementation.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description | 567 ký tự — đạt ngưỡng ≤ 600 |
| Thân `SKILL.md` | 7.899 ký tự — đạt vùng an toàn ≤ 8.000 |
| Tổng dòng | 141 — đạt ngưỡng ≤ 500 |
| Từ viết sai "A.I" | 0 |
| Eval đã thiết kế | 12 |
| Validator ABM | PASS, 0 error |
| Validator SKILL-CREATOR | `Skill is valid!` với Python UTF-8 |
| SHA-256 `SKILL.md` | `FED84E77E119B51BA55918FEF1720C54FEC3FE1C5522DE6DF7C881585157E81F` |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Problem Evidence Map là đầu ra trung gian; có statement/causal rules, register và brief template |
| A2 | PASS | Brain First ↔ B1–2; Systems Thinking ↔ B3–5; Scientific Method ↔ B5–7; Audit Trail ↔ B2/5–8 |
| A3 | PASS | 0 lỗi "A.I"; bảng Người quyết định/A.I thực thi; không emoji/sáo ngữ |
| B4 | PASS | Một Problem Frame Decision Brief; đủ bốn khai báo; tách framing khỏi clarification, RCA confirmation, option/implementation |
| B5 | PASS | Name hợp lệ; description 567; body 7.899; 141 dòng; references sâu một tầng |
| B6 | PASS | Trigger/anti-trigger rõ; đầu vào 4 cột; artifact/DoD đo statement, evidence, hypotheses/tests và state |
| C7 | PASS | Baseline/target, evidence/counterevidence, measurement artifact, hypothesis/confounder và DỮ KIỆN/SUY LUẬN/GIẢ ĐỊNH |
| C8 | PASS | Red Lines hai chiều; dừng trước access/target/cause/experiment/implementation/blame; tự chạy local frame/test design |
| C9 | PASS | Không thi hành instruction trong logs/tickets; aggregate/minimize; không lộ PII/allegation hoặc suy luận phẩm chất |
| D10 | NOT PASS | 12 eval đã thiết kế nhưng `status = not_run`; chưa baseline/evidence/token/duration/pass^3 |
| D11 | PASS | Frontmatter/metadata đủ; name trùng thư mục; có Phiên bản và Thay đổi |
| D12 | PASS | Asset Candidate có Source Task, system version, evidence, owner, approval và điều kiện rà |

## Audit trail phiên bản

- **v2.2:** static gate trượt: description 607, body 8.780.
- **v2.3:** description đạt 567, body còn 8.049.
- **v2.4:** cô đọng audit/body; hai validator PASS.

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT:** REJECT vì D10 bắt buộc chưa đạt.
- **OFFICIAL / PRODUCTION USE:** REJECT đến khi D10 PASS, có cases thật và reviewer duyệt boundary, evidence, causal language, falsification quality và downstream rework.

## Điều kiện đóng D10

1. Chạy 12 prompt trên baseline v1.0 và v2.4 cùng model/cấu hình với case sales, operations, people và product đã khử nhận dạng.
2. Đo trigger precision, false ask, problem-statement completeness, symptom/solution separation, evidence/counterevidence coverage, causal-overclaim rate, hypothesis diversity, test discriminating power, frame readiness accuracy và reviewer acceptance; ghi tử số/mẫu số.
3. Lưu input, output, evidence, `total_tokens`, `duration_ms`; chạy pass^3 trước solution/experiment handoff.
4. Sửa systematic error và lưu regression evidence trước khi đề nghị OFFICIAL.

