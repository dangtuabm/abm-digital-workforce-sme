---
title: "ABM-SQS Static Pre-score — contract-drafting"
skill_id: "76"
version: "2.3"
date: "2026-08-22"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — contract-drafting

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên giao dịch/hợp đồng thật.**

Skill đã chuyển từ khung 2-input/4-step thành Evidence-Grounded Contract Draft & Legal Review Pack: mandate/party/authority/jurisdiction, source-term ledger, commercial/obligation/risk matrices, clause positions, IP/data/confidentiality, term/exit/dispute, annexes/precedence, consistency/TBD audit, negotiation issues và human legal/signing decision.

Không nâng PILOT/OFFICIAL: positive case là dữ liệu tổng hợp; chưa so v1.0/v2.3 trên contract thật, chưa có current law/party authority/commercial ground truth, qualified counsel/counterpart outcome, execution evidence, token và duration.

## 2. Bằng chứng máy

- Description / thân / dòng: **514 / 7.903 / 104**.
- 12 eval; đủ must_not_trigger, no_false_ask, red_line, injection.
- ABM validator + Quick Validator: **PASS**; D10 chờ pilot.
- Positive: READY_FOR_HUMAN_LEGAL_CONTRACT_DECISION, 0 defect, 0 review gap; **8 sources, 2 parties, 12 term items, 10 commercial items, 10 obligations, 12 clause positions, 4 annexes, 10 consistency checks, 6 risks, 6 decisions, 7/7 tests, 6 reviews PASS**.
- Negative: NOT_READY; bắt **182 defects + 6 review gaps**, gồm 113 forbidden flags và 19 forbidden states.
- Cây trước Scorecard: 7 tệp, không __pycache__; cây bàn giao: 8 tệp.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| SKILL.md | 3561A76C9FB0A6F3156F301ED0B47C7CDEFD8A6CF14A49D4E01BEA6F933C0DBF |
| scripts/evaluate_contract_drafting.py | 3B1D295246B5EBB2CCBAD5010E6056CB6600D2DE5967F8A300165342B62D075D |
| evals.json | 512C8916E1B6B2B2589A5B8DE9B014897B8DE6D22F2A043D97B68FFDA7409435 |
| templates/contract-drafting-input.json | 293868DEFD615A2D2DB8DA8C2365DC8DC2FC0A651779AD61C00A9613EA7746EA |
| evals/selftest-negative.json | 67C49EFAEC64D2EDA605B37D78FFECF3A2F5A2DB4CA00D331C8510BEEEF1C858 |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Rules, review-pack template, runnable engine and integrated deal test cases |
| A2 · Neo Kinh điển | PASS | Formation/authority, performance/non-performance, commercial terms, risk allocation, term/exit, dispute and formalities |
| A3 · Chất ABM | PASS | Brain First – A.I Second; commercial intent, evidence, counsel and authority before clause automation |
| B4 · Nhiệm vụ đơn nhất | PASS | Authorized deal sources → contract draft/legal review pack; negotiation/acceptance/signature/execution outside |
| B5 · Dung lượng | PASS | Name/folder đúng; description 514; thân 7.903; 104 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | Mandate/parties/law/sources/commercial/risk → matrices, draft, annexes, issues and human decision |
| C7 · Có căn cứ | PASS | Source/version/rights/priority/status, party authority, term state and clause-position traceable |
| C8 · Ranh giới Đỏ | PASS | Chặn fabricated legal/commercial terms, hidden redlines/TBDs and 19 communication/acceptance/signature/execution states |
| C9 · Chống Injection | PASS | RFP/proposal/template/prior-contract/redline data cannot order disclosure, term change, review bypass or signature |
| D10 · Eval và Baseline | NOT PASS | 12 eval/self-tests chạy; thiếu real baseline, pass^3, counsel/counterpart/execution evidence, token và duration |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; draft/review/decision state rõ |
| D12 · Kaizen | PASS | Clause/playbook asset cần owner, jurisdiction/scope, source/rights, positions, counsel, tests and change log |

## 5. Nguồn và quyết định thiết kế

- Baseline v1.0 đúng về loại văn bản, commercial brief, rights/obligations, payment, exceptions, annexes and legal confirmation nhưng chỉ 2 input/4 bước/5 eval; chưa có party/authority/law, term states, clause trace, negotiation positions, TBD/consistency or execution states.
- CONTRACT-DRAFT là nguồn chuyên môn chính: giữ clear CEO language, scope/exclusions, milestones/acceptance, IP/NDA, warranty/termination/liability, annexes and counsel gate. Loại đúng 3 loại/9 phần, 40–40–20, 30–90 ngày, notice 30 ngày, absolute symmetry, fixed refund conditions and no-placeholder-at-any-cost.
- UNIDROIT Principles 2016 được dùng như non-binding commercial-contract issue framework; UNCITRAL electronic-commerce/automated-contracting texts cho functional equivalence, technology neutrality and automated-formation issue spotting. Applicability/enforceability vẫn thuộc current law and counsel.
- SKILL-CREATOR khóa I/O/eval; FINAL-GATEKEEPER khóa party authority, term conflicts/TBD, privilege/confidentiality, negotiation and execution states.

## 6. Điều kiện đóng D10

1. Pilot v1.0/v2.3 trên ít nhất 3 giao dịch thật: services/SOW, data/IP/security-heavy và cross-border/e-sign or complex amendment.
2. Có verified party/authority, current law/formality, approved commercial terms, source priority, counsel, finance/tax/data/delivery and signing reviewers.
3. Đo missing/contradictory terms, clause/source defects, crossref/defined-term/TBD errors, review time, redline acceptance and post-draft dispute/prevented-risk signals.
4. Không dùng pilot để send/offer/accept/negotiate/approve/sign/e-sign/execute/pay/file/contact/certify; chỉ ghi external evidence do đúng authority tạo.
5. So sánh pass^3; ghi token, duration, counsel corrections, counterpart outcomes, confidentiality/security incidents and unintended effects.

**Cổng hiện tại:** STATIC PASS. Chỉ chuyển PILOT khi đủ bằng chứng trên.
