---
document_code: "ABM-SQS-SC-98"
skill: "ai-governance"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — A.I GOVERNANCE v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh cho mandate, inventory/lineage/lifecycle, data–action–impact, applicability, risk/tier, policy–control–enforcement–evidence, authority/SoD, disclosure/provenance, audit, vendor, monitoring, incident/rollback, exception và reporting. Skill không ban hành policy, chứng nhận compliance, cấu hình enforcement hay thực hiện external action. D10 chưa đạt vì chưa pilot trên hệ thống doanh nghiệp thật.

Chuỗi: `SKILL-CREATOR → A.I-GOVERNANCE-TRAIL → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 chưa có baseline/evidence/tokens/duration |
| SKILL-CREATOR quick_validate | PASS |
| Description | 538 ký tự, ≤ 600 |
| Body | 7.971 ký tự, ≤ 8.000 |
| Lines | 102, ≤ 500 |
| Evals | 12; trigger/must_not_trigger/routing/no_false_ask/ambiguity/missing/red_line/injection/inventory-risk/policy-enforcement/audit-incident-exception/vendor-lifecycle |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive:** `READY_FOR_HUMAN_GOVERNANCE_DECISION`; 0 defect; 0 review gap. Coverage: 12 evidence sources, 10 inventory records, 8 obligations, 8 risk assessments, 12 controls, 10 authority rules, 10 audit events, 6 incident controls, 6 exception controls, 8 monitoring controls, 12 test cases, 6 decisions, 6 risks, 7/7 tests và 6/6 reviews.

**Negative:** `NOT_READY`; 104 defects; 6 review gaps. Chặn inventory thiếu nhưng nhận complete; UNKNOWN thành compliant; legal opinion/certification giả; fixed 80/20/tier/SLA/label/tool/stop-word; critical-gate washing; paper control; evidence bịa/backdate; audit tự sửa/xóa; incident bị che; exception mở/tự duyệt; residual risk tự chấp nhận; policy enactment, permission/start/stop/notify/sign/purchase/publish/decommission trái quyền; injection và secret material.

## 4. Final Gatekeeper

- PASS mandate/inventory: entity, scope, jurisdiction, owners, rights, DoD, asset/version/lineage/lifecycle và unknown-gap rule.
- PASS applicability/risk: current official/contract source, effective scope/date, qualified owner, conflict/UNKNOWN, method/rationale/confidence và critical gate.
- PASS control/authority: requirement–control–enforcement–test/evidence, owner/frequency/remediation; ALLOW/CONDITIONAL/DENY, SoD và Human Control.
- PASS disclosure/audit: provenance, audience/policy owner, tamper control, minimization/access/retention, before–action–after verification.
- PASS operations/lifecycle: vendor/exit, evaluation/drift, incident/rollback/re-entry, exception expiry/closure, admission/change/canary/recertification/suspend/decommission.

## 5. Nguồn specialist được sửa cứng

Giữ nguyên lõi `AI-GOVERNANCE-TRAIL`: quản trị theo rủi ro, Ranh giới Đỏ, Human Control, nhật ký kiểm toán, incident và cải tiến liên tục. Chuyển các giả định 80/20, ba tier, SLA 2h/24h, nhãn, stop-word, thời lượng đào tạo và Notion/Google Sheet thành control có scope/source/owner/evidence hoặc cấu hình do authority phê duyệt; bổ sung inventory/lineage, applicability register, policy-to-control enforcement, SoD, vendor assurance, exception và lifecycle. Không tuyên bố một pattern ngành/công cụ là universal rule.

## 6. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `9EACBC0C33D59233AAC249FBF00FF1A1FBAEF8FE60E045AFC33C80EB9121DD42` |
| evaluator | `CA90EF570E6AAAA33E75D1BECBA088EEE6604D00AAF9C9AE1F2BF369E0388250` |
| evals | `F971D5222E3EE9B96B52EE53F5DACB96628903C217A6773630A64AE608CBC18D` |
| positive fixture | `50AD42574F8D67F997BAA1DBE2546ADD52E2D3B5B55FD376C4099C8EE74FBA03` |
| negative fixture | `24F626DE8C45B34B0B1EDF1F0A87F38A57AB30F596B7C91732FB1D3C135DCF95` |
| rules | `D91964AEE98AD33B0D957941C56BB7693AF72704EBBD8CDEB06723716C15D795` |
| template | `44C48AF550CE3638D01C14869732C5E24C2CC947B7070CECB8860797B9B38CCA` |

## 7. Cổng còn thiếu

D10 cần pilot trên inventory và hệ thống A.I thật với applicability do qualified owners xác nhận, control-enforcement evidence, authority/SoD, audit integrity, vendor change, monitoring/drift, incident/rollback, exception expiry và lifecycle/decommission; đo false trigger, token và duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.
