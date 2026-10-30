# QUY TẮC KIỂM, DẤU VẾT VÀ ĐỐI SOÁT

## 1. Kiểm nhãn Xanh – Vàng – Đỏ trước khi bóc

Nhãn gắn **một lần cho từng thư mục**; nhìn chứng từ nằm ở thư mục nào là biết loại dữ liệu.

| Nhãn | Ví dụ chứng từ | Cách làm |
|---|---|---|
| **Xanh** | Báo giá công khai, phiếu nhập kho không có thông tin cá nhân, đơn hàng đã che thông tin khách | Dùng thoải mái trong công cụ A.I được doanh nghiệp cho phép |
| **Vàng** | Hóa đơn mua vào, đơn hàng có tên và số điện thoại khách, phiếu chi | Che tên, số điện thoại, số tài khoản khi không cần cho bộ trường; chỉ dùng tài khoản công ty |
| **Đỏ** | Bảng lương, số tài khoản ngân hàng nhân viên, CCCD, hồ sơ thuế chi tiết, hồ sơ sức khỏe | Không đưa lên A.I; dừng lại, hỏi người phụ trách. Chỉ làm khi đã có duyệt bằng văn bản và công cụ được phép |

Thư mục chưa gắn nhãn mà chứng từ có dấu hiệu Đỏ: coi là Đỏ cho tới khi được xác nhận.

## 2. Bốn lớp kiểm

| Lớp | Kiểm gì | Bằng chứng |
|---|---|---|
| Phủ đủ | Mọi chứng từ, trang, bảng trong phạm vi có trạng thái | Danh mục chứng từ nguồn và số lượng |
| Cấu trúc | Tên cột, kiểu, ô bắt buộc, danh mục, định dạng, mã không trùng | Báo cáo của `kiem_file_trich_xuat.py` |
| Giá trị | Gốc ↔ chuẩn, chữ scan mờ, tổng ↔ chi tiết, khoảng hợp lệ | Trạng thái từng dòng và Sổ ngoại lệ |
| Đối soát | Nguồn = đã bóc + ngoại lệ + loại, tính theo "một dòng là gì" | Bảng đối soát |

## 3. Dấu vết tối thiểu của mỗi dòng

- mã dòng, phiên bản hợp đồng trích xuất;
- mã nguồn, tên/phiên bản file;
- trang/vùng/bảng/dòng/ô;
- cách đọc và thời điểm;
- giá trị gốc và giá trị chuẩn cho trường đã đổi;
- trạng thái và mã ngoại lệ nếu có;
- người sửa và người duyệt cho giá trị đã sửa tay.

## 4. Công thức đối soát

Chọn theo "một dòng là gì" và ghi rõ mẫu số. Ví dụ:
- `số chứng từ trong phạm vi = đã xử lý + không đọc được + ngoài phạm vi`
- `số dòng dự kiến = dòng đạt + dòng ngoại lệ + dòng loại`
- `số hóa đơn = hóa đơn có dòng hàng + hóa đơn hợp lệ không có dòng hàng`
- `cộng tiền các dòng hàng (trước thuế) = tiền trước thuế in trên hóa đơn` (khi chứng từ có)

Không ghi phần trăm trơn; luôn ghi tử số/mẫu số, ví dụ "98/100 chứng từ đã xử lý".

## 5. Lấy mẫu

Lấy mẫu không thay được phủ đủ. Khi lô lớn:
1. Soát 100% ngoại lệ và trường tác động cao (số tiền, mã số thuế, số tài khoản).
2. Lấy mẫu đại diện theo loại chứng từ, mẫu trình bày, chất lượng ảnh — không chỉ ngẫu nhiên cả lô.
3. Ghi cỡ mẫu, mẫu số, cách lấy và loại lỗi.
4. Thấy lỗi có hệ thống: dừng lô, sửa quy tắc, chạy lại phần bị ảnh hưởng.

## 6. Vòng đời ngoại lệ

Trạng thái: MỞ → ĐÃ GIAO → ĐÃ XỬ LÝ, hoặc CHẤP NHẬN RỦI RO, hoặc LOẠI CHỨNG TỪ.

Mỗi ngoại lệ ghi: giá trị gốc, vị trí, loại lỗi, ảnh hưởng, người xử lý, quyết định, giá trị sau xử lý, căn cứ. Không đóng ngoại lệ bằng cách xóa dòng.

## 7. Cổng lô

- **LÀM TIẾP**: lô thử đạt bộ trường, dấu vết, luồng ngoại lệ và tiêu chí đã chốt.
- **SỬA**: lỗi cục bộ, sửa quy tắc/ánh xạ rồi chạy lại.
- **DỪNG**: "một dòng là gì" hoặc bộ trường sai, chứng từ không đủ, lỗi đọc có hệ thống, hoặc dữ liệu Đỏ chưa được duyệt.

*[A.I Generated — Claude Code — 30/10/2026]*
