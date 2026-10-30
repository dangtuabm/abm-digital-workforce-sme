# CHẨN ĐOÁN LỖI KẾT NỐI

Dùng ở chế độ Chữa lỗi. Luôn bắt đầu từ **ví dụ thật** (mã đơn, ngày giờ, hai bản ghi trùng), không từ cảm nhận "hay bị lệch".

| Triệu chứng | Nguyên nhân thường gặp | Cách kiểm | Hướng sửa (đề xuất, người có quyền làm) |
|---|---|---|---|
| Một đơn/khách xuất hiện hai lần | Bên nguồn báo lại, kết nối chạy lại nhưng không có mã chống trùng | So mã gốc của hai bản ghi; xem nhật ký có hai lần nhận | Thêm mã chống trùng theo mã nghiệp vụ; lập danh sách bản ghi trùng để người phụ trách gộp |
| Số liệu hai bên lệch nhau | Lệch múi giờ, lệch cách làm tròn, đơn hủy bên này chưa cập nhật bên kia | Đối chiếu từng ngày, từng trạng thái đơn | Sửa bảng ánh xạ; thêm quy tắc đồng bộ trạng thái hủy |
| Bản ghi bị thiếu | Báo sự kiện bị mất khi bên nhận ngừng; lô chạy dở; vượt giới hạn số lần gọi | Đếm số bản ghi hai bên theo khoảng thời gian; xem hàng chờ lỗi | Thêm đối chiếu định kỳ và chạy bù có kiểm soát |
| Dữ liệu cũ đè dữ liệu mới | Nhận sai thứ tự, lấy thời điểm nhận thay vì thời điểm thay đổi | So thời điểm thay đổi ở hệ thống gốc | Quy định bản nào thắng theo thời điểm thay đổi gốc |
| Chữ tiếng Việt bị lỗi font | Sai mã hóa ký tự khi xuất/nhập file | Mở file bằng trình soạn thảo, xem mã hóa | Thống nhất mã hóa UTF-8 trong bảng ánh xạ |
| Kết nối báo "thành công" nhưng không thấy dữ liệu | Bên nhận đã nhận nhưng xử lý lỗi sau đó; ghi vào môi trường thử | Kiểm trên hệ thống gốc, kiểm môi trường | Chỉ coi xong khi kiểm trên hệ thống gốc khớp |
| Kết nối ngừng đột ngột | Khóa hết hạn, bị thu hồi quyền, nhà cung cấp đổi phiên bản | Xem thông báo lỗi, lịch thay khóa, thông báo nhà cung cấp | Thay khóa theo quy trình; cập nhật theo phiên bản mới; ghi vào lịch vòng đời |
| Chạy chậm, nghẽn giờ cao điểm | Vượt giới hạn, chạy lại dồn dập | Xem số lần gọi theo giờ, số lần chạy lại | Giãn cách chạy lại, chia lô, đặt hàng chờ |

## Cách viết Phiếu chẩn đoán
1. Triệu chứng + 2–5 ví dụ thật (đã che dữ liệu Vàng).
2. Nguyên nhân khả dĩ, xếp theo khả năng, ghi [Chắc chắn] / [Nhiều khả năng] / [Giả định].
3. Cách kiểm từng nguyên nhân và ai kiểm.
4. Phương án sửa kết nối và phương án dọn dữ liệu sai — cả hai là **đề xuất**.
5. Cách đối chiếu sau khi sửa để biết đã hết lỗi.

Không tự xóa, gộp hay sửa bản ghi trên hệ thống thật.

*[A.I Generated — Claude Code — 30/10/2026]*
