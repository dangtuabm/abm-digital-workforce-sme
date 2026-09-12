# Focus Management Gate Rules

1. `focus_capacity = working - fixed - recovery - buffer`; all values are non-negative.
2. Sum of focus-block minutes cannot exceed focus capacity. Each block maps to an authorized commitment and outcome tier.
3. Active WIP cannot exceed the agreed limit. `BLOCKED` is not counted as completed progress.
4. `DELEGATE/DEFER/DROP/ESCALATE` remains proposed until authority and affected-owner evidence exist.
5. Forbidden flags: `fabricated_availability`, `overbooked`, `sleep_or_recovery_cut`, `secret_surveillance`, `auto_rescheduled`, `auto_declined`, `auto_delegated`, `deleted_commitment`, `fake_done`.
6. Required tests: `capacity_reconciliation`, `wip_limit`, `commitment_dependency`, `authority_boundary`, `wellbeing_recovery`, `interruption_protocol`, `scheduling_execution_boundary`.
7. Errors → `NOT_READY`; clean plan with final review pending → `READY_FOR_FOCUS_REVIEW`; all required reviews PASS → `READY_FOR_AUTHORIZED_SCHEDULING`. Engine never changes external state.

