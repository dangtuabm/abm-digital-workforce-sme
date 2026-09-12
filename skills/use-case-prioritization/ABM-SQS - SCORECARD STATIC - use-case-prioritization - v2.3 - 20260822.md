---
document_code: "ABM-SQS-SC-91"
skill: "use-case-prioritization"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — USE-CASE PRIORITIZATION v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh để nhận Opportunity Register có bằng chứng, khóa critical gates và scoring contract, chấm điểm theo rubric/weight có nguồn, kiểm double-count/UNKNOWN/value hypothesis, tính lại weighted score, stress sensitivity và đề xuất SHORTLIST/BACKLOG/DEFER/EXCLUDE. Output dừng trước selected portfolio, vendor/architecture, resource commitment và spend. D10 chưa đạt vì chưa pilot trên portfolio, evidence, gates, weights, economics, constraints và human decision thật.

Chuỗi kiểm định: `SKILL-CREATOR → A.I-ROI-MEASURE → FINAL-GATEKEEPER`; tham chiếu `priority-allocation` để khóa capacity boundary.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 `designed_not_run` |
| SKILL-CREATOR quick_validate | PASS — `Skill is valid!` |
| Description | 528 ký tự, ≤ 600 |
| Body | 7.775 ký tự, ≤ 8.000 |
| Lines | 114, ≤ 500 |
| Evals | 12; must_trigger, must_not_trigger, no_false_ask, ambiguity, missing_input, red_line, injection, adversarial, sensitivity, capacity_boundary |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive fixture:** `READY_FOR_HUMAN_PRIORITY_DECISION`; 0 defect; 0 review gap. Coverage: 12 evidence sources, 8 criteria, 10 candidates, 10 critical gates, 10 priority results, 3 sensitivity scenarios, 5 portfolio views, 6 decisions, 10 test cases, 6 risks, 7/7 gate tests và 6/6 reviews.

**Negative fixture:** `NOT_READY`; 188 defects; 6 review gaps. Engine chặn missing mandate/scoring/authority; fabricated pain/baseline/metric/ROI; realized-ROI claim trước pilot; UNKNOWN thành 0; gate score washing; sponsor-driven weight/score; hidden double-count; protected attribute; vendor/architecture/budget/assignment/stop-work/publication/send; evidence mutation; prompt injection và secret material.

## 4. Final Gatekeeper

- PASS boundary: prioritization khác discovery, post-implementation ROI, solution selection, allocation commitment và work design.
- PASS gates: scope/owner, evidence, data rights, testability, human control, harm/security/privacy phải PASS trước rank; critical fail không bị score bù.
- PASS scoring: 8 criteria có anchors/evidence/missing/double-count rule; weights tổng 100 và do human authority duyệt; score engine được recompute.
- PASS value integrity: pre-pilot chỉ value hypothesis/baseline candidate/range; không claim realized ROI; effort/cost/risk tách khỏi benefit.
- PASS uncertainty: conflict/UNKNOWN/tie giữ nguyên; sensitivity trả rank movement, shortlist stability và trigger.
- PASS portfolio authority: SHORTLIST/BACKLOG/DEFER/EXCLUDE chỉ là proposal; selected set, exception, capacity, people và spend vẫn PENDING human decision.

## 5. Nguồn nội bộ sử dụng

- Bộ tiêu chuẩn Skill ABM và `SKILL-CREATOR` — cấu trúc, eval, static gate và D10.
- `A.I-ROI-MEASURE` — kỷ luật baseline, công thức, nguồn số và ranh giới giữa value hypothesis với realized ROI; không tái sử dụng tuyên bố thương mại làm điểm ưu tiên.
- `priority-allocation` Skill 18 — mandatory/gates, capacity, dependency, opportunity cost và commitment boundary.
- `FINAL-GATEKEEPER` — negative controls, human authority và bàn giao.

Không dùng universal weights, benchmark, ROI threshold hoặc claim pháp lý/thị trường bên ngoài. Portfolio thật phải khóa scoring contract và evidence theo tổ chức.

## 6. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `CAD7BE820DAC7F03145CD6B1A5C9EEAC9410363FF81F1473C5E4FA31D02D46C9` |
| evaluator | `D42F8B33ECE255EDFE763B400AB27115D0E678FD54CB59D2C475AEA7779D6B92` |
| evals | `7429A5AB59B778C2E1688203626A8DDD56C638AE16F93D4541D1D4B862367C97` |
| positive fixture | `25D14B11F240C65B13F9A8059C53C3ED4283273FDB6E5A8286081DB6BF5196D2` |
| negative fixture | `5375F02AE89768C29493E6D2890BC39B1567D6421B8056F7758673E94B9B64E7` |
| rules reference | `CB43FFD14E94712F584B468E78E36F8588E67380B9AB4E98EF4361C295C8EDAE` |
| pack template | `51C6040BC966E0A8C8B3705A0A84A295763F820BDEC41F82486A97611C4186A4` |

## 7. Cổng còn thiếu

D10 cần pilot trên candidate register/version/hash, source/rights, critical gates, approved criteria/weights/rubric, value/effort/cost/risk ranges, dependencies/capacity envelope và portfolio authority thật. Sáu owner phải xác nhận gates, scores, double-count, sensitivity, disposition và selected-set boundary; kèm false trigger, token và duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.

