# Workflow Automation Rules v2.3

## 1. State và evidence

- Tách `process truth`, `workflow design`, `runtime evidence` và `human decision`.
- Mỗi run có correlation/run ID; mỗi side effect có idempotency key hoặc bị đánh dấu non-retryable.
- Log chưa đủ: phải reconcile `state_before → intended_action → state_after → verification` với System of Record.
- Trigger chỉ khởi tạo evaluation; approval/authority quyết định side effect.

## 2. Failure taxonomy

| Class | Default disposition |
|---|---|
| Validation/business rule | Không retry; reject/route human với reason code |
| Policy/permission | Không bypass; stop và escalate đúng owner |
| Transient dependency | Bounded retry theo provider guidance, backoff/jitter, timeout |
| Persistent dependency | Circuit open, queue/DLQ hoặc manual fallback |
| Partial side effect | Stop, verify SoR, compensate/reconcile theo approved runbook |
| Unknown | Fail closed đối với mutation; preserve evidence |

Retry chỉ an toàn khi action idempotent hoặc duplicate được kiểm soát. Không nested retry, infinite retry hay retry business error.

## 3. Sáu risk/review domains

1. `PROCESS_POLICY_AUTHORITY`
2. `DATA_EVENT_IDENTITY`
3. `ACTION_APPROVAL_SOD`
4. `RELIABILITY_IDEMPOTENCY_RECOVERY`
5. `SECURITY_PRIVACY_CONNECTOR`
6. `DEPLOYMENT_MONITORING_CHANGE`

Required reviews: `BUSINESS_PROCESS_OWNER`, `RISK_COMPLIANCE_LEGAL`, `SECURITY_PRIVACY_IAM`, `DATA_SYSTEM_OWNER`, `ENGINEERING_SRE_PLATFORM`, `OPERATIONS_CHANGE_UAT`.

## 4. Bảy gate tests

`mandate_process`; `contracts_state`; `authority_controls`; `reliability_recovery`; `security_audit`; `tests_reconciliation`; `pilot_monitoring_change`.

## 5. Nguồn kiểm tra ngày 22/08/2026

- OMG BPMN 2.0.2: https://www.omg.org/spec/BPMN/2.0.2 — process/event/activity/gateway notation; không mặc định diagram executable.
- NIST SP 800-53 Rev. 5: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final — least privilege, audit/accountability, system integrity and contingency-control families; tailoring required.
- Microsoft Azure Architecture Center — Retry pattern: https://learn.microsoft.com/en-us/azure/architecture/patterns/retry — transient-fault retry, idempotency and transaction-consistency considerations.
- Microsoft Azure Architecture Center — Retry Storm antipattern: https://learn.microsoft.com/en-us/azure/architecture/antipatterns/retry-storm/ — bounded attempts/duration and backoff.

Các nguồn không thay thế policy, threat model, provider-specific contract, testing hay human approval.
