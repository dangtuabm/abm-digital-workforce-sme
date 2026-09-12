#!/usr/bin/env python3
"""Deterministic gate for an Audience Adaptation & Fidelity Pack.

Reads one local JSON file. It does not open sources or URLs, enrich profiles,
call APIs, target recipients, send, publish, release, or grant approval.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


REQUIRED_TESTS = {
    "semantic_fidelity", "material_coverage", "action_authority",
    "audience_comprehension", "tone_trust", "accessibility_channel",
    "cross_variant_consistency",
}
ALLOWED_INVARIANT_TYPES = {
    "fact", "number_date", "decision", "scope", "defined_term",
    "risk", "qualifier", "commitment", "authority", "core_outcome",
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


def require_list_keys(obj: Any, fields: list[str], path: str, errors: list[str]) -> None:
    if not isinstance(obj, dict):
        return
    for field in fields:
        if field not in obj or not isinstance(obj.get(field), list):
            errors.append(f"missing or invalid {path}.{field}")


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
    guardrails = ["HUMAN_APPROVAL_REQUIRED_BEFORE_TARGET_SEND_PUBLISH_OR_RELEASE"]

    contract = payload.get("contract")
    require_fields(contract, [
        "id", "source_message_id", "source_version", "source_authority",
        "core_outcome", "audience_ids", "channels", "languages",
        "allowed_transforms", "prohibited_transforms", "classification",
        "owner", "reviewer", "approval_route", "status",
    ], "contract", errors)
    require_list_keys(contract, ["audience_ids", "channels", "languages", "allowed_transforms", "prohibited_transforms"], "contract", errors)

    sources = payload.get("sources", [])
    if not isinstance(sources, list) or not sources:
        errors.append("sources must be a non-empty list")
        sources = []
    source_ids = unique_ids(sources, "sources", errors)
    active_sources = 0
    for index, source in enumerate(sources):
        require_fields(source, ["id", "title", "version", "date", "owner", "authority", "locator", "classification", "status"], f"sources[{index}]", errors)
        if source.get("authorized") is not True:
            errors.append(f"sources[{index}] is not authorized")
        if source.get("status") == "active":
            active_sources += 1

    conflicts = payload.get("conflicts", [])
    if not isinstance(conflicts, list):
        errors.append("conflicts must be a list")
        conflicts = []
    unresolved_conflicts = 0
    for index, conflict in enumerate(conflicts):
        if conflict.get("material") is True and conflict.get("status") not in {"resolved", "accepted"}:
            unresolved_conflicts += 1
            errors.append(f"conflicts[{index}] material conflict is unresolved")

    audiences = payload.get("audiences", [])
    if not isinstance(audiences, list) or not audiences:
        errors.append("audiences must be a non-empty list")
        audiences = []
    audience_ids = unique_ids(audiences, "audiences", errors)
    for index, audience in enumerate(audiences):
        require_fields(audience, [
            "id", "role", "name", "power_accountability", "domain_literacy",
            "prior_knowledge", "information_need", "concern", "desired_action",
            "channel", "language_accessibility", "disclosure", "confidence",
        ], f"audiences[{index}]", errors)
        require_list_keys(audience, ["evidence_refs"], f"audiences[{index}]", errors)
    contract_audience_ids = set(contract.get("audience_ids", [])) if isinstance(contract, dict) else set()
    if contract_audience_ids != audience_ids:
        errors.append("contract.audience_ids must equal audiences id set")

    evidence = payload.get("audience_evidence", [])
    if not isinstance(evidence, list) or not evidence:
        errors.append("audience_evidence must be a non-empty list")
        evidence = []
    evidence_ids = unique_ids(evidence, "audience_evidence", errors)
    for index, item in enumerate(evidence):
        require_fields(item, ["id", "audience_id", "type", "statement", "source_ref", "date", "confidence", "status"], f"audience_evidence[{index}]", errors)
        if item.get("audience_id") not in audience_ids:
            errors.append(f"audience_evidence[{index}] unknown audience_id")
        if item.get("source_ref") not in source_ids:
            errors.append(f"audience_evidence[{index}] unknown source_ref")
        if item.get("authorized") is not True:
            errors.append(f"audience_evidence[{index}] is not authorized")
    for index, audience in enumerate(audiences):
        bad_refs = sorted(set(audience.get("evidence_refs", [])) - evidence_ids)
        if bad_refs:
            errors.append(f"audiences[{index}] unknown evidence refs: {', '.join(bad_refs)}")
        if not audience.get("evidence_refs"):
            errors.append(f"audiences[{index}] has no evidence refs")

    invariants = payload.get("invariants", [])
    if not isinstance(invariants, list) or not invariants:
        errors.append("invariants must be a non-empty list")
        invariants = []
    invariant_ids = unique_ids(invariants, "invariants", errors)
    material_invariants = supported_material_invariants = unsupported_material_invariants = 0
    required_by_audience: dict[str, set[str]] = {audience_id: set() for audience_id in audience_ids}
    for index, invariant in enumerate(invariants):
        require_fields(invariant, ["id", "type", "text", "status", "qualifier"], f"invariants[{index}]", errors)
        require_list_keys(invariant, ["source_refs", "required_for"], f"invariants[{index}]", errors)
        if invariant.get("type") not in ALLOWED_INVARIANT_TYPES:
            errors.append(f"invariants[{index}] unsupported type")
        refs = invariant.get("source_refs", [])
        bad_refs = sorted(set(refs) - source_ids)
        if bad_refs:
            errors.append(f"invariants[{index}] unknown source refs: {', '.join(bad_refs)}")
        required_for = set(invariant.get("required_for", []))
        targets = audience_ids if "ALL" in required_for else required_for
        bad_targets = sorted(set(targets) - audience_ids)
        if bad_targets:
            errors.append(f"invariants[{index}] unknown required audience ids: {', '.join(bad_targets)}")
        for audience_id in set(targets) & audience_ids:
            required_by_audience[audience_id].add(str(invariant.get("id", "")))
        if invariant.get("material") is True:
            material_invariants += 1
            if invariant.get("status") == "supported" and refs:
                supported_material_invariants += 1
            else:
                unsupported_material_invariants += 1

    actions = payload.get("actions", [])
    if not isinstance(actions, list) or not actions:
        errors.append("actions must be a non-empty list")
        actions = []
    action_ids = unique_ids(actions, "actions", errors)
    for index, action in enumerate(actions):
        require_fields(action, ["id", "owner", "authority", "deliverable", "deadline", "status"], f"actions[{index}]", errors)
        require_list_keys(action, ["required_for"], f"actions[{index}]", errors)
        bad_targets = sorted(set(action.get("required_for", [])) - audience_ids)
        if bad_targets:
            errors.append(f"actions[{index}] unknown audience ids: {', '.join(bad_targets)}")

    plans = payload.get("plans", [])
    if not isinstance(plans, list) or not plans:
        errors.append("plans must be a non-empty list")
        plans = []
    planned_audiences: set[str] = set()
    for index, plan in enumerate(plans):
        require_fields(plan, [
            "audience_id", "must_know", "emphasize", "explain", "defer_appendix",
            "depth_tone", "terminology_examples", "disclosure", "reviewer",
        ], f"plans[{index}]", errors)
        require_list_keys(plan, ["action_refs"], f"plans[{index}]", errors)
        audience_id = str(plan.get("audience_id", ""))
        planned_audiences.add(audience_id)
        if audience_id not in audience_ids:
            errors.append(f"plans[{index}] unknown audience_id")
        bad_actions = sorted(set(plan.get("action_refs", [])) - action_ids)
        if bad_actions:
            errors.append(f"plans[{index}] unknown action refs: {', '.join(bad_actions)}")
    if planned_audiences != audience_ids:
        errors.append("plans must cover every audience exactly at least once")

    variants = payload.get("variants", [])
    if not isinstance(variants, list) or not variants:
        errors.append("variants must be a non-empty list")
        variants = []
    variant_ids = unique_ids(variants, "variants", errors)
    variant_audiences: set[str] = set()
    coverage_gaps = 0
    for index, variant in enumerate(variants):
        require_fields(variant, ["id", "audience_id", "channel", "language", "status", "title_or_subject"], f"variants[{index}]", errors)
        sections = variant.get("sections", [])
        if not isinstance(sections, list) or not sections:
            errors.append(f"variants[{index}].sections must be non-empty")
            sections = []
        audience_id = str(variant.get("audience_id", ""))
        variant_audiences.add(audience_id)
        if audience_id not in audience_ids:
            errors.append(f"variants[{index}] unknown audience_id")
        covered_invariants: set[str] = set()
        for section_index, section in enumerate(sections):
            require_fields(section, ["id", "text", "adaptation_rationale"], f"variants[{index}].sections[{section_index}]", errors)
            require_list_keys(section, ["invariant_refs", "action_refs"], f"variants[{index}].sections[{section_index}]", errors)
            invariant_refs = set(section.get("invariant_refs", []))
            action_refs = set(section.get("action_refs", []))
            bad_invariants = sorted(invariant_refs - invariant_ids)
            bad_actions = sorted(action_refs - action_ids)
            if bad_invariants:
                errors.append(f"variants[{index}].sections[{section_index}] unknown invariant refs: {', '.join(bad_invariants)}")
            if bad_actions:
                errors.append(f"variants[{index}].sections[{section_index}] unknown action refs: {', '.join(bad_actions)}")
            covered_invariants |= invariant_refs
        missing_required = sorted(required_by_audience.get(audience_id, set()) - covered_invariants)
        if missing_required:
            coverage_gaps += len(missing_required)
            warnings.append(f"variant {variant.get('id')} missing required invariants: {', '.join(missing_required)}")
    if variant_audiences != audience_ids:
        errors.append("variants must cover every audience")

    fidelity_checks = payload.get("fidelity_checks", [])
    if not isinstance(fidelity_checks, list):
        errors.append("fidelity_checks must be a list")
        fidelity_checks = []
    checked_variant_ids: set[str] = set()
    variant_defects = 0
    for index, check in enumerate(fidelity_checks):
        require_fields(check, ["variant_id", "status", "evidence"], f"fidelity_checks[{index}]", errors)
        checked_variant_ids.add(str(check.get("variant_id", "")))
        for field in [
            "facts_preserved", "qualifiers_preserved", "no_new_material_claims",
            "no_contradictions", "disclosure_ok", "stereotype_sensitive_inference_free",
            "accessibility_ok",
        ]:
            if check.get(field) is not True:
                variant_defects += 1
        if check.get("status") != "passed":
            variant_defects += 1
    if checked_variant_ids != variant_ids:
        errors.append("fidelity_checks must cover every variant exactly at least once")

    tests = payload.get("tests", [])
    if not isinstance(tests, list):
        errors.append("tests must be a list")
        tests = []
    test_types: set[str] = set()
    test_statuses: list[str] = []
    for index, test in enumerate(tests):
        require_fields(test, ["type", "method", "artifact_version", "sample", "threshold", "reviewer", "status", "evidence"], f"tests[{index}]", errors)
        test_types.add(str(test.get("type", "")))
        test_statuses.append(str(test.get("status", "")))
    missing_tests = sorted(REQUIRED_TESTS - test_types)
    if missing_tests:
        errors.append("missing required tests: " + ", ".join(missing_tests))

    review = payload.get("review")
    require_fields(review, [
        "source_canon_check", "audience_evidence_check", "disclosure_check",
        "fairness_privacy_check", "accessibility_check", "cross_variant_check",
        "validation_state",
    ], "review", errors)
    require_list_keys(review, ["required_specialist_reviews", "completed_specialist_reviews"], "review", errors)
    review_gaps: list[str] = []
    missing_specialist_reviews: list[str] = []
    if isinstance(review, dict):
        for field in [
            "source_canon_check", "audience_evidence_check", "disclosure_check",
            "fairness_privacy_check", "accessibility_check", "cross_variant_check",
        ]:
            if review.get(field) is not True:
                review_gaps.append(field)
        missing_specialist_reviews = sorted(set(review.get("required_specialist_reviews", [])) - set(review.get("completed_specialist_reviews", [])))
        if review.get("release_approved") is True:
            guardrails.append("ENGINE_CANNOT_GRANT_OR_VERIFY_RELEASE_APPROVAL")

    if errors:
        state = "NOT_READY"
        next_action = "resolve_errors_and_rerun"
    elif unsupported_material_invariants or coverage_gaps or variant_defects or review_gaps or "failed" in test_statuses:
        state = "VARIANTS_READY" if variants else "CANON_LOCKED"
        next_action = "close_invariant_coverage_fidelity_review_or_test_gaps"
    elif test_statuses and all(status == "passed" for status in test_statuses) and not missing_specialist_reviews and review.get("validation_state") == "passed":
        state = "VALIDATED_FOR_RELEASE_REVIEW"
        next_action = "obtain_human_release_approval"
    else:
        state = "READY_FOR_AUDIENCE_REVIEW"
        next_action = "run_reader_tests_and_required_reviews"

    if missing_specialist_reviews:
        warnings.append("missing specialist reviews: " + ", ".join(missing_specialist_reviews))

    result = {
        "state": state,
        "errors": errors,
        "warnings": warnings,
        "guardrails": guardrails,
        "metrics": {
            "source_count": len(sources), "active_source_count": active_sources,
            "audience_count": len(audience_ids), "audience_evidence_count": len(evidence_ids),
            "material_invariant_count": material_invariants,
            "supported_material_invariant_count": supported_material_invariants,
            "unsupported_material_invariant_count": unsupported_material_invariants,
            "action_count": len(action_ids), "variant_count": len(variant_ids),
            "invariant_coverage_gap_count": coverage_gaps,
            "variant_defect_count": variant_defects,
            "unresolved_material_conflict_count": unresolved_conflicts,
            "test_type_coverage": sorted(test_types), "review_gap_count": len(review_gaps),
        },
        "next_action": next_action,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: evaluate_audience_adaptation.py INPUT.json", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
