# GOVERNED WORKFLOW AUTOMATION DESIGN & PILOT READINESS PACK

## 0. Document control

Version · owner · reviewers · status · environment · evidence cutoff · source hashes · changes · approvals.

## 1. Mandate và process truth

Objective/decision · baseline/pain · current flow · target flow · scope/exclusions · start/end · volume/peak · SLA · owner · policy · prohibited actions · success/kill.

## 2. Source, event và state contracts

| ID | SoR/source | Schema/version | Keys/timezone | Correlation/idempotency | Validation | Duplicate/late/replay | Rights/retention | Hash/as-of |
|---|---|---|---|---|---|---|---|---|

| State | Entry | Allowed trigger/guard | Actor/system | Exit | Terminal/failure/manual | Evidence |
|---|---|---|---|---|---|---|

## 3. Step và control matrix

| Step | From→to | Trigger/input | Actor/system/permission | Action/output/acceptance | Approval/SoD | Timeout | Failure route | Evidence |
|---|---|---|---|---|---|---|---|---|

## 4. Reliability và recovery

Error taxonomy · retry eligibility · attempts/backoff/jitter · timeout · circuit breaker · queue/DLQ · dedupe · manual fallback · compensation · reconciliation · RTO/RPO basis · escalation.

## 5. Security, privacy và audit

Threats · data class/purpose/minimization · service identity/least privilege · connector approval · secret references · encryption/redaction · access lifecycle · audit immutability · correlation/run IDs · retention.

## 6. Test evidence

Happy path · validation · duplicate/replay · timeout/retry · partial success · denial · DLQ/manual · compensation/reconciliation · load/recovery. Mỗi case: setup/input/version, expected state/output/evidence, owner, PASS/FAIL.

## 7. Pilot, monitoring và action

Sandbox/canary scope · UAT · entry/success/kill · change window · monitoring/SLO · alert/runbook · action options/authority · rollback/manual continuity · communication · release decision PENDING.

## 8. Risks, decisions, reviews và audit

Sáu risk domains · residual risk · six reviews · open decisions/TBD · action queue · version/change/audit log.
