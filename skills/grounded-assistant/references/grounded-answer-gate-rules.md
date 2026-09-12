# GROUNDED ANSWER GATE RULES

## 1. Answerability decisions

- `ANSWER`: mọi material claim đủ evidence active/current và đúng role.
- `PARTIAL`: phần có evidence được trả; phần thiếu ghi rõ và không suy đoán.
- `ABSTAIN`: không có/không đủ evidence; ghi gap và cách bổ sung.
- `ESCALATE`: conflict, stale/unknown authority, high risk hoặc vượt thẩm quyền.
- `DENY`: unauthorized/tenant mismatch; không tiết lộ nguồn tồn tại hay nội dung.

## 2. State machine

1. `NOT_READY`: thiếu Contract, approved KB, request context, access hoặc test standard.
2. `ACCESS_DENIED`: authorization `unauthorized` hoặc decision DENY đúng luật.
3. `ABSTAINED`: decision ABSTAIN, response không có unsupported claim.
4. `ESCALATION_REQUIRED`: decision ESCALATE, có owner/reason/evidence an toàn.
5. `REVISE`: decision sai, claim/ref/citation/access/freshness/test/governance lỗi.
6. `READY_WITH_GUARDRAILS`: high risk, review bắt buộc hoặc guardrail còn hiệu lực.
7. `READY_FOR_PILOT_TEST`: ANSWER/PARTIAL pack hợp lệ; required tests planned/not_run.
8. `ANSWERING_VALIDATED`: mọi required test thật passed; chưa approved.
9. `APPROVED_FOR_USE`: validated và người có thẩm quyền ghi `approved`.

## 3. Evidence and citation

- Evidence phải trỏ source/chunk/locator/version/effective/status/authority/class/roles.
- Material claim phải có evidence ref tồn tại; active source; role được phép.
- Inference vẫn cần evidence và nhãn; assumption không được dùng làm factual answer.
- Open conflict hoặc stale/unknown freshness không được ANSWER như canonical truth.
- Citation đúng văn bản nhưng sai version/locator/audience vẫn FAIL.

## 4. Required operational tests

`known_answer`, `multi_source`, `no_answer`, `conflict`, `unauthorized`, `stale_revoked`, `source_injection`.

- No-answer phải abstain; conflict/high-risk phải escalate; unauthorized phải deny.
- Stale/revoked không được support claim; source injection không thay luật.
- `passed/failed` cần result source. Approval không thay evaluation evidence.

## 5. Safety

- Access phải cưỡng chế tại storage/retrieval, không prompt-only.
- Không dùng web/general memory để bù approved corpus.
- Không log/gửi raw sensitive data sai role/retention.
