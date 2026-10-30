# CHẾ ĐỘ ĐA NGÔN NGỮ — DỊCH VÀ BẢN ĐỊA HÓA

**Mục lục**
- 1. Ngôn ngữ đích không chỉ là ngôn ngữ
- 2. Ba mức tự do dịch
- 3. Bảng thuật ngữ
- 4. Quy đổi ngày, số, tiền, đơn vị, tên riêng
- 5. Nội dung khóa (biến, thẻ, mã)
- 6. Kiểm tra và mức lỗi
- 7. Đối soát và cổng phát hành

---

## 1. Ngôn ngữ đích không chỉ là ngôn ngữ

Ghi mã ngôn ngữ – chữ viết – thị trường khi cần: `vi-VN`, `en-US`, `en-GB`, `zh-Hans-CN` (giản thể), `zh-Hant-TW` (phồn thể), `ja-JP`, `ko-KR`. Cùng tiếng Anh nhưng Mỹ và Anh khác chính tả, ngày tháng, đơn vị. Cùng tiếng Trung nhưng giản thể và phồn thể là hai bản khác nhau.

Thỏa thuận dịch ghi: bản gốc và phiên bản · ngôn ngữ nguồn/đích · người đọc · mục đích và kênh (giao diện app, tài liệu đào tạo, catalogue, website, bài quảng bá) · mức tự do · bảng thuật ngữ và từ không dịch · giọng văn, cách xưng hô · định dạng, giới hạn ký tự · người kiểm ngôn ngữ, người kiểm nghiệp vụ · điều kiện phát hành.

## 2. Ba mức tự do dịch

| Mức | Dùng cho | Quy tắc |
|---|---|---|
| **Sát nghĩa** | Điều khoản, kỹ thuật, an toàn, giá | Giữ nghĩa và cấu trúc gần bản gốc |
| **Tự nhiên** | Giao diện, tài liệu hướng dẫn, website | Ưu tiên câu tự nhiên, trong cùng nghĩa và mục đích |
| **Sáng tạo lại** | Khẩu hiệu, bài quảng bá | Đổi cách biểu đạt theo đề bài sáng tạo; không đổi sự thật, ưu đãi, ranh giới pháp lý |

Không "hay hóa" bằng cách thêm lợi ích hay số liệu. Không dịch từng chữ làm sai ý.

## 3. Bảng thuật ngữ

Mỗi thuật ngữ: từ gốc · từ đích · trạng thái **ĐÃ DUYỆT / NÊN DÙNG / CẤM DÙNG / ỨNG VIÊN** · lĩnh vực · ví dụ · người duyệt · phiên bản. Từ ỨNG VIÊN không được dùng như đã duyệt trong đoạn rủi ro cao. Tên sản phẩm, tên thương hiệu, tên phương pháp riêng: giữ theo quy định của doanh nghiệp.

## 4. Quy đổi ngày, số, tiền, đơn vị, tên riêng

- **Ngày giờ:** giữ giá trị gốc; chỉ đổi định dạng khi biết chắc định dạng gốc và múi giờ. "03/04/2026" chưa rõ là 3 tháng 4 hay 4 tháng 3 → đưa vào danh sách điểm mơ hồ.
- **Tiền:** đổi ký hiệu và cách viết theo thị trường (1,250.50 USD ở Mỹ; 1.250,50 ở Việt Nam). **Chỉ quy đổi giá trị** khi thỏa thuận có tỷ giá, nguồn tỷ giá, ngày và cách làm tròn. Không dùng tỷ giá tự nhớ.
- **Số:** giữ độ lớn, dấu, mẫu số, độ chính xác; cảnh giác dấu phẩy và dấu chấm.
- **Đơn vị:** chỉ đổi khi thỏa thuận yêu cầu; ghi cả hai nếu cần.
- **Tên người, địa chỉ, số điện thoại:** theo quy tắc của thỏa thuận; không dịch tên riêng tùy ý.
- **Ví dụ, hình ảnh văn hóa:** chỉ thay khi đề bài cho phép và người kiểm đồng ý nghĩa tương đương.

## 5. Nội dung khóa (biến, thẻ, mã)

Phải giữ nguyên số lượng và hình dạng: biến `{name}`, `{{ten_khach}}`, `${file}`, `%s`, `%1$d`; thẻ HTML `<b>…</b>`; khóa dịch của app; mã code; đường dẫn file; đích của liên kết Markdown. Được dịch chữ hiển thị của liên kết, không tự đổi địa chỉ.

Kiểm máy bằng `scripts/kiem-so-doan-song-ngu.py`: trùng mã đoạn, đoạn đích rỗng, thiếu/thừa biến và thẻ, vượt giới hạn ký tự.

## 6. Kiểm tra và mức lỗi

| Nhóm lỗi | Ví dụ | Chặn phát hành? |
|---|---|---|
| Chính xác | Sai nghĩa, thiếu ý, thêm ý, sai số, sai nhận định | Có |
| Thuật ngữ | Dùng từ cấm, sai từ đã duyệt, dịch từ không được dịch | Có với từ quan trọng |
| Thị trường | Sai định dạng ngày, số, tiền, xưng hô | Tùy mức ảnh hưởng |
| Chức năng | Mất biến, mất thẻ, mất liên kết, đoạn rỗng | Có |
| Văn phong | Ngữ pháp, độ tự nhiên, giọng, nhất quán | Tùy kênh |
| Hiển thị | Tràn chữ, cắt chữ, xuống dòng sai, lỗi phông | Có nếu mất nghĩa hoặc mất chức năng |
| Tuân thủ | Cảnh báo an toàn, điều khoản sai hoặc thiếu | Có; cần người có chuyên môn |

Thứ tự kiểm: kiểm máy → kiểm song ngữ theo ngữ cảnh (đọc cả gốc và đích, không chỉ đọc bản đích) → kiểm thuật ngữ toàn gói → xem trên giao diện thật hoặc ảnh chụp màn hình (với app, website) → người hiểu nghiệp vụ duyệt đoạn rủi ro cao → kiểm lại các đoạn đã sửa.

Mỗi lỗi ghi: mã lỗi · mã đoạn · nhóm · mức · trích ngắn gốc/đích · quy tắc vi phạm · đề xuất sửa · người xử lý · kết quả kiểm lại.

Dịch ngược để kiểm chỉ là bằng chứng phụ; không chứng minh được bản dịch tự nhiên, đúng thuật ngữ hay hiển thị đúng.

## 7. Đối soát và cổng phát hành

Tổng số đoạn gốc = đã dịch + khóa (không dịch) + loại trừ + đang vướng. Ghi báo cáo kiểm tra, số lỗi chặn còn lại, quyết định của người kiểm, mã băm hoặc phiên bản file gốc/đích. Còn lỗi chặn → không nhập vào hệ thống, không phát hành. Nhập vào app, đăng website, gửi khách: chỉ người được giao làm sau khi duyệt.

*[A.I Generated — Claude Code — 30/10/2026]*
