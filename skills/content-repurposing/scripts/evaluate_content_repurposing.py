#!/usr/bin/env python3
"""Deterministic static gate for a Content Repurposing System Pack."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


TEST_TYPES = {
    "contract_rights_integrity",
    "claim_atom_trace",
    "variant_lineage_fidelity",
    "channel_audience_fit",
    "brand_cta_accessibility",
    "duplicate_distortion_check",
    "approval_release_boundary",
}
REVIEW_TYPES = {
    "SOURCE_OWNER",
    "RIGHTS_PRIVACY",
    "BRAND_EDITORIAL",
    "ACCESSIBILITY",
    "FINAL_RELEASE",
}
VARIANT_STATES = {"DRAFT", "REVIEW_PENDING", "REVIEWED"}
FORBIDDEN_VARIANT_STATES = {"APPROVED", "PUBLISHED", "SENT", "SCHEDULED", "RELEASED"}
FORBIDDEN_VARIANT_FLAGS = {
    "fabricated_claim",
    "changed_meaning",
    "quote_distortion",
    "source_attribution_removed",
    "rights_unknown",
    "contains_restricted_data",
    "deceptive_edit",
    "unauthorized_testimonial",
    "voice_or_likeness_without_consent",
}
FORBIDDEN_AUDIENCE_FIELDS = {
    "protected_traits",
    "private_personal_data",
    "personality_diagnosis",
    "secret_vulnerability",
}


def load_json(path: Path) -> dict[str, Any]:
    with path.open("r", encoding="utf-8-sig") as handle:
        data = json.load(handle)
    if not isinstance(data, dict):
        raise ValueError("Root JSON must be an object")
    return data


def blank(value: Any) -> bool:
    return value is None or value == "" or value == [] or value == {}


def require_fields(obj: dict[str, Any], fields: Iterable[str], label: str, errors: list[str]) -> None:
    for field in fields:
        if field not in obj or blank(obj[field]):
            errors.append(f"{label}: missing {field}")


def unique_ids(items: list[dict[str, Any]], field: str, label: str, errors: list[str]) -> set[str]:
    values = [str(item.get(field, "")).strip() for item in items]
    if any(not value for value in values):
        errors.append(f"{label}: blank {field}")
    duplicates = [value for value, count in Counter(values).items() if value and count > 1]
    if duplicates:
        errors.append(f"{label}: duplicate {field}: {', '.join(sorted(duplicates))}")
    return {value for value in values if value}


def validate_refs(refs: Any, valid: set[str], label: str, field: str, errors: list[str]) -> set[str]:
    if not isinstance(refs, list) or not refs:
        errors.append(f"{label}: {field} must be a non-empty list")
        return set()
    normalized = {str(ref) for ref in refs}
    unknown = sorted(normalized - valid)
    if unknown:
        errors.append(f"{label}: unknown {field}: {', '.join(unknown)}")
    return normalized


def evaluate(data: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    contract = data.get("contract") or {}
    require_fields(
        contract,
        (
            "family_id", "version", "objective", "source_asset_id", "source_canon_ref",
            "rights_record_id", "rights_evidence_ref", "brand_profile_ref", "owner", "final_approver",
            "classification", "retention", "prohibited_actions", "stop_or_escalation", "required_reviews",
        ),
        "contract",
        errors,
    )
    if contract.get("data_authorized") is not True:
        errors.append("contract: data_authorized must be true")

    sources = data.get("sources") or []
    source_ids = unique_ids(sources, "source_id", "sources", errors)
    active_sources: set[str] = set()
    for index, source in enumerate(sources):
        label = f"source[{index}]"
        require_fields(
            source,
            ("source_id", "title", "version", "locator", "owner", "classification", "effective_date"),
            label,
            errors,
        )
        if source.get("active") is True:
            active_sources.add(str(source.get("source_id")))
    if not active_sources:
        errors.append("sources: at least one active source is required")
    for field in ("source_canon_ref", "rights_evidence_ref", "brand_profile_ref"):
        if contract.get(field) not in active_sources:
            errors.append(f"contract: {field} is not active")

    rights = data.get("rights") or []
    rights_ids = unique_ids(rights, "rights_id", "rights", errors)
    valid_rights: set[str] = set()
    rights_by_id: dict[str, dict[str, Any]] = {}
    rights_violation_count = 0
    for index, record in enumerate(rights):
        label = f"rights[{index}]"
        require_fields(
            record,
            (
                "rights_id", "source_id", "status", "evidence_ref", "owner", "usage_scope",
                "allowed_channel_ids", "allowed_formats", "territory", "expiry", "attribution",
                "voice_likeness_consent",
            ),
            label,
            errors,
        )
        rights_id = str(record.get("rights_id", ""))
        rights_by_id[rights_id] = record
        if record.get("source_id") not in active_sources or record.get("evidence_ref") not in active_sources:
            rights_violation_count += 1
            errors.append(f"{label}: source/evidence is not active")
        if record.get("status") != "APPROVED":
            rights_violation_count += 1
            errors.append(f"{label}: status must be APPROVED")
        if record.get("voice_likeness_consent") not in {"CONFIRMED", "NOT_APPLICABLE"}:
            rights_violation_count += 1
            errors.append(f"{label}: voice_likeness_consent is unresolved")
        if not errors or (
            record.get("status") == "APPROVED"
            and record.get("source_id") in active_sources
            and record.get("evidence_ref") in active_sources
        ):
            valid_rights.add(rights_id)
    if contract.get("rights_record_id") not in rights_ids:
        errors.append("contract: unknown rights_record_id")

    source_asset = data.get("source_asset") or {}
    require_fields(
        source_asset,
        (
            "asset_id", "title", "canonical_version", "source_ref", "locator", "owner",
            "asset_type", "language", "transcript_status", "classification",
        ),
        "source_asset",
        errors,
    )
    if source_asset.get("asset_id") != contract.get("source_asset_id"):
        errors.append("source_asset: asset_id does not match contract")
    if source_asset.get("source_ref") not in active_sources:
        errors.append("source_asset: source_ref is not active")
    if source_asset.get("transcript_status") not in {"VERIFIED", "NOT_APPLICABLE"}:
        errors.append("source_asset: transcript_status must be VERIFIED or NOT_APPLICABLE")

    claims = data.get("claims") or []
    claim_ids = unique_ids(claims, "claim_id", "claims", errors)
    prohibited_claim_ids: set[str] = set()
    for index, claim in enumerate(claims):
        label = f"claim[{index}]"
        require_fields(
            claim,
            ("claim_id", "statement", "claim_type", "status", "source_refs", "locator", "context", "owner"),
            label,
            errors,
        )
        if claim.get("status") != "CONFIRMED":
            errors.append(f"{label}: status must be CONFIRMED")
        validate_refs(claim.get("source_refs"), active_sources, label, "source_refs", errors)
        if claim.get("prohibited_for_derivatives") is True:
            prohibited_claim_ids.add(str(claim.get("claim_id")))

    atoms = data.get("atoms") or []
    atom_ids = unique_ids(atoms, "atom_id", "atoms", errors)
    for index, atom in enumerate(atoms):
        label = f"atom[{index}]"
        require_fields(
            atom,
            (
                "atom_id", "atom_type", "content", "claim_ids", "source_refs", "context",
                "transformation_permissions", "owner",
            ),
            label,
            errors,
        )
        validate_refs(atom.get("claim_ids"), claim_ids, label, "claim_ids", errors)
        validate_refs(atom.get("source_refs"), active_sources, label, "source_refs", errors)

    audiences = data.get("audiences") or []
    audience_ids = unique_ids(audiences, "audience_id", "audiences", errors)
    forbidden_audience_count = 0
    for index, audience in enumerate(audiences):
        label = f"audience[{index}]"
        require_fields(
            audience,
            ("audience_id", "segment", "job", "need", "evidence_refs", "owner"),
            label,
            errors,
        )
        validate_refs(audience.get("evidence_refs"), active_sources, label, "evidence_refs", errors)
        for field in FORBIDDEN_AUDIENCE_FIELDS:
            if not blank(audience.get(field)):
                forbidden_audience_count += 1
                errors.append(f"{label}: forbidden audience field {field}")

    channel_briefs = data.get("channel_briefs") or []
    channel_ids = unique_ids(channel_briefs, "channel_id", "channel_briefs", errors)
    briefs_by_id: dict[str, dict[str, Any]] = {}
    for index, brief in enumerate(channel_briefs):
        label = f"channel_brief[{index}]"
        require_fields(
            brief,
            (
                "channel_id", "platform", "objective", "audience_id", "format", "behavior",
                "constraints", "cta_policy", "accessibility", "metric_hypothesis", "owner", "evidence_refs",
            ),
            label,
            errors,
        )
        briefs_by_id[str(brief.get("channel_id", ""))] = brief
        if brief.get("audience_id") not in audience_ids:
            errors.append(f"{label}: unknown audience_id")
        validate_refs(brief.get("evidence_refs"), active_sources, label, "evidence_refs", errors)

    variants = data.get("variants") or []
    variant_ids = unique_ids(variants, "variant_id", "variants", errors)
    covered_channels: set[str] = set()
    forbidden_variant_count = 0
    untraced_variant_count = 0
    unauthorized_release_count = 0
    variant_contents: list[str] = []
    transformation_types: set[str] = set()
    for index, variant in enumerate(variants):
        label = f"variant[{index}]"
        require_fields(
            variant,
            (
                "variant_id", "parent_atom_ids", "claim_ids", "claim_refs", "source_refs", "rights_id",
                "audience_id", "channel_id", "format", "transformation", "angle", "hook", "value",
                "content", "cta", "voice_profile_ref", "attribution", "accessibility", "version",
                "owner", "approval_status",
            ),
            label,
            errors,
        )
        validate_refs(variant.get("parent_atom_ids"), atom_ids, label, "parent_atom_ids", errors)
        variant_claims = validate_refs(variant.get("claim_ids"), claim_ids, label, "claim_ids", errors)
        claim_refs = validate_refs(variant.get("claim_refs"), claim_ids, label, "claim_refs", errors)
        validate_refs(variant.get("source_refs"), active_sources, label, "source_refs", errors)
        if claim_refs != variant_claims or claim_refs & prohibited_claim_ids:
            untraced_variant_count += 1
            errors.append(f"{label}: claim lineage mismatch or prohibited claim")
        channel_id = str(variant.get("channel_id", ""))
        audience_id = str(variant.get("audience_id", ""))
        if channel_id not in channel_ids or audience_id not in audience_ids:
            errors.append(f"{label}: unknown channel_id or audience_id")
        else:
            covered_channels.add(channel_id)
            brief = briefs_by_id[channel_id]
            if brief.get("audience_id") != audience_id or brief.get("format") != variant.get("format"):
                errors.append(f"{label}: does not match channel brief audience/format")
        rights_id = str(variant.get("rights_id", ""))
        record = rights_by_id.get(rights_id)
        if rights_id not in valid_rights or record is None:
            rights_violation_count += 1
            errors.append(f"{label}: invalid rights_id")
        else:
            if channel_id not in {str(item) for item in record.get("allowed_channel_ids", [])}:
                rights_violation_count += 1
                errors.append(f"{label}: channel not allowed by rights")
            if variant.get("format") not in record.get("allowed_formats", []):
                rights_violation_count += 1
                errors.append(f"{label}: format not allowed by rights")
            if variant.get("attribution") != record.get("attribution"):
                rights_violation_count += 1
                errors.append(f"{label}: attribution does not match rights")
        if variant.get("voice_profile_ref") not in active_sources:
            errors.append(f"{label}: voice_profile_ref is not active")
        approval = str(variant.get("approval_status", ""))
        if approval in FORBIDDEN_VARIANT_STATES:
            unauthorized_release_count += 1
            errors.append(f"{label}: forbidden approval/release state {approval}")
        elif approval not in VARIANT_STATES:
            errors.append(f"{label}: invalid approval_status")
        for flag in FORBIDDEN_VARIANT_FLAGS:
            if variant.get(flag) is True:
                forbidden_variant_count += 1
                errors.append(f"{label}: forbidden variant flag {flag}")
        content = str(variant.get("content", "")).strip()
        if content:
            variant_contents.append(content)
        transformation_types.add(str(variant.get("transformation", "")))
    missing_channels = sorted(channel_ids - covered_channels)
    if missing_channels:
        errors.append(f"variants: channel briefs not covered: {', '.join(missing_channels)}")
    duplicate_contents = sum(count - 1 for count in Counter(variant_contents).values() if count > 1)
    if duplicate_contents:
        errors.append(f"variants: exact duplicate contents found: {duplicate_contents}")

    release_sequence = data.get("release_sequence") or []
    release_ids = unique_ids(release_sequence, "release_id", "release_sequence", errors)
    sequenced_variants: set[str] = set()
    for index, item in enumerate(release_sequence):
        label = f"release[{index}]"
        require_fields(
            item,
            ("release_id", "order", "variant_id", "dependency", "embargo", "fallback", "owner"),
            label,
            errors,
        )
        if item.get("variant_id") not in variant_ids:
            errors.append(f"{label}: unknown variant_id")
        else:
            sequenced_variants.add(str(item.get("variant_id")))
        try:
            if int(item.get("order")) < 1:
                errors.append(f"{label}: order must be positive")
        except (TypeError, ValueError):
            errors.append(f"{label}: order must be an integer")
    missing_sequence = sorted(variant_ids - sequenced_variants)
    if missing_sequence:
        errors.append(f"release_sequence: variants not covered: {', '.join(missing_sequence)}")

    risks = data.get("risks") or []
    risk_ids = unique_ids(risks, "risk_id", "risks", errors)
    for index, risk in enumerate(risks):
        label = f"risk[{index}]"
        require_fields(
            risk,
            ("risk_id", "type", "trigger", "harm", "prevention", "stop_or_rollback", "owner", "evidence_refs"),
            label,
            errors,
        )
        validate_refs(risk.get("evidence_refs"), active_sources, label, "evidence_refs", errors)

    tests = data.get("tests") or []
    present_test_types = {str(item.get("test_type", "")) for item in tests}
    missing_tests = sorted(TEST_TYPES - present_test_types)
    if missing_tests:
        errors.append(f"tests: missing types: {', '.join(missing_tests)}")
    for index, test in enumerate(tests):
        require_fields(test, ("test_type", "evidence", "reviewer", "date"), f"test[{index}]", errors)
        if test.get("passed") is not True:
            errors.append(f"test[{index}]: passed must be true")

    reviews = data.get("reviews") or []
    present_reviews = {str(item.get("review_type", "")) for item in reviews if item.get("required") is True}
    missing_reviews = sorted(REVIEW_TYPES - present_reviews)
    if missing_reviews:
        errors.append(f"reviews: missing required types: {', '.join(missing_reviews)}")
    for index, review in enumerate(reviews):
        label = f"review[{index}]"
        require_fields(review, ("review_type", "reviewer", "status"), label, errors)
        if review.get("required") is True and review.get("status") not in {"PASS", "PENDING"}:
            errors.append(f"{label}: invalid required review status")
        if review.get("status") == "PASS" and blank(review.get("evidence_ref")):
            errors.append(f"{label}: PASS requires evidence_ref")

    final_release_pass = any(
        review.get("review_type") == "FINAL_RELEASE"
        and review.get("required") is True
        and review.get("status") == "PASS"
        and not blank(review.get("evidence_ref"))
        for review in reviews
    )
    required_reviews_pass = bool(reviews) and all(
        review.get("status") == "PASS" for review in reviews if review.get("required") is True
    )
    if errors:
        state = "NOT_READY"
    elif required_reviews_pass and final_release_pass:
        state = "READY_FOR_AUTHORIZED_RELEASE"
        warnings.append("Human release and channel execution remain outside the engine")
    else:
        state = "READY_FOR_CONTENT_REVIEW"
        warnings.append("Required human reviews remain; the engine does not approve, schedule, post, or publish")

    return {
        "family_id": contract.get("family_id", ""),
        "state": state,
        "metrics": {
            "sources": len(source_ids),
            "active_sources": len(active_sources),
            "rights_records": len(rights_ids),
            "claims": len(claim_ids),
            "atoms": len(atom_ids),
            "audiences": len(audience_ids),
            "channel_briefs": len(channel_ids),
            "variants": len(variant_ids),
            "transformation_types": len({item for item in transformation_types if item}),
            "release_steps": len(release_ids),
            "risks": len(risk_ids),
            "test_types": len(present_test_types & TEST_TYPES),
            "forbidden_audience_count": forbidden_audience_count,
            "forbidden_variant_count": forbidden_variant_count,
            "untraced_variant_count": untraced_variant_count,
            "rights_violation_count": rights_violation_count,
            "duplicate_content_count": duplicate_contents,
            "unauthorized_release_count": unauthorized_release_count,
            "critical_defects": len(errors),
        },
        "errors": errors,
        "warnings": warnings,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    result = evaluate(load_json(args.input))
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    print(rendered)
    return 0 if result["state"] != "NOT_READY" else 1


if __name__ == "__main__":
    raise SystemExit(main())
