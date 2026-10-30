# SOI NGÁCH BẰNG CHỨNG CỨ

## Mục lục
- I. Chốt ràng buộc
- II. Quy trình thu chứng cứ
- III. Chứng cứ cần ghi cho mỗi sản phẩm
- IV. Thang điểm 100
- V. Bộ lọc loại
- VI. Quy tắc chống bịa số
- VII. Kiểm trước khi báo cáo
- VIII. Mẫu báo cáo

Đọc ở Bước 7. Dùng cho Shopee, TikTok Shop, Lazada và sàn tương tự.

## I. CHỐT RÀNG BUỘC
- Sàn và thị trường (mặc định sàn Việt Nam doanh nghiệp đang bán).
- Mô hình: **tự sản xuất / nhập hàng bán lại / bán tiếp thị liên kết** — hỏi nếu chưa rõ, vì cách chấm kinh tế khác nhau.
- Ngân sách thử, biên lợi nhuận hoặc hoa hồng tối thiểu, khoảng giá, đối tượng khách.

## II. QUY TRÌNH THU CHỨNG CỨ
1. Bung ngách rộng thành 8–12 từ khóa sản phẩm cụ thể (ví dụ "gia dụng" → hộp cơm, máy hút bụi cầm tay, nồi chiên, kệ bếp...).
2. Mỗi từ khóa: tìm trên sàn, ưu tiên sắp xếp theo bán chạy, mở **trang sản phẩm cụ thể**. Trang tìm kiếm chỉ để khám phá.
3. Ghi chứng cứ từng sản phẩm vào `templates/bang-ung-vien-san-pham.csv`, kèm ảnh chụp hoặc đoạn trích làm nguồn.
4. Đối chiếu xu hướng bằng nguồn khác: video ngắn có tương tác tự nhiên gần đây, gợi ý tìm kiếm, mùa vụ.
5. Xếp hạng trong từng từ khóa: đã bán → số đánh giá → điểm đánh giá → khả năng làm nội dung / kinh tế. Chọn sản phẩm tốt nhất mỗi từ khóa rồi xếp chéo.
6. Chấm điểm bằng `scripts/cham-diem-ung-vien.py`; mạnh dạn LOẠI sản phẩm yếu dù trông đang "hot".

Thứ bậc chứng cứ (mạnh → yếu): trang sản phẩm có số đã bán, đánh giá nhìn thấy được → nhiều shop cùng bán chạy một loại → video ngắn gần đây có tương tác tự nhiên → gợi ý tìm kiếm tăng → đối thủ chi quảng cáo. Yếu: một video lan truyền nhưng không có chứng cứ mua; số bán cao nhưng nhiều đánh giá xấu; ảnh chụp màn hình không có đường dẫn.

## III. CHỨNG CỨ CẦN GHI CHO MỖI SẢN PHẨM
Đường dẫn trang sản phẩm, tên shop · giá, khoảng giá · số đã bán (tổng, theo tháng nếu có) · điểm đánh giá, số đánh giá · số shop bán tương tự · mã giảm giá, miễn phí giao, flash sale đang chạy · có ảnh, video không · đánh giá xấu (hàng lỗi, giao chậm, hàng giả, sai size) · ngày ghi nhận.

## IV. THANG ĐIỂM 100
| Phần | Điểm | Mức cao khi |
|---|---|---|
| Nhu cầu | 0–30 | Bán theo tháng ≥ 3.000 hoặc tổng ≥ 50.000 với đánh giá mới (30); 1.000–2.999/tháng hoặc 10.000–49.999 tổng (25); 200–999/tháng hoặc 2.000–9.999 tổng (19); có bán nhưng chậm (7–12); không có chứng cứ bán (0) |
| Xu hướng | 0–20 | Nhu cầu tăng rõ trên nhiều nguồn và đúng mùa (17–20); có tín hiệu nhưng chưa bùng (13–16); nhu cầu ổn định (8–12); đang giảm (0–7) |
| Kinh tế | 0–20 | Giá dễ quyết mua, biên hoặc hoa hồng tốt, phí giao thấp. Ngưỡng giá mặc định của script: ≤ 300.000đ và ≤ 700.000đ — doanh nghiệp chỉnh bằng tham số |
| Dễ làm nội dung | 0–15 | Trình diễn trước/sau, vấn đề/giải pháp trong dưới 30 giây (13–15); khó quay, lợi ích vô hình (0–5) |
| Cạnh tranh | 0–10 | Cao = dễ cạnh tranh: nhu cầu đã rõ, chưa quá nhiều shop, có góc khác biệt (8–10); bão hòa, đua giá (0–4) |
| Trừ rủi ro | 0–5 | Phàn nàn chất lượng nhẹ (−1); hoàn hàng, sai size cao (−2); dễ vỡ, an toàn điện (−3); công dụng sức khỏe, nghi hàng giả (−4); vi phạm chính sách, pháp lý (−5). Điểm đánh giá dưới 4,6 tự trừ tối thiểu 3 |

Nhóm kết luận: **80–100 THỬ NGAY** (làm 3–5 nội dung thử) · **65–79 THEO DÕI / THỬ NHỎ** · **50–64 CHỈ THỬ NẾU CÓ GÓC NỘI DUNG MẠNH** · **dưới 50 LOẠI**.

## V. BỘ LỌC LOẠI
Loại hoặc trừ nặng: điểm đánh giá dưới 4,6 khi không có lý do rõ; nhiều đánh giá 1 sao về chất lượng, lừa đảo, an toàn; hàng giả, hàng vi phạm sở hữu trí tuệ; công dụng y tế; đồ điện không an toàn; hàng cần chứng minh không làm được; hàng giá cao khó mua bộc phát khi không được yêu cầu; sản phẩm chỉ có điểm mạnh là "rẻ".

## VI. QUY TẮC CHỐNG BỊA SỐ
- Không bịa số đã bán, điểm đánh giá, số đánh giá, hoa hồng, biên lợi nhuận.
- Không chuyển số của sản phẩm này sang sản phẩm khác.
- Số lấy từ trang tìm kiếm ghi "mức trang tìm kiếm"; số lấy từ đoạn trích ghi "ước lượng từ đoạn trích" kèm nguồn.
- Sàn chặn xem dữ liệu: ghi "bị chặn", dùng nguồn khác, giảm độ tin cậy.
- Trang sản phẩm hiện số khác báo cáo: báo cáo sai, sửa ngay, hạ độ tin cậy.
- Không dùng dòng ví dụ hay số mẫu trong báo cáo thật.

## VII. KIỂM TRƯỚC KHI BÁO CÁO
1. Mỗi sản phẩm là trang sản phẩm cụ thể, không phải trang tìm kiếm, trang danh mục.
2. Mỗi con số có nguồn nhìn thấy được.
3. Chỉ có trang tìm kiếm → báo "chưa đủ chứng cứ sản phẩm cụ thể", không đưa khuyến nghị cuối.
4. Không nói "hot nhất"; nói "đáng thử nhất theo dữ liệu hiện có".

## VIII. MẪU BÁO CÁO
```
## Sản phẩm đáng thử
1. <Tên sản phẩm> — <điểm>/100 (ước lượng) — <nhóm>
- Chứng cứ: <đã bán / theo tháng / đánh giá / điểm> — nguồn: <đường dẫn, ngày>
- Xu hướng: <chứng cứ>
- Vì sao có thể bán được: <...>
- Góc nội dung: <3 câu mở đầu, 1 góc trình diễn, 1 góc nỗi đau, 1 góc so sánh>
- Rủi ro cần tránh: <...>
- Việc tiếp theo: <thử 3–5 nội dung ngắn trước khi nhập hàng nhiều>
## Theo dõi
## Loại (kèm lý do)
```
