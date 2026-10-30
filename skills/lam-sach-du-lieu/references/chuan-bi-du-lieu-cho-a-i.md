# CHUẨN BỊ KHO TÀI LIỆU CHO A.I HỎI ĐÁP

**Mục lục**
- I. Kiểm kê kho
- II. Cây thư mục và quy ước tên file
- III. Chuyển sang Markdown
- IV. Thông tin đầu file
- V. Làm mẫu, chuyển giao, nghiệm thu
- VI. Điều không làm

---

## I. KIỂM KÊ KHO

Báo cáo kiểm kê gồm: tổng số file theo định dạng (PDF chữ, PDF scan, Word, Excel, ảnh, khác) · file trùng (so mã băm nội dung, không so tên) · file hỏng, không mở được · tài liệu có nhiều bản (nháp, cũ, chính thức) · tên file lỗi (dấu, ký tự lạ, quá dài) · ước lượng khối lượng việc theo mức khó.

Xếp quy mô: ít (dưới vài trăm file) · trung bình · nhiều · rất nhiều — để chọn cách làm mẫu và chuyển giao.

## II. CÂY THƯ MỤC VÀ QUY ƯỚC TÊN FILE

**Cây thư mục 2–3 cấp** (nếu doanh nghiệp chưa có quy ước riêng):
- Cấp 1: phòng ban hoặc dự án.
- Cấp 2: loại tài liệu (quy trình, hợp đồng mẫu, báo giá, chính sách, biên bản).
- Cấp 3: năm hoặc quý.

Tên thư mục: chữ in hoa, không dấu, nối bằng gạch ngang (mặc định đề xuất). Không lẫn phòng ban với dự án trong cùng một cấp.

**Quy ước tên file mặc định**: `<LOAI>-<TEN>-<DD-MM-YYYY>.md` — ví dụ `QUY-TRINH-NHAP-KHO-15-09-2026.md`. Doanh nghiệp đã có quy ước thì theo quy ước đó; điều quan trọng là **thống nhất một quy ước cho cả kho**. Giữ đường dẫn đầy đủ đủ ngắn để phần mềm văn phòng mở được.

Bản hết hiệu lực chuyển vào thư mục lưu trữ, không xóa, không để lẫn với bản chính thức — A.I hay trả lời theo bản cũ nếu hai bản nằm cạnh nhau.

## III. CHUYỂN SANG MARKDOWN

| Loại file | Cách làm | Kiểm tra |
|---|---|---|
| PDF có chữ, Word | Chuyển bằng công cụ chuyển định dạng, giữ tiêu đề, danh sách, bảng | So số trang/mục với bản gốc |
| PDF scan, ảnh | Nhận dạng chữ (OCR), sau đó kiểm tra chéo độc lập với ảnh gốc | Chuyển người xem khi độ tin cậy dưới ngưỡng doanh nghiệp đặt, khi là tài liệu chính thức hoặc chạm Ranh giới Đỏ |
| Excel nhiều công thức | **Giữ file gốc**, tạo file `.md` mô tả: mục đích, các sheet, ý nghĩa cột, nơi lưu file gốc | Không chuyển thành bảng Markdown vì sẽ mất công thức |
| Excel dạng danh sách đơn giản | Có thể chuyển thành bảng hoặc giữ CSV | Đủ dòng, đủ cột |

Tài liệu Vàng chỉ xử lý bằng tài khoản A.I của công ty hoặc sau khi che; tài liệu Đỏ (bảng lương, hợp đồng giá trị lớn có thông tin nhạy cảm) chỉ xử lý bằng công cụ chạy nội bộ hoặc dịch vụ doanh nghiệp có cam kết bảo vệ dữ liệu, không dùng bản miễn phí công cộng.

## IV. THÔNG TIN ĐẦU FILE

Mỗi file `.md` có khối thông tin đầu file với tối thiểu 5 trường: tiêu đề · loại tài liệu · ngày · phòng ban · trạng thái (nháp / chính thức / hết hiệu lực). Nên thêm: người phụ trách, nhãn dữ liệu, file gốc, phiên bản. Mẫu: `templates/mau-thong-tin-dau-file.md`.

## V. LÀM MẪU, CHUYỂN GIAO, NGHIỆM THU

1. **Làm mẫu** một lô đại diện nhiều mức khó (gợi ý 50–100 file, doanh nghiệp điều chỉnh theo quy mô kho) để chứng minh cách làm và đo thời gian thật.
2. **SOP chuyển giao**: các bước, ảnh chụp màn hình minh họa, ví dụ đúng – sai, ai làm phần nào, hỏi ai khi vướng.
3. **Hướng dẫn một buổi** cho nhân viên sẽ làm tiếp (nội dung lấy từ SOP).
4. **Nghiệm thu** sau một khoảng thời gian doanh nghiệp chốt: tỷ lệ file đúng chuẩn (tên, thư mục, thông tin đầu file, định dạng) so với ngưỡng doanh nghiệp đặt (gợi ý từ 90% trở lên) [GIẢ ĐỊNH — người phụ trách chốt]. Đạt mới mở rộng sang phần kho tiếp theo.

## VI. ĐIỀU KHÔNG LÀM

- Không nhận làm hết toàn bộ kho thay nhân viên; làm mẫu rồi chuyển giao.
- Đợt đầu không nhảy sang tóm tắt nội dung hay gắn thẻ chuyên sâu.
- Không công bố kết quả nhận dạng chữ chưa kiểm tra chéo.
- Không thiết kế trợ lý hỏi đáp trong việc này — dữ liệu sạch chỉ là nguyên liệu.

*[A.I Generated — Claude Code — 30/10/2026]*
