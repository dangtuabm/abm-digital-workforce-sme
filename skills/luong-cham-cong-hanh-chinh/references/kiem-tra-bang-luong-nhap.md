# DANH MỤC SOÁT BẢNG LƯƠNG NHÁP

Mục đích: giúp người phụ trách lương phát hiện lỗi **trước khi** trình duyệt. A.I chỉ chỉ ra, không sửa bảng lương, không ra số lương thay.

## 1. Khớp với bảng công đã chốt

- Số nhân viên trên bảng lương = số nhân viên có công trong kỳ (cộng người nghỉ việc còn được trả, trừ người chưa đủ điều kiện theo quy chế).
- Từng người: ngày công, giờ tăng ca theo loại ngày, ngày nghỉ có lương/không lương trên bảng lương = bảng công đã chốt.
- Bảng công chưa chốt → dừng soát phần này, báo người phụ trách.

## 2. Kiểm cấu trúc bảng tính

| Kiểm | Dấu hiệu lỗi |
|---|---|
| Ô gõ tay giữa cột công thức | Một ô là số cố định trong khi cả cột là công thức |
| Tham chiếu sai dòng | Công thức dòng của người A lấy công của người B |
| Vùng cộng thiếu | Tổng cộng không gồm dòng cuối hoặc dòng mới chèn |
| Làm tròn không thống nhất | Một số dòng làm tròn khác quy chế |
| Ô trống được hiểu là 0 | Người có công nhưng ô lương cơ bản trống |

## 3. Biến động so kỳ trước

- Mỗi người: thực nhận kỳ này so kỳ trước thay đổi vượt ngưỡng doanh nghiệp đặt (ví dụ quy chế ghi ±[...]%) → liệt kê kèm lý do có thể giải thích được từ dữ liệu (tăng ca nhiều, nghỉ không lương, đổi mức lương có quyết định).
- Không có lý do giải thích được từ dữ liệu → ghi "cần người phụ trách giải thích", không đoán.
- Doanh nghiệp chưa đặt ngưỡng → liệt kê 10 người biến động lớn nhất theo số tuyệt đối, gắn [GIẢ ĐỊNH].

## 4. Trường hợp đặc biệt

- Nhân viên mới vào giữa kỳ, nghỉ việc giữa kỳ, đổi vị trí, đổi mức lương có quyết định trong kỳ.
- Khấu trừ, tạm ứng, truy thu, truy lĩnh: có chứng từ đi kèm không.
- Các khoản bảo hiểm, thuế: chỉ kiểm có áp dụng nhất quán với quy chế không; đúng sai theo quy định pháp luật → đối chiếu văn bản pháp luật hiện hành, cần người có chuyên môn xác nhận.

## 5. Cách ghi một chỗ lệch

| Cột | Nội dung |
|---|---|
| Mã | SL-[kỳ]-[số] |
| Mã nhân viên | |
| Mục kiểm | Khớp bảng công / Cấu trúc / Biến động / Đặc biệt |
| Ô trên bảng lương | Tên cột, dòng |
| Giá trị trên bảng lương | |
| Giá trị theo nguồn đối chiếu | (bảng công, quyết định, kỳ trước) |
| Nhận định | [DỮ KIỆN] / [SUY LUẬN] |
| Người cần xử lý | Người phụ trách lương |

Báo cáo soát không chứa toàn bộ bảng lương; chỉ chứa các dòng có chỗ lệch, mã nhân viên thay cho tên.

*[A.I Generated — Claude Code — 30/10/2026]*
