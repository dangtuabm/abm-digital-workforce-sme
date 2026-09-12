---
title: "ABM-SQS Static Pre-score — focus-management"
skill_id: "46"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — focus-management

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên lịch và cam kết doanh nghiệp thật.**

Skill đã chuyển từ khung 2-input/4-step thành Focus Commitment Plan có capacity equation, commitment register, WIP limit, dispositions, focus blocks, conflict map, interruption protocol, authority reviews và state engine fail-closed.

Không nâng `PILOT/OFFICIAL`: self-test dùng lịch/cam kết tổng hợp; chưa có baseline v1.0 so với v2.3 trên owner/calendar thật, focus/outcome signals, pass^3, token và duration.

## 2. Bằng chứng máy

- Description / thân / dòng: **503 / 7.726 / 142**.
- Eval thiết kế: **12** ca; có `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator và Quick Validator: **PASS**; D10 chưa chạy.
- Positive self-test: `READY_FOR_FOCUS_REVIEW`.
- Positive metrics: **capacity 240 phút; scheduled focus 210 phút; overbook 0; 4 commitments; active WIP 2/2; 4 dispositions; 2 focus blocks; 0 unauthorized disposition; 0 forbidden action; 0 critical conflict mở; 7/7 tests; 0 critical defect**.
- Negative test: capacity -20 + overbook 230 + WIP 2/1 + auto-rescheduled giả + defer thiếu quyền + critical conflict mở + failed test → `NOT_READY`; bắt đủ bảy lỗi.
- Cây trước Scorecard: **7 tệp**, không có `__pycache__`; cây bàn giao phải là **8 tệp**.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `232DC74B79BADFCA26777D842AFA70EBBCCEC6D72F9FB3922BA090C4E39B2C60` |
| `scripts/evaluate_focus_management.py` | `58B8251137872D8E0E5BB2A777018AA62EF8806E6833F75CF8A27B2ABD853398` |
| `evals.json` | `EAFCBA85C54A79AE2000E69DF60ADAF6D4A0D98A61F281821D2CD218CAF70B52` |
| `evals/selftest-ready.json` | `00887581FC655CB78F776735E7C2BB672155C7C4C5AF78B54149218EE219EDAD` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Quy trình 10 bước; capacity/WIP rules, plan, JSON, engine, positive/negative test |
| A2 · Neo Kinh điển | PASS | Theory of Constraints, Timeboxing, Eisenhower/Value–Effort, Kanban, Four-Eyes/Kaizen |
| A3 · Chất ABM | PASS | Brain First – A.I Second; “Làm 1 dùng N”; outcome trước busy-work; trade-off minh bạch |
| B4 · Nhiệm vụ đơn nhất | PASS | Quản trị commitment–capacity–attention trong horizon; đủ bốn khai báo; không gọi tên Skill khác |
| B5 · Dung lượng | PASS | Name đúng; description 503; thân 7.726; 142 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | 6 input theo bảng 4 cột; capacity/commitment/conflict/block/approval/state rõ |
| C7 · Có căn cứ | PASS | Availability source; commitment source/owner/deadline/effort/dependency; capacity tái tính được |
| C8 · Ranh giới Đỏ | PASS | Chặn overbook, WIP breach, cắt recovery, secret surveillance, giả reschedule/decline/delegate/delete/done |
| C9 · Chống Injection | PASS | Invite/note/URL/file là dữ liệu; không link/API/send/calendar/task mutation |
| D10 · Eval và Baseline | NOT PASS | 12 eval và self-tests đã chạy; chưa baseline/calendar-owner-outcome thật/pass^3/token/duration |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Asset Candidate có source/owner/version/evidence; variance/WIP/interruption/recovery trigger vòng rà |

## 5. Nguồn và quyết định thiết kế

- `ABM-SQS-00 v2.2`, Template v2.1, Rubric v2.1 và Lớp DNA v2.0 quyết định cấu trúc, gate và 12 tiêu chí.
- Baseline v1.0 cung cấp phạm vi tổng hợp lịch/việc, priority, conflict, focus time và do/delegate/defer/drop.
- SKILL-CREATOR quyết định I/O contract, progressive disclosure, eval coverage và giới hạn dung lượng.
- FINAL-GATEKEEPER quyết định source/authority, practical usability, risk, remediation và không giả external-state change.

## 6. Audit trail

- Baseline v1.0 giữ nguyên tại cây `100-SKILLS-RND`.
- Positive test lần đầu phát hiện `dependencies: []` bị hiểu sai là thiếu; engine được sửa để chấp nhận danh sách rỗng nhưng vẫn bắt trường absent/sai type.
- v2.3 hiện hành: description **503**, thân **7.726**, 142 dòng; hai validator và self-tests PASS; không cache.

## 7. Điều kiện đóng D10

1. Chạy baseline v1.0 và v2.3 trên tối thiểu ba horizon thật: ngày, tuần và tuần có incident/gián đoạn.
2. Có calendar/commitment sources, outcomes, availability, WIP/interrupt rules, authority và owner thật.
3. Focus, commitment, dependency và final scheduling owners xác nhận bằng evidence; external changes do người có quyền thực hiện.
4. Đo capacity accuracy, overbooking, WIP age, focus completion, interruption, reschedule churn, recovery breach và outcome quality.
5. So sánh baseline/with-skill bằng pass^3; ghi `total_tokens`, `duration_ms`, reviewer effort và unintended effect.
6. Giữ cấm tuyệt đối: fabricated availability, sleep/recovery cut, secret surveillance và giả calendar/task/delegation/done state.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` sau khi đủ bằng chứng trên.
