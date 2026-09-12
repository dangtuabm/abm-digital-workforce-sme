# SIGNAL DETECTION PROTOCOL

## Đơn vị cơ bản

- Observation: giá trị/sự kiện thô tại source và thời điểm cụ thể.
- Signal: observation hoặc pattern đã qua rule của Watch Contract.
- Alert: signal đạt state/severity cần owner xem trong SLA.

## Kiểm tra trước detection

1. Indicator version, unit, denominator, segment và timezone có khớp contract.
2. Source đủ coverage, chưa stale và không đổi phương pháp.
3. Baseline window đủ đại diện; seasonality/campaign/calendar effect đã ghi.
4. Duplicate và evidence family đã gộp đúng.

## Loại signal

- `EVENT`: sự kiện rời rạc, xác định thời điểm.
- `TREND`: thay đổi cùng hướng, bền qua số kỳ đã chốt.
- `ANOMALY`: lệch khỏi expected band nhưng chưa có nguyên nhân.
- `RUMOR`: assertion chưa đủ authority/corroboration.
- `NOISE`: variation trong expected band hoặc artifact dữ liệu.

## Confirmation và hysteresis

- Confirmation có thể là số kỳ liên tiếp, nguồn độc lập, nguồn chính thức hoặc evidence trực tiếp; phải ghi trong contract.
- Trigger mở và reset đóng phải tách; reset band ngăn alert bật/tắt quanh threshold.
- Một safety trigger có thể bypass confirmation chỉ khi contract nêu rõ owner/SLA.
- Missing/stale data không phải `NO_SIGNAL`; dùng `DATA_GAP` và escalate theo rule riêng.

## State transition

`NO_SIGNAL → OBSERVE → WATCH → ALERT → CLOSED`. Có thể quay về `OBSERVE` khi disproved/reset; mọi chuyển state giữ timestamp, reason, evidence và reviewer.

