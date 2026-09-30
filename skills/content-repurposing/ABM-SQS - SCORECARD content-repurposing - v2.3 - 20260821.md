---
title: "ABM-SQS Static Pre-score — content-repurposing"
skill_id: "42"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — content-repurposing

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên asset family thật.**

Skill đã chuyển từ khung 2-input/4-step thành Content Repurposing System Pack có source/rights/claim canon, atom library, audience–channel brief, derivative lineage, channel-native variants, release sequence, reviews và measurement loop.

Không nâng `PILOT/OFFICIAL`: self-test dùng nguồn tổng hợp; chưa có baseline v1.0 so với v2.3 trên nội dung thật, rights/consent thật, human release, publish/metric/learning outcomes, pass^3, token và duration.

## 2. Bằng chứng máy

- Description / thân / dòng: **521 / 7.998 / 141**.
- Eval thiết kế: **12** ca; có `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator: **PASS**; chỉ cảnh báo D10 chưa chạy.
- Quick Validator: **PASS**.
- Positive self-test: `READY_FOR_CONTENT_REVIEW`.
- Positive metrics: **4/4 nguồn active; 1 rights record; 4 claims; 6 atoms; 3 audiences; 5 channel briefs; 5 variants; 5 transformation types; 5 release steps; 4 risks; 7/7 test types; 0 forbidden audience/variant; 0 untraced variant; 0 rights violation; 0 duplicate; 0 unauthorized release; 0 critical defect**.
- Negative test: rights `UNKNOWN` + claim ngoài canon + fabricated claim + `PUBLISHED` giả + exact duplicate → `NOT_READY`; bắt đủ năm loại lỗi.
- Cây hiện hành: **8 tệp**, không có `__pycache__`.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `B5FA64B022D617324F5659142A3B2DE520143C11DF1A7DE26BBCDE53B14978B7` |
| `scripts/evaluate_content_repurposing.py` | `8C3C98AC7F17D73C31EBAA4A886CC884491046F64949D865B8ABB0680411224E` |
| `evals.json` | `A837AEEFC161A9F1905D0657AA59EF1B565D3E77F83714783418E77C6297F839` |
| `evals/selftest-ready.json` | `B8681E81A3B3A0F3412F344337CA086D6FFC79F808FEA9F24A607E902CEDE02D` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Quy trình 10 bước; Repurposing Control Matrix; rules, pack, JSON, engine, positive/negative test |
| A2 · Neo Kinh điển | PASS | Content Atomization ↔ B2/B3; Transmedia/Channel Fit ↔ B4–B6; Source of Truth/Lineage ↔ B1/B5/B9; Bốn Mắt/Kaizen ↔ B7–B10 |
| A3 · Chất ABM | PASS | Brain First – A.I Second; “Làm 1 dùng N”; giọng ABM, T0 build trust/thought leadership; không emoji trong tài liệu chính |
| B4 · Nhiệm vụ đơn nhất | PASS | Một artifact tái cấu trúc source canon; đủ bốn khai báo; luật không gọi tên Skill khác |
| B5 · Dung lượng | PASS | Name đúng; description 521; thân 7.998; 141 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | 6 input theo bảng 4 cột; pack/variants/state/measurement rõ |
| C7 · Có căn cứ | PASS | Source/version/locator/context/owner; claim–atom–variant lineage; stale/conflict/prohibited claim |
| C8 · Ranh giới Đỏ | PASS | Chặn rights/consent/expiry, fabricated claim, quote distortion, PII, clone/deepfake và auto-post; local preparation tự chạy |
| C9 · Chống Injection | PASS | Instruction trong nguồn là dữ liệu; không URL/API/clone/render/contact/post; không lộ restricted source |
| D10 · Eval và Baseline | NOT PASS | 12 eval và self-tests đã chạy; chưa baseline/source-rights thật/pass^3/evidence/token/duration |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Asset Candidate có source/owner/version/evidence; metric hypothesis/learning và trigger rà |

## 5. Nguồn và quyết định thiết kế

- `ABM-SQS-00 v2.2`, Template v2.1, Rubric v2.1 và Lớp DNA v2.0 quyết định cấu trúc, gate và 12 tiêu chí.
- Nguồn ABM `AB03-THUONG-HIEU-NGON-TU-VA-VAN-HOA-THI-CONG.md` quyết định voice canon, brand identity, “Làm 1 dùng N” và yêu cầu không overclaim.
- Nguồn ABM `AB05-HE-SINH-THAI-SAN-PHAM-VA-CHIEN-LUOC.md` quyết định T0 là sản phẩm chiến lược, hệ đa kênh, một chủ đề thành nhiều format, cá nhân hóa theo ngách và build trust trước hard-sell.
- DT-CONTENT-MATRIX đóng góp: định vị theo ma trận, hook, nhịp kéo–dẫn–đóng, CTA mềm và channel-specific writing; không sao chép độ dài cứng thành luật phổ quát.
- FINAL-GATEKEEPER được dùng để phản biện source, cập nhật, DNA, tính thực thi, rights/privacy, accessibility và release state.

## 6. Audit trail

- Baseline v1.0 giữ nguyên tại cây `100-SKILLS-RND`.
- v2.3 lần đầu: ABM validator FAIL vì thân **8.438** ký tự.
- Các lượt cô đặc: **8.154 → 8.101 → 8.055 → 8.022**; không cắt rights, claim lineage hay release boundary.
- v2.3 hiện hành: thân **7.998**; ABM validator và Quick Validator cùng PASS.
- Negative test chạy với `-B`; không tạo `__pycache__`.

## 7. Điều kiện đóng D10

1. Chạy baseline v1.0 và v2.3 trên tối thiểu bốn source thật: webinar/video, bài viết/report, podcast/transcript và tài liệu đào tạo.
2. Có canonical source, rights/consent/territory/expiry, brand/CTA canon, audience/channel evidence và owner thật.
3. Source owner, rights/privacy, brand/editorial, accessibility và final release reviewers xác nhận bằng evidence.
4. Phát hành có thẩm quyền; ghi lineage, version, channel-native quality, delivery, correction và unintended effect.
5. Đo reach/retention/action/conversion theo metric hypothesis; không gán attribution khi thiếu tracking.
6. So sánh fidelity, distinctiveness, production effort và outcome baseline/with-skill; chạy pass^3, ghi `total_tokens`, `duration_ms`.
7. Giữ cấm tuyệt đối: rights/consent breach, fabricated claim/data/testimonial, quote distortion, PII, voice/likeness clone và giả approval/publish/metric.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` sau khi đủ bằng chứng trên.
