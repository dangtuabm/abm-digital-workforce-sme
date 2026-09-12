# People Signal Diagnostic Control Rules

## Purpose and privacy

- Purpose, lawful basis/consent, population, retention, allowed/prohibited use và correction route phải khóa trước dữ liệu.
- Output chỉ ở cohort/group level; không individual score/profile/watchlist.
- Không covert surveillance, private communication mining, emotion/personality/intent/health/burnout/flight-risk inference.
- Protected traits chỉ được dùng trong fairness audit hợp pháp bởi reviewer có quyền; không cho diagnostic score hoặc adverse action.

## Data and cohort

- Source có version/locator/access/freshness/coverage/quality; missing/stale/denied phải hiển thị.
- Metric có definition/formula/unit/grain/window/denominator/allowed aggregation.
- Cohort count phải đạt contract minimum; intersection có re-identification risk phải suppress/merge theo policy.
- So sánh cần kiểm role mix, exposure, demand, seasonality, staffing, process/system change và selection bias.

## Inference and action

- Signal là observation; hypothesis phải có alternatives, confounders, evidence for/against, confidence và falsifiable question.
- Correlation không là cause. Không label “burnout”, “disengaged”, “flight risk”, “toxic”, “low potential”.
- Chỉ đề xuất support experiment cấp hệ thống/nhóm; không adverse people recommendation.
- Mọi output mang nhãn `[A.I Suggested]` và chờ human review.

## Forbidden controls

Flags: `identity_exposed`, `individual_scored`, `reidentified`, `small_cohort_exposed`, `protected_trait_used`, `private_message_mined`, `covert_surveillance`, `emotion_inferred`, `personality_inferred`, `intent_inferred`, `diagnosis_made`, `burnout_labeled`, `flight_risk_labeled`, `source_fabricated`, `metric_cherry_picked`, `denominator_hidden`, `missingness_hidden`, `confounder_ignored`, `correlation_as_causation`, `adverse_action_recommended`, `auto_alerted`, `auto_case_opened`, `auto_rated`, `auto_disciplined`, `auto_promoted`, `auto_terminated`, `hr_file_updated`.

States: `ALERTED`, `CASE_OPENED`, `SCORED`, `RATED`, `DISCIPLINED`, `PROMOTED`, `TERMINATED`, `HR_FILE_UPDATED`, `APPROVED`.

Reviews: `PEOPLE_ANALYTICS`, `PRIVACY_LEGAL`, `DOMAIN_MANAGER` phải PASS; `FINAL_HUMAN_PEOPLE_REVIEW` phải PENDING.
