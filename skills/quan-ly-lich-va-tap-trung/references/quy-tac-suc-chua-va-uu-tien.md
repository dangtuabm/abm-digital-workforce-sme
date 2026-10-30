# QUY TẮC SỨC CHỨA, ƯU TIÊN VÀ GIÁN ĐOẠN

## 1. Tính sức chứa

**Sức chứa tập trung = Giờ làm việc − Việc cố định − Nghỉ − Dự phòng** (tính bằng phút).

| Thành phần | Gồm | Mặc định khi người dùng chưa nói [GIẢ ĐỊNH] |
|---|---|---|
| Giờ làm việc | Giờ thật sự có mặt làm việc trong khoảng thời gian | 8 giờ/ngày |
| Việc cố định | Họp đã chốt, giao ban, gặp khách, di chuyển | Lấy từ lịch |
| Nghỉ | Ăn trưa, nghỉ giữa giờ | 60 phút/ngày |
| Dự phòng | Việc phát sinh, trễ giờ | 10–15% giờ làm việc |

- Mọi số không âm. Sức chứa âm nghĩa là lịch đã quá tải ngay cả trước khi xếp việc chính.
- Không tính trùng: một cuộc họp có trong lịch thì không cộng thêm vào sổ việc.
- Tổng thời lượng khối tập trung ≤ sức chứa.

Ví dụ (giám đốc một công ty phân phối vật liệu xây dựng, thứ Hai): làm việc 480 phút − họp giao ban và gặp đại lý 150 phút − nghỉ 60 − dự phòng 60 = **210 phút** tập trung. Người dùng đang muốn làm 3 việc tổng 300 phút → thiếu 90 phút, phải nhả việc.

## 2. Các cổng kiểm

| Cổng | ĐẠT khi | KHÔNG ĐẠT khi |
|---|---|---|
| Sức chứa | Tổng khối tập trung ≤ sức chứa | Quá tải hoặc số âm |
| Việc làm dở | Số việc ĐANG LÀM ≤ giới hạn (mặc định 3) | Mở thêm việc mà không nhả việc nào |
| Mục tiêu | Mỗi khối nối với một mục tiêu PHẢI XONG / NÊN XONG / HỖ TRỢ | "Bận" nhưng không ra kết quả nào |
| Người chịu trách nhiệm | Mỗi việc có người nhận | Đẩy việc sang người chưa nhận |
| Hạn | Nguồn và hạn khớp nhau | Tự đổi hạn |
| Nghỉ | Có nghỉ và dự phòng hợp lý | Hy sinh ngủ, nghỉ để lấp lịch |
| Gián đoạn | Có phân loại, người quyết, cách quay lại | Việc gì cũng "khẩn" |

## 3. Năm cách xử lý một cam kết

| Cách | Dùng khi | Cần ai đồng ý |
|---|---|---|
| **LÀM** | Nối thẳng mục tiêu chính, người dùng là người phù hợp nhất | Người dùng |
| **GIAO** | Người khác làm được ≥ 80% chất lượng, người dùng chỉ cần duyệt | Người dùng + người nhận việc |
| **HOÃN** | Không ảnh hưởng mục tiêu trong khoảng thời gian này | Người dùng + người đang chờ kết quả |
| **BỎ** | Không còn phục vụ mục tiêu nào | Người dùng + người đã giao việc |
| **XIN Ý KIẾN** | Vướng quyền, phụ thuộc người khác, hoặc cam kết với bên ngoài | Người có quyền quyết |

Mọi cách ngoài LÀM chỉ là **đề xuất** cho tới khi người có quyền đồng ý. Không dùng chữ "khẩn" để che việc ít giá trị.

Mức ưu tiên của cam kết: **PHẢI XONG** (không xong thì mục tiêu hỏng) · **NÊN XONG** (tạo khác biệt rõ) · **HỖ TRỢ** (giúp việc chính tốt hơn) · **CHƯA LÀM** (để sau khoảng thời gian này).

## 4. Phân loại gián đoạn

| Loại | Ví dụ | Xử lý |
|---|---|---|
| **KHẨN** | Sự cố an toàn, khách lớn dọa hủy đơn, hệ thống bán hàng ngừng | Được chen ngang ngay, qua điện thoại |
| **QUAN TRỌNG** | Đại lý cần duyệt chiết khấu trong ngày | Gom lại, xử lý ở khe giữa hai khối |
| **THƯỜNG** | Hỏi thông tin, xin tài liệu | Ghi vào danh sách chờ, trả lời cuối ngày |

Cách quay lại việc chính: ghi một dòng "đang dừng ở đâu" trước khi xử lý việc chen ngang; quay lại thì đọc dòng đó trước.

## 5. Lỗi hay gặp

- Lịch kín 100%, không còn dự phòng → chỉ một cuộc họp trễ là vỡ cả ngày.
- Việc gì cũng "ưu tiên số 1" → thực chất không có ưu tiên.
- Không giới hạn việc làm dở → mở 8 việc, xong 0 việc.
- Tự hoãn cam kết của người khác; giao việc mà người nhận chưa đồng ý; xóa việc cho "sạch danh sách".
- Lấy làm thêm giờ, thiếu ngủ làm sức chứa.
- Đo số giờ bận thay vì việc đã xong và chất lượng.

## 6. Chỉ số theo dõi (gợi ý)

Tỷ lệ khối tập trung làm được trọn · số lần dời lịch trong tuần · số việc chen ngang mỗi ngày · số lần cắt giờ nghỉ (mục tiêu: 0) · tuổi trung bình của việc đang làm dở.

*[A.I Generated — Claude Code — 30/10/2026]*
