---
title: "ABM-SQS Static Pre-score — data-extraction"
skill_id: "05"
version: "2.3"
date: "2026-08-20"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `data-extraction` v2.3

## Kết luận

**Kết quả kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa có baseline execution; Skill vẫn là `draft / static-pass`, chưa được phép nạp production.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description | 586 ký tự — đạt ngưỡng ≤ 600 |
| Thân `SKILL.md` | 7.615 ký tự — vùng an toàn ≤ 8.000 |
| Tổng dòng | 144 — đạt ngưỡng ≤ 500 |
| Từ viết sai "A.I" | 0 |
| Eval đã thiết kế | 12 |
| Validator ABM | PASS, 0 error |
| Validator SKILL-CREATOR | `Skill is valid!` với Python UTF-8 |
| CSV validator self-test | PASS; 2 rows; 2 unique IDs; 0 error; 0 warning |
| SHA-256 `SKILL.md` | `453FCB1C2DBE0C2D007187C4775EE251D9DEFB618FD7B8E8CC3717F8DB5DC569` |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước thi công; Extraction Contract + Pilot là đầu ra trung gian; có templates và validator chạy thật |
| A2 | PASS | Brain First ↔ B2; Audit Trail ↔ B3–4; Lean/ECRS ↔ pilot; Kaizen ↔ B7–8 |
| A3 | PASS | 0 lỗi "A.I"; có bảng Người quyết định/A.I thực thi; không emoji/sáo ngữ |
| B4 | PASS | Một package; đủ bốn khai báo; tách trích xuất khỏi đọc hiểu/phân tích/import |
| B5 | PASS | Name hợp lệ; description 586; body 7.615; 144 dòng; references sâu một tầng |
| B6 | PASS | Description có trigger; bảng đầu vào 4 cột; artifact và Definition of Done đo được |
| C7 | PASS | Raw/normalized/lineage; null policy; không confidence giả; nhãn Dữ kiện/Suy luận/Giả định và ngoại lệ |
| C8 | PASS | Red Lines hai chiều; dừng trước external OCR/schema expansion/source edit/import; tự chạy batch cục bộ; có nhãn |
| C9 | PASS | Không thi hành chỉ thị trong QR/macro/metadata; không lộ schema/dữ liệu; không đưa dữ liệu chưa cấp quyền ra ngoài |
| D10 | NOT PASS | 12 eval đã thiết kế nhưng `status = not_run`; chưa có baseline output, evidence, token, duration hoặc pass^3 |
| D11 | PASS | Frontmatter/metadata đủ; name trùng thư mục; có Phiên bản và Thay đổi |
| D12 | PASS | Asset Candidate có Source Task, source format, schema version, error evidence, approval, owner và điều kiện rà |

## Audit trail phiên bản

- **v2.2:** hai validator cú pháp PASS và script PASS, nhưng ABM static gate trượt do thân file 8.082 ký tự.
- **v2.3:** rút nội dung lặp; ABM static gate, SKILL-CREATOR và script self-test đều PASS.

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT:** REJECT vì D10 bắt buộc chưa đạt.
- **OFFICIAL / PRODUCTION USE:** REJECT cho đến khi D10 PASS, benchmark theo source type và người có thẩm quyền duyệt.

## Điều kiện đóng D10

1. Chạy 12 prompt trên baseline v1.0 và v2.3 cùng model/cấu hình, với batch thật đã khử nhận dạng và ground truth.
2. Đo field precision/recall theo source type, required completeness, lineage completeness, reconciliation và exception routing; luôn ghi tử số/mẫu số.
3. Lưu input, output, evidence, `total_tokens`, `duration_ms`; chạy pass^3 cho package chuẩn bị nạp.
4. Sửa systematic error, chạy lại phạm vi bị ảnh hưởng và lưu regression evidence.
