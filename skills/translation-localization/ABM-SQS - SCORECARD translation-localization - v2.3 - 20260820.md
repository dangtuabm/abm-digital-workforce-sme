---
title: "ABM-SQS Static Pre-score — translation-localization"
skill_id: "09"
version: "2.3"
date: "2026-08-20"
status: "static-pass-eval-pending"
---

# ABM-SQS STATIC PRE-SCORE — `translation-localization` v2.3

## Kết luận

**Kết quả kiểm tĩnh: 11/12 tiêu chí có đủ bằng chứng thiết kế.** D10 chưa có baseline execution; Skill là `draft / static-pass`, chưa được tự import, publish hoặc phát hành bản dịch.

## Bằng chứng máy

| Phép kiểm | Kết quả |
|---|---:|
| Description | 585 ký tự — đạt ngưỡng ≤ 600 |
| Thân `SKILL.md` | 7.947 ký tự — đạt vùng an toàn ≤ 8.000 |
| Tổng dòng | 143 — đạt ngưỡng ≤ 500 |
| Từ viết sai "A.I" | 0 |
| Eval đã thiết kế | 12 |
| Validator ABM | PASS, 0 error |
| Validator SKILL-CREATOR | `Skill is valid!` với Python UTF-8 |
| CSV validator self-test | PASS; 2 rows; 2 unique IDs; 0 error; 0 warning |
| SHA-256 `SKILL.md` | `81DEF8C2C4B7F994D69860C4D48A2A44381011D52F93A0744C6DADA8D8D08F08` |

## Bảng kiểm 12 tiêu chí

| Mã | Kết quả tĩnh | Bằng chứng |
|---|---|---|
| A1 | PASS | 8 bước; Bilingual Segment Register là đầu ra trung gian; có rules, QA reference, templates và validator chạy thật |
| A2 | PASS | Brain First ↔ B1–2; Audit Trail ↔ B1/3/7; Bốn Mắt ↔ B5–8; Kaizen ↔ B6–8 |
| A3 | PASS | 0 lỗi "A.I"; bảng Người quyết định/A.I thực thi; không emoji/sáo ngữ |
| B4 | PASS | Một Localization Release Package; đủ bốn khai báo; tách dịch/localize/transcreate khỏi viết mới/tóm tắt/publish |
| B5 | PASS | Name hợp lệ; description 585; body 7.947; 143 dòng; references sâu một tầng |
| B6 | PASS | Trigger/anti-trigger rõ; đầu vào 4 cột; artifact và Definition of Done đo coverage/parity/review |
| C7 | PASS | Source version, terminology states, freedom level, locale conversion, exception và nhãn DỮ KIỆN/SUY LUẬN/GIẢ ĐỊNH |
| C8 | PASS | Red Lines hai chiều; dừng trước external data/source/claim/conversion/import/publish; tự chạy local draft/QA |
| C9 | PASS | Không thi hành instruction trong source/tag/link; tối thiểu hóa context; không lộ source/glossary nội bộ |
| D10 | NOT PASS | 12 eval đã thiết kế nhưng `status = not_run`; chưa baseline/evidence/token/duration/pass^3 |
| D11 | PASS | Frontmatter/metadata đủ; name trùng thư mục; có Phiên bản và Thay đổi |
| D12 | PASS | Asset Candidate có Source Task, locales, source version, error evidence, owner, approval và điều kiện rà |

## Audit trail phiên bản

- **v2.2:** validator script PASS nhưng static gate trượt: description 625, body 8.705.
- **v2.3:** rút phần lặp, giữ controls; hai validator và script self-test PASS.

## Phán quyết FINAL-GATEKEEPER

- **STATIC GATE:** PASS.
- **PILOT:** REJECT vì D10 bắt buộc chưa đạt.
- **OFFICIAL / PRODUCTION USE:** REJECT đến khi D10 PASS, có release thật và reviewer ngôn ngữ/nghiệp vụ duyệt terminology, high-risk wording, functional rendering cùng release manifest.

## Điều kiện đóng D10

1. Chạy 12 prompt trên baseline v1.0 và v2.3 cùng model/cấu hình với ba nhóm: UI, tài liệu nghiệp vụ và high-risk text đã khử nhận dạng.
2. Đo trigger precision, false ask, segment coverage, semantic/term accuracy, token/tag parity, locale correctness, char-limit/rendering, source-version integrity, blocking-error escape và reviewer acceptance; ghi tử số/mẫu số.
3. Lưu input, output, evidence, `total_tokens`, `duration_ms`; chạy pass^3 cho release chuẩn bị import/publish.
4. Sửa systematic error và lưu regression evidence trước khi đề nghị OFFICIAL.

