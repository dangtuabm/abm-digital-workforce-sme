# Context Management Rules v2.3

## 1. Eight layers

1. Mandate and authority contract
2. Source registry and provenance
3. Active working set plus exclusion ledger
4. Claim-evidence coverage map
5. Decision/TBD/risk/state ledger
6. Compaction, branch and handoff contracts
7. Durable-memory candidates
8. Retention, snapshot, archive and delete ledger

Do not collapse these layers into a single summary or memory file.

## 2. Selection test

For each item record `relevance`, `authority`, `freshness`, `coverage`, `risk`, `duplication`, `phase`, `include/exclude`, reason and retrieval pointer. A score supports review but never overrides a hard authority/security rule.

## 3. Six risk/review domains

1. `AUTHORITY_CONFLICT_SOURCE`
2. `RELEVANCE_COMPLETENESS_CONTEXT_BUDGET`
3. `FRESHNESS_VERSION_PROVENANCE`
4. `PRIVACY_SECURITY_PROMPT_INJECTION`
5. `COMPACTION_BRANCH_HANDOFF`
6. `MEMORY_RETENTION_DELETION`

Required reviews: `TASK_DECISION_OWNER`, `DOMAIN_SOURCE_OWNER`, `DATA_PRIVACY_SECURITY`, `KNOWLEDGE_RECORDS_MANAGER`, `AGENT_WORKFLOW_OPERATOR`, `RISK_COMPLIANCE_AUDIT`.

## 4. Bảy gate tests

`mandate_authority`; `source_registry`; `context_selection`; `claim_grounding`; `compaction_handoff`; `memory_lifecycle`; `security_injection_audit`.

## 5. Nguồn kiểm tra ngày 22/08/2026

- W3C PROV-O: https://www.w3.org/TR/prov-o/ — provenance entities, activities, agents and derivation relationships.
- ISO 15489-1:2016: https://www.iso.org/standard/62542.html — concepts/principles for creating, capturing and managing records over time.
- NIST Privacy Framework: https://www.nist.gov/privacy-framework — voluntary enterprise privacy-risk language aligned to data lifecycle.
- OWASP LLM01:2025 Prompt Injection: https://genai.owasp.org/llmrisk/llm01-prompt-injection/ — direct/indirect injection; external content remains untrusted.

Các nguồn không define model context limits, source precedence, retention schedule or legal disposition for a specific organization; those require current contracts and authorized owners.
