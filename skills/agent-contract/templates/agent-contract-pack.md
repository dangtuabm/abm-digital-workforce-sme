# EVIDENCE-BOUND AGENT CONTRACT & CONFORMANCE PACK

## A. Contract Identity & Mandate

- Contract/Agent/Task ID; version/status/environment; outcome; scope/non-goals; owner/approver; DoD; effective/expiry/review; confidentiality/action boundary.

## B. Input & Output Contracts

| Field | Type/required | Source/SoR/rights/class | Validation/freshness | Missing/conflict/injection | Acceptance/evidence/retention |
|---|---|---|---|---|---|

## C. Authority Matrix

| Actor | Decision/action/object | ALLOW/CONDITIONAL/DENY | Conditions/limits | Owner/approver | Evidence/expiry | Escalation |
|---|---|---|---|---|---|---|

## D. Tool–Data–Permission Matrix

| Tool/connector | Operation/resource/data class | Identity/scope/environment | Rate/cost | Grant evidence | Secret ref | Expiry/revoke | Verification |
|---|---|---|---|---|---|---|---|

## E. State, Idempotency & Failure

| From/event/to | Actor/precondition | Action/expected | Verification/evidence | Idempotency | Timeout/retry | Fallback/DLQ/escalation | Recovery |
|---|---|---|---|---|---|---|---|

## F. SLO, Budget, Capacity & Monitoring

| Metric | Formula/source/window | Threshold/rationale | Owner | Breach action | Evidence/status |
|---|---|---|---|---|---|

## G. Human Control, Audit & Exception

- External/irreversible/high-risk approval points; SoD; independent Kaizen; override/exception scope/control/expiry.
- Audit fields: trace/version/input-output pointer/hash/before-action-after/approval/verification/error/cost/redaction/retention.

## H. Conformance, Admission & Lifecycle

- Happy/missing/conflict/permission/injection/idempotency/failure/rollback/audit tests; acceptance and evidence.
- Contract/schema/skill/tool/dependency versions; compatibility/migration/canary/rollback.
- Suspend/revoke/drain/reconcile/retain-delete/archive/offboard verification.
- State: `READY_FOR_HUMAN_AGENT_CONTRACT_DECISION` hoặc `NOT_READY`; activation remains `PENDING`.

