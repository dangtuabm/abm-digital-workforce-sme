# THIẾT KẾ CHUỖI CHĂM SÓC

## Mục lục
- I. Khung chuỗi theo tệp khách
- II. Nhịp gửi và tỷ lệ giá trị / mời mua
- III. Cấu trúc một tin
- IV. Phân nhánh theo hành vi
- V. Chỉ số theo dõi và cách lập mốc
- VI. Lỗi hay gặp
- VII. Ví dụ ngắn

Đọc ở Bước 3–5 và Bước 10. Số tin, nhịp gửi dưới đây là gợi ý khởi điểm; doanh nghiệp chỉnh theo kết quả thật của mình.

## I. KHUNG CHUỖI THEO TỆP KHÁCH

| Tệp | Ví dụ | Số tin gợi ý | Đích cuối thường gặp |
|---|---|---|---|
| Khách mới để lại thông tin | Đăng ký nhận báo giá, tải tài liệu, ghé gian hàng hội chợ | 5–7 | Đặt lịch tư vấn, nhận báo giá |
| Khách đang cân nhắc | Đã nhận báo giá, đã hỏi kỹ nhưng chưa quyết | 4–6 | Mua, đặt cọc, thăm xưởng/cửa hàng |
| Khách nguội | Để lại thông tin lâu, không mở tin gần đây | 3–4 | Khách xác nhận còn quan tâm hay không |
| Khách cũ cần mua lại (A23) | Đã mua, tới chu kỳ dùng hết, lâu chưa quay lại | 3–5 | Mua lại, mua sản phẩm đi kèm |
| Ra mắt sản phẩm mới | Khách đã quan tâm dòng sản phẩm liên quan | 4–6 | Đặt trước, mua trong đợt ra mắt |

Chuỗi dài nhất khoảng 12 tin. Hết chuỗi mà khách không phản hồi: chuyển sang tệp khách nguội hoặc dừng, không gửi vô hạn.

## II. NHỊP GỬI VÀ TỶ LỆ GIÁ TRỊ / MỜI MUA

- Khách nóng (vừa để lại thông tin, đang cân nhắc): cách 2–3 ngày.
- Khách nguội, khách cũ: cách khoảng 1 tuần.
- Trần tần suất do doanh nghiệp đặt (ví dụ: một người không nhận quá [số] tin mỗi tuần từ tất cả các chuỗi cộng lại).
- **Tỷ lệ gợi ý 80% giá trị / 20% mời mua — đếm thật trên sơ đồ.** Tin giá trị: mẹo dùng, cách chọn, câu chuyện khách thật đã đồng ý, giải đáp băn khoăn thường gặp, so sánh khách quan. Tin mời mua: ưu đãi đã duyệt, lời mời đặt lịch.

## III. CẤU TRÚC MỘT TIN

1. **Móc:** một câu chạm đúng mối bận tâm của tệp (không giật tít).
2. **Giá trị:** nội dung chính, cụ thể, đọc được trong một phút.
3. **Chuyển ý:** nối từ giá trị sang hành động.
4. **Lời kêu gọi:** một hành động duy nhất (một nút hoặc một câu).

Email:
- 2 phương án tiêu đề cho mỗi tin (ngắn / dạng câu hỏi, hoặc nêu lợi ích / gợi tò mò), tối đa khoảng 50 ký tự.
- Đoạn xem trước bổ sung ý cho tiêu đề, không lặp lại.
- Ưu tiên chữ, ảnh nhẹ; có chữ ký người gửi thật và cách từ chối nhận tin.

Zalo OA: ngắn hơn email, câu mở thay cho tiêu đề, đúng loại tin nền tảng cho phép (xem `kenh-email-va-zalo.md`).

Biến cá nhân hóa: `{ten}`, `{san_pham_quan_tam}`, `{ngay_mua_gan_nhat}`, `{nhan_vien_phu_trach}`. Thiếu dữ liệu biến → dùng câu thay thế đã soạn sẵn, không để lộ dấu ngoặc.

## IV. PHÂN NHÁNH THEO HÀNH VI

| Hành vi | Rẽ nhánh gợi ý |
|---|---|
| Mở nhưng không bấm | Tiếp tục chuỗi bình thường |
| Bấm vào nội dung sản phẩm, bảng giá | Gắn nhãn "quan tâm cao", rút ngắn nhịp hoặc chuyển nhân viên bán hàng gọi |
| Trả lời tin | Chuyển nhân viên bán hàng ngay, tạm dừng tin tự động cho người đó |
| Không mở 3 tin liên tiếp | Chuyển sang tệp khách nguội |
| Mua hàng | Ra khỏi chuỗi trước mua, vào chuỗi sau mua (nếu có) |
| Từ chối nhận tin | Dừng mọi chuỗi, mọi kênh; ghi danh sách từ chối |
| Phàn nàn | Tạm dừng chuỗi, chuyển xử lý khiếu nại |

## V. CHỈ SỐ THEO DÕI VÀ CÁCH LẬP MỐC

| Chỉ số | Cách tính |
|---|---|
| Tỷ lệ mở (email) | Số người mở / số tin gửi thành công |
| Tỷ lệ bấm | Số người bấm / số tin gửi thành công |
| Tỷ lệ trả lời | Số người trả lời / số tin gửi thành công |
| Tỷ lệ từ chối nhận tin | Số người từ chối / số tin gửi thành công |
| Tỷ lệ chuyển bán hàng | Số khách chuyển nhân viên bán hàng / số người trong chuỗi |
| Tỷ lệ đạt đích | Số khách đạt đích cuối / số người trong chuỗi |

- Không lấy "chuẩn ngành" không rõ nguồn làm mục tiêu. Chạy 2–3 đợt đầu để có **mốc của chính doanh nghiệp**, rồi đặt mục tiêu cải thiện so với mốc. Mục tiêu đặt trước khi có mốc phải gắn [GIẢ ĐỊNH].
- Số liệu lấy từ công cụ gửi; ghi kỳ đo và nguồn.
- Tỷ lệ từ chối hoặc báo rác tăng bất thường so với mốc: dừng, xem lại nội dung, tệp, nhịp.

## VI. LỖI HAY GẶP
- Tiêu đề giật tít nhưng nội dung không liên quan — mất tin tưởng.
- 3–5 lời kêu gọi trong một tin — người đọc không biết bấm gì.
- Một bản dán cho mọi tệp — không cá nhân hóa.
- Ảnh nặng — dễ vào hộp thư rác hoặc thư quảng cáo.
- Gửi tiếp cho người đã từ chối ở kênh khác.

## VII. VÍ DỤ NGẮN (công ty nội thất văn phòng, khách để lại thông tin ở hội chợ)

| Tin | Ngày | Kênh | Loại | Mục tiêu |
|---|---|---|---|---|
| 1 | Ngày 0 | Email | Giá trị | Cảm ơn ghé gian hàng, gửi tài liệu "5 lỗi bố trí văn phòng nhỏ" |
| 2 | Ngày 3 | Email | Giá trị | Cách tính số chỗ ngồi theo diện tích |
| 3 | Ngày 6 | Zalo OA | Giá trị | Ảnh thật văn phòng khách đã đồng ý chia sẻ |
| 4 | Ngày 10 | Email | Giá trị | Giải đáp băn khoăn về độ bền ghế xoay |
| 5 | Ngày 14 | Email | Mời mua | Mời đặt lịch khảo sát miễn phí (đã duyệt) |
