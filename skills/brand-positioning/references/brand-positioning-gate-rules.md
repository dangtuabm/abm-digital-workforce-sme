# BRAND POSITIONING GATE RULES

## 1. Mô hình trạng thái

| State | Điều kiện |
|---|---|
| `NOT_READY` | Thiếu unit/owner/source access/target/frame hoặc có material conflict chưa xử lý |
| `HYPOTHESIS_READY` | Có fact base và territory nhưng material evidence/proof còn là giả thuyết |
| `READY_FOR_MARKET_TEST` | Chọn một territory, material claims có refs, đủ năm test đã lập kế hoạch |
| `VALIDATED_FOR_PILOT_REVIEW` | Test thật đạt threshold đã duyệt; reviewer xác nhận evidence và claim |
| `APPROVED` | Chỉ người có thẩm quyền gắn sau duyệt; engine không tự gắn |

Không suy từ `READY_FOR_MARKET_TEST` sang “định vị đúng”. Readiness chỉ chứng minh pack đủ điều kiện để kiểm chứng.

## 2. Evidence Ledger

Mỗi nguồn phải có: `id · type · title · version/date · owner · authority · access · status · locator · strength`.

Loại evidence ưu tiên theo câu hỏi, không theo một thứ tự cứng:

- `customer`: interview, win/loss, survey, search/review, behavior;
- `market`: category demand, occasion, channel, regulation;
- `competitor`: offer, message, proof, share of mind, substitution;
- `internal`: strategy, capability, product performance, delivery evidence.

Material claim phải có nguồn hiện hành và locator. Internal aspiration không chứng minh customer relevance; customer quote không chứng minh khả năng delivery; competitor copy không chứng minh claim của đối thủ là thật.

Conflict ghi: claims/sources, authority, version, impact, owner, decision/status. Hai nguồn ngang authority mâu thuẫn → `ESCALATE`, không chọn nguồn thuận ý.

## 3. Territory và lựa chọn

Một territory hợp lệ có đủ: target/occasion, category, problem, promise, difference, sacrifice/exclusion, proof refs, strategic fit và failure mode.

- Tối đa ba territory; khác nhau về strategic choice, không chỉ câu chữ.
- Difference phải relevant, distinctive, credible và defendable.
- Points of parity bảo đảm target nhận đúng category; point of difference cho lý do chọn.
- Không có sacrifice/exclusion nghĩa là chưa chọn.

Score 1–5 theo tiêu chí owner đặt trọng số. Engine tính:

`weighted_total = sum(weight × rating) / sum(weight)`

Không bù một điểm `credibility` thấp bằng câu chữ mạnh. Recommendation phải là điểm cao nhất; nếu hòa, owner chốt bằng strategic fit và reversal condition.

## 4. Proof Architecture

Chuỗi bắt buộc: `capability/feature → functional benefit → business/emotional payoff → material claim → reason to believe → source refs/limitation`.

Trạng thái claim:

- `supported`: đủ evidence hiện hành cho đúng scope;
- `hypothesis`: cần test/proof bổ sung, không dùng như dữ kiện;
- `rejected`: sai, stale hoặc vượt scope;
- `escalated`: conflict/authority cần người quyết.

Các từ “số 1”, “duy nhất”, “tốt nhất”, số ROI/kết quả, cam kết tuyệt đối và comparison superiority luôn là material claim.

## 5. Năm test bắt buộc

| Type | Câu hỏi nghiệm thu |
|---|---|
| `category_clarity` | Target hiểu thương hiệu thuộc lựa chọn nào và dùng khi nào? |
| `relevance` | Problem/promise có quan trọng trong buying occasion thật? |
| `distinctiveness_substitution` | Thay logo bằng đối thủ, câu còn đúng không? |
| `credibility_proof` | Target tin claim nào, đòi proof nào, phản đối gì? |
| `unaided_recall` | Sau khoảng trì hoãn đã định, target nhớ khác biệt nào? |

Mỗi test ghi sample, method, threshold, owner, result/evidence. Không tự đặt sample/threshold ảnh hưởng quyết định; owner phê duyệt trước khi chạy. Đầu ra đối ngoại hoặc rủi ro cao cần `pass^3` theo ABM-SQS.

## 6. Gate trước bàn giao

- Unit/brand level không lẫn corporate, product và personal brand.
- Một primary target và một recommended territory; runner-up chỉ để reversal.
- Category/frame, alternatives, parity/difference và exclusion rõ.
- Mọi material claim map nguồn; không unresolved material conflict.
- Statement là chiến lược nội bộ, không bị ngụy trang thành slogan đã duyệt.
- Test plan đủ năm type; state không vượt evidence.
- Publication/rebrand/media/trademark/claim approval vẫn thuộc người có thẩm quyền.

