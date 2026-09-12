# Meeting Readiness Rules

1. Meeting identity is `meeting_id + version + start + end + timezone`.
2. Type is `DECIDE/ALIGN/SOLVE/REVIEW/CREATE`; each requires an explicit output.
3. Required decider and attendees must be available/authorized; quorum must be true before invite readiness.
4. Every decision item needs question, at least two options, recommendation, evidence, decision rule, owner and deadline.
5. Sum of agenda durations cannot exceed meeting duration. Every segment needs objective, mode, owner, inputs, output and stop rule.
6. Pre-read must be active, fresh, accessible to required roster and in `DRAFT/REVIEWED`; engine never marks `SENT/READ`.
7. Forbidden flags: `fabricated_history`, `hidden_open_commitment`, `fake_quorum`, `fake_attendance`, `fake_pre_read_sent`, `fake_pre_read_read`, `auto_invited`, `auto_rescheduled`, `false_decision`.
8. Required tests: `meeting_contract`, `source_freshness`, `attendee_quorum`, `decision_readiness`, `agenda_timebox`, `pre_read_accessibility`, `invitation_execution_boundary`.
9. Errors → `NOT_READY`; clean with final pending → `READY_FOR_MEETING_REVIEW`; all reviews PASS → `READY_FOR_AUTHORIZED_INVITE`. Engine never invites or sends.

