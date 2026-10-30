# QUY TẮC HỢP ĐỒNG TRÍCH XUẤT

## 1. Chốt "một dòng là gì"

Viết đúng một câu: **"Mỗi dòng đại diện cho một [chứng từ/sự việc] duy nhất, nhận biết bằng [khóa]."**

| Tình huống | Cách chốt đúng | Lỗi hay gặp |
|---|---|---|
| Hóa đơn mua vào | Hoặc một dòng = một hóa đơn, hoặc một dòng = một dòng hàng; nếu cần cả hai thì làm hai bảng cha–con | Trộn trường của hóa đơn với trường của dòng hàng trong cùng một dòng |
| Biểu mẫu, phiếu khảo sát | Một dòng = một phiếu; phần lặp (nhiều người, nhiều món) tách bảng con | Nhân bản thông tin chung cho từng dòng lặp |
| Hồ sơ nhiều trang | Một dòng = một hồ sơ theo mã gốc | Coi mỗi trang là một dòng |
| Bảng trong PDF | Một dòng logic, không nhất thiết một dòng hình học | Ô xuống dòng bị tách thành dòng mới |

## 2. Mô tả từng trường

Mỗi trường ghi:
- tên cột (chữ thường, không dấu) và nghĩa nghiệp vụ;
- kiểu: chữ, số nguyên, số thập phân, ngày, có/không, danh mục;
- bắt buộc / tùy chọn / có điều kiện;
- lặp hay không, thuộc bảng cha hay bảng con;
- lấy ở đâu trên chứng từ;
- quy tắc chuẩn hóa và đơn vị;
- giá trị cho phép hoặc khoảng hợp lệ (nếu có căn cứ);
- cách xử lý khi thiếu và người xử lý ngoại lệ;
- ví dụ đúng/sai đã được duyệt (nếu có).

## 3. Giá trị gốc, giá trị chuẩn và trạng thái

- **Giá trị gốc**: đúng như chứng từ hoặc như công cụ đọc được, không "làm đẹp".
- **Giá trị chuẩn**: sau khi áp quy tắc; nằm ở cột riêng, không thay giá trị gốc.
- **Vị trí nguồn**: file + trang/vùng/bảng/dòng/ô.
- **Cách đọc**: lớp chữ có sẵn, đọc ảnh scan, đọc bảng, người nhập tay xác nhận.
- **Trạng thái**:
  - KHỚP NGUỒN — đọc rõ, đúng định dạng;
  - CẦN SOÁT — đọc từ ảnh, có ký tự dễ nhầm (0/O, 1/l, 5/S, mất dấu);
  - MƠ HỒ — có hai cách hiểu (ví dụ ngày 03/04 khi chưa chốt kiểu ngày);
  - THIẾU — chứng từ không có hoặc không đọc được;
  - SAI ĐỊNH DẠNG — có giá trị nhưng không khớp kiểu/quy tắc.

Chỉ dùng "% độ tin cậy" khi công cụ đã được kiểm trên cùng loại chứng từ. Nếu không, trạng thái bằng lời có căn cứ tốt hơn một con số phần trăm giả.

## 4. Quy tắc ô thiếu

Phân biệt rõ, không dùng ô trống cho mọi trường hợp:
- KHÔNG CÓ TRÊN CHỨNG TỪ — nguồn không ghi;
- KHÔNG ĐỌC ĐƯỢC — có nhưng mờ, rách, che;
- KHÔNG ÁP DỤNG — trường không áp cho dòng này theo quy tắc;
- CHƯA ĐƯỢC GIAO — cần phụ lục/chứng từ kèm mà chưa có;
- SAI ĐỊNH DẠNG — có giá trị gốc nhưng không chuyển được.

## 5. Chuẩn hóa theo quy ước Việt Nam

- **Ngày**: chứng từ Việt Nam thường ghi dd/mm/yyyy. Chỉ chuyển sang yyyy-mm-dd khi quy tắc đã chốt kiểu ngày; ngày có thể hiểu hai cách thì để MƠ HỒ.
- **Số tiền**: "12.650.000" là mười hai triệu sáu trăm năm mươi nghìn (dấu chấm phân cách hàng nghìn, dấu phẩy là phần thập phân). Không xóa dấu theo cảm tính; ghi đơn vị tiền ở cột riêng.
- **Quy đổi ngoại tệ**: chỉ khi có quy tắc, tỷ giá và ngày áp dụng đã chốt.
- **Mã số thuế, số hóa đơn, mã hàng, số điện thoại**: lưu dạng chữ, giữ số 0 ở đầu; không ép thành số.
- **Danh mục** (đơn vị tính, loại chi phí): chỉ ánh xạ theo bảng ánh xạ đã duyệt; không tự gộp "cái", "chiếc", "bộ".
- **Có/không**: chỉ chuyển theo cụm từ đã chốt; ô trống không có nghĩa là "không".
- **Thuế suất, tiền thuế**: giữ đúng như in trên hóa đơn; việc kiểm đúng sai thuế suất là việc khác.

## 6. Không áp dụng

- Bộ trường đổi giữa các lô thì tăng phiên bản; không trộn kết quả hai phiên bản.
- Quy tắc của một nhà cung cấp/một mẫu hóa đơn không tự áp cho mẫu khác.
- Hai nguồn khác nhau cho cùng một giá trị không được "giải quyết" bằng chọn bản mới hơn; đưa vào Sổ ngoại lệ.

*[A.I Generated — Claude Code — 30/10/2026]*
