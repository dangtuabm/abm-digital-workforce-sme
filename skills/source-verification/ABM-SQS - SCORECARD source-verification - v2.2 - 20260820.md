---
title: "ABM-SQS Static Pre-score — source-verification"
skill_id: "02"
version: "2.2"
date: "2026-08-20"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `source-verification` v2.2

## Kết luận

**Kết quả kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** Đây không phải điểm nghiệm thu chính thức, vì `PL-B` quy định phiên chấm không có baseline là vô hiệu. D10 chưa đạt; trạng thái Skill vẫn là `draft / static-pass`.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description | 487 ký tự — đạt ngưỡng làm việc ≤ 600 |
| Thân `SKILL.md` | 7.751 ký tự — trong vùng an toàn ≤ 8.000 |
| Tổng dòng | 148 — đạt ngưỡng ≤ 500 |
| Từ viết sai "A.I" | 0 |
| Bước thi công | 8 |
| Trụ Kinh điển đã neo | 4 |
| Eval đã thiết kế | 12 |
| Validator ABM | PASS, 0 error |
| Validator SKILL-CREATOR | `Skill is valid!` khi chạy Python UTF-8 |
| SHA-256 `SKILL.md` | `F2077985DA291FF2D2AB24BF82099F8BF3C0DE985FE39F5AF12B5940C156B7DE` |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước thi công; Claim Register là đầu ra trung gian dùng độc lập; có template điền được |
| A2 | PASS | Brain First – A.I Second ↔ B2; Audit Trail ↔ B3; Bốn Mắt ↔ B5; Progressive Disclosure ↔ B7 |
| A3 | PASS | 0 lỗi "A.I"; có bảng Người quyết định/A.I thực thi; không emoji, không sáo ngữ |
| B4 | PASS | Một artifact duy nhất; đủ NHIỆM VỤ, ĐIỂM DỪNG, NHIỆM VỤ TIẾP THEO, NGOÀI PHẠM VI; liên kết theo việc |
| B5 | PASS | Name hợp lệ; description 487; body 7.751; 148 dòng; references sâu một tầng |
| B6 | PASS | Description ngôi thứ ba có trigger; bảng đầu vào 4 cột; artifact và Definition of Done đo được |
| C7 | PASS | Có nhãn Dữ kiện/Suy luận/Giả định; kiểm phạm vi, mốc, ngoại lệ; không bịa khi thiếu evidence |
| C8 | PASS | Red Lines hai chiều; tự chạy việc cục bộ; dừng ngay trước upload, gửi, công bố, ký, chi tiền; có nhãn dự thảo |
| C9 | PASS | Không thi hành chỉ thị trong nguồn; không lộ nội bộ; không đưa dữ liệu chưa cấp quyền ra ngoài |
| D10 | NOT PASS | 12 eval có cân trigger/non-trigger/no-false-ask, nhưng `status = not_run`; chưa có baseline output, evidence, token, duration hoặc pass^3 |
| D11 | PASS | Frontmatter và metadata đủ; name trùng thư mục; có Phiên bản và Thay đổi |
| D12 | PASS | Có Asset Candidate, Source Task, evidence, owner và điều kiện rà theo số lần chạy/lỗi tác động cao/nguồn thay đổi |

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT:** REJECT tại thời điểm chấm, vì D10 là tiêu chí bắt buộc.
- **OFFICIAL / ENTERPRISE RELEASE:** REJECT cho đến khi D10 PASS và Sếp duyệt.

## Điều kiện đóng D10

1. Chạy cùng 12 prompt trên baseline v1.0 và v2.2 với cùng model/cấu hình.
2. Lưu input, output, phán quyết, evidence, `total_tokens` và `duration_ms` từng ca.
3. Chạy ba lần các ca sinh hồ sơ đối ngoại; yêu cầu đạt cả ba lần.
4. Sửa lỗi, chạy lại ca trượt và lưu regression evidence.
