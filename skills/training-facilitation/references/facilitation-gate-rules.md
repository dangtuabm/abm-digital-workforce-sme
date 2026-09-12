# Facilitation Gate Rules

Đọc ở Bước 7. Engine kiểm cấu trúc và tính toán; reviewer chịu trách nhiệm về chuyên môn, safety, accessibility, psychological safety và tính khả thi.

## State

- NOT_READY: thiếu source/outcomes/cohort/mode/time/owner/standards hoặc roles.
- DRAFT: contract đủ nhưng chưa có run-of-show.
- REVISE: sai time, coverage, segment protocol, monologue, readiness, incident hoặc measurement.
- READY_WITH_GUARDRAILS: logic đạt nhưng risk cao, expert review/guardrail còn mở.
- READY_FOR_DRY_RUN: gate tĩnh đạt; chưa cho phép mở lớp.

## Gate

1. General segment: id/order/type/duration/owner/accessibility/fallback.
2. Segment không phải break/admin: outcome refs, learner action, evidence, check-for-understanding, facilitation moves và debrief.
3. Mọi outcome được phủ; refs phải hợp lệ.
4. Tổng duration khớp total_minutes trong sai số 0,1 phút.
5. Segment loại input không vượt max_monologue_minutes.
6. Roles có lead facilitator, producer, participant support, incident owner. Một người có thể kiêm nhiệm nhưng role không được ẩn.
7. Readiness có venue/platform, materials, role brief, accessibility check, emergency contacts.
8. Mỗi required incident có trigger, owner, response, stop/escalate threshold và fallback.
9. Measurement có time drift, participation distribution, evidence completion, unanswered questions, incidents, commitments và result owner.
10. Risk cao, expert_review != approved hoặc guardrail mở không được vượt READY_WITH_GUARDRAILS.

## Quy tắc vận hành

- READY_FOR_DRY_RUN không đồng nghĩa READY_FOR_PILOT; dry-run reviewer phải duyệt actual timing, role load và recovery.
- Break/admin tính vào tổng phút nhưng không phải nối learning outcome.
- Engine không đo psychological safety hay facilitation quality thật; cần observation evidence.
