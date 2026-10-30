# HỒ SƠ TỰ ĐỘNG HÓA — [Tên luồng] v[0.x]

**Ngày:** [dd/mm/yyyy] · **Người phụ trách quy trình:** [họ tên] · **Người quản trị kết nối:** [họ tên] · **Người duyệt dùng thử:** [họ tên]
**Trạng thái:** [ĐÃ THIẾT KẾ / ĐÃ RÀ KIỂM SOÁT / ĐÃ THỬ TRONG MÔI TRƯỜNG THỬ / CHỜ DUYỆT DÙNG THỬ]

## 1. Phạm vi
- Mục tiêu, bắt đầu – kết thúc: [...] · Khối lượng, lúc cao điểm: [...] · Cách làm hiện tại và chi phí (căn cứ): [...]
- Không thuộc phạm vi: [...] · Việc cấm: [...] · Tiêu chí đạt – dừng: [...]

## 2. Quy trình đã sửa
- Hiện tại: [...] · Bước thừa đã bỏ: [...] · Quy trình đích (người phụ trách duyệt ngày ...): [...]

## 3. Dữ liệu gốc

| Dữ liệu | Nơi giữ gốc | Trường khóa | Định dạng, ngày giờ, múi giờ | Trùng / đến muộn / chạy lại | Nhãn | Lưu bao lâu |
|---|---|---|---|---|---|---|

## 4. Trạng thái

| Trạng thái | Vào khi | Bước chuyển hợp lệ | Ai/hệ thống | Kết thúc / LỖI / CHỜ NGƯỜI |
|---|---|---|---|---|

## 5. Bước và kiểm soát
Chi tiết: `bang-buoc-kiem-soat.csv`. Liệt kê điểm người duyệt bắt buộc:

| Bước gửi ra ngoài / chi tiền / cam kết | Điểm duyệt ngay trước | Người duyệt, hạn mức | Hết giờ không ai duyệt thì |
|---|---|---|---|

## 6. Độ tin cậy, bảo mật, dấu vết
- Phân loại lỗi và cách xử lý: [...] · Thử lại: [chỉ lỗi tạm thời, tối đa ... lần theo hướng dẫn công cụ]
- Chống trùng: [mã riêng ...] · Bước KHÔNG THỬ LẠI: [...]
- Hàng chờ lỗi, người xử lý: [...] · Chạy tay dự phòng: [...]
- Đối soát cuối ngày: [so ... với ...]
- Tài khoản chạy luồng, quyền tối thiểu: [...] · Chỗ cất mã API (không ghi giá trị): [...] · Che dữ liệu trong nhật ký: [...]
- Dấu vết mỗi lần chạy: mã lần chạy, giờ, phiên bản luồng, bước, người duyệt, lỗi, trạng thái trước – sau.
- Cần kết nối: [Zalo OA / email / sàn TMĐT / CRM ...]

## 7. Kiểm thử

| Ca | Đầu vào, phiên bản | Mong đợi | Kết quả thật | ĐẠT / KHÔNG ĐẠT | Người xem |
|---|---|---|---|---|---|

## 8. Dùng thử
| Mục | Nội dung |
|---|---|
| Phạm vi hẹp | [một chi nhánh / 10% đơn / 1 tuần] |
| Người kiểm nghiệm | |
| Tiêu chí đạt | |
| Tiêu chí dừng ngay | |
| Theo dõi, báo động | |
| Cách tắt, ai tắt | |
| Quay lui, làm tay trong lúc tắt | |
| Báo người liên quan | |

Bật dùng thử, chạy chính thức: CHỜ NGƯỜI PHỤ TRÁCH QUYẾT

## 9. Rà soát luồng đang chạy (chế độ Rà soát)
- Hiện tượng: [gửi hai lần / mất đơn / lỗi không ai biết] · Thời gian: [...] · Số bản ghi bị ảnh hưởng: [...]
- Dòng thời gian từ nhật ký: [...]
- Đối soát với dữ liệu gốc: [...]
- Nguyên nhân: [sự kiện đến hai lần / thử lại khi bước trước đã thành công / hai luồng cùng nghe một sự kiện / chạy tay chồng luồng tự động / khác]
- Đề xuất sửa: [...] · Việc với khách hoặc giao dịch bị ảnh hưởng (người quyết): [...]

## 10. Rủi ro, quyết định, nhật ký thay đổi
- Rủi ro còn lại: [...] · Việc chờ quyết định: [...] · Phiên bản và thay đổi: [...]

*[A.I Generated — Claude Code — 30/10/2026]*
