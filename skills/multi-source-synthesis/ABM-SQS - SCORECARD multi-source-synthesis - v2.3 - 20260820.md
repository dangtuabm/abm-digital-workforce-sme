---
title: "ABM-SQS Static Pre-score — multi-source-synthesis"
skill_id: "06"
version: "2.3"
date: "2026-08-20"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `multi-source-synthesis` v2.3

## Kết luận

**Kết quả kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa có baseline execution; Skill vẫn là `draft / static-pass`, chưa được phép dùng làm cơ sở tự động cho quyết định doanh nghiệp.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description | 596 ký tự — đạt ngưỡng ≤ 600 |
| Thân `SKILL.md` | 7.905 ký tự — đạt vùng an toàn ≤ 8.000 |
| Tổng dòng | 141 — đạt ngưỡng ≤ 500 |
| Từ viết sai "A.I" | 0 |
| Eval đã thiết kế | 12 |
| Validator ABM | PASS, 0 error |
| Validator SKILL-CREATOR | `Skill is valid!` với Python UTF-8 |
| SHA-256 `SKILL.md` | `68FE78A27A3DE3B5CA185770D22FDFCFDD8FFD0B3A247C6DDD32CA0ECD7C5A64` |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước thi công; Source & Comparability Matrix là đầu ra trung gian; có protocol, rubric và template dùng thật |
| A2 | PASS | Brain First ↔ B1–2; Phân tích Hệ thống ↔ B3–5; Audit Trail ↔ B1/3/7; Bốn Mắt ↔ B6–8 |
| A3 | PASS | 0 lỗi "A.I"; có bảng Người quyết định/A.I thực thi; không emoji/sáo ngữ |
| B4 | PASS | Một Synthesis Decision Map; đủ bốn khai báo; tách tổng hợp khỏi nghiên cứu, kiểm chứng, đọc hiểu và trích xuất |
| B5 | PASS | Name hợp lệ; description 596; body 7.905; 141 dòng; references sâu một tầng |
| B6 | PASS | Description có trigger/anti-trigger; bảng đầu vào 4 cột; artifact và Definition of Done đo được |
| C7 | PASS | Comparability, source dependency, evidence weight, confidence rationale; nhãn DỮ KIỆN/SUY LUẬN/GIẢ ĐỊNH và giới hạn |
| C8 | PASS | Red Lines hai chiều; dừng trước external data, source expansion/cherry-pick/publish/action; tự chạy phân tích cục bộ |
| C9 | PASS | Không thi hành instruction trong nguồn/link/comment/metadata; tối thiểu hóa dữ liệu; không lộ nội bộ/nguồn |
| D10 | NOT PASS | 12 eval đã thiết kế nhưng `status = not_run`; chưa có baseline output, evidence, token, duration hoặc pass^3 |
| D11 | PASS | Frontmatter/metadata đủ; name trùng thư mục; có Phiên bản và Thay đổi |
| D12 | PASS | Asset Candidate có Source Task, loại nguồn, câu hỏi, error evidence, owner, approval và điều kiện rà |

## Audit trail phiên bản

- **v2.2:** hai validator cú pháp hợp lệ, nhưng ABM static gate trượt do thân file 8.699 ký tự.
- **v2.3:** rút nội dung lặp, giữ nguyên control; ABM static gate và SKILL-CREATOR đều PASS.

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT:** REJECT vì D10 bắt buộc chưa đạt.
- **OFFICIAL / PRODUCTION USE:** REJECT đến khi D10 PASS và người có thẩm quyền duyệt quy tắc thẩm quyền, comparability và conflict escalation.

## Điều kiện đóng D10

1. Chạy 12 prompt trên baseline v1.0 và v2.3 cùng model/cấu hình, với bộ nguồn thật đã khử nhận dạng và decision question có ground truth/reviewer.
2. Đo trigger precision, false-ask rate, source coverage, claim traceability, comparability classification, dependency detection, conflict preservation và unsupported conclusion; luôn ghi tử số/mẫu số.
3. Lưu input, output, evidence, `total_tokens`, `duration_ms`; chạy pass^3 cho package phục vụ quyết định.
4. Sửa systematic error, chạy lại phạm vi bị ảnh hưởng và lưu regression evidence trước khi đề nghị OFFICIAL.

