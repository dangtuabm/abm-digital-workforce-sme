# COMMITMENT AND ACTION RUBRIC

## Phân biệt ba lớp

| Lớp | Điều kiện | Cách ghi |
|---|---|---|
| `EXPLICIT` commitment | Chủ thể nhận làm outcome cụ thể bằng ngôn ngữ rõ | Owner + outcome + due/raw due + MSG-ID |
| `INFERRED` commitment | Ngữ cảnh gợi ý nhưng không có lời nhận rõ | Không tạo action chắc chắn; đưa clarification queue |
| `NONE` | Ý kiến, mong muốn, lịch sự, dự kiến hoặc thông tin | Không gán owner |

Ví dụ `EXPLICIT`: “Lan sẽ gửi bảng giá trước 16:00 thứ Sáu.”  
Ví dụ `INFERRED`: “Để tôi xem”, “có lẽ bên tôi xử lý được”, “hy vọng xong sớm.”  
Ví dụ `NONE`: “Nên có bảng giá”, “cảm ơn”, “đã nhận thông tin.”

## Action row tối thiểu

`action_id`, outcome, owner canonical/raw, due raw/normalized, dependency, waiting_on, status, next checkpoint, decision link, `msg_id`, confidence class và reviewer note.

## Open loop

Tạo open loop khi có câu hỏi chưa trả lời, tài liệu hứa nhưng chưa thấy evidence, blocker chưa owner, decision pending hoặc action quá hạn/chưa status. Không tự đóng loop vì thread im lặng.

## Deadline và owner mơ hồ

- “Chúng ta”, “bên em”, “mọi người”: giữ raw owner, gắn `UNRESOLVED` trừ khi rule cho phép.
- “Mai”, “cuối tuần”, “sớm”: giữ raw; chỉ normalize khi timestamp/timezone và quy ước lịch rõ.
- Nếu hai message gán owner/due khác, giữ conflict và chờ authority rule; không chọn bản thuận tiện.

