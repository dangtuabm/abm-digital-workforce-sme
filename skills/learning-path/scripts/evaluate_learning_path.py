#!/usr/bin/env python3
"""Deterministic learning-path contract, dependency and workload gate."""
import argparse
import json
import sys
from pathlib import Path


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def has_cycle(graph):
    visiting, done = set(), set()

    def visit(node):
        if node in visiting:
            return True
        if node in done:
            return False
        visiting.add(node)
        if any(visit(parent) for parent in graph.get(node, [])):
            return True
        visiting.remove(node)
        done.add(node)
        return False

    return any(visit(node) for node in graph)


def run(data):
    issues = []
    contract = data.get("contract", {})
    for key in ("learner_or_role", "target_capability", "target_evidence",
                "baseline_ref", "owner", "risk_level", "capacity_hours"):
        if contract.get(key) in (None, "", []):
            issues.append(f"contract missing {key}")
    if not number(contract.get("capacity_hours")) or contract.get("capacity_hours", 0) <= 0:
        issues.append("capacity_hours invalid")
    gaps = data.get("gaps", [])
    if not gaps:
        issues.append("gaps missing")
    if issues:
        return {"path_id": data.get("path_id"), "state": "NOT_READY",
                "issues": sorted(set(issues)), "warnings": []}

    stages = data.get("stages", [])
    if not stages:
        return {"path_id": data.get("path_id"), "state": "DRAFT",
                "issues": ["stages missing"], "warnings": []}

    stage_issues, ids, graph, total_effort = [], [], {}, 0.0
    for stage in stages:
        sid = stage.get("id")
        if not sid or sid in ids:
            stage_issues.append("stage id missing/duplicate")
        ids.append(sid)
        for key in ("outcomes", "practice", "artifact", "assessment", "gate"):
            if stage.get(key) in (None, "", []):
                stage_issues.append(f"{sid or 'unknown'} missing {key}")
        effort = stage.get("effort_hours")
        if not number(effort) or effort < 0:
            stage_issues.append(f"{sid or 'unknown'} effort invalid")
        else:
            total_effort += effort
        graph[sid] = stage.get("prerequisites", [])
    known = set(ids)
    unknown_prereq = sorted({p for parents in graph.values() for p in parents if p not in known})
    self_links = sorted({sid for sid, parents in graph.items() if sid in parents})
    if unknown_prereq:
        stage_issues.append("unknown prerequisite")
    if self_links or has_cycle(graph):
        stage_issues.append("dependency cycle/self-link")
    if total_effort > contract["capacity_hours"]:
        stage_issues.append("effort exceeds capacity")

    transfer = data.get("transfer", {})
    for key in ("workplace_application", "manager_or_mentor", "feedback_cadence",
                "reinforcement", "success_measure", "recheck_trigger"):
        if not transfer.get(key):
            stage_issues.append(f"transfer missing {key}")
    if stage_issues:
        return {"path_id": data.get("path_id"), "state": "REVISE",
                "total_effort_hours": total_effort,
                "capacity_hours": contract["capacity_hours"],
                "issues": sorted(set(stage_issues)), "warnings": []}

    review = data.get("expert_review", {})
    review_pending = (
        contract["risk_level"] in ("high", "critical") or review.get("required") is True
    ) and review.get("status") != "approved"
    guardrails = data.get("guardrails", [])
    state = "READY_WITH_GUARDRAILS" if guardrails or review_pending else "READY_FOR_PILOT"
    return {"path_id": data.get("path_id"), "state": state,
            "total_effort_hours": total_effort,
            "capacity_hours": contract["capacity_hours"],
            "stage_count": len(stages), "guardrails": guardrails,
            "issues": [], "warnings": []}


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
