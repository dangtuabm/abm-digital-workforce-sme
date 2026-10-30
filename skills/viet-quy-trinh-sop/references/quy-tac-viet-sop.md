# QUY TẮC VIẾT VÀ RÀ SOÁT SOP

**Mục lục**
- 1. Căn cứ và đầu bài
- 2. Ranh giới và SIPOC
- 3. Vai trò và tách nhiệm
- 4. Viết từng bước
- 5. Ngoại lệ, chuyển cấp, phương án dự phòng
- 6. Điểm kiểm soát và chỉ số
- 7. Biểu mẫu và hồ sơ
- 8. Chạy thử, ban hành, thay phiên bản
- 9. Tám nhóm lỗi khi rà soát SOP
- 10. Ví dụ đạt / chưa đạt

---

## 1. Căn cứ và đầu bài

Khóa trước khi viết: mục tiêu, loại tài liệu (SOP gọn, bộ SOP, hướng dẫn nhanh, checklist), người đọc, tín hiệu bắt đầu – điểm kết thúc, khối lượng, mức quan trọng, mốc thời gian, người phụ trách, người duyệt, người ban hành, việc không làm.

Mọi nhận định về cách làm hiện tại phải có căn cứ: quan sát tại chỗ, phỏng vấn người làm thật, nhật ký phần mềm, hồ sơ, quy định, sổ sự cố. Ghi tách 5 loại:

| Loại | Ví dụ | Cách dùng |
|---|---|---|
| Việc đang làm thật | "Thủ kho đếm hàng rồi mới ký phiếu" | Đưa vào luồng hiện tại |
| Việc quy định bắt buộc | "Hàng lạnh phải kiểm nhiệt độ khi nhận" | Đưa vào bước và điểm kiểm soát |
| Mẹo riêng của từng người | "Chị Lan hay gọi trước cho tài xế" | Hỏi người phụ trách có chuẩn hóa không |
| Giả thuyết | "Có lẽ chậm vì chờ ký" | Ghi [GIẢ ĐỊNH], kiểm khi chạy thử |
| Mâu thuẫn | Quy định ghi 2 người ký, thực tế 1 người | Ghi cả hai, hỏi người có quyền chốt |

## 2. Ranh giới và SIPOC

SIPOC = Nhà cung cấp (Supplier) – Đầu vào (Input) – Quy trình (Process) – Đầu ra (Output) – Khách hàng (Customer).

Ghi thêm: điều kiện trước khi bắt đầu, tiêu chí nhận đầu ra, giao diện với bộ phận trước và sau, **hồ sơ gốc lưu ở đâu** (phần mềm bán hàng, phần mềm kế toán, bảng tính dùng chung, sổ giấy).

So sánh luồng hiện tại với luồng mục tiêu, nêu lý do cho từng bước bỏ hoặc thêm. Cắt bước thừa được, nhưng **không bỏ điểm kiểm soát** và không tự động hóa một quy trình đang hỏng khi chưa có căn cứ và người có quyền đồng ý.

## 3. Vai trò và tách nhiệm

Mỗi quy trình có: người chịu trách nhiệm kết quả · người làm · người kiểm · người duyệt · người được báo · người thay thế khi vắng. Có thể trình bày dạng bảng RACI (R làm – A chịu trách nhiệm – C được hỏi ý kiến – I được báo).

- Ghi theo chức danh, không theo tên người: "Thủ kho", không ghi "anh Hùng".
- Tách nhiệm: người đề nghị chi không tự duyệt chi; người nhận hàng không tự xác nhận chất lượng lô hàng mình nhận ở việc quan trọng; người làm không tự đóng sự cố nghiêm trọng của chính mình.
- Bảng vai trò không tự cấp quyền truy cập hay quyền duyệt; cấp quyền là việc của người quản trị hệ thống theo quy chế.

## 4. Viết từng bước

Mỗi bước có đủ:

| Trường | Ghi gì |
|---|---|
| Mã bước | B01, B02… |
| Tín hiệu bắt đầu / đầu vào | Việc gì xảy ra thì làm bước này |
| Vai trò làm / vai trò chịu trách nhiệm | Chức danh |
| Việc làm hoặc quy tắc quyết định | Động từ đầu câu; nếu có rẽ nhánh thì ghi điều kiện rõ ("Nếu chênh lệch > 2% → chuyển B05") |
| Đầu ra và tiêu chí đạt | Người khác nhìn vào biết đạt hay chưa |
| Thời hạn | Chỉ ghi khi có số đo thật hoặc đã được duyệt; chưa có thì ghi "chờ đo" |
| Hồ sơ / bằng chứng | Phiếu, ảnh chụp, dòng trong phần mềm |
| Điểm kiểm soát | Mã kiểm soát áp dụng |
| Phụ thuộc / bước tiếp theo | Bước sau, hoặc trạng thái kết thúc |

Tránh chữ "linh hoạt", "tùy tình hình", "khi cần" mà không có điều kiện.

## 5. Ngoại lệ, chuyển cấp, phương án dự phòng

Mỗi ngoại lệ đáng kể ghi: dấu hiệu nhận biết · cách khoanh vùng an toàn (tạm dừng, cách ly, giữ nguyên hiện trạng) · việc được phép làm khác · ngưỡng chuyển cấp, chuyển cho ai, trong bao lâu · ai quyết · bằng chứng cần giữ · cách khôi phục · điều kiện đóng.

Nên rà các loại: thiếu hoặc sai dữ liệu đầu vào · phần mềm lỗi hoặc mất mạng (có phiếu giấy dự phòng, nhập bù sau) · người phụ trách vắng · nhà cung cấp hoặc đối tác chậm · quá tải · nghi lộ dữ liệu, sai quyền.

## 6. Điểm kiểm soát và chỉ số

**Điểm kiểm soát:** mục tiêu · loại (phòng ngừa / phát hiện / khắc phục) · người giữ · tần suất hoặc sự kiện · bằng chứng · đạt / không đạt · xử lý khi không đạt · rủi ro còn lại. Điểm kiểm soát trọng yếu phải đạt riêng, không lấy điểm khác bù.

**Chỉ số:** mục đích · công thức · tử số / mẫu số · nhóm và kỳ đo · nguồn số liệu · người theo dõi · căn cứ chỉ tiêu. Tách 4 nhóm: tốc độ (thời gian từ đầu đến cuối) · chất lượng (tỷ lệ đạt ngay lần đầu, tỷ lệ làm lại) · hiệu lực kiểm soát · kết quả cho khách hàng. Không đặt chỉ tiêu "chung cho mọi ngành"; chưa có số đo thì ghi "chỉ tiêu: chờ số liệu nền".

## 7. Biểu mẫu và hồ sơ

Đính kèm thứ dùng được ngay: phiếu nhập, checklist, bảng quyết định, mẫu tin nhắn gửi khách, danh sách trường dữ liệu cần ghi. Mỗi biểu mẫu có: mã, gắn với bước nào, phiên bản, ai được sửa, ai được xem, lưu bao lâu, thế nào là "đã hoàn thành".

Ví dụ trong biểu mẫu dùng dữ liệu giả. Không đưa mật khẩu, số tài khoản, số CCCD, dữ liệu cá nhân thật vào biểu mẫu mẫu.

## 8. Chạy thử, ban hành, thay phiên bản

Chạy thử trên giấy (đọc từng bước với người làm thật) cho 5 loại ca: bình thường · ngoại lệ · biên (số lượng rất lớn, hàng đặc biệt) · mất hệ thống · sai quyền. Mỗi ca ghi kết quả mong đợi, lỗi phát hiện, đã sửa chưa, thử lại chưa.

Chạy thử trên giấy **không** chứng minh SOP hiệu quả khi áp dụng thật, cũng không chứng nhận nhân viên đã đủ năng lực. Đào tạo và kiểm tra năng lực là việc riêng, cần bằng chứng riêng.

Gói ban hành gồm: phiên bản đề xuất, ngày hiệu lực đề xuất, người bị ảnh hưởng, nội dung thay đổi và lý do, kế hoạch đào tạo và xác nhận đã đọc, cách quay lại bản cũ, xử lý bản cũ (lưu trữ chỉ đọc). Ô "Người ban hành / ngày" để trống.

Gợi ý thử điểm thật: chọn 3 quy trình khác mức rủi ro (một việc lặp lại đơn giản, một việc nhiều ngoại lệ liên phòng ban, một việc chạm dữ liệu nhạy cảm), so sánh trước – sau về số lần hỏi lại, lỗi, làm lại, thời gian.

## 9. Tám nhóm lỗi khi rà soát SOP

| # | Nhóm lỗi | Câu hỏi soát | Mức thường gặp |
|---|---|---|---|
| 1 | Mục tiêu, ranh giới | Bắt đầu – kết thúc ở đâu? Áp dụng cho ai? Có việc không làm? | Nghiêm trọng nếu thiếu |
| 2 | Căn cứ | Bước nào không có căn cứ hoặc mâu thuẫn quy định? | Nghiêm trọng |
| 3 | Vai trò, tách nhiệm | Có bước "tự làm tự duyệt"? Có người thay thế? Ghi tên người thay chức danh? | Nghiêm trọng ở việc chạm tiền |
| 4 | Bước | Bước mơ hồ, gộp nhiều việc, thiếu tiêu chí đạt, thiếu hồ sơ? | Trung bình |
| 5 | Ngoại lệ | Ngoại lệ đã từng xảy ra có đường xử lý chưa? Có phương án khi mất hệ thống? | Nghiêm trọng nếu sự cố đã lặp |
| 6 | Kiểm soát, chỉ số | Có bằng chứng? Chỉ số có mẫu số? Chỉ tiêu có căn cứ? | Trung bình |
| 7 | Biểu mẫu, dữ liệu | Biểu mẫu còn dùng? Có dữ liệu thật, mật khẩu trong mẫu? | Nghiêm trọng nếu lộ dữ liệu |
| 8 | Phiên bản, áp dụng | Bản nào đang hiệu lực? Người làm có đang dùng bản cũ? Có cách quay lại? | Trung bình |

Mức nghiêm trọng: **NGHIÊM TRỌNG** (có thể gây thiệt hại tiền, khách, an toàn, dữ liệu — sửa trước khi dùng tiếp) · **CẦN SỬA** (gây làm lại, hỏi lại) · **GÓP Ý** (trình bày).

## 10. Ví dụ đạt / chưa đạt

| Chưa đạt | Đạt |
|---|---|
| "Nhận hàng và kiểm tra cẩn thận." | "B03 — Thủ kho đếm số kiện, đối chiếu với phiếu giao. Lệch số kiện → ghi biên bản lệch (BM-02), chụp ảnh, báo Trưởng kho trước khi ký." |
| "Xử lý nhanh trong ngày." | "Thời hạn: chờ đo trong 2 tuần chạy thử (hiện chưa có số liệu nền)." |
| "Anh Tuấn duyệt." | "Trưởng phòng Kinh doanh duyệt; vắng thì Phó phòng duyệt." |

*[A.I Generated — Claude Code — 30/10/2026]*
