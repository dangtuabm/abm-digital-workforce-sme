# LỪA ĐẢO, SỰ CỐ VÀ MẤT DỮ LIỆU — HƯỚNG DẪN CHO NGƯỜI DÙNG

Mức hướng dẫn cho nhân viên và lãnh đạo, không phải điều tra kỹ thuật. Việc cần quyền quản trị luôn chuyển người quản trị hệ thống.

## 1. Dấu hiệu email, tin nhắn lừa đảo

| Dấu hiệu | Ví dụ |
|---|---|
| Giục gấp, dọa hậu quả | "Tài khoản sẽ bị khóa trong 2 giờ", "chuyển ngay trước 15h kẻo lỡ hàng" |
| Đổi thông tin nhận tiền | "Công ty chúng tôi đổi số tài khoản, từ đơn này chuyển vào số mới" |
| Người gửi gần giống thật | Tên miền sai một chữ, dùng email miễn phí cho việc của công ty, tên hiển thị là giám đốc nhưng địa chỉ lạ |
| Xin thông tin không cần thiết | Hỏi mật khẩu, mã OTP, ảnh CCCD, "xác minh tài khoản" qua link |
| Link, file lạ | Link rút gọn, tên miền lạ; file nén có mật khẩu; file đuôi .exe, .scr, .js; file Office đòi "bật macro" |
| Mã QR lạ | QR trong email, tờ rơi, tin nhắn đề nghị quét để "nhận quà", "thanh toán" |
| Giả danh người quen trên Zalo, Facebook | Tài khoản mới tạo, ảnh đại diện lấy của người thật, nhờ chuyển tiền giúp |
| Giả danh cơ quan, ngân hàng | Yêu cầu cài ứng dụng, cung cấp OTP, chuyển tiền "để xác minh" |

Kết luận khi soi:
- **ĐÁNG NGỜ:** có từ 1 dấu hiệu nặng (đổi số tài khoản, xin OTP/mật khẩu, file chạy được) hoặc từ 2 dấu hiệu khác.
- **CHƯA RÕ:** có 1 dấu hiệu nhẹ, chưa đủ căn cứ → xác minh trước khi làm theo.
- **CHƯA THẤY DẤU HIỆU:** không thấy dấu hiệu nào. Không nói "an toàn tuyệt đối".

A.I chỉ soi phần nội dung người dùng dán vào; không mở link, không tải file để kiểm tra.

## 2. Xác minh qua kênh thứ hai

- Yêu cầu chuyển tiền, đổi số tài khoản, gửi dữ liệu: **gọi lại số điện thoại đã lưu từ trước** hoặc gặp trực tiếp. Không gọi số, không bấm link nằm trong chính email đó.
- Giám đốc "nhắn gấp" nhờ chuyển tiền: gọi điện thoại cho giám đốc; công ty nên có quy định "không chuyển tiền chỉ theo tin nhắn".
- Đã lỡ bấm link nhưng chưa nhập gì: đóng trang, báo người quản trị.
- Đã nhập mật khẩu hoặc OTP: đổi mật khẩu ngay từ trang chính thức (gõ địa chỉ tay), báo người quản trị và ngân hàng nếu liên quan tài khoản tiền.

## 3. Việc làm ngay khi có sự cố

Áp dụng cho: gửi nhầm dữ liệu Vàng/Đỏ cho A.I hoặc người ngoài, chia sẻ link sai quyền, bấm link lừa đảo, mở file lạ, mất máy.

1. **Dừng lan rộng.** Ngừng gửi tiếp. Không chia sẻ thêm. Máy nghi nhiễm thì ngắt mạng (rút cáp, tắt Wi-Fi), không tắt nguồn nếu người quản trị chưa dặn.
2. **Giữ bằng chứng.** Ghi giờ, ảnh chụp màn hình, mã hoặc tên cuộc trò chuyện, địa chỉ người nhận, đường link. **Không chép lại nội dung nhạy cảm** vào phiếu. Không xóa email, lịch sử, nhật ký.
3. **Báo người phụ trách** ngay (người quản trị hệ thống hoặc người phụ trách dữ liệu đó). Nói rõ đã làm gì.
4. **Đề xuất khoanh vùng** để người có quyền quyết: thu hồi link chia sẻ, đăng xuất các phiên, đổi mật khẩu, thu hồi mã API, xóa cuộc trò chuyện với A.I theo hướng dẫn chính thức, liên hệ người nhận nhầm đề nghị xóa.
5. **Đánh giá phạm vi:** loại dữ liệu, số lượng bản ghi, ai đã nhận, đã bị xem chưa.
6. **Ghi lại** vào `templates/phieu-su-co.md` và theo dõi đến khi đóng.

Không hứa "đã xóa hết": xóa lịch sử trò chuyện chưa chắc xóa bản lưu phía nhà cung cấp. Việc báo khách hàng hoặc cơ quan chức năng do lãnh đạo và người phụ trách pháp chế quyết — đối chiếu văn bản pháp luật hiện hành, cần người có chuyên môn xác nhận.

## 4. Mất máy, máy hỏng, mất dữ liệu

| Tình huống | Việc người dùng làm | Việc chuyển người quản trị |
|---|---|---|
| Mất điện thoại, laptop | Báo ngay; nhớ lại tài khoản nào đang đăng nhập trên máy | Khóa hoặc xóa máy từ xa, đăng xuất phiên, đổi mật khẩu |
| Máy hỏng, không khởi động | Không tự cài phần mềm khôi phục lạ; không mang ra tiệm khi máy có dữ liệu Đỏ mà chưa hỏi | Lấy dữ liệu, khôi phục từ bản sao lưu |
| Xóa nhầm file | Kiểm thùng rác của Drive/OneDrive và máy; kiểm lịch sử phiên bản của file | Khôi phục từ bản sao lưu |
| File bị khóa, đòi tiền chuộc | Ngắt mạng, không trả tiền, báo ngay | Xử lý theo quy trình sự cố |

## 5. Sao lưu cơ bản — người dùng nên biết

- File công việc để trong thư mục đồng bộ của công ty (Google Drive/OneDrive...), không để riêng trên máy.
- Quy tắc 3-2-1 thường dùng: 3 bản, trên 2 loại nơi lưu, 1 bản ở nơi khác (ví dụ đám mây hoặc ổ cất riêng).
- Thỉnh thoảng thử khôi phục một file để chắc bản sao lưu dùng được.
- Thiết lập, lịch và kiểm tra sao lưu là việc của người quản trị hệ thống.

*[A.I Generated — Claude Code — 30/10/2026]*
