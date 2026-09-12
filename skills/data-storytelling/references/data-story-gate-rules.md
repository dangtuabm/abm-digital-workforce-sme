# Data Story Gate Rules

1. Candidate identity is `story_id + version + data_snapshot_hash`.
2. Metric requires formula, unit, baseline/outcome windows, sample, exclusions, source refs and validated delta.
3. Relative delta with zero baseline is invalid. Reported delta must equal recalculation.
4. Insight attribution cannot exceed the measurement contract. Observation and interpretation stay separate.
5. Bar charts start at zero. Every chart states question, fields, scale, sort, source note and alt text.
6. Forbidden flags: `fabricated_data`, `denominator_changed`, `cherry_picked_window`, `causal_overclaim`, `hidden_missing_data`, `hidden_uncertainty`, `truncated_bar_axis`, `unjustified_dual_axis`, `misleading_area`, `fake_render_or_publish`.
7. Required tests: `source_data_contract`, `metric_reconciliation`, `insight_claim_lineage`, `chart_encoding_integrity`, `narrative_consistency`, `accessibility_medium`, `approval_render_boundary`.
8. Engine states: error → `NOT_READY`; clean with final review pending → `READY_FOR_STORY_REVIEW`; all required reviews PASS → `READY_FOR_AUTHORIZED_RENDER`. Engine never renders or publishes.

