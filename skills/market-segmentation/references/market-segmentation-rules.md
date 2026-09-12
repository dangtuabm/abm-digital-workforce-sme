# Market Segmentation Rules

## Segment quality

A segment is not merely a label. It needs a reproducible membership rule and evidence that it is measurable, substantial for the stated objective, differentiable in response/need, accessible within lawful channels, actionable with available capability and sufficiently stable for the decision horizon.

## Coverage and membership

Declare the population frame, unit of analysis, denominator, inclusion/exclusion, unknown/unassigned policy, overlap policy and outlier handling. A model can be mutually exclusive or overlapping; it must state which and reconcile coverage.

## Evidence and estimates

Use `FACT`, `ESTIMATE`, `HYPOTHESIS`, `UNKNOWN`. Size, growth, willingness-to-pay, access and economics need source, method, range and confidence. CRM share is observed-customer share, not automatically market share.

## Scoring

Define criteria, scale direction, weights, normalization, missing-data rule and thresholds before scoring. Run alternative weights and sensitivity around material estimates. A rank is decision support, not authorization.

## Privacy and fairness

Do not use protected/sensitive traits or proxies. Apply purpose limitation, minimum cell size and aggregation. Do not expose row-level identities or use the model for high-impact eligibility, discriminatory exclusion or individual manipulation.

## State policy

Publishable states: `NOT_READY`, `READY_FOR_SEGMENT_REVIEW`, `READY_FOR_HUMAN_SEGMENT_DECISION`. Execution states `TARGETED`, `EXCLUDED`, `FUNDED`, `PRICED`, `CONTACTED`, `LAUNCHED`, `EXITED`, `APPROVED` require external human evidence.
