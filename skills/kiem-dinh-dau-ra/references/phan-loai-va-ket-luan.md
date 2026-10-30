# PHÂN LOẠI PHÁT HIỆN VÀ KẾT LUẬN

## 1. Luật độc lập và chọn chế độ

| Tình huống | Chế độ | Người chạy |
|---|---|---|
| Người/Nhân sự số đang chạy đã làm phần chính của đầu ra và được yêu cầu "phản biện" | Không chạy — kết luận **CHUYỂN NGƯỜI** | Người hoặc Nhân sự số khác |
| Đầu ra chạm tiền, pháp lý, khách hàng thật, dữ liệu thật, đi ra ngoài, khó hoàn tác | Chỉ tìm lỗi → Chốt bản cuối | Hai người/Nhân sự số khác nhau |
| Đầu ra nội bộ, dễ hoàn tác, không ra ngoài | Chốt bản cuối luôn | Nên khác người làm; trùng người vẫn được |

Người chốt bản cuối trùng người làm chỉ chấp nhận với đầu ra nội bộ, dễ hoàn tác. Đầu ra rủi ro cao mà trùng người → **CHUYỂN NGƯỜI**.

## 2. Ba loại phát hiện (dùng ở cả hai chế độ)

| Loại | Nghĩa |
|---|---|
| **CHẶN** | Phải xử lý trước khi dùng hoặc phát hành. Một lỗi CHẶN là đủ, không bù trừ bằng điểm trung bình |
| **NÊN SỬA** | Có giá trị đáng kể nhưng không chặn |
| **GHI NHẬN** | Không xử lý lượt này, đáng lưu ý về sau |

Với đầu ra ra ngoài, mức nặng tương ứng: CHẶN = có thể gây sai sự thật, vi phạm pháp luật, lộ dữ liệu, thiếu quyền dùng, chỉ dẫn không an toàn, nhầm bản, hoặc không có đường thu hồi khi gây hại lớn; lỗi làm người đọc hiểu sai đáng kể hoặc phá vỡ quy chuẩn bắt buộc cũng xếp CHẶN. NÊN SỬA = lỗi cục bộ không đổi nghĩa, quyền, an toàn.

## 3. Năm ca chặn tức thì

Gặp một ca: dừng đánh giá ngay, kết luận KHÔNG ĐẠT (hoặc CHƯA ĐẠT) kèm nhãn **CHẶN TỨC THÌ**, ghi Sổ lỗi bị chặn.

1. **Số liệu sai sự thật kiểm chứng được** — ví dụ "đứng số 1 thị trường" trong khi số liệu ngành không ủng hộ.
2. **Cam kết tuyệt đối, hứa quá** — ví dụ "cam kết tăng doanh thu 100% trong 3 tháng".
3. **Gây hiểu nhầm pháp lý hoặc rủi ro tài chính lớn** — ví dụ điều khoản phạt sai luật, đề xuất đầu tư lớn không có thử nghiệm.
4. **Sao chép không nguồn, không có quyền dùng** — ví dụ biểu đồ của tổ chức khác không ghi nguồn, ảnh lấy trên mạng.
5. **Lộ dữ liệu cá nhân hoặc bí mật kinh doanh** — ví dụ ảnh chụp màn hình còn tên, số điện thoại khách hàng.

Doanh nghiệp có thể bổ sung ca chặn riêng trong quy chuẩn của mình.

## 4. Bộ kết luận

### Chế độ Chỉ tìm lỗi

| Kết luận | Khi nào |
|---|---|
| **ĐẠT** | Không còn phát hiện CHẶN. Dùng được, không cần vòng 2 |
| **ĐẠT CÓ ĐIỀU KIỆN** | Hết CHẶN, còn NÊN SỬA đáng kể. Người làm sửa và xác nhận là xong |
| **KHÔNG ĐẠT** | Còn ít nhất một CHẶN. Làm lại, kiểm vòng 2. Thêm nhãn CHẶN TỨC THÌ nếu trúng mục 3 |
| **CHUYỂN NGƯỜI** | Phạm luật độc lập, hoặc cần người quyết ngoại lệ, mục tiêu, Ranh giới Đỏ |

### Chế độ Chốt bản cuối

| Kết luận | Khi nào |
|---|---|
| **ĐẠT BẢN CUỐI** | Mọi tiêu chí đạt sau khi sửa |
| **CÒN LỖI NHỎ** | Chỉ còn NÊN SỬA, đã có người sửa và hạn |
| **CHƯA ĐẠT** | Còn ít nhất một CHẶN không tự xử lý được trong phạm vi |
| **CHUYỂN NGƯỜI** | Như trên |

Bảng đối chiếu tiêu chí là bắt buộc; không có thì không được kết luận ĐẠT BẢN CUỐI.

### Trạng thái phát hành (đầu ra đi ra ngoài)

| Trạng thái | Điều kiện | Việc của người |
|---|---|---|
| **CHƯA SẴN SÀNG** | Còn CHẶN, nhầm bản, quyền dùng chưa rõ, nhận định sai | Bổ sung hoặc sửa |
| **CHỜ SỬA LỖI NHỎ** | Chỉ còn NÊN SỬA có người sửa và cách kiểm lại | Sửa hoặc chấp nhận rủi ro có thời hạn |
| **CHỜ NGƯỜI DUYỆT PHÁT HÀNH** | 10 lớp sạch, các vòng duyệt trước đạt, chỉ còn duyệt cuối | Người có quyền quyết định |
| **ĐỦ ĐIỀU KIỆN PHÁT HÀNH** | Mọi vòng duyệt bắt buộc đã đạt, có bằng chứng | Người có quyền tự gửi, đăng |

Không nhảy từ còn lỗi sang phát hành. Bản bị sửa dù một con số sau khi duyệt → kết quả cũ hết hiệu lực, kiểm lại.

## 5. Sổ lỗi bị chặn

Mỗi lần KHÔNG ĐẠT hoặc CHƯA ĐẠT ghi một dòng vào `templates/so-loi-bi-chan.csv`. Định kỳ (doanh nghiệp tự đặt, gợi ý 6 tháng) rà: lỗi nào lặp; đầu ra loại nào hay bị chặn; thiếu hướng dẫn, thiếu đào tạo hay quy trình duyệt chưa chặt; đề xuất sửa hướng dẫn của việc liên quan.

*[A.I Generated — Claude Code — 30/10/2026]*
