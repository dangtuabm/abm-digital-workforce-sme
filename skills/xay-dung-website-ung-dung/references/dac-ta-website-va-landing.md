# ĐẶC TẢ WEBSITE DOANH NGHIỆP VÀ LANDING THU KHÁCH

**Mục lục:** 1. Website doanh nghiệp: mục tiêu · 2. Bản đồ trang mẫu · 3. Thứ tự khối trang chủ · 4. Landing thu khách: cấu trúc 7 khối · 5. Form thu khách · 6. Chuẩn nội dung khi lập trình · 7. Chuẩn hình ảnh khi lập trình · 8. Chữ tiếng Việt và ngắt dòng · 9. Kỹ thuật tối thiểu

> Phần giao diện (màu, kiểu chữ, bố cục chi tiết) theo bản thiết kế đã duyệt. Tài liệu này chỉ nêu khung để lập trình và những lỗi phải tránh.

## 1. Website doanh nghiệp: mục tiêu

Trong 5 giây khách hiểu doanh nghiệp là ai, phục vụ ai; trong 1 phút thấy bằng chứng (khách hàng, hình ảnh thật, chứng nhận); lúc nào cũng có lối đi tiếp (gọi điện, nhắn Zalo OA, để lại thông tin).

## 2. Bản đồ trang mẫu (doanh nghiệp chọn, thêm, bớt)

| Nhóm menu | Trang | Ghi chú |
|---|---|---|
| Giới thiệu | Về chúng tôi · Đội ngũ · Năng lực, chứng nhận | Chỉ đăng chứng nhận còn hiệu lực |
| Sản phẩm – Dịch vụ | Trang tổng + mỗi nhóm sản phẩm một trang | Lấy từ Bảng sản phẩm của doanh nghiệp |
| Khách hàng – Dự án | Danh sách khách hàng/dự án tiêu biểu | Chỉ đơn vị đã đồng ý cho dùng tên, logo |
| Tin tức | Bài viết, thông báo | Có ngày đăng, có nguồn nếu dẫn số liệu |
| Tuyển dụng | Vị trí đang tuyển + form ứng tuyển | Dữ liệu ứng viên là dữ liệu Vàng |
| Liên hệ | Form + địa chỉ + bản đồ + giờ làm việc | |

## 3. Thứ tự khối trang chủ (gợi ý)

1. Đầu trang: doanh nghiệp làm gì, cho ai; 1–2 nút hành động.
2. Dải logo khách hàng (đã được phép).
3. Sản phẩm, dịch vụ chính theo nhóm khách.
4. Vì sao chọn: 3–6 lý do có bằng chứng.
5. Hình ảnh hoạt động thật, có chú thích.
6. Khách hàng nói gì (chỉ lời khen có thật, có đồng ý).
7. Câu hỏi thường gặp.
8. Lời mời + form liên hệ.
Xen khối nhiều ảnh với khối chỉ chữ; trên điện thoại, nhóm thẻ dài chuyển sang vuốt ngang.

## 4. Landing thu khách: cấu trúc 7 khối

1. Đầu trang: lợi ích chính, câu dẫn, nút đăng ký, hình chính.
2. Vấn đề khách đang gặp.
3. Giải pháp / ưu đãi.
4. Lợi ích (3–6 ý dễ quét mắt).
5. Bằng chứng: khách hàng, số liệu có nguồn.
6. Câu hỏi thường gặp ngắn.
7. Form + nút hành động cuối; nút đăng ký xuất hiện ở đầu, giữa và cuối trang.

Lưu ý khi lập trình: không để cả trang cùng một nền đặc; hộp chứa chữ trên nền đậm phải đổi sang màu tương phản; ảnh ngang trên điện thoại không được cắt mất nút; không đưa ghi chú vận hành nội bộ ra chữ hiển thị.

## 5. Form thu khách

- Chỉ các trường thật sự cần (thường: họ tên, số điện thoại, nhu cầu). Mỗi trường thêm vào phải có lý do trong danh sách trường form.
- Kiểm tra định dạng ở trình duyệt (số điện thoại, email) và kiểm lại ở nơi nhận nếu có máy chủ.
- Câu xin đồng ý xử lý dữ liệu cá nhân, liên kết tới chính sách của doanh nghiệp (nội dung do pháp chế duyệt).
- Chống thư rác: trường ẩn bẫy máy (honeypot), giới hạn số lần gửi.
- Sau khi gửi: chuyển về trang cảm ơn của chính landing, giữ nhận diện, gợi ý bước tiếp (nhắn Zalo OA, lưu lịch) — không đẩy người dùng sang trang biểu mẫu thô.
- Nơi nhận: Google Sheet, phần mềm CRM, email nội bộ — **cần kết nối**; chỉ nơi đã được duyệt, chỉ người được duyệt xem.

## 6. Chuẩn nội dung khi lập trình

- Chỉ đưa lên nội dung đã duyệt. Thiếu nội dung → ô chờ, tự ẩn ở bản thật.
- Không bịa số liệu, khách hàng, giá, lời chứng thực, trích dẫn.
- Không để ghi chú nội bộ ("chờ anh duyệt", "kiểm lại ngày") thành chữ hiển thị.
- Web công khai xưng hô theo quy chuẩn thương hiệu của doanh nghiệp (thường "Quý khách", "Anh/Chị").

## 7. Chuẩn hình ảnh khi lập trình

- Dùng ảnh đã được duyệt và có quyền dùng; mỗi ảnh có chữ thay thế (alt) mô tả ngắn.
- Ảnh thu nhỏ đúng kích cỡ hiển thị, định dạng nén tốt (WebP/JPG), tải chậm cho ảnh dưới màn hình đầu.
- Logo khách hàng: chỉ bản nét do bộ phận nội dung cung cấp; không tự vẽ, ghép logo.
- Video: chỉ tải ảnh bìa, bấm mới nhúng video; tỉ lệ 16:9 thống nhất.

## 8. Chữ tiếng Việt và ngắt dòng

- Không để từ ghép bị tách đôi ở cuối dòng tiêu đề ("doanh / nghiệp"); dùng dấu cách không ngắt cho cụm ngắn quan trọng, hoặc ngắt dòng chủ động theo nhịp nghĩa.
- Tiêu đề dùng `text-wrap: balance`, đoạn văn dùng `text-wrap: pretty`.
- Không để dấu — · & đứng đầu dòng.
- Kiểm bằng `scripts/kiem-thu-giao-dien.js` (lỗi MOCOI, DAU).

## 9. Kỹ thuật tối thiểu

- Ưu tiên trang tĩnh (nhanh, rẻ, ít lỗ hổng); chỉ dùng máy chủ khi cần lưu dữ liệu hoặc xử lý.
- Hai chế độ build nếu công cụ hỗ trợ: bản xem trước (chặn lập chỉ mục, hiện ô chờ) và bản thật.
- Có sơ đồ trang (sitemap), tiêu đề và mô tả từng trang, ảnh chia sẻ khi gửi link qua Zalo/Facebook.
- Tôn trọng chế độ "giảm chuyển động" của người dùng; vùng bấm khoảng 44px trên điện thoại.

*[A.I Generated — Claude Code — 30/10/2026]*
