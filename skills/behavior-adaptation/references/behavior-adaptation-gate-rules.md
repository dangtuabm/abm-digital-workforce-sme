# BEHAVIOR ADAPTATION GATE RULES

## 1. Mô hình trạng thái

| State | Điều kiện |
|---|---|
| `NOT_READY` | Thiếu purpose/context/evidence/consent/non-negotiable hoặc có prohibited use/conflict |
| `OBSERVATION_READY` | Ledger có nhưng hypotheses/playbook/trial chưa đủ |
| `PLAYBOOK_READY` | Có playbook nhưng trace/fairness/trial design gap còn mở |
| `READY_FOR_CONSENTED_TRIAL` | Trace, alternatives, playbook và safe trial đủ; tests đã lập |
| `VALIDATED_FOR_OWNER_REVIEW` | Trial/response tests thật đạt; required reviews hoàn tất |
| `APPROVED_FOR_OPERATION` | Chỉ người có thẩm quyền cấp; engine không tự cấp |

## 2. Observation và context

Observation hợp lệ ghi `id · exact excerpt/behavior · source/date · role/context/channel · dimension · counterexample · quality · authorized status`. Không gọi adjective về người là observation. “Trả lời ba câu trong hai dòng tại email này” là observation; “thiếu kiên nhẫn” là interpretation.

Dimensions có thể dùng: `pace_latency`, `detail_structure`, `task_people_focus`, `autonomy_control`, `risk_uncertainty`, `decision_style`, `channel_feedback`. Chúng mô tả interaction, không xếp hạng con người.

## 3. Hypothesis, confidence và DISC

Hypothesis ghi `id · text · observation refs · alternatives · context/scope · confidence · expiry/review · falsifier · next evidence · status`.

- `low`: một/ít signal, context hẹp hoặc alternatives mạnh.
- `medium`: pattern lặp trong cùng context, có counterexample review.
- `high`: nhiều signal độc lập qua thời gian/context đã xác định; vẫn không thành identity.

DISC chỉ là optional shorthand cho pattern quan sát. Phải ghi context/confidence và ít nhất hai dimensions có evidence. Cấm bird label, “người này là D/I/S/C”, deep fear/motivation, clinical inference hoặc dùng cho employment/high-stakes decisions.

## 4. Safe fallback và mode levers

Mọi playbook có fallback: mục tiêu rõ, information chunk nhỏ, evidence/assumption tách, quyền hỏi/từ chối, action/owner/deadline, comprehension check và respectful tone.

| Mode | Lever được thử |
|---|---|
| `presentation` | conclusion-first vs context-first, detail layer, pause/question, visual/evidence |
| `delegation` | outcome vs steps, autonomy range, acceptance criteria, written recap |
| `feedback` | timing, specific behavior-impact-request, private/live vs written follow-up |
| `coaching` | question breadth, reflection time, example, choice of next action |
| `negotiation` | options, evidence order, pace, issue sequencing, recap/check |
| `objection` | acknowledge, clarify, evidence, testable next step, escalation |

Levers không được đổi fact, standard, consequence, fairness, authority, consent hay legal/HR rights.

## 5. Trial design

Một trial ưu tiên một lever và ghi `baseline · adaptation · prediction · metric/threshold · sample/window · risk · consent · owner · stop · rollback · status`. Không thử covert, không gây bất lợi, không dùng dark pattern, artificial urgency hoặc asymmetric information.

Kết quả “không hiệu quả” là evidence hợp lệ. Update phải có response, counterevidence và quyết định `retain|revise|reject`; không chỉ ghi success story.

## 6. Privacy, fairness và retention

- Dùng pseudonym khi có thể; thu ít nhất; chỉ đúng purpose/consent; access log và expiry.
- Cấm sensitive/protected trait inference, surveillance, hidden scoring, retaliation và unequal performance/quality standard.
- Không dùng response latency ngoài giờ, disability/accessibility behavior, language proficiency hoặc cultural style như proxy năng lực/commitment.
- Người tương tác có quyền biết purpose phù hợp, hỏi, sửa và dừng trial theo policy.

## 7. Bảy test bắt buộc

| Type | Pass khi |
|---|---|
| `observation_trace` | Mọi hypothesis truy exact behavior/source/context; không adjective giả observation |
| `hypothesis_humility` | Có alternatives, confidence, falsifier, expiry và counterevidence route |
| `interaction_fit` | Người tương tác hiểu/tiếp nhận format tốt hơn theo metric đã duyệt |
| `outcome_action_accuracy` | Outcome/action/standard/authority không drift |
| `dignity_nonmanipulation` | Không coercion, deception, stereotype, sensitive inference hay loss of autonomy |
| `accessibility_channel` | Channel/pace/detail/format usable, có safe fallback |
| `update_transfer_boundary` | Kết quả update đúng context; không overgeneralize hoặc giữ profile quá hạn |

Mỗi test ghi artifact/version, method, sample/reviewer, threshold, status/evidence. High-stakes context bị out-of-scope; external/reputational trial cần `pass^3` theo ABM-SQS.

## 8. Gate bàn giao

- Contract, Ledger, Hypotheses, Map, Playbooks, Trials, Response/Test Log cùng version/hash.
- Không prohibited use, untraced inference, expired consent, sensitive trait, unequal standard hoặc trial defect mở.
- Required privacy/HR/legal/accessibility reviews hoàn tất theo risk.
- Human chạy interaction; A.I không giả response/outcome. Material change phải rerun affected tests.
- Operational approval chỉ do người có thẩm quyền cấp.
