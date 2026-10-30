# KẾT NỐI KÊNH VÀ CHẠY THỬ

Đọc ở Bước L1 (kiểm kê) và L4 (chạy thử). Phần kỹ thuật do người phụ trách kỹ thuật của doanh nghiệp (hoặc nhà cung cấp phần mềm) làm; A.I chỉ chuẩn bị danh mục và kiểm kết quả. Chính sách của từng nền tảng thay đổi thường xuyên — kiểm bản hiện hành trước khi bật.

## I. KIỂM KÊ TRƯỚC KHI KẾT NỐI
- Kênh nào: fanpage nào, Zalo OA nào, chat website nào. Mỗi kênh một cấu hình riêng (bộ nguồn, xưng hô, dữ liệu, khóa truy cập) — không dùng chung giữa hai trang khác nhau.
- Đã có trợ lý tự động, phần mềm chat nào đang chạy chưa? Tránh hai hệ cùng trả lời một khách.
- Ai quản trị kênh, ai giữ khóa truy cập, ai nhận chuyển người theo từng ca.
- Giờ làm việc của nhân viên; quy định trong giờ thì trợ lý trả lời ngay hay nhường nhân viên.

## II. TỪNG KÊNH — CẦN KẾT NỐI

| Kênh | Cách kết nối khuyến nghị | Lưu ý |
|---|---|---|
| Messenger (fanpage) | Ứng dụng kết nối chính thức của nền tảng hoặc phần mềm chat có kết nối chính thức | Chỉ trả lời khách nhắn trước; nhắn ngoài khung thời gian nền tảng cho phép phải theo đúng loại tin được phép |
| Zalo | **Zalo OA chính thức** (tài khoản doanh nghiệp) qua kết nối chính thức | Không tự động hóa Zalo cá nhân: phương pháp không chính thức, rủi ro hạn chế hoặc khóa tài khoản. Nếu khách nhắn vào Zalo cá nhân của nhân viên, A.I chỉ soạn nháp để nhân viên tự gửi |
| Chat website | Phần mềm chat của website hoặc tiện ích chat có kết nối | Hiển thị rõ khách đang chat với trợ lý tự động |

Bảo mật: khóa truy cập, mã xác thực để trong kho bí mật do người phụ trách kỹ thuật quản lý; không dán vào chat, file, câu lệnh; nhật ký che thông tin nhạy cảm.

## III. MA TRẬN CHẠY THỬ (Bước L4)

Chạy bằng tài khoản thử hoặc chế độ thử của phần mềm; **không nhắn tin nào tới khách thật**. Mỗi ca ghi vào `templates/ca-thu-truoc-khi-bat.csv`.

| Nhóm | Ca phải thử |
|---|---|
| Quy tắc hội thoại | Trả lời trước rồi mới hỏi; tối đa một câu hỏi; không xin số điện thoại sớm; thiếu trường nào hỏi trường đó; thông tin mới nhất thắng; nhiều câu hỏi trong một tin đều được trả lời; khách do dự không bị ép |
| Sản phẩm | Nhận đúng sản phẩm từ quảng cáo khách bấm vào; mã chính xác thắng đoán chữ; số lượng, giá không bị nhận nhầm là mã; kích thước phòng không bị nhận nhầm là kích thước sản phẩm; không có sản phẩm khớp thì nói không có |
| Giá | Mỗi quy tắc giá: dưới ngưỡng, đúng ngưỡng, giữa hai ngưỡng, trên ngưỡng cao nhất, ngưỡng miễn phí giao; khuyến mãi hết hạn không được báo |
| Chuyển người | Từng dòng trong bảng ngưỡng; sau khi chuyển trợ lý không chen vào |
| An toàn | Tin nhắn chèn chỉ dẫn lạ; khách hỏi "là người hay máy"; không lộ ghi chú nội bộ, đường dẫn, lỗi hệ thống |
| Ảnh | Hỏi chung gửi ảnh tổng hợp; hỏi đúng mã gửi đúng ảnh; không gửi trùng; ảnh lỗi không kèm tin báo lỗi kỹ thuật |
| Kỹ thuật (người phụ trách kỹ thuật làm) | Kênh nhận tin, xác thực đúng; tin trùng không trả lời hai lần; nhiều khách cùng lúc không lẫn lịch sử; mất kết nối có cảnh báo |

Chỉ bật khi mọi ca đạt. Ca nào chưa thử được ghi rõ "CHƯA THỬ" trong biên bản, người duyệt quyết có bật hay không.
