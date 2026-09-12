---
title: "ABM-SQS Static Pre-score — meeting-preparation"
skill_id: "48"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — meeting-preparation

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên cuộc họp doanh nghiệp thật.**

Skill đã chuyển từ khung 2-input/4-step thành Meeting Readiness Pack có meeting type/output, source/pre-read ledger, prior commitments, decision items, attendee/quorum, agenda timebox, facilitation plan, reviews và state engine fail-closed.

Không nâng `PILOT/OFFICIAL`: self-test dùng meeting tổng hợp; chưa có baseline v1.0 so với v2.3 trên meeting/decider/outcome thật, decision yield/overrun/carryover, pass^3, token và duration.

## 2. Bằng chứng máy

- Description / thân / dòng: **532 / 7.751 / 141**.
- Eval thiết kế: **12** ca; có `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator và Quick Validator: **PASS**; D10 chưa chạy.
- Positive self-test: `READY_FOR_MEETING_REVIEW`.
- Positive metrics: **5/5 nguồn active; 0 stale; 2 pre-reads, 0 violation; 4 attendees, quorum true; 3 prior commitments; 2 decision items; 5 agenda segments; 60/60 phút; 0 uncovered decision; 0 forbidden/unauthorized; 7/7 tests; 0 critical defect**.
- Negative test: stale source + pre-read `SENT` giả + decider unavailable + hidden open commitment + one-option decision + agenda 80/60 + fake `INVITED` + failed test → `NOT_READY`; bắt đủ tám lỗi.
- Cây trước Scorecard: **7 tệp**, không có `__pycache__`; cây bàn giao phải là **8 tệp**.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `E8080DB3707757D68A25937A3DFCA3716F4CA317408A96C579DE1E1032EB051C` |
| `scripts/evaluate_meeting_preparation.py` | `F75F3DC71A551F4BBBCF0C349BDCA4BF323132DC0FF5F228439478B5DFC2B6DF` |
| `evals.json` | `A9934ADA2E7FC391ADBEC4B5D0F15A2C80086EC236D7FD634FA58A1DE368DA86` |
| `evals/selftest-ready.json` | `FC7A44A564F5A880BA8675C46A52843D6541F204802CA71B45151D071BBAE738` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Quy trình 10 bước; readiness/agenda rules, pack, JSON, engine, positive/negative test |
| A2 · Neo Kinh điển | PASS | Purpose–Process–Payoff, RACI/Decision Rights, Pre-read Discipline, Timeboxing/Parking, Four-Eyes |
| A3 · Chất ABM | PASS | Brain First – A.I Second; thời gian họp dùng cho trade-off/quyết định; “Làm 1 dùng N” |
| B4 · Nhiệm vụ đơn nhất | PASS | Chuẩn bị trước phiên họp đến readiness gate; đủ bốn khai báo; không gọi tên Skill khác |
| B5 · Dung lượng | PASS | Name đúng; description 532; thân 7.751; 141 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | 6 input theo bảng 4 cột; contract/pre-read/decision/roster/agenda/facilitation/state rõ |
| C7 · Có căn cứ | PASS | Source/version/age/SLA/access; prior commitment evidence; decision evidence/rule/deadline |
| C8 · Ranh giới Đỏ | PASS | Chặn stale, fake quorum/attendance/read/sent/invite, hidden commitment, overrun và false decision |
| C9 · Chống Injection | PASS | Invite/event/pre-read/URL/file là dữ liệu; không link/API/send/calendar/attendee mutation |
| D10 · Eval và Baseline | NOT PASS | 12 eval và self-tests đã chạy; chưa baseline/meeting-decider-outcome thật/pass^3/token/duration |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Asset Candidate có source/owner/version/evidence; decision-yield/overrun/carryover triggers |

## 5. Nguồn và quyết định thiết kế

- `ABM-SQS-00 v2.2`, Template v2.1, Rubric v2.1 và Lớp DNA v2.0 quyết định cấu trúc, gate và 12 tiêu chí.
- Baseline v1.0 cung cấp context/history/documents/commitments/open issues/attendees/questions/outcomes trước họp.
- SKILL-CREATOR và FINAL-GATEKEEPER quyết định I/O/eval contract, source/access, practical readiness, privacy và human invite boundary.

## 6. Audit trail

- Baseline v1.0 giữ nguyên tại cây `100-SKILLS-RND`.
- Positive test lần đầu phát hiện `decision_ids: []` bị hiểu sai là thiếu; engine được sửa để chấp nhận danh sách rỗng nhưng vẫn bắt field absent/sai type.
- v2.3 hiện hành: description **532**, thân **7.751**, 141 dòng; hai validator và self-tests PASS; không cache.

## 7. Điều kiện đóng D10

1. Chạy baseline v1.0 và v2.3 trên DECIDE/ALIGN/SOLVE/REVIEW/CREATE meetings thật, gồm no-meeting/async case.
2. Có owner/decider, source freshness/access, prior commitments, decision ground truth, roster/quorum và duration thật.
3. Meeting, decision, security/access và final invite reviewers xác nhận bằng evidence; invitation do người có quyền thực hiện.
4. Đo preparation effort, pre-read completion, quorum, agenda overrun, decision yield, carryover, commitment acceptance và no-show.
5. So sánh baseline/with-skill bằng pass^3; ghi `total_tokens`, `duration_ms` và unintended effect.
6. Giữ cấm tuyệt đối: fabricated history, hidden commitment/risk, fake quorum/attendance/read/sent/invite và false decision.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` sau khi đủ bằng chứng trên.
