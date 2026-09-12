#!/usr/bin/env python3
"""Deterministic explanation-integrity linter and verification gate."""
import argparse
import json
import sys
from pathlib import Path


def number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def run(data):
    contract_issues = []
    concept = data.get("concept", {})
    for key in ("name", "canonical_definition", "source_id", "scope",
                "boundary_conditions", "prerequisites", "mechanism", "risk_level"):
        if concept.get(key) in (None, "", []):
            contract_issues.append(f"concept missing {key}")
    audience = data.get("audience", {})
    for key in ("role", "prior_knowledge", "use_case"):
        if audience.get(key) in (None, ""):
            contract_issues.append(f"audience missing {key}")
    if contract_issues:
        return {"explanation_id": data.get("explanation_id"), "state": "NOT_READY",
                "issues": sorted(set(contract_issues)), "warnings": []}

    draft_issues = []
    explanation = data.get("explanation", {})
    for key in ("plain_language", "layers", "examples", "non_examples"):
        if explanation.get(key) in (None, "", []):
            draft_issues.append(f"explanation missing {key}")
    analogy = explanation.get("analogy", {})
    if analogy.get("used") is True:
        if not analogy.get("mappings") or not analogy.get("breakpoints"):
            draft_issues.append("analogy missing mappings/breakpoints")
    if draft_issues:
        return {"explanation_id": data.get("explanation_id"), "state": "DRAFT",
                "issues": sorted(set(draft_issues)), "warnings": []}

    verification = data.get("verification")
    if not verification:
        return {"explanation_id": data.get("explanation_id"), "state": "DRAFT",
                "issues": ["verification missing"], "warnings": []}
    traceability = verification.get("source_traceability")
    threshold = verification.get("traceability_min")
    checks = verification.get("checks", [])
    check_map = {item.get("id"): item.get("passed") for item in checks}
    required = {"recall", "discriminate", "transfer"}
    missing_checks = sorted(required - set(check_map))
    if (not verification.get("result_source_id") or not number(traceability)
            or not number(threshold) or missing_checks):
        return {"explanation_id": data.get("explanation_id"), "state": "INCONCLUSIVE",
                "issues": ["verification evidence invalid"], "warnings": missing_checks}

    failed_checks = sorted(key for key in required if check_map.get(key) is not True)
    critical_errors = verification.get("critical_errors", [])
    traceability_pass = traceability >= threshold
    misconception_pass = verification.get("misconceptions_resolved") is True
    if failed_checks or critical_errors or not traceability_pass or not misconception_pass:
        state = "REVISE"
    else:
        review = verification.get("expert_review", {})
        review_pending = (
            concept["risk_level"] in ("high", "critical") or review.get("required") is True
        ) and review.get("status") != "approved"
        state = "EXPERT_REVIEW_REQUIRED" if review_pending else "VERIFIED"
    return {
        "explanation_id": data.get("explanation_id"),
        "state": state,
        "traceability_pass": traceability_pass,
        "misconception_pass": misconception_pass,
        "failed_checks": failed_checks,
        "critical_errors": critical_errors,
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
