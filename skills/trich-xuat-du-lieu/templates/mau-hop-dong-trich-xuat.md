# HỢP ĐỒNG TRÍCH XUẤT — [Tên lô]

**Mã / phiên bản bộ trường:** HDTX-[YYYY]-[NNN] / v[1] · **Lô / phạm vi:** [...]
**Nhãn dữ liệu thư mục:** [Xanh / Vàng / Đỏ — nếu Đỏ: người duyệt, ngày duyệt, công cụ được phép]
**Một dòng là:** Mỗi dòng đại diện cho [...] duy nhất, nhận biết bằng [khóa].
**Đầu ra / nơi nhận:** [CSV UTF-8 / Excel / mẫu nhập của phần mềm ...]
**Quy tắc ô thiếu, ngoại lệ:** [...] · **Người duyệt:** [...]

## 1. Danh mục chứng từ nguồn

| Mã nguồn | File / phiên bản | Loại chứng từ | Phạm vi | Số dòng dự kiến | Trạng thái | Nghi trùng |
|---|---|---|---|---:|---|---|
| NG-001 | | | | | | |

## 2. Bộ trường

| Cột | Nghĩa nghiệp vụ | Kiểu | Bắt buộc | Lặp | Lấy ở đâu | Quy tắc chuẩn hóa | Giá trị cho phép / khoảng | Khi thiếu | Ví dụ đã duyệt |
|---|---|---|---|---|---|---|---|---|---|
| ma_ban_ghi | Mã dòng | chữ | Có | 1 | Tự sinh | | không trùng | | BG-0001 |
| vi_tri_nguon | File + trang/vùng | chữ | Có | 1 | | | | | |
| trang_thai_trich | Trạng thái | danh mục | Có | 1 | | | KHỚP NGUỒN / CẦN SOÁT / MƠ HỒ / THIẾU / SAI ĐỊNH DẠNG | | |
| [trường nghiệp vụ] | | | | | | | | | |

## 3. Lô thử

| Chỉ số | Tử số / mẫu số | Kết quả | Căn cứ | Quyết định |
|---|---|---|---|---|
| Chứng từ đã đọc | / | | | LÀM TIẾP / SỬA / DỪNG |
| Ô bắt buộc có giá trị | / | | | |
| Dòng khớp với bản nhập tay đã duyệt | / | | | |
| Dòng vào Sổ ngoại lệ | / | | | |

## 4. Duyệt

- [ ] Nhãn dữ liệu đã kiểm; dữ liệu Đỏ (nếu có) đã được duyệt bằng văn bản
- [ ] "Một dòng là gì", bộ trường, quy tắc ô thiếu đã chốt
- [ ] Lô thử đại diện cho các mẫu chứng từ chính
- [ ] Luồng ngoại lệ dùng được; người có thẩm quyền đã chọn LÀM TIẾP / SỬA / DỪNG

*[A.I Generated — Claude Code — 30/10/2026]*
