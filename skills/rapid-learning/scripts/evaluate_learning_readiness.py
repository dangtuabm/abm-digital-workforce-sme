#!/usr/bin/env python3
"""Deterministic Learning Readiness contract linter and gate."""
import argparse
import json
import sys
from pathlib import Path


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def run(data):
    issues = []
    mission = data.get("mission", {})
    for key in ("learner", "target_task", "success_criteria", "scope", "owner", "risk_level"):
        if mission.get(key) in (None, "", []):
            issues.append(f"mission missing {key}")

    baseline = data.get("baseline", {})
    if baseline.get("completed") is not True:
        issues.append("baseline not completed")
    if not baseline.get("source_id"):
        issues.append("baseline missing source_id")

    coverage = data.get("coverage", {})
    required = set(coverage.get("required_topics", []))
    completed = set(coverage.get("completed_topics", []))
    if not required:
        issues.append("required_topics missing")
    traceability = coverage.get("source_traceability")
    if not number(traceability) or not 0 <= traceability <= 1:
        issues.append("source_traceability invalid")

    assessment = data.get("assessment")
    if issues:
        return {"learning_id": data.get("learning_id"), "state": "NOT_READY",
                "issues": sorted(set(issues)), "warnings": []}
    if not assessment:
        return {"learning_id": data.get("learning_id"), "state": "IN_PROGRESS",
                "issues": [], "warnings": []}

    score_keys = ("knowledge_score", "application_score", "knowledge_min",
                  "application_min", "traceability_min")
    invalid = [key for key in score_keys if not number(assessment.get(key))]
    if invalid or not assessment.get("result_source_id"):
        return {"learning_id": data.get("learning_id"), "state": "INCONCLUSIVE",
                "issues": ["assessment score/result source invalid"], "warnings": invalid}

    critical = assessment.get("critical_checks", [])
    failed_critical = [item.get("id", "unnamed") for item in critical if item.get("passed") is not True]
    missing_topics = sorted(required - completed)
    knowledge_pass = assessment["knowledge_score"] >= assessment["knowledge_min"]
    application_pass = assessment["application_score"] >= assessment["application_min"]
    traceability_pass = traceability >= assessment["traceability_min"]

    if missing_topics or failed_critical or not all((knowledge_pass, application_pass, traceability_pass)):
        state = "REMEDIATE"
    else:
        unknowns = data.get("critical_unknowns", [])
        guardrails = data.get("guardrails", [])
        review = data.get("expert_review", {})
        review_pending = (
            mission["risk_level"] in ("high", "critical") or review.get("required") is True
        ) and review.get("status") != "approved"
        state = "READY_WITH_GUARDRAILS" if unknowns or guardrails or review_pending else "READY_FOR_TASK"

    return {
        "learning_id": data.get("learning_id"),
        "state": state,
        "knowledge_pass": knowledge_pass,
        "application_pass": application_pass,
        "traceability_pass": traceability_pass,
        "missing_topics": missing_topics,
        "failed_critical_checks": failed_critical,
        "critical_unknowns": data.get("critical_unknowns", []),
        "guardrails": data.get("guardrails", []),
        "issues": [],
        "warnings": []
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = run(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    text = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
