# Stakeholder communication gate rules

## 1. Evidence before label

| Field | Minimum evidence | Do not infer |
|---|---|---|
| Power | formal authority, resource/control right, recorded dependency | power from title alone |
| Interest | stated need, behavior or documented impact | interest from silence |
| Impact | process/data/financial/legal/people consequence with source | impact from general role |
| Stance | dated quote, vote, decision or observed action | support/resistance from tone |
| Influence path | documented relationship or decision flow | friendship, loyalty or hidden motive |

Every rating needs `evidence_refs`, `confidence`, `last_verified` and a review trigger. Unknown stays `UNKNOWN`.

## 2. Salience and engagement level

Use power–interest as the default routing, then override for formal rights, legitimacy, urgency, harm or severe impact.

| Level | Typical condition | Required handling |
|---|---|---|
| `MANAGE_CLOSELY` | high decision power or severe impact/urgency | direct owner, pre-brief, two-way loop, explicit closure |
| `KEEP_SATISFIED` | high power, lower active interest | concise decision/risk view, exception trigger |
| `KEEP_INFORMED` | lower power, high impact/interest | timely detail, feedback route, no token consultation |
| `MONITOR` | low current power/impact/interest | proportionate update, review trigger |

Never downgrade a party's legal right or material harm because interest appears low.

## 3. Decision-right gate

For every issue declare one accountable decision/approval owner. Separate:

- `PROPOSE`: prepares recommendation;
- `DECIDE` or `APPROVE`: owns the final authorized choice;
- `CONSULT`: input is requested before choice;
- `VETO_OR_ESCALATE`: formal stop or escalation right;
- `EXECUTE`: carries out the authorized action;
- `INFORMED`: receives the approved result.

Two final owners, no owner, or a hidden veto makes the issue `NOT_READY`.

## 4. Message integrity gate

Each message unit must trace to an active source and one issue. Preserve:

- state now and decision status;
- facts, number/date/unit and locator;
- uncertainty, qualifier, risk and alternative;
- impact and what does not change;
- ask/choice, owner and due condition;
- disclosure/accessibility/channel boundary.

An audience-specific version may change order, depth and vocabulary, never truth, right, consequence or commitment.

## 5. No-surprise sequencing

Default route: affected/authorized owner pre-brief → formal decision → manager/partner cascade → broad notice → feedback → closure. Change the route only with a documented reason.

Block release when a stakeholder with formal authority, execution responsibility or severe direct impact would learn after an external/public audience without an approved exception.

## 6. Ethical engagement

Allowed: transparent rationale, evidence, options, genuine consultation, explicit trade-off and accessible feedback.

Blocked: deception, hidden sponsorship, fake grassroots support, bribery, threat, retaliation, selective omission of material harm, protected-trait targeting, covert profiling or fabricated endorsement.

“Consensus” means recorded understanding and positions; it never means erasing dissent.

## 7. State model

| State | Meaning |
|---|---|
| `NOT_READY` | missing contract, source, stakeholder, rights, message, sequence or critical control |
| `READY_FOR_STAKEHOLDER_REVIEW` | pack is internally coherent; stakeholder/fact/accessibility review remains |
| `READY_FOR_AUTHORIZED_RELEASE` | required human approvals are evidenced; sender still decides and performs release |

The engine never emits `APPROVED`, `SENT` or `RELEASED`.

## 8. Seven test types

1. `stakeholder_evidence_trace`
2. `decision_rights_integrity`
3. `message_truth_action`
4. `sequence_no_surprise`
5. `disclosure_accessibility_fairness`
6. `feedback_commitment_closure`
7. `approval_state_boundary`
