# QUY TẮC THEO DÕI TÍN HIỆU

**Mục lục**
- 1. Ba đơn vị cơ bản
- 2. Kiểm trước khi phát hiện
- 3. Năm loại tín hiệu
- 4. Xác nhận, vùng đặt lại và chuyển trạng thái
- 5. Bốn chiều chấm điểm và bốn mức độ
- 6. Phiếu cảnh báo đạt chuẩn
- 7. Ví dụ đối chiếu

---

## 1. Ba đơn vị cơ bản

| Đơn vị | Nghĩa | Ví dụ |
|---|---|---|
| **Số liệu quan sát** | Giá trị hoặc sự kiện thô, lấy từ một nguồn, tại một thời điểm | Tuần 42 có 37 khiếu nại giao hàng chậm (phần mềm CSKH, chốt 17h thứ Sáu) |
| **Tín hiệu** | Số liệu quan sát (hoặc một chuỗi) đã qua quy tắc trong Hợp đồng theo dõi | Khiếu nại giao chậm vượt dải dự kiến 2 tuần liên tiếp |
| **Cảnh báo** | Tín hiệu đạt mức cần người phụ trách xem trong hạn đã định | Mức 3, giao Trưởng phòng Vận hành, xem trong 24 giờ |

Mỗi số liệu quan sát gán mã `QS-...`, mỗi tín hiệu `TH-...`, mỗi nguồn `NG-...`.

## 2. Kiểm trước khi phát hiện

1. Định nghĩa chỉ số, đơn vị, mẫu số, phân khúc, múi giờ khớp với Hợp đồng theo dõi (doanh thu có/không VAT, đơn hàng có/không đơn hủy).
2. Nguồn đủ phạm vi, không quá cũ, không đổi cách tính giữa chừng (ví dụ phần mềm bán hàng vừa đổi cách ghi nhận đơn trả).
3. Mức nền đủ đại diện: ghi rõ cửa sổ (ví dụ 12 tuần gần nhất), mùa vụ (Tết, mùa mưa, mùa tựu trường), chương trình khuyến mãi, ngày lễ.
4. Đã gộp số liệu trùng và gộp các nguồn đăng lại cùng một gốc thành một **nhóm bằng chứng**.

Nguồn thiếu hoặc hỏng **không phải** KHÔNG CÓ TÍN HIỆU — ghi THIẾU DỮ LIỆU và xử lý theo quy tắc riêng.

## 3. Năm loại tín hiệu

| Loại | Nhận biết | Ví dụ SME |
|---|---|---|
| **SỰ KIỆN** | Việc rời rạc, có thời điểm rõ | Nhà cung cấp chính báo tăng giá 8% từ ngày 1/12 |
| **XU HƯỚNG** | Thay đổi cùng chiều, kéo dài qua số kỳ đã chốt | Vòng quay tồn kho giảm 4 tháng liền |
| **BẤT THƯỜNG** | Lệch khỏi dải dự kiến, chưa rõ vì sao | Đơn trả hàng chi nhánh Cần Thơ gấp 3 lần mức nền tuần này |
| **TIN ĐỒN** | Thông tin chưa đủ thẩm quyền hoặc chưa có nguồn độc lập | Nhóm Zalo đại lý nói đối thủ sắp giảm giá 15% |
| **NHIỄU** | Dao động trong dải dự kiến, hoặc lỗi nhập liệu | Doanh thu ngày giảm 6% nhưng vẫn trong dải 12 tuần |

BẤT THƯỜNG chưa rõ nguyên nhân → chuyển tiếp việc phân tích bất thường, không tự đoán nguyên nhân trong phiếu cảnh báo.

## 4. Xác nhận, vùng đặt lại và chuyển trạng thái

**Xác nhận** có thể là: số kỳ liên tiếp, nguồn độc lập thứ hai, nguồn chính thức (văn bản cơ quan nhà nước, thông báo của nhà cung cấp), hoặc bằng chứng trực tiếp. Cách xác nhận phải ghi sẵn trong Hợp đồng theo dõi. Bốn mức: CHƯA XÁC NHẬN · XÁC NHẬN MỘT PHẦN · ĐÃ XÁC NHẬN · ĐÃ BÁC BỎ.

Kiểm 5 điểm: nguồn có độc lập không · nguồn có thẩm quyền không · còn mới không · nói trực tiếp hay suy ra · có bằng chứng phản bác không. 30 bài báo cùng dẫn một tài khoản ẩn danh = **một** nhóm bằng chứng.

**Vùng đặt lại:** ngưỡng mở và ngưỡng đóng phải khác nhau. Ví dụ: mở cảnh báo khi tỷ lệ giao trễ > 8%, chỉ đóng khi < 6% trong 2 tuần liên tiếp. Không có vùng đặt lại thì chỉ số dao động 7,9% – 8,1% sẽ làm cảnh báo bật tắt liên tục.

**Chuyển trạng thái:** KHÔNG CÓ TÍN HIỆU → QUAN SÁT → THEO DÕI → CẢNH BÁO → ĐÃ ĐÓNG. Được quay về QUAN SÁT khi bị bác bỏ hoặc về dưới ngưỡng đặt lại. Mọi lần chuyển ghi thời điểm, lý do, bằng chứng, người duyệt. THIẾU DỮ LIỆU là trạng thái riêng.

Một quy tắc an toàn (cháy nổ, ngộ độc thực phẩm, mất tiền lớn) được bỏ qua bước xác nhận chỉ khi Hợp đồng theo dõi ghi rõ, kèm người phụ trách và hạn.

## 5. Bốn chiều chấm điểm và bốn mức độ

| Chiều | Câu hỏi |
|---|---|
| Tác động | Nếu tín hiệu đúng, ảnh hưởng tới mục tiêu, khách hàng, tiền, pháp lý tới đâu? |
| Độ gấp | Còn bao lâu để kịp hành động? |
| Độ tin cậy | Bằng chứng xác nhận mạnh đến đâu? |
| Khả năng đảo ngược | Nếu phản ứng sai thì quay lại được không, tốn bao nhiêu? |

| Mức | Ý nghĩa | Xử lý gợi ý (doanh nghiệp tự điền người và hạn) |
|---|---|---|
| **Mức 1 — THÔNG TIN** | Không đổi quyết định | Lưu, xem ở chu kỳ thường |
| **Mức 2 — THEO DÕI** | Có thể đổi một giả định | Người phụ trách kiểm trong hạn chuẩn (ví dụ 3 ngày làm việc) |
| **Mức 3 — ĐÁNG KỂ** | Có thể đổi kế hoạch hoặc quyết định | Người duyệt xem sớm (ví dụ trong 24 giờ) |
| **Mức 4 — NGHIÊM TRỌNG** | An toàn, pháp lý, tài chính, danh tiếng trọng yếu, cửa sổ ngắn | Áp kịch bản ứng phó đã duyệt; A.I chỉ soạn, không tự hành động |

Không nâng mức vì tin lan truyền mạnh. Không hạ mức chỉ vì độ tin cậy thấp nếu thiệt hại tiềm ẩn lớn — khi đó giữ mức và ghi rõ "chưa xác nhận".

## 6. Phiếu cảnh báo đạt chuẩn

Có đủ: mã tín hiệu · điều gì đã đổi · mức nền hoặc dải dự kiến · bằng chứng và bằng chứng phản bác · mức xác nhận · tác động · độ gấp · lý do độ tin cậy · đối tượng bị ảnh hưởng · người phụ trách · hạn · việc kiểm tiếp theo · các phương án phản ứng (chưa thực hiện) · tình trạng duyệt · đường dẫn nguồn.

Phiếu không trình bày suy luận như sự thật: tách rõ **[DỮ KIỆN]** và **[NHẬN ĐỊNH]**.

## 7. Ví dụ đối chiếu

**Sai:** "Khiếu nại tăng 20% so với tuần trước, phát CẢNH BÁO." — trong khi đang mùa cao điểm cuối năm và vẫn nằm trong dải dự kiến của cùng kỳ.
**Đúng:** "So với cùng kỳ mùa cao điểm năm trước, khiếu nại vẫn trong dải dự kiến → NHIỄU / KHÔNG CÓ TÍN HIỆU. Ghi chú để xem lại tuần sau."

**Sai:** "Hai nguồn lỗi không lấy được số, ghi KHÔNG CÓ TÍN HIỆU."
**Đúng:** "NG-03, NG-05 lỗi kết nối từ thứ Ba → THIẾU DỮ LIỆU; báo người phụ trách dữ liệu."

*[A.I Generated — Claude Code — 30/10/2026]*
