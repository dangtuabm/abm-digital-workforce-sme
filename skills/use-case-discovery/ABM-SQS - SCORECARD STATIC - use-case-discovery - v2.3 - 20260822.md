---
document_code: "ABM-SQS-SC-90"
skill: "use-case-discovery"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — USE-CASE DISCOVERY v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh để khám phá use case từ outcome/value stream đến work moment, pain/evidence, data/system authority, output/action, human boundary, value hypothesis, basic screen, coverage/bias và validation backlog. Skill dừng trước score/rank/select; Skill 91 chịu trách nhiệm prioritization. D10 chưa đạt vì chưa pilot trên doanh nghiệp, value stream, vai trò, nguồn, systems, quyền, workload và opportunity thật; chưa có measured false trigger, token và duration.

Chuỗi kiểm định: `SKILL-CREATOR → CUSTOMER-XRAY → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 `designed_not_run` |
| SKILL-CREATOR quick_validate | PASS — `Skill is valid!` |
| Description | 479 ký tự, ≤ 600 |
| Body | 7.890 ký tự, ≤ 8.000 |
| Lines | 111, ≤ 500 |
| Evals | 12; must_trigger, must_not_trigger, no_false_ask, ambiguity, missing_input, red_line, injection, adversarial, coverage, solution_bias |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive fixture:** `READY_FOR_HUMAN_DISCOVERY_REVIEW`; 0 defect; 0 review gap. Coverage: 12 evidence sources, 10 work moments, 10 opportunities, 8 data/system maps, 10 basic screens, 8 coverage records, 8 validation items, 6 decisions, 10 test cases, 6 risks, 7/7 gate tests và 6/6 reviews.

**Negative fixture:** `NOT_READY`; 190 defects; 6 review gaps. Engine chặn missing contract/context/authority; invented process/pain/metric/ROI; sensitive inference; employee surveillance; job elimination; score/rank/select; vendor/architecture/automation approval; outreach/publication; bypass data rights; hidden conflict; evidence mutation; prompt injection và secret material.

## 4. Final Gatekeeper

- PASS boundary: opportunity discovery khác prioritization, business case, vendor selection, architecture và workflow build.
- PASS evidence: observed/documented/system-derived/self-reported/calculated/estimated/unverified tách riêng; conflict không bị làm phẳng.
- PASS work decomposition: outcome → value stream → role/user → job/task/decision → pain/evidence → output/action/consumer.
- PASS data authority: System of Record, owner, rights, classification, access, quality, integration và dependency hiển thị.
- PASS human control: không surveillance, sensitive inference, job elimination hoặc high-impact autonomy; action vẫn PENDING human authority.
- PASS bias control: coverage matrix, exception/source gaps, sponsor/office bias, dedupe và non-A.I alternatives bắt buộc.
- PASS handoff: chỉ `VALIDATE/DEFER/EXCLUDE`; score/rank/select được chuyển Skill 91.

## 5. Nguồn nội bộ sử dụng

- Bộ tiêu chuẩn Skill ABM và `SKILL-CREATOR` — cấu trúc, static gate, eval và D10.
- `CUSTOMER-XRAY` — logic investigation, evidence/source hierarchy và gap; không mang sales profiling/DISC vào discovery vận hành.
- `FINAL-GATEKEEPER` — boundary, negative controls, human authority và bàn giao.

Không dùng claim pháp lý, tiêu chuẩn hoặc thị trường bên ngoài trong nội dung Skill 90; mọi nguồn doanh nghiệp thật phải được kiểm quyền và phiên bản khi pilot.

## 6. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `8137BEEE079FAD5435A4417C90D6ACD1B236AA2C8B676A4A40D10217C5B5AEA3` |
| evaluator | `7657F1D4A53F4423D0C352C58A27A065F0570B6206E4208410341ACB8C74EE72` |
| evals | `9CFE724542CFF8F0C72ECA18CBAC41FDC8FE95F38C5E76B72F9942919A5B6C99` |
| positive fixture | `F8F80FA8AA8B7DE3138DBC28CCE7DF62377E0B6900A98B9D722742D273320EFF` |
| negative fixture | `1543EEDD722C04AB267C0D9514DEA613F3352595F0A7198EE4503CC7DE807E1C` |
| rules reference | `AA2676714BD9D20656794FDE9011349B486DC7B0296C509AD1266E2D916FFC7C` |
| pack template | `411AF6F0C8316A23636296E0E158FCBE9CFE4735200418997D58E4C4EB3DBC76` |

## 7. Cổng còn thiếu

D10 cần pilot trên discovery mandate, value streams, roles/users, work evidence, systems/rights, pain/workload, opportunities và validation owners thật. Sáu owner phải xác nhận traceability, coverage/bias, data authority, human boundary, value hypotheses và alternatives; kèm false trigger, token và duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.

