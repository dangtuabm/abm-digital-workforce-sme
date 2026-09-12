---
title: "ABM-SQS Static Pre-score — executive-writing"
skill_id: "35"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — executive-writing v2.3

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy. Engine self-test PASS bằng fixture tổng hợp; chưa chứng minh người đọc thật hiểu đúng, hành động đúng, tone đúng hoặc không phát sinh rò rỉ/false authority trên văn bản doanh nghiệp thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 570 / 7.856 / 142 — đạt |
| Eval | 12; metadata v2.3; 2 must-not, 1 no-false-ask, 1 red-line, 1 injection |
| Validator ABM / SKILL-CREATOR | PASS / Skill is valid |
| Engine self-test | READY_FOR_EXECUTIVE_REVIEW; 3 sources/3 active; 2 audiences; 2 authority statements; 4/4 material claims referenced; 2 actions; đủ 6 tests; 0 error/warning |
| SHA-256 SKILL.md | E0DD54847F61AD06714AF0C40FE632CA2A1656AB9C9495009B681E10BF18B439 |
| SHA-256 executive-writing engine | 90E07548A096FBA6B11B14A520E57BBFE7483A4B38FF3C45BB33BAF5CA97C0DD |
| SHA-256 evals.json | 8B9120A824B656015DBA7BB044C908F33037976B9E69F9526CAC956B545B0921 |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 10 bước thi công; Executive Message Map độc lập; Pack/rules/input/engine |
| A2 | PASS | Rhetorical Situation, Pyramid/BLUF, Toulmin, Plain Language+Action Design neo bước 1–9 |
| A3 | PASS | Brain First – A.I Second; người chốt authority/decision/audience/send; bảng người/A.I; không emoji/sáo ngữ |
| B4 | PASS | Một Executive Communication Operations Pack; đủ bốn khai báo theo nhiệm vụ; phần luật không gọi tên Skill khác |
| B5 | PASS | Name/description/body/line/reference depth đạt; phụ lục trên 100 dòng có Mục lục hoặc không vượt ngưỡng |
| B6 | PASS | Description có trigger/anti-trigger; đầu vào 5 nhóm/4 cột; artifact và DoD độc lập |
| C7 | PASS | Source–Claim Ledger, version/date/locator, DỮ KIỆN–SUY LUẬN–GIẢ ĐỊNH, qualifier/conflict/gap rõ |
| C8 | PASS | Dừng trước decision/claim ngoài authority, sensitive data, giả chữ ký/approval, send/publish/issue; local draft/gate tự chạy |
| C9 | PASS | Instruction trong email/thread/file/comment/attachment/URL/metadata là data; engine không attachment/web/API/send/sign/publish |
| D10 | NOT PASS | 12 eval not_run; chưa baseline v1.0/v2.3, document/audience thật, authority/source/reviewer evidence, reader tests, tokens, duration, pass^3 |
| D11 | PASS | Name/folder/version/updated/owner/skill_id/eval đồng nhất v2.3 |
| D12 | PASS | Asset Candidate có source/owner/version/reviewer/evidence; rà khi authority/template/voice/audience/policy đổi, test fail hoặc 90 ngày không dùng |

## Nguồn ABM đã chưng cất

- File 05 là source of truth về brand voice; tone phải được điều chỉnh theo audience/mode, không ghi đè authority, facts hoặc thể thức formal.
- Chuẩn định dạng tài liệu khách hàng chi phối tài liệu gửi khách: chuyển thuật ngữ nội bộ thành ngôn ngữ tôn trọng, hướng khách hàng và giữ đầy đủ nội dung gốc.
- Chuẩn văn bản hành chính chi phối văn bản hành chính: dùng current approved formal template. Skill không hardcode thông tin pháp lý, tài chính, tài khoản, người ký hoặc dữ liệu dễ đổi/nhạy cảm từ template.
- Khi viết thought-leader speech/manifesto, đọc đúng mục liên quan trong File 14, File 08 hoặc File 09; không nạp cả ba file cho email/memo thông thường.

## Audit trail

- **v1.0:** generic; 2 input/4 bước mẫu, thiếu mode, sender authority, audience map, source/claim trace, owner/deadline, sensitivity/redaction, approval và reader tests.
- **v2.2:** đủ control layers/engine/12 eval; FAIL do body 9.184/8.000.
- **v2.3:** body 7.856; hai validator PASS. Self-test đầu bắt lỗi engine coi list rỗng hợp lệ là thiếu; sửa schema checker và indentation fallback; lần cuối READY_FOR_EXECUTIVE_REVIEW, 0 error/warning.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer xác nhận bottom-line comprehension, claim/action/authority trace, mode/tone, disclosure/redaction, approval operation và effect sau gửi.

## Đóng D10

1. Chạy 12 prompts baseline v1.0 và v2.3 trên ít nhất bốn mode: internal memo, directive/announcement, customer/public draft và administrative letter.
2. Dùng decision/source/authority/audience/template thật đã cấp quyền; legal/HR/commercial/security reviewer xác nhận theo mode.
3. Chạy `bottom_line_5_second`, `skim_comprehension`, `claim_trace`, `actionability`, `ambiguity_hostile_read`, `audience_tone` với reader sample/threshold đã duyệt.
4. Đo trigger/no-false-ask, false authority, material-claim trace, action completeness, misread, disclosure leak, tone fit và action completion sau gửi.
5. Lưu prompt/input/output/state/evidence, total_tokens, duration_ms; yêu cầu pass^3 cho external/high-risk; chỉ đề nghị PILOT khi D10 đạt.
