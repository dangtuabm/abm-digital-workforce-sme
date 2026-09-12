# USE-CASE PRIORITIZATION — CONTROL RULES

## 1. Boundary

- Input chính là Opportunity Register từ Skill 90 hoặc tương đương có evidence trace.
- Skill 91 đánh giá, xếp hạng đề xuất và shortlist; không khám phá pain, commit nguồn lực, chọn vendor, duyệt ngân sách hoặc thiết kế workflow.
- Khi cần allocation dưới capacity/dependency/WIP thật, chuyển `priority-allocation`; khi selected use case cần thiết kế vai trò, chuyển Skill 92.

## 2. Gate before score

Candidate chỉ được rank khi critical gates về scope/owner, evidence sufficiency, data rights, output testability, human control và prohibited harm đều PASS. FAIL → EXCLUDE; UNKNOWN → DEFER. Điểm cao không bù gate FAIL/UNKNOWN.

## 3. Scoring contract

Mỗi criterion phải có ID, định nghĩa, hướng tốt/xấu, weight, rubric anchors, evidence rule, owner, missing rule và double-count rule. Weights do human authority duyệt và tổng bằng 100. Không dùng universal weights.

## 4. Evidence and value

- Score phải trỏ source/version; UNKNOWN không phải 0.
- Pre-pilot chỉ ghi value hypothesis/range/baseline candidate; không gọi là realized ROI.
- Không cộng cùng một lợi ích ở pain, workload, value và scalability nếu không chứng minh độc lập.
- Effort/cost/risk hiển thị riêng; không giấu bằng composite.

## 5. Ranking integrity

- Lưu input, contract, engine version và hash.
- Tie-break theo rule đã duyệt; nếu chưa có, giữ tie và yêu cầu decision.
- Chạy sensitivity theo weight/range/unknown/gate/capacity shock; ranking đổi mạnh → UNSTABLE.
- Hiển thị score distribution, uncertainty, gate state, constraint, opportunity cost và simpler alternative.

## 6. Human authority

Output là proposal: SHORTLIST/BACKLOG/DEFER/EXCLUDE. Chỉ human portfolio owner phê duyệt selected set, exception, resource envelope, spend, assignment và stop work.

