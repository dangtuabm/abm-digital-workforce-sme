# Finance & Accounting Rules — v2.3

## 1. Thứ tự sự thật

1. Entity-specific law, tax and reporting basis current at `as_of`.
2. Approved accounting policies, Chart of Accounts (COA – hệ thống tài khoản), materiality, period lock and authority matrix.
3. Authorized system-of-record snapshots and immutable source documents.
4. Reconciled subledgers, bank records and operational evidence.
5. Human assertions, OCR and model inferences — always labelled, never promoted without verification.

IFRS Conceptual Framework, IAS 7 and COSO are principle references only. They do not override the entity's applicable law, reporting basis, tax rules, COA or policy.

## 2. Accounting contract

- Identity: entity/legal unit, branch, consolidation boundary, counterparty and intercompany relation.
- Time: transaction/document/posting/due dates, reporting period, cutoff, timezone, open/locked/closed state.
- Value: transaction/base currency, gross/net/tax, approved exchange-rate source/date and rounding.
- Classification: account, subaccount, department/cost center/project/product, tax code and policy citation.
- Evidence: source ID/hash/version/as-of, system of record, document–transaction–journal links, rights and confidence.
- Authority: preparer, reviewer, approver, poster, payment maker/checker, period controller and tax/reporting authority.

Missing contract fields remain `UNKNOWN` and create a review gap; never silently default.

## 3. Document and transaction controls

- OCR is a draft extraction. Preserve original, extracted field, confidence, correction and reviewer.
- Detect duplicate by document ID, supplier/customer, date, amount, currency, bank reference and content hash; ambiguous matches stay queued.
- One transaction may have many sources; one source may support many lines. Preserve cardinality and allocations.
- Reject mixed entity, currency, period or tax basis unless an explicit transformation/reconciliation explains it.
- Never create or alter source evidence to make a reconciliation pass.

## 4. Journal draft rules

- Draft only; each journal has rationale, policy/source IDs, transaction IDs, date/period/currency, debit lines, credit lines, reviewer and `PENDING` state.
- Debit total equals credit total in relevant currency/base currency after documented rounding.
- Unsupported account, tax, accrual, reclass, FX or intercompany treatment is a decision gap.
- A locked/closed period is immutable to this Skill. Propose treatment in an authorized open period and route it.
- Reversal, recurring and adjusting entries require explicit basis, effective period and authority.

## 5. Reconciliation rules

- Declare equation, populations, snapshot dates, tolerance basis, matching keys and completeness tests.
- Opening balance + authorized movements = closing balance; explain every transformation.
- Keep matched, timing, known exception, suspected duplicate, disputed and unknown buckets separate.
- Every unmatched material item has amount/currency/age/source/owner/next evidence/due decision.
- Critical reconciliation does not pass by averaging or netting unrelated differences.

## 6. AR/AP, cash and budget rules

- Aging bucket definitions come from approved policy; due date source and disputed/credit/refund/chargeback states remain visible.
- Cash actual is bank/cash evidence; cash forecast is a scenario with horizon, assumptions, sources, trigger and uncertainty.
- Budget, actual and forecast must share entity, currency, period, account/metric definition and consolidation treatment before variance.
- Variance shows formula, denominator and basis. Root-cause labels are hypotheses until evidence supports them.
- No analysis can approve payment, change terms, modify budget or contact an external party.

## 7. Control and SOD rules

- Separate create/master-data, prepare, review, approve, post, pay, reconcile and audit roles according to local authority matrix.
- Detect self-approval, approval-limit bypass, split payment, bank/master-data change, duplicate, override, unusual timing/value and missing evidence.
- A signal is not a fraud finding. Preserve alternative explanation and route sensitive investigation.
- Critical control requires owner, event/frequency, evidence, pass/fail, failure action and residual risk.

## 8. Stop conditions

Stop at `NOT_READY` for missing entity/basis/period/COA/materiality/authority, unavailable critical source, unresolved material mismatch, unbalanced draft, locked-period mutation request, unsafe data transfer, hidden exception or execution request.

Final state can only be `READY_FOR_HUMAN_FINANCE_ACCOUNTING_DECISION`; all posting, payment, filing, publishing and certification remain outside.
