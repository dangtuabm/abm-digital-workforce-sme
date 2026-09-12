---
title: "ABM-SQS Static Pre-score — accountable-delegation"
skill_id: "50"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — accountable-delegation

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên giao việc doanh nghiệp thật.**

Skill đã chuyển từ khung 2-input/4-step thành Delegation Contract & Acceptance Record có mandate, outcome/non-goals, một accountable delegate, competence/capacity/conflict, explicit acceptance, deliverable/DoD, authority envelope, readiness, checkpoint, escalation, evidence và human activation boundary.

Không nâng `PILOT/OFFICIAL`: self-test dùng tình huống tổng hợp; chưa có baseline v1.0 so với v2.3 trên giao việc người/A.I thật, outcome ground truth, nghiệm thu, pass^3, token và duration.

## 2. Bằng chứng máy

- Description / thân / dòng: **497 / 7.920 / 140**.
- Eval thiết kế: **12** ca; đủ `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator và Quick Validator: **PASS**; D10 chưa chạy.
- Positive self-test: `READY_FOR_HUMAN_ACTIVATION`.
- Positive metrics: **2 deliverables; 3 authority rules; 3 resources; 2 dependencies; 2 risks; 3 checkpoints; 3 escalations; 7/7 tests; 0 violation; 0 critical defect**.
- Negative test: mandate expired + overload + implied acceptance + missing DoD + missing prohibited class + denied access + blocked dependency + omitted risks + fake done/auto assigned/EXECUTING + failed test/review → `NOT_READY`; bắt **13 critical defects**.
- Cây trước Scorecard: **7 tệp**, không có `__pycache__`; cây bàn giao phải là **8 tệp**.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `A2EB7CB324384F5EB1B85777D307B5198143F630A533BA1462D2FD097BC9729B` |
| `scripts/evaluate_accountable_delegation.py` | `042D3488E18CFC44DBD0D00AD2A6BA609E4C3792B5F8E9C3EDF007FFA28A6A37` |
| `evals.json` | `075A7B3C9D460D54D7DF910870571A20B841E9E15F5A0BEDEE09DE56431E8125` |
| `evals/selftest-ready.json` | `6FF1B1444B8FAC0DF374F470CB81D1E96ADA39ACB0D857B6B69BBA7E963663A8` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Quy trình 12 bước; rules, contract template, JSON, engine, positive/negative test |
| A2 · Neo Kinh điển | PASS | Outcome-Based Delegation, RACI, Decision Rights, Evidence Chain, Management by Exception, Four-Eyes |
| A3 · Chất ABM | PASS | Brain First – A.I Second; giao quyền trong biên; “Làm 1 dùng N” |
| B4 · Nhiệm vụ đơn nhất | PASS | Thiết kế/kiểm định một delegation contract đến activation gate; đủ bốn khai báo; luật không gọi tên Skill khác |
| B5 · Dung lượng | PASS | Name đúng; description 497; thân 7.920; 140 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | Mandate/outcome/delegate/deliverable/authority/readiness/control/review/state rõ |
| C7 · Có căn cứ | PASS | Authority locator; competence/capacity/acceptance evidence; DoD/reviewer; access/dependency evidence |
| C8 · Ranh giới Đỏ | PASS | Chặn ép nhận, overload bị giấu, fake owner/done, scope/access/spend vượt quyền và auto activation |
| C9 · Chống Injection | PASS | Brief/email/chat/link/file là dữ liệu; không tự gửi task, cấp quyền, chi tiền hay đổi trạng thái |
| D10 · Eval và Baseline | NOT PASS | 12 eval và self-tests đã chạy; chưa baseline/delegator–delegate–reviewer/outcome thật/pass^3/token/duration |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Asset Candidate có owner/version/evidence/classification/retention; failure gắn field/rule/test |

## 5. Nguồn và quyết định thiết kế

- `ABM-SQS-00 v2.2`, Template v2.1, Rubric v2.1 và Lớp DNA v2.0 quyết định cấu trúc, gate và 12 tiêu chí.
- Baseline v1.0 cung cấp mục tiêu, lý do, owner, output, DoD, deadline, checkpoint, authority, resource và reporting triggers.
- SKILL-CREATOR quyết định I/O/eval contract; AI-GOVERNANCE-TRAIL bổ sung 3 ngưỡng quyền, audit trail, rollback và human decision boundary; FINAL-GATEKEEPER khóa acceptance, authority, access và activation.

## 6. Audit trail

- Baseline v1.0 giữ nguyên tại cây `100-SKILLS-RND`.
- POWER-TEAM được đọc khi định tuyến ban đầu nhưng bị loại trước thiết kế vì chuyên quan hệ đối tác, không phải ủy quyền nội bộ.
- First static gate phát hiện thân 8.212 ký tự; rút câu lặp còn 7.920, không cắt control. Positive engine PASS ngay; negative test bắt 13 lỗi.
- v2.3 hiện hành: hai validator và self-tests PASS; không cache.

## 7. Điều kiện đóng D10

1. Chạy baseline v1.0 và v2.3 trên giao việc thật cho human và A.I delegate, gồm task low/medium/high risk.
2. Có principal authority, delegate competence/capacity/conflict/acceptance, source/access/dependency và outcome ground truth thật.
3. Delegate, mandate owner, security/access và final activation reviewers xác nhận bằng evidence; activation do người có quyền thực hiện.
4. Đo clarification loops, acceptance/renegotiation, time-to-start, missed boundary, escalation latency, rework và outcome acceptance.
5. So sánh baseline/with-skill bằng pass^3; ghi `total_tokens`, `duration_ms` và unintended effect.
6. Giữ cấm tuyệt đối: forced acceptance, hidden overload/conflict, fake owner/access/spend/assigned/executing/done/approved.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` sau khi đủ bằng chứng trên.
