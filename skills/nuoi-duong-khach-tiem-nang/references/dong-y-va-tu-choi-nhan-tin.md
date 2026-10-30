# ĐỒNG Ý VÀ TỪ CHỐI NHẬN TIN

Đọc ở Bước 2 (kiểm trước khi thiết kế, trước mỗi đợt gửi) và Bước 9 (xử lý phản hồi). Đây là hướng dẫn thực hành; quy định về quảng cáo qua tin nhắn, thư điện tử và bảo vệ dữ liệu cá nhân cần đối chiếu văn bản pháp luật hiện hành, cần người có chuyên môn xác nhận.

## I. CĂN CỨ ĐỒNG Ý
| Nguồn khách | Căn cứ đồng ý thường gặp | Cần lưu |
|---|---|---|
| Biểu mẫu trên website, trang đích | Ô đồng ý nhận thông tin ghi rõ nội dung sẽ nhận | Thời điểm, nội dung ô đồng ý, nguồn |
| Hội chợ, sự kiện | Phiếu đăng ký có câu đồng ý nhận tin | Ảnh phiếu hoặc bản ghi, ngày |
| Khách đã mua | Điều khoản lúc mua có nêu nhận thông tin chăm sóc | Đơn hàng, điều khoản áp dụng |
| Quan tâm Zalo OA | Theo chính sách của nền tảng cho loại tin tương ứng | Ngày quan tâm |
| Danh sách mua, danh sách cào từ mạng, danh bạ đối tác chuyển sang | **Không phải căn cứ đồng ý** | Không dùng |

Không xác định được căn cứ → không đưa vào đợt gửi; báo người giao.

## II. XỬ LÝ TỪ CHỐI
- Mọi tin có cách từ chối rõ ràng. Khách bấm từ chối, nhắn "không nhận nữa", "đừng nhắn", hoặc phàn nàn bị làm phiền → coi là từ chối.
- Ghi vào `templates/danh-sach-tu-choi-nhan-tin.csv` trong ngày; dừng **mọi** chuỗi, **mọi** kênh với người đó.
- Không gửi tin "tiếc nuối" kèm ưu đãi để níu kéo. Có thể gửi một tin xác nhận đã ngừng nếu công cụ tự gửi.
- Trước mỗi đợt gửi: đối chiếu danh sách gửi với danh sách từ chối mới nhất.
- Khách từ chối kênh này nhưng vẫn là khách hàng: nhân viên vẫn phục vụ đơn hàng, bảo hành bình thường — chỉ dừng tin chăm sóc, quảng bá.

## III. YÊU CẦU XÓA HOẶC SỬA DỮ LIỆU
- Khách yêu cầu xóa, sửa thông tin cá nhân: chuyển người phụ trách dữ liệu của doanh nghiệp xử lý; A.I không tự xóa trong hệ thống.
- Ghi nhận yêu cầu và ngày tiếp nhận để theo dõi.

## IV. DỮ LIỆU VÀNG KHI LÀM VỚI A.I
- Tên, email, số điện thoại, lịch sử mua là dữ liệu Vàng.
- Soạn mẫu tin: dùng biến, không dán danh sách khách thật vào công cụ A.I ngoài tài khoản công ty.
- Báo cáo đợt: ghi số tổng hợp, không liệt kê thông tin cá nhân trừ danh sách chuyển bán hàng nội bộ.
