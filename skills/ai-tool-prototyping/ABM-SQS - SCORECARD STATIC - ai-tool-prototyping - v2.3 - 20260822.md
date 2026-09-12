---
document_code: "ABM-SQS-SC-84"
skill: "ai-tool-prototyping"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — A.I TOOL PROTOTYPING v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh để khóa problem/value/learning question, compare no-build/buy/reuse/custom, thiết kế product/data/A.I behavior contracts, architecture/trust boundaries/dependencies, human control, reproducible build evidence, functional/model/security/privacy/accessibility/resilience tests, monitoring, governed pilot, kill/rollback/delete và handover. D10 chưa đạt vì chưa có baseline/with-skill pilot trên người dùng, task, dữ liệu, model, tool và environment thật; chưa có measured false trigger, token và duration.

Chuỗi kiểm định: `SKILL-CREATOR → AGENT-ORCHESTRATION → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 `designed_not_run` |
| SKILL-CREATOR quick_validate | PASS — `Skill is valid!` |
| Description | 592 ký tự, ≤ 600 |
| Body | 7.945 ký tự, ≤ 8.000 |
| Lines | 104, ≤ 500 |
| Evals | 12; trigger, must_not_trigger, no_false_ask, ambiguity, red_line, injection, adversarial |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive fixture:** `READY_FOR_HUMAN_PROTOTYPE_DECISION`; 0 defect; 0 review gap. Coverage: 6 sources, 6 user tasks, 8 product requirements, 6 data contracts, 8 architecture components, 8 A.I behavior cases, 12 test cases, 4 rollout plans, 4 monitoring records, 6 action options, 6 risks, 6 decisions, 7/7 gate tests và 6/6 reviews.

**Negative fixture:** `NOT_READY`; 104 defects; 6 review gaps. Engine chặn missing problem/user/baseline/value/owner/learning question; solution-by-trend; fake accuracy; unknown data rights/schema/lineage; production data và secret hardcode; admin permission; unpinned dependency/unknown license; missing grounding/abstain/human gate; demo-only tests; accessibility/security/privacy/recovery gaps; test mutation; auto purchase, permission change, production connection, deployment, hosting, publication, notification và action.

## 4. Final Gatekeeper

- PASS product: prototype starts from evidenced task and learning question; smallest reversible type is selected after no-build/buy/reuse/custom comparison.
- PASS contracts: sources, fixtures, schemas, rights, model/tool/prompt/context and expected behavior are versioned and hashed.
- PASS architecture: trust boundaries, identities, least privilege, secret references, dependencies/licenses, SoR, audit and reproduction evidence are explicit.
- PASS assurance: frozen tests cover function, grounding, abstention, injection, authorization, privacy, accessibility, resilience, performance and human control.
- PASS safety: no production data/secret/connection or auto deploy/host/publish/action; six reviews PASS and final human decision PENDING.

## 5. Nguồn chính thức kiểm tra ngày 22/08/2026

- NIST AI RMF 1.0: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
- NIST SP 800-218 SSDF 1.1: https://csrc.nist.gov/pubs/sp/800/218/final
- OWASP ASVS 5.0: https://owasp.org/www-project-application-security-verification-standard/
- W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/

Các nguồn hỗ trợ quản trị/risk measurement, secure development, application-control verification và accessibility criteria. Chúng phải được tailor theo tool type/risk/environment và không chứng nhận prototype, compliance, security, accessibility, accuracy hay ROI.

## 6. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `EC4A4A3829C57F3F828CCFC05160D6B068619410BAB9245C599CB309063E3C93` |
| evaluator | `2B4F294987B5945B24793C0AC4B7CE3EC0E5C36F6C9C7E4AAB7A219BB8E77BF3` |
| evals | `785DA3FEC5E2AB7D4F6FCDEE2FA6A6E2E85C4FE6D31ACFA8212299DE164DD2EF` |
| positive fixture | `11EC9396B120016734EBF79E0501739598F58142A82699D0261EF5B84953C4F1` |
| negative fixture | `0E4ACC027690B710B3EA023D3EEFEF185A900B003940CEA9862B005DCEA0E147` |
| rules reference | `EB688470D8CD585C6B568BF6672B4DCB0A9024500738D5219A2822E3DBA788ED` |
| pack template | `1899F27CBC9BD6442BE06B9A610BFEDB87885D0E23784EA61BAE67ECD3586021` |

## 7. Cổng còn thiếu

D10 cần pilot trên real user/task/baseline, authorized source/fixture, model/tool/prompt/context, prototype/build/dependency and environment; six owners phải xác nhận problem/value, data/labels, A.I behavior/error slices, security/privacy/legal, UX/accessibility, engineering/reliability, UAT/monitoring/support/kill/rollback/delete/handover; kèm false trigger, token và duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.
