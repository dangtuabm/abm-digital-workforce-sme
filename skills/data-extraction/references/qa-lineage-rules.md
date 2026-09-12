# QUY TẮC QA, LINEAGE VÀ RECONCILIATION

## 1. Bốn lớp kiểm

| Lớp | Kiểm gì | Bằng chứng |
|---|---|---|
| Coverage | Mọi source/page/form/table trong phạm vi có trạng thái | Source inventory và count |
| Schema | Header, type, required, enum, format, unique, relation | Validator report |
| Value | Raw ↔ normalized, OCR mờ, total/subtotal, range nghiệp vụ | Field status và exception |
| Reconciliation | Source = extracted + exception + rejected theo grain | Reconciliation table |

## 2. Lineage tối thiểu

Mỗi record có:

- `record_id`, `schema_version`;
- `source_id`, tên/hash/phiên bản file;
- trang/region/table/row/cell;
- extraction method và thời điểm;
- raw và normalized value cho field đã biến đổi;
- extraction status và exception ID nếu có;
- approval/correction actor cho giá trị đã sửa bằng người.

## 3. Reconciliation

Chọn công thức theo grain và khai báo mẫu số. Ví dụ:

`source documents = processed + unreadable + out of scope`

`expected records = accepted records + exception records + rejected records`

`parent count = parents with children + parents legitimately without children`

Không dùng % trần trụi; luôn ghi numerator/denominator, ví dụ `98/100 source đã xử lý`.

## 4. Sampling

Sampling không thay coverage. Khi batch lớn:

1. Kiểm 100% exception và field tác động cao.
2. Lấy mẫu đại diện theo source type/layout/chất lượng scan, không chỉ random toàn batch.
3. Ghi cỡ mẫu, mẫu số, phương pháp và error type.
4. Nếu phát hiện systematic error, dừng batch, sửa rule và chạy lại phạm vi bị ảnh hưởng.

## 5. Exception lifecycle

Trạng thái: `OPEN`, `ASSIGNED`, `RESOLVED`, `ACCEPTED_RISK`, `REJECTED_SOURCE`.

Mỗi exception ghi raw, pointer, loại lỗi, tác động, owner, quyết định, giá trị sau xử lý và evidence. Không đóng exception bằng cách xóa record.

## 6. Cổng batch

- `GO`: pilot đạt schema, lineage, exception flow và acceptance đã chốt.
- `FIX`: lỗi cục bộ có thể sửa rule/mapping rồi chạy lại.
- `STOP`: grain/schema sai, source không đủ, systematic OCR error hoặc rủi ro dữ liệu chưa được cấp quyền.


