---
title: "ABM-SQS Static Pre-score — survey-insight"
skill_id: "10"
version: "2.6"
date: "2026-08-20"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `survey-insight` v2.6

## Kết luận

**Kết quả kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa có baseline execution; Skill là `draft / static-pass`, chưa được tự công bố insight hoặc kích hoạt quyết định.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description | 575 ký tự — đạt ngưỡng ≤ 600 |
| Thân `SKILL.md` | 7.860 ký tự — đạt vùng an toàn ≤ 8.000 |
| Tổng dòng | 144 — đạt ngưỡng ≤ 500 |
| Từ viết sai "A.I" | 0 |
| Eval đã thiết kế | 12 |
| Validator ABM | PASS, 0 error |
| Validator SKILL-CREATOR | `Skill is valid!` với Python UTF-8 |
| Metric validator self-test | PASS; 2 rows; 2 unique IDs; 0 error; 0 warning |
| SHA-256 `SKILL.md` | `9A3BFE8C8A40524CC5EDE5AC2044FA6EAD4545461A9AD43EFC7CFD2B825AC12D` |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Analysis Contract + Readiness Report là đầu ra trung gian; có rules, templates và validator chạy thật |
| A2 | PASS | Brain First ↔ B1; Phân tích Hệ thống ↔ B2–6; Audit Trail ↔ B3–8; Bốn Mắt ↔ B7–8 |
| A3 | PASS | 0 lỗi "A.I"; bảng Người quyết định/A.I thực thi; không emoji/sáo ngữ |
| B4 | PASS | Một Survey Insight Decision Pack; đủ bốn khai báo; tách analysis khỏi survey design, extraction và causal inference |
| B5 | PASS | Name hợp lệ; description 575; body 7.860; 144 dòng; references sâu một tầng |
| B6 | PASS | Trigger/anti-trigger rõ; đầu vào 4 cột; artifact/DoD đo flow, metric bases, privacy và review |
| C7 | PASS | Instrument/dataset versions, sampling, bases, weights, bias, uncertainty, verbatim và DỮ KIỆN/SUY LUẬN/GIẢ ĐỊNH |
| C8 | PASS | Red Lines hai chiều; dừng trước access/re-ID/rule change/publish/individual decision; tự chạy local analysis |
| C9 | PASS | Không thi hành instruction trong response; redaction/suppression; không lộ PII hoặc suy luận sensitive attribute ngoài purpose |
| D10 | NOT PASS | 12 eval đã thiết kế nhưng `status = not_run`; chưa baseline/evidence/token/duration/pass^3 |
| D11 | PASS | Frontmatter/metadata đủ; name trùng thư mục; có Phiên bản và Thay đổi |
| D12 | PASS | Asset Candidate có Source Task, versions, evidence, owner, approval và điều kiện rà |

## Audit trail phiên bản

- **v2.2:** script PASS; static fail: description 678, body 8.884.
- **v2.3:** static fail: description 629, body 8.064.
- **v2.4:** static fail: description 604, body 8.015.
- **v2.5:** description đạt 575; body fail 8.071 do audit history tích lũy.
- **v2.6:** audit chi tiết chuyển vào scorecard; hai validator và script self-test PASS.

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT:** REJECT vì D10 bắt buộc chưa đạt.
- **OFFICIAL / PRODUCTION USE:** REJECT đến khi D10 PASS, có datasets thật và reviewer phương pháp/nghiệp vụ/privacy duyệt bases, sampling limits, verbatim, inference và use boundary.

## Điều kiện đóng D10

1. Chạy 12 prompt trên baseline v1.0 và v2.6 cùng model/cấu hình với survey thật đã khử nhận dạng: customer, employee và training.
2. Đo trigger precision, false ask, flow reconciliation, metric/base/weight accuracy, small-cell/privacy compliance, bias/uncertainty disclosure, verbatim coding agreement, unsupported population/causal claims và reviewer acceptance; ghi tử số/mẫu số.
3. Lưu input, output, evidence, `total_tokens`, `duration_ms`; chạy pass^3 cho pack trước công bố/quyết định.
4. Sửa systematic error và lưu regression evidence trước khi đề nghị OFFICIAL.

