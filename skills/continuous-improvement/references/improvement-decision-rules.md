# IMPROVEMENT DECISION RULES

## Cổng trước thử nghiệm

- Problem/baseline/metric definition, measurement system, owner và process version phải khóa.
- Hypothesis có mechanism, prediction, falsification criterion và alternative explanation.
- Change có scope, comparison/control logic, sample/window, primary metric, countermetrics, acceptance, stop/rollback và approval.
- Baseline không ổn định hoặc measurement không đáng tin: `NOT_READY`; không gán mọi biến động cho change.

## Trạng thái sau đo

- `ADOPT`: primary acceptance đạt; countermetrics/red lines không vi phạm; evidence window đủ; effect có practical significance và owner duyệt.
- `ITERATE`: signal hữu ích nhưng hypothesis/change/measurement cần sửa; giữ version và learning.
- `REJECT`: evidence bác hypothesis/change hoặc benefit không đủ điều kiện áp dụng.
- `ROLLBACK`: red line/countermetric/stop rule bị vi phạm hoặc downside vượt tolerance.
- `INCONCLUSIVE`: sample/window/data quality không đủ; không gọi thắng/thua.

Không p-hack, cherry-pick segment/time window, đổi metric/target sau khi thấy result hoặc chạy đồng thời nhiều changes không thể attribution. Standardization cần SOP/version, training, control plan, owner, audit date và reopen trigger; không tự scale/publish/đổi production.
