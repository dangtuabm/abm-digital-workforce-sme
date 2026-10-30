# QUY TẮC KẾT NỐI HỆ THỐNG

**Mục lục**
- I. Sáu lớp thỏa thuận của một kết nối
- II. Bốn cách nối và khi nào dùng
- III. Chống ghi trùng, chạy lại và đối chiếu
- IV. Sáu nhóm rủi ro, sáu người rà, bảy cổng kiểm
- V. Trạng thái hồ sơ
- VI. Nguồn tham khảo

---

## I. SÁU LỚP THỎA THUẬN CỦA MỘT KẾT NỐI

| Lớp | Trả lời câu hỏi | Ví dụ |
|---|---|---|
| 1. Đối tượng và hệ thống gốc | Dữ liệu gì, hệ thống nào là nơi ghi nhận chuẩn | Khách hàng: CRM là gốc; hóa đơn: phần mềm kế toán là gốc |
| 2. Cách nối | Gọi trực tiếp, báo sự kiện, chạy lô hay file; phiên bản tài liệu | API phiên bản 2 của phần mềm bán hàng, tài liệu ngày 01/09/2026 |
| 3. Nghĩa dữ liệu | Trường nào ứng với trường nào, đơn vị, múi giờ, giá trị trống | "Ngày đơn" bên website theo giờ UTC, bên kho theo giờ Việt Nam |
| 4. Danh tính và quyền | Kết nối chạy bằng tài khoản nào, được đọc/ghi/xóa/gửi gì | Tài khoản "ket-noi-kho" chỉ được tạo phiếu xuất, không được xóa |
| 5. Giao nhận và nhất quán | Chống trùng, chạy lại, hàng chờ lỗi, xử lý ghi dở | Mỗi đơn có mã chống trùng = mã đơn website |
| 6. Vận hành và vòng đời | Chạy thử, bật, theo dõi, quay lui, thay khóa, ngừng | Thay khóa 90 ngày/lần [GIẢ ĐỊNH — người phụ trách chốt] |

Không lớp nào được "mặc định cho qua". Lớp nào chưa rõ → ghi vào Việc còn mở.

## II. BỐN CÁCH NỐI VÀ KHI NÀO DÙNG

| Cách nối | Hợp khi | Điểm yếu cần kiểm soát |
|---|---|---|
| Gọi trực tiếp (API) | Cần dữ liệu gần như ngay, khối lượng vừa | Giới hạn số lần gọi, lỗi mạng giữa chừng, nhà cung cấp đổi phiên bản |
| Báo sự kiện (webhook) | Bên nguồn chủ động báo khi có thay đổi | Báo trùng, báo sai thứ tự, mất báo khi bên nhận ngừng |
| Chạy theo lô (theo giờ, theo ngày) | Khối lượng lớn, chấp nhận độ trễ | Lô chạy dở, lô chạy hai lần, khó biết bản ghi nào lỗi |
| Xuất/nhập file | Phần mềm không có cách nối trực tiếp | Sai định dạng, sai mã hóa chữ tiếng Việt, người làm tay quên |

Ghi rõ lý do chọn và điều chấp nhận đánh đổi. Không gắn cứng một cách nối cho mọi trường hợp.

## III. CHỐNG GHI TRÙNG, CHẠY LẠI VÀ ĐỐI CHIẾU

1. **Mã theo dõi**: mỗi lần chạy có mã riêng để lần lại toàn bộ đường đi.
2. **Mã chống ghi trùng**: mỗi thao tác ghi gắn một mã duy nhất theo nghiệp vụ (ví dụ mã đơn). Bên nhận thấy mã đã có thì không tạo bản ghi mới.
3. **Không hứa "đúng một lần"** chỉ dựa vào phần mềm truyền dữ liệu. Ghi trung thực: "có thể nhận trùng, đã chặn bằng mã chống trùng và đối chiếu".
4. **Chạy lại có giới hạn**: số lần tối đa, giãn cách tăng dần; hết lượt → vào hàng chờ lỗi, báo người phụ trách; không chạy lại vô hạn.
5. **Sai thứ tự, đến muộn**: quy định bản nào thắng (theo thời điểm thay đổi ở hệ thống gốc, không theo thời điểm nhận).
6. **Ghi dở dang**: xác định "một đơn vị việc" (ví dụ đơn + các dòng hàng). Dở dang thì có cách bù trừ đã được duyệt, không tự xóa.
7. **Chuỗi bằng chứng cho mỗi lần ghi**: trước khi ghi → lệnh ghi → phản hồi của phần mềm → trạng thái sau khi ghi → kiểm trên hệ thống gốc → quyết định của người (nếu cần).
8. **Trạng thái giao nhận**: "ĐÃ BÁO NHẬN" khi phần mềm trả lời thành công; chỉ chuyển "ĐÃ XONG NGHIỆP VỤ" khi kiểm trên hệ thống gốc khớp.
9. **Đối chiếu định kỳ**: so số bản ghi, tổng tiền, bản ghi lỗi giữa hai bên theo ngày; mọi chênh lệch phải giải thích được.

## IV. SÁU NHÓM RỦI RO, SÁU NGƯỜI RÀ, BẢY CỔNG KIỂM

**Sáu nhóm rủi ro**
1. Phạm vi nghiệp vụ và quyền sở hữu hệ thống.
2. Nghĩa dữ liệu, nguồn gốc dữ liệu, chất lượng.
3. Danh tính, quyền, khóa kết nối.
4. Giao nhận, chạy lại, nhất quán.
5. An toàn thông tin, dữ liệu cá nhân, tuân thủ.
6. Chuyển đổi, vận hành, vòng đời kết nối.

**Sáu người rà** (doanh nghiệp nhỏ có thể kiêm, trừ việc người làm kết nối tự duyệt bật)
1. Chủ quy trình nghiệp vụ.
2. Người phụ trách dữ liệu của từng hệ thống.
3. Người phụ trách tài khoản và an toàn thông tin.
4. Người làm kỹ thuật kết nối.
5. Người vận hành, hỗ trợ.
6. Người phụ trách rủi ro và kiểm soát thay đổi (thường là lãnh đạo bộ phận hoặc giám đốc).

**Bảy cổng kiểm**: (1) mục đích và hệ thống gốc · (2) thỏa thuận kết nối và nghĩa dữ liệu · (3) danh tính và quyền · (4) giao nhận và nhất quán · (5) an toàn và nhật ký · (6) kiểm thử và đối chiếu · (7) chuyển đổi và vòng đời.

## V. TRẠNG THÁI HỒ SƠ

ĐÃ THIẾT KẾ → ĐÃ RÀ THỎA THUẬN → ĐÃ THỬ Ở MÔI TRƯỜNG THỬ → ĐÃ RÀ KIỂM SOÁT → DUYỆT CHẠY THỬ NHỎ → CHỜ CHUYỂN ĐỔI → SẴN SÀNG CHỜ DUYỆT.

Các trạng thái ĐÃ KẾT NỐI / ĐÃ BẬT / ĐÃ CHUYỂN DỮ LIỆU chỉ ghi khi có bằng chứng do người có quyền thực hiện.

## VI. NGUỒN THAM KHẢO (kiểm tra ngày 22/08/2026)

- OpenAPI Specification 3.1.1 — cách mô tả một API; tài liệu của nhà cung cấp vẫn là chuẩn.
- CloudEvents 1.0.2 — quy ước mô tả sự kiện; không bảo đảm việc giao nhận.
- IETF RFC 9700 — thực hành an toàn cho OAuth 2.0.
- NIST SP 800-207 — nguyên lý "không tin mặc định" (zero trust); cần điều chỉnh theo doanh nghiệp.

Các nguồn trên là tham khảo, không thay tài liệu nhà cung cấp, kiểm thử thật hay quyết định của người có quyền.

*[A.I Generated — Claude Code — 30/10/2026]*
