# QUY TẮC QUYẾT ĐỊNH VÒNG CẢI TIẾN

## 1. Cổng số liệu nền

- Vấn đề, chỉ số, định nghĩa, cách đo, người phụ trách và phiên bản quy trình phải khóa.
- Số liệu nền lấy **nhiều kỳ** (ví dụ 6–8 tuần), không lấy một điểm. Kiểm: có xu hướng tăng/giảm sẵn không, có mùa vụ không (Tết, mùa mưa, mùa khai trường), cơ cấu đơn hàng có đổi không, có thay đổi nào khác đang chạy không.
- Kiểm cách đo: hai người đếm cùng một lô có ra cùng số không; phần mềm có ghi thiếu không.
- Nền không ổn định hoặc cách đo không đáng tin: **CHƯA SẴN SÀNG**. Không gán mọi biến động cho thay đổi.

## 2. Cổng trước khi thử

- Giả thuyết có cơ chế, dự đoán, điều kiện bác bỏ ("sau đủ 4 tuần mà không giảm thì giả thuyết sai") và ít nhất một giải thích khác.
- Thay đổi có phạm vi nhỏ, cách đối chứng (nhóm giữ cách cũ cùng thời gian là tốt nhất; so trước–sau chỉ khi điều kiện giống nhau), cỡ mẫu, thời gian, chỉ số chính và ngưỡng, chỉ số cảnh báo và ngưỡng, ngưỡng dừng, cách quay lại, người duyệt.
- **Chỉ số cảnh báo** là chỉ số theo dõi tác dụng phụ: giảm lỗi nhưng tăng thời gian? giảm thời gian nhưng tăng khiếu nại? tiết kiệm chi phí nhưng ảnh hưởng an toàn?
- Mỗi lần thử **một** thay đổi. Nhiều thay đổi cùng lúc thì không biết cái nào có tác dụng.
- Thiếu đối chứng, chỉ số cảnh báo hoặc cách quay lại: không chạy.

## 3. Trạng thái sau khi đo

| Trạng thái | Khi nào | Ai chốt |
|---|---|---|
| ĐỀ XUẤT ÁP DỤNG | Chỉ số chính đạt ngưỡng; không chỉ số cảnh báo nào vi phạm; đủ thời gian; mức cải thiện đủ ý nghĩa thực tế | Người có quyền duyệt thành ĐÃ ÁP DỤNG |
| LÀM VÒNG MỚI | Có tín hiệu hữu ích nhưng giả thuyết, thay đổi hoặc cách đo cần sửa; giữ phiên bản và bài học | Người phụ trách |
| LOẠI BỎ | Bằng chứng bác bỏ giả thuyết, hoặc lợi ích không đủ điều kiện áp dụng | Người phụ trách |
| QUAY LẠI CÁCH CŨ | Chỉ số cảnh báo, ngưỡng dừng bị vi phạm, hoặc thiệt hại vượt mức chịu được | Người có quyền; A.I chỉ đề xuất |
| CHƯA KẾT LUẬN | Cỡ mẫu, thời gian, chất lượng số liệu không đủ; hoặc thiếu số của chỉ số cảnh báo | Người phụ trách quyết đo thêm hay đóng |

Bộ kiểm `scripts/kiem-vong-cai-tien.py` tính được: CHƯA SẴN SÀNG, ĐANG CHẠY, CHƯA KẾT LUẬN, QUAY LẠI CÁCH CŨ, ĐỀ XUẤT ÁP DỤNG, LOẠI BỎ. Trạng thái LÀM VÒNG MỚI do người chốt.

## 4. Chuẩn hóa

Chỉ chuẩn hóa sau khi người có quyền duyệt áp dụng. Cần: SOP và phiên bản mới · phạm vi áp dụng và giới hạn (chỉ trong phạm vi đã thử) · người đào tạo · điểm kiểm soát · chỉ số theo dõi và lịch kiểm lại · điều kiện mở lại (khi chỉ số quay về mức cũ) · cách quay lại · xử lý bản cũ.

## 5. Lỗi hay gặp

1. Nhảy vào giải pháp, lấy một điểm làm nền, nhiều thay đổi cùng lúc, "sau tốt hơn trước" là đủ.
2. Làm đẹp số: chọn lọc nhóm hay kỳ có lợi, đổi chỉ tiêu sau khi thấy kết quả, bỏ số bị thiếu, bỏ chỉ số cảnh báo.
3. Tối ưu chỉ số một khâu làm xấu cả hệ thống; mở rộng vượt phạm vi đã thử.
4. Chuẩn hóa kết quả chưa kết luận; để thử nghiệm treo; họp cải tiến không ra quyết định.

*[A.I Generated — Claude Code — 30/10/2026]*
