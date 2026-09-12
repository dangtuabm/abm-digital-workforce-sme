---
document_code: "ABM-SQS-SC-81"
skill: "data-anomaly"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — DATA ANOMALY v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh cho source/contract/lineage preservation, data-quality precheck, comparable baseline, method/assumption/threshold governance, reproducible signal detection, seasonality/segment/denominator/multiplicity validation, triage, hypothesis/disconfirming tests, cause-state control, human action and detector feedback. D10 chưa đạt vì chưa có baseline/with-skill pilot trên data/metric/process thật, calibrated labels, incident/cause owner evidence, false trigger, token và duration.

Chuỗi kiểm định: `SKILL-CREATOR → DATA-HYGIENE-RAG → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 `designed_not_run` |
| SKILL-CREATOR quick_validate | PASS — `Skill is valid!` |
| Description | 594 ký tự, ≤ 600 |
| Body | 7.954 ký tự, ≤ 8.000 |
| Lines | 106, ≤ 500 |
| Evals | 12; trigger, must_not_trigger, no_false_ask, ambiguity, red_line, injection, adversarial |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive fixture:** `READY_FOR_HUMAN_ANOMALY_DECISION`; 0 defect; 0 review gap. Coverage: 6 sources, 6 contracts, 6 baselines, 8 detectors, 8 signals, 8 investigations, 8 hypotheses, 6 action options, 4 monitoring/feedback records, 6 risks, 6 decisions, 7/7 gate tests và 6/6 reviews.

**Negative fixture:** `NOT_READY`; 289 defects; 6 review gaps. Engine chặn fabrication của source/contract/baseline/method/threshold/score/p-value/signal/cause/action; non-comparable baseline, failed assumptions, small sample, seasonality/segment/denominator/multiplicity hiding; correlation/alert overclaim; outlier deletion/data correction; instruction execution/secret exposure; auto mutation, threshold/detector tuning, incident/root-cause/fraud declaration, account/process/payment/customer/employee/external action, deployment/publication và evidence mutation.

## 4. Final Gatekeeper

- PASS evidence: raw source/contract/query/model snapshots and hashes are read-only; quality issues remain candidates, not assumed causes.
- PASS statistics: baseline regime/comparability, method assumptions, calibration/cost, uncertainty and multiplicity are explicit; no universal threshold or invalid p-value.
- PASS interpretation: alert ≠ anomaly ≠ incident; score ≠ impact; correlation/temporal order ≠ cause; signal checks numerator/denominator, slices, seasonality and known events.
- PASS investigation: hypotheses state mechanism, predicted observation, supporting/disconfirming evidence, alternatives/confounders and `SUPPORTED/DISPROVED/UNRESOLVED`.
- PASS safety: no auto delete/correct/tune/close/declare/remediate/notify/publish; six reviews PASS and final human decision PENDING.

## 5. Nguồn chính thức kiểm tra ngày 22/08/2026

- NIST/SEMATECH e-Handbook — Process Monitoring: https://www.itl.nist.gov/div898/handbook/pmc/pmc.htm
- ISO 7870-2:2023: https://www.iso.org/standard/78859.html
- W3C PROV-O Recommendation: https://www.w3.org/TR/prov-o/

Các nguồn chỉ hỗ trợ monitoring/control-chart/time-series và provenance principles; không áp một detector/chart cho mọi process, không biến signal thành cause/incident/fraud và không chứng nhận compliance.

## 6. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `D59BEF0240801AADBCFBC8797D22EDB27919618CF4D8AF11CBD9891CE8B59580` |
| evaluator | `C3015936F798BFF81F8A8C13588C4C1F8BED277EB0A2EF266C188067D422F32A` |
| evals | `E4210EECEA36E3904E2FDC9977CD8E2DBBE27C5CBFC13802B802B7F32B55CA86` |
| positive fixture | `5616DBB3747A856B1AD358E45C6514EDFF5CEA99AC6CCA165108F474BA51103A` |
| negative fixture | `1AE65EAAD412B9C8CC155DEBEC8C63CE4A0B123AFE114C03C0A3B21FD59CEF17` |
| rules reference | `4D43218BC36D055237EA9E35F35137ED69C2993494DDF0CEB4E955BF0C4E8989` |
| pack template | `102DB408B3F2A8C221EEBA16DEF9F0717D14169A5B61E04A7B3DA07E2B89FF48` |

## 7. Cổng còn thiếu

D10 cần pilot trên source/metric/query/model/baseline/detector/signal/incident snapshots thật, có six owners xác nhận: data quality/lineage, baseline comparability, method assumptions/threshold calibration, false positives/misses/multiplicity, impact/severity, hypotheses/disconfirming evidence/cause, action authority/rollback/verification, detector drift, false trigger, token và duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.

