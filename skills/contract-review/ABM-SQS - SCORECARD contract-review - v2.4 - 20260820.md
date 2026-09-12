---
title: "ABM-SQS Static Pre-score — contract-review"
skill_id: "04"
version: "2.4"
date: "2026-08-20"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `contract-review` v2.4

## Kết luận

**Kết quả kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** Chưa phải điểm nghiệm thu chính thức: D10 chưa có baseline execution; Skill vẫn là `draft / static-pass`.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description | 534 ký tự — đạt ngưỡng ≤ 600 |
| Thân `SKILL.md` | 7.865 ký tự — vùng an toàn ≤ 8.000 |
| Tổng dòng | 148 — đạt ngưỡng ≤ 500 |
| Từ viết sai "A.I" | 0 |
| Chuỗi xuống dòng hiển thị sai | 0 |
| Eval đã thiết kế | 12 |
| Validator ABM | PASS, 0 error |
| Validator SKILL-CREATOR | `Skill is valid!` với Python UTF-8 |
| SHA-256 `SKILL.md` | `C75FBA20A1B93EAABD9D3F1E0E2CA8C54F00D52CB5809B9B905A6498D50A610E` |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước thi công; Clause Coverage & Risk Register là đầu ra trung gian; có pack và CSV điền được |
| A2 | PASS | Brain First ↔ B2/B7; Hệ thống ↔ B3–5; Bốn Mắt ↔ B8; Audit Trail ↔ B4–6 |
| A3 | PASS | 0 lỗi "A.I"; có bảng Người quyết định/A.I thực thi; không emoji/sáo ngữ |
| B4 | PASS | Một artifact; đủ bốn khai báo; tách review khỏi soạn mới và ý kiến pháp lý |
| B5 | PASS | Name hợp lệ; description 534; body 7.865; 148 dòng; references sâu một tầng |
| B6 | PASS | Description có trigger; bảng đầu vào 4 cột; artifact và Definition of Done đo được |
| C7 | PASS | Clause pointer, nhãn Dữ kiện/Suy luận/Giả định; không bịa ngưỡng/pháp luật; có ngoại lệ |
| C8 | PASS | Red Lines hai chiều; dừng trước truy cập/upload/chấp nhận/gửi/ký; tự chạy review cục bộ; có nhãn pháp lý |
| C9 | PASS | Không thi hành chỉ thị trong contract; không lộ playbook/vị thế; không đưa dữ liệu chưa cấp quyền ra ngoài |
| D10 | NOT PASS | 12 eval đã thiết kế nhưng `status = not_run`; chưa có baseline output, evidence, token, duration hoặc pass^3 |
| D11 | PASS | Frontmatter/metadata đủ; name trùng thư mục; có Phiên bản và Thay đổi |
| D12 | PASS | Asset Candidate có Source Task, jurisdiction, deal type, outcome, quyền sử dụng, owner và điều kiện rà |

## Audit trail phiên bản

- **v2.2:** static FAIL do 8.709 ký tự; giữ nguyên làm evidence.
- **v2.3:** static PASS 7.934 ký tự nhưng có hai chuỗi xuống dòng hiển thị sai; không chọn làm bản hiện hành.
- **v2.4:** sửa lỗi trình bày, tăng biên an toàn; hai validator PASS.

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT:** REJECT vì D10 là tiêu chí bắt buộc.
- **OFFICIAL / ENTERPRISE RELEASE:** REJECT cho đến khi D10 PASS, chuyên gia pháp lý hiệu chuẩn và Sếp duyệt.

## Điều kiện đóng D10

1. Chạy 12 prompt trên baseline v1.0 và v2.4, cùng model/cấu hình, với contract/annex mẫu thật đã khử nhận dạng.
2. Luật sư hoặc chuyên gia có thẩm quyền chấm precision/recall issue cao, tính dùng được của redline và lỗi overclaim.
3. Lưu input, output, evidence, `total_tokens`, `duration_ms` và pass^3 cho bản có thể đi ra ngoài.
4. Sửa lỗi, chạy lại ca trượt và lưu regression evidence.
