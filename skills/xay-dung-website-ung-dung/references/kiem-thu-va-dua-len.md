# KIỂM THỬ, BẢN XEM TRƯỚC, ĐƯA LÊN VÀ QUAY LUI

**Mục lục:** 1. Danh mục kiểm thử · 2. Bản xem trước · 3. Đưa lên môi trường thật và gắn tên miền · 4. Bẫy thường gặp · 5. Quay lui

## 1. Danh mục kiểm thử (Bước 6)

| Nhóm | Kiểm gì | Cách kiểm |
|---|---|---|
| Hiển thị | Không tràn ngang, không chữ bị ép, ngắt dòng ổn ở 1440/375/320 | Chạy trên máy qua máy chủ thử, dán `scripts/kiem-thu-giao-dien.js` vào bảng điều khiển, gọi `await window.__kiemThuGiaoDien([...danh sách trang], [1440, 375, 320])` |
| Bằng mắt | Trang chủ và mỗi loại trang trên máy tính và điện thoại thật | Người hoặc A.I xem ảnh chụp màn hình |
| Lỗi chạy | Bảng điều khiển trình duyệt không có lỗi đỏ | DevTools |
| Liên kết | Không liên kết hỏng, nút gọi điện/Zalo đúng số | Bấm thử, công cụ kiểm liên kết |
| Form | ≥ 3 bản ghi dữ liệu thử về đúng nơi nhận, đúng cột; báo thành công/thất bại; trang cảm ơn; chống thư rác chặn được bản gửi máy | Gửi thử bằng dữ liệu thử ("Nguyễn Văn Thử", số điện thoại thử), xóa sau khi kiểm |
| Bảo mật | Không mật khẩu, khóa kết nối, đường dẫn bí mật trong mã phía trình duyệt và kho mã | Tìm các chữ "password", "key", "token", "secret" trong mã |
| Tốc độ | Trang chủ tải nhanh trên mạng điện thoại; ảnh đúng cỡ | Công cụ đo tốc độ trong DevTools |
| Truy cập | Vùng bấm đủ lớn, chữ đủ tương phản, ảnh có chữ thay thế | Xem trên điện thoại, công cụ kiểm tương phản |
| App nhỏ | Mỗi chức năng với dữ liệu thử: trường hợp đúng, thiếu, sai, quá dài; quyền người dùng | Bảng ca kiểm thử trong biên bản |

Một lỗi sửa 3 vòng chưa xong: dừng, ghi vào biên bản, báo người phụ trách.

## 2. Bản xem trước (Bước 7)

- Chỉ đưa lên nơi xem trước người phụ trách đã cho phép (ví dụ đường dẫn tạm của dịch vụ lưu trữ trang tĩnh).
- Chặn máy tìm kiếm lập chỉ mục (thẻ `noindex`, tệp robots).
- Form ở bản xem trước nối vào nơi nhận dữ liệu thử, không nối vào bảng dữ liệu khách thật.
- Gửi đường dẫn kèm danh sách cần người duyệt xem; ghi góp ý vào biên bản.

## 3. Đưa lên môi trường thật và gắn tên miền (Bước 8)

1. Lập phiếu xin duyệt (thay đổi, đã kiểm, rủi ro, cách quay lui). Chờ duyệt rõ.
2. Sao lưu bản đang chạy (mã + dữ liệu) nếu đang thay web cũ.
3. Build bản thật (bỏ chặn lập chỉ mục, ẩn ô chờ).
4. Người phụ trách tự đưa lên bằng tài khoản của mình (hoặc A.I làm nếu đã được cấp quyền đúng việc này; mật khẩu do người nhập).
5. Gắn tên miền: tên miền phụ (ví dụ `dangky.tenmien.vn`) dễ và an toàn hơn — chỉ thêm một bản ghi CNAME, không ảnh hưởng website và email đang chạy; tên miền chính cần trỏ toàn bộ, có thể ảnh hưởng email — chỉ làm khi người quản trị đồng ý. Thay đổi DNS có thể mất từ vài phút đến vài giờ mới có hiệu lực.
6. Kiểm lại trên tên miền thật: trang chính, form (một bản ghi thử rồi xóa), ảnh chia sẻ khi gửi link (thêm `?v=2` để làm mới bộ nhớ đệm của Zalo/Facebook).
7. Đổi đường dẫn cũ: đặt chuyển hướng 301 để không mất khách từ link cũ.

## 4. Bẫy thường gặp

- Mở file HTML trực tiếp trên ổ đĩa: video nhúng và một số chức năng bị chặn → luôn xem qua máy chủ thử trên máy.
- Trang tĩnh gửi form thẳng về Google Apps Script bị trình duyệt chặn (lỗi CORS): đừng thử lại nhiều vòng; đổi sang cầu nối qua Google Form (gửi ngầm, kiểm đúng mã trường của form thật) hoặc một hàm máy chủ nhỏ.
- Ô lưới thiếu `min-width: 0` làm ảnh đẩy rộng cột → tràn ngang trên điện thoại.
- Đặt `height: 100%` cùng `aspect-ratio` làm ảnh tính ngược chiều rộng → dùng `width: 100%`.
- Kho mã riêng tư gói miễn phí có thể không chạy được trang xem trước → dùng kho xem trước riêng chỉ chứa bản đã build, mã nguồn vẫn giữ riêng tư.
- Ảnh, nội dung gửi qua chat giữa chừng có thể không được lưu ra file → xin lại bản gốc.

## 5. Quay lui

- Luôn giữ bản đang chạy trước lần đưa lên gần nhất.
- Lỗi nặng trên web thật (trang trắng, form không nhận): báo người phụ trách, đề xuất quay về bản trước, rồi sửa trên bản sao.
- Ghi lại sự cố và nguyên nhân vào Sổ bài học.

*[A.I Generated — Claude Code — 30/10/2026]*
