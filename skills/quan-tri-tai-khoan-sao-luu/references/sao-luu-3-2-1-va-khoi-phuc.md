# SAO LƯU 3-2-1 VÀ KIỂM THỬ KHÔI PHỤC

**Mục lục:** 1. Phân mức dữ liệu · 2. Quy tắc 3-2-1 · 3. Đồng bộ không phải sao lưu · 4. Chống mã độc tống tiền · 5. Lịch và người chịu trách nhiệm · 6. Kiểm thử khôi phục · 7. Ví dụ

## 1. Phân mức dữ liệu (Bước 7)
Lãnh đạo chốt hai con số cho từng mức: **mất tối đa bao nhiêu dữ liệu** (tính bằng giờ, ngày kể từ lần sao lưu gần nhất) và **cần chạy lại trong bao lâu**. Chưa chốt: dùng gợi ý dưới đây, gắn [GIẢ ĐỊNH].

| Mức | Ví dụ dữ liệu | Gợi ý mức chấp nhận [GIẢ ĐỊNH] |
|---|---|---|
| **Cao** | Dữ liệu phần mềm kế toán, hợp đồng, hồ sơ khách hàng, CRM, hồ sơ nhân sự, bản vẽ, công thức sản xuất | Mất không quá 1 ngày dữ liệu; chạy lại trong 1 ngày làm việc |
| **Trung bình** | Tài liệu vận hành, file bán hàng, ảnh sản phẩm, website | Mất không quá 1 tuần; chạy lại trong vài ngày |
| **Thấp** | Tài liệu tham khảo, bản nháp cũ | Sao lưu khi tiện; chấp nhận mất |

Ghi rõ dữ liệu đang nằm ở đâu: phần mềm trên đám mây, máy chủ tại văn phòng, Drive/OneDrive, máy tính cá nhân, điện thoại. Dữ liệu chỉ nằm trên máy cá nhân là rủi ro cao nhất.

## 2. Quy tắc 3-2-1
- **3 bản:** bản đang dùng + 2 bản sao lưu.
- **2 loại nơi lưu:** ví dụ ổ cứng ngoài/thiết bị lưu trữ mạng tại văn phòng và dịch vụ lưu trữ đám mây.
- **1 bản ở nơi khác:** không cùng văn phòng (cháy, mất trộm, ngập không mất cả ba).
- Với dữ liệu mức Cao, nên có thêm **một bản không sửa, xóa được trong thời gian giữ** (bản ngoại tuyến rút ra khỏi máy, hoặc tính năng khóa phiên bản của dịch vụ sao lưu).
- Phần mềm trên đám mây (kế toán, CRM, email): hỏi nhà cung cấp họ sao lưu thế nào, giữ bao lâu, khôi phục ra sao; vẫn nên định kỳ **xuất dữ liệu** về bản của doanh nghiệp. Thông tin của nhà cung cấp phải có nguồn chính thức, có ngày.

## 3. Đồng bộ không phải sao lưu
Drive/OneDrive đồng bộ hai chiều: xóa nhầm, ghi đè, mã độc mã hóa file ở máy → bản trên đám mây cũng bị theo. Đồng bộ giúp dùng chung, **không thay sao lưu**. Lịch sử phiên bản và thùng rác giúp cứu một phần trong thời gian giới hạn của dịch vụ; không tính là một bản sao lưu trong 3-2-1.

## 4. Chống mã độc tống tiền
- Ổ sao lưu không cắm thường trực vào máy; sau khi sao lưu thì rút ra hoặc dùng tài khoản riêng chỉ để sao lưu.
- Tài khoản quản trị sao lưu khác tài khoản dùng hằng ngày, có xác thực hai lớp.
- Khi nghi bị nhiễm: ngắt máy nghi nhiễm khỏi mạng, báo người phụ trách an toàn thông tin; **không** cắm ổ sao lưu vào máy đó, không khôi phục đè khi chưa làm sạch.

## 5. Lịch và người chịu trách nhiệm
Mỗi dòng trong lịch sao lưu có: dữ liệu, mức, nơi gốc, tần suất, bản 1 ở đâu, bản 2 ở đâu (nơi khác), giữ bao nhiêu bản/bao lâu, công cụ (ghi chung, ví dụ "tính năng sao lưu của thiết bị lưu trữ mạng"), người chịu trách nhiệm, người dự phòng, cách kiểm tra đã chạy (nhật ký, email báo của công cụ), ngày thử khôi phục gần nhất.

Gợi ý tần suất [GIẢ ĐỊNH]: mức Cao hằng ngày; mức Trung bình hằng tuần; xuất dữ liệu phần mềm đám mây hằng tháng. Người quản trị kiểm nhật ký sao lưu ít nhất hằng tuần.

## 6. Kiểm thử khôi phục
- Lịch thử gợi ý [GIẢ ĐỊNH]: mỗi tháng thử một mẫu nhỏ (một file, một thư mục); mỗi quý thử khôi phục một bộ dữ liệu mức Cao; mỗi năm diễn tập khôi phục cả một máy hoặc một phần mềm.
- Khôi phục ra **vùng riêng** (thư mục thử, máy thử), không ghi đè dữ liệu đang dùng.
- Đo: mất bao lâu, dữ liệu mới nhất là của ngày nào, file mở được không, có thiếu gì.
- So với mức chấp nhận lãnh đạo đã chốt: ĐẠT / KHÔNG ĐẠT. Không đạt → ghi nguyên nhân, đề xuất khắc phục, ngày thử lại.
- Người quản trị chạy; A.I chuẩn bị kế hoạch, ghi biên bản theo `bien-ban-thu-khoi-phuc.md`, nhắc lịch.

## 7. Ví dụ (văn phòng kiến trúc 20 người)
"[DỮ KIỆN] Bản vẽ dự án nằm trên Drive đồng bộ, không có bản sao lưu riêng; dữ liệu phần mềm kế toán do nhà cung cấp giữ, chưa từng xuất về. [SUY LUẬN] Nếu một máy nhiễm mã độc, bản vẽ trên Drive có thể bị mã hóa theo. Đề xuất: thiết bị lưu trữ mạng tại văn phòng sao lưu Drive hằng đêm (bản 1), dịch vụ sao lưu đám mây có khóa phiên bản (bản 2, nơi khác); xuất dữ liệu kế toán hằng tháng; thử khôi phục một dự án mỗi quý. Mức chấp nhận [GIẢ ĐỊNH]: mất không quá 1 ngày bản vẽ — cần Anh/Chị chốt."

*[A.I Generated — Claude Code — 30/10/2026]*
