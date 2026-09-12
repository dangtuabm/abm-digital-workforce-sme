# CHALLENGE FINDING & CLOSURE RULES

## 1. Anatomy của finding

Mỗi finding có: `CHG-ID`, target `CLM/ASM/EVD-ID`, attack hypothesis, mechanism, evidence/counterevidence, falsification/verification test, decision impact, severity, owner, due/closure/status.

## 2. Severity

| Nhãn | Nghĩa |
|---|---|
| BLOCKER | Có thể vi phạm hard gate/authority hoặc tạo downside không chấp nhận; không nên commit trước closure |
| MATERIAL | Nếu đúng có thể đổi recommendation, condition, scope hoặc timing |
| WATCH | Không đổi quyết định hiện tại nhưng cần indicator/trigger |
| CLEARED | Attack đã được adjudicator đóng bằng evidence/control đã kiểm |

Không dùng điểm tổng để che blocker; severity có rationale, không fake precision.

## 3. Response và closure

- `ACCEPTED`: owner công nhận; brief/option/control phải cập nhật.
- `REFUTED`: có evidence trực tiếp và lý do attack không còn đứng vững.
- `MITIGATED`: control có owner, verification, residual risk và trigger.
- `DEFERRED`: chưa đủ evidence; ghi consequence, owner, deadline và quyết định bị khóa/mở.

A.I không tự adjudicate. “Đã có kế hoạch”, “CEO tin”, “team đồng ý” không phải closure evidence.
