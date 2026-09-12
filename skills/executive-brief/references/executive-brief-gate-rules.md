# Executive Brief Gate Rules

1. Brief identity is `brief_id + version + as_of + snapshot_hash`.
2. Active source needs owner, observed time, age and SLA. `age_hours > freshness_sla_hours` is stale and cannot support a current claim.
3. Every `CRITICAL` signal and decision due within the horizon must appear on the front page. Max-item limits never justify critical omission.
4. Metric exception needs actual, threshold, direction, denominator, window and source; reported breach must match recalculation.
5. Decision request needs 2–3 real options, one explicit recommendation, evidence, owner, deadline, delay harm and reversibility.
6. Forbidden flags: `fabricated_signal`, `hidden_bad_news`, `downgraded_severity`, `stale_as_current`, `vanity_metric`, `false_approval`, `false_decision`, `false_delivery`.
7. Required tests: `source_freshness`, `metric_exception`, `critical_front_page_coverage`, `decision_recommendation`, `bad_news_unknown_integrity`, `privacy_distribution`, `approval_delivery_boundary`.
8. Errors → `NOT_READY`; clean with final review pending → `READY_FOR_EXECUTIVE_REVIEW`; all reviews PASS → `READY_FOR_AUTHORIZED_DELIVERY`. Engine never decides or sends.

