# BẢY MỨC PHÂN VIỆC NGƯỜI – A.I

## 1. Bảy mức

| Mức | Nghĩa | Khi nào hợp | Ví dụ ở doanh nghiệp vừa và nhỏ |
|---|---|---|---|
| **BỎ** | Việc thừa, trùng, không ai dùng kết quả → bỏ hẳn hoặc gộp | Việc tồn tại chỉ vì thói quen | Nhập lại đơn hàng từ Zalo sang Excel rồi sang phần mềm bán hàng (hai lần chép) |
| **CHỈ NGƯỜI LÀM** | A.I không tham gia | Quyết định tác động lớn, cần trách nhiệm pháp lý, cần quan hệ con người, dữ liệu Đỏ | Duyệt giá đặc biệt cho đại lý lớn; nói chuyện với nhân viên sắp nghỉ |
| **A.I HỖ TRỢ** | Người làm chính, A.I gợi ý, tra cứu, soạn thô | Việc cần phán đoán nhưng tốn thời gian tìm, soạn | Kế toán hỏi A.I cách hạch toán một khoản lạ rồi tự quyết |
| **A.I LÀM – NGƯỜI DUYỆT** | A.I làm bản hoàn chỉnh, người duyệt trước khi có hiệu lực | Việc lặp lại, có mẫu, sai thì hậu quả vừa, hoặc có đi ra ngoài | A.I soạn báo giá theo bảng giá, nhân viên kinh doanh duyệt rồi mới gửi khách |
| **A.I TỰ LÀM TRONG HẠN MỨC** | A.I tự làm, không cần duyệt từng lần, nhưng trong giới hạn rõ | Việc nội bộ, sai sửa được, khối lượng lớn, có quy tắc rõ | A.I tự phân loại email đến vào 5 nhóm và gắn nhãn; không gửi, không xóa |
| **A.I THEO DÕI – CẢNH BÁO** | A.I không làm, chỉ phát hiện và báo người | Cần để mắt liên tục, người không theo dõi xuể | A.I báo khi tồn kho mã hàng chủ lực dưới mức an toàn, hoặc đơn quá hạn giao |
| **NGOẠI LỆ CHUYỂN NGƯỜI** | Mọi trường hợp ngoài quy tắc tự động chuyển về đúng người | Đi kèm các mức A.I làm hoặc tự làm | Khách khiếu nại có chữ "luật sư", "báo chí" → chuyển trưởng phòng ngay |

## 2. Bỏ trước khi tự động

Trước khi gán mức A.I, hỏi từng việc:
1. Ai dùng kết quả của việc này? Không ai dùng → BỎ.
2. Việc này có lặp lại một việc khác không (chép hai lần, kiểm hai lần)? → gộp.
3. Có làm được bằng quy tắc đơn giản (công thức bảng tính, mẫu cố định) không? → không cần A.I.

Mức BỎ là bỏ **việc**, không phải bỏ **người**. Thời gian tiết kiệm được ghi vào bảng thay đổi vai trò.

## 3. Chọn mức theo rủi ro

| Câu hỏi | Nếu "có" |
|---|---|
| Việc có gửi ra ngoài (khách, đối tác, cơ quan) không? | Tối đa A.I LÀM – NGƯỜI DUYỆT |
| Có chi tiền, cam kết giá, ký kết không? | Tối đa A.I HỖ TRỢ hoặc A.I LÀM – NGƯỜI DUYỆT với người có hạn mức |
| Có chạm dữ liệu Đỏ không? | CHỈ NGƯỜI LÀM, trừ khi có đường xử lý riêng đã duyệt |
| Có ảnh hưởng quyền lợi một người (tuyển, lương, kỷ luật) không? | CHỈ NGƯỜI LÀM hoặc A.I HỖ TRỢ |
| Sai có sửa lại được trong ngày không? | Nếu "không" → hạ một mức |
| Có quy tắc rõ, ví dụ mẫu, tiêu chí đạt kiểm được không? | Nếu "không" → chưa giao A.I làm |

Việc luôn giữ quyền quyết định cho người: mục tiêu, chính sách, ngoại lệ chính sách, cấp quyền, quyết định tác động lớn, mọi thứ có hiệu lực ra bên ngoài.

## 4. Giới hạn tự làm (cho mức A.I LÀM và A.I TỰ LÀM)

Mỗi việc ghi đủ:
- **Được đọc:** thư mục, phần mềm, loại dữ liệu.
- **Được làm:** đọc / soạn nháp / gắn nhãn / cập nhật trường nào. Tách rõ đọc – đề xuất – duyệt – thay đổi.
- **Hạn mức:** số lượng mỗi ngày, số tiền tối đa, khung giờ, ngày hết hiệu lực của quyền.
- **Dừng hỏi khi:** thiếu dữ liệu, độ chắc thấp, gặp từ khóa ngoại lệ, vượt hạn mức.
- **Cấm:** gửi ra ngoài, xóa, đổi giá, đổi quyền...
- **Nhật ký:** mỗi lần làm ghi gì, lưu ở đâu.
- **Lỗi thì:** thử lại mấy lần, chuyển ai, chạy tay thế nào.
- **Dừng khẩn:** ai tắt được, tắt bằng cách nào, quay lại trạng thái cũ ra sao.

Thiếu một trong các dòng trên → việc đó chưa được ở mức tự làm.

## 5. Thay đổi vai trò

So việc của từng vai trò trước và sau: việc bớt đi, việc thêm vào (duyệt, xử lý ngoại lệ), quyền quyết định đổi thế nào, khối lượng và độ căng thẳng (xử lý toàn ca khó có thể nặng hơn), kỹ năng mới cần học, rủi ro mất kỹ năng cũ, góp ý của người làm. Không dùng số người cắt giảm làm tiêu chí đạt.

*[A.I Generated — Claude Code — 30/10/2026]*
