# Customer Profile Rules

## 1. Claim taxonomy

- `FACT`: directly supported by an authorized source.
- `ESTIMATE`: method, range, source and uncertainty are visible.
- `HYPOTHESIS`: material claim awaiting validation; evidence for and against retained.
- `UNKNOWN`: no adequate evidence; convert to a discovery question.

Do not downgrade an UNKNOWN to a confident narrative. Profile usefulness is not measured by filled fields.

## 2. Entity resolution

Use at least two stable keys where practical: legal/trading name, domain, geography, registration/public identifier, parent/subsidiary or brand relation. Record ambiguity instead of merging namesakes.

## 3. Buying context

- Role labels describe participation, not verified authority.
- Budget, timeline, intent and priority require evidence.
- A public event is a signal with alternative explanations, not proof of buying readiness.
- Generic industry pain is context, not a fact about a customer.

## 4. Privacy and fairness

Use purpose limitation and data minimization. Exclude protected/sensitive traits, health, family, beliefs, sexual life, precise location, private contacts, vulnerabilities and unrelated personal activity. Do not infer psychology or manipulate personal fear. Do not use a profile for employment, credit, insurance or other high-impact eligibility.

## 5. Reviews

Required reviews are `DOMAIN_ENTITY`, `DATA_PRIVACY`, `COMMERCIAL_USE` and `FINAL_HUMAN_CUSTOMER_USE_DECISION`. Legal/security review is added when source terms, personal data, confidentiality or regulated context require it. Final decision remains `PENDING` in the artifact.

## 6. State policy

Publishable states: `NOT_READY`, `READY_FOR_CUSTOMER_PROFILE_REVIEW`, `READY_FOR_HUMAN_CUSTOMER_USE_DECISION`. Execution states such as `SCORED`, `TARGETED`, `PERSONALIZED`, `CONTACTED`, `ENRICHED`, `DISQUALIFIED`, `APPROVED` are forbidden without external human evidence.
