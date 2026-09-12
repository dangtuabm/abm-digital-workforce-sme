# Content Repurposing Gate Rules

## 1. State machine

- `NOT_READY`: source/rights/claim/lineage/channel/review thiếu, conflict mở hoặc có ranh giới đỏ.
- `READY_FOR_CONTENT_REVIEW`: pack đủ static gate; còn human review.
- `READY_FOR_AUTHORIZED_RELEASE`: mọi required review `PASS` có evidence. Đây không phải `APPROVED/PUBLISHED/SENT`.

Engine không phát trạng thái đã duyệt, đăng, gửi hoặc đo hiệu quả.

## 2. Source, rights và claim canon

- Source active có ID, title, version, locator, owner, classification, effective date.
- Rights record có evidence ref, owner, usage scope, allowed channels/formats, territory, expiry, attribution và voice/likeness consent.
- Claim chỉ `CONFIRMED`; có source refs, locator, context, owner. Prohibited claim không được vào variant.
- Unknown rights, hết hạn, sai channel/format hoặc thiếu attribution → `NOT_READY`.

## 3. Atoms và lineage

- Atom có type, content, claim/source refs, context, permission, owner.
- Variant có parent atom IDs, claim IDs, source refs; `claim_refs` phải nằm trong tập đã khai báo.
- Không atom/claim mồ côi được dùng. Không được thêm claim mới bằng visual, hook, CTA hoặc edit.

## 4. Audience–channel fit

- Audience có job/need/evidence; không suy protected trait hay dữ liệu cá nhân.
- Channel brief có platform, objective, format, behavior, constraints, CTA policy, accessibility, metric hypothesis và owner.
- Mỗi channel brief phải có ít nhất một variant; variant chỉ dùng audience/channel hợp lệ.

## 5. Variant safety

Cấm các flag: `fabricated_claim`, `changed_meaning`, `quote_distortion`, `source_attribution_removed`, `rights_unknown`, `contains_restricted_data`, `deceptive_edit`, `unauthorized_testimonial`, `voice_or_likeness_without_consent`.

Approval status chỉ `DRAFT`, `REVIEW_PENDING`, `REVIEWED`; cấm `APPROVED`, `PUBLISHED`, `SENT`, `SCHEDULED`.

## 6. Review set

1. `SOURCE_OWNER`
2. `RIGHTS_PRIVACY`
3. `BRAND_EDITORIAL`
4. `ACCESSIBILITY`
5. `FINAL_RELEASE`

`PASS` cần evidence ref. Final release còn `PENDING` thì tối đa `READY_FOR_CONTENT_REVIEW`.

## 7. Seven deterministic tests

1. `contract_rights_integrity`
2. `claim_atom_trace`
3. `variant_lineage_fidelity`
4. `channel_audience_fit`
5. `brand_cta_accessibility`
6. `duplicate_distortion_check`
7. `approval_release_boundary`

Mỗi test có evidence, reviewer, date và `passed=true`.
