# QUY TẮC QUẢN LÝ PHIÊN BẢN

**Mục lục**
- I. Mã định danh và nơi lưu bản chuẩn
- II. Gợi ý đặt tên và đánh số phiên bản
- III. Trạng thái và đánh giá ảnh hưởng
- IV. Kiểm bản ứng viên và khôi phục
- V. Mười quy tắc bắt buộc
- VI. Ví dụ đối chiếu

---

## I. MÃ ĐỊNH DANH VÀ NƠI LƯU BẢN CHUẨN

- Mỗi tài liệu có **một mã định danh** không đổi suốt vòng đời (ví dụ `QT-KHO-003` = quy trình kho số 3). Đổi tên file không đổi mã.
- Mỗi tài liệu có **một nơi lưu bản chuẩn** (một thư mục hoặc phần mềm). Bản gửi qua email, Zalo, tải về máy chỉ là bản sao, phải trỏ về mã.
- Bản sao, bản đổi tên, bản "final", "moi", "sua" được gom về cùng mã trong sổ đăng ký.

## II. GỢI Ý ĐẶT TÊN VÀ ĐÁNH SỐ PHIÊN BẢN

Doanh nghiệp tự chốt; dưới đây là gợi ý [GIẢ ĐỊNH, chờ duyệt]:

**Tên file:** `[Mã] - [Tên nội dung] - v[X.Y] - [YYYYMMDD]`
Ví dụ: `QT-KHO-003 - Quy trinh xuat kho - v2.1 - 20261030`

**Đánh số theo loại tài liệu:**
| Loại | Tăng số đầu (X) khi | Tăng số sau (Y) khi |
|---|---|---|
| Quy định, quy trình, mẫu biểu | Đổi cấu trúc, đổi định hướng, đổi trách nhiệm | Sửa câu chữ, sửa lỗi nhỏ, cập nhật số liệu không đổi ý nghĩa |
| Bảng dữ liệu, bảng giá | Đổi cột, đổi cách tính, đổi đơn vị | Cập nhật giá trị theo cấu trúc cũ |
| Câu lệnh A.I, cấu hình | Đổi nhiệm vụ, đổi đầu ra, đổi quyền | Sửa diễn đạt, thêm ví dụ |

Bản nháp có thể thêm hậu tố `-nhap`. Không đánh số kiểu "final", "final2", "moi nhat".

Phần mềm có cơ chế đánh số riêng (ví dụ quản lý mã nguồn) thì theo phần mềm, nhưng sổ đăng ký vẫn ghi mã và trạng thái.

## III. TRẠNG THÁI VÀ ĐÁNH GIÁ ẢNH HƯỞNG

**Trạng thái** (chỉ ghi khi có bằng chứng):
PHÁT HIỆN → ĐÃ ĐĂNG KÝ → BẢN NHÁP → ĐANG XEM XÉT → ĐÃ DUYỆT → BẢN ỨNG VIÊN PHÁT HÀNH → ĐÃ PHÁT HÀNH / ĐANG HIỆU LỰC. Các trạng thái BỊ THAY THẾ · NGỪNG DÙNG · ĐÃ LƯU TRỮ · ĐÃ HỦY · ĐÃ KHÔI PHỤC cần bản ghi của người có quyền.

**Đánh giá ảnh hưởng** — trả lời từng câu:
1. Ai, phòng nào đang dùng bản hiện tại?
2. File nào đang liên kết tới nó (bảng tính lấy số, mẫu in, báo cáo)?
3. Quy trình hay phần mềm nào dựa vào nó (tự động hóa, công cụ A.I đọc kho)?
4. Có cần chuyển dữ liệu, đào tạo lại, thông báo khách hàng, đối tác?
5. Có chạm dữ liệu nhạy cảm, quyền xem, quy định lưu giữ?
6. Còn điều gì chưa biết? (ghi rõ, không bỏ trống)

## IV. KIỂM BẢN ỨNG VIÊN VÀ KHÔI PHỤC

**Kiểm bản ứng viên:**
- Mã không trùng; số phiên bản đúng quy tắc; trỏ đúng bản trước.
- Dấu kiểm nội dung (nếu công cụ hỗ trợ, ví dụ SHA-256) được ghi; bản người duyệt xem trùng dấu kiểm với bản sẽ phát hành.
- So sánh trước – sau đầy đủ, không bỏ sót đoạn sửa.
- Liên kết, dẫn chiếu không gãy; quyền xem và phân loại đúng.
- Đã thử khôi phục về bản trước (với tài liệu quan trọng).

**Khôi phục là một thay đổi có kiểm soát:**
| Cần có | Ý nghĩa |
|---|---|
| Điều kiện kích hoạt | Lỗi gì thì quay lại |
| Người có quyền | Ai được quyết khôi phục |
| Bản đích | Bản nào, mã, dấu kiểm |
| Bản sao lưu | Bản sao của hiện trạng trước khi khôi phục |
| Các bước | Thứ tự làm, nơi cập nhật |
| Kiểm sau khôi phục | Người dùng, file liên kết, hệ thống chạy lại đúng chưa |
| Ghi sự cố | Nguyên nhân, bản mới thay thế dự kiến |

Khôi phục không xóa lịch sử; bản lỗi vẫn giữ trong sổ với trạng thái phù hợp.

## V. MƯỜI QUY TẮC BẮT BUỘC

1. Một tài liệu – một mã – một nơi lưu bản chuẩn.
2. "Mới nhất", "vừa sửa", "vừa gửi" không đồng nghĩa "hiệu lực".
3. Bản đã phát hành không sửa tại chỗ.
4. Dấu kiểm chứng minh nội dung giống nhau; bằng chứng duyệt chứng minh thẩm quyền — cần cả hai.
5. Quy tắc đánh số khai báo theo loại tài liệu.
6. Mọi thay đổi nối: nguồn → phiếu → so sánh → ảnh hưởng → kiểm → duyệt → phát hành → nhật ký.
7. Duyệt chỉ có giá trị cho đúng bản đã xem.
8. Khôi phục có bản đích, sao lưu, người có quyền, cách kiểm.
9. Lưu trữ, hủy theo quy định giữ tài liệu và người phụ trách; không tự động.
10. Nhật ký chỉ ghi thêm, không sửa: thời điểm · người làm · việc · tài liệu · trước · sau · kết quả.

## VI. VÍ DỤ ĐỐI CHIẾU

**Sai:** "Trên Drive có `Bang gia 2027_final` (sửa 28/10) và `Bang gia 2027` (sửa 15/10). Bản hiệu lực là bản sửa 28/10."
**Đúng:** "Hai bản cùng mã BG-2027. Bản 15/10 có email duyệt của giám đốc kinh doanh ngày 16/10; bản 28/10 chưa có bằng chứng duyệt, khác bản 15/10 ở 3 dòng chiết khấu đại lý cấp 2. Đề xuất: bản 15/10 đang hiệu lực, bản 28/10 là bản nháp — chờ giám đốc kinh doanh chốt."

*[A.I Generated — Claude Code — 30/10/2026]*
