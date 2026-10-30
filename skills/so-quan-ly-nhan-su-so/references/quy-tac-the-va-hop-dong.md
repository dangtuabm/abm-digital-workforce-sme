# QUY TẮC THẺ NHÂN SỰ SỐ VÀ HỢP ĐỒNG GIAO VIỆC

**Mục lục**
- I. 06 thành phần và các trường bắt buộc
- II. Có thể – được phép – người quyết
- III. Chuỗi truy vết và đầu vào – đầu ra
- IV. Quyền, trạng thái, lỗi
- V. Nhật ký và kiểm thử tuân thủ
- VI. Điều cấm làm tắt

---

## I. 06 THÀNH PHẦN VÀ CÁC TRƯỜNG BẮT BUỘC

| Thành phần | Trường bắt buộc |
|---|---|
| **ROLE** | Phòng ban · **nỗi đau giải quyết** · nhiệm vụ · đầu ra và tiêu chí đạt · việc không thuộc vai trò · người giao việc và duyệt · **kích hoạt** (theo lệnh, theo lịch hay khi có sự kiện; chi tiết ở Workflow) |
| **MODEL** | Nền tảng và mô hình · khi nào dùng mô hình mạnh, khi nào dùng mô hình tiết kiệm |
| **KNOWLEDGE** | Thư mục được đọc · vùng cấm · **nhãn Xanh – Vàng – Đỏ của từng thư mục** · **Sổ bài học** · xử lý khi thiếu hoặc mâu thuẫn dữ liệu |
| **SKILLS** | **Skill chuyên môn** · **Skill nền theo việc** |
| **TOOLS** | Công cụ kết nối và mức quyền thật: Đọc / Soạn nháp / Hành động sau duyệt; chỉ ghi khi đã thử thật |
| **CONTROL** | **Quy tắc nền** · việc phải xin duyệt · Ranh giới Đỏ · khi nào dừng · **chỉ số theo dõi** (2–3 chỉ số để quyết giữ, sửa hay thay) · **người chịu trách nhiệm** · quy tắc chỉ là lời dặn, muốn chặn thật phải hạ quyền ở TOOLS |

Workflow (kích hoạt → các bước → điểm duyệt → đầu ra) đặt ở cuối Thẻ.

**Quy tắc nền** ghi trong CONTROL của mọi Thẻ:
1. Làm rõ yêu cầu — việc mơ hồ hỏi tối đa 3 câu, có sẵn phương án; việc lớn, nhiều bên thì gọi việc làm rõ yêu cầu đầy đủ.
2. Ghi nguồn — số liệu, dẫn chứng ghi rõ nguồn; tài liệu gửi ra ngoài hoặc trình lãnh đạo thì kiểm chứng nguồn và kiểm định đầu ra.
3. Xanh – Vàng – Đỏ — Xanh dùng thoải mái; Vàng che tên, số điện thoại, số tiền hoặc chỉ dùng tài khoản công ty; Đỏ không đưa lên A.I, dừng lại hỏi người phụ trách. Nhãn gắn một lần cho từng thư mục.
4. Sổ bài học — đọc sổ trước khi làm, ghi thêm sau mỗi lần bị sửa.

**Nhân sự số chạm dữ liệu Đỏ** (đối soát chứng từ, công nợ, lương – chấm công): chỉ đối soát, kiểm tra, soạn nháp, nhắc; con người duyệt; không tự tính lương chính thức, không tự đòi nợ, không tự gửi ra ngoài.

**Kênh cần kết nối** (Messenger, Zalo, sàn thương mại điện tử, email marketing, quảng cáo): ghi "cần kết nối" ở TOOLS; luôn có người duyệt trước khi gửi ra ngoài; Zalo khuyến nghị dùng Zalo OA chính thức.

## II. CÓ THỂ – ĐƯỢC PHÉP – NGƯỜI QUYẾT

- **Có thể** (công cụ có nút xóa) ≠ **được phép** (Thẻ cho xóa) ≠ **ai quyết** (người chịu trách nhiệm).
- Không suy quyền từ việc công cụ có sẵn, từ câu lệnh, từ chức danh hay từ lần trước làm được.
- "Chưa rõ" ở việc quan trọng = không làm, không phải được làm.
- Thẻ đạt kiểm tra nghĩa là đủ điều kiện để quyết; đưa vào chạy thật là một quyết định riêng của người có quyền.
- Quyền thật do tài khoản và kết nối trên phần mềm quyết định; Thẻ chỉ mô tả. Muốn chặn thật thì hạ quyền tài khoản.

## III. CHUỖI TRUY VẾT VÀ ĐẦU VÀO – ĐẦU RA

**Chuỗi truy vết tối thiểu**: kết quả → việc → đầu vào, nguồn, quyền → hành động → đối tượng, dữ liệu → công cụ, quyền → đầu ra, tiêu chí chấp nhận → bằng chứng → người quyết → trạng thái, kiểm lại.

**Đầu vào**: tên trường · kiểu · bắt buộc · nguồn / hệ thống gốc · độ tươi · nhãn dữ liệu · quyền dùng · kiểm hợp lệ · xử khi thiếu / mâu thuẫn · cách ly · xử lý lệnh chèn.

**Đầu ra**: tên · định dạng · nơi nhận · nhãn dữ liệu · tiêu chí chấp nhận · bằng chứng · mức chắc chắn · khi phải từ chối hoặc ghi "chưa rõ" · thời hạn lưu · xác nhận của bên nhận.

Xong việc khi có bằng chứng được chấp nhận — không phải khi đã tạo file, đã tải lên hay không ai phàn nàn.

**Một việc** có một kết quả được nghiệm thu độc lập và một người làm chính từ đầu đến cuối. Tìm hiểu, phân tích, soạn, tự soát là các bước bên trong, không phải lý do tách thêm A.I.

## IV. QUYỀN, TRẠNG THÁI, LỖI

**Ma trận quyền**: người / A.I · hành động · đối tượng · môi trường · ĐƯỢC LÀM / CÓ ĐIỀU KIỆN / CẤM · điều kiện, giới hạn · người duyệt · bằng chứng · hạn · báo lên ai. Tách riêng đọc, tạo, sửa, xóa, chạy, gửi / đăng, duyệt, mua / ký, quản trị quyền. Quyền tối thiểu; tách biệt nhiệm vụ — A.I không là người soát độc lập của chính mình, không tự duyệt quyền.

**Công cụ – dữ liệu – quyền**: công cụ · thao tác · tài nguyên · nhãn dữ liệu · tài khoản · phạm vi · giới hạn tốc độ / chi phí · tên tham chiếu khóa · bằng chứng cấp · hạn / thu hồi · cách kiểm.

**Trạng thái**: tên trạng thái do từng việc đặt; mỗi bước chuyển ghi từ – sang, sự kiện, ai làm, điều kiện, hành động, kết quả mong đợi, cách kiểm, bằng chứng, hạn chờ, bước chuyển khi lỗi. Mã chống làm trùng xử lý việc lặp, chạy lại, đến muộn.

**Lỗi**: phân loại chạy lại được / không / chưa rõ; chạy lại có giới hạn, giãn cách; không gây tác động trùng (gửi hai lần, ghi hai lần); hạn chờ, dự phòng, bù trừ, đối chiếu, chuyển người, hàng chờ lỗi, làm tay, dừng khẩn, quay lại sau sửa. Không im lặng khi lỗi.

**Mức dịch vụ – ngân sách – sức chứa**: chỉ số, công thức / nguồn, lý do ngưỡng, khung thời gian, người phụ trách, hành động khi vượt, bằng chứng. Không tự tăng chi tiêu hay tự nâng quyền.

## V. NHẬT KÝ VÀ KIỂM THỬ TUÂN THỦ

**Nhật ký**: mã theo dõi, thời điểm, phiên bản Thẻ – Skill – mô hình – công cụ, đường dẫn đầu vào – đầu ra, trạng thái trước – sau, hành động, quyền, duyệt, kiểm, lỗi, chạy lại, dự phòng, chi phí, đường dẫn kết quả. Che, tối thiểu hóa; khóa chỉ ghi tên tham chiếu.

**Kiểm thử tuân thủ tối thiểu**: đúng mẫu dữ liệu · thiếu / mâu thuẫn · tiêu chí xong việc · quyền và quyền tối thiểu · chèn lệnh · chống làm trùng · hạn chờ · chạy lại / dự phòng · chuyển người / hàng chờ lỗi · quay lui / đối chiếu · nhật ký / che dữ liệu · người duyệt · cho nghỉ. Có ca lỗi và ca sai, không chỉ ca suôn sẻ.

**Phiên bản**: Thẻ, mẫu dữ liệu, Skill, công cụ, phụ thuộc đều có phiên bản; ghi cách tương thích ngược, chuyển đổi, chạy thử nhỏ, quay lui, báo bên dùng.

## VI. ĐIỀU CẤM LÀM TẮT

Không bịa quyền hay bằng chứng · không coi "chưa rõ" là được làm · không dùng câu lệnh thay hợp đồng · không dùng chung khóa tĩnh · không để chạy lại, ngân sách, việc làm dở vô hạn · không im lặng khi lỗi · không tự tạo tài khoản, khóa · không tự kích hoạt, chạy, gửi, ghi, xóa, duyệt, ký, mua, công bố · không đổi phạm vi hay phiên bản khi chưa rà · không cho nghỉ trước khi qua bước khôi phục và lưu giữ.

*[A.I Generated — Claude Code — 30/10/2026]*
