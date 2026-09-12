# CHALLENGE COVERAGE PROTOCOL

## 1. Chọn độ sâu theo consequence

| Decision profile | Coverage tối thiểu |
|---|---|
| Reversible, bounded | Logic, evidence, constraint, execution, stop/rollback |
| Material, cross-functional | Thêm base rate, incentives, dependency/cascade, option completeness, stakeholder externality |
| Irreversible/high-impact | Thêm independent expert, pre-mortem sâu, legal/ethics/safety/privacy, correlated failure và worst credible case |

## 2. Coverage axes

- **Logic:** conclusion có theo premises; circular reasoning, false dichotomy, hidden objective.
- **Evidence:** source/version/freshness, denominator, selection bias, counterevidence, measurement artifact.
- **Reference class:** base rate/analogy có thật và comparable; nếu thiếu ghi request, không bịa.
- **System:** incentive, power, handoff, dependency, bottleneck, feedback, delay, second-order/externality.
- **Execution:** capability, adoption, control, sequencing, single point of failure, rollback.
- **Decision process:** authority, option/status quo completeness, sunk cost, anchoring, escalation of commitment.

## 3. Independent rounds

1. Steelman không xem kết luận challenge cũ.
2. Attack theo axes và material assumptions.
3. Pre-mortem: giả định outcome thất bại, truy failure mechanisms.
4. Opposite case: điều gì phải đúng để alternative/inaction thắng.
5. Synthesis: gộp findings theo mechanism; giữ dissent và gaps.

Coverage không tính bằng số objections. Một material assumption chưa test quan trọng hơn mười câu hỏi nhỏ.
