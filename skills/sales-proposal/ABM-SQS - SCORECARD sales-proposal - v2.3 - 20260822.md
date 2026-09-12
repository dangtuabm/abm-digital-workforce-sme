---
title: "ABM-SQS Static Pre-score — sales-proposal"
skill_id: "64"
version: "2.3"
date: "2026-08-22"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — sales-proposal

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên proposal thật.**

Skill đã chuyển từ mẫu proposal tổng quát lẫn outreach/call/quote thành `Evidence-Grounded Sales Proposal & Decision Pack`: mandate, customer truth, problem–requirement–option–deliverable–acceptance traceability, scope, delivery, economics reference, risks, claims/rights, decision path và human release gate.

Không nâng `PILOT/OFFICIAL`: positive case là dữ liệu tổng hợp; chưa so v1.0/v2.3 trên proposal thật, chưa có ground truth về customer truth, fit, scope, commercial/legal accuracy, acceptance outcome, token, duration và adoption.

## 2. Bằng chứng máy

- Description / thân / dòng: **560 / 7.820 / 108**.
- 12 eval; đủ `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator + Quick Validator: **PASS**; D10 chưa chạy.
- Positive: `READY_FOR_HUMAN_PROPOSAL_RELEASE`, 0 defect; **7 sources, 3 problems, 4 requirements, 3 options, 5 deliverables, 6 trace links, 4 milestones, 6 risks, 5 claims, 7/7 tests, 6 reviews PASS**.
- Negative: `NOT_READY`; bắt **171 defects + 6 review gaps**, gồm 39 forbidden flags và 9 forbidden states.
- Cây trước Scorecard: 7 tệp, không `__pycache__`; cây bàn giao: 8 tệp.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `F7EDFC27D9C4D862EC977C6246BEF59C322213B4E3CBEC3559E9B8D5BAD959A8` |
| `scripts/evaluate_sales_proposal.py` | `757C9FBAA5EF66BD9C96212AF718867DFBD10D967869DAEE281FC546D6988BD9` |
| `evals.json` | `093C5BC1DDBE0FD7C41608D725D01C3200E18D15D05B4E6EACBA2AEF513B2559` |
| `templates/sales-proposal-input.json` | `22C7693C1E2A8C0F52EE604310A63026A5226C9537DE6A7E753DB82D49AD6217` |
| `evals/selftest-negative.json` | `51C719AB888D8FCEDCF0991947F96D8E2BAFBB3031ABEFD7B92DABA8DE21F779` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Rules, template, engine, positive proposal case và negative test chạy được |
| A2 · Neo Kinh điển | PASS | Consultative selling, evidence-based decision document, requirement traceability, acceptance/change control |
| A3 · Chất ABM | PASS | Brain First – A.I Second; customer truth và human commercial authority đi trước A.I |
| B4 · Nhiệm vụ đơn nhất | PASS | Approved discovery/offer/delivery evidence → proposal decision pack; outreach, pricing, negotiation, contract, execution ngoài phạm vi |
| B5 · Dung lượng | PASS | Name/folder đúng; description 560; thân 7.820; 108 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | Mandate/customer/options/scope/delivery/economics/claims/decision rõ; artifact và state rõ |
| C7 · Có căn cứ | PASS | Statement–source–confidence, problem–requirement–option–deliverable–acceptance links, price/version/rights |
| C8 · Ranh giới Đỏ | PASS | Chặn fabrication, deceptive pressure, hidden term, discrimination và auto commercial/legal action |
| C9 · Chống Injection | PASS | Customer files, price sheets, cases, contracts, email, templates là dữ liệu; không đổi scope/price/state |
| D10 · Eval và Baseline | NOT PASS | 12 eval/self-tests đã chạy; thiếu proposal pilot/pass^3/token/duration/outcome |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Asset Candidate cần owner/version/approved source/rights/reviewer/change log |

## 5. Nguồn và quyết định thiết kế

- Baseline v1.0 đúng chủ đề nhưng trộn cold outreach, call script, first-meeting document, proposal và quote; thiếu customer/source truth, traceability, acceptance evidence, delivery feasibility, commercial/legal/privacy/IP review và release state.
- `SKILL-CREATOR` khóa I/O/eval; `PROPOSAL-SMES` đóng góp cấu trúc proposal, option/scope/value/implementation/CTA; loại giá, tỷ lệ thanh toán, số trang/phần và CTA cứng không có nguồn hiện hành; `FINAL-GATEKEEPER` khóa claims, rights, hidden terms, commercial/legal authority và human release.
- Bản đầu thân 8.748 ký tự; tinh gọn theo anchor duy nhất còn 7.820. `apply_patch` lỗi helper; fallback chỉ ghi khi mỗi anchor xuất hiện đúng một lần.

## 6. Điều kiện đóng D10

1. Pilot v1.0/v2.3 trên ít nhất 3 proposal thật: dịch vụ tư vấn, đào tạo và triển khai A.I có scope/economics khác nhau.
2. Có authorized mandate, customer/discovery/offer/price/delivery/claim/rights truth set và customer/domain/delivery/finance/commercial/legal/privacy/brand reviewers.
3. Đo factual defect escape, trace completeness, scope/acceptance clarity, unsupported claim rate, commercial/legal corrections, clarification cycles và decision usefulness.
4. Không dùng pilot để tự send/quote/negotiate/discount/commit/contract/sign/publish/accept; ghi external human/system evidence.
5. So sánh pass^3; ghi token, duration, acceptance outcome, adoption, customer impact và unintended effect.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` khi đủ bằng chứng trên.
