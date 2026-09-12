# A.I Tool Prototyping Rules v2.3

## 1. Prototype decision

- Start with the learning question and user task, not stack/model.
- Compare `NO_BUILD`, `CONFIGURE/BUY`, `REUSE`, `CUSTOM_PROTOTYPE`; state assumptions and reversible exit.
- Use synthetic/masked frozen fixtures by default. Real/production data requires separate rights, environment and approval evidence.
- Prototype outcome is `reject`, `revise`, `pilot` or `hold`; never silent production promotion.

## 2. Evidence chain

`problem evidence → requirement → source/data contract → behavior contract → component/build hash → test case/result → defect/risk → decision`.

Every A.I case records input/context version, expected behavior, actual structured output, citations/grounding, human decision and error slice. Track false accept, false reject, abstain and unsafe action separately.

## 3. Sáu risk/review domains

1. `PROBLEM_VALUE_SCOPE`
2. `DATA_MODEL_BEHAVIOR`
3. `SECURITY_PRIVACY_SUPPLY_CHAIN`
4. `UX_ACCESSIBILITY_HUMAN_CONTROL`
5. `RELIABILITY_OBSERVABILITY_RECOVERY`
6. `PILOT_RELEASE_OWNERSHIP`

Required reviews: `PRODUCT_BUSINESS_OWNER`, `DOMAIN_DATA_OWNER`, `AI_MODEL_EVALUATION`, `SECURITY_PRIVACY_LEGAL`, `ENGINEERING_UX_ACCESSIBILITY`, `OPERATIONS_PILOT_CHANGE`.

## 4. Bảy gate tests

`mandate_problem_value`; `product_data_contracts`; `architecture_dependencies`; `ai_behavior_human_control`; `security_privacy_accessibility`; `functional_resilience_evidence`; `pilot_monitoring_release`.

## 5. Nguồn kiểm tra ngày 22/08/2026

- NIST AI RMF 1.0: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10 — Govern/Map/Measure/Manage; voluntary, use-case agnostic.
- NIST SP 800-218 SSDF 1.1: https://csrc.nist.gov/pubs/sp/800/218/final — secure software-development practices integrated into SDLC.
- OWASP ASVS 5.0: https://owasp.org/www-project-application-security-verification-standard/ — requirements and verification basis for web-application technical controls.
- W3C WCAG 2.2: https://www.w3.org/TR/WCAG22/ — testable accessibility success criteria; conformance requires full-scope evaluation.

Tailor by tool type, risk, users and environment. These sources do not certify a prototype or replace legal, privacy, accessibility or security review.
