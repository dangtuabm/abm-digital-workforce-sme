---
title: "ABM-SQS Static Pre-score — marketing-system"
skill_id: "69"
version: "2.3"
date: "2026-08-22"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — marketing-system

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên hệ thống content thật.**

Skill đã chuyển từ khung 2-input/4-step thành `Evidence-Grounded Multichannel Content Marketing Operating System`: mandate/objective, audience job/journey, source/claim/rights, brand/editorial, pillar/matrix, channel contract, backlog/capacity/workflow/calendar, repurpose lineage, metric/experiment, risk/review và human activation.

Không nâng `PILOT/OFFICIAL`: positive case tổng hợp; chưa so v1.0/v2.3 trên content operation thật, chưa có ground truth về customer insight, claim/rights, platform policy, production adoption, market/commercial outcome, harm, token và duration.

## 2. Bằng chứng máy

- Description / thân / dòng: **584 / 7.248 / 104**.
- 12 eval; đủ `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator + Quick Validator: **PASS**; D10 chưa chạy.
- Positive: `READY_FOR_HUMAN_CONTENT_SYSTEM_ACTIVATION`, 0 defect; **7 sources, 4 audience jobs, 5 pillars, 4 channel contracts, 6 content items, 6 repurpose links, 6 metrics, 3 experiments, 6 risks, 6 decisions, 7/7 tests, 6 reviews PASS**.
- Negative: `NOT_READY`; bắt **163 defects + 6 review gaps**, gồm 45 forbidden flags và 9 forbidden states.
- Cây trước Scorecard: 7 tệp, không `__pycache__`; cây bàn giao: 8 tệp.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `FDDC00F283CF6A5A93FA09E859522B682EE23CB9A591822DBA9EB5497E2B2211` |
| `scripts/evaluate_marketing_system.py` | `9DE98202C59338926B398366978A391DA46918D99C36C8745A0385861C0E66B8` |
| `evals.json` | `3C12F1CD3FF7701DBB314664FAA4D1FF63BFA341D6014AE0846F53A105B0254B` |
| `templates/marketing-system-input.json` | `F2FFA4C74EF6B732691694161127345BC11FDB2359D3DC116DA9880913DD2E1B` |
| `evals/selftest-negative.json` | `0533543E1C0F092A5D1BED7D2C9452D31F7F2F96873F435EB45759E71F835DCC` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Rules, template, engine, six-item operating case và negative test chạy được |
| A2 · Neo Kinh điển | PASS | Customer jobs/journey, editorial operations, channel contracts, experimentation và measurement discipline |
| A3 · Chất ABM | PASS | Brain First – A.I Second; objective/customer truth và capacity trước content volume/tool/trend |
| B4 · Nhiệm vụ đơn nhất | PASS | Authorized evidence → multichannel content operating system; asset đơn, paid media, publishing và outreach ngoài phạm vi |
| B5 · Dung lượng | PASS | Name/folder đúng; description 584; thân 7.248; 104 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | Mandate/evidence/audience/pillar/channel/workflow/repurpose/metric/experiment/review rõ |
| C7 · Có căn cứ | PASS | Source/claim/rights/date/confidence, audience job, item lineage, metric denominator/cohort/window và authority traceable |
| C8 · Ranh giới Đỏ | PASS | Chặn fabrication, plagiarism, dark pattern, consent/tracking breach, metric gaming và auto external action |
| C9 · Chống Injection | PASS | Brief/asset/platform/analytics là dữ liệu; không bỏ rights/review, đổi claim, bật tracking hay publish |
| D10 · Eval và Baseline | NOT PASS | 12 eval/self-tests đã chạy; thiếu real-content pilot/pass^3/token/duration/customer-market-commercial outcome |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Pillar/channel/brief/repurpose/metric asset cần owner/version/source-rights/reviews/outcome/change log |

## 5. Nguồn và quyết định thiết kế

- Baseline v1.0 chỉ nêu xây hệ thống nội dung đa kênh bằng 2 input/4 bước; thiếu mandate, audience evidence, claim/rights, channel contract, production capacity, repurpose lineage, metric/experiment, human activation và chỉ 5 eval generic.
- `DT-CONTENT-MATRIX` được chọn làm nguồn chuyên môn chính: giữ pillar/matrix, platform adaptation, brand voice và CTA mềm; loại universal length/cadence/CTA, tuyên bố growth và quy tắc nền tảng không có nguồn hiện hành. `SKILL-CREATOR` khóa I/O/eval; `FINAL-GATEKEEPER` khóa claim/rights/privacy/accessibility/measurement và release authority. Funnel analytics, paid media, landing page, email execution và publishing giữ ngoài ranh giới B4.

## 6. Điều kiện đóng D10

1. Pilot v1.0/v2.3 trên ít nhất 3 context thật: evergreen education, campaign/launch và regulated/claim-sensitive content.
2. Có customer/job, source/claim/rights, brand/editorial, channel/platform, production capacity và metric truth set cùng reviewers.
3. Đo evidence/claim defects, production lead time/WIP, rights/accessibility/privacy findings, content-to-outcome traceability, harm/complaints và market/commercial outcome có giới hạn nhân quả.
4. Không dùng pilot để tự publish/send/schedule/buy media/track/change campaign/contact; ghi external human evidence.
5. So sánh pass^3; ghi token, duration, adoption, outcome và unintended effect.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` khi đủ bằng chứng trên.
