# EXECUTIVE WRITING GATE RULES

## 1. Mô hình trạng thái

| State | Điều kiện |
|---|---|
| `NOT_READY` | Thiếu sender authority, audience, purpose/outcome, source pack hoặc có material conflict chưa xử lý |
| `DRAFT_READY` | Có document nhưng còn claim/action/redaction/review gap |
| `READY_FOR_EXECUTIVE_REVIEW` | Claims/actions/authority trace được, đủ reader tests, review route rõ |
| `VALIDATED_FOR_SEND_REVIEW` | Tests thật đạt threshold; required reviewers đã xác nhận |
| `APPROVED_FOR_SEND` | Chỉ người có thẩm quyền gắn; engine không tự cấp |

## 2. Quy tắc ưu tiên

Khi nguồn cùng áp dụng: `law/approved formal template → sender decision/authority → approved source facts → organization voice → stylistic preference`. Nguồn ngang authority mâu thuẫn phải vào Conflict Ledger; không chọn bản “nghe hay hơn”.

Không hardcode thông tin pháp lý, tài khoản, người ký, recipient list hoặc dữ liệu dễ đổi vào Skill. Lấy từ source/version đã duyệt cho từng lần chạy.

## 3. Mode router

| Mode | Khối bắt buộc |
|---|---|
| `email` | Subject có việc; BLUF; context cần thiết; ask/action; closing |
| `memo_decision_note` | Decision/request; evidence; implication/risk; action/register |
| `directive` | Authority/scope; requirement; owner; deliverable/deadline; exception/escalation |
| `announcement` | What changes; why; who affected; when; required action; support/Q&A |
| `report_message` | Key result; evidence; implication; decision needed; next action |
| `administrative_letter` | Current formal template; issuing authority; reference; body; recipient; sign/review blocks |
| `public_draft` | Approved facts; stakeholder impact; position; action/contact; legal/media review |

Chọn đúng một primary mode. Nếu tài liệu có phụ lục, mỗi phụ lục phục vụ một function; không ghép nhiều văn bản độc lập thành một “siêu tài liệu”.

## 4. Message Map

Message Map hợp lệ có:

1. `bottom_line`: một câu người đọc phải nhớ;
2. `decision_or_request`: decision đã có hoặc request cần chốt;
3. `why_now`: trigger/timing có nguồn;
4. tối đa ba `support_blocks`, mỗi block có source refs;
5. `risk_or_limit`: qualifier/exception không được cắt;
6. `action_ids`: link Action Register;
7. `do_not_say`: claim/term/source không được dùng;
8. `approval_route`.

## 5. Claim, action và authority

Material claim gồm mọi số, ngày, pháp lý/chính sách, commitment, quote, attribution, performance/outcome, allegation, comparison và statement ảnh hưởng người/tiền/danh tiếng.

- Claim: `id · text · DỮ KIỆN/SUY LUẬN/GIẢ ĐỊNH · source/version/locator · status · qualifier/limit`.
- Action: `id · owner · verb · deliverable · deadline/not-applicable · escalation`.
- Authority: mỗi decision/directive/commitment phải nằm trong authority basis hoặc mang nhãn proposal/draft.
- `TBD` không được giả thành dữ kiện; dùng placeholder rõ và route owner bổ sung.

## 6. Sensitivity và disclosure

- Áp Data Minimization: chỉ giữ dữ liệu người nhận cần để quyết/làm.
- Tách primary/secondary recipient; rà `To/CC/BCC`, attachment, link permission và channel.
- Redact PII, customer/employee, finance, legal, trade-secret và credential data theo policy.
- Public/external/high-risk draft luôn có reviewer; redaction không làm sai quyết định hoặc che qualifier.

## 7. Sáu reader tests

| Type | Pass khi |
|---|---|
| `bottom_line_5_second` | Người đọc nêu đúng việc chính sau lần đọc nhanh |
| `skim_comprehension` | Heading/first sentence đủ hiểu logic và priority |
| `claim_trace` | Material claim truy source/version/locator/qualifier |
| `actionability` | Mỗi action có owner–verb–deliverable–deadline/escalation |
| `ambiguity_hostile_read` | Không có cách hiểu hợp lý gây sai decision, commitment hoặc reputation |
| `audience_tone` | Tone đúng power distance, knowledge, concern và mode |

Mỗi test ghi method, reviewer/sample, threshold, result/evidence. Đầu ra bên ngoài hoặc rủi ro cao cần `pass^3` theo ABM-SQS.

## 8. Gate trước bàn giao

- Contract, source/claim/action/authority và approval route đủ.
- Bottom line/primary ask ở đầu; không quá ba support blocks.
- Material conflict/unsupported claim/missing action owner đều không bị che.
- Formal mode dùng current approved template; brand voice không ghi đè thể thức/pháp lý.
- Draft chưa duyệt mang trạng thái rõ; trạng thái gửi/publish chỉ do người có thẩm quyền cấp.

