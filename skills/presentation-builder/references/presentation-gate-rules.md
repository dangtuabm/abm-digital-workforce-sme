# PRESENTATION GATE RULES

## 1. Mô hình trạng thái

| State | Điều kiện |
|---|---|
| `NOT_READY` | Thiếu objective/audience/source authority/output contract hoặc có material conflict |
| `STORYBOARD_READY` | Blueprint/inventory có nhưng claim/asset/build gap còn mở |
| `RENDER_QA_READY` | Deck đã build/render; integrity hoặc visual QA chưa đóng |
| `READY_FOR_REHEARSAL` | Claims/assets/slides/render truy được, đủ QA tests và review route |
| `VALIDATED_FOR_DELIVERY_REVIEW` | Rehearsal thật đạt threshold; required reviews hoàn tất |
| `APPROVED_FOR_DELIVERY` | Chỉ người có thẩm quyền cấp; engine không tự cấp |

## 2. Mode và output contract

Mode được hỗ trợ: `executive_decision`, `pitch`, `training`, `report`, `keynote`, `workshop`. Contract khóa source format, deliverable format, aspect ratio, slide budget/range, language, naming, notes, accessibility và package contents. Không giả PPTX là bắt buộc; chọn PPTX/PDF/image/HTML theo hợp đồng đầu ra.

Khi contract yêu cầu batch ảnh: một source slide tương ứng đúng một output; lọc heading Markdown, backtick tag và trailing metadata khỏi Literal Copy trước layout; giữ thứ tự; tạo tên tuần tự đúng quy ước; kiểm count/missing/extra/dimension trước nén gói. Đây là rule điều kiện, không áp cho mọi deck.

## 3. Claim, source, asset và chart

- Material claim: số, ngày, quote, comparison, performance, outcome, price, legal/policy, commitment hoặc statement ảnh hưởng người/tiền/danh tiếng.
- Claim ghi `id · text · label · source/version/locator · status · qualifier`.
- Asset ghi `id · type · origin · owner · license/permission · credit · status`.
- Chart ghi data source/version/locator, denominator/timeframe/unit, transform, scale/baseline, caveat và alt summary.
- Conflict ngang authority phải hiện; không chọn bản “đẹp hơn”. Placeholder/TBD không được render như fact.

## 4. Slide specification

Mỗi slide có `id · order · section · function · message_title · literal_copy · layout · claim_refs · asset_refs · transition · speaker_notes · timing_seconds`. Title phải nêu message, không chỉ topic. `literal_copy` là chữ thật; `speaker_notes` chứa diễn giải, example, transition và caveat không nên nhồi lên slide.

Cho phép title/divider/visual/list/framework/chart/table/demo/interaction/Q&A/CTA theo purpose. Một slide có thể dùng nhiều phần tử nhưng chỉ một message. Không dùng màu là tín hiệu duy nhất; reading order, contrast, type size và alt summary phải phù hợp môi trường trình chiếu.

## 5. Integrity và render QA

Integrity pass khi:

1. source deck mở được; slide count/order/ID khớp inventory;
2. file output/name/aspect/dimension đúng contract; `missing=0`, `extra=0`;
3. font/fallback/embedding, links, media và speaker notes đúng yêu cầu;
4. không placeholder, overflow, overlap, crop, broken glyph, hidden disclaimer;
5. chart/table có label, unit, legend/caveat đọc được;
6. contact sheet có; visual inspection phủ first/last, mọi section boundary, chart/dense/complex slide và mẫu risk-based;
7. package manifest ghi file/hash/version/tool/template/time.

Không dùng “export thành công” thay cho visual QA. Kiểm trên rendered artifact mà audience sẽ thấy.

## 6. Bảy test bắt buộc

| Type | Pass khi |
|---|---|
| `narrative_recall` | Audience nhắc lại đúng promise, 3–5 support blocks và close |
| `claim_trace` | 100% material claims/chart truy source/version/locator/qualifier |
| `slide_integrity` | Count/order/name/aspect/dimension/missing/extra đúng contract |
| `visual_comprehension` | Người xem hiểu đúng message/chart mà không cần giải thích cứu hộ |
| `accessibility_readability` | Contrast, type, reading order, color independence và alt summary đạt rule |
| `timing_rehearsal` | Presenter hoàn tất trong timebox, có buffer và không đọc slide |
| `decision_action` | Audience nêu đúng decision/CTA, owner và next step |

Mỗi test ghi method, sample/reviewer, threshold, status/evidence. External/high-risk output cần `pass^3` theo ABM-SQS.

## 7. Gate bàn giao

- Contract, source/claim/asset ledger, Journey, Blueprint, Inventory và Visual System đủ.
- Source deck + render + manifest + contact sheet cùng version/hash.
- Không material conflict, unsupported claim, unlicensed asset hoặc render defect mở.
- Required content/brand/legal/accessibility reviews hoàn tất theo risk.
- Rehearsal chỉ chạy trên bản render bàn giao; thay deck sau rehearsal phải rerun phần ảnh hưởng.
- Delivery/publish/present approval chỉ do người có thẩm quyền cấp.
