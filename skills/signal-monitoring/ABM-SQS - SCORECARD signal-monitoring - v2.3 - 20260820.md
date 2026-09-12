---
title: "ABM-SQS Static Pre-score — signal-monitoring"
skill_id: "08"
version: "2.3"
date: "2026-08-20"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `signal-monitoring` v2.3

## Kết luận

**Kết quả kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa có baseline execution; Skill là `draft / static-pass`, chưa được tự động gửi alert hoặc kích hoạt response.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description | 590 ký tự — đạt ngưỡng ≤ 600 |
| Thân `SKILL.md` | 7.881 ký tự — đạt vùng an toàn ≤ 8.000 |
| Tổng dòng | 143 — đạt ngưỡng ≤ 500 |
| Từ viết sai "A.I" | 0 |
| Eval đã thiết kế | 12 |
| Validator ABM | PASS, 0 error |
| Validator SKILL-CREATOR | `Skill is valid!` với Python UTF-8 |
| SHA-256 `SKILL.md` | `E1636D39FD5203E397ED783076655C37BB001DC96053F36D7120F295F9BF0969` |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Signal Register là đầu ra trung gian; có detection protocol, severity rubric và templates |
| A2 | PASS | Brain First ↔ B1–2; Phân tích Hệ thống ↔ B3–5; SPC ↔ B4; Audit Trail/Bốn Mắt ↔ B5–8 |
| A3 | PASS | 0 lỗi "A.I"; bảng Người quyết định/A.I thực thi; không emoji/sáo ngữ |
| B4 | PASS | Một Signal Watch Cycle Package; đủ bốn khai báo; tách monitoring khỏi research, root-cause, portfolio và synthesis |
| B5 | PASS | Name hợp lệ; description 590; body 7.881; 143 dòng; references sâu một tầng |
| B6 | PASS | Trigger/anti-trigger rõ; đầu vào 4 cột; artifact và Definition of Done đo coverage/traceability/escalation |
| C7 | PASS | Baseline, seasonality, dependency, confirmation, hysteresis, confidence và nhãn DỮ KIỆN/SUY LUẬN/GIẢ ĐỊNH |
| C8 | PASS | Red Lines hai chiều; dừng trước access/buy/scope/rule/send/response; tự chạy local cycle theo contract |
| C9 | PASS | Không thi hành instruction trong source/feed/link; tối thiểu hóa; không giám sát thuộc tính nhạy cảm ngoài mục đích |
| D10 | NOT PASS | 12 eval đã thiết kế nhưng `status = not_run`; chưa baseline/evidence/token/duration/pass^3 |
| D11 | PASS | Frontmatter/metadata đủ; name trùng thư mục; có Phiên bản và Thay đổi |
| D12 | PASS | Asset Candidate có Source Task, indicator/source version, evidence, owner, approval và điều kiện rà |

## Audit trail phiên bản

- **v2.2:** static gate trượt: description 641, body 8.484.
- **v2.3:** rút phần lặp, giữ controls; hai validator PASS.

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT:** REJECT vì D10 bắt buộc chưa đạt.
- **OFFICIAL / PRODUCTION USE:** REJECT đến khi D10 PASS, có watch cycle thật và owner nghiệp vụ duyệt baseline, threshold, severity cùng escalation matrix.

## Điều kiện đóng D10

1. Chạy 12 prompt trên baseline v1.0 và v2.3 cùng model/cấu hình, với 10 cycle thật đã khử nhận dạng và reviewer-labeled signals.
2. Đo trigger precision, false ask, source/indicator coverage, detection precision/recall, rumor/dependency handling, false-positive/negative, alert flapping, owner/SLA completeness và escalation correctness; ghi tử số/mẫu số.
3. Lưu input, output, evidence, `total_tokens`, `duration_ms`; chạy pass^3 cho cycle có escalation.
4. Sửa systematic error và lưu regression evidence trước khi đề nghị OFFICIAL.

