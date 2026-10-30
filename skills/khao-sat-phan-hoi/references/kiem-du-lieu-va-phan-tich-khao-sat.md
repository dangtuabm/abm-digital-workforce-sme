# KIỂM DỮ LIỆU VÀ PHÂN TÍCH KHẢO SÁT

## Mục lục
1. Cổng sẵn sàng dữ liệu
2. Tính chỉ số
3. So sánh nhóm
4. Nhóm ý kiến mở
5. Sai lệch và cách nói đúng mức
6. Đọc kết quả theo ngưỡng

## 1. Cổng sẵn sàng dữ liệu

**Dòng người trả lời** — giữ riêng từng số: đã gửi/đã nhận link · bắt đầu · hoàn thành · bỏ dở · bị loại do không thuộc đối tượng · trùng · phiếu thử · không hợp lệ. Chỉ dùng từ "tỷ lệ phản hồi" khi có số đã gửi làm mẫu số.

**Bảy điểm kiểm:**
1. Mã câu, thang đo, cách mã hóa, câu bỏ qua có điều kiện đúng phiên bản bảng hỏi.
2. Kiểu dữ liệu, khoảng giá trị khớp thang đo; câu trống **không** bị đổi thành 0.
3. Mỗi phiếu một mã; quy tắc xử lý trùng có người duyệt.
4. Đường trả lời không hợp lý, trả lời mâu thuẫn, trả lời quá nhanh, chọn cùng một đáp án cho mọi câu được ghi lại — ghi cờ không có nghĩa là tự loại.
5. Trọng số (nếu có): nguồn, phiên bản, trọng số quá lớn.
6. Câu mở: mã chữ, ngôn ngữ, thông tin cá nhân cần che.
7. Số trong dòng người trả lời khớp với số dòng dữ liệu.

**Kết luận:**
- **ĐẠT** — đủ để phân tích; lỗi nhỏ không đổi con số chính.
- **CÓ ĐIỀU KIỆN** — phân tích được phần xác định; giới hạn ghi theo từng chỉ số.
- **KHÔNG ĐẠT** — thiếu bảng hỏi, mẫu số, dòng người trả lời hoặc lỗi làm chỉ số không đọc được; dừng báo cáo con số chính.

Mỗi lần sửa hoặc loại phiếu ghi: quy tắc · số trước/sau · chỉ số bị ảnh hưởng · người duyệt.

## 2. Tính chỉ số

Mỗi chỉ số ghi: mã chỉ số · mã câu, phiên bản · nhóm người · tử số · mẫu số · cỡ mẫu chưa gia quyền · mẫu số đã gia quyền (nếu có) · số câu trống, số phiếu loại · công thức · nguồn.

- Luôn viết % kèm tử số/mẫu số: "70% (70/100 người trả lời câu 5)".
- Không trộn mẫu số: 70 người hài lòng trong 100 người trả lời câu 5 **không** phải 70% của 400 phiếu hoàn thành.
- Thang Likert: báo phân phối từng mức (1–5) cùng điểm trung bình; không mặc định coi khoảng cách giữa các mức là bằng nhau.
- Trung bình có trọng số: không dùng mẫu số gia quyền như số người thật.
- Chạy `scripts/kiem_chi_so_khao_sat.py` trên bảng chỉ số trước khi viết báo cáo.

## 3. So sánh nhóm

- Chỉ so nhóm đã định trước (ví dụ chi nhánh, nhóm khách); không lục tìm nhóm cho tới khi thấy chênh lệch.
- Nhóm quá nhỏ (mặc định dưới 5 người trả lời với khảo sát nội bộ [GIẢ ĐỊNH, doanh nghiệp chốt]) → gộp nhóm hoặc không báo; chú ý không để người đọc đoán ra qua phép trừ.
- Báo độ chênh và mức không chắc chắn (khoảng tin cậy khi điều kiện cho phép), không chỉ nói "cao hơn".
- So nhiều cặp nhóm cùng lúc → gắn nhãn "khám phá", không kết luận chắc.
- So theo thời gian chỉ khi cùng bảng hỏi, cùng thang đo, cùng cách chọn mẫu; nếu đổi thì ghi "không so trực tiếp được".

## 4. Nhóm ý kiến mở

1. Đọc toàn bộ câu trả lời, không lọc trước.
2. Lập bộ mã: tên chủ đề · định nghĩa · thế nào là thuộc/không thuộc · ví dụ. Ghi phiên bản bộ mã.
3. Một câu trả lời có thể thuộc nhiều chủ đề.
4. Đếm theo số người nhắc tới chủ đề, ghi rõ mẫu số (người trả lời câu mở, không phải tổng phiếu).
5. Trích dẫn đã che tên, số điện thoại, chi tiết dễ nhận diện; kèm một phản ví dụ khi chủ đề quan trọng.
6. Nhận diện cảm xúc tích cực/tiêu cực chỉ là gợi ý, không phải sự thật.

## 5. Sai lệch và cách nói đúng mức

Các sai lệch cần xem: người tự chọn tham gia (link mở) · thiếu nhóm người trong danh sách gửi · người không trả lời khác người trả lời · nhớ sai · trả lời theo điều "nên nói" · thứ tự và cách hỏi · kênh khảo sát. Trọng số sửa được một phần lệch cơ cấu, không sửa được mọi sai lệch.

| Nói quá | Nói đúng mức |
|---|---|
| "82% khách hàng bất mãn" | "Trong 820 người trả lời qua link mở, 82% chấm 1–2; mẫu tự chọn nên không đại diện toàn bộ khách" |
| "Chương trình X làm nhân viên nghỉ việc" | "Nhóm có điểm thấp ở câu X có tỷ lệ nghỉ cao hơn; đây là tương quan, chưa chứng minh nguyên nhân" |
| "Khách thích món mới" | "45/120 người trả lời câu mở nhắc tới món mới theo hướng tích cực; 12 người góp ý về giá" |

Khảo sát cho biết người trả lời **cảm nhận** gì, không tự chứng minh sự việc vận hành (ví dụ "giao chậm" cần đối chiếu dữ liệu giao hàng).

## 6. Đọc kết quả theo ngưỡng

Ngưỡng do doanh nghiệp đặt trong Kế hoạch phân tích. Khi chưa có, có thể dùng ngưỡng khởi điểm sau và gắn [GIẢ ĐỊNH]:

| Điểm Likert trung bình | Đọc | Hành động gợi ý |
|---|---|---|
| ≥ 4,0 | Đạt | Giữ, ghi cách làm tốt |
| 3,5 – 3,9 | Cần cải thiện | Có việc cải tiến, người phụ trách, hạn trong khoảng 2 tuần |
| < 3,5 | Có vấn đề | Họp xem lại trong khoảng 1 tuần |

Chủ đề ý kiến mở được nhắc bởi khoảng 30% người trả lời câu mở trở lên → nên có việc cần làm cụ thể [GIẢ ĐỊNH]. Lựa chọn "Khác" được chọn nhiều (khoảng 20% trở lên) → xem lại danh sách đáp án ở lần sau.

Hành động liên hệ từng người (ví dụ gọi người chấm NPS thấp) chỉ làm khi người trả lời đã đồng ý được liên hệ, và do người phụ trách thực hiện.

*[A.I Generated — Claude Code — 30/10/2026]*
