# TRẠNG THÁI VÀ ĐỐI SOÁT ĐƠN HÀNG

## Mục lục
1. Tách đối tượng và mã
2. Trạng thái gợi ý
3. Bảo toàn số lượng và giá trị
4. Đối soát tiền hàng và COD
5. Chỉ số
6. Nguồn nguyên tắc tham khảo

## 1. Tách đối tượng và mã

Mỗi loại sau có mã và trạng thái riêng: **đơn** · **dòng hàng** (từng sản phẩm trong đơn) · **kiện** · **vận đơn** · **thanh toán** · **COD** (tiền thu hộ khi giao) · **yêu cầu đổi trả** · **hoàn tiền** · **ngoại lệ**.

Mỗi bản ghi giữ: mã chuẩn · mã gốc theo kênh · kênh · phần mềm gốc · thời điểm xảy ra và thời điểm nhận (kèm múi giờ) · người/hệ thống ghi · bằng chứng.

Chống trùng:
- Cùng kênh, cùng mã gốc → cùng một đơn, dù gửi lại nhiều lần.
- Khác kênh nhưng trùng khách + sản phẩm + thời điểm gần nhau → **NGHI TRÙNG**, không tự gộp; ghi lý do, chờ người xác nhận.
- Sự kiện đến muộn hoặc mâu thuẫn → ngoại lệ, không ghi đè lặng lẽ.

Tách đơn, gộp kiện, giao thay thế, hoàn về: giữ liên kết cha – con.

## 2. Trạng thái gợi ý

Tên trạng thái phải ánh xạ về trạng thái thật trong phần mềm của doanh nghiệp. A.I không cập nhật trạng thái trên phần mềm thật.

| Đối tượng | Trạng thái gợi ý |
|---|---|
| Đơn | MỚI NHẬN · CHỜ KIỂM · ĐÃ XÁC NHẬN · GIAO MỘT PHẦN · ĐÃ GIAO ĐỦ · CHỜ HỦY · ĐÃ HỦY · ĐÃ ĐÓNG |
| Dòng hàng | MỞ · ĐÃ GIỮ HÀNG · CHỜ HÀNG · ĐÃ LẤY · ĐÃ ĐÓNG GÓI · ĐÃ GỬI · ĐÃ GIAO · ĐÃ TRẢ · ĐÃ HỦY |
| Vận đơn | ĐÃ TẠO · ĐÃ BÀN GIAO VẬN CHUYỂN · ĐANG GIAO · GIAO LỖI · ĐÃ GIAO · MẤT/HỎNG · ĐANG HOÀN VỀ |
| Thanh toán / COD | CHỜ THANH TOÁN · ĐÃ THANH TOÁN · CHỜ THU COD · ĐÃ THU COD · CHỜ CHUYỂN TIỀN · ĐÃ ĐỐI SOÁT · CHÊNH LỆCH · CHỜ HOÀN · ĐÃ HOÀN |
| Đổi trả | ĐÃ YÊU CẦU · ĐANG XÉT ĐIỀU KIỆN · ĐÃ CHẤP THUẬN · HÀNG ĐANG VỀ · ĐÃ NHẬN · ĐÃ KIỂM · CHỜ QUYẾT PHƯƠNG ÁN · ĐÃ ĐÓNG |

Chuyển trạng thái chỉ hợp lệ khi có sự kiện, nguồn, thời điểm, người ghi và bằng chứng.

## 3. Bảo toàn số lượng và giá trị

- Số lượng (theo dòng hàng): **đặt = đã hủy + đang chờ/mở + đã giao**. Đã đóng gói, đã gửi, đã giao, đã trả phải khớp theo dòng hàng và kiện.
- Giá trị: **giá gốc − giảm giá được duyệt + thuế + phí giao − hoàn/ghi có = tiền phải thu** theo chính sách và nguồn. Không bịa công thức, cách làm tròn, ngưỡng.
- Lệch ở đâu ghi ngoại lệ ở đó, có số cụ thể.

## 4. Đối soát tiền hàng và COD

Chuỗi đối soát COD:

**Đơn đã giao có bằng chứng → đơn vị vận chuyển ghi đã thu COD → bảng kê chuyển tiền của đơn vị vận chuyển → tiền về sao kê ngân hàng → trừ phí, thuế theo hợp đồng → chuyển kế toán ghi sổ.**

- "ĐÃ GIAO" không tự sinh "ĐÃ THU COD" hay "ĐÃ ĐỐI SOÁT".
- Với sàn TMĐT: tiền sàn chuyển về = doanh thu đơn − phí sàn − phí thanh toán − phí vận chuyển (nếu có) − hoàn tiền; các khoản phí lấy từ bảng kê của sàn, không tự tính theo tỷ lệ đoán.
- Chênh lệch ghi: mã đơn · số phải nhận · số đã nhận · chênh lệch · nguồn mỗi số · lý do nghi ngờ · người phụ trách · trạng thái.
- Lý do chênh lệch thường gặp (phải kiểm): phí tính sai · đơn hoàn chưa trừ · đơn giao một phần · tiền về muộn sang kỳ sau · nhập trùng · bảng kê thiếu đơn.
- Ngưỡng chênh lệch cho phép do kế toán chốt; chưa có ngưỡng thì báo mọi chênh lệch khác 0.

## 5. Chỉ số

Mỗi chỉ số ghi: tên · đơn vị tính (đơn, dòng hàng, kiện) · công thức · tử số, mẫu số · điều kiện tính/loại trừ · kỳ, múi giờ · nguồn · ngày dữ liệu · người phụ trách. Không trộn mẫu số đơn với mẫu số kiện.

Chỉ số thường dùng (chỉ khi dữ liệu cho phép):
- Tỷ lệ giao đúng hạn = đơn giao trong hạn cam kết ÷ đơn đã giao.
- Tỷ lệ giao thành công lần đầu = vận đơn giao được ở lần đầu ÷ vận đơn đã giao thử.
- Tỷ lệ hủy, tỷ lệ hoàn về, tỷ lệ đổi trả = số đơn tương ứng ÷ tổng đơn cùng kỳ.
- Thời gian xử lý đơn = từ lúc nhận đơn tới lúc bàn giao vận chuyển.
- Số đơn treo = đơn không đổi trạng thái quá số giờ/ngày doanh nghiệp quy định.
- Tuổi COD chưa về = số ngày từ lúc giao thành công tới hôm nay với đơn chưa có tiền về.

## 6. Nguồn nguyên tắc tham khảo

Các chuẩn quốc tế về chuỗi đặt hàng – giao hàng – thanh toán (ví dụ bộ chuẩn GS1) và hướng dẫn xử lý khiếu nại ISO 10002 chỉ dùng làm nguyên tắc tham khảo; không thay chính sách doanh nghiệp, điều khoản sàn, hợp đồng vận chuyển hay pháp luật. Luôn đối chiếu bản hiện hành tại thời điểm làm.

*[A.I Generated — Claude Code — 30/10/2026]*
