#!/usr/bin/env python3
"""Deterministic structural gate for a Learning Experience Control Blueprint."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def nonempty(value: Any) -> bool:
    return value not in (None, "", [], {})


def evaluate(data: dict[str, Any]) -> dict[str, Any]:
    contract = data.get("contract") or {}
    standards = contract.get("standards") or {}
    issues: list[str] = []
    warnings: list[str] = []
    guardrails = list(data.get("guardrails") or [])

    required_contract = (
        "experience_id", "curriculum_ref", "cohort", "learning_outcomes",
        "delivery_mode", "total_during_minutes", "owner", "risk_level",
    )
    missing = [key for key in required_contract if not nonempty(contract.get(key))]
    for key in ("required_phases", "min_format_variety", "max_same_format_minutes", "required_moments"):
        if not nonempty(standards.get(key)):
            missing.append(f"standards.{key}")
    if missing:
        return {"state": "NOT_READY", "issues": [f"missing:{x}" for x in missing], "warnings": [], "guardrails": guardrails}

    touchpoints = data.get("touchpoints") or []
    if not touchpoints:
        return {"state": "DRAFT", "issues": ["no_touchpoints"], "warnings": [], "guardrails": guardrails}

    outcome_set = set(contract["learning_outcomes"])
    covered: set[str] = set()
    tp_ids: set[str] = set()
    phases: set[str] = set()
    during: list[dict[str, Any]] = []
    required_tp_fields = ("id", "order", "phase", "outcome_refs", "learner_action", "format", "feedback", "owner", "accessibility", "fallback")
    for index, tp in enumerate(touchpoints, start=1):
        label = tp.get("id") or f"row_{index}"
        absent = [field for field in required_tp_fields if not nonempty(tp.get(field))]
        if absent:
            issues.append(f"touchpoint_fields:{label}:{','.join(absent)}")
        if nonempty(tp.get("id")):
            if tp["id"] in tp_ids:
                issues.append(f"duplicate_touchpoint:{tp['id']}")
            tp_ids.add(tp["id"])
        phase = tp.get("phase")
        if phase:
            phases.add(phase)
        refs = set(tp.get("outcome_refs") or [])
        unknown = refs - outcome_set
        if unknown:
            issues.append(f"unknown_outcomes:{label}:{','.join(sorted(unknown))}")
        covered |= refs & outcome_set
        if phase == "during":
            during.append(tp)

    for phase in standards["required_phases"]:
        if phase not in phases:
            issues.append(f"missing_phase:{phase}")
    for outcome in sorted(outcome_set - covered):
        issues.append(f"uncovered_outcome:{outcome}")

    try:
        during_total = round(sum(float(tp.get("duration_minutes") or 0) for tp in during), 2)
        expected_total = float(contract["total_during_minutes"])
        if abs(during_total - expected_total) > 0.1:
            issues.append(f"during_time_mismatch:{during_total}!={expected_total}")
    except (TypeError, ValueError):
        during_total = None
        issues.append("invalid_duration")

    formats = {tp.get("format") for tp in during if nonempty(tp.get("format"))}
    if len(formats) < int(standards["min_format_variety"]):
        issues.append(f"format_variety:{len(formats)}<{standards['min_format_variety']}")

    try:
        ordered = sorted(during, key=lambda tp: float(tp.get("order")))
        current = None
        run = 0.0
        maximum = 0.0
        for tp in ordered:
            fmt = tp.get("format")
            duration = float(tp.get("duration_minutes") or 0)
            run = run + duration if fmt == current else duration
            current = fmt
            maximum = max(maximum, run)
        if maximum > float(standards["max_same_format_minutes"]):
            issues.append(f"same_format_run:{maximum}>{standards['max_same_format_minutes']}")
    except (TypeError, ValueError):
        maximum = None
        issues.append("invalid_order_or_format_duration")

    present_moments: set[str] = set()
    for moment in data.get("moments") or []:
        kind, tp_id = moment.get("type"), moment.get("touchpoint_id")
        if not nonempty(kind) or tp_id not in tp_ids:
            issues.append(f"invalid_moment:{kind or 'missing'}:{tp_id or 'missing'}")
        else:
            present_moments.add(kind)
    for kind in standards["required_moments"]:
        if kind not in present_moments:
            issues.append(f"missing_moment:{kind}")

    service = data.get("service_blueprint") or {}
    for key in ("facilitator", "platform", "support", "assets", "incident_recovery", "data_privacy"):
        if not nonempty(service.get(key)):
            issues.append(f"service_missing:{key}")
    measurement = data.get("measurement") or {}
    for key in ("engagement_behavior", "learning_evidence", "application_signal", "feedback_source", "result_owner"):
        if not nonempty(measurement.get(key)):
            issues.append(f"measurement_missing:{key}")

    state = "REVISE" if issues else "READY_FOR_PILOT"
    if not issues and (contract.get("risk_level") == "high" or data.get("expert_review") != "approved" or guardrails):
        state = "READY_WITH_GUARDRAILS"
        if data.get("expert_review") != "approved":
            warnings.append("expert_review_pending")
    return {
        "state": state,
        "issues": sorted(set(issues)),
        "warnings": sorted(set(warnings)),
        "guardrails": guardrails,
        "metrics": {
            "touchpoint_count": len(touchpoints),
            "during_minutes": during_total,
            "format_variety": len(formats),
            "max_same_format_run": maximum,
            "covered_outcomes": sorted(covered),
        },
    }


def selftest() -> dict[str, Any]:
    touchpoints = [
        {"id": "TP-B1", "order": 1, "phase": "before", "outcome_refs": ["LO-1"], "learner_action": "baseline", "format": "form", "feedback": "readiness", "owner": "ops", "accessibility": "keyboard", "fallback": "phone"},
        {"id": "TP-D1", "order": 2, "phase": "during", "outcome_refs": ["LO-1"], "learner_action": "diagnose", "format": "case", "duration_minutes": 30, "feedback": "peer rubric", "owner": "trainer", "accessibility": "text alternative", "fallback": "printed case"},
        {"id": "TP-D2", "order": 3, "phase": "during", "outcome_refs": ["LO-1", "LO-2"], "learner_action": "build", "format": "practice", "duration_minutes": 35, "feedback": "coach", "owner": "trainer", "accessibility": "paired support", "fallback": "offline template"},
        {"id": "TP-D3", "order": 4, "phase": "during", "outcome_refs": ["LO-2"], "learner_action": "review", "format": "gallery", "duration_minutes": 25, "feedback": "rubric", "owner": "trainer", "accessibility": "verbal alternative", "fallback": "table review"},
        {"id": "TP-D4", "order": 5, "phase": "during", "outcome_refs": ["LO-2"], "learner_action": "commit", "format": "practice", "duration_minutes": 30, "feedback": "manager check", "owner": "trainer", "accessibility": "large print", "fallback": "paper plan"},
        {"id": "TP-A1", "order": 6, "phase": "after", "outcome_refs": ["LO-2"], "learner_action": "apply", "format": "workplace", "feedback": "manager", "owner": "manager", "accessibility": "async", "fallback": "office hour"},
    ]
    data = {
        "contract": {"experience_id": "LX-T", "curriculum_ref": "CUR-T", "cohort": "managers", "learning_outcomes": ["LO-1", "LO-2"], "delivery_mode": "blended", "total_during_minutes": 120, "owner": "learning-owner", "risk_level": "medium", "standards": {"required_phases": ["before", "during", "after"], "min_format_variety": 3, "max_same_format_minutes": 35, "required_moments": ["peak", "valley", "commitment", "shareable"]}},
        "touchpoints": touchpoints,
        "moments": [{"type": "valley", "touchpoint_id": "TP-D1"}, {"type": "peak", "touchpoint_id": "TP-D3"}, {"type": "shareable", "touchpoint_id": "TP-D3"}, {"type": "commitment", "touchpoint_id": "TP-D4"}],
        "service_blueprint": {"facilitator": "guide", "platform": "LMS", "support": "ops", "assets": ["case", "template"], "incident_recovery": "offline pack", "data_privacy": "minimum data"},
        "measurement": {"engagement_behavior": "attempt rate", "learning_evidence": "rubric", "application_signal": "30-day artifact", "feedback_source": "survey", "result_owner": "learning-owner"},
        "guardrails": [], "expert_review": "approved",
    }
    result = evaluate(data)
    assert result["state"] == "READY_FOR_PILOT", result
    assert result["metrics"]["during_minutes"] == 120.0, result
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    result = selftest() if args.self_test else evaluate(json.loads(args.input.read_text(encoding="utf-8")))
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
