# MODEL INTEGRITY RULES

Mỗi driver/equation/output có ID, definition, unit, source/version/date, range, owner và confidence/gap. Phân biệt stock/flow, controllable/exogenous, actual/forecast, nominal/real và timestep.

- Formula chỉ dùng số, names, `+ - * / **`, unary và parentheses; không function, attribute, file hay network.
- Equations chạy theo thứ tự khai báo; dependency chưa có, circularity hoặc division by zero làm model `INVALID`.
- Scenario phải có mọi driver đúng range. Missing không là zero.
- Configurations phải có causal narrative/joint assumptions; không đồng loạt extrema nếu dependencies không cho phép.
- Probability chỉ dùng khi có calibrated data/model và reviewer duyệt; nếu không, scenarios là possibilities.

Validation gồm dimensional review, known-case check nếu có, formula peer review, range/source freshness và reconciliation với source totals.
