# QUY TẮC CUNG ỨNG, KHO VÀ TÀI SẢN

**Mục lục**
- 1. Thứ tự nguồn đúng
- 2. Hợp đồng dữ liệu và mã hàng
- 3. Tồn kho và dự báo
- 4. Mua hàng và nhà cung cấp
- 5. Kho vận, chất lượng, truy xuất
- 6. Tài sản và bảo trì
- 7. Kiểm soát và kịch bản
- 8. Điều kiện dừng

---

## 1. Thứ tự nguồn đúng

Khi các nguồn nói khác nhau, ưu tiên theo thứ tự:
1. Yêu cầu an toàn, chất lượng, sản phẩm, môi trường, thương mại, hải quan đang áp dụng cho mặt hàng, địa điểm (đối chiếu văn bản pháp luật hiện hành, cần người có chuyên môn xác nhận).
2. Chính sách công ty đã duyệt, hợp đồng, quy cách kỹ thuật, mục tiêu phục vụ, mức rủi ro chấp nhận, ma trận phân quyền.
3. Số liệu đã đối soát trên phần mềm bán hàng / kho / kế toán, biên bản kiểm kê, biên bản kiểm tra, ảnh chụp số liệu tại thời điểm chốt.
4. Hồ sơ có phiên bản của nhà cung cấp, đơn vị vận chuyển, đơn vị bảo trì; số liệu thị trường được phép dùng.
5. Kết quả mô hình, lời kể, số liệu A.I đọc từ ảnh/tài liệu chưa kiểm — luôn gắn nhãn, không nâng thành sự thật khi chưa rà.

## 2. Hợp đồng dữ liệu và mã hàng

- **Phạm vi:** công ty, kho, cửa hàng, mã hàng, lô, serial, tài sản, nhà cung cấp, kỳ.
- **Đo lường:** đơn vị tính và quy đổi (thùng ↔ hộp ↔ cái), tiền tệ, lịch và múi giờ, số lượng, tình trạng, chi phí.
- **Bằng chứng:** nguồn, phiên bản, ngày chốt số, quyền, độ mới, độ tin, phần mềm gốc, các bước biến đổi số liệu.
- **Phân quyền:** người lập kế hoạch, người mua, người duyệt, người nhận, người kiểm, thủ kho, người bảo trì, người giữ tài sản, người thanh lý, người rà soát — tách nhiệm.

Mã hàng, quy đổi, tình trạng hay độ mới chưa rõ: ghi CHƯA RÕ và chặn đề xuất lớn.

## 3. Tồn kho và dự báo

- Giữ tách: đơn đặt, hàng đã giao, ngày hết hàng (bán mất), trả hàng, khuyến mãi, đơn bất thường một lần, hàng thay thế.
- **Nhu cầu bị cắt khi hết hàng không bằng 0.** Ngày hết hàng phải ghi riêng, không coi là ngày không có nhu cầu.
- Dự báo ghi: cấp chi tiết (mã/nhóm, tuần/tháng), tầm xa, cách làm, phiên bản, kỳ dùng để học và kỳ dùng để kiểm, sai số, khoảng, giả định, cách so với cách đơn giản (ví dụ lấy trung bình 3 kỳ gần nhất).
- Đối soát: đầu kỳ + mọi loại nhập − mọi loại xuất ± điều chỉnh = cuối kỳ. Không gộp hàng cách ly, hết hạn, hỏng, chưa rõ vào hàng bán được.
- Mức tồn an toàn, điểm đặt hàng lại, chu kỳ xem lại, ABC/XYZ, FIFO/FEFO, hàng thay thế phụ thuộc mức phục vụ đã duyệt, biến động, hạn dùng, sức chứa và chính sách.
- Mỗi đề xuất có kịch bản, độ nhạy, điều kiện kích hoạt, người theo dõi, cách quay lại; không tự đổi danh mục hay mức tồn trên phần mềm.

## 4. Mua hàng và nhà cung cấp

- Yêu cầu và quy cách, số lượng, đơn vị, thời gian giao, tiêu chí nghiệm thu, bảo hành, an toàn dữ liệu, yêu cầu tuân thủ phải có **trước** khi so giá.
- Giữ phiên bản báo giá, hợp đồng, thời hạn hiệu lực, năng lực, độ dao động thời gian giao, số lượng đặt tối thiểu, chất lượng, khả năng liên tục, mức phụ thuộc một nguồn, xung đột lợi ích, quan hệ liên quan.
- Tổng chi phí tách: giá, vận chuyển, thuế phí (căn cứ), lưu kho, vốn, lỗi chất lượng, dừng máy, tích hợp, bảo trì, thanh lý.
- Trọng số chấm nhà cung cấp phải được duyệt và kiểm độ nhạy; **thiếu bằng chứng không phải điểm 0**, ghi THIẾU.
- **Luận điểm đàm phán** dựa trên số liệu mua: sản lượng mua 12 tháng, mức tăng trưởng, lịch sử giao trễ, giá thị trường tham khảo, phương án thay thế — đề xuất xin giảm thời gian giao, giãn hạn thanh toán, hạ số lượng đặt tối thiểu. Người có quyền đàm phán.
- **Rủi ro đứt gãy:** nhà cung cấp chính chậm, đóng cửa, thiên tai, tắc tuyến vận chuyển → phương án B (nguồn thứ hai đã kiểm, tồn đệm cho mã nhóm A, hàng thay thế), điều kiện kích hoạt, người phụ trách.
- Phương án đơn mua, yêu cầu báo giá, chọn nhà cung cấp chỉ ở dạng nháp CHỜ QUYẾT; không liên hệ, không cam kết, không đổi tài khoản ngân hàng.

## 5. Kho vận, chất lượng, truy xuất

- **Bố trí kho:** mã nhóm A, lấy nhiều để gần cửa xuất, tầm tay; hàng nặng để dưới; hàng có hạn xếp theo FEFO (hết hạn trước xuất trước), hàng khác theo FIFO (nhập trước xuất trước).
- **Vận chuyển:** tuyến, phương thức, đơn vị vận chuyển, sức chở, người chịu trách nhiệm hàng trên đường, đóng gói, nhiệt độ, hàng nguy hiểm, khung giờ giao, phương án dự phòng.
- **Truy xuất:** ghi đối tượng (lô, serial), bên liên quan, địa điểm, các sự kiện quan trọng (nhận, chuyển, chia lô, gộp lô, xuất) kèm dữ liệu chính; giữ liên kết lô – đơn hàng.
- **Nhận hàng không phải nghiệm thu:** kiểm tra, cách ly, giải phóng, hàng không phù hợp, khắc phục – phòng ngừa, thu hồi đều cần người có quyền và bằng chứng.
- **Diễn tập truy xuất:** chọn một lô, thử lần ra đã bán cho ai, còn ở đâu, mất bao lâu, có sót không — không thực hiện thu hồi thật.
- **Công cụ:** gợi ý theo quy mô — sổ/bảng tính có mã lô → mã vạch và máy quét → phần mềm quản lý kho; chỉ đề xuất, người quyết đầu tư.

## 6. Tài sản và bảo trì

- Sổ tài sản: mã, nhóm, người giữ, vị trí, mức trọng yếu (dừng thì ảnh hưởng gì), tình trạng, giờ chạy/mức sử dụng, thời gian dừng, bảo hành, phụ tùng, chi phí, phụ thuộc.
- Vòng đời: nhu cầu → mua → nhận → nghiệm thu đưa vào dùng → vận hành → bảo trì → nâng cấp → ngừng dùng → thanh lý; mỗi bước có người có quyền và bằng chứng.
- Phương án bảo trì ghi: kiểu hỏng, dấu hiệu tình trạng, hậu quả an toàn, căn cứ chu kỳ, phụ tùng, công, thời gian dừng, phương án tạm thời, người có quyền giao việc.
- Dự đoán hỏng không phải sự thật; không lệnh bảo trì, không bỏ qua an toàn, không đưa vào dùng hay thanh lý khi chưa có người đủ thẩm quyền duyệt.

## 7. Kiểm soát và kịch bản

- Tách nhiệm: đề nghị mua, tìm nguồn, duyệt, nhận hàng, kiểm tra, điều chỉnh tồn, nhận hóa đơn, thanh toán, giữ tài sản, bảo trì, thanh lý không dồn vào một người.
- Phát hiện: đơn trùng hoặc chia nhỏ để lách hạn mức, đổi dữ liệu gốc hoặc tài khoản ngân hàng, xung đột lợi ích, hàng giả, bị tráo, hàng thay thế chưa duyệt, điều chỉnh/xóa sổ tồn bất thường, bỏ qua an toàn.
- Tối ưu trên nhiều mặt cùng lúc: chi phí, vốn, mức đáp ứng, chất lượng, an toàn, sức chứa, môi trường, liên tục. **Ràng buộc cứng không được lấy trung bình để bù.**
- Mỗi kịch bản có: điểm xuất phát, giả định, độ bất định, độ nhạy, điều kiện kích hoạt, rào chắn, người phụ trách, điều kiện dừng/quay lại.

## 8. Điều kiện dừng

Dừng ở CHƯA SẴN SÀNG khi: thiếu mã hàng, đơn vị, nguồn, người quyết; tồn chưa cân ở mức trọng yếu; dự báo chưa kiểm lại; còn giấu hàng cách ly, cận hạn, lỗi; nhận định về nhà cung cấp/tài sản không có căn cứ; xung đột an toàn – chất lượng; hoặc được yêu cầu thực hiện hành động.

Trạng thái cuối cùng là CHỜ NGƯỜI CÓ QUYỀN QUYẾT. Mọi hành động mua, kho, vận chuyển, bảo trì, hệ thống nằm ngoài Skill.

Cảnh báo: hồ sơ đạt kiểm không chứng minh dự báo đúng, tồn thực tế đúng, nhà cung cấp đủ năng lực, chất lượng – an toàn đạt, máy móc đúng tình trạng hay ai đó có quyền thực hiện.

*[A.I Generated — Claude Code — 30/10/2026]*
