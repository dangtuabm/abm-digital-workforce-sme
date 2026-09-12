# Systems Integration Rules v2.3

## 1. Contract hierarchy

1. Business object/SoR contract
2. Interface/event/file contract
3. Semantic mapping and validation contract
4. Identity/authorization contract
5. Delivery/reliability/consistency contract
6. Operations/cutover/lifecycle contract

Never claim `exactly once` from transport alone. State observed delivery semantics, idempotency/deduplication, replay and reconciliation controls.

## 2. State evidence

Every mutation uses `correlation_id`, `idempotency_key`, contract/config version and evidence chain:

`state_before → intended_action → provider_response → state_after → SoR_verification → human/action decision`.

HTTP/API success without SoR verification remains `DELIVERY_ACKNOWLEDGED`, not `BUSINESS_COMPLETED`.

## 3. Sáu risk/review domains

1. `BUSINESS_SCOPE_SYSTEM_OWNERSHIP`
2. `DATA_SEMANTICS_LINEAGE_QUALITY`
3. `IDENTITY_AUTHORIZATION_SECRETS`
4. `DELIVERY_RELIABILITY_CONSISTENCY`
5. `SECURITY_PRIVACY_COMPLIANCE`
6. `CUTOVER_OPERATIONS_CONNECTOR_LIFECYCLE`

Required reviews: `BUSINESS_PROCESS_OWNER`, `SYSTEM_DATA_OWNERS`, `SECURITY_PRIVACY_IAM`, `INTEGRATION_ENGINEERING_ARCHITECTURE`, `OPERATIONS_SRE_SUPPORT`, `RISK_COMPLIANCE_CHANGE`.

## 4. Bảy gate tests

`mandate_system_ownership`; `contracts_semantics`; `identity_authorization`; `delivery_consistency`; `security_audit`; `tests_reconciliation`; `cutover_lifecycle`.

## 5. Nguồn kiểm tra ngày 22/08/2026

- OpenAPI Specification 3.1.1: https://spec.openapis.org/oas/v3.1.1.html — language-agnostic HTTP API description; provider contract remains authoritative.
- CloudEvents 1.0.2: https://cloudevents.io/ — interoperable event metadata conventions; does not guarantee delivery or processing semantics.
- IETF RFC 9700 / BCP 240: https://www.rfc-editor.org/info/rfc9700/ — OAuth 2.0 security best current practice, threat model and deprecated modes.
- NIST SP 800-207: https://csrc.nist.gov/pubs/sp/800/207/final — zero-trust concepts and deployment models; requires organizational tailoring.

Các nguồn không thay thế provider documentation, threat model, contract tests, data-governance policy hoặc human approval.
