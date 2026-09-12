---
document_code: "ABM-SQS-SC-86"
skill: "context-management"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — CONTEXT MANAGEMENT v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh để quản trị mandate/authority, nguồn và provenance, working set, claim-evidence, quyết định/TBD, context budget, compaction loss, branch/handoff, durable-memory candidate và retention/archive/delete review. D10 chưa đạt vì chưa có baseline/with-skill pilot trên nguồn, quyền, provider context limit, quy trình bàn giao, memory store và records policy thật; chưa có measured false trigger, token và duration.

Chuỗi kiểm định: `SKILL-CREATOR → NOTEBOOKLM-DESIGN → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 `designed_not_run` |
| SKILL-CREATOR quick_validate | PASS — `Skill is valid!` |
| Description | 565 ký tự, ≤ 600 |
| Body | 7.965 ký tự, ≤ 8.000 |
| Lines | 99, ≤ 500 |
| Evals | 12; trigger, must_not_trigger, no_false_ask, ambiguity, red_line, injection, adversarial |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive fixture:** `READY_FOR_HUMAN_CONTEXT_DECISION`; 0 defect; 0 review gap. Coverage: 8 sources, 10 context items, 8 claim-evidence records, 6 decisions, 6 TBD, 4 compaction records, 4 branch/handoffs, 6 memory candidates, 6 lifecycle actions, 10 test cases, 6 risks, 7/7 gate tests và 6/6 reviews.

**Negative fixture:** `NOT_READY`; 182 defects; 6 review gaps. Engine chặn thiếu mandate/authority/budget/source metadata; nguồn hoặc quyết định bịa; conflict bị giấu; source overwrite; rights bypass; tiết lộ prompt/reasoning; mở rộng dữ liệu nhạy cảm; chuyển context qua boundary; tự promote memory; archive/delete/mutate evidence; secret material; auto approval và thiếu mọi review bắt buộc.

## 4. Final Gatekeeper

- PASS authority: precedence được tách theo data type; xung đột dừng tại human owner, không dùng “mới hơn” thay cho “có thẩm quyền hơn”.
- PASS provenance: source registry giữ locator, owner, rights, class, version/hash, as-of/effective, scope, quality, supersedes, retention và provenance.
- PASS context control: active/excluded/retrieve-on-demand có lý do, pointer và claim scope; context budget không hardcode giới hạn model.
- PASS continuity: compaction khai báo mất mát và recovery; handoff giới hạn recipient, rights, security zone, expiry, revalidation và merge/close.
- PASS lifecycle: memory chỉ là candidate; promote/transfer/archive/delete/overwrite đều PENDING human approval và post-action verification.
- PASS safety: không tiết lộ hidden prompt/reasoning, không coi retrieved content là instruction, không mở rộng quyền hoặc tự thay đổi record.

## 5. Nguồn chính thức kiểm tra ngày 22/08/2026

- W3C PROV-O: https://www.w3.org/TR/prov-o/
- ISO 15489-1:2016 Records management: https://www.iso.org/standard/62542.html
- NIST Privacy Framework: https://www.nist.gov/privacy-framework
- OWASP LLM01:2025 Prompt Injection: https://genai.owasp.org/llmrisk/llm01-prompt-injection/

Các nguồn hỗ trợ provenance, records controls, privacy-risk management và prompt-injection controls. Chúng phải được tailor theo nguồn, quyền, records policy, provider limit và security boundary thực tế; không chứng nhận compliance, completeness, privacy, security hay lossless compaction.

## 6. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `C87D79C607F0DB3C8515E90CBD222B744F5CC80452FEA3EBD49669A36BF8CF71` |
| evaluator | `78B73635A1151C882D02242E22A6AF0616C7B0DE06A84EA8E5D88FA53D66AFA6` |
| evals | `E2709895051A9FB4891448E76D3D457F653193E3BD5E97371503ED8A69B5481E` |
| positive fixture | `DBE1FC518B1B598B453F4CE397993203EFEB81F88998849F4758687032DC5CB4` |
| negative fixture | `E1F07157F6BFE636A0C9276B11B676BA43C2A164C7C4E24E33960CE61E7C596B` |
| rules reference | `C99321DEB2315071E0E9670B1077C9EA0F71D8B6C631DD511718A7E4404BED4E` |
| pack template | `D8BAA5145961F8541D31C6147152B93ABE59AF6786F64DCF571BB53C698B658D` |

## 7. Cổng còn thiếu

D10 cần pilot trên task dài/nhiều nguồn/nhiều phiên hoặc Agent thật; dùng authority map, source registry, provider limit, compaction/branch/handoff, memory store, privacy/security và records policy thật. Sáu owner phải xác nhận quyền, coverage, loss/recovery, handoff boundary, retention/promotion/archive/delete và audit evidence; kèm false trigger, token và duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.
