# Evidence Case Study Gate Rules

## 1. State machine

- `NOT_READY`: thiếu source/consent/measurement/intervention/confounder/claim/review hoặc có ranh giới đỏ.
- `READY_FOR_CASE_REVIEW`: dossier đủ static gate; còn human review.
- `READY_FOR_AUTHORIZED_PUBLICATION`: mọi required review `PASS` có evidence; không có nghĩa đã ký, gửi hay publish.

## 2. Measurement integrity

- Metric có definition, unit, direction, formula, baseline/outcome value và window, sample size, exclusions, source refs, owner, validation.
- Absolute delta = outcome − baseline.
- Relative delta = (outcome − baseline) / baseline; baseline 0 thì không được báo relative delta.
- So sánh phải giữ cùng definition/unit/sampling hoặc nêu adjustment có owner approval.
- Không trộn phần trăm và điểm phần trăm.

## 3. Attribution levels

- `DESCRIPTIVE`: chỉ nói thay đổi xảy ra sau/trong giai đoạn.
- `CONTRIBUTION`: nói intervention có đóng góp, kèm confounders và residual uncertainty.
- `CAUSAL`: chỉ khi measurement design và domain reviewer cho phép bằng evidence.

Các flag cấm: `fabricated_evidence`, `causal_overclaim`, `cherry_picked_window`, `denominator_changed`, `limitation_omitted`, `unauthorized_testimonial`.

## 4. Consent, quote và asset

- Consent `APPROVED`, có subject display mode, allowed quotes/assets/channels/formats, expiry, revocation route và evidence.
- Quote verbatim có locator, speaker role, consent ID; paraphrase không được gắn ngoặc kép.
- Tên/logo/ảnh/video chỉ dùng trong đúng scope; revoked/expired/unknown → `NOT_READY`.

## 5. Version consistency

Ba loại bắt buộc: `SOCIAL_SHORT`, `WEBSITE_LONG`, `ONE_PAGER`.
Mỗi version truy claim/metric/quote/asset, có disclosure, audience, owner, approval status. Claim canon không đổi giữa bản.

Approval status chỉ `DRAFT`, `REVIEW_PENDING`, `REVIEWED`; cấm `APPROVED`, `PUBLISHED`, `SIGNED`, `SENT`.

## 6. Required reviews

1. `DATA_OWNER`
2. `SUBJECT_CONSENT`
3. `DOMAIN_MEASUREMENT`
4. `BRAND_LEGAL_PRIVACY`
5. `FINAL_PUBLICATION`

`PASS` cần evidence ref. Final publication còn `PENDING` thì tối đa `READY_FOR_CASE_REVIEW`.

## 7. Seven deterministic tests

1. `contract_consent_integrity`
2. `metric_baseline_delta`
3. `intervention_trace`
4. `attribution_confounder`
5. `quote_asset_rights`
6. `version_claim_consistency`
7. `approval_publication_boundary`

Mỗi test có evidence, reviewer, date và `passed=true`.
