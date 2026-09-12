# COMPARABILITY & SENSITIVITY RULES

## 1. Comparable data checklist

So khớp definition, population/volume, geography, time window, unit, currency/base date, tax, inflation, CapEx/OpEx, gross/net, actual/forecast, confidence và dependencies. Mọi transform có công thức/source.

## 2. Comparison states

- `COMPARABLE`: gates pass; material cells có comparable evidence và approved mapping/weights.
- `PROVISIONAL`: có gap/uncertainty nhưng vẫn thấy conditional trade-off; không claim winner chắc chắn.
- `NOT_COMPARABLE`: option/scope/gate/criterion chưa khóa, gate unknown hoặc missing material data.

## 3. Sensitivity

- Tính low/base/high cho mỗi option.
- `STABLE` chỉ khi top option low lớn hơn mọi competitor high trong dải đã duyệt.
- Nếu intervals overlap hoặc plausible weight/input change đảo rank: `UNSTABLE/TIED/CONDITIONAL`.
- Nêu flip point: weight/input/assumption nhỏ nhất làm recommendation đổi; không bịa probability.
- Pareto dominance chỉ khi option không kém ở mọi material criterion và tốt hơn ít nhất một criterion trên evidence comparable.

Nếu cần nhiều future states/correlation/dynamic path, handoff `scenario-modeling`; comparison chỉ tiêu thụ output/version.
