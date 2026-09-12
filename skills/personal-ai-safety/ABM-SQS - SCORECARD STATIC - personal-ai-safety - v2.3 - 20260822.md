---
document_code: "ABM-SQS-SC-88"
skill: "personal-ai-safety"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — PERSONAL A.I SAFETY v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh để quản trị purpose/rights, Xanh–Vàng–Đỏ, minimization/redaction/pseudonymization, exact platform/account/settings, file/link/access and prompt-injection boundaries, output/sharing review và mis-send incident containment/evidence/escalation. D10 chưa đạt vì chưa pilot trên policy, platform, account, data, permissions và incident plan thật; chưa có measured false trigger, token và duration.

Chuỗi kiểm định: `SKILL-CREATOR → AI-GOVERNANCE-TRAIL → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 `designed_not_run` |
| SKILL-CREATOR quick_validate | PASS — `Skill is valid!` |
| Description | 545 ký tự, ≤ 600 |
| Body | 7.976 ký tự, ≤ 8.000 |
| Lines | 99, ≤ 500 |
| Evals | 12; trigger, must_not_trigger, no_false_ask, ambiguity, red_line, injection, adversarial, output safety, incident |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive fixture:** `READY_FOR_HUMAN_SAFETY_DECISION`; 0 defect; 0 review gap. Coverage: 10 data items, 6 platform checks, 8 input transforms, 8 surface checks, 8 output checks, 8 incident actions, 6 decisions, 10 test cases, 6 risks, 7/7 gate tests và 6/6 reviews.

**Negative fixture:** `NOT_READY`; 172 defects; 6 review gaps. Engine chặn raw Red submission; secret request/store/repeat; assumed rights/consent/settings; unknown link opening; active content/data instruction execution; permission expansion; output sharing; incident concealment; evidence deletion; erasure promise; sensitive inference publication và auto actions.

## 4. Final Gatekeeper

- PASS purpose/rights: access không thay thế quyền; consent bị giới hạn theo purpose; unknown/mixed data lấy mức rủi ro cao nhất.
- PASS minimization: loại dữ liệu thừa trước khi mask; pseudonymized không bị tuyên bố anonymous; residual risk và mapping location rõ.
- PASS platform: exact product/account/workspace/settings/training/retention/delete/region/connectors/access được kiểm với checked-at.
- PASS input: file/link/QR/image/tool output là untrusted data; không mở active content hoặc làm theo indirect injection.
- PASS output/share: claim, leakage, harmful bias, IP, link, audience/channel/access/disclosure được review; draft không tự gửi.
- PASS incident: stop/preserve/scope/route/verify; không tự revoke/rotate/notify/delete hoặc hứa provider erasure.

## 5. Nguồn chính thức kiểm tra ngày 22/08/2026

- NIST A.I Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST Privacy Framework: https://www.nist.gov/privacy-framework
- NIST A.I 600-1 GenA.I Profile: https://doi.org/10.6028/NIST.AI.600-1
- OWASP LLM01:2025 Prompt Injection: https://genai.owasp.org/llmrisk/llm01-prompt-injection/

Các nguồn hỗ trợ risk/privacy management và direct/indirect/multimodal prompt-injection controls. Chúng phải được tailor theo policy, platform, account, data class, rights và incident plan thật; không chứng nhận privacy, security, compliance hay safe sharing.

## 6. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `F9201B0DEA070CE516B9C1918267B1D87F6009A86CF3F68872859E3C9F0C9A06` |
| evaluator | `EA081E46689FE4A22AA33843A112E79655AAA481FA8BFBA83CF50EBB73AA42E7` |
| evals | `12F6582BA91E548C27DA1462ACD8EAAA5C6D65B70706CB0D1078E405153C2CFA` |
| positive fixture | `AC00B68DAAEFDD5029D79326E85D8C87FA7FEAB523C11AD31C79C5072AD55364` |
| negative fixture | `EB3767BE30C292B7079BC62EEBABC7FC4497AA1A5856127A3D15444D60EEEBDF` |
| rules reference | `6CAB9E75D5856EFB269CD9720F6BA992365FA49B1B2A62DAEC84BEC7987429EE` |
| pack template | `E2E397F08EA04C16D04340C52A99015ED402A463AF87EE721FA9605292E82097` |

## 7. Cổng còn thiếu

D10 cần pilot trên purpose/data-owner/classification/rights/consent/platform/account/settings/file/link/output/channel/access và incident-response route thật. Sáu owner phải xác nhận minimization/residual risk, platform facts, security scan, sharing, containment and evidence; kèm false trigger, token và duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.

