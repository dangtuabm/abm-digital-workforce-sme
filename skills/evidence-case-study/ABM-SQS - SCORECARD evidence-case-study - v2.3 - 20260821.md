---
title: "ABM-SQS Static Pre-score — evidence-case-study"
skill_id: "43"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — evidence-case-study

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên case doanh nghiệp thật.**

Skill đã chuyển từ khung viết case study cơ bản thành Evidence Case Study Dossier có Task Contract, source/consent ledger, measurement contract, baseline–outcome metrics, intervention/confounder logs, claim–evidence matrix, quote/asset rights, ba phiên bản đầu ra, reviews và publication gate.

Không nâng `PILOT/OFFICIAL`: self-test dùng dữ liệu tổng hợp; chưa có baseline v1.0 so với v2.3 trên case thật, consent thật, phép đo thật, human publication approval, pass^3, token và duration.

## 2. Bằng chứng máy

- Description / thân / dòng: **509 / 7.999 / 142**.
- Eval thiết kế: **12** ca; có `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator: **PASS**; chỉ cảnh báo D10 chưa chạy.
- Quick Validator: **PASS**.
- Positive self-test: `READY_FOR_CASE_REVIEW`.
- Positive metrics: **5/5 nguồn active; consent hợp lệ; 3 metrics; 2 interventions; 2 confounders; 4 claims; 2 quotes; 2 assets; 3/3 version types; 4 risks; 7/7 test types; 0 lỗi phép tính; 0 forbidden claim; 0 attribution overclaim; 0 quote/asset violation; 0 unauthorized publication; 0 critical defect**.
- Negative test: consent `REVOKED` + baseline 0 cho relative delta + causal overclaim + forbidden claim flag + paraphrased quote + `PUBLISHED` giả → `NOT_READY`; bắt đủ sáu lỗi.
- Cây trước Scorecard: **7 tệp**, không có `__pycache__`; cây bàn giao phải là **8 tệp**.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `5AB636234AFA3DF112BE12DC1B9C9BC1568AE058C85B87A06635409808547A98` |
| `scripts/evaluate_evidence_case_study.py` | `950712EE6CCAE7D544C681361341523CB6DBE673934209198FE956FE1B214292` |
| `evals.json` | `7BA0739BCEBDE96DDBCC72483479D811A5C7292EF1A0B155FF64BAFD0C3D4506` |
| `evals/selftest-ready.json` | `7534C9B252CDA0BA76BAA2DD6FA72FE3F5E9044D55F5C0284239AFF7C7F319A2` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Quy trình tạo dossier; gate rules, template pack, JSON, engine, positive/negative test |
| A2 · Neo Kinh điển | PASS | Baseline–outcome measurement, contribution analysis, evidence lineage, consent, Bốn Mắt và Kaizen |
| A3 · Chất ABM | PASS | Brain First – A.I Second; “Làm 1 dùng N”; tài sản case phục vụ CEO nhưng không đánh đổi sự thật |
| B4 · Nhiệm vụ đơn nhất | PASS | Một artifact biến bằng chứng đã cấp quyền thành case dossier; luật không gọi tên Skill khác |
| B5 · Dung lượng | PASS | Name đúng; description 509; thân 7.999; 142 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | Contract, source, consent, measurement, metrics, intervention/confounder, claim, quote/asset và state rõ |
| C7 · Có căn cứ | PASS | Source/version/locator/owner; metric formula/window/sample/exclusion; claim–metric–intervention–confounder lineage |
| C8 · Ranh giới Đỏ | PASS | Chặn fabricated evidence, causal overclaim, cherry-picking, đổi mẫu số, bỏ limitation, testimonial trái phép và tự công bố |
| C9 · Chống Injection | PASS | Nội dung nguồn chỉ là dữ liệu; không tự truy cập, xin consent, ký, gửi, duyệt hay publish |
| D10 · Eval và Baseline | NOT PASS | 12 eval và self-tests đã chạy; chưa baseline/case-consent-measurement-review-publication thật/pass^3/token/duration |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Asset Candidate có source/owner/version/evidence; trigger rà khi source, consent, metric hoặc test đổi |

## 5. Nguồn và quyết định thiết kế

- `ABM-SQS-00 v2.2`, Template v2.1, Rubric v2.1 và Lớp DNA v2.0 quyết định cấu trúc, gate và 12 tiêu chí.
- Nguồn ABM về Tầng 4 A.I Mastery for SMEs quyết định case phải có Outcome Tracking, dữ liệu thời gian/chi phí/ROI thật và trở thành tài sản marketing có kiểm soát.
- CASE-STUDY đóng góp cấu trúc before–after, quote nguyên văn, consent/sign-off và ba phiên bản social–website–one-pager.
- FINAL-GATEKEEPER được dùng để phản biện source, độ chính xác, tính cập nhật, overclaim, quyền riêng tư, quyền tài sản và publication state.

## 6. Audit trail

- Baseline v1.0 giữ nguyên tại cây `100-SKILLS-RND`.
- v2.3 lần đầu: ABM validator FAIL vì thân **8.247** ký tự.
- Các lượt cô đặc đã ghi nhận: **8.072 → 8.055 → 8.030 → 8.024 → 8.004 → 7.999**; không cắt consent, measurement, attribution hay publication boundary.
- v2.3 hiện hành: thân **7.999**; ABM validator và Quick Validator cùng PASS.
- Negative test chạy in-memory với `-B`; không tạo `__pycache__`.

## 7. Điều kiện đóng D10

1. Chạy baseline v1.0 và v2.3 trên case doanh nghiệp thật có nguồn, owner, classification và retention hợp lệ.
2. Có consent/sign-off thật cho danh tính, quote, asset, channel, format, thời hạn và tuyến thu hồi.
3. Khóa measurement contract trước outcome: metric, công thức, cửa sổ, mẫu số, exclusions, missing-data rule và attribution level.
4. Ghi interventions, adoption evidence, confounders và residual uncertainty; không biến tương quan thành nhân quả.
5. Data owner, subject, domain/measurement, brand–legal–privacy và final publication reviewer xác nhận bằng evidence.
6. So sánh accuracy, traceability, reviewer effort và outcome baseline/with-skill; chạy pass^3, ghi `total_tokens`, `duration_ms`.
7. Giữ cấm tuyệt đối: bịa bằng chứng/quote, cherry-picking, đổi denominator, giấu limitation, consent breach và giả approval/publication.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` sau khi đủ bằng chứng trên.
