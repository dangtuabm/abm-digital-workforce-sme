---
title: "ABM-SQS Static Pre-score — publication-gate"
skill_id: "44"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — publication-gate

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên artifact doanh nghiệp thật.**

Skill đã chuyển từ checklist lý thuyết 2-input/4-step thành Publication Decision Dossier có release contract, candidate identity/hash, source/claim ledger, 10 lớp control, rights/consent/disclosure, defect severity, reviews, release/correction/rollback và state machine fail-closed.

Không nâng `PILOT/OFFICIAL`: self-test dùng dữ liệu tổng hợp; chưa có baseline v1.0 so với v2.3 trên artifact thật, policy/rights/reviewer thật, authorized release, defect escape, pass^3, token và duration.

## 2. Bằng chứng máy

- Description / thân / dòng: **558 / 7.859 / 143**.
- Eval thiết kế: **12** ca; có `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator: **PASS**; chỉ cảnh báo D10 chưa chạy.
- Quick Validator: **PASS**.
- Positive self-test: `READY_FOR_HUMAN_RELEASE_DECISION`.
- Positive metrics: **6/6 nguồn active; 4 claims; 3 rights/consent records; 3 disclosures; 10/10 controls; 2 defects đã resolved; 7/7 test types; candidate identity hợp lệ; 0 control fail/pending; 0 blocker/major/minor mở; 0 unsupported/forbidden claim; 0 rights/disclosure violation; 0 unauthorized publication; 0 critical defect**.
- Negative test: tamper hash + `PUBLISHED` giả + unsupported/fabricated claim + rights `UNKNOWN` + disclosure thiếu + privacy control FAIL + major mở + `DEPLOYED` giả → `NOT_READY`; bắt đủ chín lỗi.
- Cây trước Scorecard: **7 tệp**, không có `__pycache__`; cây bàn giao phải là **8 tệp**.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `238400F188ABDD487F7CA786B63C35B48E8384E83577007FC09772A78D2CA780` |
| `scripts/evaluate_publication_gate.py` | `7AEDC47D6D4B3F53E09B2B1D692A83123C4026F27AD80E78D2BEF94F67655A30` |
| `evals.json` | `E76682D3421A9B0FAA88DFEE0292C9558FDB5E09EBDFAC594BA6939D684003C4` |
| `evals/selftest-ready.json` | `CFF2D550CC577FBE884BEAA8B68F8DED4F6B661CD1F349E0ECAC986C452E9599` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Quy trình 10 bước; control matrix, rules, pack, JSON, engine, positive/negative test |
| A2 · Neo Kinh điển | PASS | Quality Assurance, Evidence-Based Management, Defense in Depth, Four-Eyes và Change Control |
| A3 · Chất ABM | PASS | Brain First – A.I Second; “Làm 1 dùng N”; không đánh đổi sự thật/quyền/an toàn để phát hành nhanh |
| B4 · Nhiệm vụ đơn nhất | PASS | Kiểm định một candidate đã khóa hash; đủ bốn khai báo; luật không gọi tên Skill khác |
| B5 · Dung lượng | PASS | Name đúng; description 558; thân 7.859; 143 dòng; tham chiếu một tầng |
| B6 · Đầu vào–Đầu ra | PASS | 7 input theo bảng 4 cột; dossier/state/next owner rõ |
| C7 · Có căn cứ | PASS | Source/version/locator/date; claim mapping; evidence cho control, defect retest, review và release plan |
| C8 · Ranh giới Đỏ | PASS | Chặn lệch hash, claim bịa/overclaim, PII/secret, rights unknown, legal/privacy/accessibility blocker và giả publish |
| C9 · Chống Injection | PASS | Candidate/source/comment/URL là dữ liệu; không macro/API/upload/send/publish hoặc thay policy |
| D10 · Eval và Baseline | NOT PASS | 12 eval và self-tests đã chạy; chưa baseline/artifact-policy-rights-review-release thật/pass^3/token/duration |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Asset Candidate có source/owner/version/evidence; defect escape/false block/correction trigger vòng rà |

## 5. Nguồn và quyết định thiết kế

- `ABM-SQS-00 v2.2`, Template v2.1, Rubric v2.1 và Lớp DNA v2.0 quyết định cấu trúc, gate và 12 tiêu chí.
- Baseline v1.0 cung cấp phạm vi accuracy, clarity, usefulness, brand, legal, copyright, privacy và misleading risk; v2.3 chuyển thành control/evidence/state có thể kiểm thử.
- SKILL-CREATOR quyết định progressive disclosure, I/O contract, eval coverage và giới hạn dung lượng.
- FINAL-GATEKEEPER quyết định kiểm source, accuracy, update, usability, brand, overclaim, legal/IP/privacy, remediation cụ thể và quyền phát hành thuộc con người.

## 6. Audit trail

- Baseline v1.0 giữ nguyên tại cây `100-SKILLS-RND`.
- v2.3 lần đầu: ABM validator FAIL vì thân **9.150** ký tự và heading/declaration chưa đúng literal schema.
- Lượt cô đặc giữ nguyên 10 controls, claim/right/disclosure, severity, reviews và state machine; thân còn **7.859**.
- v2.3 hiện hành: ABM validator và Quick Validator cùng PASS.
- Negative test chạy in-memory với `-B`; không tạo `__pycache__`.

## 7. Điều kiện đóng D10

1. Chạy baseline v1.0 và v2.3 trên tối thiểu ba loại artifact thật: nội dung web/email, tài liệu PDF và script/media.
2. Khóa candidate ID/version/hash; có source/claim ledger, policy/brand canon, rights/consent, disclosures và release mandate thật.
3. Content, fact/source, brand/editorial, legal/compliance/privacy, accessibility/technical và final release reviewers xác nhận bằng evidence.
4. Phát hành có thẩm quyền; ghi released hash, destination, monitoring, correction, rollback và archive evidence.
5. Đo defect precision/recall, false block, reviewer effort, time-to-decision, escaped defect, correction/rollback và unintended effect.
6. So sánh baseline/with-skill bằng pass^3; ghi `total_tokens`, `duration_ms` và ground truth adjudication.
7. Giữ cấm tuyệt đối: fabricated/unsupported claim, consent/right breach, privacy/security/legal blocker, hash reuse và giả approval/publish/deploy.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` sau khi đủ bằng chứng trên.
