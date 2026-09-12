# AUDIENCE ADAPTATION GATE RULES

## 1. Mô hình trạng thái

| State | Điều kiện |
|---|---|
| `NOT_READY` | Thiếu source authority/core outcome/invariants/audience/disclosure hoặc có material conflict |
| `CANON_LOCKED` | Canon có nhưng audience evidence/plan/variant chưa đủ |
| `VARIANTS_READY` | Có variants nhưng coverage/disclosure/fairness/review gap còn mở |
| `READY_FOR_AUDIENCE_REVIEW` | Canon–audience–variant trace đủ; không defect; reader tests đã lập |
| `VALIDATED_FOR_RELEASE_REVIEW` | Reader tests thật đạt; required reviews hoàn tất |
| `APPROVED_FOR_RELEASE` | Chỉ người có thẩm quyền cấp; engine không tự cấp |

## 2. Canon và phép biến đổi

**Bất biến mặc định:** fact, number/date/unit/denominator, decision, scope, defined term, legal meaning, risk, qualifier/exception, commitment, authority, source status và core outcome.

**Có thể đổi khi Contract cho phép:** order, depth, explanation, terminology gloss, example, tone, length, channel format, visual hierarchy và CTA wording trong cùng action authority.

**Cấm:** tạo claim/quote/urgency, đổi mẫu số/timeframe, giấu risk/exception, nâng proposal thành decision, làm promise mạnh hơn, đổi recipient rights, cherry-pick để gây hiểu sai hoặc dùng persuasion để vượt consent/access.

Mỗi invariant ghi `id · type · text · source/version/locator · material · required_for · qualifier · status`. `required_for=[ALL]` phải xuất hiện trong mọi variant; audience-specific invariant phải có đúng audience IDs.

## 3. Audience evidence và confidence

Nguồn ưu tiên: explicit brief/role policy → self-reported need/feedback → observed behavior trong bối cảnh được phép → hypothesis. Ghi source/date/owner/confidence. Hypothesis không được trình bày là fact và phải xác nhận bằng reader test.

Không infer race/ethnicity, religion, political view, health/disability, sexuality, union status, precise location, finance, family, mental state hoặc personality type. Không dùng proxy như title/age/culture để gán năng lực, động cơ hay niềm tin cá nhân.

## 4. Audience design matrix

Các archetype dưới đây chỉ là câu hỏi khởi tạo, không phải stereotype:

| Audience | Thường cần kiểm chứng |
|---|---|
| Board/governance | decision, materiality, risk, options, assurance, accountability |
| Executive | enterprise outcome, trade-off, resources, owner, escalation |
| Manager | implication, workflow, dependency, deliverable, deadline |
| Employee/frontline | what changes/does not, why, when, support, feedback route |
| Customer | outcome, scope, evidence, limitation, responsibility, next step |
| Partner | mutual value, interface, obligation, handoff, exception |
| Investor/media/public | approved material facts, context, risk, spokesperson/disclosure |
| Regulator/auditor | exact meaning, authority, evidence, record, control, accountable owner |

Mỗi row phải được thay bằng evidence của case thật trước release.

## 5. Disclosure và fairness

- Áp need-to-know, least privilege và approved disclosure list theo audience/channel.
- Giảm chi tiết vì access rule nhưng không tạo câu sai; dùng “không công bố trong kênh này” thay suy diễn.
- Một audience không được nhận claim tốt hơn, risk yếu hơn hay action khác nếu authority không giải thích được.
- Personalization không được dựa trên surveillance, sensitive inference, discriminatory exclusion hoặc dark pattern.
- Bản khách hàng chuyển internal labels sang ngôn ngữ tôn trọng, chủ động; không lược mục tiêu, nội dung trọng tâm hay đầu ra đo được từ source đã duyệt.

## 6. Fidelity Diff

Variant hợp lệ khi:

1. mọi required invariant có refs và meaning tương đương;
2. number/date/unit/denominator/timeframe và qualifier không drift;
3. action có owner/authority/deliverable/deadline hoặc `not_applicable`;
4. không new material claim, contradiction, false attribution hay invented familiarity;
5. disclosure/classification/channel đúng;
6. cross-variant differences có lý do audience evidence/role, không phải cảm tính;
7. terminology gloss không đổi defined term hoặc legal meaning.

## 7. Bảy reader tests

| Type | Pass khi |
|---|---|
| `semantic_fidelity` | Reviewer xác nhận meaning/decision/commitment không drift |
| `material_coverage` | 100% required invariants/qualifiers có đúng variant refs |
| `action_authority` | Audience nêu đúng action, owner, limit và escalation |
| `audience_comprehension` | Mẫu audience hiểu đúng core outcome và must-know |
| `tone_trust` | Tone tôn trọng, credible, không manipulative/false familiarity |
| `accessibility_channel` | Language, format, reading/listening và channel usable |
| `cross_variant_consistency` | Không contradiction hoặc unequal material omission không có authority |

Ghi method, artifact/version, sample/reviewer, threshold, status/evidence. External/high-risk output cần `pass^3` theo ABM-SQS.

## 8. Gate bàn giao

- Contract, Canon, Evidence Map, Matrix, Disclosure Map, Variants, Diff và Action Register cùng version/hash.
- Không material conflict, unsupported invariant, sensitive inference, disclosure breach hoặc fidelity defect mở.
- Required content/authority/brand/legal/privacy/accessibility reviews hoàn tất theo risk.
- Reader test chạy trên đúng variant/channel sẽ release; sửa material content phải rerun phần ảnh hưởng.
- Send/publish/mass-target/release approval chỉ do người có thẩm quyền cấp.
