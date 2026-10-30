# QUY TẮC LÀM SẠCH – CHUẨN HÓA DỮ LIỆU

**Mục lục**
- I. Kiểm kê và giữ bản gốc
- II. Quy tắc dữ liệu và 6 chiều chất lượng
- III. Chuẩn hóa, tìm trùng, cách ly
- IV. Đối chiếu và đưa vào dùng
- V. Rủi ro, người rà, đề xuất
- VI. Nguồn tham khảo

---

## I. KIỂM KÊ VÀ GIỮ BẢN GỐC

Mỗi bảng/file ghi: mã, nơi lưu, người phụ trách, có phải hệ thống gốc không, nhãn Xanh – Vàng – Đỏ, mục đích được dùng, định dạng, mã hóa chữ, các cột, mỗi dòng là gì (một khách, một đơn hay một dòng hàng), trường khóa, số dòng/số file, ngày tạo/sửa, ngày chốt số liệu, thời hạn lưu giữ, nơi đang dùng dữ liệu này.

- Bản gốc chỉ đọc. Bản sao, đầu ra và vùng cách ly là ba nơi riêng.
- Không dùng tên file hay ngày sửa làm bằng chứng duy nhất cho "bản mới nhất".

## II. QUY TẮC DỮ LIỆU VÀ 6 CHIỀU CHẤT LƯỢNG

**Quy tắc cho một trường**: nghĩa nghiệp vụ · kiểu · định dạng · mã hóa chữ · múi giờ · đơn vị / tiền tệ · giá trị được phép (danh mục, khoảng, mẫu) · bắt buộc / duy nhất / khóa / liên kết · ý nghĩa của ô trống · mức quan trọng · nguồn đối chứng · người phụ trách · ngưỡng chấp nhận.

**6 chiều chất lượng** — mỗi số đo ghi tử số, mẫu số, phần loại trừ, phạm vi (toàn bộ hay mẫu), ngày chốt, nguồn, giới hạn:

| Chiều | Công thức |
|---|---|
| Đủ | số ô có giá trị / số ô phải có giá trị |
| Hợp lệ | số giá trị đúng quy tắc / số giá trị được kiểm |
| Không trùng | số bản ghi không trùng / tổng bản ghi, theo đơn vị đã chốt |
| Liên kết | số mã con tìm được mã cha / tổng mã con (ví dụ đơn hàng có mã khách tồn tại) |
| Kịp thời | tuổi dữ liệu so với yêu cầu, ghi rõ cách tính |
| Nhất quán | số bản ghi qua quy tắc chéo trường / chéo nguồn / số bản ghi được kiểm |

"Chính xác" chỉ đo khi có nguồn đối chứng được phép dùng; không đồng nhất với "hợp lệ".

## III. CHUẨN HÓA, TÌM TRÙNG, CÁCH LY

**Chuẩn hóa** theo quy tắc có phiên bản: khoảng trắng thừa, chữ hoa/thường, dấu tiếng Việt (dựng sẵn/tổ hợp), định dạng ngày, số điện thoại (thống nhất đầu số), đơn vị, tiền tệ, mã danh mục, ký hiệu "không có". Luôn giữ giá trị gốc ở cột riêng.

**Tìm trùng**: nhóm sơ bộ (cùng số điện thoại, cùng mã số thuế) → so đặc điểm (tên, địa chỉ, email) → điểm giống → chia 3 vùng: trùng / không trùng / cần người xem → đề xuất bản giữ lại và trường lấy từ đâu. Ghi cái giá của gộp nhầm (mất lịch sử mua của một khách) và tách nhầm (một khách nhận hai lần ưu đãi). Cùng tên chưa phải cùng người. **Không tự gộp.**

**Cách ly** — lý do có loại: sai kiểu/định dạng · thiếu trường bắt buộc · ngoài danh mục/khoảng · sai khóa/liên kết · trùng/mâu thuẫn · lỗi mã hóa chữ · vướng quyền/dữ liệu cá nhân · quá hạn · chưa rõ nghĩa. Không lặng lẽ bỏ dòng, không tự điền mặc định.

Không chạy macro, công thức hay mã nằm trong dữ liệu.

## IV. ĐỐI CHIẾU VÀ ĐƯA VÀO DÙNG

Đối chiếu nguồn – đích: số file, số dòng, số khóa khác nhau, số trùng, số ô trống, số dòng nhận / cách ly, số liên kết hỏng, tổng tiền kiểm soát, mọi chênh lệch và lời giải thích → ĐẠT / KHÔNG ĐẠT.

Thử nơi dùng: nhập thử vào phần mềm đích (môi trường thử), chạy báo cáo đang dùng, ca thường – ca lỗi – ca biên; ghi mong đợi và thực tế.

Đưa vào dùng chính thức chỉ khi đạt ngưỡng, đã rà, đã thử nơi dùng, có đường quay lui và người có quyền quyết.

## V. RỦI RO, NGƯỜI RÀ, ĐỀ XUẤT

**6 nhóm rủi ro**: phạm vi và quyền sở hữu nguồn · nghĩa dữ liệu và chuyển đổi · trùng, gộp, bản giữ lại · ngưỡng chất lượng và nguồn đối chứng · dữ liệu cá nhân, lưu giữ, an toàn · nguồn gốc thay đổi, đối chiếu, nơi dùng.

**6 người rà** (doanh nghiệp nhỏ có thể kiêm): người phụ trách nghiệp vụ của dữ liệu · người quản lý dữ liệu của phòng · người làm kỹ thuật / phần mềm · người phụ trách pháp chế – an toàn thông tin · người phụ trách nơi dùng dữ liệu · người kiểm soát nội bộ.

**Đề xuất có thể đưa ra**: rà phạm vi nguồn · rà quy tắc dữ liệu · rà ngưỡng chất lượng · rà danh sách gộp · rà chuyển đổi và cách ly · rà đối chiếu trước khi dùng · rà lưu giữ dữ liệu cá nhân · sửa lại · tạm dừng. Quyết định cuối luôn để trống.

## VI. NGUỒN THAM KHẢO (kiểm tra ngày 22/08/2026)

- ISO 8000-63:2019 — đo lường chất lượng dữ liệu theo quy trình.
- W3C PROV-O — cách ghi nguồn gốc dữ liệu; không bắt buộc dùng đúng định dạng này.
- NIST Privacy Framework — khung tham khảo rủi ro dữ liệu cá nhân; không thay luật, hợp đồng, quy định lưu giữ.

Đây là tham khảo, không phải chứng nhận chất lượng hay tuân thủ. Quy định về dữ liệu cá nhân: đối chiếu văn bản pháp luật hiện hành, cần người có chuyên môn xác nhận.

*[A.I Generated — Claude Code — 30/10/2026]*
