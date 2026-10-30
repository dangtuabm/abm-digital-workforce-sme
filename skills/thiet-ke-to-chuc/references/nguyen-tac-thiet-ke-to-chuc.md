# NGUYÊN TẮC THIẾT KẾ TỔ CHỨC

## 1. Thứ bậc nguồn
1. Chiến lược, điều lệ, quy chế, sơ đồ quyền hạn đã được người có thẩm quyền duyệt.
2. Dữ liệu vận hành có mốc ngày: khối lượng công việc, thời gian chờ duyệt, sự cố, chuẩn dịch vụ.
3. Phỏng vấn, hội thảo có biên bản và người xác nhận.
4. Giả định thiết kế — gắn nhãn [GIẢ ĐỊNH], có người phụ trách xác minh.

Nguồn cấp thấp không ghi đè nguồn cấp cao. Mâu thuẫn đưa vào tóm tắt cho người quyết.

## 2. Truy vết
- Mỗi mục tiêu chiến lược nối tới ít nhất một dòng giá trị (chuỗi việc tạo ra giá trị cho khách: tìm khách → bán → giao → thu tiền → chăm sóc).
- Mỗi dòng giá trị cần những năng lực (ví dụ: dự báo nhu cầu, mua hàng, kiểm soát chất lượng, giao vận).
- Mỗi năng lực quan trọng có **đúng một** đơn vị/vai trò chịu trách nhiệm cuối; nhiều đơn vị được phép đóng góp.
- Mỗi đơn vị/vai trò trong mô hình mới nối được về ít nhất một năng lực. Vai trò không có mục đích, kết quả, khối lượng và nguồn là chưa hợp lệ.
- Lập danh sách công việc và quyết định thật, không suy ra từ chức danh.

## 3. Chẩn đoán
| Vấn đề | Dấu hiệu | Cách xác nhận |
|---|---|---|
| Chỗ hở | Năng lực không ai chịu ("việc này ai lo?") | Không có tên trong cột chịu trách nhiệm cuối |
| Chồng chéo | Hai người cùng nghĩ mình quyết, hoặc cùng đổ cho nhau | Hai tên ở cột chịu trách nhiệm cuối |
| Nút thắt quyết định | Việc chờ một người duyệt quá lâu, thường là giám đốc | Thời gian chờ duyệt, số việc chờ |
| Phối hợp kém | Bàn giao giữa phòng hay sót, sai | Sự cố lặp ở điểm bàn giao |
| Tầm quản lý quá rộng/hẹp | Quản lý không kèm được người, hoặc quản lý chỉ có 1–2 người | Có dữ liệu khối lượng, độ phức tạp |

Tầm quản lý và số tầng:
- **Không** dùng con số lý tưởng chung. Việc lặp lại, đã chuẩn hóa (thu ngân, đóng gói) cho phép một quản lý phụ trách nhiều người hơn; việc phức tạp, ít chuẩn hóa (kỹ thuật, bán hàng dự án) cần ít hơn.
- Chỉ kết luận khi có dữ liệu khối lượng, độ phức tạp, mức chuẩn hóa, năng lực quản lý, rủi ro. Thiếu → ghi CHƯA ĐỦ DỮ LIỆU.
- Một tầng quản lý chỉ bị coi là thừa khi có bằng chứng: không thêm giá trị, làm chậm quyết định, trùng trách nhiệm.

## 4. Mẫu cơ cấu và đánh đổi
| Mẫu | Hợp khi | Điểm mạnh | Điểm yếu cần kiểm soát |
|---|---|---|---|
| Theo chức năng (kinh doanh, kho, kế toán...) | Ít dòng sản phẩm, quy mô nhỏ – vừa | Chuyên môn sâu, dễ chuẩn hóa | Phối hợp ngang chậm, dồn lên giám đốc |
| Theo sản phẩm hoặc nhóm khách hàng | Nhiều dòng sản phẩm/khách khác nhau rõ | Nhanh với khách, rõ lãi lỗ từng mảng | Trùng chức năng, tốn người |
| Theo khu vực/chi nhánh | Nhiều điểm bán, địa bàn khác nhau | Sát thị trường địa phương | Khó đồng bộ chuẩn, kiểm soát |
| Kết hợp (ma trận) | Cần cả chuyên môn sâu và sát khách | Linh hoạt | Hai "sếp", dễ xung đột; cần quyền quyết định rất rõ |

So sánh phương án theo: phù hợp chiến lược · dòng chảy tới khách · tốc độ quyết định · năng lực và chi phí (có căn cứ) · rủi ro · độ khó chuyển đổi. Mỗi phương án ghi giả định và điều kiện nên chọn.

## 5. Bảy phép kiểm trước khi bàn giao
1. **Truy vết:** mọi đơn vị, vai trò mới nối được về năng lực, dòng giá trị, mục tiêu.
2. **Người chịu cuối:** mỗi năng lực quan trọng đúng một người chịu; vai trò có mục đích, kết quả, khối lượng, nguồn.
3. **Quyền quyết định:** mỗi quyết định đúng một người quyết, có ngưỡng và người thực hiện.
4. **Phối hợp và phân tách nhiệm vụ:** thỏa thuận phối hợp đủ trường; không vai trò nào tự đề xuất – tự duyệt – tự kiểm.
5. **Tầm quản lý:** nhận định có dữ liệu, không dùng số chuẩn.
6. **Ranh giới người – A.I:** việc có A.I tham gia có người giám sát, có cách kiểm lại, có cách quay về làm tay; A.I không chịu trách nhiệm cuối.
7. **Ranh giới thực hiện:** không thay đổi nhân sự, lương, tuyến báo cáo, quyền hay cơ cấu nào được ghi là đã thực hiện.

Một phép kiểm không đạt → trạng thái CHƯA SẴN SÀNG hoặc SẴN SÀNG ĐỂ RÀ SOÁT kèm lỗi cần sửa.

*[A.I Generated — Claude Code — 30/10/2026]*
