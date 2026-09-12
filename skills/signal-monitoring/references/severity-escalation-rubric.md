# SEVERITY AND ESCALATION RUBRIC

## Bốn chiều không được trộn

| Chiều | Câu hỏi |
|---|---|
| Impact | Nếu signal đúng, mức ảnh hưởng đến mục tiêu/đối tượng là gì? |
| Urgency | Cửa sổ hành động còn bao lâu? |
| Confidence | Evidence xác nhận signal mạnh đến đâu? |
| Reversibility | Response có thể đảo ngược và chi phí sai là gì? |

## Severity gợi ý

- `S1 INFORMATIONAL`: không đổi quyết định; lưu và xem ở cadence thường.
- `S2 WATCH`: có thể đổi giả định; owner kiểm trong SLA chuẩn.
- `S3 MATERIAL`: có thể đổi kế hoạch/quyết định; reviewer xem sớm.
- `S4 CRITICAL`: safety/pháp lý/tài chính/danh tiếng trọng yếu với cửa sổ ngắn; áp playbook đã duyệt, không tự hành động.

Mỗi tổ chức phải map S1–S4 sang impact, owner, SLA và kênh cụ thể. Không nâng severity vì tin lan truyền mạnh; không hạ vì confidence thấp nếu downside lớn.

## Alert quality

Alert đạt chuẩn cần: signal ID, what changed, baseline/expected band, evidence/counterevidence, confirmation, impact, urgency, confidence rationale, affected object, owner, SLA, next verification, response options, approval status và source pointers.

