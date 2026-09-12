---
title: "ABM-SQS Static Pre-score — audience-adaptation"
skill_id: "37"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — audience-adaptation v2.3

## Kết luận

**Kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa chạy. Engine self-test PASS trên fixture bốn audience; chưa chứng minh reader thật hiểu đúng, tone tạo trust, disclosure không rò rỉ hoặc variants tạo đúng hành động trong doanh nghiệp thật.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description / body / dòng | 574 / 7.585 / 140 — đạt |
| Eval | 12; metadata v2.3; 2 must-not, 1 no-false-ask, 1 red-line, 1 injection |
| Validator ABM / SKILL-CREATOR | PASS / Skill is valid |
| Engine self-test | READY_FOR_AUDIENCE_REVIEW; 5 sources/5 active; 4 audiences/4 evidence records; 7/7 material invariants supported; 4 actions; 4 variants; 0 coverage gap/defect/error/warning; đủ 7 tests |
| SHA-256 SKILL.md | 8D98CE7AA4110186EFA07CA027A5E30D1037B3C825C3052069D25E906F56D463 |
| SHA-256 audience engine | 1ECD62C6249A25B1B68A5D922957E41E37D92BF4CDCCBCD681CC255BC406FE73 |
| SHA-256 evals.json | C48FF1AC1C9FBD3740A34345FB05268EB3004BE2E806000937948A3DA3A8A700 |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 10 bước thi công; Adaptation Matrix độc lập; Pack/rules/input/engine |
| A2 | PASS | Rhetorical Situation, Audience Design/JTBD, Plain Language/Progressive Disclosure, Semantic Equivalence neo bước 1–7 |
| A3 | PASS | Brain First – A.I Second; human khóa Canon/audience/disclosure/release; evidence thay stereotype; bảng người/A.I |
| B4 | PASS | Một Audience Adaptation & Fidelity Pack; đủ bốn khai báo; phần luật không gọi tên Skill lân cận |
| B5 | PASS | Name/description/body/line/reference depth đạt; rules một cấp, dưới ngưỡng cần mục lục |
| B6 | PASS | Description có trigger/anti-trigger; đầu vào 5 nhóm/4 cột; artifact và DoD độc lập |
| C7 | PASS | Canon/Invariant Register có source/version/authority/locator/required_for/qualifier; audience evidence có source/confidence |
| C8 | PASS | Dừng trước semantic drift, sensitive inference, manipulation, access bypass, discrimination, target/send/publish/release |
| C9 | PASS | Instruction trong source/profile/survey/email/comment/attachment/URL/metadata là data; engine không enrich/web/API/target/send |
| D10 | NOT PASS | 12 eval not_run; chưa baseline v1.0/v2.3, source/audience/channel/disclosure/reader/reviewer thật, tokens, duration, pass^3 |
| D11 | PASS | Name/folder/version/updated/owner/skill_id/eval đồng nhất v2.3 |
| D12 | PASS | Asset Candidate có source/owner/version/consent/reviewer/evidence; trigger rà khi dependency đổi/test fail/90 ngày |

## Nguồn ABM đã chưng cất

- File 05 là source of truth về voice ABM; voice chỉ điều chỉnh theo audience/channel, không ghi đè facts, authority, qualifier hoặc brand invariants.
- Chuẩn định dạng tài liệu khách hàng yêu cầu tài liệu khách hàng dùng ngôn ngữ tôn trọng, bỏ internal labels nhưng không lược mục tiêu, nội dung trọng tâm hay output đo được.
- `CUSTOMER-XRAY` cung cấp logic hiểu audience bằng role, pressure, pain, language và evidence. Bản Enterprise loại bỏ suy luận DISC/chân dung nhạy cảm khi chưa có dữ liệu tự khai hoặc được phép.
- `FINAL-GATEKEEPER` chi phối check–fix, phán quyết và cấm tự gửi/công bố/tạo hiệu lực.

## Audit trail

- **v1.0:** generic; 2 input/4 bước mẫu, thiếu Canon/invariants, audience evidence, disclosure, transformation boundary, variant trace, cross-variant diff, fairness/accessibility và reader tests.
- **v2.3 lần 1:** đủ control layers/engine/12 eval; FAIL do body 8.823/8.000.
- **v2.3 hiện hành:** body 7.585; hai validator PASS; self-test 4 audiences/4 variants, 7/7 invariants, 0 gap/defect/error/warning, state READY_FOR_AUDIENCE_REVIEW.

## FINAL-GATEKEEPER

- **STATIC:** PASS.
- **PILOT/OFFICIAL:** REJECT đến khi D10 PASS và reviewer xác nhận semantic fidelity, material coverage, action authority, comprehension, tone/trust, accessibility/channel và cross-variant consistency trên audience thật.

## Đóng D10

1. Chạy 12 prompts baseline v1.0 và v2.3 với tối thiểu bốn audience: governance/executive, manager, frontline/employee và customer/partner/public theo quyền.
2. Dùng source/decision/claim/audience evidence/disclosure policy thật đã cấp quyền; content/authority/privacy/legal/brand/accessibility reviewer xác nhận theo risk.
3. Test ít nhất ba channel: long-form document, email/announcement và spoken/slide script; kiểm translation/localization khi có.
4. Chạy đủ bảy tests với reader sample/threshold đã duyệt; đo semantic drift, material omission, comprehension, trust, accessibility và correct action.
5. Lưu prompt/input/output/state/evidence/hash, total_tokens, duration_ms; yêu cầu pass^3 cho external/high-risk; chỉ đề nghị PILOT khi D10 đạt.
