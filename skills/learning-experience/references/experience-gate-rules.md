# Experience Gate Rules

Đọc file này ở Bước 7 trước khi chạy engine. Ngưỡng phải đến từ Experience Contract, không mặc định biến các khuyến nghị ABM thành luật cho mọi khách hàng.

## State

- `NOT_READY`: thiếu curriculum/outcome, cohort/mode/time, standards hoặc owner.
- `DRAFT`: contract đủ nhưng chưa có touchpoint.
- `REVISE`: có blueprint nhưng sai phase, mapping, time, format, moment, ownership, accessibility, fallback, service hoặc measurement.
- `READY_WITH_GUARDRAILS`: logic đạt nhưng high-risk/expert review hoặc guardrail còn mở.
- `READY_FOR_PILOT`: toàn bộ gate tĩnh đạt; chưa chứng minh effectiveness và chưa cho phép release.

## Các gate bắt buộc

1. Required phases trong contract đều có touchpoint.
2. Mỗi learning outcome có ít nhất một touchpoint; mỗi touchpoint trỏ outcome hợp lệ.
3. Tổng `duration_minutes` của phase `during` khớp `total_during_minutes` trong sai số 0,1 phút.
4. Số format khác nhau ở phase `during` đạt `min_format_variety`.
5. Tổng thời lượng liên tiếp của cùng format không vượt `max_same_format_minutes`; thứ tự lấy theo `order`.
6. Mỗi `required_moment` có ít nhất một moment trỏ tới touchpoint tồn tại.
7. Mỗi touchpoint có learner action, feedback, owner, accessibility và fallback.
8. Service blueprint có facilitator, platform, support, assets, incident recovery và data privacy.
9. Measurement có đủ engagement behavior, learning evidence, application signal, feedback source và result owner.
10. High-risk hoặc `expert_review=pending` không thể vượt `READY_WITH_GUARDRAILS`.

## Diễn giải

- Format variety là cơ chế chống đơn điệu, không phải mục tiêu học tập.
- Peak/Valley/Commitment/Shareable chỉ bắt buộc nếu được ghi trong `required_moments`.
- Một touchpoint có thể phục vụ nhiều outcomes nhưng phải chỉ rõ bằng mảng `outcome_refs`.
- Engine lint cấu trúc; reviewer vẫn phải duyệt accuracy, safety, accessibility và tính khả thi.
