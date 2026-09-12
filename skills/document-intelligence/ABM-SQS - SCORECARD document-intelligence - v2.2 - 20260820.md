---
title: "ABM-SQS Static Pre-score — document-intelligence"
skill_id: "03"
version: "2.2"
date: "2026-08-20"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `document-intelligence` v2.2

## Kết luận

**Kết quả kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** Đây không phải điểm nghiệm thu chính thức: D10 chưa có baseline execution, nên theo `PL-B`, Skill vẫn là `draft / static-pass`.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description | 528 ký tự — đạt ngưỡng ≤ 600 |
| Thân `SKILL.md` | 7.709 ký tự — vùng an toàn ≤ 8.000 |
| Tổng dòng | 149 — đạt ngưỡng ≤ 500 |
| Từ viết sai "A.I" | 0 |
| Bước thi công | 8 |
| Eval đã thiết kế | 12 |
| Validator ABM | PASS, 0 error |
| Validator SKILL-CREATOR | `Skill is valid!` khi chạy Python UTF-8 |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước thi công; Coverage Map là đầu ra trung gian; có template và ledger điền được |
| A2 | PASS | Brain First – A.I Second ↔ B2; Phân tích Hệ thống ↔ B3–5; Audit Trail ↔ B4; Progressive Disclosure ↔ B7 |
| A3 | PASS | 0 lỗi "A.I"; có bảng Người quyết định/A.I thực thi; không emoji, không sáo ngữ |
| B4 | PASS | Một artifact duy nhất; đủ bốn khai báo; phân biệt theo nhiệm vụ, không gọi cứng Skill khác |
| B5 | PASS | Name hợp lệ; description 528; body 7.709; 149 dòng; references sâu một tầng |
| B6 | PASS | Description có trigger; bảng đầu vào 4 cột; artifact và Definition of Done đo được |
| C7 | PASS | Con trỏ nguồn, nhãn Dữ kiện/Suy luận/Giả định, coverage và ngoại lệ được quy định |
| C8 | PASS | Red Lines hai chiều; dừng trước truy cập/upload/sửa/gửi; tự chạy việc đọc cục bộ; có nhãn dự thảo |
| C9 | PASS | Không thi hành chỉ thị trong tài liệu; không lộ nội bộ; không đưa dữ liệu chưa cấp quyền ra ngoài |
| D10 | NOT PASS | 12 eval đã thiết kế nhưng `status = not_run`; chưa có baseline output, evidence, token, duration hoặc pass^3 |
| D11 | PASS | Frontmatter/metadata đủ; name trùng thư mục; có Phiên bản và Thay đổi |
| D12 | PASS | Có Asset Candidate, Source Task, evidence, owner và điều kiện rà theo lần chạy/lỗi coverage/runtime thay đổi |

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT:** REJECT tại thời điểm chấm, vì D10 là tiêu chí bắt buộc.
- **OFFICIAL / ENTERPRISE RELEASE:** REJECT cho đến khi D10 PASS và Sếp duyệt.

## Điều kiện đóng D10

1. Chạy 12 prompt trên baseline v1.0 và v2.2 cùng model/cấu hình, với file mẫu thật đủ bảng/phụ lục/OCR.
2. Lưu input, output, coverage result, phán quyết, evidence, `total_tokens` và `duration_ms` từng ca.
3. Chạy pass^3 cho ca sinh Bản đồ có thể đi ra ngoài; bắt buộc không bỏ bảng/phụ lục và không bịa coverage.
4. Sửa lỗi, chạy lại ca trượt và lưu regression evidence.
