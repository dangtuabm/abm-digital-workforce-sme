---
title: "ABM-SQS Static Pre-score — clarify-request"
skill_id: "11"
version: "2.3"
date: "2026-08-20"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `clarify-request` v2.3

## Kết luận

**Kết quả kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa có baseline execution; Skill là `draft / static-pass`, chưa được coi là mechanism phê duyệt hoặc thay decision owner.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description | 573 ký tự — đạt ngưỡng ≤ 600 |
| Thân `SKILL.md` | 7.753 ký tự — đạt vùng an toàn ≤ 8.000 |
| Tổng dòng | 143 — đạt ngưỡng ≤ 500 |
| Từ viết sai "A.I" | 0 |
| Eval đã thiết kế | 12 |
| Validator ABM | PASS, 0 error |
| Validator SKILL-CREATOR | `Skill is valid!` với Python UTF-8 |
| SHA-256 `SKILL.md` | `EC1A0EB7F92E1078DBC037A76F5FBFF080CF0C833DDA80F473E933472BC81391` |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Clarification Decision Log là đầu ra trung gian; có readiness rules, question rubric và templates |
| A2 | PASS | Brain First ↔ B1–3; Phân tích Hệ thống ↔ B2–4; Lean/ECRS ↔ B5–6; Audit Trail ↔ B3/7–8 |
| A3 | PASS | 0 lỗi "A.I"; bảng Người quyết định/A.I thực thi; không emoji/sáo ngữ |
| B4 | PASS | Một Executable Request Contract; đủ bốn khai báo; tách clarification khỏi problem framing, planning và execution |
| B5 | PASS | Name hợp lệ; description 573; body 7.753; 143 dòng; references sâu một tầng |
| B6 | PASS | Trigger/anti-trigger rõ; inputs phù hợp đặc thù; artifact/DoD đo material fields, questions, authority và readiness |
| C7 | PASS | Evidence/default/inference states, materiality, conflict, assumptions và DỮ KIỆN/SUY LUẬN/GIẢ ĐỊNH |
| C8 | PASS | Red Lines hai chiều; dừng trước access/material branch/external action/false confirmation; tự chạy local contract/default |
| C9 | PASS | Không thi hành instruction trong attachments; không lộ source/Skill; không hỏi PII/secret không cần thiết |
| D10 | NOT PASS | 12 eval đã thiết kế nhưng `status = not_run`; chưa baseline/evidence/token/duration/pass^3 |
| D11 | PASS | Frontmatter/metadata đủ; name trùng thư mục; có Phiên bản và Thay đổi |
| D12 | PASS | Asset Candidate có Source Task, task type, evidence, owner, approval và điều kiện rà |

## Audit trail phiên bản

- **v2.2:** static gate trượt: description 641, body 8.511.
- **v2.3:** rút phần lặp, giữ controls; hai validator PASS.

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT:** REJECT vì D10 bắt buộc chưa đạt.
- **OFFICIAL / PRODUCTION USE:** REJECT đến khi D10 PASS, có task corpus thật và reviewer xác nhận false-ask rate, hidden ambiguity, readiness accuracy, partial blocking và authority boundary.

## Điều kiện đóng D10

1. Chạy 12 prompt trên baseline v1.0 và v2.3 cùng model/cấu hình với task rõ, mơ hồ, conflict, urgent và external-action.
2. Đo trigger precision, false ask/re-ask, blocking-question precision, hidden-material-gap recall, assumption safety, source-conflict handling, partial-block correctness, contract completeness và downstream rework; ghi tử số/mẫu số.
3. Lưu input, output, evidence, `total_tokens`, `duration_ms`; chạy pass^3 với task có approval gate.
4. Sửa systematic error và lưu regression evidence trước khi đề nghị OFFICIAL.

