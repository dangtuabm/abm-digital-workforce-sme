# LEGAL COMPLIANCE RULES

## 1. Mô hình dữ liệu tối thiểu

- `mandate`: entity/activity/product/process, purpose, jurisdiction/geography, as-of/horizon, owners/authorities, reviews, privilege/privacy, non-goals.
- `sources`: id, instrument/type/issuer/official locator, version/publication/effective/status dates, jurisdiction/scope, binding status, language, rights/access, supersession, confidence, supports.
- `applicability`: subject/activity/product/person/data/transaction, territorial/material/temporal scope, trigger/threshold, exemption, source IDs, interpretation owner/status.
- `obligations`: actor, required/prohibited action, trigger/frequency/deadline/threshold, exception, process/system/record, evidence/retention, owner/authority, consequence, source pinpoint.
- `controls`: objective/risk, type, frequency, population, performer/reviewer, system, evidence, exception/fallback, obligation IDs.
- `evidence_tests`: period/population/sample/method, evidence source/custody/integrity/access, result/deviation/limitation/re-performance, control IDs.
- `exceptions_incidents`, `regulatory_changes`, `remediations`, `risks`, `decision_queue`, `tests`, `reviews`, `output_sections`.

## 2. Quy tắc nguồn và applicability

1. Ưu tiên văn bản/website chính thức của cơ quan ban hành hoặc quản lý; ghi URL, ngày truy cập/as-of, phiên bản, ngày công bố/hiệu lực/hết hiệu lực và phạm vi.
2. Tách: law/regulation/order/license/permit/contract/policy/standard/guidance/interpretation. Gắn binding status theo jurisdiction và xác nhận của counsel; không tự nâng guidance/standard thành luật.
3. Mọi nghĩa vụ material có source pinpoint và applicability record. Khi có bản dịch, giữ link bản gốc và ghi translation status.
4. Mâu thuẫn, supersession, amendment, transition và unknown phải visible; không chọn nguồn thuận tiện để ép kết luận.
5. `APPLICABLE_PENDING_COUNSEL` không đồng nghĩa `APPLICABLE_CONFIRMED`; `NOT_APPLICABLE` cần owner, rationale và source.

## 3. Trace và assurance

Trace bắt buộc: source → applicability → obligation → process/owner/authority → control → evidence → test → finding/gap → remediation/decision.

- Design: control có mục tiêu, loại, performer/reviewer, frequency, population, evidence, exception/fallback.
- Operation: test có period, population, sample/method/basis, result, deviation, evidence integrity/custody và limitation.
- Không suy từ document tồn tại thành control vận hành; không suy từ sample thành toàn population; không gọi assurance khi thiếu reviewer independence.
- Finding phải tách fact/allegation/hypothesis. Remediation và closure luôn có authorized approval/evidence.

## 4. Change, incident và quyết định

- Regulatory change: detected/publication/effective dates, source, applicability impact, affected obligations/controls/policies/contracts/training, transition/cutover, interim control, owner and decision.
- Incident/exception: confidentiality/privilege/privacy/security route trước; reporting/filing/self-disclosure là human legal decision.
- Decision recommendation chỉ: `LEGAL_INTERPRETATION_REVIEW`, `APPLICABILITY_REVIEW`, `CONTROL_GAP_REVIEW`, `INCIDENT_REPORTING_REVIEW`, `REGULATORY_CHANGE_REVIEW`, `REMEDIATION_REVIEW`, `ASSURANCE_REVIEW`, `REVISE`, `HOLD`.
- Human state luôn `PENDING` trong artifact do A.I tạo.

## 5. Rủi ro và cấm

Sáu risk types: `SOURCE_APPLICABILITY_INTERPRETATION`, `OBLIGATION_DEADLINE_REPORTING`, `CONTROL_DESIGN_OPERATING_EFFECTIVENESS`, `EVIDENCE_PRIVILEGE_RECORDS`, `REGULATORY_CHANGE_LICENSE_CONTINUITY`, `BREACH_REMEDIATION_ENFORCEMENT_REPUTATION`.

Cấm fabricate/hide source, law, date, threshold, obligation, control, evidence, exception, incident, reporting deadline hoặc review; cấm expose privilege/PII/credential; cấm alter/delete/falsify evidence; cấm auto legal opinion/certification/filing/reporting/contact/admission/investigation/discipline/remediation/control change/issue closure.

## 6. Nguồn nguyên tắc tham chiếu — as-of 22/08/2026

- ISO 37301:2021, Compliance management systems: https://www.iso.org/standard/75080.html — management-system reference; không tự chứng nhận và không thay luật địa phương.
- OECD Guidelines for Multinational Enterprises on Responsible Business Conduct, 2023: https://www.oecd.org/en/publications/oecd-guidelines-for-multinational-enterprises-on-responsible-business-conduct_81f92357-en.html — due-diligence reference; recommendations, không mặc định là binding law.
- U.S. DOJ, Evaluation of Corporate Compliance Programs, September 2024: https://www.justice.gov/criminal/criminal-fraud/page/file/937501 — enforcement guidance trong phạm vi Hoa Kỳ; dùng ba lens design, empowerment/resources và operation-in-practice, không áp thành luật toàn cầu.

Luôn kiểm lại nguồn chính thức tại thời điểm dùng; law/regulator/counsel hiện hành có thẩm quyền cao hơn reference này.
