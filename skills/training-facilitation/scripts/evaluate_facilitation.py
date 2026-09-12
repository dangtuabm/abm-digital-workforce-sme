#!/usr/bin/env python3
"""Deterministic structural gate for a Facilitation Control Runbook."""
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
    required = ("session_id", "source_ref", "session_outcomes", "cohort", "delivery_mode", "total_minutes", "owner", "risk_level")
    missing = [key for key in required if not nonempty(contract.get(key))]
    for key in ("max_monologue_minutes", "required_incidents"):
        if not nonempty(standards.get(key)):
            missing.append(f"standards.{key}")
    roles = data.get("roles") or {}
    for key in ("lead_facilitator", "producer", "participant_support", "incident_owner"):
        if not nonempty(roles.get(key)):
            missing.append(f"roles.{key}")
    if missing:
        return {"state": "NOT_READY", "issues": [f"missing:{x}" for x in missing], "warnings": [], "guardrails": guardrails}

    segments = data.get("segments") or []
    if not segments:
        return {"state": "DRAFT", "issues": ["no_segments"], "warnings": [], "guardrails": guardrails}

    outcomes = set(contract["session_outcomes"])
    covered: set[str] = set()
    ids: set[str] = set()
    general = ("id", "order", "type", "duration_minutes", "owner", "accessibility", "fallback")
    learning = ("outcome_refs", "learner_action", "evidence", "check_for_understanding", "facilitation_moves", "debrief")
    total = 0.0
    for index, segment in enumerate(segments, start=1):
        label = segment.get("id") or f"row_{index}"
        absent = [key for key in general if not nonempty(segment.get(key))]
        if segment.get("type") not in {"break", "admin"}:
            absent += [key for key in learning if not nonempty(segment.get(key))]
        if absent:
            issues.append(f"segment_fields:{label}:{','.join(absent)}")
        if nonempty(segment.get("id")):
            if segment["id"] in ids:
                issues.append(f"duplicate_segment:{segment['id']}")
            ids.add(segment["id"])
        refs = set(segment.get("outcome_refs") or [])
        unknown = refs - outcomes
        if unknown:
            issues.append(f"unknown_outcomes:{label}:{','.join(sorted(unknown))}")
        if segment.get("type") not in {"break", "admin"}:
            covered |= refs & outcomes
        try:
            duration = float(segment.get("duration_minutes") or 0)
            total += duration
            if segment.get("type") == "input" and duration > float(standards["max_monologue_minutes"]):
                issues.append(f"monologue_limit:{label}:{duration}>{standards['max_monologue_minutes']}")
        except (TypeError, ValueError):
            issues.append(f"invalid_duration:{label}")
    for outcome in sorted(outcomes - covered):
        issues.append(f"uncovered_outcome:{outcome}")
    try:
        expected = float(contract["total_minutes"])
        total = round(total, 2)
        if abs(total - expected) > 0.1:
            issues.append(f"time_mismatch:{total}!={expected}")
    except (TypeError, ValueError):
        issues.append("invalid_total_minutes")

    readiness = data.get("readiness") or {}
    for key in ("venue_or_platform", "materials", "role_brief", "accessibility_check", "emergency_contacts"):
        if not nonempty(readiness.get(key)):
            issues.append(f"readiness_missing:{key}")

    present_incidents: set[str] = set()
    incident_fields = ("type", "trigger", "owner", "response", "stop_or_escalate", "fallback")
    for incident in data.get("incident_playbooks") or []:
        label = incident.get("type") or "missing"
        absent = [key for key in incident_fields if not nonempty(incident.get(key))]
        if absent:
            issues.append(f"incident_fields:{label}:{','.join(absent)}")
        if nonempty(incident.get("type")):
            present_incidents.add(incident["type"])
    for kind in standards["required_incidents"]:
        if kind not in present_incidents:
            issues.append(f"missing_incident:{kind}")

    measurement = data.get("measurement") or {}
    for key in ("time_drift", "participation_distribution", "evidence_completion", "unanswered_questions", "incidents", "commitments", "result_owner"):
        if not nonempty(measurement.get(key)):
            issues.append(f"measurement_missing:{key}")

    state = "REVISE" if issues else "READY_FOR_DRY_RUN"
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
            "segment_count": len(segments),
            "total_minutes": total,
            "covered_outcomes": sorted(covered),
            "incident_coverage": sorted(present_incidents),
        },
    }


def selftest() -> dict[str, Any]:
    base = {"owner": "lead", "accessibility": "multimodal", "fallback": "offline card"}
    segments = [
        {**base, "id": "S1", "order": 1, "type": "opening", "duration_minutes": 10, "outcome_refs": ["LO-1"], "learner_action": "commit", "evidence": "goal card", "check_for_understanding": "sample", "facilitation_moves": ["pair-first"], "debrief": "purpose"},
        {**base, "id": "S2", "order": 2, "type": "input", "duration_minutes": 20, "outcome_refs": ["LO-1"], "learner_action": "diagnose", "evidence": "diagnosis", "check_for_understanding": "poll+why", "facilitation_moves": ["wait time"], "debrief": "pattern"},
        {**base, "id": "S3", "order": 3, "type": "practice", "duration_minutes": 35, "outcome_refs": ["LO-1", "LO-2"], "learner_action": "build", "evidence": "artifact", "check_for_understanding": "rubric check", "facilitation_moves": ["triads"], "debrief": "observe-meaning-apply"},
        {**base, "id": "S4", "order": 4, "type": "debrief", "duration_minutes": 20, "outcome_refs": ["LO-2"], "learner_action": "review", "evidence": "revision", "check_for_understanding": "teach-back", "facilitation_moves": ["gallery"], "debrief": "transfer"},
        {**base, "id": "S5", "order": 5, "type": "closing", "duration_minutes": 5, "outcome_refs": ["LO-2"], "learner_action": "commit", "evidence": "action plan", "check_for_understanding": "next-step", "facilitation_moves": ["individual"], "debrief": "commitment"},
    ]
    incident_types = ["dominant_voice", "silence", "conflict", "tech_failure", "accessibility_failure", "wellbeing_concern"]
    incidents = [{"type": kind, "trigger": "defined signal", "owner": "incident-owner", "response": "response ladder", "stop_or_escalate": "threshold", "fallback": "safe alternative"} for kind in incident_types]
    data = {
        "contract": {"session_id": "FAC-T", "source_ref": "LX-T", "session_outcomes": ["LO-1", "LO-2"], "cohort": "managers", "delivery_mode": "hybrid", "total_minutes": 90, "owner": "learning-owner", "risk_level": "medium", "standards": {"max_monologue_minutes": 20, "required_incidents": incident_types}},
        "roles": {"lead_facilitator": "lead", "producer": "producer", "participant_support": "support", "incident_owner": "incident-owner"},
        "readiness": {"venue_or_platform": "checked", "materials": "checked", "role_brief": "complete", "accessibility_check": "complete", "emergency_contacts": "available"},
        "segments": segments, "incident_playbooks": incidents,
        "measurement": {"time_drift": "planned vs actual", "participation_distribution": "turns by channel", "evidence_completion": "artifact rate", "unanswered_questions": "parking lot", "incidents": "incident log", "commitments": "action cards", "result_owner": "learning-owner"},
        "guardrails": [], "expert_review": "approved",
    }
    result = evaluate(data)
    assert result["state"] == "READY_FOR_DRY_RUN", result
    assert result["metrics"]["total_minutes"] == 90.0, result
    assert len(result["metrics"]["incident_coverage"]) == 6, result
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
