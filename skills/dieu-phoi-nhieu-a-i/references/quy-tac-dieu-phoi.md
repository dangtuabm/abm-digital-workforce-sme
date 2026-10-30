# QUY TẮC ĐIỀU PHỐI NHIỀU A.I

**Mục lục**
- I. Cổng cần thiết
- II. Đơn vị việc, phân việc, hàng chờ
- III. Chuyển giao, soát, hợp nhất
- IV. Lỗi và người duyệt
- V. An toàn, dấu vết, vòng đời
- VI. Điều cấm làm tắt

---

## I. CỔNG CẦN THIẾT

So ba phương án trên **cùng một kết quả cuối và cùng tiêu chí nghiệm thu**:

| Tiêu chí | Quy trình cố định | Một A.I có công cụ | Nhiều A.I |
|---|---|---|---|
| Đạt tiêu chí nghiệm thu | | | |
| Khối lượng, cao điểm | | | |
| Cần chuyên môn khác nhau? | | | |
| Làm song song có lợi? | | | |
| Cách ly dữ liệu / rủi ro | | | |
| Chi phí phối hợp (chuyển giao, chờ, soát) | | | |
| Độ trễ, chi phí chạy | | | |
| Bề mặt lỗi | | | |

Nhiều A.I chỉ hợp khi có các đầu ra độc lập, chuyên môn khác biệt, lợi ích làm song song hoặc cần cách ly — và lợi ích đó lớn hơn chi phí phối hợp. Nhiều vai, nhiều mô hình hay nhiều lượt gọi không phải bằng chứng giá trị. Phương án đơn giản đạt thì chọn phương án đơn giản.

## II. ĐƠN VỊ VIỆC, PHÂN VIỆC, HÀNG CHỜ

**Một việc** = một đầu ra được nghiệm thu độc lập + một người chịu trách nhiệm + một người làm chính từ đầu đến cuối + một người soát độc lập + nơi lưu kết quả. **Gói việc** chỉ lập khi có nhiều việc mà mỗi việc được nghiệm thu riêng. Tìm hiểu, phân tích, soạn, tự soát nằm trong một việc trừ khi đầu ra của từng bước được người khác dùng riêng.

Chia ra – gộp vào phải có người chịu trách nhiệm gộp, quy tắc đủ, quy tắc trùng và quy tắc khi mâu thuẫn.

**Nhận việc**: kiểm nguồn, mẫu dữ liệu, quyền; mã chống nhận trùng; việc báo lại, đến muộn; cách ly việc lạ; quyết định là một việc hay một gói việc; hủy việc.

**Phân việc**: lọc đủ điều kiện trước (đúng Skill, đúng quyền dữ liệu, đúng môi trường, còn sức chứa, đang hoạt động), chấm điểm sau (chất lượng, thời gian, chi phí). Ghi danh sách ứng viên, lý do loại, cách xử khi hòa, khi không ai nhận, khi người sửa tay, phiên bản quy tắc. Bộ phân việc không cấp quyền, không đổi Thẻ của A.I.

**Hàng chờ**: hạng ưu tiên · chống việc nằm quá lâu · giới hạn việc đang làm dở cho từng A.I · giới hạn tốc độ, số việc song song, chi phí · giữ chỗ và hết hạn giữ chỗ · hạn chót · hủy · chống chạy lại dồn dập.

**Trạng thái việc** do từng hệ thống đặt; mỗi bước chuyển ghi: từ – sự kiện – sang, ai làm, điều kiện, hành động, kết quả mong đợi, cách kiểm, mã theo dõi, hạn chờ, nhịp báo còn sống, bước chuyển khi lỗi. Trạng thái kết thúc không được sửa ngược.

## III. CHUYỂN GIAO, SOÁT, HỢP NHẤT

**Phiếu chuyển giao** ghi: bên giao, bên nhận, mã việc, phiên bản Thẻ và mẫu dữ liệu, đường dẫn kết quả, nguồn, mức chắc chắn, phần chưa rõ, nhãn dữ liệu, chấp nhận / trả lại / làm lại, hạn chờ, cách xử khi trùng hoặc mâu thuẫn, dấu vết. Mặc định không chuyển toàn bộ hội thoại hay khóa kết nối.

**Soát**: người làm chính ra bản 1; người soát độc lập đối chiếu tiêu chí và nguồn rồi sửa thành bản cuối. Chỉ CHẶN hoặc CHUYỂN NGƯỜI khi thiếu nguồn, mục tiêu đổi, chạm quyền hay rủi ro, hoặc bằng chứng không thể dung hòa.

**Hợp nhất**: có người chịu trách nhiệm, quy tắc đủ, sổ mâu thuẫn, quy tắc nguồn nào thắng, truy được từ bản cuối về từng kết quả con. Đa số đồng ý, các mô hình giống nhau hay câu chữ trơn tru không thay nguồn, tiêu chí nghiệm thu hay quyết định của người phụ trách.

## IV. LỖI VÀ NGƯỜI DUYỆT

Xác định vùng lỗi; lỗi nào chạy lại được, lỗi nào không; chạy lại có giới hạn và giãn cách tăng dần; mã chống làm trùng; phương án dự phòng; ngắt mạch khi lỗi lặp; vách ngăn để lỗi một A.I không kéo A.I khác; hàng chờ lỗi; bù trừ và đối chiếu; chuyển người; làm tay; dừng khẩn; quay lại sau sửa; rà sự cố. Tránh lỗi lan dây chuyền, làm trùng, việc mồ côi.

Người duyệt đứng trước: hành động ra ngoài (gửi khách, đăng bài), khó đảo ngược (xóa, chuyển tiền), rủi ro cao, ngoại lệ, đổi mục tiêu / Thẻ / quyền / ngân sách, phát hành bản cuối. Giữ tách biệt nhiệm vụ: người làm không tự duyệt. Không bắt người duyệt mọi bước nội bộ sửa được.

## V. AN TOÀN, DẤU VẾT, VÒNG ĐỜI

- **Ranh giới tin cậy**: danh tính từng A.I, quyền tối thiểu, nhãn dữ liệu, dữ liệu lộ chéo giữa A.I, chỉ dẫn nhúng, khóa kết nối chỉ ghi tên tham chiếu, rà quyền định kỳ.
- **Dấu vết** mỗi lần chạy: gói việc, việc, A.I, phiên bản Thẻ – Skill – mô hình – công cụ – quy tắc phân việc, đầu vào/ra, trạng thái trước/sau, duyệt, lỗi, chạy lại, dự phòng, thời gian, chi phí, đường dẫn kết quả.
- **Theo dõi**: chọn 2–3 chỉ số chính từ: tỷ lệ đạt nghiệm thu, thời gian hoàn thành, số việc làm dở, số việc rơi/trùng, số lần người phải can thiệp, chi phí mỗi việc. Mỗi chỉ số có công thức, nguồn, khung thời gian, người phụ trách, hành động khi vượt ngưỡng.
- **Thay đổi**: có phiên bản, kiểm tương thích, chạy thử nhỏ, quay lui, báo các bên dùng.
- **Cho nghỉ một A.I**: ngừng nhận việc → làm hết hoặc chuyển việc dở → đối chiếu → thu tài khoản, kết nối, khóa → lưu hoặc xóa theo quyết định người có quyền → kiểm không còn việc và quyền sót lại.

## VI. ĐIỀU CẤM LÀM TẮT

Không dùng nhiều A.I khi chưa qua Cổng cần thiết · không A.I nào chạy khi chưa có Thẻ · không gắn cứng mô hình vào vai · không để người làm tự soát · không chuyển toàn bộ ngữ cảnh · không coi phân việc là cấp quyền · không để hàng chờ, chạy lại vô hạn · không để lỗi im lặng hay lan dây chuyền · không tự tạo, cấp quyền, bật, chạy, sửa dữ liệu thật, gửi, chi tiền · không đổi lớn hay cho nghỉ A.I khi chưa kiểm tương thích, có quay lui và kiểm lại.

*[A.I Generated — Claude Code — 30/10/2026]*
