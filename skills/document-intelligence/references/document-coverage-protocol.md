# PROTOCOL KIỂM COVERAGE TÀI LIỆU

## 1. Kiểm kê trước khi đọc

| Định dạng | Thành phần phải kiểm | Dấu hiệu coverage yếu |
|---|---|---|
| PDF | Tổng trang, bookmark, text layer, scan/OCR, bảng, hình, footnote, phụ lục | Text trống, trang ảnh, bảng vỡ cột, số trang nhảy |
| DOCX | Heading, paragraph, table, header/footer, footnote/endnote, comment, text box, tracked changes | Chỉ trích paragraph; bỏ table/comment; revision chưa chốt |
| XLSX | Sheet ẩn/hiện, used range, table, formula, note, named range, filter | Chỉ đọc sheet đang mở; nhầm công thức với giá trị |
| PPTX | Slide, notes, hidden slide, chart/table, appendix | Chỉ đọc text box; bỏ speaker notes/slide ẩn |
| HTML/MD/TXT | Heading, table, list, link, code block, metadata | Bỏ nội dung gập/mở, bảng hoặc link đích |
| Ảnh/scan | Số ảnh/trang, orientation, OCR confidence, vùng chữ, bảng | OCR mất dấu, nhầm số, bỏ vùng rìa |

## 2. Coverage Map

Ghi mỗi thành phần với:

- ID và vị trí;
- loại: văn bản, bảng, hình, note, phụ lục, metadata;
- trạng thái: `ĐÃ ĐỌC`, `KHÔNG ĐỌC ĐƯỢC`, `NGOÀI PHẠM VI`;
- lý do nếu không đọc;
- mức tin cậy OCR/parse nếu có rủi ro;
- hành động khắc phục.

Chỉ ghi "đã đọc toàn bộ" khi không còn thành phần chưa có trạng thái.

## 3. Quy tắc đọc tài liệu lớn

1. Lập inventory và cấu trúc tổng thể trước.
2. Chia chunk theo ranh giới ngữ nghĩa, không cắt giữa bảng, điều khoản hoặc footnote.
3. Lưu ID chunk và phạm vi trang/mục.
4. Tổng hợp sau khi mọi chunk trong phạm vi có trạng thái.
5. Tái kiểm các kết luận có tác động cao trên file gốc, không chỉ trên text trích xuất.

## 4. Quy tắc OCR và parse

- Gắn `[OCR CẦN XÁC NHẬN]` cho số, tên riêng, điều khoản hoặc ký hiệu không chắc.
- So ảnh gốc với text ở các đoạn tác động cao.
- Không tự điền chữ bị mất theo ngữ cảnh mà không gắn Giả định.
- Nếu bảng vỡ cột, quay lại layout gốc; không dùng thứ tự text stream để suy ra hàng/cột.

## 5. Ngoại lệ

- Phụ lục được tuyên bố không thuộc phạm vi vẫn phải xuất hiện trong inventory với trạng thái `NGOÀI PHẠM VI`.
- File hỏng hoặc mật khẩu không được coi là đã đọc; ghi blocker và yêu cầu bản có quyền truy cập.
- Hai phiên bản trùng chủ đề là xung đột nguồn, không phải hai phụ lục.
