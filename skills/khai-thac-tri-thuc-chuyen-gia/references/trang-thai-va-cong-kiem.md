# TRẠNG THÁI VÀ CỔNG KIỂM

## 1. Trạng thái

| Trạng thái | Chế độ | Khi nào |
|---|---|---|
| CHƯA SẴN SÀNG | Cả hai | Thiếu phạm vi, mục đích, người dùng, người đóng góp/nguồn, quyền, nhãn dữ liệu, người duyệt hoặc ngưỡng đạt |
| BẢN NHÁP | Cả hai | Thỏa thuận đủ nhưng chưa có nguồn hoặc đơn vị/thành phần |
| CẦN SỬA | Cả hai | Nguồn hoặc đơn vị thiếu trường, mã nguồn đứt, thiếu loại/lớp bắt buộc, thiếu quyết định giữ – sửa – bỏ – thử |
| MỚI LÀ GIẢ THUYẾT | Cả hai | Số tình huống/bằng chứng khác nhau thấp hơn ngưỡng (không dưới 2 cho nhận định chung) |
| CHỜ CHUYÊN GIA XÁC NHẬN | Phỏng vấn | Còn đơn vị chưa được chuyên gia xác nhận |
| SẴN SÀNG KÈM RÀO CHẮN | Cả hai | Rủi ro cao, còn xung đột mở, bắt buộc có người duyệt chuyên môn |
| SẴN SÀNG THỬ CHUYỂN GIAO | Phỏng vấn | Quyền, nguồn, đơn vị, xác nhận đạt; đã lập bài thử |
| SẴN SÀNG THỬ ĐIỂM | Giải mã | Cổng kiểm đạt; chưa chứng minh được chuyển giao hay hiệu quả |
| ĐÃ KIỂM CHỨNG CHUYỂN GIAO | Phỏng vấn | Chỉ khi bài thử thật có kết quả ĐẠT và nguồn kết quả truy được |

A.I không tự chuyển sang ĐÃ KIỂM CHỨNG CHUYỂN GIAO. SẴN SÀNG THỬ ĐIỂM không có nghĩa cơ chế đúng hay kết quả sẽ lặp lại.

## 2. Quy tắc bằng chứng và quyền

- Mỗi đơn vị tri thức / thành phần có ít nhất một mã nguồn tồn tại trong sổ nguồn.
- Mỗi nguồn có mã tình huống, nơi lưu gốc, quyền, nhãn dữ liệu, phạm vi, giới hạn.
- Một tình huống chỉ sinh giả thuyết. Chuyên gia xác nhận không thay cho thử chuyển giao.
- Độ tin "cao" về nhân quả cần đủ số bằng chứng đã thỏa thuận và không có mã nguồn rỗng.
- Chỉ xử lý nguồn có quyền rõ (đã đồng ý hoặc công khai). Quyền "chưa rõ / bị từ chối / đã rút lại" là lỗi.
- Nhãn Xanh – Vàng – Đỏ quyết định ai được xem; không tự hạ nhãn.
- Có cách sửa và rút lại, có người phụ trách.

## 3. Bài thử chuyển giao (chế độ phỏng vấn)

- Tình huống thử phải **mới**, không trùng tình huống đã phỏng vấn.
- Thang chấm tối thiểu: chọn đúng tín hiệu và quy tắc · trình bày được lý do · nhận ra ngoại lệ và lúc phải chuyển cấp · đầu ra có bằng chứng.
- Ghi "ĐẠT" cần: ngưỡng đạt, người tham gia, người phụ trách, nguồn kết quả. Thiếu một trong các trường → hạ về CẦN SỬA.
- Thất bại: phân tích lỗi, sửa quy tắc/ngoại lệ/thang chấm, thử lại bằng tình huống mới khác.

## 4. Thử điểm (chế độ giải mã)

- Đủ: giả thuyết, số liệu nền, chỉ số dẫn và chỉ số kết quả, nguồn số liệu, ngưỡng đạt, ngưỡng dừng, thời gian xem lại, người phụ trách, cách quay lại.
- Rủi ro cao, chuyên gia chưa duyệt, rào chắn còn mở: không vượt SẴN SÀNG KÈM RÀO CHẮN.
- Giống nhau bề ngoài không thay cho khớp về cấu trúc và bối cảnh.

*[A.I Generated — Claude Code — 30/10/2026]*
