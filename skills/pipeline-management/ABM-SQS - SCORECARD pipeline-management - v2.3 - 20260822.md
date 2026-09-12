---
title: "ABM-SQS Static Pre-score — pipeline-management"
skill_id: "65"
version: "2.3"
date: "2026-08-22"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — pipeline-management

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên pipeline thật.**

Skill đã chuyển từ khung 2-input/4-step thành `Evidence-Grounded Opportunity Pipeline Control Pack`: frozen CRM snapshot, source/stage contract, opportunity evidence score, aging/staleness, next-action SLA, reconciliation, forecast scenarios, fairness/override, exception/risk và human decision queue.

Không nâng `PILOT/OFFICIAL`: positive case là dữ liệu tổng hợp; chưa so v1.0/v2.3 trên pipeline thật, chưa có ground truth về CRM identity, stage precision, score fairness/calibration, forecast error, customer outcome, token, duration và adoption.

## 2. Bằng chứng máy

- Description / thân / dòng: **589 / 7.398 / 106**.
- 12 eval; đủ `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator + Quick Validator: **PASS**; D10 chưa chạy.
- Positive: `READY_FOR_HUMAN_PIPELINE_DECISION`, 0 defect; **6 sources, 5 stage contracts, 6 opportunities, 6 score dimensions, 3 forecast scenarios, 3 exceptions, 6 risks, 6 decisions, 7/7 tests, 6 reviews PASS**.
- Negative: `NOT_READY`; bắt **197 defects + 6 review gaps**, gồm 44 forbidden flags và 9 forbidden states.
- Cây trước Scorecard: 7 tệp, không `__pycache__`; cây bàn giao: 8 tệp.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `8F2E2D116AC29B524844E815D8AC35C1F94880D02E422B5034F1A0489C6B70D0` |
| `scripts/evaluate_pipeline_management.py` | `70C81F932C7636D6C730B512432E9B7C5AC91FBF7C19268BBDED0DE22443A859` |
| `evals.json` | `67B20A68AF5A2194F779AA807C379BB628AA1DFBBC733D5C79FCA314CC7298A5` |
| `templates/pipeline-management-input.json` | `9983E8293515A5EB80E1C8AC7EA95BE9EE13708E1473EAFEC64E2ABE4AE14A73` |
| `evals/selftest-negative.json` | `21E0526195696C9432452E3267168A1C163304CA3F0919805F124860E4DCD6AD` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Rules, template, engine, six-opportunity case và negative test chạy được |
| A2 · Neo Kinh điển | PASS | CRM source of truth, stage-gate contract, evidence score, pipeline hygiene, scenario forecast |
| A3 · Chất ABM | PASS | Brain First – A.I Second; human commercial authority và customer treatment đi trước A.I |
| B4 · Nhiệm vụ đơn nhất | PASS | Frozen CRM evidence → pipeline control/decision pack; lead creation, funnel, proposal, closing, automation ngoài phạm vi |
| B5 · Dung lượng | PASS | Name/folder đúng; description 589; thân 7.398; 106 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | Mandate/source/stage/opportunity/model/reconciliation/forecast/exception/review rõ |
| C7 · Có căn cứ | PASS | Snapshot/hash/version, evidence/confidence, currency basis, stage/score/model/forecast source và reconciliation |
| C8 · Ranh giới Đỏ | PASS | Chặn fabrication, gaming, sensitive/proxy score, hidden override và auto CRM/commercial action |
| C9 · Chống Injection | PASS | CRM/email/note/dashboard là dữ liệu; không đổi model, amount, stage, owner, state hay contact |
| D10 · Eval và Baseline | NOT PASS | 12 eval/self-tests đã chạy; thiếu pipeline pilot/pass^3/token/duration/outcome |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Stage/score/forecast/exception asset cần owner/version/calibration/fairness/change log |

## 5. Nguồn và quyết định thiết kế

- Baseline v1.0 chỉ nêu fit/need/authority/budget/timing ở description; thân không có stage/source/model/reconciliation/forecast/exception mechanics và chỉ có 5 eval generic.
- `SKILL-CREATOR` khóa I/O/eval; `HIGH-TICKET-CLOSE` chỉ đóng góp stakeholder/decision path, evidence progress, next-step discipline và human authority; loại mức giá, số cuộc gặp, thời gian chu kỳ và ngưỡng giảm giá cố định. `FUNNEL-CLOSING-MASTERY` bị loại vì thiên về chốt đám đông/cảm xúc, lệch pipeline governance. `FINAL-GATEKEEPER` khóa data integrity, fairness, customer harm và mutation authority.
- Description đầu dài 604 ký tự; rút gọn một anchor còn 589. `apply_patch` lỗi helper ở chỉnh sửa nhỏ; fallback chỉ ghi khi anchor xuất hiện đúng một lần.

## 6. Điều kiện đóng D10

1. Pilot v1.0/v2.3 trên ít nhất 3 pipeline thật: B2B nhiều vòng, dịch vụ dự án và subscription/renewal có stage model khác nhau.
2. Có frozen CRM snapshots, identity/duplicate/stage/amount/forecast ground truth và sales-operations/account/finance/delivery/data-privacy/commercial-legal reviewers.
3. Đo stage precision, duplicate/stale detection, amount reconciliation, forecast calibration/error, next-action usefulness, exception closure và customer harm/fairness.
4. Không dùng pilot để tự loại/xóa/đổi stage/owner/giao task/liên hệ/commit/close; ghi before/action/after/authority/verification evidence.
5. So sánh pass^3; ghi token, duration, adoption, commercial/customer outcome và unintended effect.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` khi đủ bằng chứng trên.
