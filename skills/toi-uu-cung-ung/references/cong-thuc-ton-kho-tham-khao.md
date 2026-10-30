# CÔNG THỨC TỒN KHO THAM KHẢO

**Mục lục**
- 1. Chỉ số sức khỏe kho
- 2. Dự báo và sai số
- 3. Phân nhóm ABC và XYZ
- 4. Mức tồn an toàn và điểm đặt hàng lại
- 5. Lượng đặt hàng và danh sách cảnh báo
- 6. Tổng chi phí khi so nhà cung cấp
- 7. Khi nào không dùng các công thức này

> Đây là công thức phổ biến trong quản trị tồn kho, dùng để **gợi ý**. Mức phục vụ, ngưỡng, nhóm do người có quyền chốt theo ngành hàng và chính sách công ty. Số trong ví dụ là minh họa.

---

## 1. Chỉ số sức khỏe kho

| Chỉ số | Công thức | Đọc thế nào |
|---|---|---|
| Vòng quay tồn kho | Giá vốn hàng bán trong kỳ / Tồn kho bình quân (theo giá vốn) | Càng cao hàng càng quay nhanh; so với chính mình các kỳ trước và với nhóm hàng tương tự |
| Số ngày tồn kho | Số ngày trong kỳ / Vòng quay | Hàng nằm kho bao nhiêu ngày mới bán hết |
| Tỷ lệ đáp ứng đơn (fill rate) | Số lượng giao đủ ngay / Số lượng khách đặt | Đo mức phục vụ thật |
| Tỷ lệ hết hàng | Số ngày-mã hết hàng / Tổng số ngày-mã | Mã nhóm A cần gần 0 |
| Tỷ lệ hàng chậm luân chuyển | Giá trị tồn không bán trong N ngày / Tổng giá trị tồn | N do công ty chốt (ví dụ 90 ngày) |

## 2. Dự báo và sai số

- Cách đơn giản để so: trung bình 3 kỳ gần nhất; cùng kỳ năm trước nhân hệ số tăng trưởng.
- Có mùa vụ (Tết, mùa cưới, mùa khai giảng): dùng cùng kỳ năm trước, điều chỉnh khuyến mãi và ngày hết hàng.
- Kiểm lại: dùng các kỳ cũ để "dự báo thử" kỳ đã biết, so với thực tế.
- Sai số phần trăm tuyệt đối trung bình (MAPE) = trung bình của |thực tế − dự báo| / thực tế. Dễ hiểu nhưng sai lệch khi thực tế gần 0; khi đó dùng tổng |sai| / tổng thực tế.
- Luôn ghi 3 kịch bản: cơ sở – tăng – giảm, kèm giả định của từng kịch bản.

## 3. Phân nhóm ABC và XYZ

**ABC theo giá trị tiêu thụ** (số lượng × giá vốn trong kỳ), xếp giảm dần, cộng dồn:
- Nhóm A: các mã chiếm khoảng 70–80% giá trị (thường ít mã) — kiểm soát chặt, đếm thường xuyên, để vị trí lấy nhanh.
- Nhóm B: khoảng 15–25% tiếp theo.
- Nhóm C: phần còn lại (nhiều mã, giá trị thấp) — kiểm soát đơn giản.
Ngưỡng % do công ty chốt.

**XYZ theo độ ổn định nhu cầu** (hệ số biến thiên = độ lệch chuẩn / trung bình nhu cầu theo kỳ):
- X: ổn định · Y: dao động vừa · Z: thất thường. Ngưỡng do công ty chốt.
Ghép AX, AZ, CZ… để chọn cách quản: AX đặt hàng đều theo dự báo; AZ cần tồn đệm và theo dõi sát; CZ cân nhắc đặt theo đơn.

## 4. Mức tồn an toàn và điểm đặt hàng lại

Khi thời gian giao tương đối ổn định:
- **Mức tồn an toàn** ≈ z × độ lệch chuẩn nhu cầu mỗi ngày × √(thời gian giao tính theo ngày)
- **Điểm đặt hàng lại** = nhu cầu trung bình mỗi ngày × thời gian giao + mức tồn an toàn

Khi thời gian giao cũng dao động:
- Mức tồn an toàn ≈ z × √(thời gian giao trung bình × độ lệch chuẩn nhu cầu² + nhu cầu trung bình² × độ lệch chuẩn thời gian giao²)

Hệ số z theo mức phục vụ (xác suất không hết hàng trong một chu kỳ): 90% → 1,28 · 95% → 1,65 · 98% → 2,05 · 99% → 2,33.

Ví dụ minh họa: nhu cầu trung bình 40 thùng/ngày, độ lệch chuẩn 10, thời gian giao 9 ngày, mức phục vụ 95% → tồn an toàn ≈ 1,65 × 10 × 3 ≈ 50 thùng; điểm đặt hàng lại ≈ 40 × 9 + 50 = 410 thùng.

Luôn chạy độ nhạy: đổi mức phục vụ 90% / 95% / 98% thì tồn và vốn đọng thay đổi bao nhiêu — để người quyết thấy đánh đổi.

## 5. Lượng đặt hàng và danh sách cảnh báo

- **Lượng đặt kinh tế (EOQ)** ≈ √(2 × nhu cầu năm × chi phí mỗi lần đặt / chi phí lưu kho mỗi đơn vị mỗi năm). Sau đó làm tròn theo số lượng đặt tối thiểu, quy cách thùng/pallet, sức chứa.
- **Cần nhập gấp:** tồn bán được + hàng đang về ≤ điểm đặt hàng lại, ưu tiên nhóm A.
- **Chậm bán:** không bán trong N ngày hoặc số ngày tồn vượt ngưỡng công ty chốt.
- **Cận hạn:** thời hạn còn lại < ngưỡng (theo ngành; ví dụ hàng thực phẩm thường xét theo % hạn dùng còn lại) — đề xuất cách xử lý (đẩy bán, khuyến mãi, chuyển kênh, trả nhà cung cấp nếu hợp đồng cho phép); người có quyền quyết.

## 6. Tổng chi phí khi so nhà cung cấp

Tổng chi phí cho một kỳ ≈ giá mua × số lượng + vận chuyển + thuế phí (theo căn cứ) + chi phí lưu kho (gồm phần tồn an toàn tăng thêm nếu thời gian giao dao động nhiều) + chi phí vốn đọng + chi phí lỗi, đổi trả + chi phí dừng bán/dừng máy khi giao trễ + chi phí chuyển đổi nhà cung cấp.

Ví dụ: bên B rẻ hơn bên A 5% nhưng thời gian giao dao động gấp đôi → tồn an toàn phải tăng, vốn đọng tăng; tính đủ mới biết B có thật sự rẻ hơn.

## 7. Khi nào không dùng các công thức này

- Dữ liệu quá ngắn, nhiều ngày hết hàng chưa ghi, hoặc hàng mới chưa có lịch sử.
- Hàng thời trang, hàng theo mùa ngắn, hàng đặt theo dự án — nhu cầu không theo phân phối ổn định.
- Hàng có hạn dùng ngắn hơn chu kỳ đặt hàng — ràng buộc hạn dùng quyết định, không phải công thức.
- Nhà cung cấp chỉ giao theo đợt cố định, số lượng tối thiểu rất lớn.
Khi đó ghi rõ lý do, dùng kịch bản và phán đoán của người phụ trách, gắn [GIẢ ĐỊNH].

*[A.I Generated — Claude Code — 30/10/2026]*
