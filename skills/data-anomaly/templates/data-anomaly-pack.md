# DATA ANOMALY TRIAGE & INVESTIGATION PACK

## 1. Document control / mandate

Decision/use · metric/process/entity scope/exclusions · impact/severity rubric · as-of/horizon · owners/reviewers · action boundary · non-goals · version/hash.

## 2. Source / contract / baseline

| Source/metric | Snapshot/version/hash | Schema/grain/keys/time/unit | Formula/denominator/filters | Query/model/code hash | Rights/lineage | Baseline regime/window/population | Stability/seasonality/known events/limitation |
|---|---|---|---|---|---|---|---|

## 3. Detector registry

| Detector/version | Metric/slice | Method/rationale | Assumptions/tests | Parameters/threshold/authority | Calibration/cost | Multiplicity/uncertainty | Owner/state |
|---|---|---|---|---|---|---|---|

## 4. Signal register

| Signal | Detector | Expected/actual/delta/score | Window/slice | Raw evidence/hash | Quality/denominator/seasonality checks | Impact/confidence | State |
|---|---|---|---|---|---|---|---|

## 5. Triage / investigation

Raw-vs-aggregate · adjacent/control segments · numerator/denominator · time/unit/timezone · ingestion/revision · known events · triage type · owner/SLA.

## 6. Hypothesis / cause evidence

| Hypothesis/mechanism | Predicted observation | Supporting evidence | Disconfirming test/result | Alternatives/confounders | Cause state | Reviewer/limitation |
|---|---|---|---|---|---|---|

## 7. Impact / actions / monitoring / feedback

Action option · impact/blast radius · authority/prerequisites · owner/SLA · rollback · verification · human state. Monitor recurrence/misses/false positives/drift; versioned tuning proposal only.

## 8. Risks, decisions, reviews và audit

Ghi đủ six risks, decision queue, six reviews, prohibited-action check and audit log. Final: `FINAL_HUMAN_ANOMALY_DECISION = PENDING`.

