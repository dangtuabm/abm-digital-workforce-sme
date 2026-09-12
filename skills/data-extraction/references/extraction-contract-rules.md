# QUY TẮC EXTRACTION CONTRACT

## 1. Khóa grain

Viết một câu: **“Mỗi record đại diện cho [thực thể/sự kiện] duy nhất, được xác định bằng [khóa].”**

| Tình huống | Grain đúng | Lỗi phổ biến |
|---|---|---|
| Hóa đơn | Một invoice hoặc một line item; chọn một và thiết kế parent-child | Trộn field invoice với line item trong một row |
| Biểu mẫu | Một submission; bảng lặp tách child table | Nhân bản thông tin submission cho từng dòng lặp |
| Hồ sơ nhiều trang | Một hồ sơ theo ID gốc | Coi mỗi trang là một record |
| Bảng trong PDF | Một dòng logic, không nhất thiết một dòng hình học | Tách cell xuống dòng thành record mới |

## 2. Schema field

Mỗi field ghi:

- `field_name` và business definition;
- data type: string, integer, decimal, boolean, date, datetime, enum, array, object;
- required/optional/conditional;
- repeatability và parent-child relation;
- source location/rule;
- raw representation;
- normalization rule và locale/timezone/unit;
- allowed values/range/regex nếu có căn cứ;
- null policy và exception owner;
- ví dụ đúng/sai đã được duyệt nếu có.

## 3. Raw, normalized và status

- `raw_value`: đúng như nguồn/OCR đọc, không “làm đẹp”.
- `normalized_value`: giá trị sau rule; không thay raw.
- `source_pointer`: file + trang/region/table/row/cell.
- `extraction_method`: text layer, OCR, table parser, manual-confirmed.
- `extraction_status`: `EXACT`, `OCR_REVIEW`, `AMBIGUOUS`, `MISSING`, `INVALID_FORMAT`.

Chỉ dùng confidence số học khi công cụ đã được hiệu chuẩn trên cùng loại tài liệu. Nếu không, status bằng chứng tốt hơn một % giả.

## 4. Null policy

Phân biệt:

- `MISSING_IN_SOURCE`: nguồn không có;
- `UNREADABLE`: nguồn có nhưng không đọc được;
- `NOT_APPLICABLE`: field không áp cho record theo rule;
- `NOT_PROVIDED`: tài liệu/phụ lục cần thiết chưa được giao;
- `INVALID_FORMAT`: có raw nhưng không map được theo type/rule.

Không dùng chuỗi rỗng cho tất cả trường hợp.

## 5. Chuẩn hóa

- Date mơ hồ như `03/04/2026`: giữ raw và `AMBIGUOUS` khi locale chưa khóa.
- Số: tách decimal/thousands theo locale; không xóa dấu theo cảm tính.
- Currency/unit: lưu value và unit/currency riêng; không quy đổi nếu chưa có rule/tỷ giá/mốc.
- Identifier: giữ leading zero nếu là mã, không ép integer.
- Enum: không map từ gần nghĩa nếu mapping table chưa duyệt.
- Boolean: chỉ map theo phrase/rule đã khóa; trống không đồng nghĩa false.

## 6. Không áp dụng

- Schema thay đổi giữa batch phải tăng version; không trộn output.
- Rule từ một nhà cung cấp/format không tự áp cho format khác.
- Source conflict không được “giải quyết” bằng chọn giá trị mới hơn; đẩy exception.


