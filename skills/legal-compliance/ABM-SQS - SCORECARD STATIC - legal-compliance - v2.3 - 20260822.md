---
document_code: "ABM-SQS-SC-77"
skill: "legal-compliance"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — LEGAL COMPLIANCE v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh để lập legal register, đánh giá applicability, truy vết obligation–process–owner–control–evidence–test, quản lý incident/change/remediation và dừng tại quyết định pháp lý/tuân thủ của con người. D10 chưa đạt vì chưa có baseline/with-skill pilot trên hồ sơ doanh nghiệp thật, ground truth của counsel, evidence, token và duration.

Chuỗi kiểm định: `SKILL-CREATOR → AI-GOVERNANCE-TRAIL → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 `designed_not_run` |
| SKILL-CREATOR quick_validate | PASS — `Skill is valid!` |
| Description | 492 ký tự, ≤ 600 |
| Body | 7.937 ký tự, ≤ 8.000 |
| Lines | 102, ≤ 500 |
| Evals | 12; có trigger, must_not_trigger, no_false_ask, ambiguity, red_line, injection, adversarial |
| Artifact tree | 8 file; 0 `__pycache__` |

## 3. Self-test engine

**Positive fixture:** `READY_FOR_HUMAN_LEGAL_COMPLIANCE_DECISION`; 0 defect; 0 review gap. Coverage: 7 sources, 8 applicability records, 10 obligations, 10 controls, 10 evidence tests, 4 exceptions/incidents, 4 regulatory changes, 5 remediations, 6 risks, 6 decisions, 7/7 tests và 6/6 reviews.

**Negative fixture:** `NOT_READY`; 175 defects; 6 review gaps. Engine chặn fabrication, source/applicability mixing, tự chứng nhận/nộp báo cáo, tự liên hệ cơ quan, nhận vi phạm, điều tra/kỷ luật, thay đổi control/system, sửa/xóa evidence, waive privilege và auto closure.

## 4. Final Gatekeeper

- PASS logic: applicability không bị đồng nhất với compliance; control design tách operating effectiveness; allegation tách fact; draft filing tách filed.
- PASS authority: legal counsel, compliance owner, reporting authority, audit/assurance và privacy/security có review gate; final decision luôn `PENDING`.
- PASS trace: source → applicability → obligation → process/owner/authority → control → evidence/test → finding/change/remediation/decision.
- PASS security: prompt/data injection, privilege, reporter identity, PII, evidence custody, retention và audit-log mutation được chặn.
- PASS current-source boundary: ISO/OECD/DOJ chỉ là scoped references; official law/regulator/local counsel hiện hành kiểm soát.

## 5. Nguồn chính thức kiểm tra ngày 22/08/2026

- ISO 37301:2021: https://www.iso.org/standard/75080.html
- OECD Guidelines for Multinational Enterprises on Responsible Business Conduct, 2023: https://www.oecd.org/en/publications/oecd-guidelines-for-multinational-enterprises-on-responsible-business-conduct_81f92357-en.html
- U.S. DOJ Evaluation of Corporate Compliance Programs, September 2024: https://www.justice.gov/criminal/criminal-fraud/page/file/937501

Các nguồn này hỗ trợ nguyên tắc quản trị, không tự xác định luật áp dụng, certification hay legal opinion cho doanh nghiệp cụ thể.

## 6. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `DB2FE3A09E86716612F07E8B5FF58C4E7BBE8C40871845475D709A5C99103DB7` |
| evaluator | `E5A9B69556DCD91C7A48B906ED875E29BF3465B4203A72E444D8958597277191` |
| evals | `DF6D3B37D49CF8766470F056B51590951FA7903EBA5A0AAED831555BC5E78472` |
| positive fixture | `E9DA731E5C922E325E70DF5694F8E2B1015D5BDAAEC45C87671D47A20BE75FA9` |
| negative fixture | `BC079B7169D2E9F19B3584C9075A80E0ACB23497A3DB55CC3487FC8C175C8D17` |
| rules reference | `67C849F8555D44FB83FA42D785FE11EE85E03036D19B163BDCE061F54035944A` |
| pack template | `0C4344840BCBE026CD9955C14B1D65770C500B963D3A68592A68B293B12B706D` |

## 7. Cổng còn thiếu

D10 cần pilot trên legal register và control evidence thật, có qualified local counsel/compliance owner xác nhận: source completeness/freshness, applicability, obligation trace, control design/operation, evidence sufficiency, incident/change route, false trigger, token và duration. Chỉ sau D10 và phê duyệt của Sếp mới được xem xét PILOT/OFFICIAL.
