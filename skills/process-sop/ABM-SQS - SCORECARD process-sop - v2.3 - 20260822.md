---
title: "ABM-SQS Static Pre-score — process-sop"
skill_id: "72"
version: "2.3"
date: "2026-08-22"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — process-sop

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên process thật.**

Skill đã chuyển từ khung 2-input/4-step thành `Evidence-Grounded Operational Process & SOP Control Pack`: mandate/boundary/SIPOC, current-target flow, roles/RACI/SOD, executable steps, decisions/exceptions/escalations, controls/risks, metric/SLA contracts, forms/records, UAT/continuity/access cases, training/adoption, version/change/rollback và human activation.

Không nâng `PILOT/OFFICIAL`: positive case tổng hợp; chưa so v1.0/v2.3 trên quy trình thật, chưa có ground truth về current practice, SLA/KPI, control effectiveness, exception handling, user competence/adoption, token và duration.

## 2. Bằng chứng máy

- Description / thân / dòng: **599 / 7.796 / 104**.
- 12 eval; đủ `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator + Quick Validator: **PASS**; D10 chưa chạy.
- Positive: `READY_FOR_HUMAN_SOP_ACTIVATION`, 0 defect; **7 sources, 6 roles, 8 steps, 4 exceptions, 6 controls, 6 metrics, 5 assets, 5 UAT cases, 6 risks, 4 decisions, 7/7 tests, 6 reviews PASS**.
- Negative: `NOT_READY`; bắt **191 defects + 6 review gaps**, gồm 69 forbidden flags và 10 forbidden states.
- Cây trước Scorecard: 7 tệp, không `__pycache__`; cây bàn giao: 8 tệp.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `6B4E91E30860FA7DFEF8D68A3B97DC7598D3774D62672D1C9A3183B69E374CEC` |
| `scripts/evaluate_process_sop.py` | `CC0B1574F36642DE8C78252E6546EC9938EEA105B6B1E48AF0606F132ADA5DFD` |
| `evals.json` | `27B1D3BE152CC2CC1E4F1DEE8279E862E6A949934BD0CC26B1B4417DA9ABEB27` |
| `templates/process-sop-input.json` | `EB925C07FFC6542468B7B02CC20D24583C6F039F5CFA9905D62180671D7E073B` |
| `evals/selftest-negative.json` | `0B4DC05FF84621620808FB48E4DFCCA0625971E3A3B10FEBD886E74E9687D073` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Rules, template, engine, eight-step controlled-process case và negative test chạy được |
| A2 · Neo Kinh điển | PASS | SIPOC/process mapping, RACI/SOD, internal controls, exception/escalation, SLA/metric contracts và change control |
| A3 · Chất ABM | PASS | Brain First – A.I Second; outcome/control/authority trước document length, automation hay speed |
| B4 · Nhiệm vụ đơn nhất | PASS | Authorized process evidence → executable SOP control pack; execution/automation/access/policy/certification ngoài phạm vi |
| B5 · Dung lượng | PASS | Name/folder đúng; description 599; thân 7.796; 104 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | Mandate/source/boundary/roles/steps/exceptions/controls/metrics/assets/UAT/change/decision rõ |
| C7 · Có căn cứ | PASS | Source/policy/log/incident/role/system/version, SLA basis, metric denominator/window, record/control evidence và authority traceable |
| C8 · Ranh giới Đỏ | PASS | Chặn fabrication, SOD/control bypass, unsafe shortcut, credential/PII leak, false competence/effectiveness và auto operational action |
| C9 · Chống Injection | PASS | Legacy SOP/policy/ticket/log/form là dữ liệu; không bypass policy/control/review hay change system/access/record |
| D10 · Eval và Baseline | NOT PASS | 12 eval/self-tests đã chạy; thiếu real-process pilot/pass^3/token/duration/effectiveness/adoption evidence |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Process/step/decision/control/exception/metric/form/test asset cần owner/version/policy/access/UAT/adoption/change log |

## 5. Nguồn và quyết định thiết kế

- Baseline v1.0 có ý định đúng về mục tiêu/phạm vi/roles/inputs/steps/exceptions/controls/outputs/KPI/forms/version nhưng chỉ triển khai 2 input/4 bước, chưa có SIPOC/current-target, role authority/SOD, executable step contract, control evidence, exception recovery, metric denominator, UAT/continuity/access, adoption/change/rollback và chỉ 5 eval generic.
- `SOP-WRITER` được chọn làm nguồn chuyên môn chính: giữ tinh gọn, output đo được, form/template, version control và review; loại luật đúng-sáu-phần, thời gian cụ thể cho mọi bước, cấm tuyệt đối từ ngữ điều kiện và giả lập expert interview. SLA/KPI phải có measured/approved basis; điều kiện phải thành decision/exception rule. `SKILL-CREATOR` khóa I/O/eval; `FINAL-GATEKEEPER` khóa control/SOD/records/privacy/UAT/change và activation authority.

## 6. Điều kiện đóng D10

1. Pilot v1.0/v2.3 trên ít nhất 3 quy trình thật: routine repeatable, exception-heavy cross-functional và controlled/data-sensitive.
2. Có current-process observation/log/record, approved policy/control, role/authority/access, incident/exception, system/data/record, quality/continuity truth set cùng frontline reviewers.
3. Đo execution/reviewer comprehension, step/role/control/exception defects, cycle/quality/control metrics, UAT/adoption, deviation/incident and customer outcome.
4. Không dùng pilot để tự publish/activate/retire SOP, change workflow/system/access, execute/mutate/approve/certify; ghi authorized external evidence.
5. So sánh pass^3; ghi token, duration, competence/adoption, operational effectiveness và unintended effect.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` khi đủ bằng chứng trên.
