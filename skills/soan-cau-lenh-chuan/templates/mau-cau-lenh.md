# MẪU SOẠN CÂU LỆNH

**Mục lục**
- Mẫu 1 — Bảng soát 6 nhãn (Bước 2)
- Mẫu 2 — Một câu hỏi phỏng vấn ngược (Bước 3)
- Mẫu 3 — Bản tóm lược đề bài chờ duyệt (Bước 4)
- Mẫu 4 — Bốn dạng câu lệnh thành phẩm (Bước 5): 4A · 4B · 4C · 4D
- Mẫu 5 — Gói bàn giao (Bước 6)
- Quy tắc điền

---

## MẪU 1 — BẢNG SOÁT 6 NHÃN

```
BẢNG SOÁT CÂU LỆNH — [Tên nhu cầu] — [dd/mm/yyyy]
Chế độ: [A VIẾT MỚI / B NÂNG CẤP / C DÙNG MẪU DOANH NGHIỆP — mã ...]
Van 3 cổng: Cổng 1 [Đủ/Chưa đủ] · Cổng 2 [Gấp/Không] · Cổng 3 [Rẻ/Đắt]
→ Kết luận: [Xuất ngay / Nêu giả định rồi xuất / Hỏi N câu]

| Nhãn            | Trạng thái     | Căn cứ / ghi chú                 |
|-----------------|----------------|----------------------------------|
| ROLE            | Mặc định được  | [suy từ TASK + lĩnh vực]         |
| TASK            | Đã rõ          | [trích phần đã rõ]               |
| DETAILS         | Khuyết         | [thiếu dữ liệu gì]               |
| CONTEXT         | ...            | ...                              |
| FORMAT & STYLE  | ...            | ...                              |
| NOTE            | ...            | ...                              |

Phân loại dữ liệu: [Xanh / Vàng — cần che ... / Đỏ — không dán vào A.I]
Số câu sẽ hỏi: [N] — bằng số nhãn khuyết không mặc định được (tối đa 8).
```

Chế độ B thêm cột "Điểm hiện tại (0–2)" và tổng điểm câu lệnh cũ.

---

## MẪU 2 — MỘT CÂU HỎI PHỎNG VẤN NGƯỢC

```
Câu [i]/[N] — Nhãn [TASK/CONTEXT/...]

[Nội dung hỏi — một câu, thẳng]

A. [Phương án 1 — cụ thể, có số/đối tượng]
B. [Phương án 2]
C. [Phương án 3]
D. Khác — Anh/Chị tự ghi

Vì sao em hỏi: [một dòng — gắn nhãn nào, hậu quả nếu đoán sai]
```

Hỏi xong dừng, đợi trả lời. Người dùng muốn "hỏi một lượt" → tối đa 3 câu mỗi lượt, đánh số, mỗi câu vẫn đủ cấu trúc trên.

---

## MẪU 3 — BẢN TÓM LƯỢC ĐỀ BÀI CHỜ DUYỆT

```
TÓM LƯỢC ĐỀ BÀI — [Tên câu lệnh] — [dd/mm/yyyy]

ROLE:            [...]
TASK:            [...]
DETAILS:         [...]
CONTEXT:         [...]
FORMAT & STYLE:  [...]
NOTE:            [...]
Tiêu chí đạt (đưa vào câu tự kiểm): [tiêu chí 1] · [tiêu chí 2] · …

ĐÃ XÁC NHẬN:      [điểm do người dùng trả lời]
[SUY LUẬN]:       [điều suy ra từ ngữ cảnh — suy từ đâu]
[GIẢ ĐỊNH]:       [nội dung — căn cứ]
CHỜ QUYẾT ĐỊNH:   [nếu có]

Anh/Chị duyệt đề bài này để em xuất câu lệnh nhé?
```

---

## MẪU 4 — BỐN DẠNG CÂU LỆNH THÀNH PHẨM

### 4A — Câu lệnh chuẩn 6 nhãn

```text
[ROLE] Bạn là [Chọn góc nhìn: Cố vấn lãnh đạo / Chuyên gia nghiệp vụ / Chuyên viên phân tích / Biên tập viên / Khác: …], làm việc ở mức [Chọn: Tổng quan / Chuyên sâu / Liên ngành] trong lĩnh vực [Điền lĩnh vực; gợi ý: Kinh doanh / Tài chính / Nhân sự / Vận hành / Khác: …]. Khi thực hiện, hãy làm việc theo quan điểm [Chọn 1–3: Dựa trên bằng chứng / Khách hàng là trọng tâm / Tinh gọn / Tuân thủ / Phản biện / Khác: …].

[TASK] Tôi cần Bạn [động từ hành động + đối tượng cụ thể]. Thực hiện theo thứ tự:
1. [...]
2. [...]
3. [...]
Kết quả cuối cùng cần giúp Tôi [kết quả mong muốn].

[DETAILS] Tôi cung cấp cho Bạn: [dữ kiện / file đính kèm]. Dữ liệu cần xử lý:
"""
[dán dữ liệu đã che thông tin nhạy cảm]
"""
Ưu tiên nguồn Tôi cung cấp; khi cần tìm thêm, ưu tiên nguồn chính thức, ghi ngày truy cập.

[CONTEXT] Tôi dùng kết quả cho [Chọn đối tượng: Ban giám đốc / Quản lý / Nhân viên / Khách hàng / Đối tác / Khác: …] qua [Chọn kênh: Cuộc họp / Email / Zalo / Tài liệu nội bộ / Bài thuyết trình / Khác: …], với mục đích [Điền mục tiêu; gợi ý: Ra quyết định / Phê duyệt / Triển khai / Đào tạo / Truyền thông / Khác: …]. Điều chỉnh nội dung cho phù hợp đối tượng này.

[FORMAT & STYLE] Định dạng: [Chọn 1 hoặc kết hợp: Bảng so sánh / Checklist / Báo cáo / Kế hoạch hành động; điền cấu trúc cần có]. Giọng: [Chọn 1–2: Trực diện / Súc tích / Trang trọng / Dễ hiểu / Thuyết phục / Khác: …]. Độ dài: [số từ / số trang / số ý].

[NOTE] Lưu ý:
- Không bịa số liệu, nguồn, quy định; thiếu thông tin thì ghi rõ "chưa có dữ liệu" hoặc hỏi lại Tôi.
- Số liệu không có nguồn phải ghi [Giả định] hoặc [Minh họa].
- Chỉ soạn nội dung; không tự gửi, công bố, chi tiền hoặc ghi đè dữ liệu.
- [Ràng buộc nghiệp vụ / điều cấm cụ thể].
- Trước khi trả, tự kiểm: [tiêu chí 1]; [tiêu chí 2]; … (mỗi tiêu chí kiểm được).
```

### 4B — Câu lệnh rút gọn (việc đơn giản)

```text
[Động từ hành động + đối tượng + kết quả mong muốn], dành cho [Chọn đối tượng: Ban giám đốc / Quản lý / Nhân viên / Khách hàng / Khác: …], dạng [Chọn 1 hoặc kết hợp: Đoạn văn / Bảng / Checklist / Khác: …], khoảng [độ dài]. Không bịa thông tin; chưa chắc thì ghi rõ.
```

### 4C — Chuỗi câu lệnh

```text
CÂU LỆNH 1 — DÀN Ý
[ROLE] ... [DETAILS] ... [CONTEXT] ...
[TASK] Ở bước này CHỈ phân tích dữ liệu và lập dàn ý chi tiết cho [sản phẩm]: các phần, ý chính, dữ liệu dùng cho từng phần, điểm còn thiếu. Chưa viết nội dung.
[NOTE] Không bịa dữ liệu. Trước khi trả, tự kiểm: dàn ý phủ đủ [tiêu chí].

— Người dùng duyệt/chỉnh dàn ý —

CÂU LỆNH 2..n — TRIỂN KHAI
Dựa trên dàn ý đã chốt, triển khai ĐÚNG phần [số/tên]. Giữ [định dạng, giọng, độ dài]. Không thêm số liệu ngoài nguồn. Trước khi trả, tự kiểm: [tiêu chí phần này].
```

### 4D — Câu lệnh để A.I khác tự phỏng vấn người dùng

```text
[ROLE] Bạn là trợ lý làm rõ yêu cầu, giỏi đặt câu hỏi ngắn, có phương án sẵn để người bận rộn chọn nhanh.

[TASK] Tôi muốn nhờ A.I làm việc sau: [mô tả nhu cầu ban đầu]. Trước khi làm, hãy phỏng vấn Tôi để có đủ thông tin:
1. Đọc nhu cầu trên, xác định thông tin còn thiếu để làm đúng: mục tiêu, người dùng kết quả, dữ liệu đầu vào, hình thức và độ dài, điều cấm.
2. Hỏi Tôi từ 3 đến 8 câu trong một lượt, đánh số. Mỗi câu có 2–4 phương án cụ thể để Tôi chọn và một lựa chọn "Khác". Chỉ hỏi điều thật sự thiếu.
3. Sau khi Tôi trả lời, tóm lại đề bài trong 5–7 dòng và hỏi Tôi xác nhận.
4. Khi Tôi xác nhận, mới bắt đầu làm việc.

[NOTE] Không đoán thay Tôi ở các điểm về số liệu, tiền, khách hàng, nhân sự. Không bắt đầu làm khi chưa có xác nhận. Trước khi hỏi, tự kiểm: mỗi câu có phương án cụ thể, không hỏi điều Tôi đã nói.
```

Chỉ điền `[mô tả nhu cầu ban đầu]`; giữ nguyên phần còn lại.

---

## MẪU 5 — GÓI BÀN GIAO

```
CÂU LỆNH: [Tên] — dạng [4A/4B/4C/4D] — [dd/mm/yyyy]

[khối câu lệnh]

PHIẾU CHẤM: ROLE [x/2] · TASK [x/2] · DETAILS [x/2] · CONTEXT [x/2] · FORMAT & STYLE [x/2] · NOTE [x/2] = [xx/12] → [ĐẠT / CẢNH BÁO nhãn ...]
GIẢ ĐỊNH: [GIẢ ĐỊNH] ... (hoặc "Không có")
Ô CẦN ĐIỀN KHI CHẠY: [liệt kê, nếu có]
DỮ LIỆU: [nhắc phân loại Xanh – Vàng – Đỏ nếu có dữ liệu doanh nghiệp]
TINH CHỈNH: lệch hướng → tạo lại · quên dữ kiện → sửa câu lệnh gốc · đạt khoảng 90% → hỏi tiếp sửa đúng phần.
LƯU MẪU: [đề xuất thêm vào thư viện câu lệnh doanh nghiệp: mã · tên · nơi lưu — chờ duyệt] (chỉ khi dùng lặp lại)
```

---

## QUY TẮC ĐIỀN

| Loại ô | Ví dụ |
|---|---|
| Chọn một | `[Chọn 1: Báo cáo / Tờ trình / Kế hoạch / Checklist / Khác: …]` |
| Chọn nhiều | `[Chọn 1–3: Giảm sai sót / Rút ngắn thời gian / Chuẩn hóa thao tác / Khác: …]` |
| Điền thật | `[Điền ngân sách được duyệt và đơn vị tiền]` |
| Mô tả có gợi ý | `[Mô tả vấn đề; gợi ý: Báo cáo trễ / Số liệu lệch / Trùng việc / Khác: …]` |

- Khi bàn giao mẫu dùng lại, hướng dẫn giữ lựa chọn phù hợp và bỏ phần không dùng. Khi bàn giao câu lệnh cho việc đã rõ, điền thẳng dữ kiện đã xác nhận.
- Gợi ý theo nghiệp vụ: câu lệnh cho kho dùng "Phiếu nhập / Phiếu xuất / Biên bản kiểm kê", không dùng menu chung.
- Tên, số tiền, hạn, nguồn, quyền không thay bằng giá trị giả. Nhãn `[ROLE]`…`[NOTE]` và `[GIẢ ĐỊNH]` không phải ô lựa chọn.
- Mỗi câu lệnh một khối sao chép, xuống dòng theo nhóm thông tin. Không chia vụn một câu lệnh cần chạy cùng nhau.
- Mọi `[...]` trong câu lệnh thành phẩm phải được thay — trừ ô điền có chủ đích, đã liệt kê ở "Ô cần điền khi chạy".
- Giá trị A.I tự mặc định nằm ở mục GIẢ ĐỊNH, không trộn như dữ kiện. Không đưa nội dung thực thi việc vào gói bàn giao.
