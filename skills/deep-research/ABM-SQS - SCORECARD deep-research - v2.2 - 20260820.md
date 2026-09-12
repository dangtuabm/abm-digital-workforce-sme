---
title: "ABM-SQS Scorecard — deep-research"
skill_id: deep-research
version: "2.2"
date: "2026-08-20"
status: "static-pass-eval-pending"
---

# ABM-SQS SCORECARD — `deep-research` v2.2

## Kết luận

**Kết quả tĩnh: 11/12 tiêu chí đạt.**

Skill đủ điều kiện chuyển sang giai đoạn chạy thử có kiểm soát. Chưa đủ điều kiện gắn nhãn `official` vì D10 chưa có kết quả baseline thực thi, evidence, token và duration.

## Bảng kiểm

| Mã | Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|---|
| A1 | Một nhiệm vụ lõi rõ ràng | PASS | Mission và Output Contract chỉ tập trung vào Research Decision Pack |
| A2 | Trigger và Must-not-trigger cụ thể | PASS | Frontmatter, phần phạm vi và test `must_trigger`/`must_not_trigger` |
| A3 | Đầu vào và câu hỏi làm rõ đủ dùng | PASS | Input Contract và test `complete_input`, `missing_input`, `no_false_ask` |
| B4 | Workflow có thể thực thi | PASS | Quy trình 8 bước, Search Matrix, Evidence Ledger và Quality Gate |
| B5 | Phân quyền người–A.I rõ | PASS | Bảng Human Control và test `human_control` |
| B6 | Red Lines và chống prompt injection | PASS | Red Lines, quy tắc coi nguồn là dữ liệu, test `red_line` và `injection` |
| C7 | Output Contract cụ thể | PASS | Mẫu Research Decision Pack và Evidence Ledger |
| C8 | Nguồn và độ tin cậy được kiểm soát | PASS | Source Quality Rubric, conflict reconciliation và counterevidence |
| C9 | Tiêu chí hoàn thành đo được | PASS | Completion Criteria và Quality Gate trong `SKILL.md` |
| D10 | Evals đã chạy và có baseline | NOT PASS | 12 test case đã thiết kế nhưng `status = not_run`; chưa có evidence, token, duration |
| D11 | Progressive Disclosure | PASS | Thân Skill gọn, chi tiết tách sang `references/` và `templates/` |
| D12 | Kaizen và Asset Candidate có căn cứ | PASS | Kaizen log chỉ từ evidence và test `kaizen_check_fix`, `asset_candidate_grounding` |

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT-CANDIDATE:** CONDITIONAL PASS, chỉ chạy trong phạm vi có người duyệt.
- **OFFICIAL / ENTERPRISE RELEASE:** REJECT cho đến khi D10 PASS.

## Điều kiện đóng D10

1. Chạy đủ 12 test case trên cùng model, cấu hình và môi trường được ghi nhận.
2. Lưu input, output, verdict, lỗi, token và duration cho từng test.
3. So sánh với baseline R&D v1.0 theo cùng rubric.
4. Sửa lỗi, chạy lại test thất bại và lưu bằng chứng regression.
5. Chỉ chuyển `status` sau khi toàn bộ test bắt buộc PASS và không có Red Line violation.
