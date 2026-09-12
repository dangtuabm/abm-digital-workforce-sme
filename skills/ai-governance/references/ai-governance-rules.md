# A.I GOVERNANCE RULES

## 1. Governance evidence chain

`entity/scope → inventory item → purpose/outcome → data/action/affected parties → applicability/obligation → risk/tier → control/enforcement → test/evidence → authority/decision → monitor/incident/change/retire`.

Policy text defines intent; enforcement constrains behavior; evidence shows a control operated; qualified human owners decide applicability and residual risk. Do not infer any link.

## 2. Inventory and classification

Inventory every governed use case, system, Agent, model/service, vendor, version, owner, user group, lifecycle state, deployment footprint, data/SoR, tools/actions, integrations/dependencies and related contracts. Shadow/unknown assets remain gaps, not low risk.

Classify data and rights separately from actions and effects. Actions include read/create/update/delete/send/publish/execute/recommend/decide/approve. Assess affected parties, criticality, scale/exposure, reversibility/contestability, detectability, safety, security, privacy, fairness/people, financial, legal/contractual and operational impacts.

## 3. Applicability and current sources

- Record jurisdiction/entity/activity/population/product context before mapping obligations.
- For changing external rules and vendor terms, use current official/contract sources with effective/access date and scope; record conflict/supersession.
- A qualified legal/compliance/privacy/security owner provides applicability findings. A.I may organize evidence but must not issue legal opinion or compliance certification.
- UNKNOWN, conflict, expired evidence or missing owner blocks critical conclusions.

## 4. Risk and tier

Define method and anchors before scoring. Consider impact, likelihood, exposure/scale, reversibility/contestability, detectability, affected-party vulnerability, control dependency and uncertainty. Record inherent risk, controls, residual risk, confidence and acceptance authority.

Tier names/counts and thresholds are organization-specific. Critical prohibited actions/gates cannot be averaged away. A risk score is prioritization evidence, not approval.

## 5. Policy-control-enforcement

Map principle/policy → requirement → control objective → preventive/detective/corrective control → enforcement point → test → evidence → owner/frequency → defect/remediation/exception. Mark design versus implemented versus tested versus operating; never call a paper control effective.

Enforcement may use IAM, connector scopes, schemas, approval gates, data filters, rate/cost limits, content/action restrictions, sandbox, stop/rollback, retention/deletion and immutable evidence stores. Design is platform-neutral until selected evidence exists.

## 6. Authority, disclosure and audit

- Express decision/action/object/environment as ALLOW/CONDITIONAL/DENY with conditions, limits, owner/approver, evidence, expiry and escalation.
- Preserve Separation of Duties; governed system cannot approve its own tier, grant, exception, residual risk or evidence deletion.
- Disclosure/label syntax follows approved policy and audience/channel needs. Provenance records system/Agent/version/time/source/reviewer; label does not replace consent, acceptance or audit.
- Audit needs identity, trace/time/version, I-O pointer/hash, action/authority/approval, state before/after, verification, error/retry/cost and result link. Minimize/redact, control access/retention/deletion and prevent governed actor from altering original evidence.

## 7. Third party, evaluation and monitoring

Review vendor/model/service contract, data use/training, subprocessors, residency findings, security, IP, availability/SLA, incident/change/deprecation, portability/deletion and exit. Marketing claims do not override contract/admin/security evidence.

Evaluate quality/utility, safety, security/privacy, robustness, fairness/affected groups, explainability/contestability where relevant, human override, failure recovery, drift, cost/value and accessibility. Every metric needs formula/source/denominator/cohort/window/threshold rationale/owner/action.

## 8. Incident, exception and lifecycle

Incident: classify using approved criteria; detect, contain, stop/revoke, rollback, reconcile, preserve evidence, notify/escalate under correct authority/basis, recover, root-cause, remediate, verify and pass re-entry. Never hardcode universal severity or notification SLA.

Exception: requirement/control, scope, reason, risk, compensating control, owner/approver, start/expiry, monitoring, renewal/closure and evidence. No open-ended, retroactive or self-approved exceptions.

Lifecycle: admission, change/version/compatibility, canary/rollback, periodic/event review, access recertification, suspend, vendor/model replacement, retain/delete/archive and decommission verification. Do not retire before continuity, evidence, retention and residual-access gates.

## 9. Prohibited shortcuts

No incomplete inventory as compliance evidence; no legal claim from model; no fixed 80/20, tier, SLA, label, Notion/Sheet, stop-word list or training duration as universal; no policy without enforcement/test; no mutable self-audit; no hidden incident/exception; no auto-approve/grant/configure/run/stop/notify/sign/purchase/publish.

