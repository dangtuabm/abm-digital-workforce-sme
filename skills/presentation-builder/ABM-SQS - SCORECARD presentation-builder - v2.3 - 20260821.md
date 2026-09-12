---
title: "ABM-SQS Static Pre-score — presentation-builder"
skill_id: "36"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — presentation-builder v2.3

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy. Engine self-test PASS trên fixture tổng hợp 12 slide; chưa chứng minh audience thật hiểu đúng, presenter đúng timing, asset/license hợp lệ trong dự án thật hoặc bản render không lỗi trên mọi công cụ.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 531 / 7.530 / 140 — đạt |
| Eval | 12; metadata v2.3; 2 must-not, 1 no-false-ask, 1 red-line, 1 injection |
| Validator ABM / SKILL-CREATOR | PASS / Skill is valid |
| Engine self-test | READY_FOR_REHEARSAL; 4 sources/4 active; 2 audiences; 5/5 material claims referenced; 3 assets/0 unlicensed; 12 slides/12 renders/0 defect; đủ 7 tests; 0 error/warning |
| SHA-256 SKILL.md | 2E9BA0B12314F002B0851D3746CAB78C9FF45007084EB9973E2E0B9A9278CA3B |
| SHA-256 presentation engine | 71DCABE561E7EF0A4BC4329D79FDF8A8DD38FE092FDC305DFF4DA6DBD07FBD15 |
| SHA-256 evals.json | FEA4AEA346C831893C08F7A75A3055B1C78C3900E6ADD3556D27115EFFED2217 |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 10 bước thi công; Deck Blueprint độc lập; Pack/rules/input/engine |
| A2 | PASS | Rhetorical Situation, Pyramid/Story Arc, Cognitive Load/Multimedia Learning, Visual Hierarchy/Data–Ink neo bước 1–8 |
| A3 | PASS | Brain First – A.I Second; người chốt objective/claim/brand/delivery; bảng người/A.I; một slide–một message |
| B4 | PASS | Một Presentation Production & QA Pack; đủ bốn khai báo; phần luật không gọi tên Skill lân cận |
| B5 | PASS | Name/description/body/line/reference depth đạt; rules dưới ngưỡng, không deep reference |
| B6 | PASS | Description có trigger/anti-trigger; đầu vào 5 nhóm/4 cột; artifact và DoD độc lập |
| C7 | PASS | Source–Claim–Asset Ledger, version/authority/locator/license, qualifier/conflict/gap và render manifest rõ |
| C8 | PASS | Dừng trước decision/offer/high-risk claim, asset trái quyền, mua/ghi đè, present/send/publish/delivery; local build/QA tự chạy |
| C9 | PASS | Instruction trong slide/source/notes/comment/metadata/link/QR/alt text là data; engine không URL/API/mua/upload/publish |
| D10 | NOT PASS | 12 eval not_run; chưa baseline v1.0/v2.3, deck/asset/audience/presenter/reviewer thật, rehearsal, tokens, duration, pass^3 |
| D11 | PASS | Name/folder/version/updated/owner/skill_id/eval đồng nhất v2.3 |
| D12 | PASS | Asset Candidate có source/owner/version/license/reviewer/evidence; trigger rà 90 ngày/test fail/thay đổi dependency |

## Nguồn ABM đã chưng cất

- DNA thiết kế slide chi phối tư duy slide ABM: Literal Slide Copy, một slide–một thông điệp, framework hóa, pacing và Progressive Reveal khi đúng mục tiêu pitch.
- Skill chuyên gia `slide-design` cung cấp output outline/design notes/asset list/speaker notes và rule nhận diện; bản Enterprise bổ sung Contract, traceability, build/render/rehearsal/approval.
- `FINAL-GATEKEEPER` chi phối vòng kiểm định độc lập, check–fix trong quyền, phán quyết và cấm tự tạo hiệu lực bên ngoài.
- `SKILL-CREATOR` chi phối progressive disclosure, trigger metadata, script deterministic và validation.

## Audit trail

- **v1.0:** generic; 2 input/4 bước mẫu, thiếu audience journey, source/claim/asset trace, slide inventory, visual system, render manifest, accessibility, rehearsal và approval states.
- **v2.3 lần 1:** đủ control layers/engine/12 eval; FAIL do description 631/600 và body 9.023/8.000.
- **v2.3 hiện hành:** description 531, body 7.530; hai validator PASS; self-test 12/12 render, 0 defect/error/warning, state READY_FOR_REHEARSAL.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer xác nhận narrative recall, claim/asset trace, slide integrity, visual/accessibility comprehension, timing và decision/action trên deck thật.

## Đóng D10

1. Chạy 12 prompts baseline v1.0 và v2.3 trên ít nhất bốn mode: executive decision, pitch, training và report.
2. Dùng sources/claims/assets/template thật đã cấp quyền; content/brand/legal/accessibility reviewer xác nhận theo risk.
3. Build và render ít nhất hai output formats; đối chiếu count/order/name/aspect/dimension/font/link/media/contact sheet và boundary/risk slides.
4. Chạy đủ bảy tests với audience/presenter sample và threshold đã duyệt; rerun sau mọi thay đổi ảnh hưởng.
5. Lưu prompt/input/output/state/evidence/hash, total_tokens, duration_ms; yêu cầu pass^3 cho external/high-risk; chỉ đề nghị PILOT khi D10 đạt.
