# NGUYÊN TẮC RÀ SOÁT TRẢI NGHIỆM

## Mục lục
1. 10 nguyên tắc dễ dùng (Nielsen) với ví dụ SME
2. Thang mức nặng 0–4
3. Danh mục kiểm trên điện thoại
4. Danh mục tiếp cận tối thiểu (WCAG 2.2 mức AA)
5. Cách đi thử một luồng

## 1. 10 nguyên tắc dễ dùng

| # | Nguyên tắc | Hỏi gì khi rà | Lỗi hay gặp ở website/app SME |
|---|---|---|---|
| 1 | Cho biết đang xảy ra gì | Bấm xong có thấy phản hồi không? Đang tải có báo không? | Bấm "Gửi" không thấy gì, khách bấm 3 lần ra 3 đơn |
| 2 | Nói ngôn ngữ của khách | Chữ trên nút, menu có phải từ khách hay dùng? | Menu "Giải pháp", "Hệ sinh thái" khi khách tìm "Bảng giá" |
| 3 | Cho khách quyền quay lại, hủy | Có nút quay lại, sửa giỏ hàng, hủy lịch không? | Đặt lịch xong không sửa được giờ |
| 4 | Thống nhất | Cùng một việc có cùng cách gọi, cùng kiểu nút ở mọi trang? | Trang này nút xanh "Đặt ngay", trang khác nút đỏ "Mua" |
| 5 | Phòng lỗi trước | Có chặn nhập sai từ đầu không? | Ô ngày cho nhập tự do, khách gõ "thứ 7" |
| 6 | Nhìn thấy thay vì phải nhớ | Thông tin cần cho bước sau có hiện sẵn không? | Bước thanh toán không còn thấy tên món đã chọn |
| 7 | Linh hoạt cho người quen | Khách quen có lối tắt không? | Khách mua lại phải nhập lại toàn bộ địa chỉ |
| 8 | Gọn, chỉ giữ cái cần | Màn hình có thứ không giúp khách làm việc chính? | Trang chủ 6 băng chuyền ảnh, 4 cửa sổ bật lên |
| 9 | Báo lỗi dễ hiểu, chỉ cách sửa | Báo lỗi có nói sai ở đâu, sửa thế nào? | "Lỗi hệ thống 500", "Dữ liệu không hợp lệ" |
| 10 | Có trợ giúp khi cần | Có cách hỏi nhanh (gọi, nhắn) đúng lúc khách bối rối? | Số hotline chỉ có ở cuối trang, chữ nhỏ |

## 2. Thang mức nặng (Nielsen)

| Mức | Ý nghĩa | Xử lý |
|---|---|---|
| 0 | Không phải vấn đề | Bỏ |
| 1 | Thẩm mỹ, sửa khi rảnh | Gom vào đợt sau |
| 2 | Nhỏ, khách hơi chậm | Sửa trong đợt thường |
| 3 | Lớn, nhiều khách kẹt hoặc bỏ đi | Sửa sớm, ưu tiên cao |
| 4 | Thảm họa, khách không làm được việc chính | Sửa trước khi làm bất cứ gì khác |

Chấm mức nặng dựa trên: bao nhiêu khách gặp, có vượt qua được không, có lặp lại mỗi lần dùng không. Có số liệu truy cập (trang thoát nhiều, bước bỏ dở) thì ghi kèm làm bằng chứng.

## 3. Danh mục kiểm trên điện thoại (375px và 320px)

- [ ] Màn hình đầu tiên cho biết ngay: đây là gì, cho ai, làm gì tiếp.
- [ ] Nút hành động chính (Gọi, Nhắn, Đặt, Mua) thấy được không cần cuộn xa, nằm trong tầm ngón cái.
- [ ] Không tràn ngang, không phải phóng to mới đọc được; chữ thân bài khoảng 16px trở lên.
- [ ] Vùng bấm khoảng 44px, cách nhau đủ xa.
- [ ] Menu gọn; mở ra không che mất nút đóng.
- [ ] Cửa sổ bật lên không che toàn màn hình, đóng được dễ dàng.
- [ ] Ô nhập gọi đúng bàn phím (số điện thoại → bàn phím số, email → bàn phím có @).
- [ ] Số điện thoại bấm vào gọi được; địa chỉ bấm vào mở bản đồ.
- [ ] Bảng giá, bảng thông số đọc được trên màn hình nhỏ (xếp dọc hoặc cuộn trong khung).
- [ ] Trang tải lên thấy nội dung chính nhanh; ảnh không làm xô lệch bố cục khi tải.

## 4. Danh mục tiếp cận tối thiểu (WCAG 2.2 mức AA)

- [ ] Tương phản chữ với nền: chữ thường từ 4,5:1; chữ lớn từ 3:1; viền ô nhập, biểu tượng quan trọng từ 3:1.
- [ ] Không chỉ dùng màu để truyền thông tin (ô lỗi có cả chữ báo lỗi, không chỉ viền đỏ).
- [ ] Mỗi ô nhập có nhãn hiện rõ; chữ gợi ý mờ trong ô không thay được nhãn.
- [ ] Dùng được bằng bàn phím: đi qua các ô bằng phím Tab đúng thứ tự, thấy rõ ô đang chọn.
- [ ] Ảnh có ý nghĩa cần chữ mô tả (ô chờ "mô tả ảnh" chuyển bộ phận nội dung viết).
- [ ] Phóng chữ lên 200% vẫn đọc và dùng được.
- [ ] Không có nội dung nhấp nháy nhanh; băng chuyền ảnh tự chạy có nút dừng.
- [ ] Mục tiêu bấm không quá nhỏ (WCAG 2.2 yêu cầu tối thiểu 24×24px ở mức AA; chuẩn nội bộ khuyến nghị khoảng 44px cho điện thoại).

Người lớn tuổi, người dùng điện thoại màn hình nhỏ, người đang dùng một tay ngoài đường đều hưởng lợi từ các mục trên, không chỉ người khuyết tật.

## 5. Cách đi thử một luồng

1. Chọn 1–3 việc chính khách đến để làm (ví dụ: tìm món và đặt bàn; xem giá và để lại số).
2. Đóng vai khách lần đầu vào, trên điện thoại, bắt đầu từ nơi khách thật hay vào (trang chủ, trang sản phẩm từ quảng cáo, Google Maps).
3. Ghi từng bước: bấm gì, thấy gì, chỗ nào phải đoán, chỗ nào phải quay lại.
4. Đếm số bước và số lần phải đoán. Chụp màn hình chỗ kẹt (che dữ liệu khách thật nếu có).
5. Lặp lại trên máy tính 1440px.
6. Ghi vào bảng rà: vị trí, nguyên tắc, mức nặng, đề xuất, việc cần chuyển (giao diện / nội dung / lập trình).

*[A.I Generated — Claude Code — 30/10/2026]*
