# Practice & Feedback Gate Rules

Đọc ở Bước 7. Engine lint cấu trúc, tính score và stage mastery; reviewer chịu trách nhiệm về validity, domain accuracy, bias, safety và quyết định high-stakes.

## State

- NOT_READY: thiếu contract, rubric, threshold/owner/standards.
- DRAFT: contract/rubric đủ nhưng chưa có task.
- REVISE: weight/stage/task/calibration/attempt/feedback/measurement lỗi.
- READY_FOR_PRACTICE: control pack đạt, chưa có attempt.
- MASTERY_NOT_YET: có attempt hợp lệ nhưng chưa đạt required stages.
- MASTERY_EVIDENCED: required independent/transfer stages đạt threshold, không critical error.
- READY_WITH_GUARDRAILS: logic đạt nhưng risk cao, expert review hoặc guardrail còn mở.

## Gate

1. Rubric criterion: id, weight, observable, pass/failure anchors; ID duy nhất; tổng weight 100 ±0,1.
2. Task: id/stage/instructions/evidence/conditions/difficulty/feedback timing/accessibility/safety/data minimization/owner.
3. Task ladder phủ required stages; task ID duy nhất.
4. Calibration có examples, adjudication rule và owner.
5. Attempt trỏ task tồn tại, đóng evidence ref, scale max, đủ criterion scores, critical errors, reviewer và feedback.
6. Score = tổng weight × criterion score/scale max; score nằm 0–100.
7. Feedback có evidence, diagnosis, priority, next task và confidence.
8. Mastery chỉ khi mỗi mastery-required stage có ít nhất một attempt đạt threshold và không critical error.
9. Vượt max attempts phải revise/escalate, không lặp vô hạn.
10. Measurement có baseline/latest, attempts-to-mastery, error recurrence, transfer, evaluator agreement và result owner.

## Giới hạn

- Synthetic self-test chỉ kiểm engine, không chứng minh learner mastery.
- Score không hợp lệ nếu source/rubric/submission version hoặc evidence thiếu.
- Cùng task/item có thể chứng minh correction nhưng không tự chứng minh transfer.
