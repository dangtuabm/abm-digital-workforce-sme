# DATA HYGIENE & MIGRATION CONTROL PACK

## 1. Document control / mandate

Use case/domain · datasets/tables/files/records/exclusions · environments · as-of/horizon · owner/steward/reviewers · approved purpose · classification/access/residency/retention/hold · SoR/golden authority · non-goals · version/hash.

## 2. Inventory / source snapshot

| Asset ID | Locator/environment | Owner/SoR | Format/schema/grain/keys | Size/count/freshness | Classification/purpose/rights | Retention/hold | Dependencies/downstream | Snapshot/hash |
|---|---|---|---|---|---|---|---|---|

## 3. Data contract / profile

| Field/CDE | Meaning/type/null | Format/encoding/locale/timezone | Unit/currency/domain/range | Key/referential/unique | Ground truth | Quality metric/formula/denominator | Threshold/owner | Finding/limitation |
|---|---|---|---|---|---|---|---|---|

## 4. Mapping / transform / lineage

| Source asset/field/value | Target asset/field/value | Rule/version/code hash | Activity/agent/time | Old→new reason | Deterministic/reversible | Evidence/hash | Approval state |
|---|---|---|---|---|---|---|---|

## 5. Dedup / entity-resolution queue

| Candidate/cluster | Blocking/features | Score/method/version | Match/non-match/review thresholds | Evidence | False merge/split cost | Survivorship proposal | Human owner/state |
|---|---|---|---|---|---|---|---|

## 6. Quarantine / reconciliation / downstream tests

Quarantine: record/field/source · typed reason · original value · rule/version · impact · owner/SLA · remediation/waiver · state.

Reconciliation: source/target rows/files/keys/nulls/duplicates/rejects · aggregates/control totals · referential breaks · hashes · delta explanation · PASS/FAIL.

Downstream tests: schema/query/process/interface · positive/negative/edge fixture · expected/actual · coverage/limitation · privacy/security/fairness · rollback.

## 7. Risks, decisions và reviews

Ghi đủ six risks, decision queue và six reviews. Final: `FINAL_HUMAN_DATA_HYGIENE_DECISION = PENDING`.

## 8. Audit / change log

Version · timestamp · source/staging/target/quarantine snapshots/hashes · contract/rule changes · test/reconciliation run · reviewer · unresolved TBD/conflicts · prohibited-action check · next authorized release action.
