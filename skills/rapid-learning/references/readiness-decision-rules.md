# Readiness decision rules

## 1. Contract trước nội dung

Một lần chạy chỉ có một learner/cohort, một target task, một use moment và một bộ success criteria. Khóa risk, authority, scope/non-goals, knowledge/application thresholds và critical checks trước assessment.

## 2. Bằng chứng tối thiểu

- Baseline có câu trả lời hoặc performance artifact và source ID.
- Required topics được định danh; critical concepts không được score-bù.
- Claim quyết định có source ID/version/date; nguồn phụ thuộc thời điểm phải còn hiệu lực.
- Assessment có unseen case, result source và reviewer khi rủi ro cao.
- Unknowns, guardrails và expiry không được ẩn để nâng state.

## 3. Thứ tự phán quyết

1. Thiếu mission, baseline, thresholds hoặc cấu trúc evidence: NOT_READY.
2. Chưa có assessment: IN_PROGRESS.
3. Result thiếu source hoặc score không hợp lệ: INCONCLUSIVE.
4. Thiếu required topic, trượt critical check hoặc dưới knowledge/application/traceability threshold: REMEDIATE.
5. Đạt điểm nhưng còn critical unknown, guardrail hoặc high-risk chưa được expert review: READY_WITH_GUARDRAILS.
6. Đủ coverage, traceability, critical checks, hai score; không còn critical unknown/guardrail chưa xử lý: READY_FOR_TASK.

State chỉ áp cho target task/version đã khóa. Nó không đồng nghĩa expertise, chứng nhận hay quyền hành động.

## 4. Luật không score-bù

- Critical check trượt không được bù bằng điểm trung bình.
- Knowledge score không bù application score.
- Confidence không bù performance.
- Nhiều link không bù source traceability.
- Case đã học không thay unseen case.

## 5. Recheck

Hết hiệu lực khi task, rule/source, tool/process, learner role hoặc risk thay đổi; khi reviewer phát hiện lỗi critical; hoặc khi assessment bị lộ/bão hòa. Dùng case mới khi retest.
