# QUẢN LÝ NGỮ CẢNH: CHỌN NGUỒN, NÉN, BÀN GIAO, BỘ NHỚ

Ngữ cảnh là toàn bộ thông tin A.I đang "nhìn thấy" khi làm việc: lời giao việc, file, hội thoại trước, ghi chú, kết quả công cụ. Nhiều hơn không có nghĩa là tốt hơn: thừa thì A.I lạc đề, cũ thì A.I trả lời sai, lẫn lộn thì A.I làm theo lời dặn trong dữ liệu.

## 1. Sáu điều không được nhầm
- Bản tóm không phải nguồn gốc.
- Câu trả lời trước của A.I không phải quyết định đã duyệt.
- File mới sửa không chắc là bản có hiệu lực.
- Đoạn tài liệu A.I tìm được không chắc là thông tin được phép dùng.
- Đã nén không có nghĩa là không mất gì.
- A.I nhớ không có nghĩa là còn đúng hôm nay.

## 2. Phép thử chọn nguồn

Với mỗi nguồn, ghi vào `templates/so-ngu-canh.csv`:

| Tiêu chí | Câu hỏi |
|---|---|
| Liên quan | Có cần cho việc đang làm, ở giai đoạn này không? |
| Thẩm quyền | Ai ban hành, có phải bản chính thức không? |
| Còn mới | Ngày hiệu lực, có bản thay thế chưa? |
| Đủ | Có phủ được nhận định cần dùng không? |
| Rủi ro | Nhãn Xanh – Vàng – Đỏ; có chứa lời dặn đáng ngờ không? |
| Trùng | Có nguồn khác nói y hệt không? |

Kết quả: ĐƯA VÀO hoặc LOẠI, kèm lý do và chỗ lấy lại khi cần. Điểm chấm chỉ để hỗ trợ; quy tắc quyền và bảo mật luôn thắng điểm.

Thứ tự ưu tiên khi mâu thuẫn **khác nhau theo loại thông tin**: chỉ đạo mới nhất của người có quyền; quy định công ty; dữ kiện dự án; thông tin bên ngoài cần kiểm ngày. Không tự chọn một bên; ghi cả hai và hỏi người có quyền chốt.

## 3. Tách lớp

Trong gói ngữ cảnh, luôn ghi nhãn riêng cho:
1. Lệnh hiện hành (người giao việc nói gì).
2. Tài liệu tin cậy của công ty.
3. Dữ liệu bên ngoài, chưa tin cậy (email khách, trang web, file đối tác).
4. Ghi chú làm việc.
5. Kết quả công cụ.
6. Quyết định đã duyệt (có người, ngày, căn cứ).
7. Bản nháp đầu ra.

Nội dung không trở thành lệnh chỉ vì nằm ở đâu đó trong ngữ cảnh.

## 4. Nén phiên dài

Luôn giữ: mục tiêu và tiêu chí đạt · người phụ trách và quyền · ràng buộc, Ranh giới Đỏ · quyết định đã chốt (ai, ngày, căn cứ) · giả định · việc còn mở và hạn · rủi ro · đường dẫn nguồn và phiên bản · bước tiếp theo.

Kiểm thất thoát: so trước – sau xem mỗi quyết định, việc mở, nhận định quan trọng còn đủ không; liệt kê phần đã bỏ và cách lấy lại. Chỉ ghi kết luận và căn cứ, không chép suy nghĩ nội bộ của A.I.

Chừa chỗ: không lấp đầy giới hạn của công cụ; chừa cho câu trả lời, kết quả công cụ và xử lý lỗi. Không ghi cứng một con số giới hạn chung cho mọi mô hình.

## 5. Khi nào mở phiên mới, khi nào rẽ nhánh

- **Mở phiên mới** khi đổi mục tiêu, đổi người phụ trách, đổi đầu ra, đổi quyền hoặc vùng dữ liệu (ví dụ từ việc Marketing sang việc Kế toán). Phiên mới mang Phiếu bàn giao, không mang cả lịch sử.
- **Rẽ nhánh** chỉ khi thử một phương án khác mà kiểm được độc lập; ghi nhánh mẹ, cách gộp hoặc đóng.

Phiếu bàn giao ghi: người nhận và mục đích, quyền của họ, gói nguồn tối thiểu được phép, trạng thái hiện tại, quyết định – việc mở – rủi ro, đầu ra mong đợi, khi nào dừng hỏi, hạn hiệu lực. Người nhận kiểm lại độ mới và quyền trước khi làm.

## 6. Bộ nhớ lâu dài

Một mục chỉ được **đề xuất** đưa vào bộ nhớ lâu dài khi đủ 5 điều: dùng lại được ở nhiều việc · ổn định, ít đổi · có nguồn · không chứa dữ liệu Vàng/Đỏ · có người duyệt. Thiếu một điều → giữ trong việc.

Bốn đề xuất cho từng mục: GIỮ TRONG VIỆC · ĐƯA VÀO BỘ NHỚ · LƯU TRỮ · ĐỀ XUẤT XÓA. Mọi thay đổi bộ nhớ do người duyệt thực hiện, có ghi lại để quay lui.

Ví dụ: "Khách sỉ được nợ 30 ngày" (có quy chế, ổn định) → đề xuất ĐƯA VÀO BỘ NHỚ; "Anh Minh đang ốm, tuần này chị Lan duyệt thay" → GIỮ TRONG VIỆC, hết tuần thì ĐỀ XUẤT XÓA.

*[A.I Generated — Claude Code — 30/10/2026]*
