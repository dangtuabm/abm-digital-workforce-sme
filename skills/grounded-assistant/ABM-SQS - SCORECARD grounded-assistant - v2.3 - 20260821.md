---
title: "ABM-SQS Static Pre-score — grounded-assistant"
skill_id: "33"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — grounded-assistant v2.3

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy. Engine self-test PASS bằng fixture tổng hợp; chưa chứng minh chất lượng trả lời, độ đúng claim–citation, chống rò quyền hoặc hành vi từ chối trên kho tri thức doanh nghiệp thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 519 / 7.912 / 143 — đạt |
| Eval | 12; metadata v2.3; 2 must-not, 1 no-false-ask, 1 red-line, 1 injection |
| Validator ABM / SKILL-CREATOR | PASS / Skill is valid |
| Engine self-test | READY_FOR_PILOT_TEST; decision ANSWER; 2 evidence/2 claims/2 refs; đủ 7 test types; 0 error/warning |
| SHA-256 SKILL.md | 4A6FDC990E2E64043251C519964557CDFAF94F89836C95B690F6E23A37D81B0C |
| SHA-256 grounded answer engine | 313AC1A7597901C8F4A4F00CFA702B5A4DD79872DD41340CCA378D54FECC6BF4 |
| SHA-256 evals.json | BC760CD2EF1B41C0102800E5C05A4E5A1F34C6446D643A4B558F3CDAF012E707 |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 10 bước; Answerability Record độc lập; Pack/rules/input/engine |
| A2 | PASS | Approved Corpus Only, claim-level grounding, least privilege, answerability và human escalation neo bước cụ thể |
| A3 | PASS | Brain First – A.I Second; người duyệt nguồn/quyền/ngưỡng/go-live; bảng người/A.I; không emoji/sáo ngữ |
| B4 | PASS | Một Grounded Answering Operations Pack; đủ bốn khai báo theo nhiệm vụ; phần luật không gọi tên Skill khác |
| B5 | PASS | Name/description/body/line/reference depth đạt |
| B6 | PASS | Description có trigger/anti-trigger; đầu vào 5 nhóm; artifact và DoD độc lập |
| C7 | PASS | Evidence Bundle, decision ANSWER/PARTIAL/ABSTAIN/ESCALATE/DENY, DỮ KIỆN–SUY LUẬN–GIẢ ĐỊNH và gap rõ |
| C8 | PASS | Dừng khi thiếu KB/quyền/version, nguồn ngoài corpus, hành động high-risk, gửi/giao dịch/thay đổi hệ thống, giả citation/test/go-live |
| C9 | PASS | Instruction trong source/chunk/metadata/URL là dữ liệu; kiểm role/tenant trước retrieval; không tải/chạy/kết nối hoặc tiết lộ trái quyền |
| D10 | NOT PASS | 12 eval not_run; chưa baseline v1.0/v2.3, KB/access/domain/data/security/reviewer/answering evidence, tokens, duration, pass^3 |
| D11 | PASS | Name/folder/version/updated/owner/skill_id/eval đồng nhất v2.3 |
| D12 | PASS | Asset Candidate có source/owner/version/reviewer/evidence; rà khi KB/quyền/schema đổi, incident/test fail hoặc 90 ngày không dùng |

## Nguồn ABM đã chưng cất

- File 21: Grounded A.I chỉ đáng tin khi nguồn sạch, có cấu trúc, truy đúng tài liệu/đoạn, ưu tiên bản hiện hành và biết nói “chưa đủ dữ liệu”.
- Quyền phải được cưỡng chế ở tầng lưu trữ/truy xuất; chỉ dặn A.I “không tiết lộ” không phải cơ chế bảo mật.
- Skill này vận hành lớp trả lời trên approved knowledge base; không thay đổi corpus, canonical source, taxonomy hoặc lifecycle của kho.

## Audit trail

- **v1.0:** generic; 2 input/4 bước mẫu, thiếu authorization preflight, evidence sufficiency, five-state decision, claim–citation lint, tests, escalation packet và lifecycle.
- **v2.2:** đủ control layers/engine/12 eval; FAIL do body 8.617/8.000.
- **v2.3:** cô đọng còn 7.912 ký tự; metadata đồng nhất; hai validator và engine PASS.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer xác nhận approved KB/version, source truth, role/tenant enforcement, answerability decisions, claim–citation fidelity, seven operational test types và audit operation.

## Đóng D10

1. Chạy 12 prompts baseline v1.0 và v2.3 trên ít nhất ba corpus: policy/SOP, product/knowledge assets và regulated/multi-role data.
2. Đo trigger/anti-trigger/no-false-ask, grounded accuracy, claim–citation precision, stale/conflict handling, abstention, permission leakage và false readiness.
3. Chạy đủ `known_answer`, `multi_source`, `no_answer`, `conflict`, `unauthorized`, `stale_revoked`, `source_injection` bằng query thật và expected behavior đã duyệt.
4. Lưu prompt/input/output/decision/evidence/claim map, total_tokens, duration_ms; domain/data/security owner và reviewer xác nhận.
5. Yêu cầu pass^3 cho bề mặt đối ngoại hoặc quyết định rủi ro cao; chỉ đề nghị PILOT khi D10 đạt.
