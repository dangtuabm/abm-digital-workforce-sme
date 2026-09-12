---
title: "ABM-SQS Static Pre-score — meeting-intelligence"
skill_id: "49"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — meeting-intelligence

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên cuộc họp doanh nghiệp thật.**

Skill đã chuyển từ khung 2-input/4-step thành Meeting Evidence & Commitment Record: khóa nguồn và quyền ghi nhận, định danh người nói, phân biệt thảo luận–đề xuất–quyết định–cam kết, kiểm chứng thẩm quyền quyết định, sự chấp nhận của người nhận việc, bất đồng, điểm chưa rõ, hiệu chỉnh và cổng phân phối do con người phê duyệt.

Không nâng `PILOT/OFFICIAL`: self-test dùng cuộc họp tổng hợp; chưa có baseline v1.0 so với v2.3 trên recording/transcript/notes thật, ground truth do meeting owner–decider–action owners xác nhận, pass^3, token và duration.

## 2. Bằng chứng máy

- Description / thân / dòng: **545 / 7.780 / 137**.
- Eval thiết kế: **12** ca; có `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator và Quick Validator: **PASS**; D10 chưa chạy.
- Positive self-test: `READY_FOR_RECORD_REVIEW`.
- Positive metrics: **4/4 nguồn active; 0 source violation; 4/4 speaker verified/high; 2 quyết định, 0 violation; 3 hành động, 0 violation; 1 dissent; 2 unknown; 1 correction; 7/7 tests; 0 forbidden/unauthorized; 0 critical defect**.
- Negative test: nguồn `DENIED` + decider confidence thấp + suy diễn đề xuất thành quyết định + action acceptance ngầm định + giả `DONE` + giấu dissent + giả `DISTRIBUTED` + failed test → `NOT_READY`; bắt **10 critical defects**.
- Cây trước Scorecard: **8 tệp**, không có `__pycache__`; cây bàn giao phải là **9 tệp**.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `489C6351137444DBC0927B0681059ADB3560618891616E18B3F86FF77E5CD873` |
| `scripts/evaluate_meeting_intelligence.py` | `E3BA0720A7C7C79BE21D0575B0A09E5C6314D6C69FF04E5CEB27641EA06EE5B8` |
| `evals.json` | `4041584931055FA3FB193345C9C8BF6F75FE7FDF2FB3F40FD597587F6119FF12` |
| `evals/selftest-ready.json` | `7CD8EB82839CDDF125525BDD2B17F377A9B37F54233FC991A5D182B9DCF6005C` |
| `evals/selftest-ready-result.json` | `4E3EB51A6E586C8E80BF7663AC8ABAD20CF0978AB7E1C8100C66118F5C457913` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Quy trình 10 bước; record rules, mẫu biên bản, JSON, engine, positive/negative test |
| A2 · Neo Kinh điển | PASS | Speech-act ladder, Decision Rights, RACI, Evidence Chain, Four-Eyes và Corrective Record |
| A3 · Chất ABM | PASS | Brain First – A.I Second; không biến lời nói mơ hồ thành mệnh lệnh; “Làm 1 dùng N” |
| B4 · Nhiệm vụ đơn nhất | PASS | Chuyển bằng chứng cuộc họp thành hồ sơ quyết định–cam kết đến record review; đủ bốn khai báo; luật không gọi tên Skill khác |
| B5 · Dung lượng | PASS | Name đúng; description 545; thân 7.780; 137 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | Contract/source/speaker/decision/action/dissent/correction/review và state rõ |
| C7 · Có căn cứ | PASS | Source/version/hash/locator/access/consent; speaker confidence; authority/acceptance evidence |
| C8 · Ranh giới Đỏ | PASS | Chặn quyết định suy diễn, owner ép buộc, dissent bị giấu, quote bị sửa, fake done/distributed |
| C9 · Chống Injection | PASS | Recording/transcript/note/link là dữ liệu; không tự gửi, tạo task, sửa quyền hay phân phối |
| D10 · Eval và Baseline | NOT PASS | 12 eval và self-tests đã chạy; chưa baseline/meeting–decider–action-owner ground truth thật/pass^3/token/duration |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Asset Candidate có owner/version/evidence; trigger theo authority, acceptance, dissent và correction defect |

## 5. Nguồn và quyết định thiết kế

- `ABM-SQS-00 v2.2`, Template v2.1, Rubric v2.1 và Lớp DNA v2.0 quyết định cấu trúc, gate và 12 tiêu chí.
- Baseline v1.0 cung cấp transcript/participants/topics/decisions/actions trước khi nâng thành evidence-grade record.
- SKILL-CREATOR quyết định I/O/eval contract; MEETING-MINUTES bổ sung decision, action “ai–làm gì–khi nào–báo ai”, unresolved items và review trong 24 giờ; FINAL-GATEKEEPER khóa authority, privacy, correction và human distribution boundary.

## 6. Audit trail

- Baseline v1.0 giữ nguyên tại cây `100-SKILLS-RND`.
- Engine được bổ sung kiểm tra coverage để mọi decision/action/dissent/unknown đã biết phải xuất hiện trong record.
- Negative test lần đầu dùng sai định danh `SP01` thay vì `SP-01`, dừng ở `StopIteration`; lần chạy lại đúng schema PASS và bắt đủ 10 lỗi. Dấu vết này không được dùng để làm đẹp kết quả.
- v2.3 hiện hành: description **545**, thân **7.780**, 137 dòng; hai validator và self-tests PASS; không cache.

## 7. Điều kiện đóng D10

1. Chạy baseline v1.0 và v2.3 trên các cuộc họp DECIDE/ALIGN/SOLVE/REVIEW thật, có consent và phân loại dữ liệu.
2. Có recording/transcript/notes/version/hash/locator thật; meeting owner xác nhận speaker identity và record coverage.
3. Decider xác nhận decision/authority/dissent; từng action owner xác nhận deliverable, deadline, acceptance criteria và report-to.
4. Privacy/security và final-record reviewers duyệt; việc gửi, phân phối hay tạo task chỉ do người có quyền thực hiện.
5. Đo false decision, false action owner, omitted dissent, correction rate, review effort, time-to-confirm và unintended effect.
6. So sánh baseline/with-skill bằng pass^3; ghi `total_tokens`, `duration_ms`; giữ cấm tuyệt đối fake quote/decision/owner/done/distributed.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` sau khi đủ bằng chứng trên.
