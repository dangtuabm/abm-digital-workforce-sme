# CONVERSATION STATE PROTOCOL

## Message inventory

Mỗi message cần: `thread_id`, `msg_id`, channel, sender raw/canonical, timestamp raw/UTC nếu biết, topic, reply-to, quoted/forwarded flag, attachment, scope và read status.

## Chuẩn hóa

1. Giữ timestamp gốc; tạo timestamp chuẩn ở trường mới.
2. Map alias bằng bảng có owner xác nhận; không gộp người chỉ vì tên giống.
3. Tách text mới khỏi quoted/forwarded block, signature, disclaimer và bot notification.
4. Message được quote lại giữ pointer về message gốc; không tạo event/commitment trùng.
5. Thread split/merge phải có rule và ghi source relation.

## Decision state

- `PROPOSED`: phương án được nêu nhưng chưa có phê duyệt rõ.
- `DECIDED`: người có thẩm quyền chấp thuận/quyết định rõ.
- `DISPUTED`: có phản đối chưa giải quyết.
- `SUPERSEDED`: message sau thay state; giữ pointer hai chiều.
- `REVOKED`: quyết định/cam kết bị thu hồi rõ.
- `UNRESOLVED`: thiếu evidence, authority hoặc context.

Không dùng số đông, im lặng, emoji reaction hoặc “nghe hợp lý” để nâng `PROPOSED` thành `DECIDED` nếu taxonomy tổ chức chưa quy định.

## Timeline rules

- Sắp theo instant tuyệt đối nếu có timezone; nếu không, giữ local time và cảnh báo.
- Deadline tương đối neo vào timestamp của message và timezone người nói/kênh.
- Message edited giữ version nếu export có; bản cũ không là state hiện hành nhưng còn audit history.
- Gap do export thiếu/xóa phải xuất hiện trong coverage note.

