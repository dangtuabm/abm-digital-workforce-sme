#!/usr/bin/env python3
"""Deterministic curriculum alignment, time and practice gate."""
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
    required = ("program_name", "cohort", "business_problem", "target_capabilities",
                "baseline_ref", "delivery_format", "total_minutes",
                "minimum_practice_ratio", "owner", "risk_level")
    for key in required:
        if contract.get(key) in (None, "", []):
            issues.append(f"contract missing {key}")
    total_target = contract.get("total_minutes")
    ratio_target = contract.get("minimum_practice_ratio")
    if not number(total_target) or total_target <= 0:
        issues.append("total_minutes invalid")
    if not number(ratio_target) or not 0 <= ratio_target <= 1:
        issues.append("minimum_practice_ratio invalid")
    references = data.get("reference_programs", [])
    if contract.get("reference_library_available") is True and len(references) < 2:
        issues.append("reference trace requires at least two programs")
    if issues:
        return {"curriculum_id": data.get("curriculum_id"), "state": "NOT_READY",
                "issues": sorted(set(issues)), "warnings": []}

    modules = data.get("modules", [])
    if not modules:
        return {"curriculum_id": data.get("curriculum_id"), "state": "DRAFT",
                "issues": ["modules missing"], "warnings": []}

    design_issues, ids, graph, covered = [], [], {}, set()
    theory, practice = 0.0, 0.0
    required_sections = {"hook", "core", "case", "action"}
    for module in modules:
        mid = module.get("id")
        if not mid or mid in ids:
            design_issues.append("module id missing/duplicate")
        ids.append(mid)
        graph[mid] = module.get("prerequisites", [])
        covered.update(module.get("capabilities", []))
        for key in ("capabilities", "outcomes", "quick_win", "artifact", "assessment"):
            if module.get(key) in (None, "", []):
                design_issues.append(f"{mid or 'unknown'} missing {key}")
        if not required_sections.issubset(set(module.get("sections", []))):
            design_issues.append(f"{mid or 'unknown'} missing Hook-Core-Case-Action")
        if module.get("anti_pattern_before_best_practice") is not True:
            design_issues.append(f"{mid or 'unknown'} anti-pattern order invalid")
        for key in ("theory_minutes", "practice_minutes"):
            value = module.get(key)
            if not number(value) or value < 0:
                design_issues.append(f"{mid or 'unknown'} {key} invalid")
            elif key == "theory_minutes":
                theory += value
            else:
                practice += value
    known = set(ids)
    if any(parent not in known for parents in graph.values() for parent in parents):
        design_issues.append("unknown prerequisite")
    if any(mid in parents for mid, parents in graph.items()) or has_cycle(graph):
        design_issues.append("dependency cycle/self-link")
    uncovered = sorted(set(contract["target_capabilities"]) - covered)
    if uncovered:
        design_issues.append("target capability uncovered")
    total = theory + practice
    ratio = practice / total if total else 0.0
    if abs(total - total_target) > 0.01:
        design_issues.append("module time does not match contract")
    if ratio + 1e-12 < ratio_target:
        design_issues.append("practice ratio below contract")
    for area, keys in {
        "materials": ("facilitator_guide", "learner_workbook", "slide_outline", "prework", "source_ledger"),
        "evaluation": ("baseline", "formative", "summative", "transfer", "outcome_measure", "result_owner")
    }.items():
        block = data.get(area, {})
        for key in keys:
            if not block.get(key):
                design_issues.append(f"{area} missing {key}")
    if design_issues:
        return {"curriculum_id": data.get("curriculum_id"), "state": "REVISE",
                "total_minutes": total, "practice_ratio": round(ratio, 4),
                "uncovered_capabilities": uncovered,
                "issues": sorted(set(design_issues)), "warnings": []}

    review = data.get("expert_review", {})
    review_pending = (
        contract["risk_level"] in ("high", "critical") or review.get("required") is True
    ) and review.get("status") != "approved"
    guardrails = list(data.get("guardrails", []))
    if not contract.get("experience_blueprint_ref"):
        guardrails.append("experience blueprint pending")
    state = "READY_WITH_GUARDRAILS" if guardrails or review_pending else "READY_FOR_PILOT"
    return {"curriculum_id": data.get("curriculum_id"), "state": state,
            "module_count": len(modules), "total_minutes": total,
            "practice_ratio": round(ratio, 4),
            "uncovered_capabilities": [], "guardrails": guardrails,
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
