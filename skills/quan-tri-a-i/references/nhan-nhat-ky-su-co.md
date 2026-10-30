# NHÃN VẾT A.I, NHẬT KÝ, SỰ CỐ VÀ NGOẠI LỆ

**Mục lục**
- I. Nhãn vết A.I
- II. Sổ nhật ký A.I
- III. Phân cấp sự cố và quay lui
- IV. Ngoại lệ

---

## I. NHÃN VẾT A.I

**Ba nhãn, một cú pháp cho cả công ty**: `[Loại — Tên Nhân sự số — Thời điểm]`

| Nhãn | Dùng khi | Ví dụ |
|---|---|---|
| `[A.I Generated — ... — ...]` | A.I tạo mới nội dung, file | `[A.I Generated — A15 Tư vấn bán hàng — 30/10/2026]` |
| `[A.I Agent Update — ... — ...]` | A.I sửa một nội dung đã có | `[A.I Agent Update — A30 Kế toán tổng hợp — 30/10/2026 14:20]` |
| `[A.I Suggested — ... — ...]` | A.I chỉ đề xuất, người quyết | `[A.I Suggested — A27 Điều phối kho — 30/10/2026]` |

- A.I bắt buộc tự gắn nhãn. Nội dung chỉ chuyển sang chính thức khi người duyệt ghi tên và ngày.
- Không đổi cú pháp theo từng phòng ban: một cú pháp giúp tìm kiếm và lọc được trên toàn công ty.
- Nhãn không thay người rà, không thay sự đồng ý của khách, không thay nhật ký.

## II. SỔ NHẬT KÝ A.I

**Trường bắt buộc**: thời điểm · Nhân sự số · phiên bản (Thẻ, Skill, mô hình) · loại hành động · đối tượng (file, bản ghi) · dữ liệu nguồn (đường dẫn, không chép dữ liệu thô) · quyền đã dùng · trước / sau (tóm tắt hoặc đường dẫn) · trạng thái · người rà · mã theo dõi · lỗi, chạy lại · chi phí · ghi chú.

**Quy tắc**
- Lưu trong bảng tính hoặc phần mềm quản lý công việc của doanh nghiệp; có bản sao định kỳ.
- A.I chỉ được **ghi thêm dòng mới**; không sửa, không xóa. Người có quyền chỉ sửa khi xử lý sự cố và phải ghi dòng giải trình.
- Che dữ liệu Vàng; không ghi dữ liệu Đỏ, mật khẩu, khóa kết nối.
- Thời hạn lưu và ai được xem do doanh nghiệp chốt.

**Từ khóa dừng và cảnh báo**: từ khóa dừng khiến A.I dừng lại hỏi người phụ trách; từ khóa cảnh báo khiến A.I gắn cờ và báo. Đây là lời dặn bổ sung — muốn chặn thật phải hạ quyền.

## III. PHÂN CẤP SỰ CỐ VÀ QUAY LUI

| Cấp | Ví dụ | Xử lý mặc định đề xuất (doanh nghiệp chốt thời hạn) |
|---|---|---|
| **1 — Nhẹ** | Sai chính tả trong bản nháp nội bộ, gắn nhầm nhãn | A.I tự sửa, ghi nhật ký |
| **2 — Trung bình** | Gửi nhầm tài liệu nội bộ cho sai phòng, tổng hợp sai số liệu đã dùng trong họp | Báo người phụ trách (gợi ý trong 24 giờ), sửa, biên bản ngắn |
| **3 — Nặng** | Gửi nhầm báo giá cho khách, lộ dữ liệu khách hàng, sửa nhầm dữ liệu thật | Dừng Nhân sự số, báo lãnh đạo ngay (gợi ý trong 2 giờ), giữ bằng chứng, điều tra |

**Các bước**: phát hiện → phân cấp → khoanh vùng → dừng / thu quyền → quay lui → đối chiếu → giữ nguyên bằng chứng → báo đúng người theo thẩm quyền → khôi phục → tìm nguyên nhân gốc → khắc phục → kiểm lại → cho chạy lại khi đạt điều kiện.

Việc báo ra ngoài (khách hàng, cơ quan chức năng) do người có quyền quyết, căn cứ quy định hiện hành do người có chuyên môn xác nhận.

## IV. NGOẠI LỆ

Mỗi ngoại lệ ghi: luật / kiểm soát được miễn · phạm vi · lý do · rủi ro · biện pháp bù · người phụ trách · người duyệt · ngày bắt đầu · ngày hết hạn · cách theo dõi · gia hạn / đóng · bằng chứng.

Không có ngoại lệ vô thời hạn, không có ngoại lệ hồi tố để che việc đã xảy ra, không có ngoại lệ do chính bên xin tự duyệt.

*[A.I Generated — Claude Code — 30/10/2026]*
