# QUY TẮC PHÁT HIỆN VÀ ĐIỀU TRA BẤT THƯỜNG

**Mục lục**
- 1. Giữ bằng chứng
- 2. Kiểm chất lượng dữ liệu
- 3. Mức nền so sánh được
- 4. Chọn cách phát hiện
- 5. Phân nhóm, giả thuyết và nguyên nhân
- 6. Phương án hành động và rút kinh nghiệm
- 7. Sáu rủi ro phải ghi
- 8. Ví dụ đối chiếu
- 9. Nguồn nguyên tắc

---

## 1. Giữ bằng chứng

Mỗi lần điều tra ghi: nguồn (phần mềm, file, người cung cấp) · phiên bản hoặc ngày trích · cấu trúc bảng, mỗi dòng là gì (một đơn hàng, một phiếu chi) · thời điểm ghi nhận, múi giờ, đơn vị · định nghĩa chỉ số, tử số, mẫu số, bộ lọc · công thức hoặc câu truy vấn đã dùng · quyền dùng. Dữ liệu gốc **chỉ đọc**; mọi phép thử chạy trên bản sao.

## 2. Kiểm chất lượng dữ liệu (luôn làm trước)

| Kiểm | Câu hỏi | Ví dụ SME |
|---|---|---|
| Độ mới | Dữ liệu đã cập nhật đến kỳ đang xét chưa? | Chi nhánh Bình Dương chưa đồng bộ đơn 3 ngày cuối tháng |
| Độ đủ | Có thiếu chi nhánh, kênh, ngày nào không? | Sàn TMĐT chưa đổ đơn về phần mềm bán hàng |
| Trùng | Có dòng bị nhập hai lần? | Phiếu nhập kho nhập lại sau khi sửa |
| Rỗng | Ô trống bị hiểu thành 0? | Ô giá vốn trống làm biên lãi vọt lên 100% |
| Thời điểm | Ghi theo ngày phát sinh hay ngày nhập? | Hóa đơn tháng 9 nhập vào ngày 2/10 |
| Sửa hồi tố | Số kỳ trước có bị sửa? | Kế toán điều chỉnh chi phí khấu hao tháng trước |
| Đổi cách tính | Có đổi phần mềm, đổi mã hàng, đổi chính sách? | Đổi từ ghi doanh thu gồm VAT sang chưa VAT |

Thiếu dữ liệu **không** bằng 0. Lỗi dữ liệu là ứng viên giải thích, phải kiểm như mọi giả thuyết khác.

## 3. Mức nền so sánh được

Ghi rõ: tập so sánh (khách nào, chi nhánh nào) · cửa sổ (ví dụ 12 tháng gần nhất) · giai đoạn (trước/sau đổi giá, đổi phần mềm) · độ ổn định · xu hướng, mùa vụ, lịch (Tết, lễ, mùa mưa, mùa tựu trường) · phân khúc · cỡ mẫu · sự kiện đã biết (khuyến mãi, mất điện, đứt hàng).

Không trộn: trước và sau một thay đổi lớn · số thực tế với kế hoạch hoặc dự báo · hai tập có đơn vị dòng khác nhau. Mức nền không so được → ghi giới hạn hoặc để người phụ trách quyết.

**Kiểm tử số và mẫu số riêng.** Tỷ lệ trả hàng tăng có thể do số đơn trả tăng **hoặc** số đơn bán giảm. **Kiểm từng phân khúc.** Biên lãi toàn công ty giảm có thể chỉ do cơ cấu bán dịch sang nhóm hàng lãi thấp, từng nhóm vẫn ổn.

## 4. Chọn cách phát hiện

| Cách | Dùng khi | Lưu ý |
|---|---|---|
| Quy tắc ràng buộc | Kiểm vi phạm rõ: số âm, ngày tương lai, mã không tồn tại | Đơn giản, nên chạy đầu tiên |
| Chênh lệch tuyệt đối / tương đối | So với kỳ trước, cùng kỳ, kế hoạch đã duyệt | Mẫu số gần 0 làm % vọt ảo; ghi cả số tuyệt đối |
| Khoảng tứ phân vị (IQR) / độ lệch trung vị (MAD) | Dữ liệu lệch, có ngoại lai (giá trị đơn, chi phí theo phiếu) | Không giả định phân phối chuẩn |
| Biểu đồ kiểm soát | Quá trình lặp ổn định (thời gian giao, tỷ lệ lỗi sản phẩm) | Cần mức nền ổn định; chọn loại biểu đồ hợp kiểu dữ liệu |
| Phần dư sau khi bỏ mùa vụ | Chỉ số có mùa vụ rõ (doanh thu theo tuần) | Cần đủ chu kỳ lịch sử |
| Điểm gãy | Nghi có thay đổi chế độ (sau đổi giá, đổi nhà cung cấp) | Chỉ là gợi ý thời điểm, không chỉ ra nguyên nhân |

Không áp một ngưỡng cho mọi chỉ số. Ghi cho mỗi tín hiệu: cách phát hiện, tham số, ngưỡng và ai duyệt, giá trị mong đợi/thực tế/chênh lệch, kỳ, phân khúc, độ bất định, số phép so đã làm. "Có ý nghĩa thống kê" không đồng nghĩa "đáng kể về kinh doanh".

## 5. Phân nhóm, giả thuyết và nguyên nhân

**Nhóm:** DỮ LIỆU · QUY TRÌNH NHẬP · ĐỊNH NGHĨA CHỈ SỐ · SỰ KIỆN ĐÃ BIẾT · VẬN HÀNH KINH DOANH · BÊN NGOÀI · RỦI RO AN NINH – GIAN LẬN · CHƯA RÕ.

**Mỗi giả thuyết** ghi: cơ chế (vì sao nó gây ra con số này) · nếu đúng thì sẽ thấy gì · bằng chứng ủng hộ · phép thử có thể bác bỏ và kết quả · giải thích khác, yếu tố gây nhiễu · người kiểm · trạng thái.

**Nguyên nhân CÓ CĂN CỨ** chỉ khi: nhiều bằng chứng độc lập cùng chỉ về một hướng · đúng trình tự thời gian · cơ chế hợp lý · đã xem xét và loại các giải thích khác · người rà chấp nhận. Còn lại: ĐÃ BÁC BỎ hoặc CHƯA RÕ.

## 6. Phương án hành động và rút kinh nghiệm

Mỗi phương án (quan sát thêm · điều tra tiếp · khoanh vùng · tính lại · sửa · thông báo) ghi: tác động và phạm vi ảnh hưởng · điều kiện và thẩm quyền · người phụ trách, hạn · cách quay lại · cách kiểm kết quả · trạng thái CHỜ QUYẾT ĐỊNH.

Sau xử lý: theo dõi tái diễn, báo nhầm, bỏ sót; đề xuất chỉnh cách phát hiện có phiên bản. Không tự bật, tắt hay chỉnh ngưỡng.

## 7. Sáu rủi ro phải ghi

1. Mức nền không so được hoặc trôi.
2. Chất lượng dữ liệu, đường đi của dữ liệu.
3. Phương pháp sai giả định, ngưỡng tùy tiện, so quá nhiều lần.
4. Mùa vụ, phân khúc, mẫu số.
5. Nói quá về nguyên nhân.
6. Cảnh báo quá nhiều gây nhờn, hoặc hành động vượt thẩm quyền.

## 8. Ví dụ đối chiếu

**Tình huống:** chuỗi 6 quán cà phê, chi phí nguyên liệu tháng 10 của quán Quận 7 tăng 38% so với tháng 9.

**Sai:** "Quán Quận 7 có dấu hiệu thất thoát nguyên liệu, đề nghị kiểm điểm quản lý quán."
**Đúng (sàng lọc):** "Kiểm dữ liệu: phiếu nhập sữa ngày 28/9 được nhập vào 2/10 (dời kỳ khoảng 9 triệu). Sau điều chỉnh, chi phí tăng 21%; doanh thu tăng 17%; tỷ lệ chi phí/doanh thu từ 31,2% lên 32,3%, vẫn trong dải 6 tháng (30–34%). Kết luận sơ bộ: chủ yếu LỖI DỮ LIỆU (dời kỳ) + BIẾN ĐỘNG BÌNH THƯỜNG. Đề nghị kế toán chốt lại kỳ ghi nhận phiếu nhập."

## 9. Nguồn nguyên tắc (kiểm tra 22/08/2026, nên xem lại khi dùng)

- NIST/SEMATECH e-Handbook of Statistical Methods — phần Process Monitoring: biểu đồ kiểm soát và chuỗi thời gian; chọn phương pháp theo bối cảnh.
- ISO 7870-2:2023 — hướng dẫn biểu đồ kiểm soát Shewhart; không áp một loại biểu đồ cho mọi dữ liệu.
- W3C PROV-O — nguyên tắc ghi nguồn gốc dữ liệu (ai, làm gì, từ đâu).

Các nguồn này không chứng nhận một tín hiệu là nguyên nhân, sự cố hay gian lận.

*[A.I Generated — Claude Code — 30/10/2026]*
