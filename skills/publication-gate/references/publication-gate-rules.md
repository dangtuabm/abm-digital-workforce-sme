# Publication Gate Rules

## 1. Decision invariants

1. Candidate identity is `artifact_id + version + content_hash`; any change requires a new gate result.
2. A claim passes only when its active evidence supports the exact wording, scope, date and qualification.
3. Rights or consent status other than `APPROVED` is blocking for the affected material.
4. `N_A` is valid only with rationale, reviewer and evidence that the control does not apply.
5. `BLOCKER` and `MAJOR` cannot be accepted by the engine. A `MINOR` accepted risk needs authority, expiry and mitigation.
6. A disclaimer cannot cure a false claim, privacy/security breach, missing rights or mandatory legal duty.
7. The engine never signs, approves, publishes, sends or deploys.

## 2. Required controls

`IDENTITY`, `ACCURACY`, `CLARITY_USEFULNESS`, `BRAND_DISCLOSURE`, `LEGAL_COMPLIANCE`, `PRIVACY_SECURITY`, `IP_RIGHTS`, `ACCESSIBILITY`, `CHANNEL_TECHNICAL`, `RELEASE_OPERATIONS`.

Each control records `result`, `evidence_refs`, `reviewer`, `date`; `N_A` also records `rationale`.

## 3. Severity

- `BLOCKER`: credible risk of falsehood, unlawful/non-compliant release, privacy/security harm, missing rights/consent, unsafe instruction, wrong artifact or no rollback for material harm.
- `MAJOR`: materially misleads the audience, breaks required brand/disclosure/accessibility/channel behavior or prevents intended use.
- `MINOR`: localized issue that does not change meaning, rights, safety or release integrity.

## 4. State rules

- Structural/control/claim/right/consent error, open blocker or open major → `NOT_READY`.
- Only open minor defects with owner/fix/retest plan → `READY_FOR_REMEDIATION`.
- No errors/open defects; all non-final reviews PASS; final review PENDING → `READY_FOR_HUMAN_RELEASE_DECISION`.
- All required reviews PASS with evidence → `READY_FOR_AUTHORIZED_RELEASE`; execution remains human-owned.

## 5. Required test types

`candidate_identity`, `claim_evidence`, `rights_consent_disclosure`, `content_quality`, `privacy_security_accessibility`, `channel_release_operations`, `approval_publication_boundary`.

