# SÁU NHÃN CÂU LỆNH — TRA CỨU

**Mục lục**
- I. Quy đổi hai bộ "6 thành phần"
- II. Diễn giải 6 nhãn câu lệnh
- III. Phiếu chấm câu lệnh 6 nhãn (12 điểm)
- IV. Van 3 cổng — bảng quyết định
- V. Sáu lỗi hay gặp kèm ví dụ đối chiếu
- VI. Kỹ thuật nâng cao khi xuất câu lệnh
- VII. Dùng thư viện câu lệnh mẫu của doanh nghiệp

---

## I. QUY ĐỔI HAI BỘ "6 THÀNH PHẦN"

Có hai bộ cùng gọi "6 thành phần", phục vụ hai đầu ra khác nhau. Không đổi tên bộ nào; chỉ quy đổi khi cần.

| Bản chốt đầu bài (làm rõ yêu cầu) | → | Câu lệnh 6 nhãn |
|---|---|---|
| 1. MỤC TIÊU — phục vụ gì, ai dùng | → | **TASK** (kết quả cần đạt) + **CONTEXT** (người dùng, mục đích) |
| 2. ĐẦU RA — sản phẩm, định dạng, dung lượng, nơi lưu | → | **FORMAT & STYLE** |
| 3. PHẠM VI — làm gì / không làm gì | → | **TASK** (làm gì) + **NOTE** (không làm gì) |
| 4. ĐẦU VÀO & NGUỒN — dữ liệu, nguồn thắng khi mâu thuẫn | → | **DETAILS** |
| 5. TIÊU CHÍ NGHIỆM THU | → | **NOTE** — câu "Trước khi trả, tự kiểm: ..." |
| 6. RÀNG BUỘC & RANH GIỚI ĐỎ | → | **NOTE** |
| (không có) | → | **ROLE** — suy từ TASK và lĩnh vực; thường mặc định được |

Hệ quả: một bản chốt đầu bài đã duyệt chuyển thành câu lệnh 4A mà **không cần hỏi lại** — chỉ bổ sung ROLE.

---

## II. DIỄN GIẢI 6 NHÃN CÂU LỆNH

| Nhãn | Nghĩa | Câu hỏi cốt lõi | Đạt khi | Lỗi hay gặp |
|---|---|---|---|---|
| **ROLE** | Vai trò | A.I đóng vai ai? | Chức danh + mức chuyên sâu mong muốn + quan điểm làm nghề | "Bạn là chuyên gia marketing." — thiếu góc nhìn |
| **TASK** | Nhiệm vụ | A.I làm gì? | Mở bằng động từ hành động; rõ, cụ thể; việc phức tạp liệt kê bước | "Nói về...", "Viết về..." |
| **DETAILS** | Dữ liệu đầu vào | Dựa trên dữ liệu nào? | Đủ, đúng, liên quan, đã che thông tin nhạy cảm; dữ liệu dài bọc `"""..."""`; có thể kèm ví dụ mẫu | Để A.I tự đoán số liệu |
| **CONTEXT** | Bối cảnh | Dùng cho ai, để làm gì? | Nêu người đọc + kênh + mục đích | Đúng nội dung, sai người đọc |
| **FORMAT & STYLE** | Hình thức và văn phong | Trình bày thế nào, giọng gì, dài bao nhiêu? | Định dạng cụ thể + giọng + **số đo** độ dài (từ, trang, ý) | "Ngắn gọn thôi" |
| **NOTE** | Lưu ý | Không được làm gì, kiểm gì trước khi trả? | 4 dòng bắt buộc + ràng buộc nghiệp vụ | Không có dòng chống bịa; không có câu tự kiểm |

Bốn dòng bắt buộc của NOTE (dạng 4A, 4C):
1. Không bịa số liệu, nguồn, quy định; thiếu thì ghi "chưa có dữ liệu" hoặc hỏi lại.
2. Số không có nguồn ghi [Giả định] hoặc [Minh họa].
3. Chỉ soạn nội dung; không tự gửi, công bố, chi tiền, ghi đè dữ liệu.
4. "Trước khi trả, tự kiểm: [tiêu chí 1]; [tiêu chí 2]; …"

Việc đơn giản (tra cứu, dịch một câu) không cần đủ 6 nhãn → dạng 4B. Việc quan trọng, mở phiên mới → bắt buộc 4A.

---

## III. PHIẾU CHẤM CÂU LỆNH 6 NHÃN (12 ĐIỂM)

Mỗi nhãn 0 · 1 · 2 điểm.

| Nhãn | 0 điểm | 1 điểm | 2 điểm |
|---|---|---|---|
| ROLE | Không có | Chỉ chức danh | Chức danh + mức chuyên sâu + quan điểm làm nghề |
| TASK *(bắt buộc)* | Mơ hồ / không động từ hành động | Có động từ, thiếu yêu cầu phụ hoặc bước | Động từ hành động + kết quả mong muốn + bước (nếu phức tạp) |
| DETAILS *(bắt buộc khi có dữ liệu)* | Không có, A.I phải đoán | Có nhưng thiếu, nhiễu, chưa che thông tin nhạy cảm | Đủ, đúng, liên quan, tách rõ khỏi mệnh lệnh |
| CONTEXT | Không có | Có mục đích hoặc người đọc | Có người đọc, kênh, mục đích |
| FORMAT & STYLE | Không có | Có định dạng, thiếu số đo độ dài hoặc giọng | Định dạng + giọng + số đo độ dài |
| NOTE *(bắt buộc)* | Không có | Có ràng buộc, thiếu ít nhất 1 trong 4 dòng bắt buộc | Đủ 4 dòng bắt buộc + ràng buộc nghiệp vụ |

**Ngưỡng [GIẢ ĐỊNH, doanh nghiệp có thể chỉnh]:** từ 10/12 và không nhãn bắt buộc nào 0 điểm → ĐẠT. 7–9 → tự sửa 1 vòng. Từ 6 trở xuống → quay lại hỏi bổ sung (nếu Van 3 cổng cho phép).

---

## IV. VAN 3 CỔNG — BẢNG QUYẾT ĐỊNH

Chạy im lặng, không hiển thị cho người dùng.

| Cổng 1 — đủ dữ kiện? | Cổng 2 — tín hiệu gấp? | Cổng 3 — đoán sai đắt? | Hành động |
|---|---|---|---|
| Đủ | — | — | Xuất câu lệnh ngay, không hỏi |
| Chưa đủ | Có | — | Nêu giả định, xuất câu lệnh, ghi rõ chỗ đã đoán |
| Chưa đủ | Không | Rẻ | Tự mặc định, gắn [GIẢ ĐỊNH], xuất câu lệnh |
| Chưa đủ | Không | Đắt | **Bật phỏng vấn ngược** |

Tín hiệu gấp: "viết luôn", "khỏi hỏi", "làm nhanh", "đưa bản nháp trước", hoặc đã trả lời cùng câu ở lượt trước.
Đắt khi có ít nhất một: câu lệnh dùng lặp lại hoặc phát cho nhiều người · chạm tiền · khách hàng thật · pháp lý · nhân sự – lương · dữ liệu cá nhân · dữ liệu thật · đầu ra đi ra ngoài công ty.

---

## V. SÁU LỖI HAY GẶP KÈM VÍ DỤ ĐỐI CHIẾU

**1. Hỏi đủ 6 câu cho tròn bộ.**
Số câu bám nhãn **khuyết**, không bám số nhãn. Đã rõ lĩnh vực trong TASK thì không hỏi ROLE.

**2. Phương án chung chung.**
Sai: "Anh muốn dài hay ngắn?" · Đúng: "Khoảng 150 từ cho Zalo · 1 trang A4 · 3 trang có bảng".

**3. ROLE thổi phồng thành sự thật.**
Sai: "Bạn có 20 năm kinh nghiệm nên luôn đúng." · Đúng: "Bạn đóng vai Kế toán trưởng doanh nghiệp phân phối, làm việc thận trọng, dựa trên số liệu."

**4. NOTE thiếu hàng rào.**
Sai: câu lệnh phân tích công nợ không có dòng chống bịa. · Đúng: "Chỉ dùng số trong file đính kèm; thiếu thì ghi 'chưa có dữ liệu'; số minh họa ghi [Minh họa]."

**5. Nhồi một câu lệnh cho nhiệm vụ nhiều tầng.**
Phần giữa của câu lệnh dài hay bị làm hời hợt. · Đúng: dạng 4C — bước 1 chỉ lập dàn ý, người duyệt, rồi triển khai từng phần.

**6. Lấn sân thực thi.**
Sai: viết câu lệnh xong tự chạy và trả luôn báo cáo. · Đúng: bàn giao câu lệnh, dừng; chạy là việc tiếp theo khi được giao rõ.

---

## VI. KỸ THUẬT NÂNG CAO KHI XUẤT CÂU LỆNH

Chỉ thêm khi việc cần.

| Kỹ thuật | Khi nào | Cách đưa vào câu lệnh |
|---|---|---|
| Chuỗi câu lệnh | Việc nhiều tầng, tài liệu dài | Dạng 4C, mỗi bước một câu lệnh, có điểm duyệt |
| Suy luận từng bước | Bài toán tính toán, suy luận | NOTE: "Trình bày các bước lập luận trước khi kết luận." |
| Nhân bản cấu trúc từ tài liệu mẫu | Có tài liệu mẫu muốn làm tương tự | TASK: "Phân tích cấu trúc, logic, văn phong tài liệu sau, rồi tạo câu lệnh để làm tài liệu tương tự cho [chủ đề]." |
| Giải thích và dẫn nguồn | Đầu ra có số liệu, khẳng định | NOTE: "Nêu nguồn cho mọi số liệu; không có nguồn ghi [Chưa xác minh]." |
| Đối chiếu nhiều công cụ A.I | Quyết định quan trọng | Hướng dẫn kèm: chạy cùng câu lệnh trên 2 công cụ, so khác biệt |
| Phản biện | Kế hoạch, đề xuất | Câu lệnh nối tiếp: "Đóng vai người phản biện, chỉ ra 5 điểm yếu lớn nhất của bản sau…" |

Hướng dẫn tinh chỉnh bàn giao kèm câu lệnh: lệch hướng hoàn toàn → tạo lại câu trả lời · quên dữ kiện → sửa câu lệnh gốc, không gõ thêm bên dưới · đạt khoảng 90% → hỏi tiếp, sửa đúng phần.

---

## VII. DÙNG THƯ VIỆN CÂU LỆNH MẪU CỦA DOANH NGHIỆP

- Doanh nghiệp tự xây thư viện theo `templates/thu-vien-cau-lenh-doanh-nghiep.csv`: mỗi mẫu có mã, nhóm việc, tên, dạng (4A/4B/4C/4D), nơi lưu nguyên văn, người phụ trách, phiên bản, trạng thái.
- Chỉ dùng mẫu có trạng thái ĐANG DÙNG. Dẫn **mã mẫu** khi dùng; lấy nguyên văn từ nơi lưu, chỉ điền ô trống.
- Mẫu chuyên biệt không đủ 6 nhãn vẫn là mẫu hợp lệ — không ép về 6 nhãn.
- Không có mẫu khớp hoặc không mở được nơi lưu → báo rõ, chuyển chế độ viết mới; không dựng lại "mẫu" từ trí nhớ.
- Khi soạn câu lệnh mới cho tài liệu hướng dẫn nội bộ: dẫn mã mẫu, không sao chép mẫu thành bản cạnh tranh.
- Câu lệnh tốt dùng lặp lại → đề xuất thêm vào thư viện (mã, tên, nơi lưu), chờ người phụ trách duyệt.

*[A.I Generated — Claude Code — 30/10/2026]*
