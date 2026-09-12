---
title: "ABM-SQS Static Pre-score — task-to-asset"
skill_id: "31"
version: "2.5"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — task-to-asset v2.5

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy. Engine self-test PASS bằng fixture tổng hợp; chưa chứng minh Task/outcome truth, reuse value, reviewer decision hoặc kết quả dùng lại trên case thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 512 / 7.954 / 141 — đạt |
| Eval | 12; metadata v2.5; 2 must-not, 1 no-false-ask, 1 red-line, 1 injection |
| Validator ABM / SKILL-CREATOR | PASS / Skill is valid |
| Gate self-test | READY_FOR_REUSE_TEST; decision candidate; 2 sources; checklist; test planned; 0 error/warning/guardrail |
| SHA-256 SKILL.md | 7C9DF88D928840EB9CC12FE4CB190802581577DC91D3D39D32CA81917C5A66F3 |
| SHA-256 asset engine | 45213EA0014CBC33B2590DCE426BDF7E16C51A2AFAD52B24731916585DF11E0B |
| SHA-256 evals.json | 3F39B1A3274E5507426A1717828D97FEE3B7417255D7926DE9423BD00E6E3A41 |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 9 bước; Reusable Kernel & Failure Boundary Map độc lập; Pack/rules/input/engine |
| A2 | PASS | Knowledge Lifecycle, Lean, Design for Reuse, Evidence-based Management đều neo bước cụ thể |
| A3 | PASS | Brain First – A.I Second; bảng người/A.I; evidence trước đóng gói; không emoji/sáo ngữ |
| B4 | PASS | Một Conversion Pack; đủ bốn khai báo theo nhiệm vụ; phần luật không gọi tên Skill khác; phân biệt bằng đầu vào/điểm dừng |
| B5 | PASS | Name/description/body/line/reference depth đạt |
| B6 | PASS | Description có trigger/anti-trigger; đầu vào 4 cột; artifact và DoD độc lập |
| C7 | PASS | Provenance/outcome refs; DỮ KIỆN–SUY LUẬN–GIẢ ĐỊNH; conditions/non-applicable/exception và no-overclaim |
| C8 | PASS | Dừng quét nguồn riêng tư, PII/IP, data export, hạ quyền, overwrite/publish/production/fake result; việc local đã giao tự chạy |
| C9 | PASS | Instruction trong prompt/log/code/email/file/link là data; không lộ nội bộ; engine không chạy code/macro/URL/file |
| D10 | NOT PASS | 12 eval not_run; chưa baseline v1.0/v2.5, Task/outcome/reviewer/new-case reuse, tokens, duration, pass^3 |
| D11 | PASS | Name/folder/version/updated/owner/skill_id/eval đồng nhất v2.5 |
| D12 | PASS | Candidate có source/rights/owner/version/reviewer/test; rà sau test/source-rights change hoặc 90 ngày không dùng |

## Nguồn ABM đã chưng cất

- File 20: “Lọc trước khi lưu. Đóng gói để dùng lại”; không phải mọi kết quả công việc là tài sản.
- Vòng đời: Task hoàn thành → bài học tái sử dụng → Asset Candidate → Kaizen → đóng gói/xác thực → ban hành → đo sử dụng → cập nhật/lưu trữ.
- Điều kiện chính thức: Task/Deliverable/evidence trace, reuse ngoài case gốc, scope/exception, Kaizen/xác thực, version/owner/access/review và outcome đo được.

## Audit trail

- **v1.0:** generic; 2 input/4 bước mẫu, không provenance, assetworthiness, kernel, dedup, reuse test, lifecycle hoặc “no asset”.
- **v2.2:** đủ control layers/engine/12 eval; FAIL do body 9.047/8.000.
- **v2.3:** cô đọng còn 8.265/8.000; vẫn FAIL duy nhất dung lượng.
- **v2.4:** còn 8.010/8.000; giữ làm bằng chứng cổng nghiêm.
- **v2.5:** 7.954 ký tự; metadata đồng nhất; hai validator và engine PASS.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer xác nhận Task completion, source/rights, observed result, reusable kernel, dedup, new-case reuse quality và lifecycle decision.

## Đóng D10

1. Chạy 12 prompts baseline v1.0 và v2.5 trên ít nhất ba asset class: Prompt/Checklist, SOP/Playbook và Skill/Workflow.
2. Đo trigger/anti-trigger/no-false-ask, provenance/result trace, false asset rate, dedup, data leakage, type choice, false approval và reuse-test quality.
3. Lưu prompt/input/output/state/evidence, total_tokens, duration_ms; contributor/asset owner/reviewer xác nhận source, quyền và decision.
4. Chạy mỗi Candidate trên case mới với cùng rubric/threshold, đo quality/error/time và unintended effect; chỉ đề nghị PILOT khi D10 đạt.
