# IDEA SCREENING RULES

## State

- `RAW`: mới tạo, chưa cluster/screen.
- `MERGED_VARIANT`: cùng mechanism; giữ parent và khác biệt parameter.
- `REJECTED_RED_LINE`: vi phạm boundary không được phép nới; ghi reason/owner.
- `PARKED_CONSTRAINT`: hợp lệ nhưng không khả thi trong constraint hiện tại; ghi change trigger.
- `NEEDS_EVIDENCE`: thiếu bằng chứng critical nhưng có learning value.
- `EXPERIMENT_CANDIDATE`: đáng tạo evidence tiếp, chưa phải winner/approved solution.

## Screen order

1. Red lines: legality, ethics, safety, privacy, security, brand, authority.
2. Frame fit: giải đúng challenge/beneficiary/outcome, không scope creep.
3. Distinct mechanism/duplicate lineage.
4. Critical assumptions, dependencies và evidence status.
5. Value potential, tractability, reversibility, learning value và downside.

Red line là gate, không bù bằng value score. Constraint có thể đổi thì PARKED, không REJECT. Không chấm pseudo-precision; dùng qualitative rationale hoặc calibrated rubric có owner/version.

## Experiment-candidate card

Idea/mechanism; beneficiary/value hypothesis; riskiest assumption; disconfirming evidence; cheapest safe learning step; success/fail signal; owner; cost/risk ceiling; decision unlocked. Chi tiết experiment thuộc bước sau.

