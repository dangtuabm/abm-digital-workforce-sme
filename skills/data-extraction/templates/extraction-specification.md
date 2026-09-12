# EXTRACTION CONTRACT

**Mã/schema version:**  
**Batch/phạm vi:**  
**Row grain:** Mỗi record đại diện cho...  
**Khóa record:**  
**Output format/destination:**  
**Null/exception policy:**  
**Người duyệt:**

## 1. Source inventory

| SRC-ID | File/bản/hash | Loại | Phạm vi | Expected grain count | Trạng thái | Duplicate flag |
|---|---|---|---|---:|---|---|
| SRC-001 |  |  |  |  |  |  |

## 2. Schema

| Field | Business definition | Type | Required | Repeatability | Source rule | Normalize rule | Allowed/range | Null policy | Example đã duyệt |
|---|---|---|---|---|---|---|---|---|---|
| record_id |  | string | Yes | 1 |  |  | unique |  |  |
| source_pointer |  | string | Yes | 1 |  |  |  |  |  |
| extraction_status |  | enum | Yes | 1 |  |  | EXACT/OCR_REVIEW/AMBIGUOUS/MISSING/INVALID_FORMAT |  |  |

## 3. Pilot

| Chỉ số | Tử số/Mẫu số | Kết quả | Evidence | Quyết định |
|---|---|---|---|---|
| Source coverage | / |  |  | GO / FIX / STOP |
| Required completeness | / |  |  |  |
| Record exact match so ground truth | / |  |  |  |
| Exception rate | / |  |  |  |

## 4. Acceptance

- [ ] Grain/schema/null policy đã được chốt
- [ ] Pilot đại diện cho các layout/source quality chính
- [ ] Lineage và exception workflow dùng được
- [ ] Tiêu chí GO/FIX/STOP đã được người có thẩm quyền duyệt


