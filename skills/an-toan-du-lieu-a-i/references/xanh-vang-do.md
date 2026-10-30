# XANH – VÀNG – ĐỎ: PHÂN LOẠI, GẮN NHÃN, CHE DỮ LIỆU

## 1. Ba nhãn và cách xử lý

| Nhãn | Là gì | Ví dụ ở doanh nghiệp vừa và nhỏ | Khi dùng A.I |
|---|---|---|---|
| **Xanh** | Thông tin đã công khai hoặc lộ ra cũng không gây thiệt hại | Bài đăng fanpage, catalogue đã phát, bảng giá niêm yết, quy trình chung không có tên người, tài liệu đào tạo phổ thông | Dùng thoải mái |
| **Vàng** | Thông tin nội bộ, lộ ra gây phiền hoặc thiệt hại vừa | Danh sách khách có tên và số điện thoại, báo giá riêng cho một khách, doanh số theo cửa hàng, biên bản họp, hợp đồng mẫu đã điền tên | Che tên, số điện thoại, số tiền, mã khách; **hoặc** chỉ dùng tài khoản A.I của công ty đã được duyệt |
| **Đỏ** | Thông tin mà lộ ra gây thiệt hại lớn, vi phạm cam kết hoặc quy định | Bảng lương, số tài khoản và sao kê ngân hàng, CCCD và hồ sơ nhân sự, mật khẩu, mã API, hồ sơ sức khỏe, công thức sản xuất bí mật, giá vốn và chiết khấu đại lý chưa công bố, hồ sơ tranh chấp | **Không đưa lên A.I.** Dừng lại hỏi người phụ trách |

Ba quy tắc phụ:
- **Trộn thì lấy mức cao nhất.** File có một cột Đỏ là file Đỏ, kể cả 20 cột còn lại là Xanh. Cách gỡ: tách cột Đỏ ra trước, phần còn lại xét lại nhãn.
- **Chưa rõ thì coi là Đỏ** cho tới khi người phụ trách thư mục gắn nhãn.
- **Công khai chưa chắc an toàn.** Gom nhiều thông tin công khai về một người (tên, nơi làm, số điện thoại trên mạng) thành hồ sơ là việc không được làm.

## 2. Gắn nhãn một lần cho từng thư mục

Không bắt người dùng tự phân loại từng file. Người phụ trách mỗi thư mục gắn nhãn **một lần** vào `templates/bang-nhan-thu-muc.csv`. A.I nhìn file nằm ở đâu là biết loại dữ liệu.

Cách làm cho doanh nghiệp mới bắt đầu:
1. Liệt kê thư mục cấp 1–2 trên Google Drive/OneDrive hoặc máy chủ chung.
2. Người phụ trách từng thư mục chọn nhãn mặc định. Thư mục con khác nhãn thì ghi riêng.
3. Thư mục Đỏ ghi rõ người được hỏi khi cần dùng.
4. Rà lại khi lập thư mục mới hoặc 6 tháng một lần.

Gợi ý mặc định thường gặp: Marketing → Xanh; Kinh doanh, Chăm sóc khách hàng, Vận hành → Vàng; Kế toán, Nhân sự, Pháp chế, Ban giám đốc → Đỏ. Doanh nghiệp tự quyết, đây chỉ là điểm xuất phát.

## 3. Bỏ trước, che sau

**Bước 1 — Bỏ.** Hỏi: việc này cần cột nào? Ví dụ nhờ A.I phân tích lý do khách hủy đơn thì chỉ cần cột "lý do hủy" và "ngày", không cần tên khách, số điện thoại, địa chỉ.

**Bước 2 — Gộp.** Thay số chi tiết bằng nhóm khi đủ dùng: "đơn 1–5 triệu" thay cho "3.450.000 đ"; "Quận 7" thay cho số nhà.

**Bước 3 — Che.** Thay thông tin nhận diện bằng mã:

| Loại | Trước | Sau |
|---|---|---|
| Tên người | Nguyễn Văn An | KH01 |
| Số điện thoại | 0912 345 678 | [SĐT] |
| Số tiền | 125.000.000 đ | [SỐ TIỀN] hoặc nhóm "100–200 triệu" |
| Tên công ty đối tác | Công ty TNHH Minh Phát | ĐT03 |
| Email | an.nguyen@... | [EMAIL] |

Bảng đối chiếu (KH01 = ai) giữ ở máy hoặc thư mục công ty, **không** đưa lên A.I.

**Rủi ro còn lại phải ghi:** đã che nhưng ghép nhiều cột vẫn có thể nhận ra người (ví dụ "nữ, kế toán trưởng, chi nhánh Đà Nẵng" ở công ty 30 người). Che không có nghĩa là ẩn danh hoàn toàn.

## 4. Câu hỏi soát công cụ A.I và kết nối mới

1. Đang dùng **tài khoản cá nhân** (miễn phí hoặc tự trả tiền) hay **tài khoản công ty** do người quản trị cấp?
2. Trang chính thức của nhà cung cấp nói gì về: có dùng dữ liệu để huấn luyện mô hình không, lưu lịch sử bao lâu, tắt được không? Ghi đường dẫn và **ngày đọc**. Không dựa vào trí nhớ hoặc bài viết trên mạng.
3. Công cụ xin quyền gì (đọc toàn bộ hộp thư, toàn bộ Drive, gửi thay, xóa)? Quyền đó có vượt việc cần làm không? Chỉ cấp quyền nhỏ nhất đủ dùng.
4. Ai là người quản trị, ai thu hồi được quyền khi nhân viên nghỉ?
5. Tiện ích, phần mềm cài thêm có nguồn rõ ràng không (chợ ứng dụng chính thức, nhà phát triển có tên)?
6. Dữ liệu đi qua bên thứ ba nào khác (dịch vụ trung gian kết nối)?

Có điểm CHƯA RÕ ở câu 1–3 → kết luận CHƯA DÙNG, chờ người quản trị.

## 5. Kiểm đầu ra của A.I trước khi dùng hoặc chia sẻ

- Đầu ra có làm lộ lại thông tin đã che không (A.I tự "đoán" tên thật)?
- Có số liệu, tên người, điều khoản A.I tự bịa không? Đối chiếu nguồn gốc.
- Có link lạ, đoạn mã lạ chèn vào không?
- Người nhận đầu ra có được xem loại dữ liệu này không? Gửi qua kênh nào, link có hạn dùng không?
- Đầu ra dùng để quyết định việc lớn (tuyển, cho thôi việc, cho vay, giá) → phải có người có chuyên môn duyệt.

*[A.I Generated — Claude Code — 30/10/2026]*
