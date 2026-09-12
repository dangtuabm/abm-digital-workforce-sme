# EXECUTION CONTROL RULES

## Status evidence

- `NOT_STARTED`: start condition chưa đạt hoặc chưa tới window.
- `ON_TRACK`: acceptance evidence và forecast cho thấy target/milestone trong tolerance đã duyệt.
- `AT_RISK`: leading indicator/assumption/dependency vượt watch threshold; action/decision owner rõ.
- `OFF_TRACK`: milestone/KR forecast miss threshold; cần decision, không chỉ recovery promise.
- `BLOCKED`: dependency/authority/resource/evidence chặn next acceptance event.
- `DONE`: acceptance criteria được independent evidence xác nhận; activity complete không đủ.

Mỗi status có `as_of`, `EVD-ID`, variance/forecast, reason, next evidence/decision. Stale evidence hạ confidence; không tự giữ green.

## Cadence và exception

Cadence bàn exceptions/decisions: new evidence, variance, dependency, assumption, risk, decision needed, owner/deadline. Thay target, resource, scope, owner, stop/pivot/reallocate cần approval/version. Giữ decision/adaptation log và outcome link.
