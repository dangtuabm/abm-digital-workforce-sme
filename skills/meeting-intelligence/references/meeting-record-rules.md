# Meeting Evidence Record Rules

1. Evidence source needs ID/version/hash/locator/owner/capture method/time span/access/consent and remains immutable.
2. Speaker identity must map to a canonical roster entry. Decisions and commitments require `VERIFIED/HIGH` identity confidence.
3. Decision needs exact choice, authorized decider, authority evidence, locator, rationale, scope and confirmation status.
4. Commitment needs explicit owner acceptance, deliverable, due/trigger, acceptance criteria, report-to and locator.
5. Empty dissent/dependency lists are valid only when fields exist; omission of a known dissent is forbidden.
6. Forbidden flags: `fabricated_source`, `altered_quote`, `inferred_as_decided`, `unauthorized_decider`, `forced_commitment`, `hidden_dissent`, `silent_correction`, `fake_signed`, `fake_sent`, `fake_done`.
7. Required tests: `source_provenance`, `speaker_identity`, `decision_authority`, `action_acceptance`, `dissent_unknown_coverage`, `privacy_correction`, `distribution_execution_boundary`.
8. Errors → `NOT_READY`; clean with final review pending → `READY_FOR_RECORD_REVIEW`; all reviews PASS → `READY_FOR_AUTHORIZED_DISTRIBUTION`. Engine never sends or creates tasks.

