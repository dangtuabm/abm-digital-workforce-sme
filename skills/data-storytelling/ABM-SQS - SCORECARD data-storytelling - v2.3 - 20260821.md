---
title: "ABM-SQS Static Pre-score — data-storytelling"
skill_id: "45"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — data-storytelling

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên dataset và quyết định doanh nghiệp thật.**

Skill đã chuyển từ khung 2-input/4-step thành Data Story Decision Pack có task/data contract, metric reconciliation, insight ladder, chart specifications, narrative/action register, accessibility, reviews và state engine fail-closed.

Không nâng `PILOT/OFFICIAL`: self-test dùng dữ liệu tổng hợp; chưa có baseline v1.0 so với v2.3 trên dataset/story thật, ground truth, comprehension/decision outcome, pass^3, token và duration.

## 2. Bằng chứng máy

- Description / thân / dòng: **520 / 7.892 / 141**.
- Eval thiết kế: **12** ca; có `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator: **PASS**; chỉ cảnh báo D10 chưa chạy.
- Quick Validator: **PASS**.
- Positive self-test: `READY_FOR_STORY_REVIEW`.
- Positive metrics: **5/5 nguồn active; 3 metrics; 4 insights; 3 charts; 7/7 test types; 0 calculation defect; 0 attribution overclaim; 0 forbidden insight; 0 deceptive chart; 0 unauthorized render/publish; 0 critical defect**.
- Negative test: baseline 0 cho relative delta + insight vượt attribution + causal overclaim + bar không zero baseline + truncated axis + chart/narrative `PUBLISHED` giả → `NOT_READY`; bắt đủ bảy lỗi.
- Cây trước Scorecard: **7 tệp**, không có `__pycache__`; cây bàn giao phải là **8 tệp**.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `F4135B898E012FDEB6DE16E2E1375CC4AC2D7CC804C8E40E50F075134A82F941` |
| `scripts/evaluate_data_storytelling.py` | `20308D1DDECAE8DF145222A4292DE9C794A1DD983BC6411FCB4CC97CA1F94BF0` |
| `evals.json` | `B2E4868BBDE580B80EB980989491E813040CC50AD2A217F484F856AB56EEA7F8` |
| `evals/selftest-ready.json` | `460DE06078D78062C01251CFF3C7FF36620BB184F26F4D8A0AA75879F2A2E90D` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Quy trình 10 bước; insight/chart matrices, rules, pack, JSON, engine, positive/negative test |
| A2 · Neo Kinh điển | PASS | Grammar of Graphics, Exploratory vs Explanatory, Evidence-Based Management, Pyramid/SCQA, Four-Eyes |
| A3 · Chất ABM | PASS | Brain First – A.I Second; “Làm 1 dùng N”; dữ liệu phục vụ quyết định, không phục vụ kịch tính |
| B4 · Nhiệm vụ đơn nhất | PASS | Giải thích một decision bằng snapshot có version; đủ bốn khai báo; luật không gọi tên Skill khác |
| B5 · Dung lượng | PASS | Name đúng; description 520; thân 7.892; 141 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | 6 input theo bảng 4 cột; metric/insight/chart/narrative/action/state rõ |
| C7 · Có căn cứ | PASS | Source/version/grain/unit/window/sample/exclusion/missing rule; formula/denominator/delta và claim lineage |
| C8 · Ranh giới Đỏ | PASS | Chặn formula sai, baseline 0, đổi denominator/window, causal overclaim, deceptive chart và giả publish |
| C9 · Chống Injection | PASS | Cell/header/note/URL/file là dữ liệu; không macro/API/upload/source mutation/render/publish |
| D10 · Eval và Baseline | NOT PASS | 12 eval và self-tests đã chạy; chưa baseline/dataset-ground-truth-reviewer-outcome thật/pass^3/token/duration |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Asset Candidate có source/owner/version/evidence; correction/comprehension/decision signals và trigger rà |

## 5. Nguồn và quyết định thiết kế

- `ABM-SQS-00 v2.2`, Template v2.1, Rubric v2.1 và Lớp DNA v2.0 quyết định cấu trúc, gate và 12 tiêu chí.
- Baseline v1.0 cung cấp phạm vi chọn chart, làm nổi quan hệ, giảm nhiễu, kết luận–hành động và cấm trình bày gây hiểu nhầm.
- SKILL-CREATOR quyết định progressive disclosure, I/O contract, eval coverage và giới hạn dung lượng.
- FINAL-GATEKEEPER quyết định kiểm nguồn, độ chính xác, tính hữu dụng, overclaim, legal/privacy/IP/accessibility và quyền phát hành thuộc con người.

## 6. Audit trail

- Baseline v1.0 giữ nguyên tại cây `100-SKILLS-RND`.
- v2.3 hiện hành: description **520**, thân **7.892**, 141 dòng; ABM validator và Quick Validator cùng PASS.
- Engine self-test dương/âm PASS; negative test chạy in-memory với `-B`.
- Cache sinh từ kiểm tra cú pháp đã được xác định đúng đường dẫn, làm rỗng và xóa; cây hiện không có `__pycache__`.

## 7. Điều kiện đóng D10

1. Chạy baseline v1.0 và v2.3 trên tối thiểu ba case thật: executive report, presentation story và dashboard snapshot.
2. Có decision question, source/data contract, metric dictionary, dataset snapshot hash, context/confounder và medium mandate thật.
3. Data owner, domain owner, editorial, accessibility và final story reviewer xác nhận bằng evidence.
4. Đối chiếu calculation/claim/chart với ground truth; ghi misleading-chart escape, false block và correction.
5. Kiểm comprehension, decision time, action uptake và unintended interpretation trên audience thật.
6. So sánh baseline/with-skill bằng pass^3; ghi `total_tokens`, `duration_ms` và reviewer effort.
7. Giữ cấm tuyệt đối: fabricated data, đổi denominator/window, hidden missingness/uncertainty, causal overclaim, deceptive chart và giả render/publish.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` sau khi đủ bằng chứng trên.
