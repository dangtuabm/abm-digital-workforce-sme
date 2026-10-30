# QUY TẮC MÔ HÌNH KỊCH BẢN

**Mục lục**
- 1. Toàn vẹn mô hình
- 2. Đơn vị và công thức — lỗi hay gặp
- 3. Kịch bản nhất quán
- 4. Độ nhạy, hòa vốn, xếp hạng biến
- 5. Ngưỡng và tín hiệu
- 6. Diễn giải theo ba chế độ — ví dụ đã chạy
- 7. Trạng thái mô hình và thẩm định

---

## 1. Toàn vẹn mô hình

Mỗi biến, công thức, đầu ra có: mã · định nghĩa · đơn vị · nguồn, phiên bản, ngày · dải · người phụ trách · độ tin cậy hoặc chỗ thiếu. Phân biệt: số dư (tồn quỹ, tồn kho, công nợ) với dòng phát sinh (thu, chi, nhập, xuất) · biến kiểm soát được (giá bán, lịch trả nhà cung cấp) với biến bên ngoài (giá nguyên liệu, tỷ giá) · số thực tế với số dự phóng.

- Công thức chỉ dùng số, tên đã khai báo, `+ - * / **`, dấu âm và ngoặc. Công cụ không chạy hàm, không đọc file, không mạng.
- Công thức tính theo thứ tự khai báo; tên chưa có, vòng lặp, chia cho 0 → mô hình KHÔNG HỢP LỆ.
- Mỗi kịch bản phải có đủ mọi biến, giá trị trong dải. Thiếu **không** bằng 0.
- Xác suất chỉ dùng khi có dữ liệu tần suất hoặc mô hình đã kiểm chứng và người thẩm định duyệt; nếu không, kịch bản là các khả năng.

## 2. Đơn vị và công thức — lỗi hay gặp

| Lỗi | Ví dụ | Cách tránh |
|---|---|---|
| Trộn tháng với năm | Cộng doanh thu tháng với chi phí thuê năm | Đưa tất cả về cùng kỳ tính |
| Trộn số dư với dòng phát sinh | Cộng tồn kho vào doanh thu | Số dư chỉ cộng/trừ dòng phát sinh |
| Có/không VAT | Doanh thu gồm VAT, giá vốn chưa VAT | Ghi rõ trong định nghĩa biến |
| Trộn tiền tệ | Giá nhập USD, giá bán VNĐ không quy đổi | Thêm biến tỷ giá có nguồn |
| Lãi khác tiền | Lấy lợi nhuận làm dòng tiền | Dòng tiền tính theo thời điểm thu, chi thật (công nợ, lịch trả) |
| Cộng trùng | Tính phí giao hàng trong cả chi phí biến đổi và chi phí cố định | Mỗi khoản chỉ ở một chỗ |

## 3. Kịch bản nhất quán

Mỗi kịch bản có **câu chuyện nguyên nhân**: vì sao các biến cùng đi theo hướng đó. Ví dụ XẤU cho công ty phân phối: "thị trường xây dựng chững lại → doanh thu giảm, khách trả chậm hơn, nhà cung cấp không giảm giá". Không tạo kịch bản TỐT bằng "giá cao, sản lượng cao, chi phí thấp, năng lực vô hạn" khi các biến kéo ngược nhau (giá cao thường làm sản lượng giảm). Ghi các tổ hợp bị loại và lý do.

| Kịch bản | Dùng để |
|---|---|
| XẤU | Chuẩn bị phương án dự phòng |
| CƠ SỞ | Kế hoạch làm việc |
| TỐT | Biết trần, chuẩn bị năng lực |
| CỰC XẤU (tùy chọn) | Thử sức chịu đựng: doanh nghiệp có sống qua không |

## 4. Độ nhạy, hòa vốn, xếp hạng biến

- **Độ nhạy một chiều:** thay một biến trong kịch bản CƠ SỞ, giữ biến khác. Ghi giới hạn: có thể phá quan hệ giữa các biến.
- **Xếp hạng biến:** mỗi biến đặt lần lượt ở mức thấp và cao của dải, đo độ rộng kết quả; biến có độ rộng lớn nhất là biến cần canh và cần thêm bằng chứng nhất.
- **Hòa vốn / ngưỡng:** chỉ tìm trong khoảng đã duyệt. Không nằm trong khoảng → ghi KHÔNG NẰM TRONG KHOẢNG, không suy rộng. Kết quả không đơn điệu → có thể có nhiều điểm, xem bảng độ nhạy.
- **Vững / mong manh:** kết luận VỮNG khi đứng qua mọi kịch bản hợp lý và dải đã duyệt; MONG MANH khi một biến lệch nhỏ (ví dụ dưới 10% dải) hoặc một chỗ thiếu trọng yếu là đổi kết luận.

Luôn tách: thiệt hại nếu sai · thiệt hại nếu chậm · đảo ngược được hay không.

## 5. Ngưỡng và tín hiệu

Mỗi ngưỡng có: chỉ số · phép so · giá trị, đơn vị · chiều · nguồn và tần suất cập nhật · người phụ trách · thẩm quyền hành động · vùng đặt lại để tránh bật tắt. Tín hiệu là thứ **quan sát được** (tỷ lệ thu tiền tuần này, số suất bán 2 tuần đầu), không phải tên kịch bản. Ngưỡng chỉ là đề xuất cho đến khi người có quyền chốt; theo dõi định kỳ chuyển sang việc cảnh báo sớm.

## 6. Diễn giải theo ba chế độ — ví dụ đã chạy (số minh họa, 30/10/2026)

### Kịch bản kế hoạch — `templates/dau-vao-mau-ke-hoach.json`
Chuỗi cơm văn phòng mở thêm 1 quán; đơn vị nghìn đồng/tháng.

| Kịch bản | Doanh thu | Lãi gộp | Lợi nhuận |
|---|---:|---:|---:|
| XẤU | 159.600 | 64.600 | −27.400 |
| CƠ SỞ | 225.000 | 110.000 | 25.000 |
| TỐT | 291.400 | 155.000 | 70.000 |

Hòa vốn ở kịch bản CƠ SỞ: khoảng **3.864 suất/tháng** (khoảng 150 suất/ngày nếu bán 26 ngày). Biến kéo lợi nhuận mạnh nhất: số suất/tháng, rồi giá bán. Tín hiệu cần canh: số suất bán 2 tuần đầu.

### Kịch bản dòng tiền — `templates/dau-vao-mau-dong-tien.json`
Công ty phân phối thiết bị điện; triệu đồng; mức tồn quỹ tối thiểu 300.

| Kịch bản | Tồn quỹ tháng 1 | Tồn quỹ tháng 2 | Tồn quỹ tháng 3 | Chạm ngưỡng |
|---|---:|---:|---:|---|
| XẤU | 646 | **192** | 338 | Tháng 2 dưới 300 |
| CƠ SỞ | 1.010 | 720 | 1.030 | Không |
| TỐT | 1.212 | 1.029 | 1.446 | Không |

Ngưỡng: ở kịch bản CƠ SỞ, nếu tỷ lệ thu tiền trong tháng xuống khoảng **46%** thì tồn quỹ tháng 2 chạm 300 triệu (tháng 2 có trả gốc vay 600 triệu). Xếp hạng biến cho tồn quỹ tháng 2: tỷ lệ thu trong tháng (độ rộng 750 triệu) > tỷ lệ giá vốn (360) > phải thu đầu kỳ (300) > tồn quỹ đầu (200) > doanh thu (160). Nhận định: **đẩy thu tiền quan trọng hơn tăng doanh số** cho bài toán thiếu tiền tháng 2; tăng doanh thu trong dải không làm tồn quỹ tháng 2 chạm 300 (công cụ trả KHÔNG NẰM TRONG KHOẢNG). Phương án dự phòng để người có quyền chọn: đẩy thu nợ quá hạn, đàm phán giãn trả nhà cung cấp, chuẩn bị hạn mức vay ngắn hạn.

### Thử sức chịu đựng — dùng lại mẫu kế hoạch
Kết luận cần thử: "quán mới có lãi". Điều kiện phải đúng: bán ≥ 3.864 suất/tháng **và** giá bán bình quân giữ trên 40 nghìn (ở 40 nghìn, các biến khác giữ CƠ SỞ, lợi nhuận về 0). Giá chỉ cần giảm 5 nghìn (một nửa dải 40–50) là hết lãi → kết luận **MONG MANH** với giá bán. Bằng chứng cần thu: khảo sát giá chấp nhận của khách văn phòng khu vực, số suất của quán đối thủ giờ cao điểm.

## 7. Trạng thái mô hình và thẩm định

- **HỢP LỆ:** đủ biến, công thức, đơn vị, nguồn; đã rà công thức; người thẩm định duyệt.
- **TẠM:** chạy được nhưng còn dải chưa có nguồn hoặc chưa thẩm định; ghi điều kiện để nâng lên HỢP LỆ.
- **KHÔNG HỢP LỆ:** thiếu công thức, đơn vị, nguồn trọng yếu; vòng lặp; lỗi đơn vị; không chạy hoặc kết quả không được dùng.

Thẩm định gồm: rà đơn vị · đối chiếu với kỳ thực tế đã biết (nếu có) · người thứ hai rà công thức · kiểm dải và độ mới của nguồn · đối chiếu tổng với sổ sách.

*[A.I Generated — Claude Code — 30/10/2026]*
