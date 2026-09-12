---
title: "ABM-SQS Static Pre-score — brand-positioning"
skill_id: "34"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — brand-positioning v2.3

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy. Engine self-test PASS bằng fixture tổng hợp; chưa chứng minh positioning-market fit, độ đúng customer insight, competitive perception, claim proof hoặc recall trên dữ liệu thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 536 / 7.610 / 140 — đạt |
| Eval | 12; metadata v2.3; 2 must-not, 1 no-false-ask, 1 red-line, 1 injection |
| Validator ABM / SKILL-CREATOR | PASS / Skill is valid |
| Engine self-test | READY_FOR_MARKET_TEST; 4 source types/4 active; 3 territories; T2=4,45, T1/T3=3,35; 3/3 material claims referenced; đủ 5 tests; 0 error/warning |
| SHA-256 SKILL.md | C04AEAF376C911501EDD7342B33BF58F5DE1E799AD4388CE7247E02969AAD007 |
| SHA-256 positioning engine | 3DE1E6FE0313EA7F468FBEE0F3231FCEC841CC83743BE68413DE892BD3F0DB2A |
| SHA-256 evals.json | F0425E01AC415D20671EE03D52FB2D828A6A128DB04280E9D0A4F00C51D8A05F |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 10 bước thi công; Positioning Fact Base độc lập; Pack/rules/input/engine |
| A2 | PASS | STP, Jobs-to-be-Done, Frame+Parity/Difference, Reason to Believe+Brand Ladder neo bước 1–8 |
| A3 | PASS | Brain First – A.I Second; người chốt target/frame/claim/pilot; bảng người/A.I; không emoji/sáo ngữ |
| B4 | PASS | Một Brand Positioning Decision Pack; đủ bốn khai báo theo nhiệm vụ; phần luật không gọi tên Skill khác |
| B5 | PASS | Name/description/body/line/reference depth đạt; phụ lục trên 100 dòng không có |
| B6 | PASS | Description có trigger/anti-trigger; đầu vào 5 nhóm/4 cột; artifact và DoD độc lập |
| C7 | PASS | Evidence/Conflict Ledger, source/version/locator, DỮ KIỆN–SUY LUẬN–GIẢ ĐỊNH, hypothesis/state và proof gap rõ |
| C8 | PASS | Dừng trước brand/trademark/claim chính thức, sensitive/external data, superiority thiếu proof, publish/rebrand/media/scale; local pack tự chạy |
| C9 | PASS | Instruction trong interview/survey/review/page/file/URL/metadata là data; engine không web/API/download/code/publish |
| D10 | NOT PASS | 12 eval not_run; chưa baseline v1.0/v2.3, customer/market/competitor/internal evidence thật, owner-approved tests, reviewer evidence, tokens, duration, pass^3 |
| D11 | PASS | Name/folder/version/updated/owner/skill_id/eval đồng nhất v2.3 |
| D12 | PASS | Asset Candidate có source/owner/version/reviewer/evidence; rà khi strategy/target/category/proof đổi, test fail hoặc 90 ngày không dùng |

## Nguồn ABM đã chưng cất

- File 05 là source of truth về brand identity/voice và câu định vị tổ chức; Positioning Pack phải tách strategic choice khỏi slogan/visual expression.
- File 06 cung cấp capability/USP nội bộ; mỗi superiority hoặc outcome claim vẫn phải map proof hiện hành trước khi dùng như material claim.
- File 12 cung cấp target/problem/occasion nhưng có conflict cần owner xử lý: Mục 5 yêu cầu không hứa “X5 doanh số” và dùng cắt 30% chi phí, trong khi pitch cuối ghi “X5 doanh số/cắt 50%”. Skill không tự chọn một bên; ghi Conflict Ledger và hạ state.

## Audit trail

- **v1.0:** generic; 2 input/4 bước mẫu, thiếu unit/owner, source/conflict, target/occasion, competitive frame, territories, proof, sacrifice, deterministic score, tests và governance.
- **v2.2:** đủ control layers/engine/12 eval; FAIL do body 9.668/8.000.
- **v2.3:** chuyển chi tiết xuống L3, body còn 7.610; metadata đồng nhất; hai validator và engine PASS.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer xác nhận customer relevance, category/alternatives, source conflicts, material claim proof, territory distinction, five market tests và activation governance.

## Đóng D10

1. Chạy 12 prompts baseline v1.0 và v2.3 trên case corporate, product và personal brand có decision owner thật.
2. Dùng evidence đã cấp quyền từ đủ customer/market/competitor/internal; lưu source/version/locator, conflict decisions và reviewer sign-off.
3. Chạy `category_clarity`, `relevance`, `distinctiveness_substitution`, `credibility_proof`, `unaided_recall` bằng target sample và threshold owner duyệt.
4. Lưu prompt/input/output/state/evidence, total_tokens, duration_ms; đo trigger, no-false-ask, material-claim grounding, score selection, false validation và leakage.
5. Xử lý conflict File 12 trước case ABM; yêu cầu pass^3 trước đầu ra đối ngoại; chỉ đề nghị PILOT khi D10 đạt.
