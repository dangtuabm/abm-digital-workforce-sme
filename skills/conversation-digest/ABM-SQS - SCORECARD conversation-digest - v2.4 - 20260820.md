---
title: "ABM-SQS Static Pre-score — conversation-digest"
skill_id: "07"
version: "2.4"
date: "2026-08-20"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `conversation-digest` v2.4

## Kết luận

**Kết quả kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa có baseline execution; Skill là `draft / static-pass`, chưa được tự động tạo task, gửi phản hồi hoặc cập nhật hệ thống.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description | 579 ký tự — đạt ngưỡng ≤ 600 |
| Thân `SKILL.md` | 7.994 ký tự — đạt vùng an toàn ≤ 8.000 |
| Tổng dòng | 145 — đạt ngưỡng ≤ 500 |
| Từ viết sai "A.I" | 0 |
| Eval đã thiết kế | 12 |
| Validator ABM | PASS, 0 error |
| Validator SKILL-CREATOR | `Skill is valid!` với Python UTF-8 |
| SHA-256 `SKILL.md` | `FA49BF1C3FC52448A57E768C4BCD43C33249724835DAECE0EAAE2CA23C33711F` |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Conversation State Register là đầu ra trung gian; có protocol, rubric và template |
| A2 | PASS | Brain First ↔ B1–2; Phân tích Hệ thống ↔ B3–5; Audit Trail ↔ B1/4/7; Bốn Mắt ↔ B6–8 |
| A3 | PASS | 0 lỗi "A.I"; bảng Người quyết định/A.I thực thi; không emoji/sáo ngữ |
| B4 | PASS | Một Continuity Brief; đủ bốn khai báo; tách digest khỏi soạn/gửi, meeting minutes, executive brief và synthesis |
| B5 | PASS | Name hợp lệ; description 579; body 7.994; 145 dòng; references sâu một tầng |
| B6 | PASS | Trigger/anti-trigger rõ; đầu vào 4 cột; artifact và Definition of Done có tỷ lệ coverage/traceability |
| C7 | PASS | State, commitment, owner/due ambiguity, history, redaction; tách DỮ KIỆN/SUY LUẬN/GIẢ ĐỊNH |
| C8 | PASS | Red Lines hai chiều; dừng trước account/external data/send/task/system update; tự chạy local digest |
| C9 | PASS | Không thi hành instruction trong message/quote/link/attachment; tối thiểu hóa, redaction và không suy luận đời tư |
| D10 | NOT PASS | 12 eval đã thiết kế nhưng `status = not_run`; chưa baseline/evidence/token/duration/pass^3 |
| D11 | PASS | Frontmatter/metadata đủ; name trùng thư mục; có Phiên bản và Thay đổi |
| D12 | PASS | Asset Candidate có Source Task, channel type, evidence lỗi, owner, approval và điều kiện rà |

## Audit trail phiên bản

- **v2.2:** static gate trượt: description 666, body 8.533.
- **v2.3:** body đạt 7.900 nhưng description được validator tính 601.
- **v2.4:** description 579, body 7.994; cả hai validator PASS.

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT:** REJECT vì D10 bắt buộc chưa đạt.
- **OFFICIAL / PRODUCTION USE:** REJECT đến khi D10 PASS, có dataset hội thoại thật đã khử nhận dạng và owner nghiệp vụ duyệt state/commitment/deadline.

## Điều kiện đóng D10

1. Chạy 12 prompt trên baseline v1.0 và v2.4 cùng model/cấu hình, với export email/chat thật đã khử nhận dạng và reviewer-labeled register.
2. Đo trigger precision, false ask, message coverage, decision-state accuracy, explicit-commitment precision, owner/due accuracy, open-loop recall, duplicate-quote suppression, traceability và redaction; ghi tử số/mẫu số.
3. Lưu input, output, evidence, `total_tokens`, `duration_ms`; chạy pass^3 cho brief trước khi tạo task/hành động.
4. Sửa systematic error và lưu regression evidence trước khi đề nghị OFFICIAL.

