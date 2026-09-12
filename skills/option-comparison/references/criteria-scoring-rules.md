# CRITERIA & SCORING RULES

## 1. Criteria contract

Mỗi criterion có: `CRT-ID`, definition, decision relevance, direction, raw unit, scope/horizon, anchor 0/50/100, weight, evidence threshold, owner/version. Khóa trước khi thấy option totals.

- Hard gate là non-compensatory; để riêng, không weight.
- Tránh double count: nếu hai criteria cùng đo một outcome, gộp hoặc giải thích causal distinction.
- Weight thể hiện trade-off đã duyệt; tổng score weights phải bằng `1.00`.
- Qualitative score cần behavioral anchor; không đổi tính từ thành số tùy ý.

## 2. Evidence-to-score

- Giữ raw value và mapping; normalized score chỉ 0–100.
- `MISSING/UNKNOWN` không là 0 và không tự impute.
- Mỗi score có `EVD-ID`, base/low/high và `0 ≤ low ≤ base ≤ high ≤ 100`.
- Chỉ option pass mọi hard gate và đủ material scores mới `COMPARABLE`.

## 3. Weighted result

`total = Σ(weight × normalized score)`. Tính riêng low/base/high bằng cùng weights. Lưu input, tool version và output; không làm tròn trung gian để đổi rank.
