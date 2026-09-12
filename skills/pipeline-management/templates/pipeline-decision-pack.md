# PIPELINE CONTROL PACK — TEMPLATE

## 1. Document control

| Field | Value |
|---|---|
| Mandate / portfolio / scope | |
| As-of / horizon | |
| CRM snapshot ID / hash / timestamp | |
| Sales-process / score-model version | |
| Opportunity unit / currency basis | |
| Owner / stage / forecast / decision authority | |
| Rights / confidentiality / retention | |
| Reviews / final state | |

## 2. Source and lineage ledger

| Source ID | Type | Locator/version | Timestamp | Rights | Coverage/freshness | Confidence | Gap |
|---|---|---|---|---|---|---|---|

## 3. Stage contract

| Order | Stage | Entry | Evidence | Exit | Owner/authority | Age-limit source | Next-action SLA | Allowed forecast |
|---:|---|---|---|---|---|---|---|---|

## 4. Opportunity register

| Opportunity | Account entity | Owner | Amount/currency | Stage/entered | Stage evidence | Fit/need/decision/budget/timing | Stakeholders | Last meaningful activity | Data status |
|---|---|---|---:|---|---|---|---|---|---|

## 5. Score rationale

| Opportunity | Dimension | Weight | Score | Evidence | Confidence | Missing/limitation | Override audit |
|---|---|---:|---:|---|---|---|---|

## 6. Aging and next action

| Opportunity | Age/limit | Stale status | Next outcome | Owner | Due | Dependency | Expected evidence | SLA exception |
|---|---|---|---|---|---|---|---|---|

## 7. Reconciliation and coverage

- Census and included/excluded IDs:
- Duplicate/merge/split treatment:
- Amount/currency reconciliation:
- Count/amount by stage:
- Owner/capacity coverage:
- Freshness/unknowns/variance:
- Reconciliation state and unresolved items:

## 8. Forecast scenarios

| Scenario | Opportunity | Amount/currency | Category/probability basis | Timing | Assumption | Capacity/dependency | Risk/limitation |
|---|---|---:|---|---|---|---|---|

## 9. Exception and risk register

| ID | Type | Affected IDs | Evidence | Severity | Trigger | Owner/due | Verification/action | Escalation/state |
|---|---|---|---|---|---|---|---|---|

## 10. Human decision queue

| Opportunity | Recommendation | Rationale/evidence | Decision owner | Needed by | Human state | External evidence after action |
|---|---|---|---|---|---|---|

## 11. Reviews and audit

| Review | Reviewer | Result | Evidence | Gap/action |
|---|---|---|---|---|

Final human pipeline decision: `PENDING`.

## 12. D10 record

Baseline/v2.3, case/ground truth, pass^3, stage/amount/forecast/exception/customer-harm metrics, token, duration, reviewer outcome and adoption.
