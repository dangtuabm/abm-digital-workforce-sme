# AGENT CONTRACT RULES

## 1. Contract, capability and grant

- Contract describes permitted behavior; IAM/connector/system enforcement grants actual access.
- Capability answers “có thể”; permission answers “được phép”; authority answers “ai chịu trách nhiệm quyết định”. Không suy quyền từ tool availability, prompt, job title hoặc prior success.
- Critical `UNKNOWN` defaults to no action, not ALLOW. Exception requires owner, scope, reason, compensating control, expiry and evidence.
- Contract PASS means decision-ready; admission/activation/deployment remain separate human-controlled events.

## 2. Minimum trace

`outcome → task → input/source/rights → action → object/data → tool/permission → output/acceptance → evidence → decision/authority → state/verification`.

Each contract freezes Agent ID, Task ID, version, environment, owner, approver, effective/expiry/review dates and hashes/pointers to approved sources. Persona and natural-language prompt are implementation inputs, never the complete contract.

## 3. Input/output semantics

Input fields: name, type, required, source/SoR, provenance, freshness, data class, rights, validation, missing/conflict, quarantine and injection policy.

Output fields: name, schema/type/format, consumer/destination, classification, acceptance rule/test, evidence/result link, confidence/uncertainty, abstain/TBD, retention and acknowledgment.

DONE requires accepted evidence, not merely generation, upload, command success or absence of complaint.

## 4. Authority and permission

- Decision state: `ALLOW`, `CONDITIONAL`, `DENY`; include actor, action, object, environment, condition/limit, owner/approver, evidence, expiry and escalation.
- Tool/data access: connector, operation, resource, data class, identity, scope, rate/cost limit, secret reference, grant evidence, expiry/revoke and verification.
- Separate read, create, update, delete, execute, send/publish, approve, purchase/sign and permission-admin actions.
- Apply least privilege and Separation of Duties (tách biệt nhiệm vụ); Executor is not its own independent Kaizen or permission approver.

## 5. State and delivery

State names are contract-specific; each legal transition needs from/to, event, actor, precondition, action, expected result, verification, evidence, timeout and failure transition. Correlation/idempotency keys control duplicate, retry, replay and late events.

One Task has one independently accepted outcome and one end-to-end Executor. Use Work Package only for independently owned/accepted outputs; research, analysis, drafting and self-check are internal steps, not reasons to create an Agent relay.

## 6. Failure and service controls

- Classify retryable/non-retryable/ambiguous failures; bound retry and backoff; prevent duplicate side effects.
- Define timeout, fallback, compensation, reconciliation, escalation, DLQ, manual path, emergency stop, recovery and re-entry.
- SLO/budget/capacity controls require metric, formula/source, threshold rationale, window, owner, breach action and evidence. No automatic spend increase or privilege escalation.

## 7. Audit and evidence

Record trace ID, timestamps, contract/skill/model/tool/dependency versions, input/output pointers/hashes, state before/after, decision/action, authority/approval, verification, errors/retries/fallback, cost and result link. Redact/minimize; store secret references, never secret values.

## 8. Conformance and lifecycle

Minimum tests: schema, missing/conflict, DoD, permissions, least privilege, injection, idempotency, timeout, retry/fallback, escalation/DLQ, rollback/reconciliation, audit/redaction, human control and offboarding. Use negative and failure fixtures, not happy path alone.

Version contract/schema/skill/tool/dependency; define backward compatibility, migration, canary, rollback and consumer notification approval. Offboarding suspends triggers, revokes identity/connector/secrets, drains/reconciles work, retains/deletes per authority, preserves audit and verifies no residual access.

## 9. Prohibited shortcuts

No invented grant/evidence; no UNKNOWN→ALLOW; no prompt-only contract; no shared/static secret; no unlimited retry/budget/WIP; no silent fail; no auto-create account/token; no activate/deploy/run/send/write/delete/approve/sign/purchase/publish; no unreviewed scope/version change; no decommission before recovery and retention gates.

