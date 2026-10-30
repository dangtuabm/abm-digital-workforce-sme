# QUY TẮC LẬP VÀ THEO DÕI NGÂN SÁCH THEO KẾ HOẠCH

Dùng cho chế độ **Ngân sách** (Bước 9–11) và **Theo dõi** (Bước 13–14). Nguyên tắc: ngân sách đi theo kế hoạch; mỗi đồng chi gắn với một việc tạo ra nó. A.I lập, khớp và tính; con người duyệt chi.

## 1. Một dòng ngân sách gồm gì

| Trường | Ghi chú |
|---|---|
| Mã dòng | NS-01, NS-02... |
| Sáng kiến gắn với | Mã sáng kiến, hoặc "VẬN HÀNH THƯỜNG XUYÊN" |
| Phòng ban / người phụ trách | Người chịu trách nhiệm chi và giải thích chênh lệch |
| Khoản mục | Theo danh mục khoản mục của doanh nghiệp (ví dụ quảng cáo, thuê ngoài, mua sắm thiết bị, đào tạo, công tác phí) |
| Loại chi phí | Cố định / biến đổi; chi đầu tư / chi thường xuyên |
| Kỳ | Tháng hoặc quý |
| Số kế hoạch | Cùng đơn vị tiền cho toàn bảng |
| Căn cứ số | Chi phí kỳ trước, báo giá, hợp đồng, định mức × khối lượng; không có thì [GIẢ ĐỊNH] kèm cách tính |
| Số thực tế, nguồn | Chỉ lấy số kế toán đã chốt; chưa chốt ghi TẠM TÍNH |

Danh mục khoản mục và cách phân loại chi phí là **dữ liệu của doanh nghiệp**, lấy theo hệ thống tài khoản hoặc danh mục kế toán đang dùng; A.I không tự đặt ra danh mục mới.

## 2. Cách lập

1. Bắt đầu từ danh mục đã được phân bổ và kế hoạch thực thi đã duyệt; không lập ngân sách cho việc ngoài danh mục.
2. Tách **vận hành thường xuyên** (chi phí để công ty chạy như hiện nay) khỏi **ngân sách sáng kiến** (chi phí cho việc mới, thay đổi).
3. Với từng sáng kiến: liệt kê khoản mục cần chi theo mốc, tính bằng định mức × khối lượng hoặc theo báo giá; rải theo kỳ đúng thời điểm chi dự kiến.
4. Ghi **dự phòng** thành dòng riêng; mức dự phòng do người duyệt ngân sách đặt. Không giấu dự phòng vào từng dòng.
5. Khớp: tổng dòng theo sáng kiến ≤ mức được phân bổ; tổng toàn bảng ≤ ngân sách đã duyệt. Chạy công cụ kiểm.
6. Khi có kế hoạch doanh thu: đặt cạnh ngân sách chi để người duyệt thấy dòng tiền theo kỳ; dự báo nhiều kịch bản là việc mô phỏng kịch bản.

## 3. Trình duyệt

Bản trình gồm: tổng theo sáng kiến, theo phòng, theo kỳ; phần vận hành thường xuyên so với kỳ trước; các giả định lớn và ảnh hưởng nếu sai; các khoản cần duyệt riêng theo quy chế (ví dụ mua sắm trên một mức nhất định). Mức và quyền duyệt chi là **quy chế của doanh nghiệp**; A.I chỉ đọc và áp dụng, không tự đặt.

Pháp luật về thuế, chi phí được trừ, hóa đơn chứng từ: đối chiếu văn bản pháp luật hiện hành, cần người có chuyên môn xác nhận.

## 4. Theo dõi chênh lệch

- **Chênh lệch = thực tế − kế hoạch**; **% chênh lệch = chênh lệch ÷ kế hoạch × 100**. Với chi phí, chênh lệch dương là chi vượt; với doanh thu, chênh lệch dương là vượt kế hoạch — ghi rõ chiều.
- Tính theo từng dòng và lũy kế theo sáng kiến, theo phòng.
- **Ngưỡng cảnh báo** (ví dụ ±10% hoặc một số tiền tuyệt đối) do người duyệt ngân sách đặt. Dòng vượt ngưỡng phải có giải thích.
- Phân loại nguyên nhân: **giá** (đơn giá đổi), **khối lượng** (làm nhiều/ít hơn), **thời điểm** (chi sớm/muộn hơn kế hoạch, cả năm chưa chắc lệch), **phát sinh** (khoản không có trong kế hoạch), **ghi nhận** (hạch toán sai khoản mục hoặc sai kỳ).
- Chênh lệch thời điểm không phải tiết kiệm; chi ít hơn kế hoạch có thể là việc đang chậm — đối chiếu với trạng thái sáng kiến.

## 5. Đề xuất điều chỉnh

Với mỗi dòng vượt ngưỡng: nêu nguyên nhân, xu hướng đến cuối kỳ, các phương án (giữ nguyên và theo dõi; cắt giảm khoản khác cùng sáng kiến; dùng dự phòng; chuyển ngân sách từ sáng kiến khác; tạm dừng sáng kiến), ảnh hưởng tới chỉ số, người quyết. **A.I không tự chuyển ngân sách, không tự dùng dự phòng.** Điều chỉnh được duyệt tạo phiên bản ngân sách mới; giữ bản cũ để so.

## 6. Lỗi hay gặp

- Lập ngân sách bằng cách lấy năm trước cộng 10% cho mọi dòng, không gắn kế hoạch.
- Dòng ngân sách không gắn sáng kiến, cuối năm không biết tiền đi đâu.
- So số thực tế chưa chốt với kế hoạch rồi kết luận vượt chi.
- Chỉ báo dòng vượt, không báo dòng chi ít bất thường (có thể việc chưa làm).

*[A.I Generated — Claude Code — 30/10/2026]*
