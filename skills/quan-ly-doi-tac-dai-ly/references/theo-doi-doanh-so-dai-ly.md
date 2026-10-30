# THEO DÕI DOANH SỐ ĐẠI LÝ

## 1. Phân biệt các loại số

| Loại số | Nghĩa | Nguồn thường gặp | Lưu ý |
|---|---|---|---|
| **Bán vào** | Doanh nghiệp xuất hàng, xuất hóa đơn cho đại lý | Phần mềm bán hàng, phần mềm kế toán | Là số chắc nhất nhưng không cho biết đại lý đã bán được cho khách hay chưa |
| **Bán ra** | Đại lý bán tới khách cuối hoặc cửa hàng cấp dưới | Báo cáo đại lý gửi, phần mềm của đại lý | Thường thiếu, chậm, tự khai — ghi rõ độ tin cậy |
| **Trả hàng** | Đại lý trả lại hàng | Phiếu nhập trả | Tách riêng, không trừ lẫn vào kỳ khác |
| **Tồn kho đại lý** | Hàng còn tại đại lý cuối kỳ | Báo cáo đại lý, kiểm kê | Có thể ước tính = tồn đầu + bán vào − bán ra − trả hàng, gắn [GIẢ ĐỊNH] |

Không gộp ba loại số đầu vào một cột. Mỗi bảng ghi rõ đang dùng loại nào.

## 2. Chỉ số và công thức

| Chỉ số | Công thức | Ghi chú |
|---|---|---|
| Doanh số thuần kỳ | Bán vào − Trả hàng trong kỳ | Giá trị trước hay sau chiết khấu, thuế: theo quy ước của doanh nghiệp, ghi rõ |
| % hoàn thành chỉ tiêu | Doanh số thuần kỳ ÷ Chỉ tiêu kỳ × 100 | Chỉ tính khi có chỉ tiêu do doanh nghiệp đặt |
| Tăng trưởng so kỳ trước | (Kỳ này − Kỳ trước) ÷ Kỳ trước × 100 | Kỳ trước = 0 thì ghi "không so được" |
| Tăng trưởng so cùng kỳ | (Kỳ này − Cùng kỳ năm trước) ÷ Cùng kỳ năm trước × 100 | Nên dùng cho ngành có mùa vụ |
| Tỷ trọng | Doanh số thuần đại lý ÷ Tổng doanh số thuần kênh × 100 | Dùng để tìm nhóm đại lý chủ lực |
| Số ngày từ lần đặt cuối | Ngày lập báo cáo − Ngày đơn gần nhất | Dấu hiệu sớm của ngừng đặt hàng |
| Tồn kho quy ra ngày bán | Tồn kho cuối kỳ ÷ Bán ra bình quân mỗi ngày | Chỉ tính khi có số bán ra |
| Độ phủ sản phẩm | Số mã hàng đại lý có đặt ÷ Số mã hàng đại lý được phép bán | Đại lý chỉ lấy vài mã quen |

Mọi chỉ số ghi kỳ, đơn vị tiền, ngày xuất dữ liệu. Làm tròn ở bước cuối.

## 3. Xếp nhóm đại lý

| Nhóm | Điều kiện đề xuất (doanh nghiệp sửa theo chính sách của mình) |
|---|---|
| **TĂNG TRƯỞNG** | Tăng so cùng kỳ hoặc kỳ trước vượt ngưỡng tăng (đề xuất +10%) |
| **ỔN ĐỊNH** | Biến động trong khoảng ngưỡng (đề xuất ±10%) |
| **SỤT GIẢM** | Giảm vượt ngưỡng giảm (đề xuất −10%) hoặc 2 kỳ liền giảm |
| **NGỪNG ĐẶT HÀNG** | Số ngày từ lần đặt cuối vượt ngưỡng (đề xuất gấp 2 lần chu kỳ đặt hàng bình thường của chính đại lý đó) |
| **MỚI** | Chưa đủ một kỳ so sánh |

Các ngưỡng trong cột trên là **đề xuất mặc định** — khi dùng phải gắn [GIẢ ĐỊNH] cho đến khi doanh nghiệp chốt. Không áp một ngưỡng chung cho mọi ngành.

Thêm một lớp **chủ lực / còn lại**: sắp xếp đại lý theo doanh số giảm dần, nhóm đại lý cộng dồn chiếm khoảng 80% doanh số là nhóm chủ lực. Đại lý chủ lực mà SỤT GIẢM được đưa lên đầu danh sách cảnh báo.

## 4. Cảnh báo

Mỗi cảnh báo ghi: mã đại lý · loại cảnh báo · số liệu chứng minh · so với ngưỡng nào · giả thuyết lý do · cách kiểm · người phụ trách · trạng thái.

Loại cảnh báo thường gặp:
- Sụt doanh số so cùng kỳ hoặc 2 kỳ liền.
- Ngừng đặt hàng quá ngưỡng.
- Tồn kho quy ra ngày bán cao bất thường (nếu có số bán ra).
- Độ phủ sản phẩm thấp: chỉ lấy 1–2 mã.
- Trả hàng lớn bất thường.
- Công nợ quá hạn (chỉ gắn cờ, chuyển kế toán; không nhắc nợ trong Skill này).
- Số đại lý báo bán ra lệch xa số bán vào trong nhiều kỳ.

Giả thuyết lý do phổ biến (phải kiểm, không được kết luận ngay): mùa vụ · giá của mình hoặc đối thủ thay đổi · thiếu hàng, giao trễ · đổi người phụ trách vùng · đại lý gặp khó khăn tài chính · đại lý chuyển sang hãng khác · chính sách mới chưa phổ biến tới đại lý.

## 5. Hành động gợi ý theo nhóm (tất cả CHỜ DUYỆT)

| Nhóm | Hành động gợi ý |
|---|---|
| TĂNG TRƯỞNG | Ghi nhận, tìm cách làm hay để nhân rộng; xem có cần tăng hạn mức, ưu tiên giao hàng |
| ỔN ĐỊNH | Duy trì lịch thăm; đề xuất mở thêm mã hàng nếu độ phủ thấp |
| SỤT GIẢM | Người phụ trách vùng gọi hoặc thăm để kiểm giả thuyết; xem tồn kho, giá, giao hàng |
| NGỪNG ĐẶT HÀNG | Ưu tiên liên hệ trong tuần (người liên hệ, không phải A.I); kiểm công nợ và lý do |
| MỚI | Theo dõi đơn thứ hai, hỗ trợ trưng bày, hướng dẫn chính sách |

A.I chỉ soạn danh sách và nội dung gợi ý; người phụ trách quyết định và liên hệ.

## 6. Cách đọc báo cáo cho lãnh đạo

Ba dòng đầu: tổng doanh số kênh và % chỉ tiêu · số đại lý theo từng nhóm · 3–5 việc cần quyết. Bảng chi tiết để sau. Nếu chỉ có số bán vào, ghi ngay dòng đầu: "Báo cáo dựa trên số bán vào; chưa có số bán ra".

*[A.I Generated — Claude Code — 30/10/2026]*
