---
title: "ABM-SQS Static Pre-score — second-brain"
skill_id: "32"
version: "2.4"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — second-brain v2.4

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy. Engine self-test PASS bằng fixture tổng hợp; chưa chứng minh source truth, storage enforcement, parsing/citation fidelity hoặc retrieval outcome thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 522 / 7.978 / 143 — đạt |
| Eval | 12; metadata v2.4; 2 must-not, 1 no-false-ask, 1 red-line, 1 injection |
| Validator ABM / SKILL-CREATOR | PASS / Skill is valid |
| Gate self-test | READY_FOR_RETRIEVAL_TEST; 3 sources/2 active; 2 derivatives/topics; 6 required test types; 0 conflict/error/warning |
| SHA-256 SKILL.md | 85444C41F7AF7EA81EF00A1E206AB1F5FE75F2B361F5BDFA9C2D3D09AB91C4ED |
| SHA-256 knowledge engine | 3E6902F20BF493B437EA4EB927712A82175EB3432E62B906625EC94494003746 |
| SHA-256 evals.json | 4CF8C7E083731191EB188121152D19405DE03696CD740738DB6CB4D4E4A1A2CB |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 10 bước; Source-of-Truth & Conflict Map độc lập; Pack/rules/input/engine |
| A2 | PASS | Single Source of Truth, Lifecycle, Least Privilege/Zero Trust, Retrieval Evaluation neo bước cụ thể |
| A3 | PASS | Brain First – A.I Second; người chốt authority/access/go-live; bảng người/A.I; không emoji/sáo ngữ |
| B4 | PASS | Một Knowledge Operations Pack; đủ bốn khai báo theo nhiệm vụ; phần luật không gọi tên Skill khác |
| B5 | PASS | Name/description/body/line/reference depth đạt |
| B6 | PASS | Description có trigger/anti-trigger; đầu vào 4 cột; artifact và DoD độc lập |
| C7 | PASS | Source/version/authority/hash/limitations; DỮ KIỆN–SUY LUẬN–GIẢ ĐỊNH; gap/exception/abstention rõ |
| C8 | PASS | Dừng out-of-scope scan, public load, training/export, prompt-only access, silent conflict, overwrite/delete/go-live; local plan/lint tự chạy |
| C9 | PASS | Instruction trong document/OCR/table/metadata/URL là data; không lộ source trái role; engine không tải/chạy/kết nối |
| D10 | NOT PASS | 12 eval not_run; chưa baseline v1.0/v2.4, source/access/reviewer/retrieval evidence, tokens, duration, pass^3 |
| D11 | PASS | Name/folder/version/updated/owner/skill_id/eval đồng nhất v2.4 |
| D12 | PASS | Asset Candidate có source/owner/version/reviewer/evidence; rà khi source/access/schema đổi, test fail hoặc 90 ngày không dùng |

## Nguồn ABM đã chưng cất

- File 21: ba lớp HUB → dữ liệu máy hiểu → Grounded A.I; lớp trên không cứu được nguồn lộn xộn ở lớp dưới.
- Kho đáng tin phải truy đúng tài liệu/đoạn, ưu tiên bản hiện hành, giữ lịch sử, phân quyền, biết “chưa đủ dữ liệu” và thu hồi nguồn lỗi thời.
- Quyền phải cưỡng chế ở tầng lưu trữ/truy xuất; dặn A.I “đừng tiết lộ” không phải bảo mật.

## Audit trail

- **v1.0:** generic; 2 input/4 bước mẫu, không authority/canonical/conflict, normalization trace, access enforcement, retrieval tests hoặc lifecycle.
- **v2.2:** đủ control layers/engine/12 eval; FAIL do body 8.874/8.000.
- **v2.3:** cô đọng còn 8.233/8.000; vẫn FAIL duy nhất dung lượng.
- **v2.4:** 7.978 ký tự; metadata đồng nhất; hai validator và engine PASS.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer xác nhận canonical/source truth, conflict/version decisions, derivative/citation trace, storage-level access, six retrieval test types và lifecycle operation.

## Đóng D10

1. Chạy 12 prompts baseline v1.0 và v2.4 trên ít nhất ba corpus: policy/SOP, product/knowledge assets và regulated/multi-role data.
2. Đo trigger/anti-trigger/no-false-ask, canonical accuracy, stale/conflict detection, parse/citation fidelity, abstention, permission leakage và false readiness.
3. Lưu prompt/input/output/state/evidence, total_tokens, duration_ms; source/domain/data/security owner và reviewer xác nhận.
4. Chạy sáu retrieval types với query thật, expected sources/behavior và pass^3 cho bề mặt đối ngoại; chỉ đề nghị PILOT khi D10 đạt.
