# QUY TẮC CẤP, THU HỒI QUYỀN VÀ RÀ TÀI KHOẢN

**Mục lục:** 1. Chặn mật khẩu và mã bí mật · 2. Quyền tối thiểu và ma trận theo vị trí · 3. Vào – nghỉ – đổi vị trí · 4. Bốn nhóm tài khoản thừa · 5. Rà định kỳ và gia hạn · 6. Ví dụ

## 1. Chặn mật khẩu và mã bí mật (Bước 2)
Mã bí mật gồm: mật khẩu, mã OTP, mã khôi phục, khóa khôi phục, mã xác thực hai lớp, câu hỏi bảo mật, mã PIN, khóa API.
- A.I không yêu cầu, không đọc, không chép, không lưu, không gửi các mã này.
- File đầu vào có cột hoặc dòng chứa mã bí mật: dừng xử lý file đó; báo người gửi xóa phần đó (hoặc xuất lại không có cột đó) và **đổi ngay** các mật khẩu đã lộ.
- Người dùng dán mật khẩu vào cuộc trò chuyện: không nhắc lại, không dùng; khuyên đổi mật khẩu đó.
- Sổ tài khoản chỉ ghi **nơi giữ** thông tin đăng nhập (trình quản lý mật khẩu của công ty, người quản trị giữ), không ghi giá trị.
- Đặt lại mật khẩu, mở khóa tài khoản: người quản trị làm sau khi xác minh đúng người qua kênh doanh nghiệp quy định.

## 2. Quyền tối thiểu và ma trận theo vị trí
- Mỗi vị trí có một bộ quyền chuẩn: phần mềm nào, mức nào (xem / sửa / quản trị), thư mục nào, nhóm chat nào.
- Quyền quản trị chỉ cấp cho người quản trị hệ thống và người dự phòng; mỗi hệ thống quan trọng có **ít nhất hai** người quản trị để không phụ thuộc một người.
- Tài khoản quản trị chính của dịch vụ (email doanh nghiệp, tên miền, Drive/OneDrive, fanpage, Zalo OA, tài khoản quảng cáo) **đứng tên doanh nghiệp**, dùng email chung của công ty, không dùng email cá nhân.
- Bật xác thực hai lớp cho mọi tài khoản quản trị và tài khoản có dữ liệu Vàng/Đỏ.
- Quyền tạm thời (dự án, thời vụ) ghi ngày hết hạn ngay khi cấp.
- Trưởng bộ phận chốt ma trận; quyền vượt ma trận cần lãnh đạo duyệt.

## 3. Vào – nghỉ – đổi vị trí

### Nhân viên mới vào
1. Nhận thông tin từ nhân sự: họ tên, vị trí, bộ phận, ngày bắt đầu (trước ngày vào).
2. Lấy bộ quyền chuẩn theo vị trí; trưởng bộ phận xác nhận thêm, bớt.
3. Người quản trị tạo tài khoản đứng tên công ty, bật xác thực hai lớp, cấp quyền tối thiểu, cấp thiết bị đạt chuẩn.
4. Nhân viên đọc và xác nhận quy định sử dụng tài khoản, thiết bị, A.I của công ty.
5. Rà lại sau thời gian thử việc: bỏ quyền không dùng.

### Nhân viên nghỉ việc — thứ tự ưu tiên
| Ưu tiên | Việc | Hạn gợi ý |
|---|---|---|
| 1 | Khóa đăng nhập email doanh nghiệp, lưu trữ đám mây, phần mềm có dữ liệu Đỏ (kế toán, CRM, lương); thu hồi các phiên đăng nhập trên mọi thiết bị | Cuối ngày làm việc cuối cùng (nghỉ đột ngột: ngay khi có quyết định) |
| 1 | Gỡ quyền quản trị fanpage, Zalo OA, tài khoản quảng cáo, tên miền; gỡ khỏi nhóm chat công việc | Cùng thời điểm |
| 1 | Kế toán trưởng, lãnh đạo xử lý ngân hàng điện tử, chữ ký số, ủy quyền, tài khoản cổng nhà nước người đó đang giữ | Cùng thời điểm |
| 2 | Người quản trị đổi mật khẩu các tài khoản dùng chung người đó từng biết | Trong ngày |
| 2 | Chuyển sở hữu file, thư mục, lịch, nhóm sang người nhận bàn giao; thiết lập chuyển tiếp hoặc trả lời tự động cho email theo chính sách | Trước khi xóa giấy phép sử dụng |
| 3 | Thu thiết bị, thẻ ra vào, chìa khóa; kiểm máy trước khi cấp lại cho người khác (sao lưu dữ liệu công việc, cài lại) | Ngày làm việc cuối |
| 3 | Thông báo khách hàng, nhà cung cấp về đầu mối mới nếu cần (người phụ trách gửi) | Theo kế hoạch bàn giao |
| 4 | Giải phóng ghế bản quyền sau thời gian giữ dữ liệu theo chính sách; ghi vào sổ | Theo chính sách lưu giữ |

Không xóa hộp thư, file của người nghỉ ngay; giữ theo chính sách lưu giữ của doanh nghiệp (thời gian giữ do lãnh đạo chọn, cần người có chuyên môn xác nhận nếu liên quan quy định).

### Đổi vị trí
Thu quyền của vị trí cũ **trước**, cấp quyền vị trí mới **sau**; tránh tích lũy quyền qua nhiều lần chuyển.

## 4. Bốn nhóm tài khoản thừa (Bước 4)
| Nhóm | Cách phát hiện | Đề xuất |
|---|---|---|
| Người đã nghỉ còn hoạt động | Đối chiếu danh sách người dùng với danh sách nhân sự đã nghỉ | Thu hồi theo mục 3 — ưu tiên cao nhất |
| Ghế không dùng | Lần đăng nhập gần nhất quá lâu (doanh nghiệp chọn số ngày; chưa chọn thì 90 ngày, [GIẢ ĐỊNH]) | Hỏi trưởng bộ phận; đưa vào rà gia hạn |
| Tài khoản dùng chung | Một tài khoản, nhiều người dùng (kế toán chung, bán hàng chung) | Tách tài khoản riêng hoặc quản lý qua trình quản lý mật khẩu; đổi mật khẩu khi có người rời nhóm |
| Đứng tên cá nhân giữ dữ liệu công ty | Tài khoản dịch vụ đăng ký bằng email, số điện thoại cá nhân | Chuyển sang tài khoản công ty; lãnh đạo duyệt |

Danh sách này là **đề xuất**. Người quản trị kiểm lại từng dòng trước khi thu hồi.

## 5. Rà định kỳ và gia hạn
- Rà quyền hằng quý (gợi ý; doanh nghiệp chọn): trưởng bộ phận xác nhận danh sách người dùng của bộ phận mình.
- Mỗi phần mềm, tên miền, chứng chỉ, dịch vụ lưu trữ có ngày gia hạn, người theo dõi, ngày nhắc.
- Trước kỳ gia hạn, gửi kèm: số ghế mua – số ghế đang dùng, danh sách ghế không dùng → chuyển việc chọn phần mềm để lãnh đạo quyết giữ – gộp – bỏ – thay. Thanh toán do kế toán làm theo duyệt chi.
- Tên miền, chứng chỉ bảo mật website hết hạn có thể làm dừng website, email: nhắc sớm hơn và nhắc cả người dự phòng.

## 6. Ví dụ (công ty thương mại 35 người)
"[DỮ KIỆN] Đối chiếu danh sách người dùng email doanh nghiệp xuất ngày 28/10 với danh sách nhân sự: 3 tài khoản của người đã nghỉ còn hoạt động (nghỉ từ tháng 6, tháng 8, tháng 9), 5 ghế không đăng nhập hơn 90 ngày [GIẢ ĐỊNH ngưỡng], tài khoản quản trị fanpage đứng tên email cá nhân của nhân viên marketing cũ. Việc gấp: người quản trị khóa 3 tài khoản và gỡ quyền fanpage trong hôm nay — checklist đính kèm."

*[A.I Generated — Claude Code — 30/10/2026]*
