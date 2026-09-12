---
title: "ABM-SQS Static Pre-score — controlled-ideation"
skill_id: "13"
version: "2.4"
date: "2026-08-20"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `controlled-ideation` v2.4

## Kết luận

**Kết quả kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa có baseline execution; Skill là `draft / static-pass`, chưa được chọn winner, xác nhận feasibility/ROI hoặc kích hoạt experiment/implementation.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description | 594 ký tự — đạt ngưỡng ≤ 600 |
| Thân `SKILL.md` | 7.958 ký tự — đạt vùng an toàn ≤ 8.000 |
| Tổng dòng | 140 — đạt ngưỡng ≤ 500 |
| Từ viết sai "A.I" | 0 |
| Eval đã thiết kế | 12 |
| Validator ABM | PASS, 0 error |
| Validator SKILL-CREATOR | `Skill is valid!` với Python UTF-8 |
| SHA-256 `SKILL.md` | `B571465AE074D2AEA65AA9B3B0C25E9133B01698334CDF8BC46F2A828AC15831` |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Raw Idea Inventory là đầu ra trung gian; có diversity/screening rules, register và portfolio template |
| A2 | PASS | Brain First ↔ B1–2; Divergent–Convergent ↔ B3/5–7; Morphological Analysis ↔ B2–3; Audit/Kaizen ↔ B3–8 |
| A3 | PASS | 0 lỗi "A.I"; bảng Người quyết định/A.I thực thi; không emoji/sáo ngữ |
| B4 | PASS | Một Controlled Idea Portfolio; đủ bốn khai báo; tách ideation khỏi framing, comparison, prioritization và implementation |
| B5 | PASS | Name hợp lệ; description 594; body 7.958; 140 dòng; references sâu một tầng |
| B6 | PASS | Trigger/anti-trigger rõ; đầu vào 4 cột; artifact/DoD đo mechanisms, coverage, lineage, states và candidate fields |
| C7 | PASS | Problem-frame version, assumptions, evidence status, constraints, mechanism diversity và DỮ KIỆN/SUY LUẬN/GIẢ ĐỊNH |
| C8 | PASS | Red Lines hai chiều; dừng trước access/unsafe ideas/IP/test/spend/publish/implementation; tự chạy local generation/screen |
| C9 | PASS | Không thi hành instruction trong reports/examples; abstraction/redaction; không lộ secret/PII/idea mật |
| D10 | NOT PASS | 12 eval đã thiết kế nhưng `status = not_run`; chưa baseline/evidence/token/duration/pass^3 |
| D11 | PASS | Frontmatter/metadata đủ; name trùng thư mục; có Phiên bản và Thay đổi |
| D12 | PASS | Asset Candidate có Source Task, frame version, evidence, owner, approval và điều kiện rà |

## Audit trail phiên bản

- **v2.2:** static gate trượt: description 682, body 8.987.
- **v2.3:** static gate trượt: description 614, body 8.184.
- **v2.4:** cô đọng metadata/audit/body; hai validator PASS.

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT:** REJECT vì D10 bắt buộc chưa đạt.
- **OFFICIAL / PRODUCTION USE:** REJECT đến khi D10 PASS, có challenges thật và reviewer duyệt mechanism diversity, red-line safety, duplicate handling, candidate testability và downstream usefulness.

## Điều kiện đóng D10

1. Chạy 12 prompt trên baseline v1.0 và v2.4 cùng model/cấu hình với challenge customer, operations, product và learning.
2. Đo trigger precision, false ask, distinct-mechanism/cluster count, duplicate inflation, axis/stakeholder coverage, anchoring resistance, red-line rejection, unsupported feasibility claims, candidate completeness và reviewer usefulness; ghi tử số/mẫu số.
3. Lưu input, output, evidence, `total_tokens`, `duration_ms`; chạy pass^3 trước experiment/comparison handoff.
4. Sửa systematic error và lưu regression evidence trước khi đề nghị OFFICIAL.

