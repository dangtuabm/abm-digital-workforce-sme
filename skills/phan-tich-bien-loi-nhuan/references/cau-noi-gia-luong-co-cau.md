# CẦU NỐI LỢI NHUẬN: GIÁ – LƯỢNG – CƠ CẤU – CHI PHÍ

**Mục lục:** 1. Điều kiện trước khi lập cầu nối · 2. Ký hiệu · 3. Công thức từng cột · 4. Sản phẩm mới, ngừng bán · 5. Ví dụ cân số · 6. Cách diễn giải

## 1. Điều kiện trước khi lập cầu nối
- Hai kỳ cùng định nghĩa doanh thu, giá vốn, đơn vị tính, danh mục sản phẩm (hoặc đã quy đổi).
- Có số lượng, giá bán bình quân, giá vốn đơn vị cho từng sản phẩm (hoặc nhóm hàng) ở cả hai kỳ.
- Thiếu giá – lượng theo sản phẩm: chỉ lập được cầu nối ở mức tổng (doanh thu, giá vốn, chi phí); phần giá – lượng – cơ cấu ghi "chưa tách được, cần dữ liệu theo sản phẩm".

## 2. Ký hiệu
Với mỗi sản phẩm i, kỳ so sánh ký hiệu 0, kỳ này ký hiệu 1:
- Q = số lượng bán; P = giá bán bình quân sau chiết khấu; C = giá vốn đơn vị (cộng chi phí trực tiếp đơn vị nếu phân tích ở tầng lãi đóng góp).
- m = P − C = lãi đơn vị.
- Q tổng = tổng số lượng; tỷ trọng cơ cấu s_i = Q_i / Q tổng.
- Lãi bình quân kỳ 0 = tổng (m0_i × Q0_i) / Q tổng kỳ 0.

Lượng tổng chỉ có nghĩa khi các sản phẩm cùng đơn vị tính hoặc đã quy đổi. Khác đơn vị (cái, kg, bộ): chạy cầu nối theo doanh thu thay cho số lượng, ghi rõ.

## 3. Công thức từng cột

| Cột | Công thức | Ý nghĩa |
|---|---|---|
| **Lượng** | (Q tổng kỳ 1 − Q tổng kỳ 0) × lãi bình quân kỳ 0 | Bán nhiều hơn hay ít hơn, giữ nguyên cơ cấu cũ |
| **Cơ cấu** | Tổng theo i: Q tổng kỳ 1 × (s1_i − s0_i) × m0_i | Bán nghiêng sang hàng lãi thấp hay lãi cao |
| **Giá bán** | Tổng theo i: (P1_i − P0_i) × Q1_i | Giá bình quân (sau chiết khấu) tăng hay giảm |
| **Giá vốn đơn vị** | − Tổng theo i: (C1_i − C0_i) × Q1_i | Giá vốn tăng làm lãi giảm (dấu trừ) |
| **Chi phí trực tiếp ngoài đơn vị** | − (tổng kỳ 1 − tổng kỳ 0) của các khoản không tính theo đơn vị | Vận chuyển, phí sàn, hoa hồng tính gộp |
| **Chi phí chung** | − (chi phí chung kỳ 1 − kỳ 0) | Chỉ khi cầu nối tới lợi nhuận sau chi phí chung |
| **Sản phẩm mới / ngừng** | + lãi của sản phẩm chỉ có ở kỳ 1 − lãi của sản phẩm chỉ có ở kỳ 0 | Tách riêng, không nhét vào giá hay lượng |

**Kiểm cân bắt buộc:** Lợi nhuận kỳ 0 + Lượng + Cơ cấu + Giá bán + Giá vốn + Chi phí + Sản phẩm mới/ngừng = Lợi nhuận kỳ 1. Không cân → có lỗi dữ liệu hoặc công thức; dừng, không làm tròn để ép cân.

Lưu ý: Lượng + Cơ cấu luôn bằng tổng theo i của (Q1_i − Q0_i) × m0_i; Giá bán + Giá vốn luôn bằng tổng theo i của (m1_i − m0_i) × Q1_i. Dùng hai đẳng thức này để tự kiểm.

Cầu nối so với kế hoạch: thay kỳ 0 bằng số kế hoạch (giá, lượng, giá vốn kế hoạch), công thức giữ nguyên.

## 4. Sản phẩm mới, ngừng bán
- Sản phẩm chỉ có ở một kỳ không có giá so sánh: đưa toàn bộ lãi của nó vào cột "Sản phẩm mới / ngừng".
- Sản phẩm đổi mã nhưng thực chất cùng hàng: quy về một mã theo bảng quy đổi doanh nghiệp xác nhận, không tự quy.

## 5. Ví dụ cân số (số liệu minh họa)

Cửa hàng vật liệu xây dựng, hai mặt hàng, giá và giá vốn tính bằng nghìn đồng/thùng, lãi tính bằng nghìn đồng:

| Mặt hàng | Q0 | P0 | C0 | m0 | Q1 | P1 | C1 | m1 |
|---|---|---|---|---|---|---|---|---|
| Keo dán gạch A | 1.000 | 100 | 70 | 30 | 900 | 100 | 72 | 28 |
| Keo chà ron B | 1.000 | 50 | 45 | 5 | 1.500 | 48 | 45 | 3 |

- Doanh thu: kỳ 0 = 150.000; kỳ 1 = 162.000 (tăng 8%).
- Lãi gộp: kỳ 0 = 35.000; kỳ 1 = 29.700 (giảm 5.300).

Cầu nối:
| Cột | Tính | Kết quả |
|---|---|---|
| Lượng | (2.400 − 2.000) × 17,5 | +7.000 |
| Cơ cấu | 2.400 × (0,375 − 0,5) × 30 + 2.400 × (0,625 − 0,5) × 5 | −7.500 |
| Giá bán | 0 × 900 + (48 − 50) × 1.500 | −3.000 |
| Giá vốn | − (72 − 70) × 900 − 0 × 1.500 | −1.800 |
| **Tổng** | 35.000 + 7.000 − 7.500 − 3.000 − 1.800 | **29.700 — cân** |

Tự kiểm: Lượng + Cơ cấu = −100 × 30 + 500 × 5 = −500, khớp. Giá + Giá vốn = (28 − 30) × 900 + (3 − 5) × 1.500 = −4.800, khớp.

## 6. Cách diễn giải
Viết theo thứ tự cột có giá trị tuyệt đối lớn nhất trước. Ví dụ trên:

"[DỮ KIỆN] Doanh thu tăng 8% nhưng lãi gộp giảm 5,3 triệu. Bán nhiều hơn lẽ ra thêm 7 triệu lãi, nhưng phần tăng chủ yếu là keo chà ron B — hàng lãi thấp — nên cơ cấu kéo lại 7,5 triệu. Giá bán B giảm 2 nghìn/thùng làm mất 3 triệu; giá vốn A tăng 2 nghìn/thùng làm mất 1,8 triệu. [SUY LUẬN] Doanh thu tăng nhờ đẩy hàng lãi thấp kèm giảm giá. Câu hỏi cần Anh/Chị quyết: có giữ mức giá B hiện tại không, và giá vốn A tăng có chuyển được vào giá bán không?"

Không viết "nhân viên bán hàng đẩy sai hàng" khi chưa có bằng chứng; chỉ mô tả con số và nêu câu hỏi.

*[A.I Generated — Claude Code — 30/10/2026]*
