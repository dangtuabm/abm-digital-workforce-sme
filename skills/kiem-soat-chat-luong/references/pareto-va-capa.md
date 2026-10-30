# PARETO, LỖI LẶP LẠI VÀ VÒNG ĐỜI CAPA

## Mục lục
1. Pareto đúng cách và tỷ lệ có mẫu số
2. Lỗi lặp lại
3. Tìm nguyên nhân gốc
4. Khắc phục khác phòng ngừa
5. Kiểm hiệu lực và vòng đời CAPA

## 1. Pareto đúng cách

- Xếp các loại lỗi từ nhiều đến ít, cộng dồn phần trăm; khoanh nhóm đầu chiếm khoảng 80% số lỗi. Đây là nhóm nên mở CAPA trước.
- Làm **hai** bảng: theo số lượng và theo mức độ (mỗi lỗi nhân hệ số NGHIÊM TRỌNG / NẶNG / NHẸ; bộ chạy mặc định 10 / 3 / 1 [GIẢ ĐỊNH — người phụ trách chất lượng chỉnh bằng `--he-so`]). Một lỗi NGHIÊM TRỌNG ít gặp vẫn phải nêu riêng, không bị "chìm" vì số nhỏ.
- Chỉ so được khi cùng cách gọi lỗi: chuẩn hóa mã lỗi trước (sổ lỗi chuẩn hóa).
- Có thể Pareto theo chiều khác: theo công đoạn, theo ca, theo máy, theo nhà cung cấp, theo sản phẩm (`--theo <cot>` trong bộ chạy).

**Tỷ lệ phải có mẫu số:** tỷ lệ lỗi = số sản phẩm/đơn lỗi ÷ số sản phẩm/đơn đã kiểm, cùng kỳ, cùng điểm kiểm. Ca có 10 lỗi trên 2.000 sản phẩm tốt hơn ca có 5 lỗi trên 200. Thiếu số đã kiểm → chỉ báo số lỗi và ghi "chưa tính được tỷ lệ".

Đọc kết quả bộ chạy `scripts/pareto-loi.py`:

| Cột | Ý nghĩa |
|---|---|
| `so_luong` | Tổng số lỗi của nhóm trong kỳ |
| `phan_tram`, `cong_don` | Tỷ trọng và tỷ trọng cộng dồn |
| `nhom_80` | `co` nếu nằm trong nhóm đầu chiếm tới khoảng 80% |
| `nghiem_trong` | Số lỗi NGHIÊM TRỌNG trong nhóm |
| `so_tuan` | Số tuần khác nhau có lỗi này — từ 2 tuần là lỗi lặp lại |
| `lap_sau_capa` | Mã CAPA đã đóng mà lỗi vẫn quay lại sau ngày đóng |

## 2. Lỗi lặp lại

Hai loại cần báo:
1. **Lặp nhiều kỳ, chưa có CAPA:** cùng mã lỗi xuất hiện từ 2 tuần trở lên → đề xuất mở CAPA.
2. **Lặp sau khi đã đóng CAPA:** cùng mã lỗi xuất hiện sau ngày đóng → CAPA chưa hiệu lực → **MỞ LẠI** CAPA cũ (không mở phiếu mới trùng), báo người đã duyệt đóng.

Lỗi lặp lại thường do: chỉ sửa triệu chứng; hành động phòng ngừa là "nhắc nhở"; người mới chưa được đào tạo theo cách mới; thay nhà cung cấp, máy, công thức mà không kiểm lại.

## 3. Tìm nguyên nhân gốc

**5 lần Tại sao** — hỏi "tại sao" tới khi gặp nguyên nhân doanh nghiệp kiểm soát và sửa được:
> Hộp giao bị móp → tại sao? Thùng carton bị đè → tại sao? Xếp 8 tầng trên xe → tại sao? Không có quy định số tầng tối đa → tại sao? Chưa ai lập quy cách xếp hàng khi đổi sang thùng mỏng hơn.
> Nguyên nhân gốc: thay quy cách thùng mà không cập nhật quy cách xếp.

**Xương cá** — khi nhiều nguyên nhân có thể: liệt kê theo 6 nhóm Con người · Phương pháp · Máy móc · Vật tư · Đo lường · Môi trường; mỗi giả thuyết cần một bằng chứng (sổ lỗi, ảnh, số liệu ca, thử lại).

Quy tắc:
- Nguyên nhân dừng ở "công nhân không cẩn thận", "nhân viên quên" là **chưa đủ**. Hỏi tiếp: vì sao dễ quên, có danh mục kiểm không, có được đào tạo không, việc có quá tải không.
- Không ghi tên cá nhân ở cột nguyên nhân.
- Nguyên nhân chưa có bằng chứng → ghi là giả thuyết. Vấn đề phức tạp, nhiều bên → chuyển việc định khung vấn đề, tìm nguyên nhân gốc.

## 4. Khắc phục khác phòng ngừa

| Loại | Trả lời câu hỏi | Ví dụ (hộp móp) |
|---|---|---|
| Xử lý tức thời | Lỗi đã xảy ra xử lý thế nào ngay bây giờ | Giữ lại hàng chưa giao, kiểm lại kho (người có thẩm quyền quyết) |
| Khắc phục | Bỏ nguyên nhân của lỗi đã xảy ra | Lập quy cách xếp tối đa 5 tầng cho thùng mới |
| Phòng ngừa | Lỗi tương tự không xảy ra ở chỗ khác, lần khác | Mỗi lần đổi bao bì phải kiểm thử xếp chồng trước khi dùng; thêm vào danh mục thay đổi vật tư |

Thứ tự ưu tiên hành động, mạnh đến yếu: loại bỏ khả năng sai (thiết kế lại) → chống sai bằng công cụ, cữ gá, cảnh báo tự động → danh mục kiểm bắt buộc → đào tạo → nhắc nhở. Hành động chỉ có "nhắc nhở, rút kinh nghiệm" → đề xuất bổ sung hành động mạnh hơn.

Hành động cần thay đổi quy trình và phải thử xem có hiệu quả không (đổi cách xếp ca, đổi công thức, đổi bố trí xưởng) → chuyển việc cải tiến liên tục, ghi mã CAPA để nối lại.

## 5. Kiểm hiệu lực và vòng đời CAPA

Mỗi CAPA ghi trước **cách kiểm hiệu lực**: chỉ số nào, ngưỡng nào, trong bao lâu (ví dụ "không lặp lỗi móp trong 4 tuần giao hàng kế tiếp, kiểm bằng sổ lỗi giao hàng" — con số do người phụ trách đặt).

| Trạng thái | Ai chuyển | Điều kiện |
|---|---|---|
| MỞ | A.I | Có mô tả vấn đề có số |
| ĐANG XỬ LÝ | A.I | Đã có nguyên nhân, hành động, người phụ trách, hạn |
| CHỜ KIỂM HIỆU LỰC | A.I | Người phụ trách báo đã làm xong hành động, có bằng chứng |
| ĐỀ XUẤT ĐÓNG | A.I | Hết thời gian kiểm, chỉ số đạt ngưỡng |
| ĐÃ ĐÓNG | **Chỉ người có quyền** | Người duyệt xem bằng chứng |
| MỞ LẠI | A.I đề xuất, báo người duyệt | Lỗi quay lại sau ngày đóng |

Quá hạn hành động → nhắc người phụ trách, sau một lần nhắc chưa có phản hồi → báo trưởng bộ phận. Không tự dời hạn.

*[A.I Generated — Claude Code — 30/10/2026]*
