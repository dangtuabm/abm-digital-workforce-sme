#!/usr/bin/env python3
"""Deterministic readiness gate for a Brand Positioning Decision Pack.

Reads one local JSON file. It does not browse, call APIs, publish, or validate
market truth. Exit code 0 means structurally ready for the next declared state;
exit code 1 means NOT_READY because required controls are missing or invalid.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_EVIDENCE_TYPES = {"customer", "market", "competitor", "internal"}
REQUIRED_CRITERIA = {
    "relevance",
    "distinctiveness",
    "credibility",
    "defendability",
    "clarity_memorability",
    "commercial_fit",
    "strategic_stretch",
    "activation_cost",
}
REQUIRED_TESTS = {
    "category_clarity",
    "relevance",
    "distinctiveness_substitution",
    "credibility_proof",
    "unaided_recall",
}


def present(value: Any) -> bool:
    if value is None:
        return False
    if isinstance(value, str):
        return bool(value.strip())
    if isinstance(value, (list, dict, tuple, set)):
        return bool(value)
    return True


def require_fields(obj: Any, fields: list[str], path: str, errors: list[str]) -> None:
    if not isinstance(obj, dict):
        errors.append(f"{path} must be an object")
        return
    for field in fields:
        if not present(obj.get(field)):
            errors.append(f"missing {path}.{field}")


def unique_ids(items: list[dict[str, Any]], path: str, errors: list[str]) -> set[str]:
    ids = [str(item.get("id", "")).strip() for item in items]
    if any(not item_id for item_id in ids):
        errors.append(f"{path} contains blank id")
    if len(ids) != len(set(ids)):
        errors.append(f"{path} contains duplicate id")
    return {item_id for item_id in ids if item_id}


def main(input_path: str) -> int:
    payload = json.loads(Path(input_path).read_text(encoding="utf-8"))
    errors: list[str] = []
    warnings: list[str] = []
    guardrails = ["HUMAN_APPROVAL_REQUIRED_FOR_PUBLICATION_AND_REBRAND"]

    contract = payload.get("contract")
    require_fields(
        contract,
        ["id", "unit", "brand_level", "business_objective", "decision_owner", "scope", "status"],
        "contract",
        errors,
    )

    evidence = payload.get("evidence", [])
    if not isinstance(evidence, list) or not evidence:
        errors.append("evidence must be a non-empty list")
        evidence = []
    source_ids = unique_ids(evidence, "evidence", errors)
    evidence_types: set[str] = set()
    active_source_count = 0
    for index, source in enumerate(evidence):
        require_fields(
            source,
            ["id", "type", "title", "version", "owner", "authority", "locator", "status", "strength"],
            f"evidence[{index}]",
            errors,
        )
        evidence_types.add(str(source.get("type", "")))
        if source.get("authorized") is not True:
            errors.append(f"evidence[{index}] is not authorized")
        if source.get("status") == "active":
            active_source_count += 1
    missing_evidence_types = sorted(REQUIRED_EVIDENCE_TYPES - evidence_types)
    if missing_evidence_types:
        warnings.append("missing evidence types: " + ", ".join(missing_evidence_types))

    conflicts = payload.get("conflicts", [])
    if not isinstance(conflicts, list):
        errors.append("conflicts must be a list")
        conflicts = []
    unresolved_material_conflicts = 0
    for index, conflict in enumerate(conflicts):
        if conflict.get("material") is True and conflict.get("status") not in {"resolved", "accepted"}:
            unresolved_material_conflicts += 1
            errors.append(f"conflicts[{index}] material conflict is unresolved")

    target = payload.get("target")
    require_fields(
        target,
        ["primary_segment", "decision_unit", "problem", "occasion", "desired_progress", "choice_criteria", "exclusion"],
        "target",
        errors,
    )
    frame = payload.get("frame")
    require_fields(
        frame,
        ["category", "alternatives", "points_of_parity", "point_of_difference", "barrier"],
        "frame",
        errors,
    )

    territories = payload.get("territories", [])
    if not isinstance(territories, list) or not 1 <= len(territories) <= 3:
        errors.append("territories must contain 1 to 3 choices")
        territories = []
    territory_ids = unique_ids(territories, "territories", errors)
    for index, territory in enumerate(territories):
        require_fields(
            territory,
            ["id", "target_occasion", "category", "problem", "promise", "difference", "sacrifice", "proof_refs", "strategic_fit", "failure_mode"],
            f"territories[{index}]",
            errors,
        )
        bad_refs = sorted(set(territory.get("proof_refs", [])) - source_ids)
        if bad_refs:
            errors.append(f"territories[{index}] unknown proof refs: {', '.join(bad_refs)}")

    scorecard = payload.get("scorecard")
    require_fields(scorecard, ["criteria", "scores", "recommended_id"], "scorecard", errors)
    criterion_weights: dict[str, float] = {}
    if isinstance(scorecard, dict):
        for index, criterion in enumerate(scorecard.get("criteria", [])):
            name = str(criterion.get("name", "")).strip()
            weight = criterion.get("weight")
            if not name or not isinstance(weight, (int, float)) or weight <= 0:
                errors.append(f"scorecard.criteria[{index}] invalid name/weight")
                continue
            criterion_weights[name] = float(weight)
    missing_criteria = sorted(REQUIRED_CRITERIA - set(criterion_weights))
    if missing_criteria:
        errors.append("missing score criteria: " + ", ".join(missing_criteria))

    territory_scores: dict[str, float] = {}
    if isinstance(scorecard, dict) and criterion_weights:
        for index, row in enumerate(scorecard.get("scores", [])):
            territory_id = str(row.get("territory_id", "")).strip()
            ratings = row.get("ratings", {})
            if territory_id not in territory_ids:
                errors.append(f"scorecard.scores[{index}] unknown territory_id")
                continue
            missing_ratings = sorted(set(criterion_weights) - set(ratings))
            if missing_ratings:
                errors.append(f"scorecard.scores[{index}] missing ratings: {', '.join(missing_ratings)}")
                continue
            weighted_sum = 0.0
            valid = True
            for name, weight in criterion_weights.items():
                rating = ratings.get(name)
                if not isinstance(rating, (int, float)) or not 1 <= rating <= 5:
                    errors.append(f"scorecard.scores[{index}].ratings.{name} must be 1..5")
                    valid = False
                else:
                    weighted_sum += weight * float(rating)
            if valid:
                territory_scores[territory_id] = round(weighted_sum / sum(criterion_weights.values()), 4)

    recommended_id = str(scorecard.get("recommended_id", "")) if isinstance(scorecard, dict) else ""
    if recommended_id not in territory_ids:
        errors.append("scorecard.recommended_id is not a territory")
    if territory_scores and recommended_id in territory_scores:
        top_score = max(territory_scores.values())
        if territory_scores[recommended_id] != top_score:
            errors.append("recommended territory is not top-scoring")

    position = payload.get("position")
    require_fields(
        position,
        ["territory_id", "target", "frame", "problem", "promise", "difference", "reasons_to_believe", "sacrifice", "statement", "memory_hook", "status"],
        "position",
        errors,
    )
    if isinstance(position, dict) and position.get("territory_id") != recommended_id:
        errors.append("position.territory_id must equal scorecard.recommended_id")

    claims = payload.get("claims", [])
    if not isinstance(claims, list) or not claims:
        errors.append("claims must be a non-empty list")
        claims = []
    claim_ids = unique_ids(claims, "claims", errors)
    unsupported_material_claims = 0
    referenced_material_claims = 0
    for index, claim in enumerate(claims):
        require_fields(claim, ["id", "text", "status", "limitations"], f"claims[{index}]", errors)
        refs = claim.get("source_refs", [])
        bad_refs = sorted(set(refs) - source_ids)
        if bad_refs:
            errors.append(f"claims[{index}] unknown source refs: {', '.join(bad_refs)}")
        if claim.get("material") is True:
            if claim.get("status") == "supported" and refs:
                referenced_material_claims += 1
            else:
                unsupported_material_claims += 1
    if isinstance(position, dict):
        bad_rtb = sorted(set(position.get("reasons_to_believe", [])) - claim_ids)
        if bad_rtb:
            errors.append("position has unknown reasons_to_believe: " + ", ".join(bad_rtb))

    tests = payload.get("tests", [])
    if not isinstance(tests, list):
        errors.append("tests must be a list")
        tests = []
    test_types: set[str] = set()
    test_statuses: list[str] = []
    for index, test in enumerate(tests):
        require_fields(test, ["type", "method", "sample", "threshold", "owner", "status"], f"tests[{index}]", errors)
        test_types.add(str(test.get("type", "")))
        test_statuses.append(str(test.get("status", "")))
    missing_tests = sorted(REQUIRED_TESTS - test_types)
    if missing_tests:
        errors.append("missing required tests: " + ", ".join(missing_tests))

    governance = payload.get("governance")
    require_fields(
        governance,
        ["brand_owner", "customer_reviewer", "legal_commercial_reviewer", "validation_state", "decision_log"],
        "governance",
        errors,
    )
    if isinstance(governance, dict) and governance.get("publish_approved") is True:
        guardrails.append("ENGINE_CANNOT_GRANT_OR_VERIFY_PUBLICATION_APPROVAL")

    if errors:
        state = "NOT_READY"
        next_action = "resolve_errors_and_rerun"
    elif unsupported_material_claims or missing_evidence_types or "failed" in test_statuses:
        state = "HYPOTHESIS_READY"
        next_action = "close_evidence_or_test_gaps"
    elif test_statuses and all(status == "passed" for status in test_statuses) and governance.get("validation_state") == "passed":
        state = "VALIDATED_FOR_PILOT_REVIEW"
        next_action = "obtain_human_pilot_approval"
    else:
        state = "READY_FOR_MARKET_TEST"
        next_action = "run_owner_approved_market_tests"

    result = {
        "state": state,
        "errors": errors,
        "warnings": warnings,
        "guardrails": guardrails,
        "metrics": {
            "source_count": len(evidence),
            "active_source_count": active_source_count,
            "evidence_type_coverage": sorted(evidence_types),
            "territory_count": len(territories),
            "territory_scores": territory_scores,
            "material_claim_count": sum(1 for claim in claims if claim.get("material") is True),
            "referenced_material_claim_count": referenced_material_claims,
            "unsupported_material_claim_count": unsupported_material_claims,
            "test_type_coverage": sorted(test_types),
            "unresolved_material_conflict_count": unresolved_material_conflicts,
        },
        "next_action": next_action,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: evaluate_positioning_pack.py INPUT.json", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))

