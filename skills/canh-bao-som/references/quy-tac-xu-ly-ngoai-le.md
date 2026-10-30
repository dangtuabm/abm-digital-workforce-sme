# QUY TẮC XỬ LÝ NGOẠI LỆ

Ngoại lệ không phải mọi biến động. Ngoại lệ là **sai lệch vượt quy tắc đã duyệt**, hoặc tình huống cần quyền quyết định cao hơn người đang xử lý.

## 1. Ngưỡng và số liệu

- Ngưỡng phải có mã, phiên bản, người/cấp duyệt, ngày hiệu lực. Không đổi ngưỡng hồi tố sau khi đã thấy số liệu.
- Chỉ số, đơn vị, chiều vượt (trên/dưới), cửa sổ tính, phạm vi phải khớp quy tắc. Ví dụ: ngưỡng "công nợ quá hạn > 90 ngày vượt 15% tổng phải thu" không áp được cho số liệu công nợ quá hạn > 60 ngày.
- Số liệu phải có nguồn, phiên bản hoặc vị trí, độ mới, quyền truy cập, độ tin cậy. Tách số **được báo** với số **đã kiểm**.
- Số liệu thiếu, cũ, bị chặn quyền, không so được **không** được chuyển thành "không có ngoại lệ".

## 2. Mã ngoại lệ, mức ưu tiên và liên kết

- Mã ngoại lệ = phạm vi + ngưỡng + đối tượng + kỳ (ví dụ `NL-TONKHO-KHOHCM-SKU112-2026-10`). Cảnh báo gửi lặp, nhập lại phải gộp vào cùng mã.
- Mức tác động dựa trên thiệt hại; độ gấp dựa trên thời gian trước khi thiệt hại xảy ra hoặc hạn trả lời quyết định — không dựa trên ai báo to hơn.
- Ngoại lệ liên quan nối theo quan hệ cha–con hoặc cùng nguyên nhân. Thiệt hại chung chỉ tính **một lần**. Quan hệ "có thể cùng nguyên nhân" ghi rõ là chưa chứng minh.

## 3. Thẩm quyền và vòng đời

- Người phụ trách ngoại lệ, người quyết định, người kiểm chứng, người đóng phải là người thật có vai trò hợp lệ. A.I không là người phụ trách.
- Việc khoanh vùng hay khắc phục chỉ được ghi là "đã làm" khi có cho phép của người có quyền **và** bằng chứng.
- Vòng đời: PHÁT HIỆN → ĐÃ KIỂM → ĐÃ PHÂN LOẠI → ĐÃ ĐỀ XUẤT KHOANH VÙNG → CHỜ NGƯỜI CÓ QUYỀN QUYẾT ĐỊNH → ĐANG KHẮC PHỤC → CHỜ NGƯỜI CÓ QUYỀN ĐÓNG. Có lỗi nghiêm trọng trong hồ sơ → CHƯA ĐỦ ĐIỀU KIỆN.
- A.I chỉ đưa hồ sơ tới hai điểm dừng: CHỜ NGƯỜI CÓ QUYỀN QUYẾT ĐỊNH hoặc CHỜ NGƯỜI CÓ QUYỀN ĐÓNG.

## 4. Đóng ngoại lệ

- Có kết quả khắc phục chưa phải là đóng. Phải: chỉ số về trong ngưỡng suốt thời gian kiểm chứng đã định · biện pháp khoanh vùng được gỡ hoặc giữ lại có lý do · rủi ro còn lại được người có quyền chấp nhận · đã kiểm tái diễn.
- Mở lại khi: chỉ số vượt ngưỡng trở lại, bằng chứng sai hoặc cũ, rủi ro còn lại vượt mức chấp nhận.
- Bài học (sửa ngưỡng, sửa quy tắc, sửa kiểm soát) chỉ là **đề xuất**; không tự sửa bảng ngưỡng hay lịch sử.

## 5. Các việc cấm (đánh dấu ngay nếu thấy trong hồ sơ)

Đổi ngưỡng · đổi mức nền · đổi ngày chốt số · bịa nguồn · bịa số liệu · giấu ngoại lệ · hạ mức độ · cộng trùng thiệt hại · bịa người phụ trách · để A.I làm người phụ trách · tự gửi cảnh báo · tự khoanh vùng · tự chi tiền · tự kỷ luật · tự ghi đã khắc phục · tự đóng · xóa bằng chứng · bỏ qua bước duyệt.

## 6. Ví dụ đối chiếu

**Tình huống:** công ty phân phối vật liệu xây dựng; ngưỡng NG-CN-02 v3 (duyệt bởi Giám đốc tài chính, hiệu lực 01/07): "một khách hàng nợ quá hạn > 500 triệu đồng thì tạm dừng giao hàng chờ quyết định". Đại lý X nợ quá hạn 640 triệu.

**Sai:** "Đã tạm dừng giao hàng cho đại lý X và gửi email nhắc nợ." (A.I tự hành động)
**Đúng:** "Ngoại lệ NL-CN-DAILYX-2026-10 vượt ngưỡng NG-CN-02 v3 140 triệu. Phương án: (A) tạm dừng giao, (B) giao tiếp có bảo lãnh, (C) giao tiếp kèm lịch trả. Người quyết định: Giám đốc tài chính, hạn 17h hôm nay; chậm thì đơn 320 triệu chiều nay vẫn xuất kho. Trạng thái: CHỜ NGƯỜI CÓ QUYỀN QUYẾT ĐỊNH."

*[A.I Generated — Claude Code — 30/10/2026]*
