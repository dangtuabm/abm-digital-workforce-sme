# QUY TẮC ĐỌC TÍN HIỆU NHÂN SỰ

**Mục lục**
- I. Mục đích và lọc dữ liệu
- II. Điều kiện nguồn – chỉ số – nhóm
- III. Từ tín hiệu tới giả thuyết
- IV. Kiểm công bằng và thử nghiệm hỗ trợ
- V. Từ ngữ cấm và cách viết thay
- VI. Ví dụ đối chiếu

---

## I. MỤC ĐÍCH VÀ LỌC DỮ LIỆU

1. Chốt mục đích **trước** khi nhận dữ liệu: dùng để làm gì, cho nhóm nào, kỳ nào, ai xem, giữ bao lâu, việc gì bị cấm dùng.
2. Mục đích hợp lý: cải tiến quy trình, cân lại khối lượng việc, thiết kế hỗ trợ, đào tạo cho nhóm. Mục đích không nhận: tìm người để phạt, chọn người cho nghỉ, xếp hạng tiềm năng.
3. Bỏ khỏi dữ liệu trước khi phân tích: họ tên, mã nhân viên, số điện thoại, tin nhắn riêng, ghi chú cá nhân của quản lý, thông tin sức khỏe, gia đình, tôn giáo, chính trị.
4. Phân loại:

| Loại dữ liệu | Nhãn | Cách xử lý |
|---|---|---|
| Số tổng hợp theo nhóm, đã bỏ tên (tỷ lệ đúng hạn, lỗi trên 100 đơn, giờ việc trên giờ công) | Vàng | Dùng tài khoản A.I của công ty |
| Danh sách từng người có tên, lương, thưởng, kỷ luật, đánh giá cá nhân | Đỏ | Không đưa lên A.I; người phụ trách tổng hợp theo nhóm trước |
| Sức khỏe, thai sản, tôn giáo, dân tộc, tin nhắn riêng | Đỏ | Không đưa lên A.I trong mọi trường hợp |

Nhãn gắn theo thư mục chứa file. File nằm ở thư mục Đỏ thì dừng, không mở.

## II. ĐIỀU KIỆN NGUỒN – CHỈ SỐ – NHÓM

**Nguồn:** ghi tên phần mềm hoặc người cung cấp, ngày xuất, kỳ dữ liệu, tỷ lệ thiếu. Nguồn cũ hơn kỳ phân tích hoặc thiếu nhiều phải hiện rõ, không giấu.

**Chỉ số:** mỗi chỉ số cần đủ 6 ý:
| Ý | Ví dụ |
|---|---|
| Định nghĩa | Đơn giao đúng hạn lần đầu |
| Công thức | Số đơn đúng hạn / số đơn phải giao |
| Mẫu số | Số đơn phải giao trong kỳ |
| Đơn vị và kỳ đo | Tỷ lệ %, theo tuần, cộng dồn 4 tuần |
| Mốc so sánh | Trung bình 12 tuần trước của chính nhóm |
| Người phụ trách chỉ số | Trưởng kho |

Thiếu công thức hoặc mẫu số → không so sánh chỉ số đó, ghi "chưa đủ định nghĩa".

**Nhóm:** ghi số người từng nhóm. Nhóm dưới mức tối thiểu (mặc định 5 người nếu doanh nghiệp chưa quy định) phải gộp với nhóm khác hoặc ẩn. Cẩn thận khi cắt nhiều chiều cùng lúc: "tổ 3 · ca đêm · nữ" có thể chỉ còn 1–2 người và lộ danh tính.

## III. TỪ TÍN HIỆU TỚI GIẢ THUYẾT

Viết theo chuỗi:
1. **Tín hiệu** (quan sát): con số, mốc so sánh, độ lớn, xu hướng. Ví dụ: "lỗi đóng gói của ca đêm 4,2 trên 100 đơn, mốc 2,1".
2. **Giả thuyết** (cấp hệ thống): "đơn tăng 25% trong khi số người ca đêm giữ nguyên, có thể gây quá tải".
3. **Cách giải thích khác** (ít nhất một): "đổi mẫu thùng mới từ tuần 32", "cách ghi nhận lỗi đổi".
4. **Yếu tố gây nhiễu**: mùa vụ, cơ cấu vai trò, người mới, sự cố máy.
5. **Căn cứ ủng hộ / phản bác.**
6. **Mức tin cậy**: CAO · VỪA · THẤP, kèm lý do.
7. **Câu kiểm chứng** (phải có thể sai): "Nếu cân lại người cho ca đêm 2 chu kỳ, lỗi có về gần mốc không?"

Tương quan không phải nhân quả. Hai con số cùng đi xuống chỉ là gợi ý để hỏi tiếp.

## IV. KIỂM CÔNG BẰNG VÀ THỬ NGHIỆM HỖ TRỢ

Kiểm công bằng, ba câu:
- Có nhóm nào **ít được đo** hơn (ví dụ ca đêm không có người ghi nhận lỗi đều đặn)?
- Có nhóm nào **ít cơ hội** hơn (ít được đào tạo, ít ca thực hành, máy cũ hơn)?
- Có **tự chọn** không (chỉ người rảnh mới đi học, nên tỷ lệ học thấp ở nhóm bận)?

Thử nghiệm hỗ trợ phải có đủ: phạm vi cấp nhóm · cách làm · người phụ trách · cách đo thành công · thời gian · cách thông báo cho nhóm · cách quay lại nếu không hiệu quả. Không có thử nghiệm nào nhắm vào một người hay mang tính xử lý.

## V. TỪ NGỮ CẤM VÀ CÁCH VIẾT THAY

| Không viết | Viết thay |
|---|---|
| "Tổ B làm kém" | "Tỷ lệ đúng hạn của tổ B giảm từ 92% xuống 81%" |
| "Nhân viên thiếu động lực" | "Chưa có dữ liệu giải thích; câu cần hỏi: ..." |
| "Có dấu hiệu kiệt sức / sắp nghỉ việc" | "Giờ việc trên giờ công có sẵn ở mức 1,2, cao hơn mốc 0,85" |
| "Nhóm có vấn đề về thái độ" | Không viết; thái độ không đo được bằng dữ liệu này |
| "Nên thay trưởng ca" | Không viết; quyết định nhân sự thuộc quản lý có thẩm quyền |

## VI. VÍ DỤ ĐỐI CHIẾU

**Sai:** "Chi nhánh Bình Dương doanh số giảm 15% do nhân viên lười, đề nghị cắt thưởng tổ trưởng."
**Đúng:** "Tín hiệu: doanh số chi nhánh Bình Dương giảm 15% so với cùng kỳ (nguồn: phần mềm bán hàng, xuất ngày 28/10). Bối cảnh: chi nhánh thiếu 2 người từ tháng 8, đối thủ mở điểm bán cách 500 m. Giả thuyết: thiếu người làm giảm số khách được tư vấn. Cách giải thích khác: cạnh tranh mới; thay đổi giá. Mức tin cậy: VỪA. Câu kiểm chứng: số khách được tư vấn mỗi ngày có giảm tương ứng không? Thử nghiệm hỗ trợ: điều 1 người từ chi nhánh khác trong 4 tuần, đo số khách được tư vấn. [A.I gợi ý]"

*[A.I Generated — Claude Code — 30/10/2026]*
