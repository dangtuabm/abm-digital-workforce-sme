# PHÂN LOẠI LỖI VÀ HƯỚNG XỬ LÝ

**Mục lục:** 1. Ba mức lỗi · 2. Lỗi thường gặp và hướng xử lý đề xuất · 3. Lịch nhắc hạn · 4. Ví dụ báo cáo

## 1. Ba mức lỗi (Bước 6)

| Mức | Ý nghĩa | Ví dụ | Việc ngay |
|---|---|---|---|
| **CHẶN** | Đề xuất chưa hạch toán, chưa đưa vào kê khai cho đến khi kế toán xử lý xong | Sai mã số thuế người mua; hóa đơn đã bị hủy theo kết quả tra; hóa đơn trùng; sai số tiền | Báo kế toán trong ngày |
| **CẦN XỬ LÝ** | Có sai sót cần sửa hoặc bổ sung trước kỳ kê khai | Sai địa chỉ, tên viết tắt khác hồ sơ; thiếu hồ sơ đi kèm hóa đơn điều chỉnh; thuế suất khác danh mục | Đưa vào danh sách cần xử lý, có hạn |
| **CẢNH BÁO** | Chưa phải lỗi, cần người xem | Dấu hiệu rủi ro người bán; nhảy số đầu ra có lý do chưa rõ; ngày lập lệch ngày giao hàng | Kế toán trưởng xem |

Mức CHẶN chỉ là **đề xuất của bộ kiểm**. Hạch toán hay không, kê khai hay không do kế toán thuế, kế toán trưởng quyết sau khi đối chiếu quy định, cần người có chuyên môn xác nhận.

## 2. Lỗi thường gặp và hướng xử lý đề xuất

| Lỗi | Chế độ | Mức gợi ý | Hướng xử lý đề xuất (kế toán quyết, theo quy định hiện hành) | Người xử lý |
|---|---|---|---|---|
| Sai tên, mã số thuế, địa chỉ người mua (là doanh nghiệp mình) | Đầu vào | CHẶN / CẦN XỬ LÝ | Đề nghị người bán xử lý hóa đơn theo quy định; giữ hóa đơn ở trạng thái chờ | Kế toán + người phụ trách mua hàng |
| Hóa đơn đã bị hủy, bị thay thế theo kết quả tra | Đầu vào | CHẶN | Yêu cầu người bán cung cấp hóa đơn thay thế; không dùng hóa đơn đã bị thay | Kế toán |
| Trùng hóa đơn | Đầu vào | CHẶN | Giữ một bản, kiểm đã hạch toán hai lần chưa (việc đối soát) | Kế toán |
| Sai số học (thành tiền, tiền thuế, tổng) | Cả hai | CHẶN | Đầu vào: đề nghị người bán xử lý. Đầu ra: kế toán xử lý theo quy định | Kế toán |
| Thuế suất khác danh mục doanh nghiệp | Cả hai | CẦN XỬ LÝ | Ghi "cần người có chuyên môn xác nhận"; nếu danh mục đúng thì xử lý hóa đơn, nếu danh mục sai thì cập nhật danh mục | Kế toán thuế + người có chuyên môn |
| Hàng hóa chưa có trong danh mục thuế suất | Cả hai | CẦN XỬ LÝ | Bổ sung danh mục, người có chuyên môn xác nhận | Kế toán thuế |
| Thông tin người mua khác hồ sơ khách | Đầu ra | CẦN XỬ LÝ | Kiểm hồ sơ khách mới nhất; xin khách xác nhận thông tin xuất hóa đơn | Kế toán + nhân viên kinh doanh |
| Nhảy số, khoảng trống số hóa đơn | Đầu ra | CẢNH BÁO | Kiểm trên phần mềm hóa đơn nguyên nhân (hóa đơn nháp, bị hủy, lỗi đồng bộ) | Kế toán |
| Đơn đã giao chưa có hóa đơn | Đầu ra | CẦN XỬ LÝ | Kiểm thời điểm lập hóa đơn theo quy định, cần người có chuyên môn xác nhận | Kế toán |
| Hóa đơn điều chỉnh/thay thế thiếu tham chiếu, thiếu hồ sơ đi kèm | Cả hai | CẦN XỬ LÝ | Bổ sung hồ sơ theo quy tắc doanh nghiệp đã xác nhận | Kế toán |
| Khoản lớn thiếu hợp đồng, chứng từ thanh toán theo quy tắc nội bộ | Đầu vào | CẢNH BÁO | Bổ sung chứng từ; điều kiện khấu trừ cần người có chuyên môn xác nhận | Kế toán + người phụ trách mua hàng |

Khi người giao yêu cầu, A.I soạn **nháp** thư đề nghị nhà cung cấp xử lý hóa đơn (nêu số, ký hiệu, ngày, sai ở đâu, đề nghị xử lý theo quy định). Kế toán duyệt và tự gửi.

## 3. Lịch nhắc hạn (Bước 7)
- Nguồn duy nhất của việc và hạn: `lich-han-thue.csv` do doanh nghiệp tự điền, người có chuyên môn xác nhận; hoặc sổ nghĩa vụ tuân thủ của doanh nghiệp nếu có.
- A.I chỉ thêm: ngày nhắc trước hạn (doanh nghiệp chọn số ngày; chưa chọn thì đề xuất nhắc trước 5 ngày làm việc và 1 ngày làm việc, gắn [GIẢ ĐỊNH]), người nhận nhắc, việc chuẩn bị (danh sách hóa đơn còn mở cần xử lý trước hạn).
- Không tự tạo hạn từ hiểu biết chung; không đổi hạn doanh nghiệp đã điền. Nghi hạn đã thay đổi theo quy định mới → ghi "cần xác nhận lại", chuyển việc tuân thủ pháp lý.
- Hạn rơi vào ngày nghỉ: ghi "cần xác nhận hạn thực tế", không tự dời.

## 4. Ví dụ báo cáo (số liệu minh họa)

Công ty cơ khí 40 người, rà hóa đơn đầu vào tháng 10:

"[DỮ KIỆN] 312 hóa đơn, 296 ĐẠT, 9 lỗi CHẶN, 7 CẦN XỬ LÝ. Lỗi CHẶN: 5 hóa đơn ghi sai mã số thuế công ty (cùng một nhà cung cấp vật tư), 2 hóa đơn trùng, 2 hóa đơn có trạng thái đã bị thay thế theo kết quả chị Ngọc tra ngày 28/10. [SUY LUẬN] Lỗi sai mã số thuế lặp ở một nhà cung cấp — có thể họ đang lưu sai hồ sơ công ty. Việc cần Anh/Chị quyết: có gửi đề nghị nhà cung cấp này cập nhật hồ sơ và xử lý 5 hóa đơn không (em đã soạn nháp thư). 14 dòng hàng chưa có trong danh mục thuế suất: CHƯA KIỂM ĐƯỢC, cần người có chuyên môn bổ sung danh mục."

*[A.I Generated — Claude Code — 30/10/2026]*
