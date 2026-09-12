# Negotiation preparation gate rules

## 1. Mandate before tactics

Record objective, negotiator, mandate owner, final approver, authority by issue, expiry, stop/escalation, restricted data and prohibited actions. A title is not authority evidence.

| Authority state | Meaning | Action |
|---|---|---|
| `CONFIRMED` | named owner and evidence are current | prepare within limit |
| `CONDITIONAL` | permitted only if condition/reviewer passes | hold at approval gate |
| `UNKNOWN` | no current authority evidence | `NOT_READY` for that move |
| `PROHIBITED` | explicitly outside mandate | never include as available concession |

## 2. Evidence hierarchy

Prefer executed/approved term or current policy → authorized proposal/decision record → verified operational/financial data → dated direct statement → hypothesis. Show conflict; never silently choose the convenient source.

Every amount, percentage, quantity, date and duration needs value, unit/currency, source locator, effective date and owner. Estimates need a range and assumptions.

## 3. BATNA, reservation and ZOPA

- **BATNA:** best feasible alternative if no agreement; assign owner, readiness, trigger, cost/value and evidence.
- **Reservation boundary:** worst acceptable outcome by issue/package; only authority owner sets or changes it.
- **Walk-away condition:** observable trigger for pause/exit/escalation.
- **ZOPA:** overlap between reservations. If the other side's boundary is unknown, state `UNKNOWN`; an estimate never becomes confirmed through repetition.

Exactly one BATNA is active for the current mandate. Keep other alternatives as candidates.

## 4. Issue and trade discipline

| Field | Required control |
|---|---|
| Target | aspiration with objective criterion |
| Reservation | approved boundary, not opening position |
| Give | specific term and cost/impact to us |
| Get | reciprocal value, evidence or condition |
| Authority | limit and approver for this move |
| Sequence | smaller/conditional before larger/irreversible |
| Expiry | when offer or evidence becomes invalid |
| Stop | trigger to pause/escalate/walk away |

No `give` without a meaningful `get`, except a documented goodwill move approved in advance.

## 5. Package discipline

Use 2–3 packages when issues permit trade-offs. Packages must:

- satisfy non-negotiables and reservation boundaries;
- vary across issues, not disguise the same offer;
- show components, dependencies and total economics;
- carry finance/legal review when relevant;
- avoid claiming equivalence until the owner accepts the valuation method.

## 6. Counterparty hypothesis boundary

Separate known authority/interests/constraints from hypotheses. Each hypothesis needs source refs, alternative, confidence, expiry, falsifier and question to test it.

Blocked: protected/sensitive inference, private pressure point, personality diagnosis, illegal surveillance, impersonation, bluff presented as fact or fabricated leverage.

## 7. Session and agreement gate

One session has one primary objective. End with an accurate recap: agreed items, conditional items, open issues, owners, due conditions, approval/document route and next session.

Verbal alignment is not final agreement unless the authorized process says so. The engine never emits `AUTHORIZED`, `AGREED`, `SIGNED` or `EXECUTABLE`.

## 8. State model

| State | Meaning |
|---|---|
| `NOT_READY` | missing mandate, source, BATNA, reservation, trade, package, tests or critical control |
| `READY_FOR_MANDATE_REVIEW` | pack is coherent; human mandate/reviews remain |
| `READY_FOR_AUTHORIZED_SESSION` | all required human reviews and mandate evidence pass; negotiator still decides each move |

## 9. Seven test types

1. `mandate_authority_integrity`
2. `source_assumption_trace`
3. `batna_reservation_zopa`
4. `issue_trade_package_integrity`
5. `concession_reciprocity`
6. `scenario_question_process`
7. `approval_agreement_boundary`
