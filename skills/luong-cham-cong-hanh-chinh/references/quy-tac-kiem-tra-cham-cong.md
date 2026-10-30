# QUY TẮC KIỂM TRA CHẤM CÔNG

**Mục lục:** 1. Chuẩn hóa dữ liệu · 2. Chín loại sai lệch · 3. Tham số doanh nghiệp tự đặt · 4. Bảng tổng hợp công nháp · 5. Ví dụ

## 1. Chuẩn hóa dữ liệu (Bước 3)

- Mỗi dòng: mã nhân viên · ngày · giờ chấm (có thể nhiều lần/ngày) · máy/điểm chấm.
- Gom các lần chấm trong ngày: lần sớm nhất là giờ vào, lần muộn nhất là giờ ra (trừ ca qua đêm — ghép theo ca, không theo ngày lịch).
- Ghép mỗi nhân viên – ngày với: ca được xếp, đơn nghỉ đã duyệt, đơn tăng ca đã duyệt, lịch công tác, ngày lễ/ngày nghỉ của doanh nghiệp.
- Kiểm danh sách: ai có trong máy mà không có trong danh sách đang làm (người đã nghỉ vẫn chấm, mã sai) và ngược lại (người mới chưa đăng ký vân tay).

## 2. Chín loại sai lệch (Bước 4)

| Loại | Điều kiện phát hiện | Việc cần xác nhận |
|---|---|---|
| Quên chấm vào/ra | Có ca, chỉ có một lần chấm trong ngày | Quản lý bộ phận xác nhận giờ thực tế |
| Đi muộn / về sớm | Giờ vào sau giờ bắt đầu ca + mức cho phép; giờ ra trước giờ kết thúc ca | Có lý do được duyệt không |
| Thiếu giờ | Tổng giờ làm < giờ chuẩn của ca sau khi trừ nghỉ giữa ca | Theo quy chế |
| Tăng ca không có đơn | Giờ ra vượt giờ kết thúc ca quá mức tối thiểu tính tăng ca, không có đơn tăng ca | Có tính tăng ca không |
| Có đơn tăng ca nhưng không có giờ chấm tương ứng | Đơn duyệt tăng ca, giờ ra không vượt ca | Đơn có hiệu lực không |
| Vắng không có đơn | Có ca, không có lần chấm, không có đơn nghỉ hay lịch công tác | Nghỉ có phép, không phép hay công tác |
| Chấm công ngày nghỉ | Có lần chấm vào ngày lễ/ngày nghỉ, không có đơn làm thêm | Có tính công không |
| Chấm trùng | Hai bản ghi giống hệt (cùng mã, cùng giây) | Thường là lỗi máy, gộp sau khi người phụ trách đồng ý |
| Nghi chấm hộ | Nhiều mã chấm cách nhau vài giây trên cùng máy ở giờ không cao điểm, lặp nhiều ngày | Chỉ báo riêng người phụ trách, không kết luận |

Một dòng có thể có nhiều loại sai lệch; ghi từng loại.

## 3. Tham số doanh nghiệp tự đặt (lấy từ quy chế, không tự đặt)

| Tham số | Ví dụ cách ghi trong quy chế |
|---|---|
| Mức đi muộn cho phép | [... phút] |
| Mức tối thiểu tính tăng ca | [... phút sau giờ kết thúc ca] |
| Nghỉ giữa ca có trừ giờ không | [có/không, ... phút] |
| Cách tính ngày công nửa ngày | [...] |
| Ca qua đêm ghép về ngày nào | [ngày bắt đầu ca / ngày kết thúc ca] |
| Hệ số tăng ca ngày thường, ngày nghỉ, ngày lễ | [theo quy chế; đối chiếu văn bản pháp luật hiện hành, cần người có chuyên môn xác nhận] |

Chưa có quy chế cho tham số nào: hỏi; nếu người giao bảo "cứ làm", dùng giá trị người giao nói và gắn [GIẢ ĐỊNH].

## 4. Bảng tổng hợp công nháp

Cột: mã nhân viên · số ngày công thực tế · số ngày nghỉ có lương theo loại · số ngày nghỉ không lương · số giờ tăng ca theo loại ngày · số lần đi muộn/về sớm · số sai lệch chờ xác nhận. **Không có cột tiền.** Trạng thái: CHỜ NGƯỜI PHỤ TRÁCH DUYỆT. Dòng còn sai lệch chờ xác nhận gắn cờ.

## 5. Ví dụ (xưởng may 120 công nhân, 2 ca, tháng 10)

- 7 trường hợp quên chấm ra ca chiều ngày 15/10 trên cùng một máy → nghi máy lỗi sau 17h; đề xuất người phụ trách hỏi tổ trưởng xác nhận cả nhóm.
- Mã NV-0412 vắng 3 ngày liền, không có đơn → "Vắng không có đơn", chờ quản lý chuyền xác nhận.
- 14 người có giờ ra 19h30 ngày 22/10, có đơn tăng ca của chuyền 3 → khớp, không phải sai lệch.

*[A.I Generated — Claude Code — 30/10/2026]*
