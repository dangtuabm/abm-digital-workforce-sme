---
document_code: "ABM-SQS-SC-85"
skill: "systems-integration"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — SYSTEMS INTEGRATION v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh để khóa system/object ownership và one SoR/object, interface/event/file contracts, semantic mappings, service identities và exact CRUD/send rights, correlation/idempotency/delivery claims, retry/DLQ/compensation/reconciliation, security/privacy/audit, contract/E2E/failure tests, monitoring, canary/cutover/rollback/manual continuity và connector lifecycle. D10 chưa đạt vì chưa có baseline/with-skill pilot trên provider contracts, identities, data, traffic, systems và SoR thật; chưa có measured false trigger, token và duration.

Chuỗi kiểm định: `SKILL-CREATOR → AGENT-ORCHESTRATION → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 `designed_not_run` |
| SKILL-CREATOR quick_validate | PASS — `Skill is valid!` |
| Description | 589 ký tự, ≤ 600 |
| Body | 7.957 ký tự, ≤ 8.000 |
| Lines | 104, ≤ 500 |
| Evals | 12; trigger, must_not_trigger, no_false_ask, ambiguity, red_line, injection, adversarial |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive fixture:** `READY_FOR_HUMAN_INTEGRATION_DECISION`; 0 defect; 0 review gap. Coverage: 6 systems, 8 interface contracts, 8 semantic mappings, 6 identity controls, 10 flow steps, 8 reliability controls, 12 test cases, 4 cutover plans, 4 monitoring records, 6 action options, 6 risks, 6 decisions, 7/7 gate tests và 6/6 reviews.

**Negative fixture:** `NOT_READY`; 100 defects; 6 review gaps. Engine chặn missing ownership/SoR/contracts; invented endpoint/schema/event/result; field-name-only mapping; shared admin/wildcard scope/secret hardcode; incomplete CRUD/send matrix; false exactly-once claim; infinite retry; missing DLQ/compensation/reconciliation; HTTP 200 treated as business completion; production data; audit mutation; auto credential/permission/connector/production connection, deployment, migration, publication, notification và action.

## 4. Final Gatekeeper

- PASS ownership: every object has a named owner and one SoR; interface ACK is separated from business completion.
- PASS contracts: eight versioned interface contracts and semantic maps retain schemas, errors, rate/timeout, keys, types, units, timezones, enums, lineage and reconciliation.
- PASS authority: dedicated identities use least privilege, complete CRUD/send matrices, approval/SoD, secret references and rotate/revoke/expiry lifecycle.
- PASS reliability: delivery claims are honest; idempotency, ordering/replay, bounded retry, circuit/DLQ, partial state, compensation and SoR verification are explicit.
- PASS safety: no secret, production connect, permission change, deploy/migrate/send/action; six reviews PASS and final human decision PENDING.

## 5. Nguồn chính thức kiểm tra ngày 22/08/2026

- OpenAPI Specification 3.1.1: https://spec.openapis.org/oas/v3.1.1.html
- CloudEvents 1.0.2: https://cloudevents.io/
- IETF RFC 9700 / BCP 240: https://www.rfc-editor.org/info/rfc9700/
- NIST SP 800-207 Zero Trust Architecture: https://csrc.nist.gov/pubs/sp/800/207/final

Các nguồn hỗ trợ API/event description, OAuth threat/security guidance và zero-trust concepts. Chúng phải được tailor theo provider contract, data policy, threat model và environment; không chứng nhận interoperability, security, exactly-once, availability hoặc compliance.

## 6. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `736B30A88625F65EBC11DD860BDA78A299F65CEB00023CE33F47C3BB636BCBB7` |
| evaluator | `937594E4DC604E018C862A74F8176BD1E29BAEEF892FCBCBEABB693EB0D09E21` |
| evals | `801C7885D115371B028908C3491587AA187301A7D23F7EDE4CEAF44FFB323FFA` |
| positive fixture | `EDAED2F0C079194BA6680164CD7FFDA3CC535FE66E00570CFFCBFC8CAD5257FF` |
| negative fixture | `1F2C216868001D4EFF91048E43873FF4B0E9D0CD155D69DED06D7C03F387977D` |
| rules reference | `1495D5D5A9D01EEECE60E9FE7C359AF3C9ABA8C3F4A39F48A377C8E4ADC72222` |
| pack template | `A6C6B7291AA8A3C8B7F99B8A66CD13B2D948A854B47A8FB78580D44344F10DFC` |

## 7. Cổng còn thiếu

D10 cần pilot trên business flow/system/SoR/provider spec/schema/mapping/service identity/scope/secret lifecycle/event/API/file/volume/rate/error thật; six owners phải xác nhận ownership/semantics, authorization, delivery/consistency, security/privacy, contract/E2E/load/failure/reconciliation evidence, SLO/monitoring/support/canary/cutover/rollback/manual/offboarding; kèm false trigger, token và duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.
