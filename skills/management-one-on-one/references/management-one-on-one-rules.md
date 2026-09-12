# Management One-on-One Control Rules

## Contract and privacy

- Session phải có purpose, human facilitator, participants, consent, note/recording rule, access và retention.
- Không covert record, emotion recognition, keystroke/activity surveillance hoặc private-note harvesting.
- Chỉ dùng work evidence đã cấp quyền; protected traits, health/family/religion/politics và đời tư bị loại trừ trừ khi participant chủ động nêu và policy yêu cầu protected route.

## Evidence and fairness

- Fact có source/as-of/locator; interpretation có confidence và quyền phản hồi.
- Feedback dùng Situation–Behavior–Impact; không dùng “lười”, “thiếu trung thành”, “không phù hợp văn hóa” nếu không có observable behavior.
- Không biến một sự kiện thành rating; không bịa quote, intent, emotion hoặc commitment.

## Agenda and commitments

- Agenda phải có topic từ cả manager và participant; participant có protected time.
- Mỗi commitment có owner, outcome/DoD, due, dependency, support, evidence và follow-up.
- Manager commitments được kiểm như participant commitments; request khác decision.

## Sensitive boundary

- Health, harassment, discrimination, retaliation, legal và immediate safety phải đi protected route; pack không chẩn đoán hoặc điều tra.
- A.I không quyết định rating, pay, bonus, discipline, promotion, transfer, termination hoặc HR-file update.

## Forbidden controls

Flags: `evidence_fabricated`, `quote_fabricated`, `emotion_inferred`, `personality_labeled`, `protected_trait_used`, `private_note_exposed`, `covert_recording`, `surveillance_used`, `agenda_one_sided`, `system_blocker_hidden`, `manager_commitment_omitted`, `sensitive_route_bypassed`, `auto_sent`, `auto_recorded`, `auto_rated`, `auto_disciplined`, `auto_promoted`, `auto_terminated`, `hr_file_updated`, `confirmation_faked`.

States: `SENT`, `RECORDED`, `RATED`, `DISCIPLINED`, `PROMOTED`, `TERMINATED`, `HR_FILE_UPDATED`, `CONFIRMED`.

## Reviews

`MANAGER_PREP` và `PEOPLE_POLICY_PRIVACY` phải PASS. Gate cuối `FINAL_HUMAN_1ON1` hoặc `PARTICIPANT_CONFIRMATION` phải `PENDING` với reviewer/evidence.
