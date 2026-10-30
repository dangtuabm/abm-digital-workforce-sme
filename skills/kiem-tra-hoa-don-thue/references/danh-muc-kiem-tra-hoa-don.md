# DANH MỤC KIỂM TRA HÓA ĐƠN

**Mục lục:** 1. Chuẩn hóa · 2. Bảy nhóm kiểm · 3. Khác biệt đầu vào – đầu ra · 4. Tra cứu trạng thái trên cổng của cơ quan thuế · 5. Dấu hiệu rủi ro người bán · 6. Lưu ý về quy định

**Lưu ý chung:** danh sách trường và quy tắc dưới đây là **khung kiểm thực tiễn** để phát hiện sai sót. Trường nào bắt buộc, cách xử lý ra sao phải đối chiếu văn bản pháp luật hiện hành về hóa đơn, chứng từ và thuế, cần người có chuyên môn xác nhận. Doanh nghiệp bổ sung, bỏ bớt theo xác nhận đó.

## 1. Chuẩn hóa (Bước 3)
| Trường | Cách chuẩn hóa | Lỗi hay gặp |
|---|---|---|
| Mã số thuế | Chuỗi ký tự, giữ số 0 ở đầu, bỏ khoảng trắng, dấu chấm; giữ phần đuôi chi nhánh nếu có | Excel cắt số 0 đầu; ghép nhầm mã chi nhánh |
| Ký hiệu, số hóa đơn | Giữ nguyên chữ hoa, số 0 đầu | Số hóa đơn bị đổi thành dạng số, mất số 0 |
| Ngày | Ngày/tháng/năm; tách ngày lập và ngày ký số nếu có cả hai | Đảo ngày – tháng |
| Số tiền | Tách tiền hàng trước thuế, tiền thuế, tổng thanh toán; chiết khấu ghi riêng | Đọc dấu chấm phân cách thành số thập phân |
| Tên, địa chỉ | Bỏ khoảng trắng thừa; giữ nguyên chữ để so | Viết tắt "CTY", "TNHH" khác nhau |

Kiểm sau chuẩn hóa: số hóa đơn và tổng tiền bằng file gốc.

## 2. Bảy nhóm kiểm (Bước 4)

| Nhóm | Kiểm gì | Kết quả |
|---|---|---|
| **A. Đủ trường** | Có đủ các trường doanh nghiệp đã xác nhận là bắt buộc: thông tin người bán, người mua, ký hiệu, số, ngày, tên hàng hóa – dịch vụ, đơn vị tính, số lượng, đơn giá, thành tiền, thuế suất, tiền thuế, tổng thanh toán, chữ ký số, mã của cơ quan thuế nếu là loại hóa đơn có mã | ĐẠT / LỖI (ghi trường thiếu) |
| **B. Người bán – người mua** | Đầu vào: tên, mã số thuế, địa chỉ người mua trùng hồ sơ doanh nghiệp; người bán có trong danh mục nhà cung cấp. Đầu ra: thông tin người mua trùng hồ sơ khách do khách cung cấp | ĐẠT / LỖI / CẢNH BÁO (khác cách viết nhưng cùng mã số thuế) |
| **C. Số học** | Số lượng × đơn giá = thành tiền; tổng các dòng; tiền thuế = tiền hàng × thuế suất (theo quy tắc làm tròn doanh nghiệp ghi); tổng thanh toán; số tiền bằng chữ khớp bằng số | ĐẠT / LỖI (ghi chênh lệch) |
| **D. Thuế suất** | Thuế suất từng dòng hàng khớp `danh-muc-thue-suat-doanh-nghiep.csv` theo mã hàng hoặc nhóm hàng và theo thời hạn áp dụng doanh nghiệp đã ghi | ĐẠT / LỖI / CHƯA KIỂM ĐƯỢC (hàng chưa có trong danh mục, hoặc danh mục chưa xác nhận) |
| **E. Trùng, nhảy số** | Trùng: cùng mã số thuế người bán + ký hiệu + số. Đầu ra: số hóa đơn liên tục theo từng ký hiệu, chỉ ra khoảng trống, số lặp | ĐẠT / LỖI / CẢNH BÁO |
| **F. Trạng thái** | Hóa đơn đã bị hủy, bị thay thế, có hóa đơn điều chỉnh đi kèm chưa; hóa đơn điều chỉnh/thay thế có tham chiếu hóa đơn gốc và hồ sơ đi kèm theo quy tắc doanh nghiệp | ĐẠT / LỖI / CHƯA TRA |
| **G. Thời điểm và chứng từ đi kèm** | Ngày lập so với ngày giao hàng, nghiệm thu, thanh toán theo quy tắc doanh nghiệp đã xác nhận; có hợp đồng, biên bản, chứng từ thanh toán khi quy tắc nội bộ yêu cầu (ví dụ khoản trên ngưỡng doanh nghiệp tự đặt) | ĐẠT / CẢNH BÁO / CHƯA KIỂM ĐƯỢC |

Mỗi kết quả LỖI, CẢNH BÁO ghi căn cứ cụ thể: trường nào, giá trị nào, so với nguồn nào.

## 3. Khác biệt đầu vào – đầu ra
| | Đầu vào | Đầu ra |
|---|---|---|
| Trọng tâm | Hóa đơn có đúng là của doanh nghiệp, người bán có thật, còn hiệu lực | Doanh nghiệp xuất đúng người, đúng số, đúng thuế suất, đủ số, đúng lúc |
| Đối chiếu với | Hồ sơ doanh nghiệp, danh mục nhà cung cấp, kết quả tra cứu | Hồ sơ khách, đơn hàng (tổng tiền), danh mục sản phẩm – thuế suất |
| Thêm | Dấu hiệu rủi ro người bán (mục 5) | Đơn đã giao mà chưa có hóa đơn; hóa đơn xuất mà đơn hàng đã hủy |
| Người xử lý lỗi | Người bán xử lý, kế toán theo dõi | Kế toán doanh nghiệp xử lý theo quy định |

Khớp từng dòng số lượng, đơn giá với đơn đặt hàng, phiếu nhập là việc đối soát chứng từ, không làm ở đây.

## 4. Tra cứu trạng thái trên cổng của cơ quan thuế (Bước 5)
- A.I lập **danh sách cần tra**: mã số thuế người bán, ký hiệu, số, ngày, tổng tiền.
- Người tra là kế toán, trên cổng tra cứu chính thức của cơ quan thuế mà doanh nghiệp đang dùng; hoặc qua **kết nối chính thức** nếu doanh nghiệp đã thiết lập (cần kết nối). A.I không đăng nhập bằng tài khoản doanh nghiệp.
- Kết quả đưa vào bảng: trạng thái hóa đơn, trạng thái mã số thuế người bán, **ngày tra**, người tra, bằng chứng (ảnh chụp, file).
- Kết quả tra quá cũ (doanh nghiệp tự đặt số ngày) trước khi kê khai: đề xuất tra lại.
- Không có kết quả: ghi CHƯA TRA; không suy ra trạng thái từ thông tin khác.

## 5. Dấu hiệu rủi ro người bán (đầu vào)
Chỉ là dấu hiệu, không kết luận. Có từ hai dấu hiệu trở lên → chuyển kế toán trưởng xem trước khi hạch toán:
- Nhà cung cấp mới, giao dịch lần đầu với giá trị lớn.
- Kết quả tra cho thấy trạng thái mã số thuế bất thường.
- Hàng hóa, dịch vụ trên hóa đơn không liên quan ngành nghề kinh doanh của người bán hoặc nhu cầu của doanh nghiệp.
- Nhiều hóa đơn số liền nhau, cùng ngày, giá trị tròn.
- Thông tin thanh toán (tài khoản nhận) không trùng tên người bán.
- Không có hợp đồng, biên bản giao nhận dù quy tắc nội bộ yêu cầu.

## 6. Lưu ý về quy định
- Không ghi thuế suất, ngưỡng, thời hạn, mức phạt, số hiệu văn bản trong bộ kiểm nếu người có chuyên môn chưa cung cấp.
- Quy định về hóa đơn, thuế có thể thay đổi. Mỗi lần rà cuối kỳ, nhắc kế toán kiểm danh mục thuế suất và bảng hạn còn hiệu lực; nếu nghi quy định đã đổi, chuyển việc tuân thủ pháp lý và người có chuyên môn.

*[A.I Generated — Claude Code — 30/10/2026]*
