# QUY TẮC KIỂM CHỨNG THEO LOẠI CLAIM

## 1. Chọn phép kiểm

| Loại claim | Trường phải khớp | Nguồn ưu tiên | Lỗi hay gặp |
|---|---|---|---|
| Số liệu/thống kê | Con số, đơn vị, mẫu số, phương pháp, địa lý, thời gian | Dataset/báo cáo gốc và ghi chú phương pháp | Bỏ mẫu số; lấy % của một phân khúc cho toàn thị trường |
| Trích dẫn | Câu chữ, người nói, thời điểm, ngữ cảnh | Video, transcript, văn bản hoặc thông cáo gốc | Cắt mất điều kiện; dẫn lại từ bài tổng hợp |
| Sự kiện/ngày | Sự kiện, ngày, địa điểm, chủ thể | Hồ sơ cơ quan, thông báo chính thức, tài liệu đương thời | Nhầm ngày công bố với ngày sự kiện |
| Pháp lý/chính sách | Thẩm quyền, phạm vi, ngày hiệu lực, sửa đổi/thay thế | Văn bản và cơ sở dữ liệu chính thức | Dùng bản dự thảo; bỏ qua văn bản thay thế |
| Tính năng/giá | Sản phẩm, gói, khu vực, đối tượng, ngày kiểm | Tài liệu và trang giá chính thức còn hiệu lực | Lấy giá khu vực khác; dùng trang cache hoặc bài cũ |
| Quan hệ nhân quả | Biến nguyên nhân, kết quả, thiết kế nghiên cứu, yếu tố gây nhiễu | Nghiên cứu gốc có thiết kế đủ suy luận | Biến tương quan thành nhân quả |
| Nguồn gốc/tác giả | Tác giả, quyền sở hữu, lần xuất bản đầu, phiên bản | Tài liệu gốc, hồ sơ xuất bản | Gán tác giả cho người dẫn lại |

## 2. Xếp nguồn theo quan hệ với claim

1. **Nguồn gốc:** tạo ra dữ liệu, quyết định, phát ngôn hoặc tài liệu được claim nhắc tới.
2. **Nguồn chính thức:** cơ quan/chủ thể có thẩm quyền công bố, nhưng có thể tự mô tả lợi ích của mình.
3. **Nguồn thứ cấp độc lập:** phân tích hoặc tường thuật có biên tập, hữu ích để đối chứng.
4. **Nguồn tổng hợp:** dùng để tìm manh mối; không thay nguồn mà nó dẫn.
5. **Nội dung do người dùng tạo:** có thể là bằng chứng trải nghiệm, không tự chứng minh claim phổ quát.

Không chọn nguồn chỉ theo danh tiếng tổ chức. Chọn theo quan hệ trực tiếp với claim, phương pháp, độ hiện hành và khả năng tái kiểm.

## 3. Chuỗi truy nguyên tối thiểu

Ghi cho mỗi evidence:

- `EVD-ID` và `CLM-ID`;
- tác giả/cơ quan và tiêu đề;
- URL hoặc tên file;
- ngày công bố, ngày hiệu lực/phiên bản nếu có, ngày truy cập;
- vị trí cụ thể: trang, mục, bảng, dòng hoặc timestamp;
- trích đoạn ngắn hỗ trợ hoặc phản bác;
- vai trò: gốc, chính thức, đối chứng, phản biện;
- giới hạn và xung đột lợi ích.

## 4. Xử lý mâu thuẫn

1. So lại định nghĩa và đơn vị phân tích.
2. So ngày dữ liệu, ngày công bố và ngày hiệu lực.
3. So phương pháp, mẫu số, phạm vi và ngoại lệ.
4. Xác định hai nguồn có thực sự trả lời cùng một claim không.
5. Nếu vẫn xung đột, giữ cả hai, hạ phán quyết và nêu điểm cần người có thẩm quyền chốt.

## 5. Ngoại lệ

- Nguồn gốc không đồng nghĩa trung lập; claim tự báo cáo cần ghi rõ.
- Nguồn cũ có thể đúng cho mốc lịch sử; không bác chỉ vì cũ.
- Không thấy bằng chứng trên web không chứng minh claim sai.
- Ảnh chụp màn hình chứng minh trạng thái tại thời điểm chụp, không tự chứng minh nguồn gốc hay tính liên tục.
