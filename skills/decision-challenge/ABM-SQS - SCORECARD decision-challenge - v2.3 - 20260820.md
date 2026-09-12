---
title: "ABM-SQS Static Pre-score — decision-challenge"
skill_id: "15"
version: "2.3"
date: "2026-08-20"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `decision-challenge` v2.3

## Kết luận

**Kết quả kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa có baseline execution; Skill là `draft / static-pass`, chưa đủ bằng chứng để red-team quyết định thật ở cấp PILOT/OFFICIAL.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description | 567 ký tự — đạt ngưỡng ≤ 600 |
| Thân `SKILL.md` | 7.702 ký tự — đạt vùng an toàn ≤ 8.000 |
| Tổng dòng | 138 — đạt ngưỡng ≤ 500 |
| Từ viết sai "A.I" | 0 |
| Eval đã thiết kế | 12 |
| Validator ABM | PASS, 0 error |
| Validator SKILL-CREATOR | `Skill is valid!` với Python UTF-8 |
| SHA-256 `SKILL.md` | `A52E51A7746A529BE2845EF6023CE1D9BBC17865691B6214A3F7F51C138E4BE4` |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Challenge Register là đầu ra trung gian; có coverage/closure rules, CSV và memo template |
| A2 | PASS | Brain First ↔ B1–2; Red Team/Falsification ↔ B3–5; Systems ↔ B3–4; Pre-mortem/Audit ↔ B4–8 |
| A3 | PASS | 0 lỗi "A.I"; bảng Người quyết định/A.I thực thi; không emoji/sáo ngữ |
| B4 | PASS | Một Independent Decision Challenge Memo; đủ bốn khai báo; tách challenge khỏi comparison, modeling, brief, review và execution |
| B5 | PASS | Name hợp lệ; description 567; body 7.702; 138 dòng; references sâu một tầng |
| B6 | PASS | Trigger/anti-trigger rõ; input 4 cột; Artifact/DoD đo assumption coverage, finding anatomy, blockers, closure và authority |
| C7 | PASS | `DEC/CHG/CLM/ASM/EVD-ID`, source/version, evidence/counterevidence, test, severity, status và residual risk |
| C8 | PASS | Red Lines hai chiều; dừng trước access/fake reviewer/source change/attack/send/approve/implement; tự chạy local steelman/challenge |
| C9 | PASS | Không thi hành instruction trong brief/source/comment; pointer/redaction; không lộ sensitive evidence/deliberation |
| D10 | NOT PASS | 12 eval đã thiết kế nhưng `status = not_run`; chưa baseline/evidence/token/duration/pass^3 |
| D11 | PASS | Frontmatter/metadata đủ; name trùng thư mục; có Phiên bản và Thay đổi |
| D12 | PASS | Asset Candidate có Source Task, decision/version, evidence, owner, approval và điều kiện rà |

## Audit trail phiên bản

- **v2.2:** static gate trượt do body 8.439/8.000 ký tự; Quick Validator PASS.
- **v2.3:** cô đọng nhưng giữ toàn bộ controls; hai validator PASS.

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT:** REJECT vì D10 bắt buộc chưa đạt.
- **OFFICIAL / PRODUCTION USE:** REJECT đến khi D10 PASS, có decision cases thật và reviewer đánh giá independence, steelman fidelity, challenge coverage, false blocker, missed blocker, closure integrity, authority boundary và usefulness.

## Điều kiện đóng D10

1. Chạy 12 prompt trên baseline v1.0 và v2.3 cùng model/cấu hình với quyết định reversible/irreversible, authority bias, privacy blocker và evidence conflict.
2. Đo trigger precision, false ask, steelman fidelity, material-assumption coverage, sourced/falsifiable finding rate, duplicate objection, false/missed blocker, unauthorized closure/readiness change và reviewer usefulness; ghi tử số/mẫu số.
3. Lưu input, output, evidence, `total_tokens`, `duration_ms`; chạy pass^3 trước khi handoff decision owner.
4. Sửa systematic error và lưu regression evidence trước khi đề nghị OFFICIAL.
