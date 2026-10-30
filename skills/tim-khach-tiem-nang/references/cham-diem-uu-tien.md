# CHẤM ĐIỂM ƯU TIÊN VÀ LẬP DANH SÁCH GỌI HÔM NAY

## 1. Bốn chiều chấm (thang 0–3, mỗi điểm phải có căn cứ)

| Chiều | 0 | 1 | 2 | 3 |
|---|---|---|---|---|
| **Phù hợp chân dung** (`diem_phu_hop`) | Rơi vào tiêu chí loại trừ | Khớp 1 tiêu chí chính | Khớp phần lớn tiêu chí chính | Khớp đủ ngành, quy mô, khu vực, nhu cầu điển hình |
| **Tín hiệu mua** (`diem_tin_hieu`) | Không thấy tín hiệu | Tín hiệu yếu, cũ hoặc gián tiếp | Một tín hiệu rõ có ngày trong 6 tháng [GIẢ ĐỊNH] | Nhiều tín hiệu rõ, gần đây, hoặc khách tự hỏi |
| **Khả năng tiếp cận** (`diem_tiep_can`) | Không có kênh hợp lệ | Chỉ có tổng đài chung | Có kênh công việc tới đúng bộ phận | Có người giới thiệu, đã gặp ở hội chợ, khách cũ |
| **Giá trị tiềm năng** (`diem_gia_tri`) | Dưới mức đơn tối thiểu | Đơn nhỏ, mua một lần | Đơn điển hình | Đơn lớn hoặc mua lặp lại, nhiều chi nhánh |

Không có căn cứ cho một chiều → để trống, **không** cho điểm trung bình. Bộ chấm sẽ gắn cờ THIẾU ĐIỂM.

## 2. Tín hiệu mua thường gặp ở SME Việt Nam

| Tín hiệu | Ví dụ | Hợp với |
|---|---|---|
| Mở chi nhánh, nhà xưởng, cửa hàng mới | Biển "sắp khai trương", tin tuyển dụng cho địa điểm mới | Thiết bị, nội thất, phần mềm, nguyên liệu, dịch vụ vệ sinh |
| Tuyển nhiều người ở một bộ phận | Đăng tuyển 10 nhân viên kho, 5 kế toán | Đào tạo, phần mềm, dịch vụ thuê ngoài |
| Trúng thầu, ký hợp đồng lớn | Kết quả lựa chọn nhà thầu công khai | Nhà cung cấp đầu vào, thầu phụ |
| Mời thầu, chào giá công khai | Thông báo mời thầu | Đúng hàng hóa, dịch vụ trong gói |
| Đổi lãnh đạo, đổi chủ | Tin báo chí, thông báo thay đổi đăng ký | Dịch vụ tư vấn, đổi nhà cung cấp |
| Ra sản phẩm mới, vào thị trường mới | Tin tức, Fanpage | Bao bì, marketing, logistics |
| Phàn nàn công khai về nhà cung cấp hiện tại | Bài trong nhóm ngành | Đối thủ thay thế — liên hệ lịch sự, không công kích |
| Khách cũ ngừng mua sau chu kỳ mua bình thường | Dữ liệu CRM | Tái kích hoạt |
| Khách tự hỏi giá, tải tài liệu, để lại thông tin | CRM, form website | Ưu tiên cao nhất |

Mỗi tín hiệu ghi: nội dung, ngày, đường dẫn/nguồn. Tín hiệu cũ hơn 6 tháng [GIẢ ĐỊNH] coi là tín hiệu yếu (tối đa 1 điểm).

## 3. Trọng số và điểm ưu tiên

Điểm ưu tiên (0–100) = Σ (trọng số chiều × điểm chiều / 3).

| Chiều | Trọng số mặc định [GIẢ ĐỊNH — trưởng nhóm duyệt] |
|---|---|
| Phù hợp chân dung | 35 |
| Tín hiệu mua | 30 |
| Khả năng tiếp cận | 20 |
| Giá trị tiềm năng | 15 |

- Trọng số là lựa chọn quản trị, không phải chuẩn ngành. Ghi phiên bản trọng số và người duyệt vào danh sách.
- Sau 4 tuần gọi thật: so điểm ưu tiên với kết quả (khách có nhận gặp, có thành cơ hội không). Nhóm điểm cao mà kết quả kém → đề xuất chỉnh trọng số, trưởng nhóm duyệt.

Bộ chấm `scripts/cham-diem-danh-sach.py` tính điểm và gắn cờ:

| Cờ | Ý nghĩa | Xử lý |
|---|---|---|
| `TU_CHOI_LIEN_HE` | `tu_choi_lien_he` = co | Không bao giờ đưa vào danh sách gọi |
| `THIEU_NGUON` | Trống `nguon` hoặc `ngay_lay` | Không đưa vào danh sách gọi đến khi bổ sung nguồn |
| `TRUNG` | Tên doanh nghiệp (bỏ dấu, bỏ "công ty", "TNHH"…) hoặc mã số thuế trùng dòng khác | Gộp dòng |
| `DA_CO_TRONG_CRM` | `co_trong_crm` = co | Kiểm người phụ trách trước khi giao |
| `CHUA_DOI_CHIEU_CRM` | `co_trong_crm` trống | Trạng thái CHƯA ĐỐI CHIẾU |
| `THIEU_DIEM` | Thiếu một trong 4 điểm | Bổ sung căn cứ hoặc ghi rõ chưa đủ dữ liệu |
| `KHONG_KENH_HOP_LE` | Trống `kenh_lien_he_hop_le` | Không giao gọi |

## 4. Lập danh sách gọi hôm nay

1. Chỉ lấy dòng **không có cờ chặn** (`TU_CHOI_LIEN_HE`, `THIEU_NGUON`, `KHONG_KENH_HOP_LE`, `TRUNG` chưa gộp) và đã đối chiếu CRM.
2. Bỏ khách đã được liên hệ trong khoảng thời gian trưởng nhóm quy định (mặc định 14 ngày [GIẢ ĐỊNH]).
3. Khách đã có người phụ trách → chỉ giao cho đúng người đó.
4. Chia theo khu vực hoặc ngành người bán đang phụ trách; trong mỗi nhóm xếp theo điểm ưu tiên.
5. Số khách mỗi người theo năng lực trưởng nhóm đặt (ví dụ "15 cuộc gọi mới/ngày" — con số do doanh nghiệp quyết). Không dồn thêm vì danh sách còn dài.
6. Mỗi khách ghi một **lý do gọi hôm nay** cụ thể (tín hiệu mua, người giới thiệu, đã gặp ở hội chợ), một **điểm nối** để mở lời, một **câu hỏi đầu tiên** để khai thác nhu cầu. Không viết kịch bản dài.
7. Cuối bảng có ô ghi kết quả để người bán điền: GẶP ĐƯỢC · HẸN LẠI · KHÔNG NGHE · SAI ĐẦU MỐI · KHÔNG CÓ NHU CẦU · TỪ CHỐI LIÊN HỆ.

*[A.I Generated — Claude Code — 30/10/2026]*
