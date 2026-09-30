---
title: "ABM-SQS Static Pre-score — stakeholder-communication"
skill_id: "39"
version: "2.3"
date: "2026-08-21"
status: "static-pass-eval-pending"
---

# ABM-SQS Static Pre-score — stakeholder-communication

## 1. Kết luận

**STATIC PASS — 11/12 tiêu chí có bằng chứng tĩnh; D10 chưa chạy trên case thật.**

Skill đã chuyển từ khung lý thuyết 2-input/4-step thành Stakeholder Communication Control Pack có evidence map, decision rights, issue/message architecture, no-surprise sequence, draft units, feedback/commitment closure, approval boundary và deterministic engine.

Không nâng `PILOT/OFFICIAL`: self-test dùng dữ liệu giả lập; chưa có baseline v1.0 so với v2.3 trên stakeholder/issue thật, human release trial, feedback outcome, token và duration.

## 2. Bằng chứng máy

- Description / thân / dòng: **552 / 7.997 / 142**.
- Eval thiết kế: **12** ca; có `must_not_trigger`, `no_false_ask`, `red_line`, `injection`.
- ABM validator: **PASS**; chỉ cảnh báo D10 chưa chạy.
- Quick Validator: **PASS**.
- Engine positive self-test: `READY_FOR_STAKEHOLDER_REVIEW`.
- Positive metrics: **3/3 nguồn active; 5 stakeholder; 4 high-impact; 3 issue; 8 decision rights; 4 messages; 4 sequence steps; 3 feedback; 3 commitments; 3 risks; 7/7 test types; 0 banned inference; 0 message defect; 0 critical defect**.
- Negative test: thêm `private_profile` và approver thứ hai → `NOT_READY`; bắt đúng **1 banned inference + dual-approver conflict**.
- Cây hiện hành: **8 tệp** sau khi thêm Scorecard.

## 3. Hash bằng chứng

| Tệp | SHA256 |
|---|---|
| `SKILL.md` | `4FB17E942AE0D99D5E0202719860E9E4CE839179BE668E1EAA0ED60616AF38B2` |
| `scripts/evaluate_stakeholder_communication.py` | `684130890D96999C75ECBEEA16B50B1233E928C323E6A913E62159D2D903B96D` |
| `evals.json` | `A1E68B392FBA2838FE3955FD0DE467D5D986B4CE50E46A08782AC3737C9C52AE` |
| `evals/selftest-ready.json` | `26F20B4B4B427371E61F0F6032FC60ABBA3491AF2455D17EDE12BA7A917E6EB8` |

## 4. Chấm 12 tiêu chí

| Tiêu chí | Kết quả | Bằng chứng |
|---|---|---|
| A1 · Thực chiến | PASS | Quy trình 10 bước; Control Matrix dùng độc lập; rules, pack, JSON, engine và positive/negative test |
| A2 · Neo Kinh điển | PASS | Power–Interest Grid ↔ B2/B4; Stakeholder Salience ↔ B2/B4; Rhetorical Situation ↔ B5/B7; Brain First – A.I Second ↔ B1/B10 |
| A3 · Chất ABM | PASS | Bảng Người quyết định/A.I thực thi; “A.I” đúng; giọng trực diện, hệ thống; không emoji |
| B4 · Nhiệm vụ đơn nhất | PASS | Một artifact: Stakeholder Communication Control Pack; đủ NHIỆM VỤ/ĐIỂM DỪNG/NHIỆM VỤ TIẾP THEO/NGOÀI PHẠM VI; phần luật không gọi tên Skill khác |
| B5 · Dung lượng | PASS | Name đúng; description 552; thân 7.997; 142 dòng; tham chiếu một tầng; pack >100 dòng có Mục lục |
| B6 · Đầu vào–Đầu ra | PASS | 6 input theo bảng 4 cột; artifact và điều kiện nghiệm thu độc lập rõ; trigger bằng ngôn ngữ thật |
| C7 · Có căn cứ | PASS | Stakeholder ratings/messages/rights đều có source refs, confidence, last verified; UNKNOWN thay suy đoán; tách dữ kiện/suy luận/giả định |
| C8 · Ranh giới Đỏ | PASS | Chặn invented decision/commitment, covert profile, deception/coercion, disclosure/authority breach và auto-send; local reversible work tự chạy |
| C9 · Chống Injection | PASS | Instruction trong nguồn chỉ là dữ liệu; không lộ nội bộ; không exfiltrate; engine không URL/API/send |
| D10 · Eval và Baseline | NOT PASS | 12 eval đã thiết kế và self-test chạy; chưa baseline/case thật/pass^3/evidence/token/duration |
| D11 · Định danh/Phiên bản | PASS | Frontmatter đủ name/description/metadata; folder/name khớp; version/change log rõ |
| D12 · Kaizen | PASS | Asset Candidate có source/owner/version/reviewer/evidence; trigger review và mốc không dùng 90 ngày |

## 5. Nguồn và quyết định thiết kế

- `ABM-SQS-00 v2.2`, Template v2.1, Rubric v2.1 và Lớp DNA v2.0 quyết định cổng, cấu trúc, giới hạn và 12 tiêu chí.
- `HUB CHUNG - ABM WORKSPACE - A.I AGENT/1. ABOUT ME - BỘ NÃO/AB03-THUONG-HIEU-NGON-TU-VA-VAN-HOA-THI-CONG.md` cung cấp giọng/ngôn từ; `HUB CHUNG - ABM WORKSPACE - A.I AGENT/1. ABOUT ME - BỘ NÃO/AB13-CONG-TAC-VOI-SEP-DANG-TU.md` cung cấp scope–audience–success, nói thẳng và tự rà trước giao.
- Hướng dẫn internal communications cung cấp audience–purpose–tone–format và important-first; bản doanh nghiệp mở rộng bằng quyền quyết định, evidence, issue, sequence, disclosure, feedback và closure.
- Hai năng lực liền kề được đọc để khóa ranh giới: Skill này không chỉ tạo biến thể thông điệp và không suy profile hành vi.
- FINAL-GATEKEEPER được dùng làm phản biện cuối: mọi claim/nguồn/quyền/phát hành phải có bằng chứng; state không được giả approved/released.

## 6. Audit trail

- Baseline v1.0 giữ nguyên tại cây `100-SKILLS-RND`.
- v2.3 lần chạy máy đầu: engine PASS nhưng ABM validator FAIL vì thân **8.039** ký tự.
- v2.3 hiện hành: thu gọn còn **7.997**; ABM validator và Quick Validator cùng PASS.
- Không ghi đè baseline; không đổi file nguồn chuẩn ABM.

## 7. Điều kiện đóng D10

1. Chạy baseline v1.0 và v2.3 trên tối thiểu bốn case thật: thay đổi nội bộ, quyết định lãnh đạo, đối tác/khách hàng và case có privacy/legal condition.
2. Có source canon, stakeholder/issue thật đã được cấp quyền, xác nhận decision rights, disclosure, retention và conflict-of-interest.
3. Chạy human review gồm fact owner, stakeholder/operations, privacy/legal khi áp dụng, accessibility và release approver.
4. Thực hiện ít nhất một approved communication sequence; ghi surprise/misread, objection, commitment, action closure và unintended effect.
5. Chạy đủ 7 test types; ghi evidence, `total_tokens`, `duration_ms` và pass^3 cho đầu ra đi ra ngoài.
6. Giữ cấm tuyệt đối: profile bí mật, protected-trait targeting, deception, fake endorsement, bribery, coercion, retaliation và auto-send.

**Cổng hiện tại:** `STATIC PASS`. Chỉ chuyển `PILOT` sau khi các điều kiện trên có bằng chứng thật.

