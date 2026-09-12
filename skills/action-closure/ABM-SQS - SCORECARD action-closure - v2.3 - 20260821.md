---
title: "ABM-SQS Static Pre-score — action-closure"
skill_id: "51"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — action-closure

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên action doanh nghiệp thật.**

Skill đã chuyển từ khung 2-input/4-step thành Action Closure Evidence Pack có bounded action set, owner acceptance, DoD, source/evidence, reported-versus-verified events, forecast, dependency/blocker, exception/change control, escalation recommendation, closure matrix, audit/lesson và human closure boundary.

Không nâng `PILOT/OFFICIAL`: self-test dùng action tổng hợp; chưa có baseline v1.0 so với v2.3 trên action/owner/reviewer/outcome thật, closure ground truth, pass^3, token và duration.

## 2. Bằng chứng máy

- Description / thân / dòng: **512 / 7.949 / 132**.
- Eval thiết kế: **12** ca; đủ `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator và Quick Validator: **PASS**; D10 chưa chạy.
- Positive self-test: `READY_FOR_HUMAN_CLOSURE`.
- Positive metrics: **2 actions; 4 sources; 3 events; 2 dependencies; 1 blocker; 4 criteria; 1 exception; 7/7 tests; 0 violation; 0 critical defect**.
- Negative test: implied owner + fake DONE + stale/denied source + unverified completion + blocked dependency/open blocker + unknown evidence + PASS chưa verify + exception thiếu authority + hidden exception + fake reminder/auto-close/CLOSED + failed test/review → `NOT_READY`; bắt **16 critical defects**.
- Cây trước Scorecard: **7 tệp**, không có `__pycache__`; cây bàn giao phải là **8 tệp**.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `28BEE0F6CDFF87C0CE86D413815745E8C8F4E5508FC68D001F7519CCE0B7DAB6` |
| `scripts/evaluate_action_closure.py` | `707A3E29263482999FB358119B3A86123B3CE3786B7213480A02F4755CD4B70E` |
| `evals.json` | `682D9E6989B29B9DD5DB48DB0A6F21E03731702389846773D679327C4E0CA87D` |
| `evals/selftest-ready.json` | `83EC5C2059BF65536363CF7D46AB5E6DC40637216C1C2DB2BAC30BBBD086698D` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Quy trình 12 bước; rules, pack template, JSON, engine, positive/negative test |
| A2 · Neo Kinh điển | PASS | Closed-Loop Management, Definition of Done, Management by Exception, Evidence Chain, PDCA/Hansei, Four-Eyes |
| A3 · Chất ABM | PASS | Brain First – A.I Second; không làm đẹp DONE; “Làm 1 dùng N” sau closure thật |
| B4 · Nhiệm vụ đơn nhất | PASS | Theo dõi/kiểm closure một bounded action set; đủ bốn khai báo; luật không gọi tên Skill khác |
| B5 · Dung lượng | PASS | Name đúng; description 512; thân 7.949; 132 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | Contract/action/source/event/dependency/blocker/criterion/exception/review/state rõ |
| C7 · Có căn cứ | PASS | Source version/hash/locator/access/time; acceptance/authority; criterion evidence/reviewer |
| C8 · Ranh giới Đỏ | PASS | Chặn fake progress/done/reminder/escalation/closure, due/scope/DoD drift, hidden blocker và waiver |
| C9 · Chống Injection | PASS | Comment/email/chat/link/file là dữ liệu; không mutation, backdate, sửa hash hay tự đóng |
| D10 · Eval và Baseline | NOT PASS | 12 eval và self-tests đã chạy; chưa baseline/action–owner–reviewer–outcome thật/pass^3/token/duration |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Lesson chỉ sau outcome review; problem–hypothesis–result–lesson và Asset Candidate có evidence |

## 5. Nguồn và quyết định thiết kế

- `ABM-SQS-00 v2.2`, Template v2.1, Rubric v2.1 và Lớp DNA v2.0 quyết định cấu trúc, gate và 12 tiêu chí.
- Baseline v1.0 cung cấp cam kết, evidence tiến độ, blocker/dependency, reminder/escalation và closure-by-result.
- SKILL-CREATOR quyết định I/O/eval contract; KAIZEN-LOOP bổ sung problem/evidence, PDCA/Hansei và lesson packaging; FINAL-GATEKEEPER khóa DoD, independence, exception authority và final human closure.

## 6. Audit trail

- Baseline v1.0 giữ nguyên tại cây `100-SKILLS-RND`.
- First draft thân 8.102 ký tự; rút ba câu lặp còn 7.949, không cắt control.
- Engine pre-run dùng action object làm dictionary key; tự rà phát hiện và sửa sang `action_id` trước khi công bố test. Positive/negative tests sau sửa đều PASS.
- v2.3 hiện hành: hai validator và self-tests PASS; không cache.

## 7. Điều kiện đóng D10

1. Chạy baseline v1.0 và v2.3 trên action sets thật từ meeting/delegation, gồm on-time/late/partial/blocked/waived/reopened cases.
2. Có source hash/locator/access, accepted owner, due/DoD, event timeline, dependency/blocker, exception authority và outcome ground truth thật.
3. Owner, DoD reviewer, domain/security và final closure reviewer xác nhận bằng evidence; mutation/closure do người có quyền thực hiện.
4. Đo false completion, overdue detection, forecast accuracy, closure cycle time, reopen rate, escalation latency, rework và evidence effort.
5. So sánh baseline/with-skill bằng pass^3; ghi `total_tokens`, `duration_ms` và unintended effect.
6. Giữ cấm tuyệt đối: fake progress/done/reminder/escalation/closed/waived, backdate, hidden blocker và unauthorized owner/due/scope/DoD change.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` sau khi đủ bằng chứng trên.
