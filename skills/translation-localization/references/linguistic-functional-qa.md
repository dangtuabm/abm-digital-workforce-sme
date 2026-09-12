# LINGUISTIC AND FUNCTIONAL QA

## Lỗi và severity

| Nhóm | Ví dụ | Blocking mặc định |
|---|---|---|
| Accuracy | Sai meaning, omission, addition, wrong claim/number | Có |
| Terminology | Vi phạm approved/forbidden/do-not-translate | Có với term trọng yếu |
| Locale | Sai date, decimal, currency, unit, xưng hô | Tùy impact |
| Functional | Mất placeholder/tag/link, plural lỗi, target rỗng | Có |
| Fluency/style | Ngữ pháp, tự nhiên, tone, consistency | Tùy kênh |
| Layout | Overflow, truncation, bidi, line break, font | Có nếu mất nghĩa/chức năng |
| Compliance | Legal/safety warning sai hoặc thiếu | Có; expert review |

## Review sequence

1. Deterministic QA trước để loại lỗi parity/coverage.
2. Bilingual review theo source–target–context, không chỉ đọc target.
3. Terminology/consistency check toàn package.
4. In-context rendering hoặc screenshot review cho UI/layout.
5. Reviewer nghiệp vụ cho high-risk claim/term.
6. Regression check các segment bị sửa và segment dùng cùng term/placeholder.

## Evidence

Mỗi issue cần `issue_id`, `SEG-ID`, category, severity, source/target excerpt tối thiểu, rule violated, proposed fix, owner, resolution, reviewer và retest evidence.

Back-translation có thể phát hiện lệch lớn nhưng không chứng minh target tự nhiên, đúng term hay chạy đúng giao diện; không dùng làm gate duy nhất.

