# DECISION REVIEW & LEARNING RULES

## 1. Freeze before outcome

Review phải trỏ tới decision record/version được lưu trước khi outcome rõ: question, owner, context, options/status quo, evidence, assumptions, expected outcomes/ranges, confidence/probability nếu có, risks, recommendation, rationale, dissent, conditions và review date. Không sửa record gốc; correction tạo version mới và giữ diff.

## 2. Tách chất lượng khỏi kết quả

| Decision process | Outcome | Diễn giải hợp lệ |
|---|---|---|
| Tốt | Tốt | Có thể là skill + favorable conditions; vẫn kiểm luck |
| Tốt | Xấu | Không tự kết luận quyết định tồi; kiểm tail risk/exogenous change |
| Kém | Tốt | Không thưởng quy trình kém vì may mắn |
| Kém | Xấu | Kiểm process failure và external contribution riêng |

Decision quality xét information available **tại thời điểm quyết định**, không dùng dữ liệu biết sau để kết tội. Outcome quality xét actual so với expected/target/range bằng source/version/time/segment.

## 3. Attribution

Mỗi variance có `VAR-ID`, expected, actual, delta, source, mechanism hypothesis, evidence/counterevidence và nhãn: `DECISION_LOGIC / EXECUTION / ASSUMPTION / EXOGENOUS / MEASUREMENT / LUCK_OR_UNRESOLVED`. Không ép tổng attribution thành 100% nếu evidence không cho phép; correlation không là cause.

## 4. Calibration

Chỉ tính calibration khi record có probability/confidence được định nghĩa trước outcome. Giữ numerator/denominator và cohort đủ tương đồng; một case không chứng minh calibration. Không tạo probability hồi tố.

## 5. Learning và memory promotion

- `CASE_LESSON`: gắn riêng decision/context/version.
- `HYPOTHESIS`: có mechanism khả dĩ nhưng cần test/case khác.
- `REUSABLE_PATTERN_CANDIDATE`: lặp lại qua cases với evidence/conditions/limits.
- `PROMOTED_ASSET`: chỉ sau owner/reviewer approval, provenance, applicability, expiry/review trigger và rollback.

Không biến blame, allegation, personal trait hoặc một outcome đơn lẻ thành organizational truth.
