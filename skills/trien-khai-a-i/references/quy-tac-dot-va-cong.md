# QUY TẮC TRIỂN KHAI THEO ĐỢT VÀ CỔNG ĐIỀU KIỆN

**Mục lục**
- 1. Mô hình kiểm soát
- 2. Chuỗi truy vết tối thiểu
- 3. Danh sách giai đoạn
- 4. Thử hẹp và giới hạn phạm vi ảnh hưởng
- 5. Kịch bản chuyển đổi
- 6. Quay lui, làm tay dự phòng, đối soát
- 7. Theo dõi và giá trị
- 8. Quyết định và ngoại lệ
- 9. Đường tắt bị cấm

Dùng cho chế độ **Lộ trình đợt** (Bước 2–7) và **Rà cổng** (Bước 15–16).

## 1. Mô hình kiểm soát

- **Đợt là đơn vị phát hành**: có phạm vi, phiên bản, nhóm người dùng, phụ thuộc, người phụ trách, căn cứ và giới hạn ảnh hưởng. Không phải lịch trang trí, không mặc định là phòng ban hay tháng, quý.
- Lịch chỉ là khoảng dự kiến. Tiêu chí vào – ra và năng lực thật mới quyết được có đề xuất chuyển giai đoạn hay không.
- Trạng thái cổng:
  - **ĐẠT** — căn cứ còn hiệu lực đáp ứng tiêu chí.
  - **KHÔNG ĐẠT** — không đáp ứng.
  - **CHƯA BIẾT** — thiếu, hết hạn hoặc mâu thuẫn.
  - **NGOẠI LỆ** — người có quyền chấp nhận rủi ro còn lại, có phạm vi và hạn; không biến KHÔNG ĐẠT thành ĐẠT.
- Cổng quan trọng KHÔNG ĐẠT hoặc CHƯA BIẾT → dừng đề xuất mở rộng. Điểm tổng không bù được cổng quan trọng.
- A.I lập hồ sơ và kiểm tính nhất quán; người có quyền triển khai quyết TIẾP TỤC / GIỮ / LÀM LẠI / QUAY LUI / NGỪNG.

## 2. Chuỗi truy vết tối thiểu

Kết quả cần đạt → đơn vị phát hành → phụ thuộc, dữ liệu gốc → tiêu chí cổng → căn cứ → quyết định → bước chuyển đổi → cách kiểm → tín hiệu theo dõi → kết quả giá trị, mức dùng → thay đổi cho đợt sau.

Căn cứ cần: mã, nguồn, thời điểm, phạm vi – phiên bản, người phụ trách, hạn hiệu lực, mức tin cậy – mâu thuẫn, trạng thái. Không dùng "đã test", "sẵn sàng", "an toàn", "mọi người đồng ý" nếu không có sản phẩm và kết quả nghiệm thu đi kèm.

## 3. Danh sách giai đoạn

CHUẨN BỊ · KIỂM THỬ – NGHIỆM THU · THÍ ĐIỂM · THỬ HẸP · MỞ RỘNG CÓ GIỚI HẠN · MỞ RỘNG · TẠM GIỮ · QUAY LUI · NGỪNG.

Đây là danh sách để chọn, không bắt buộc dùng đủ và không mặc định một thứ tự cho mọi trường hợp. Mỗi giai đoạn có:
- mục đích, nhóm người dùng – mức tiếp xúc, phiên bản – môi trường;
- cổng vào – ra và hạn hiệu lực của căn cứ;
- tín hiệu giá trị, chất lượng, an toàn, chi phí, mức dùng;
- phụ thuộc, năng lực, hỗ trợ;
- người được dừng, quay lui, vào lại, duyệt ngoại lệ;
- bài học mang sang giai đoạn sau.

Ví dụ SME: chuỗi 6 cửa hàng F&B dùng A.I soạn đơn đặt nguyên liệu — KIỂM THỬ với dữ liệu 2 tuần trước → THÍ ĐIỂM ở 1 cửa hàng, bếp trưởng duyệt mọi đơn → MỞ RỘNG CÓ GIỚI HẠN thêm 2 cửa hàng → rà cổng → MỞ RỘNG.

## 4. Thử hẹp và giới hạn phạm vi ảnh hưởng

- Nhóm thử phải đủ đại diện cho các kiểu lỗi quan trọng nhưng hạn chế được thiệt hại.
- Ghi mức tiếp xúc: người dùng, dữ liệu, hệ thống, quyền, giao dịch, địa điểm, thời gian; cách khoanh vùng và người làm tay dự phòng.
- Thời gian quan sát gắn với tín hiệu, tần suất, cỡ mẫu, mùa vụ; không cứng số ngày.
- Không có phàn nàn không phải căn cứ thành công. Mức dùng không phải giá trị. Số trung bình không được che nhóm gặp lỗi.

## 5. Kịch bản chuyển đổi

Mỗi bước: trạng thái trước · hành động · người làm · người cho phép · phụ thuộc · kết quả mong đợi · cách kiểm · trạng thái sau · căn cứ · thời hạn · điều kiện dừng · mã quay lui · trạng thái hành động.

- Kiểm trước khi bắt đầu: phiên bản, cấu hình, dữ liệu, phân quyền, kết nối, bản sao lưu, hỗ trợ, thông báo đã duyệt, giai đoạn đóng băng thay đổi.
- Cách kiểm phải từ đầu đến cuối và đối chiếu với dữ liệu gốc; lệnh chạy thành công chưa đủ.
- Trong kế hoạch, mọi hành động ở trạng thái **CHỜ**. Skill không chạy lệnh, không đổi quyền, không ghi – xóa – chuyển dữ liệu, không gửi thông báo.

## 6. Quay lui, làm tay dự phòng, đối soát

- Hồ sơ quay lui: điều kiện kích hoạt, người quyết, bản khôi phục (phiên bản, cấu hình, dữ liệu), đã thử hay chưa và căn cứ, thời gian chấp nhận được do doanh nghiệp duyệt, đường làm tay, đảo ngược phụ thuộc, điều kiện vào lại.
- Quay lui chưa thử → ghi **CHƯA THỬ** và hậu quả; không gọi là "có sẵn".
- Đối soát: số lượng, tổng, thiếu, trùng, mồ côi, thứ tự, lỗi dở dang, truy từ nguồn sang đích. Chỉ người có quyền chấp nhận chênh lệch.
- Không ngừng cách làm cũ trước khi qua cổng ra, có quyết định lưu – xóa dữ liệu của người có quyền và có căn cứ khôi phục.

## 7. Theo dõi và giá trị

Tối thiểu xem: kết quả – giá trị, chất lượng, an toàn – dữ liệu cá nhân – bảo mật, độ ổn định, tốc độ – năng lực, chi phí, mức dùng – năng lực người dùng, sự cố – hỗ trợ. Mỗi tín hiệu có đầu kỳ, công thức – nguồn, lý do ngưỡng, tần suất – kỳ, nhóm, người phụ trách, cảnh báo, hành động, căn cứ.

Xét giá trị: so với đầu kỳ theo cùng công thức, nguồn, nhóm, kỳ; tách tương quan khỏi nguyên nhân; ghi yếu tố bên ngoài, chỉ số đối trọng và mức tin cậy. Hoàn thành đào tạo, số người dự lớp, số lượt dùng không thay cho kết quả.

## 8. Quyết định và ngoại lệ

- Quyết định ghi: mã căn cứ, người có quyền, các phương án, lý do, rủi ro còn lại, trạng thái hành động, hạn hoặc điều kiện rà lại.
- Ngoại lệ có phạm vi, người phụ trách, biện pháp bù, hạn, căn cứ đóng; không để mở vô hạn.
- Hành động ra ngoài luôn **CHỜ** cho đến khi người có quyền duyệt và người vận hành kiểm trạng thái sau.

## 9. Đường tắt bị cấm

Tự bật hoặc tự mở rộng; bịa, ghi lùi ngày, xóa căn cứ; coi CHƯA BIẾT là ĐẠT; cứng 3 đợt, một tỷ lệ phần trăm, 30–60 ngày hay một thứ tự phòng ban thành quy tắc; bỏ kiểm thử – nghiệm thu, bảo mật, phân quyền, quay lui, đối soát; tăng quyền; đụng hệ thống thật; gửi, công bố; mua, ký; ngừng cách làm cũ để ép tiến độ.

*[A.I Generated — Claude Code — 30/10/2026]*
