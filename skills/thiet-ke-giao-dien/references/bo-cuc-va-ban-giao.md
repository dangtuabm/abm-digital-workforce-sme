# BỐ CỤC, BIỂU MẪU VÀ BÀN GIAO THIẾT KẾ

## Mục lục
1. Luồng chính theo loại website/app
2. Khung sườn mẫu
3. Biểu mẫu tốt
4. Quy chuẩn giao diện tối thiểu
5. Đặc tả bàn giao cho người lập trình
6. Thử với người dùng
7. Thiết kế lừa cần tránh

## 1. Luồng chính theo loại website/app

| Loại | Việc chính của khách | Luồng gọn gợi ý |
|---|---|---|
| Website giới thiệu doanh nghiệp (sản xuất, phân phối, xây dựng) | Tin được công ty, liên hệ báo giá | Trang chủ → Sản phẩm/Năng lực → Dự án tiêu biểu → Liên hệ/Yêu cầu báo giá |
| Cửa hàng online | Tìm hàng, mua | Trang chủ/Danh mục → Lọc → Chi tiết sản phẩm → Giỏ → Thông tin nhận hàng → Xác nhận |
| Landing page thu khách | Hiểu ưu đãi, để lại thông tin | Một trang: lợi ích → bằng chứng → form ngắn → trang cảm ơn |
| Nhà hàng, cà phê, spa | Xem thực đơn/dịch vụ, đặt chỗ, chỉ đường | Trang chủ → Thực đơn/Dịch vụ → Đặt chỗ → Xác nhận; nút Gọi, Chỉ đường luôn hiện |
| App đặt lịch, tra cứu đơn | Đặt/tra nhanh | Chọn dịch vụ → Chọn giờ → Thông tin → Xác nhận; Tra cứu: nhập mã → kết quả |
| Biểu mẫu nội bộ (đề nghị, báo cáo) | Điền nhanh, ít sai | Chia nhóm trường, điền sẵn thứ đã biết, xác nhận trước khi gửi |

Mỗi luồng ghi: điểm vào, các bước, chỗ có thể bỏ dở, bước có thể bỏ. Mục tiêu: **bớt một bước là bớt một chỗ khách rời đi**.

## 2. Khung sườn mẫu (vẽ ở 375px trước)

Trang chủ website doanh nghiệp, từ trên xuống:
1. Thanh đầu: logo (bấm về trang chủ), menu gọn, nút hành động chính.
2. Khối mở đầu: một câu nói rõ làm gì cho ai [ô chờ nội dung], một nút chính, một nút phụ.
3. Bằng chứng tin cậy: khách hàng, số năm, chứng nhận [ô chờ nội dung có nguồn].
4. Sản phẩm/dịch vụ chính: 3–6 thẻ, mỗi thẻ một ảnh [ô chờ ảnh], tên, một dòng, nút xem.
5. Cách làm việc / quy trình: 3–4 bước.
6. Câu hỏi thường gặp.
7. Khối liên hệ: nút gọi, nhắn, form ngắn, bản đồ.
8. Chân trang: địa chỉ, giờ mở cửa, chính sách.

Ô chờ nội dung ghi: mục đích (khối này để khách hiểu điều gì), độ dài gợi ý, kích thước ảnh và tỷ lệ khung. Không viết nội dung thật.

## 3. Biểu mẫu tốt

- **Chỉ hỏi cái cần cho bước tiếp theo.** Form thu khách thường chỉ cần tên, số điện thoại, nhu cầu. Mỗi trường thêm phải có lý do.
- Một cột, nhãn nằm trên ô, nhãn hiện rõ.
- Đánh dấu trường không bắt buộc (thay vì đánh dấu sao khắp nơi).
- Đúng loại ô: chọn ngày bằng lịch, chọn giờ bằng danh sách khung giờ, số điện thoại bàn phím số.
- Báo lỗi ngay cạnh ô, nói rõ cách sửa ("Số điện thoại cần 10 số"), giữ lại dữ liệu đã nhập.
- Nút gửi ghi đúng việc ("Đặt lịch", "Nhận báo giá"), có trạng thái đang gửi, gửi xong chuyển trang cảm ơn nói bước tiếp theo.
- Form thu dữ liệu cá nhân có chỗ cho câu xin đồng ý và đường dẫn chính sách (câu chữ do người có chuyên môn duyệt); ô đồng ý **không tích sẵn**.
- Form dài (hồ sơ, đăng ký đại lý): chia bước, có thanh tiến độ, lưu nháp.

## 4. Quy chuẩn giao diện tối thiểu

| Thành phần | Cần chốt |
|---|---|
| Màu | Màu chính, màu phụ, màu nền, màu chữ, màu báo thành công/cảnh báo/lỗi — có mã màu; đã kiểm tương phản |
| Kiểu chữ | 1–2 kiểu chữ hỗ trợ đủ dấu tiếng Việt; cỡ tiêu đề cấp 1–3, thân bài, chú thích cho điện thoại và máy tính |
| Khoảng cách | Một thang khoảng cách cố định (ví dụ bội số của 4 hoặc 8px) dùng cho mọi trang |
| Nút | Nút chính, nút phụ, nút chữ; trạng thái bình thường, rê chuột, đang bấm, vô hiệu, đang tải; vùng bấm khoảng 44px |
| Ô nhập | Nhãn, gợi ý, đang chọn, lỗi, vô hiệu |
| Thẻ, bảng, biểu tượng | Bo góc, bóng, cỡ biểu tượng, nguồn biểu tượng có quyền dùng |
| Lưới | Số cột, lề hai bên ở 1440/375/320px |

Màu và kiểu chữ lấy từ quy chuẩn thương hiệu của doanh nghiệp. Chưa có → bảng trung tính tạm, gắn [GIẢ ĐỊNH].

## 5. Đặc tả bàn giao cho người lập trình

Gói bàn giao phải đủ để người lập trình làm mà không đoán. Khớp các mục người lập trình sẽ kiểm:

| Mục | Nội dung |
|---|---|
| Danh sách trang/màn hình | Tên, mục đích, đường dẫn dự kiến |
| Luồng người dùng | Các bước, điều kiện rẽ nhánh |
| Khổ màn hình | Khung sườn và mẫu ở **1440, 375, 320px**; ghi cách khối xếp lại khi hẹp |
| Quy chuẩn giao diện | Bảng mục 4, có mã màu, cỡ chữ, khoảng cách |
| Trạng thái | Đang tải, trống, lỗi, thành công cho từng màn hình có dữ liệu |
| Ô chờ nội dung và ảnh | Vị trí, mục đích, độ dài, kích thước ảnh — để bộ phận nội dung làm; ô chờ không được hiện ở bản thật |
| Trường form đề xuất | Tên trường, loại ô, bắt buộc hay không, kiểm tra hợp lệ, câu báo lỗi — người lập trình và bộ phận bán hàng xác nhận trong danh sách trường form của họ |
| Tiêu chí chấp nhận | Không tràn ngang; vùng bấm khoảng 44px; tương phản đạt; nhãn ô nhập hiện rõ; báo lỗi không chỉ bằng màu |
| Giới hạn đã biết | Phần chưa thử với người dùng, phần phụ thuộc nền tảng, phần [GIẢ ĐỊNH] |

Bản mẫu HTML tĩnh (nếu có) ghi rõ: chỉ để xem và duyệt, không phải mã đưa lên.

## 6. Thử với người dùng

- Mời 3–5 người đúng đối tượng (khách quen, nhân viên tuyến đầu đóng vai khách mới, người thân đúng độ tuổi khách). Nielsen khuyến nghị thử nhóm nhỏ, lặp nhiều vòng, thay vì một lần với nhóm lớn.
- Giao việc thật, không hướng dẫn: "Anh/Chị đặt giúp một bàn 4 người tối thứ Sáu".
- Quan sát, ghi chỗ họ dừng, đoán, bấm nhầm, hỏi. Không giải thích giúp.
- Tổng hợp: việc nào làm được/không làm được, mất bao lâu, chỗ kẹt chung. Sửa và thử vòng sau.
- Không ghi âm, quay màn hình khi người thử chưa đồng ý; không thu thông tin cá nhân của người thử ngoài tên gọi.

## 7. Thiết kế lừa cần tránh

| Thủ thuật | Vì sao tránh | Cách trung thực thay thế |
|---|---|---|
| Đếm ngược giả, "chỉ còn 1" khi không đúng | Lừa khách, mất uy tín khi bị phát hiện | Chỉ hiện hạn và số lượng thật |
| Ô đồng ý nhận tin, mua thêm tích sẵn | Khách không chủ động đồng ý | Để trống, khách tự chọn |
| Nút hủy, từ chối giấu, mờ, chữ khó hiểu | Ép khách | Hai lựa chọn rõ ngang nhau |
| Phí ẩn đến bước cuối | Khách bỏ giỏ, khiếu nại | Hiện tổng phí sớm |
| Khó hủy đăng ký hơn đăng ký | Khách bực, đánh giá xấu | Hủy dễ như đăng ký |

*[A.I Generated — Claude Code — 30/10/2026]*
