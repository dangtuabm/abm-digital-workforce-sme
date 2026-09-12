# AGENT ORCHESTRATION RULES

## 1. Necessity before topology

- Compare deterministic workflow, one Agent with tools, and multi-Agent against the same outcome/DoD.
- Multi-Agent needs evidence of independent outputs, specialization, parallel capacity, isolation or resilience that outweighs routing/handoff/latency/cost/data/failure overhead.
- More roles, model diversity or parallel calls are not evidence of business value. If the simpler option passes, recommend it.

## 2. Work unit and ownership

- One Task = one independently accepted output, owner, end-to-end Executor, independent Kaizen and result link.
- Work Package exists only for multiple independently accepted Tasks. Research, analysis, drafting and self-check stay within one Executor unless their outputs are independently consumed.
- Graph edges carry dependency and acceptance semantics; fan-out/fan-in needs merge owner, completeness, duplicate and conflict rules.

## 3. Registry and admission

Each Agent record needs Agent/role ID, valid Agent Contract/version, capabilities, skills, tool/data/permission envelope, trust zone, environment, capacity/cost, availability, quality evidence, admission/expiry/review/revoke and Kaizen independence. Role requirements are vendor/model-neutral.

Admission requires contract/schema/permission tests, failure/red-boundary tests, audit/observability, owner reviews and a rollback/offboarding path. Registry presence is not activation.

## 4. Intake, routing and queue

- Intake validates source/schema/rights, correlation/idempotency key, duplicate/replay/late event, quarantine and Task-versus-Work-Package decision.
- Routing applies eligibility gates before scoring: task contract, skills, data/access/trust, environment, capacity/SLO/cost and availability. Record candidate set, evidence, rejection reasons, tie/fallback/override and route version.
- Router never grants permission or changes an Agent Contract.
- Queue controls include priority class, aging/fairness, WIP, backpressure, rate/concurrency/cost, reservation/lease, starvation/deadline, cancellation and retry-storm prevention.

## 5. State and handoff

State sets vary by system. Every legal transition specifies from/event/to, actor, precondition, action, expected, verification/evidence, correlation/idempotency, timeout, heartbeat/lease, failure transition and terminal immutability.

Handoff specifies producer/consumer, Task/contract/schema versions, payload pointer/hash, provenance, confidence/TBD, data class/minimization, acceptance/reject/rework, timeout, duplicate/conflict, result link and audit trace. Never pass full context or secrets by default.

## 6. Quality and synthesis

- Executor owns V1 end-to-end; independent Kaizen check-fixes to Final against DoD/evidence.
- BLOCK/ESCALATE only for missing source, goal change, authority/risk boundary or irreconcilable evidence.
- Majority vote, model agreement and polished prose do not replace source truth, acceptance or owner decision.
- Synthesis needs named owner, completeness rule, conflict log, precedence rule and trace from Final to every accepted Task result.

## 7. Failure and human control

Define failure domains, retryability, bounded retry/backoff, idempotency, fallback, circuit breaker, bulkhead/isolation, DLQ, compensation/reconciliation, escalation, manual path, emergency stop, recovery/re-entry and incident review. Prevent cascading failure, duplicate effects and orphan work.

Human approval sits before external/irreversible/high-risk action, exception, goal/contract/permission/budget change and final release. Preserve Separation of Duties; do not require human approval for every internal reversible step.

## 8. Trust, observability and lifecycle

- Trust boundary covers identity, least privilege, data class/rights, cross-Agent exposure, injection, secret reference, connector enforcement and access recertification.
- Distributed trace records work package/task/agent/contract/skill/model/tool/schema/route/config versions, input/output hashes, state before/after, approvals, errors/retries/fallback, latency/cost and result links.
- Observe outcome/quality, queue/WIP, routing, handoff, SLO, capacity, cost, failures/incidents, human interventions and value; define metric/source/window/owner/action.
- Change via versioned config/contract/schema, compatibility test, canary, rollback and consumer coordination. Offboard by stop intake, drain/reconcile, revoke identity/connector/secret, retain/delete/archive per authority and verify no residual work/access.

## 9. Prohibited shortcuts

No multi-Agent without necessity; no Agent without contract; no vendor-locked role; no Executor=self-Kaizen; no raw-context broadcast; no routing-as-permission; no unlimited WIP/retry; no silent/cascading failure; no spawn/provision/grant/activate/run/mutate/send/spend/publish; no breaking change or offboarding without compatibility, rollback and verification.

