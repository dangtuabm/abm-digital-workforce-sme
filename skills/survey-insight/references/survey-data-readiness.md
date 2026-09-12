# SURVEY DATA READINESS

## Flow reconciliation

Giữ riêng: invitations/delivered, starts, completes, partials, screen-outs, quota-full, duplicates, test records, invalid/excluded và unknown disposition. Chỉ tính response/complete rate theo denominator đã định nghĩa; không dùng từ “response rate” khi không có invitation/frame denominator.

## Gate checks

1. Instrument/question IDs, scale, coding và skip logic đúng version.
2. Types/ranges/labels/missing codes khớp codebook; missing không thành zero.
3. Response ID uniqueness, duplicate rule và exclusion reason có owner.
4. Impossible path, contradictory answer, speed/straightline và bot/test flag được ghi; flag không mặc nhiên là loại.
5. Weight có coverage, extreme-weight review, calibration source và version.
6. Open text encoding/language, consent, PII và redaction đã kiểm.
7. Flow counts và dataset rows reconcile.

## Phán quyết

- `PASS`: đủ để chạy analysis contract; issue không làm đổi headline.
- `CONDITIONAL`: chạy được phần xác định; issue/limit phải theo metric/segment.
- `FAIL`: thiếu instrument/version, base, flow hoặc lỗi làm metric không diễn giải được; dừng headline analysis.

Mỗi repair/exclusion cần rule, before/after count, affected metrics, owner, approval và reproducible evidence.

