# QUY TẮC KHỚP VÀ PHÂN LOẠI CHÊNH LỆCH

**Mục lục:** 1. Chuẩn hóa hai nguồn · 2. Bốn tầng khớp · 3. Tám nhóm chênh lệch · 4. Dấu hiệu bất thường cần báo · 5. Mặc định khi doanh nghiệp chưa có quy tắc · 6. Ví dụ

## 1. Chuẩn hóa hai nguồn (Bước 3)

| Trường | Cách chuẩn hóa | Lỗi hay gặp |
|---|---|---|
| Ngày | Đưa về ngày/tháng/năm; tách ngày giao dịch và ngày hiệu lực nếu sao kê có cả hai | Excel đảo ngày–tháng (03/04 thành 4 tháng 3) |
| Số tiền | Một cột số tiền có dấu: tiền vào dương, tiền ra âm (theo góc nhìn tài khoản doanh nghiệp) | Sao kê tách cột Nợ/Có ngược với sổ; số có dấu chấm phân cách bị đọc thành số thập phân |
| Số tham chiếu | Số chứng từ, số hóa đơn, mã giao dịch ngân hàng, nội dung chuyển khoản; bỏ khoảng trắng thừa, chữ hoa | Mã giao dịch bị cắt trong nội dung chuyển khoản |
| Đối tượng | Mã khách hàng/nhà cung cấp theo danh mục doanh nghiệp; tên viết tắt quy về mã | Cùng một đối tác có 2–3 cách viết tên |
| Dòng tổng, dòng số dư | Tách ra, không đưa vào khớp | Dòng "Cộng phát sinh" bị khớp nhầm với giao dịch |

Kiểm sau chuẩn hóa: số dòng và tổng tiền mỗi nguồn phải bằng file gốc. Lệch → dừng, liệt kê dòng mất hoặc dòng bị nhân đôi.

## 2. Bốn tầng khớp (Bước 4)

| Tầng | Điều kiện | Mức tin cậy |
|---|---|---|
| 1. Khớp chính xác | Cùng số tiền + cùng số tham chiếu (hoặc mã giao dịch xuất hiện trong nội dung chuyển khoản) | CAO |
| 2. Khớp theo ngày | Cùng số tiền + ngày lệch trong ngưỡng (mặc định ≤ 3 ngày làm việc) + cùng đối tượng nếu có | TRUNG BÌNH |
| 3. Khớp gộp | Một dòng bên này = tổng nhiều dòng bên kia (ví dụ một lần chuyển khoản trả 4 hóa đơn); các dòng phải cùng đối tượng | TRUNG BÌNH, cần kế toán xác nhận |
| 4. Chưa khớp | Không thỏa các tầng trên | Đưa vào bảng chênh lệch |

Chế độ Hóa đơn – chứng từ – sổ, khớp ba chiều: đơn đặt hàng (số lượng, đơn giá) ↔ phiếu nhập kho (số lượng thực nhận) ↔ hóa đơn (số lượng, đơn giá, thành tiền). Ghi riêng lệch số lượng và lệch đơn giá.

Không khớp một dòng với nhiều ứng viên ngang nhau. Đưa cả các ứng viên vào bảng chênh lệch, mức tin cậy THẤP.

## 3. Tám nhóm chênh lệch (Bước 5)

| Nhóm | Dấu hiệu | Hướng xử lý đề xuất |
|---|---|---|
| Chênh lệch thời điểm | Sổ ghi cuối kỳ, ngân hàng ghi đầu kỳ sau (hoặc ngược lại); séc, ủy nhiệm chi chưa qua ngân hàng | Không bút toán; theo dõi kỳ sau |
| Phí, lãi ngân hàng chưa ghi sổ | Dòng phí chuyển khoản, phí quản lý tài khoản, lãi tiền gửi chỉ có trên sao kê | Bút toán đề xuất ghi bổ sung |
| Ghi trùng | Cùng số tiền, cùng đối tượng, cùng số chứng từ xuất hiện hai lần trong sổ | Đề xuất xóa bút toán trùng — kế toán kiểm chứng từ gốc trước |
| Ghi thiếu | Có trên sao kê/hóa đơn, không có trong sổ, có chứng từ gốc | Bút toán đề xuất ghi bổ sung |
| Sai số tiền | Cùng tham chiếu, số tiền khác | Đề xuất điều chỉnh phần chênh; ghi rõ bên nào đúng theo chứng từ gốc |
| Sai đối tượng | Số tiền khớp nhưng ghi nhầm khách hàng/nhà cung cấp | Đề xuất chuyển đối tượng |
| Thiếu chứng từ | Có giao dịch nhưng không có hóa đơn/phiếu đi kèm | Không bút toán; yêu cầu bổ sung chứng từ |
| Chưa rõ nguyên nhân | Không thuộc nhóm nào, hoặc căn cứ chưa đủ | Không bút toán; kế toán điều tra |

## 4. Dấu hiệu bất thường cần báo riêng (Bước 6)

Chỉ nêu dấu hiệu, không kết luận:
- Nhiều giao dịch cùng số tiền tròn, cùng người nhận, cách nhau ngắn.
- Người nhận không có trong danh mục nhà cung cấp, hoặc số tài khoản nhận vừa thay đổi.
- Giao dịch ngoài giờ làm việc hoặc ngày nghỉ với số tiền lớn.
- Hóa đơn có số thứ tự liền nhau từ cùng một nhà cung cấp nhỏ, tổng tiền lớn.
- Khoản chi tách nhỏ ngay dưới ngưỡng duyệt chi của doanh nghiệp.

Báo riêng cho kế toán trưởng hoặc lãnh đạo, không đưa vào báo cáo gửi rộng.

## 5. Mặc định khi doanh nghiệp chưa có quy tắc (gắn [GIẢ ĐỊNH])

| Tham số | Mặc định | Ghi chú |
|---|---|---|
| Ngưỡng lệch ngày (tầng 2) | ≤ 3 ngày làm việc | Chuyển khoản liên ngân hàng cuối tuần có thể chậm hơn |
| Ngưỡng trọng yếu | Doanh nghiệp tự đặt; nếu chưa có, xếp theo số tiền giảm dần, không lọc bỏ dòng nào | Không tự đặt con số thay kế toán |
| Ghi phí ngân hàng | Theo cách doanh nghiệp đang ghi ở các kỳ trước | Hỏi nếu không có kỳ trước |

## 6. Ví dụ (công ty phân phối vật liệu xây dựng, tháng 9)

Số dư sổ tiền gửi: 1.248.500.000 đ. Số dư sao kê: 1.251.930.000 đ. Chênh: 3.430.000 đ.
- Lãi tiền gửi chưa ghi sổ: +3.600.000 đ [DỮ KIỆN: dòng sao kê ngày 30/9].
- Phí chuyển khoản tháng 9 chưa ghi sổ: −170.000 đ [DỮ KIỆN: 17 dòng phí 10.000 đ].
- Tổng giải thích được: +3.430.000 đ → bảng điều chỉnh cân. Hai bút toán đề xuất, CHỜ KẾ TOÁN DUYỆT.

*[A.I Generated — Claude Code — 30/10/2026]*
