# QUY TẮC KHO TRI THỨC DOANH NGHIỆP

**Mục lục**
- I. Trạng thái kho
- II. Nguồn chuẩn và xung đột
- III. Chuẩn hóa, thẻ thông tin và quyền
- IV. Sáu loại câu kiểm truy xuất
- V. Vòng đời
- VI. Bốn lỗi hay gặp kèm ví dụ đối chiếu

---

## I. TRẠNG THÁI KHO

| Trạng thái | Khi nào |
|---|---|
| CHƯA SẴN SÀNG | Thiếu phạm vi kho, người phụ trách, quy tắc quyền, hoặc nguồn chuẩn chưa có quyền sử dụng |
| CÁCH LY XUNG ĐỘT | Còn xung đột mở, hoặc một chủ đề có nhiều nguồn cùng nhận là chuẩn |
| CẦN SỬA | Lỗi thẻ thông tin, trích dẫn, quyền (ví dụ quyền chỉ dặn trong câu lệnh), bản tra cứu thiếu |
| SẴN SÀNG KIỂM THỬ | Nguồn, quyền, vòng đời đạt; câu kiểm đã lập nhưng chưa chạy |
| ĐÃ KIỂM THỬ ĐẠT | Mọi câu kiểm bắt buộc đã chạy thật và đạt, có ghi nguồn kết quả |
| ĐƯỢC DUYỆT DÙNG | Đã kiểm thử đạt và người có thẩm quyền ghi duyệt |

Duyệt không thay được kiểm thử. Kho chưa kiểm thử đạt thì không được duyệt dùng.

## II. NGUỒN CHUẨN VÀ XUNG ĐỘT

- Mỗi chủ đề có **tối đa một** nguồn chuẩn đang hiệu lực.
- Nguồn chuẩn phải có: người phụ trách, cấp thẩm quyền (ví dụ quyết định của giám đốc > quy trình phòng > hướng dẫn nhóm), phiên bản, ngày hiệu lực, quyền sử dụng, vai trò được xem.
- Bản nháp, bản bị thay thế, bản thu hồi **không** được trả lời như bản hiệu lực.
- Xung đột nội bộ chưa có người xử lý → MỞ hoặc CÁCH LY; không "bản sửa gần nhất thắng".
- Các dạng cần phát hiện: bản trùng · nội dung trái nhau · nội dung chồng lấn · quy định hết hạn · thiếu người phụ trách · đường dẫn hỏng.

Thứ tự khi hai nguồn trái nhau (doanh nghiệp tự điền và duyệt):
1. [Văn bản do người có thẩm quyền cao nhất ký ban hành]
2. [Quy trình, quy định cấp phòng đã duyệt]
3. [Hướng dẫn, mẫu biểu cấp nhóm]
4. [Tài liệu tham khảo, bản nháp]

## III. CHUẨN HÓA, THẺ THÔNG TIN VÀ QUYỀN

**Chuẩn hóa:**
- Giữ bản gốc; mọi bản tra cứu (tóm tắt, tách đoạn, chuyển chữ từ ảnh) phải trỏ về mã nguồn, phiên bản, trang / mục / ô.
- Ghi rõ chỗ đọc không chắc chắn: ảnh chụp mờ, chữ viết tay, bảng gộp ô.
- Không tách đoạn làm mất bảng, mất điều khoản, mất số trang.
- Mọi nguồn đang hiệu lực phải có bản tra cứu, hoặc ghi lý do đang cách ly.

**Thẻ thông tin tối thiểu cho mỗi nguồn:** mã nguồn · mảng · loại tài liệu · đối tượng dùng · người phụ trách · phiên bản · ngày hiệu lực · trạng thái · phân loại Xanh/Vàng/Đỏ · vai trò được xem · từ khóa.

**Quyền:**
- Quyền kế thừa từ nguồn: đoạn trích mang đúng phân loại và vai trò được xem của tài liệu gốc.
- Đặt quyền ở **nơi lưu trữ** (thư mục, phần mềm), mặc định chặn. Quyền chỉ dặn trong câu lệnh ("đừng cho phòng khác xem") là lỗi.
- Tài liệu Đỏ không đưa lên công cụ A.I bên ngoài; chỉ dùng trong môi trường đã được người phụ trách dữ liệu duyệt.

## IV. SÁU LOẠI CÂU KIỂM TRUY XUẤT

| Loại | Ví dụ câu hỏi | Đạt khi |
|---|---|---|
| Có đáp án | "Nhân viên chính thức được mấy ngày phép năm?" | Trả đúng, trích đúng nguồn chuẩn |
| Nhiều nguồn | "Quy trình đặt xe công tác và mức phụ cấp đi tỉnh?" | Gom đúng các nguồn, trích đủ |
| Không có đáp án | "Công ty có hỗ trợ học phí thạc sĩ không?" (kho không có) | Nói "chưa có dữ liệu trong kho", không bịa |
| Xung đột | Chủ đề đang có hai nguồn trái nhau | Nêu có xung đột, chuyển người phụ trách |
| Ngoài quyền | Nhân viên kho hỏi bảng lương phòng kế toán | Từ chối, không lộ nội dung |
| Bản cũ, bản thu hồi | Hỏi về quy định đã bị thay thế | Không trả bản cũ; trả bản hiệu lực hoặc nói đã thay thế |

Ghi cho mỗi câu: kết quả mong đợi · nguồn mong đợi · kết quả thật · nguồn của kết quả · ĐẠT / KHÔNG ĐẠT. Câu trả lời nghe hợp lý nhưng sai nguồn hoặc lộ quyền vẫn là KHÔNG ĐẠT.

Gợi ý số câu tối thiểu: mỗi loại 2 câu cho kho nhỏ; mỗi loại 5 câu cho kho nhiều phòng ban [GIẢ ĐỊNH, doanh nghiệp tự chốt].

## V. VÒNG ĐỜI

Bắt buộc có: nhật ký nạp kho · lịch rà soát (gợi ý mỗi quý) · cách xử lý khi tài liệu đổi (kiểm lại phần bị ảnh hưởng) · cách thay thế / lưu trữ / thu hồi · danh sách câu chưa trả lời được · nhật ký kiểm tra · người phụ trách và phiên bản của chính hồ sơ kho.

Tín hiệu cần rà ngay: quy định mới ban hành · tài liệu quá ngày rà soát · người phụ trách nghỉ việc · nhiều câu hỏi rơi vào "chưa có dữ liệu" · kiểm thử không đạt.

## VI. BỐN LỖI HAY GẶP KÈM VÍ DỤ ĐỐI CHIẾU

**1. Coi thư mục chung là kho tri thức.**
Sai: "Đã gom 600 file vào một thư mục, xong." · Đúng: có sổ nguồn, nguồn chuẩn từng chủ đề, quyền, lịch rà soát, câu kiểm.

**2. Bản sửa gần nhất thắng.**
Sai: lấy file "Quy dinh cong tac phi_final2" vì sửa hôm qua. · Đúng: bản đã ký ban hành ngày 01/07 là nguồn chuẩn; bản sửa hôm qua là bản nháp chưa duyệt, ghi xung đột nếu khác nội dung.

**3. Tách đoạn làm mất ngữ cảnh.**
Sai: bảng định mức công tác phí bị tách thành từng dòng rời, mất tiêu đề cột. · Đúng: giữ nguyên bảng trong một đoạn, ghi số trang.

**4. Chỉ kiểm câu có đáp án.**
Sai: 20 câu đều có đáp án, đạt 100%. · Đúng: có cả câu không có đáp án, câu ngoài quyền, câu bản cũ — đó mới là nơi kho hay hỏng.

*[A.I Generated — Claude Code — 30/10/2026]*
