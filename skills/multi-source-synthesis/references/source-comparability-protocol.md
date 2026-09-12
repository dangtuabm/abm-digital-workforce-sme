# SOURCE COMPARABILITY PROTOCOL

## Mục đích

Quyết định claim nào có thể đặt cạnh, đối chiếu hoặc gộp mà không làm sai nghĩa.

## Bảy trục bắt buộc

| Trục | Câu hỏi kiểm tra | Sai lệch thường gặp |
|---|---|---|
| Construct | Hai nguồn có đo cùng khái niệm không? | "Doanh thu" so với "GMV" |
| Definition | Công thức và inclusion/exclusion có giống không? | Có/không VAT, hoàn trả, nội bộ |
| Unit và denominator | Đơn vị, tỷ giá, mẫu số có giống không? | % trên khách hàng so với % trên đơn hàng |
| Population và scope | Đối tượng, ngành, kênh, địa lý có khớp không? | SME toàn quốc so với startup Hà Nội |
| Time và version | Kỳ đo, cutoff và phiên bản có khớp không? | Chính sách cũ so với bản hiệu lực mới |
| Method | Cách lấy mẫu, thu thập và xử lý có tương thích không? | Survey tự chọn so với dữ liệu giao dịch |
| Granularity | Grain và cấp tổng hợp có giống không? | Chi nhánh so với toàn công ty |

## Trạng thái

- `COMPARABLE`: bảy trục tương thích hoặc có quy tắc quy đổi được duyệt; được gộp theo contract.
- `PARTIALLY_COMPARABLE`: chỉ so được một phần; ghi trục hợp lệ/không hợp lệ; không gộp thành một số.
- `NOT_COMPARABLE`: khác biệt làm đổi ý nghĩa; trình bày song song và giải thích.
- `UNKNOWN`: thiếu metadata; đưa vào gap và yêu cầu owner bổ sung.

## Quy tắc vận hành

1. So metadata trước value; số giống nhau không chứng minh comparability.
2. Giữ raw value và định nghĩa nguồn; normalization tạo trường mới, không ghi đè.
3. Mọi quy đổi phải có rule, owner, version và giả định.
4. Không nội suy thời kỳ, population hoặc denominator để lấp gap.
5. Sai lệch làm đổi quyết định là material conflict và chuyển người duyệt.

## Traceability tối thiểu

Mỗi claim cần: `claim_id`, `src_id`, source pointer, raw statement/value, definition, scope, time, method, comparability status, reason và reviewer note.

