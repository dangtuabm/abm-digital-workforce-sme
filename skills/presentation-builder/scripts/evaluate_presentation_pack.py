#!/usr/bin/env python3
"""Deterministic readiness gate for a Presentation Production & QA Pack.

Reads one local JSON file. It does not open decks, URLs or assets; browse;
call APIs; purchase; upload; present; publish; deliver; or grant approval.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


ALLOWED_MODES = {"executive_decision", "pitch", "training", "report", "keynote", "workshop"}
ALLOWED_OUTPUTS = {"pptx", "pdf", "images", "html"}
REQUIRED_TESTS = {
    "narrative_recall", "claim_trace", "slide_integrity", "visual_comprehension",
    "accessibility_readability", "timing_rehearsal", "decision_action",
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
    guardrails = ["HUMAN_APPROVAL_REQUIRED_BEFORE_PRESENT_SEND_PUBLISH_OR_DELIVER"]

    contract = payload.get("contract")
    require_fields(contract, [
        "id", "mode", "use", "objective", "decision_or_cta", "presenter",
        "primary_audience", "channel", "duration_minutes", "language", "source_format",
        "output_format", "aspect_ratio", "slide_count_min", "slide_count_max", "naming_rule",
        "brand_template", "accessibility_rule", "classification", "owner", "reviewer",
        "approval_route", "status",
    ], "contract", errors)
    mode = str(contract.get("mode", "")) if isinstance(contract, dict) else ""
    output_format = str(contract.get("output_format", "")) if isinstance(contract, dict) else ""
    if mode not in ALLOWED_MODES:
        errors.append("contract.mode is not supported")
    if output_format not in ALLOWED_OUTPUTS:
        errors.append("contract.output_format is not supported")
    min_count = int(contract.get("slide_count_min", 0) or 0) if isinstance(contract, dict) else 0
    max_count = int(contract.get("slide_count_max", 0) or 0) if isinstance(contract, dict) else 0
    if min_count < 1 or max_count < min_count:
        errors.append("contract slide count range is invalid")

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
        require_fields(audience, ["id", "role", "name", "knowledge", "belief", "concern", "need", "desired_action", "accessibility"], f"audiences[{index}]", errors)
    if audiences and not any(audience.get("role") == "primary" for audience in audiences):
        errors.append("audiences must contain a primary audience")

    claims = payload.get("claims", [])
    if not isinstance(claims, list) or not claims:
        errors.append("claims must be a non-empty list")
        claims = []
    claim_ids = unique_ids(claims, "claims", errors)
    material_claims = referenced_material_claims = unsupported_material_claims = 0
    for index, claim in enumerate(claims):
        require_fields(claim, ["id", "text", "label", "status", "qualifier"], f"claims[{index}]", errors)
        refs = claim.get("source_refs", [])
        bad_refs = sorted(set(refs) - source_ids)
        if bad_refs:
            errors.append(f"claims[{index}] unknown source refs: {', '.join(bad_refs)}")
        if claim.get("material") is True:
            material_claims += 1
            if claim.get("status") == "supported" and refs:
                referenced_material_claims += 1
            else:
                unsupported_material_claims += 1

    assets = payload.get("assets", [])
    if not isinstance(assets, list):
        errors.append("assets must be a list")
        assets = []
    asset_ids = unique_ids(assets, "assets", errors)
    unlicensed_assets = 0
    for index, asset in enumerate(assets):
        require_fields(asset, ["id", "type", "origin", "owner", "license", "credit", "status"], f"assets[{index}]", errors)
        if asset.get("authorized") is not True or asset.get("status") != "approved":
            unlicensed_assets += 1

    require_fields(payload.get("journey"), ["before", "after", "primary_objection", "decision_path"], "journey", errors)
    blueprint = payload.get("blueprint")
    require_fields(blueprint, ["one_sentence_promise", "opening_tension", "sections", "decision_or_cta", "close", "slide_budget", "pace_rule"], "blueprint", errors)
    if isinstance(blueprint, dict):
        if not 1 <= len(blueprint.get("sections", [])) <= 7:
            errors.append("blueprint.sections must contain 1 to 7 sections")
        if int(blueprint.get("slide_budget", 0) or 0) < min_count or int(blueprint.get("slide_budget", 0) or 0) > max_count:
            errors.append("blueprint.slide_budget is outside contract range")

    require_fields(payload.get("visual_system"), [
        "canvas", "grid", "master_layout", "fonts_fallback", "type_scale", "palette_contrast",
        "spacing", "image_rule", "chart_table_rule", "reading_order", "alt_summary_rule",
    ], "visual_system", errors)

    slides = payload.get("slides", [])
    if not isinstance(slides, list) or not slides:
        errors.append("slides must be a non-empty list")
        slides = []
    slide_ids = unique_ids(slides, "slides", errors)
    orders: list[int] = []
    for index, slide in enumerate(slides):
        require_fields(slide, [
            "id", "order", "section", "function", "message_title", "literal_copy", "layout",
            "transition", "speaker_notes", "timing_seconds",
        ], f"slides[{index}]", errors)
        require_list_keys(slide, ["claim_refs", "asset_refs"], f"slides[{index}]", errors)
        orders.append(int(slide.get("order", 0) or 0))
        bad_claims = sorted(set(slide.get("claim_refs", [])) - claim_ids)
        bad_assets = sorted(set(slide.get("asset_refs", [])) - asset_ids)
        if bad_claims:
            errors.append(f"slides[{index}] unknown claim refs: {', '.join(bad_claims)}")
        if bad_assets:
            errors.append(f"slides[{index}] unknown asset refs: {', '.join(bad_assets)}")
    expected_orders = list(range(1, len(slides) + 1))
    if orders != expected_orders:
        errors.append("slides.order must be sequential and match list order")
    if slides and not min_count <= len(slides) <= max_count:
        errors.append("slide count is outside contract range")

    build = payload.get("build")
    require_fields(build, [
        "tool_version", "template_version", "input_hash", "output_hash", "source_deck",
        "render_package", "contact_sheet", "manifest_version", "slide_count",
    ], "build", errors)
    render_defects = 0
    if isinstance(build, dict):
        if int(build.get("slide_count", 0) or 0) != len(slides):
            errors.append("build.slide_count must equal slides length")
        if int(build.get("missing_count", 0) or 0) != 0:
            render_defects += int(build.get("missing_count", 0) or 0)
        if int(build.get("extra_count", 0) or 0) != 0:
            render_defects += int(build.get("extra_count", 0) or 0)
        if build.get("font_media_links_ok") is not True:
            render_defects += 1

    renders = payload.get("renders", [])
    if not isinstance(renders, list) or len(renders) != len(slides):
        errors.append("renders must contain exactly one item per slide")
        renders = []
    render_slide_ids: set[str] = set()
    for index, render in enumerate(renders):
        require_fields(render, ["slide_id", "order", "file", "aspect_ratio", "width", "height", "hash", "qa_status"], f"renders[{index}]", errors)
        render_slide_ids.add(str(render.get("slide_id", "")))
        if render.get("qa_status") != "passed":
            render_defects += 1
        if render.get("aspect_ratio") != contract.get("aspect_ratio"):
            render_defects += 1
    if renders and render_slide_ids != slide_ids:
        errors.append("renders slide_id set must equal slides id set")

    tests = payload.get("tests", [])
    if not isinstance(tests, list):
        errors.append("tests must be a list")
        tests = []
    test_types: set[str] = set()
    test_statuses: list[str] = []
    for index, test in enumerate(tests):
        require_fields(test, ["type", "method", "sample", "threshold", "reviewer", "status", "evidence"], f"tests[{index}]", errors)
        test_types.add(str(test.get("type", "")))
        test_statuses.append(str(test.get("status", "")))
    missing_tests = sorted(REQUIRED_TESTS - test_types)
    if missing_tests:
        errors.append("missing required tests: " + ", ".join(missing_tests))

    review = payload.get("review")
    require_fields(review, ["content_check", "brand_check", "asset_license_check", "accessibility_check", "render_check", "validation_state"], "review", errors)
    require_list_keys(review, ["required_specialist_reviews", "completed_specialist_reviews"], "review", errors)
    review_gaps: list[str] = []
    missing_specialist_reviews: list[str] = []
    if isinstance(review, dict):
        for field in ["content_check", "brand_check", "asset_license_check", "accessibility_check", "render_check"]:
            if review.get(field) is not True:
                review_gaps.append(field)
        missing_specialist_reviews = sorted(set(review.get("required_specialist_reviews", [])) - set(review.get("completed_specialist_reviews", [])))
        if review.get("delivery_approved") is True:
            guardrails.append("ENGINE_CANNOT_GRANT_OR_VERIFY_DELIVERY_APPROVAL")

    if errors:
        state = "NOT_READY"
        next_action = "resolve_errors_and_rerun"
    elif unsupported_material_claims or unlicensed_assets or render_defects or review_gaps or "failed" in test_statuses:
        state = "RENDER_QA_READY" if slides else "STORYBOARD_READY"
        next_action = "close_claim_asset_render_review_or_test_gaps"
    elif test_statuses and all(status == "passed" for status in test_statuses) and not missing_specialist_reviews and review.get("validation_state") == "passed":
        state = "VALIDATED_FOR_DELIVERY_REVIEW"
        next_action = "obtain_human_delivery_approval"
    else:
        state = "READY_FOR_REHEARSAL"
        next_action = "run_rehearsal_tests_and_required_reviews"

    if missing_specialist_reviews:
        warnings.append("missing specialist reviews: " + ", ".join(missing_specialist_reviews))

    result = {
        "state": state,
        "errors": errors,
        "warnings": warnings,
        "guardrails": guardrails,
        "metrics": {
            "source_count": len(sources), "active_source_count": active_sources,
            "audience_count": len(audience_ids), "material_claim_count": material_claims,
            "referenced_material_claim_count": referenced_material_claims,
            "unsupported_material_claim_count": unsupported_material_claims,
            "asset_count": len(asset_ids), "unlicensed_asset_count": unlicensed_assets,
            "slide_count": len(slide_ids), "render_count": len(renders),
            "render_defect_count": render_defects, "unresolved_material_conflict_count": unresolved_conflicts,
            "test_type_coverage": sorted(test_types), "review_gap_count": len(review_gaps),
        },
        "next_action": next_action,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: evaluate_presentation_pack.py INPUT.json", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
