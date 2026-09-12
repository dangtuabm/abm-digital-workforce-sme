#!/usr/bin/env python3
"""Deterministic static gate for an Evidence Case Study Dossier."""

from __future__ import annotations

import argparse
import json
import math
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


TEST_TYPES = {
    "contract_consent_integrity", "metric_baseline_delta", "intervention_trace",
    "attribution_confounder", "quote_asset_rights", "version_claim_consistency",
    "approval_publication_boundary",
}
REVIEW_TYPES = {
    "DATA_OWNER", "SUBJECT_CONSENT", "DOMAIN_MEASUREMENT",
    "BRAND_LEGAL_PRIVACY", "FINAL_PUBLICATION",
}
VERSION_TYPES = {"SOCIAL_SHORT", "WEBSITE_LONG", "ONE_PAGER"}
ATTRIBUTION_RANK = {"DESCRIPTIVE": 1, "CONTRIBUTION": 2, "CAUSAL": 3}
VERSION_STATES = {"DRAFT", "REVIEW_PENDING", "REVIEWED"}
FORBIDDEN_VERSION_STATES = {"APPROVED", "PUBLISHED", "SIGNED", "SENT"}
FORBIDDEN_CLAIM_FLAGS = {
    "fabricated_evidence", "causal_overclaim", "cherry_picked_window",
    "denominator_changed", "limitation_omitted", "unauthorized_testimonial",
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


def validate_refs(refs: Any, valid: set[str], label: str, field: str, errors: list[str], allow_empty: bool = False) -> set[str]:
    if not isinstance(refs, list) or (not refs and not allow_empty):
        errors.append(f"{label}: {field} must be {'a list' if allow_empty else 'a non-empty list'}")
        return set()
    normalized = {str(ref) for ref in refs}
    unknown = sorted(normalized - valid)
    if unknown:
        errors.append(f"{label}: unknown {field}: {', '.join(unknown)}")
    return normalized


def number(value: Any) -> float | None:
    if isinstance(value, bool):
        return None
    try:
        result = float(value)
    except (TypeError, ValueError):
        return None
    return result if math.isfinite(result) else None


def evaluate(data: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    contract = data.get("contract") or {}
    require_fields(
        contract,
        (
            "case_id", "version", "purpose", "subject", "subject_display_mode", "audiences",
            "channels", "owner", "final_approver", "classification", "retention",
            "consent_id", "consent_evidence_ref", "prohibited_actions", "stop_or_escalation",
            "required_reviews",
        ),
        "contract", errors,
    )
    if contract.get("data_authorized") is not True:
        errors.append("contract: data_authorized must be true")

    sources = data.get("sources") or []
    source_ids = unique_ids(sources, "source_id", "sources", errors)
    active_sources: set[str] = set()
    for index, source in enumerate(sources):
        label = f"source[{index}]"
        require_fields(source, ("source_id", "title", "version", "locator", "owner", "classification", "effective_date"), label, errors)
        if source.get("active") is True:
            active_sources.add(str(source.get("source_id")))
    if not active_sources:
        errors.append("sources: at least one active source is required")
    if contract.get("consent_evidence_ref") not in active_sources:
        errors.append("contract: consent_evidence_ref is not active")

    consent = data.get("consent") or {}
    require_fields(
        consent,
        (
            "consent_id", "status", "evidence_ref", "subject_display_mode", "allowed_quote_ids",
            "allowed_asset_ids", "allowed_channels", "allowed_formats", "expiry", "revocation_route", "owner",
        ),
        "consent", errors,
    )
    consent_valid = True
    if consent.get("consent_id") != contract.get("consent_id"):
        errors.append("consent: consent_id does not match contract")
        consent_valid = False
    if consent.get("status") != "APPROVED":
        errors.append("consent: status must be APPROVED")
        consent_valid = False
    if consent.get("evidence_ref") not in active_sources:
        errors.append("consent: evidence_ref is not active")
        consent_valid = False
    if consent.get("subject_display_mode") != contract.get("subject_display_mode"):
        errors.append("consent: subject_display_mode does not match contract")
        consent_valid = False

    measurement = data.get("measurement_contract") or {}
    require_fields(
        measurement,
        (
            "measurement_id", "attribution_level", "comparison_basis", "baseline_window",
            "outcome_window", "sampling_rule", "exclusions", "missing_data_rule", "currency_rule",
            "rounding_rule", "domain_owner", "source_refs",
        ),
        "measurement_contract", errors,
    )
    attribution_level = str(measurement.get("attribution_level", ""))
    if attribution_level not in ATTRIBUTION_RANK:
        errors.append("measurement_contract: invalid attribution_level")
    validate_refs(measurement.get("source_refs"), active_sources, "measurement_contract", "source_refs", errors)
    if attribution_level == "CAUSAL" and measurement.get("causal_design_approved") is not True:
        errors.append("measurement_contract: CAUSAL requires approved design evidence")

    metrics = data.get("metrics") or []
    metric_ids = unique_ids(metrics, "metric_id", "metrics", errors)
    calculation_defect_count = 0
    for index, metric in enumerate(metrics):
        label = f"metric[{index}]"
        require_fields(
            metric,
            (
                "metric_id", "name", "definition", "unit", "direction", "formula", "delta_type",
                "baseline_value", "outcome_value", "reported_delta", "baseline_window", "outcome_window",
                "sample_size", "exclusions", "source_refs", "owner", "validation_status",
            ),
            label, errors,
        )
        validate_refs(metric.get("source_refs"), active_sources, label, "source_refs", errors)
        baseline = number(metric.get("baseline_value"))
        outcome = number(metric.get("outcome_value"))
        reported = number(metric.get("reported_delta"))
        if baseline is None or outcome is None or reported is None:
            calculation_defect_count += 1
            errors.append(f"{label}: values must be finite numbers")
            continue
        delta_type = metric.get("delta_type")
        if delta_type == "ABSOLUTE":
            expected = outcome - baseline
        elif delta_type == "RELATIVE":
            if baseline == 0:
                calculation_defect_count += 1
                errors.append(f"{label}: relative delta cannot use zero baseline")
                continue
            expected = (outcome - baseline) / baseline
        else:
            calculation_defect_count += 1
            errors.append(f"{label}: invalid delta_type")
            continue
        if not math.isclose(expected, reported, rel_tol=1e-9, abs_tol=1e-9):
            calculation_defect_count += 1
            errors.append(f"{label}: reported_delta does not match calculation")
        if metric.get("baseline_window") != measurement.get("baseline_window") or metric.get("outcome_window") != measurement.get("outcome_window"):
            errors.append(f"{label}: windows do not match measurement contract")
        if metric.get("validation_status") != "VALIDATED":
            errors.append(f"{label}: validation_status must be VALIDATED")

    interventions = data.get("interventions") or []
    intervention_ids = unique_ids(interventions, "intervention_id", "interventions", errors)
    for index, item in enumerate(interventions):
        label = f"intervention[{index}]"
        require_fields(item, ("intervention_id", "what", "owner", "start", "end", "scope", "adoption_evidence", "source_refs"), label, errors)
        validate_refs(item.get("source_refs"), active_sources, label, "source_refs", errors)

    confounders = data.get("confounders") or []
    confounder_ids = unique_ids(confounders, "confounder_id", "confounders", errors)
    if not confounder_ids:
        errors.append("confounders: at least one reviewed confounder is required")
    for index, item in enumerate(confounders):
        label = f"confounder[{index}]"
        require_fields(item, ("confounder_id", "factor", "materiality", "evidence", "treatment", "residual_uncertainty", "owner", "source_refs"), label, errors)
        validate_refs(item.get("source_refs"), active_sources, label, "source_refs", errors)

    claims = data.get("claims") or []
    claim_ids = unique_ids(claims, "claim_id", "claims", errors)
    forbidden_claim_count = 0
    attribution_overclaim_count = 0
    for index, claim in enumerate(claims):
        label = f"claim[{index}]"
        require_fields(
            claim,
            (
                "claim_id", "statement", "claim_type", "source_refs", "metric_ids", "intervention_ids",
                "confounder_ids", "attribution_level", "attribution_language", "confidence", "owner",
            ),
            label, errors,
        )
        validate_refs(claim.get("source_refs"), active_sources, label, "source_refs", errors)
        validate_refs(claim.get("metric_ids"), metric_ids, label, "metric_ids", errors, allow_empty=True)
        validate_refs(claim.get("intervention_ids"), intervention_ids, label, "intervention_ids", errors, allow_empty=True)
        validate_refs(claim.get("confounder_ids"), confounder_ids, label, "confounder_ids", errors)
        level = str(claim.get("attribution_level", ""))
        if level not in ATTRIBUTION_RANK or attribution_level not in ATTRIBUTION_RANK or ATTRIBUTION_RANK.get(level, 99) > ATTRIBUTION_RANK.get(attribution_level, 0):
            attribution_overclaim_count += 1
            errors.append(f"{label}: attribution exceeds measurement contract")
        for flag in FORBIDDEN_CLAIM_FLAGS:
            if claim.get(flag) is True:
                forbidden_claim_count += 1
                errors.append(f"{label}: forbidden claim flag {flag}")

    quotes = data.get("quotes") or []
    quote_ids = unique_ids(quotes, "quote_id", "quotes", errors)
    allowed_quote_ids = {str(item) for item in consent.get("allowed_quote_ids", [])}
    quote_violation_count = 0
    for index, quote in enumerate(quotes):
        label = f"quote[{index}]"
        require_fields(quote, ("quote_id", "text", "locator", "speaker_role", "source_ref", "consent_id", "owner"), label, errors)
        if quote.get("source_ref") not in active_sources or quote.get("consent_id") != consent.get("consent_id") or quote.get("quote_id") not in allowed_quote_ids:
            quote_violation_count += 1
            errors.append(f"{label}: quote source/consent/scope invalid")
        if quote.get("verbatim") is not True or quote.get("paraphrased") is True:
            quote_violation_count += 1
            errors.append(f"{label}: quote must be verbatim and not paraphrased")

    assets = data.get("assets") or []
    asset_ids = unique_ids(assets, "asset_id", "assets", errors)
    allowed_asset_ids = {str(item) for item in consent.get("allowed_asset_ids", [])}
    asset_violation_count = 0
    for index, asset in enumerate(assets):
        label = f"asset[{index}]"
        require_fields(asset, ("asset_id", "asset_type", "locator", "source_ref", "rights_status", "consent_id", "owner"), label, errors)
        if asset.get("source_ref") not in active_sources or asset.get("consent_id") != consent.get("consent_id") or asset.get("asset_id") not in allowed_asset_ids or asset.get("rights_status") != "APPROVED":
            asset_violation_count += 1
            errors.append(f"{label}: asset source/rights/consent invalid")

    versions = data.get("case_versions") or []
    version_ids = unique_ids(versions, "version_id", "case_versions", errors)
    present_version_types: set[str] = set()
    unauthorized_publication_count = 0
    for index, version in enumerate(versions):
        label = f"case_version[{index}]"
        require_fields(
            version,
            (
                "version_id", "version_type", "audience", "purpose", "channel", "format",
                "claim_ids", "metric_ids", "quote_ids", "asset_ids", "disclosure", "owner", "approval_status",
            ),
            label, errors,
        )
        present_version_types.add(str(version.get("version_type", "")))
        validate_refs(version.get("claim_ids"), claim_ids, label, "claim_ids", errors)
        validate_refs(version.get("metric_ids"), metric_ids, label, "metric_ids", errors)
        validate_refs(version.get("quote_ids"), quote_ids, label, "quote_ids", errors, allow_empty=True)
        validate_refs(version.get("asset_ids"), asset_ids, label, "asset_ids", errors, allow_empty=True)
        if version.get("channel") not in contract.get("channels", []) or version.get("format") not in consent.get("allowed_formats", []):
            errors.append(f"{label}: channel/format outside contract or consent")
        approval = str(version.get("approval_status", ""))
        if approval in FORBIDDEN_VERSION_STATES:
            unauthorized_publication_count += 1
            errors.append(f"{label}: forbidden approval/publication state {approval}")
        elif approval not in VERSION_STATES:
            errors.append(f"{label}: invalid approval_status")
    missing_version_types = sorted(VERSION_TYPES - present_version_types)
    if missing_version_types:
        errors.append(f"case_versions: missing types: {', '.join(missing_version_types)}")

    risks = data.get("risks") or []
    risk_ids = unique_ids(risks, "risk_id", "risks", errors)
    for index, risk in enumerate(risks):
        label = f"risk[{index}]"
        require_fields(risk, ("risk_id", "type", "trigger", "harm", "prevention", "stop_or_rollback", "owner", "source_refs"), label, errors)
        validate_refs(risk.get("source_refs"), active_sources, label, "source_refs", errors)

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

    final_pass = any(
        review.get("review_type") == "FINAL_PUBLICATION" and review.get("required") is True
        and review.get("status") == "PASS" and not blank(review.get("evidence_ref"))
        for review in reviews
    )
    all_pass = bool(reviews) and all(review.get("status") == "PASS" for review in reviews if review.get("required") is True)
    if errors:
        state = "NOT_READY"
    elif all_pass and final_pass:
        state = "READY_FOR_AUTHORIZED_PUBLICATION"
        warnings.append("Human publication decision and channel execution remain outside the engine")
    else:
        state = "READY_FOR_CASE_REVIEW"
        warnings.append("Human reviews remain; the engine does not sign, send, approve, or publish")

    return {
        "case_id": contract.get("case_id", ""),
        "state": state,
        "metrics": {
            "sources": len(source_ids), "active_sources": len(active_sources), "metrics": len(metric_ids),
            "interventions": len(intervention_ids), "confounders": len(confounder_ids), "claims": len(claim_ids),
            "quotes": len(quote_ids), "assets": len(asset_ids), "case_versions": len(version_ids),
            "version_types": len(present_version_types & VERSION_TYPES), "risks": len(risk_ids),
            "test_types": len(present_test_types & TEST_TYPES), "consent_valid": consent_valid,
            "calculation_defect_count": calculation_defect_count, "forbidden_claim_count": forbidden_claim_count,
            "attribution_overclaim_count": attribution_overclaim_count, "quote_violation_count": quote_violation_count,
            "asset_violation_count": asset_violation_count, "unauthorized_publication_count": unauthorized_publication_count,
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
