#!/usr/bin/env python3
"""Deterministic gate and scorer for deliberate practice and feedback."""
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
    required = ("practice_id", "source_ref", "capability", "outcome", "learner_context", "rubric_version", "mastery_threshold", "max_attempts", "owner", "risk_level")
    missing = [key for key in required if not nonempty(contract.get(key))]
    for key in ("required_stages", "mastery_required_stages"):
        if not nonempty(standards.get(key)):
            missing.append(f"standards.{key}")
    rubric = data.get("rubric") or []
    if not rubric:
        missing.append("rubric")
    if missing:
        return {"state": "NOT_READY", "issues": [f"missing:{x}" for x in missing], "warnings": [], "guardrails": guardrails}

    criteria: dict[str, dict[str, Any]] = {}
    total_weight = 0.0
    for index, criterion in enumerate(rubric, start=1):
        label = criterion.get("id") or f"row_{index}"
        absent = [key for key in ("id", "weight", "observable", "pass_anchor", "failure_anchor") if not nonempty(criterion.get(key))]
        if absent:
            issues.append(f"rubric_fields:{label}:{','.join(absent)}")
        if nonempty(criterion.get("id")):
            if criterion["id"] in criteria:
                issues.append(f"duplicate_criterion:{criterion['id']}")
            criteria[criterion["id"]] = criterion
        try:
            total_weight += float(criterion.get("weight") or 0)
        except (TypeError, ValueError):
            issues.append(f"invalid_weight:{label}")
    total_weight = round(total_weight, 2)
    if abs(total_weight - 100.0) > 0.1:
        issues.append(f"weight_total:{total_weight}!=100")

    tasks = data.get("tasks") or []
    if not tasks:
        if issues:
            return {"state": "REVISE", "issues": sorted(set(issues)), "warnings": [], "guardrails": guardrails}
        return {"state": "DRAFT", "issues": ["no_tasks"], "warnings": [], "guardrails": guardrails}
    task_ids: set[str] = set()
    stages: set[str] = set()
    task_fields = ("id", "stage", "instructions", "evidence_required", "conditions", "difficulty", "feedback_timing", "accessibility", "safety", "data_minimization", "owner")
    for index, task in enumerate(tasks, start=1):
        label = task.get("id") or f"row_{index}"
        absent = [key for key in task_fields if not nonempty(task.get(key))]
        if absent:
            issues.append(f"task_fields:{label}:{','.join(absent)}")
        if nonempty(task.get("id")):
            if task["id"] in task_ids:
                issues.append(f"duplicate_task:{task['id']}")
            task_ids.add(task["id"])
        if nonempty(task.get("stage")):
            stages.add(task["stage"])
    for stage in standards["required_stages"]:
        if stage not in stages:
            issues.append(f"missing_stage:{stage}")

    calibration = data.get("calibration") or {}
    for key in ("examples", "adjudication_rule", "owner"):
        if not nonempty(calibration.get(key)):
            issues.append(f"calibration_missing:{key}")
    measurement = data.get("measurement") or {}
    for key in ("baseline_score", "latest_score", "attempts_to_mastery", "error_recurrence", "transfer_score", "evaluator_agreement", "result_owner"):
        if not nonempty(measurement.get(key)):
            issues.append(f"measurement_missing:{key}")

    attempts = data.get("attempts") or []
    if len(attempts) > int(contract["max_attempts"]):
        issues.append(f"attempt_limit:{len(attempts)}>{contract['max_attempts']}")
    stage_passes: set[str] = set()
    scored_attempts: list[dict[str, Any]] = []
    for index, attempt in enumerate(attempts, start=1):
        label = attempt.get("attempt_id") or f"row_{index}"
        absent = [key for key in ("attempt_id", "task_id", "evidence_ref", "scale_max", "criterion_scores", "critical_errors", "feedback", "reviewer") if key not in attempt or not nonempty(attempt.get(key)) and key != "critical_errors"]
        if absent:
            issues.append(f"attempt_fields:{label}:{','.join(absent)}")
            continue
        task = next((item for item in tasks if item.get("id") == attempt.get("task_id")), None)
        if not task:
            issues.append(f"unknown_task:{label}:{attempt.get('task_id')}")
            continue
        feedback = attempt.get("feedback") or {}
        feedback_missing = [key for key in ("evidence", "diagnosis", "priority", "next_task_id", "confidence") if not nonempty(feedback.get(key))]
        if feedback_missing:
            issues.append(f"feedback_fields:{label}:{','.join(feedback_missing)}")
        try:
            scale_max = float(attempt["scale_max"])
            if scale_max <= 0:
                raise ValueError
            score = 0.0
            scores = attempt["criterion_scores"]
            for criterion_id, criterion in criteria.items():
                if criterion_id not in scores:
                    issues.append(f"missing_criterion_score:{label}:{criterion_id}")
                    continue
                value = float(scores[criterion_id])
                if value < 0 or value > scale_max:
                    issues.append(f"score_range:{label}:{criterion_id}")
                score += float(criterion["weight"]) * value / scale_max
            score = round(score, 2)
            critical = list(attempt.get("critical_errors") or [])
            passed = score >= float(contract["mastery_threshold"]) and not critical
            if passed:
                stage_passes.add(task["stage"])
            scored_attempts.append({"attempt_id": label, "stage": task["stage"], "score": score, "critical_errors": critical, "passed": passed})
        except (TypeError, ValueError):
            issues.append(f"invalid_attempt_score:{label}")

    mastery_required = set(standards["mastery_required_stages"])
    mastery = mastery_required.issubset(stage_passes)
    if issues:
        state = "REVISE"
    elif not attempts:
        state = "READY_FOR_PRACTICE"
    else:
        state = "MASTERY_EVIDENCED" if mastery else "MASTERY_NOT_YET"
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
            "rubric_weight": total_weight,
            "task_count": len(tasks),
            "stages": sorted(stages),
            "attempts": scored_attempts,
            "mastery_stage_passes": sorted(stage_passes),
            "mastery_evidenced": mastery,
        },
    }


def selftest() -> dict[str, Any]:
    stages = ["diagnostic", "scaffolded", "independent", "transfer"]
    tasks = [{"id": f"T{i+1}", "stage": stage, "instructions": "perform authentic task", "evidence_required": "versioned artifact", "conditions": "defined context", "difficulty": f"level-{i+1}", "feedback_timing": "after evidence", "accessibility": "equivalent mode", "safety": "reviewed", "data_minimization": "minimum", "owner": "coach"} for i, stage in enumerate(stages)]
    feedback = {"evidence": "artifact lines", "diagnosis": "execution gap", "priority": "criterion C2", "next_task_id": "T4", "confidence": "high"}
    data = {
        "contract": {"practice_id": "PRAC-T", "source_ref": "CUR-T", "capability": "business skill", "outcome": "accepted artifact", "learner_context": "manager", "rubric_version": "R1", "mastery_threshold": 80, "max_attempts": 4, "owner": "learning-owner", "risk_level": "medium", "standards": {"required_stages": stages, "mastery_required_stages": ["independent", "transfer"]}},
        "rubric": [{"id": "C1", "weight": 60, "observable": "correct decision", "pass_anchor": "accurate", "failure_anchor": "material error"}, {"id": "C2", "weight": 40, "observable": "usable artifact", "pass_anchor": "ready", "failure_anchor": "not usable"}],
        "tasks": tasks,
        "calibration": {"examples": ["pass", "borderline", "fail"], "adjudication_rule": "second reviewer resolves", "owner": "domain-owner"},
        "attempts": [
            {"attempt_id": "A1", "task_id": "T3", "evidence_ref": "artifact-v1", "scale_max": 4, "criterion_scores": {"C1": 4, "C2": 3.5}, "critical_errors": [], "feedback": feedback, "reviewer": "assessor"},
            {"attempt_id": "A2", "task_id": "T4", "evidence_ref": "artifact-v2", "scale_max": 4, "criterion_scores": {"C1": 3.5, "C2": 3.5}, "critical_errors": [], "feedback": {**feedback, "next_task_id": "maintain"}, "reviewer": "assessor"},
        ],
        "measurement": {"baseline_score": 55, "latest_score": 87.5, "attempts_to_mastery": 2, "error_recurrence": "none", "transfer_score": 87.5, "evaluator_agreement": 0.9, "result_owner": "learning-owner"},
        "guardrails": [], "expert_review": "approved",
    }
    result = evaluate(data)
    assert result["state"] == "MASTERY_EVIDENCED", result
    assert result["metrics"]["rubric_weight"] == 100.0, result
    assert result["metrics"]["mastery_evidenced"] is True, result
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
