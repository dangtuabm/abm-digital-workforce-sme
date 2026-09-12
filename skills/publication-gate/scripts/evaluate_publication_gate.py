#!/usr/bin/env python3
"""Deterministic static gate for a Publication Decision Dossier."""

from __future__ import annotations

import argparse
import json
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


CONTROL_TYPES = {
    "IDENTITY", "ACCURACY", "CLARITY_USEFULNESS", "BRAND_DISCLOSURE",
    "LEGAL_COMPLIANCE", "PRIVACY_SECURITY", "IP_RIGHTS", "ACCESSIBILITY",
    "CHANNEL_TECHNICAL", "RELEASE_OPERATIONS",
}
TEST_TYPES = {
    "candidate_identity", "claim_evidence", "rights_consent_disclosure",
    "content_quality", "privacy_security_accessibility",
    "channel_release_operations", "approval_publication_boundary",
}
REVIEW_TYPES = {
    "CONTENT_OWNER", "FACT_SOURCE_OWNER", "BRAND_EDITORIAL",
    "LEGAL_COMPLIANCE_PRIVACY", "ACCESSIBILITY_TECHNICAL", "FINAL_RELEASE",
}
CLAIM_TYPES = {"FACTUAL", "NUMERIC", "COMPARATIVE", "LEGAL", "TESTIMONIAL", "FORWARD_LOOKING"}
CHECK_RESULTS = {"PASS", "FAIL", "PENDING", "N_A"}
DEFECT_SEVERITIES = {"BLOCKER", "MAJOR", "MINOR"}
DEFECT_STATES = {"OPEN", "RESOLVED", "ACCEPTED_RISK"}
FORBIDDEN_CANDIDATE_STATES = {"APPROVED", "PUBLISHED", "SENT", "DEPLOYED", "SIGNED"}
FORBIDDEN_CLAIM_FLAGS = {
    "fabricated_evidence", "overclaim", "stale_source", "cherry_picked",
    "undisclosed_material_fact", "privacy_breach", "unlicensed_material",
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


def evaluate(data: dict[str, Any]) -> dict[str, Any]:
    errors: list[str] = []
    warnings: list[str] = []

    contract = data.get("release_contract") or {}
    require_fields(
        contract,
        (
            "gate_id", "artifact_id", "version", "content_hash", "purpose", "audiences",
            "channels", "formats", "locale", "territory", "owner", "final_approver",
            "classification", "retention", "policy_refs", "prohibited_actions",
            "stop_or_escalation", "required_reviews",
        ),
        "release_contract", errors,
    )
    if contract.get("candidate_authorized") is not True:
        errors.append("release_contract: candidate_authorized must be true")

    sources = data.get("sources") or []
    source_ids = unique_ids(sources, "source_id", "sources", errors)
    active_sources: set[str] = set()
    for index, source in enumerate(sources):
        label = f"source[{index}]"
        require_fields(source, ("source_id", "title", "version", "locator", "owner", "effective_date", "classification"), label, errors)
        if source.get("active") is True:
            active_sources.add(str(source.get("source_id")))
    if not active_sources:
        errors.append("sources: at least one active source is required")
    validate_refs(contract.get("policy_refs"), active_sources, "release_contract", "policy_refs", errors)

    candidate = data.get("candidate") or {}
    require_fields(candidate, ("artifact_id", "version", "content_hash", "locator", "format", "complete", "access_authorized", "review_status"), "candidate", errors)
    candidate_identity_valid = True
    for field in ("artifact_id", "version", "content_hash"):
        if candidate.get(field) != contract.get(field):
            errors.append(f"candidate: {field} does not match release contract")
            candidate_identity_valid = False
    if candidate.get("complete") is not True or candidate.get("access_authorized") is not True:
        errors.append("candidate: complete and authorized artifact required")
        candidate_identity_valid = False
    unauthorized_publication_count = 0
    if candidate.get("review_status") in FORBIDDEN_CANDIDATE_STATES:
        unauthorized_publication_count += 1
        errors.append(f"candidate: forbidden approval/publication state {candidate.get('review_status')}")
    elif candidate.get("review_status") not in {"DRAFT", "REVIEW_PENDING", "REVIEWED"}:
        errors.append("candidate: invalid review_status")

    claims = data.get("claims") or []
    claim_ids = unique_ids(claims, "claim_id", "claims", errors)
    forbidden_claim_count = 0
    unsupported_claim_count = 0
    for index, claim in enumerate(claims):
        label = f"claim[{index}]"
        require_fields(claim, ("claim_id", "statement", "claim_type", "source_refs", "locator", "scope", "effective_date", "qualification", "owner"), label, errors)
        refs = validate_refs(claim.get("source_refs"), active_sources, label, "source_refs", errors)
        if not refs or claim.get("evidence_status") != "SUPPORTED":
            unsupported_claim_count += 1
            errors.append(f"{label}: claim evidence is not supported")
        if claim.get("claim_type") not in CLAIM_TYPES:
            errors.append(f"{label}: invalid claim_type")
        for flag in FORBIDDEN_CLAIM_FLAGS:
            if claim.get(flag) is True:
                forbidden_claim_count += 1
                errors.append(f"{label}: forbidden claim flag {flag}")

    rights = data.get("rights_and_consents") or []
    rights_ids = unique_ids(rights, "record_id", "rights_and_consents", errors)
    rights_violation_count = 0
    for index, record in enumerate(rights):
        label = f"rights[{index}]"
        require_fields(record, ("record_id", "subject", "record_type", "status", "evidence_ref", "territory", "expiry", "owner"), label, errors)
        if record.get("status") != "APPROVED" or record.get("evidence_ref") not in active_sources:
            rights_violation_count += 1
            errors.append(f"{label}: rights/consent not approved or evidenced")

    disclosures = data.get("disclosures") or []
    disclosure_ids = unique_ids(disclosures, "disclosure_id", "disclosures", errors)
    disclosure_violation_count = 0
    for index, disclosure in enumerate(disclosures):
        label = f"disclosure[{index}]"
        require_fields(disclosure, ("disclosure_id", "type", "required", "text", "locator", "policy_ref", "status", "owner"), label, errors)
        if disclosure.get("required") is True and (disclosure.get("status") != "PRESENT" or disclosure.get("policy_ref") not in active_sources):
            disclosure_violation_count += 1
            errors.append(f"{label}: required disclosure missing or unsupported")

    controls = data.get("controls") or []
    present_controls = {str(item.get("control_type", "")) for item in controls}
    missing_controls = sorted(CONTROL_TYPES - present_controls)
    if missing_controls:
        errors.append(f"controls: missing types: {', '.join(missing_controls)}")
    failed_control_count = 0
    pending_control_count = 0
    for index, control in enumerate(controls):
        label = f"control[{index}]"
        require_fields(control, ("control_type", "result", "evidence_refs", "reviewer", "date"), label, errors)
        validate_refs(control.get("evidence_refs"), active_sources, label, "evidence_refs", errors)
        result = control.get("result")
        if result not in CHECK_RESULTS:
            errors.append(f"{label}: invalid result")
        elif result == "FAIL":
            failed_control_count += 1
            errors.append(f"{label}: control failed")
        elif result == "PENDING":
            pending_control_count += 1
        elif result == "N_A" and blank(control.get("rationale")):
            errors.append(f"{label}: N_A requires rationale")

    defects = data.get("defects") or []
    defect_ids = unique_ids(defects, "defect_id", "defects", errors)
    open_blocker_major_count = 0
    open_minor_count = 0
    invalid_accepted_risk_count = 0
    for index, defect in enumerate(defects):
        label = f"defect[{index}]"
        require_fields(defect, ("defect_id", "severity", "location", "evidence", "harm", "fix", "owner", "status"), label, errors)
        severity, status = defect.get("severity"), defect.get("status")
        if severity not in DEFECT_SEVERITIES or status not in DEFECT_STATES:
            errors.append(f"{label}: invalid severity/status")
            continue
        if status == "OPEN" and severity in {"BLOCKER", "MAJOR"}:
            open_blocker_major_count += 1
            errors.append(f"{label}: open blocker/major")
        elif status == "OPEN" and severity == "MINOR":
            open_minor_count += 1
            require_fields(defect, ("retest_plan",), label, errors)
        elif status == "RESOLVED":
            require_fields(defect, ("retest_evidence", "reviewer", "test_date"), label, errors)
        elif status == "ACCEPTED_RISK":
            require_fields(defect, ("acceptance_authority", "acceptance_evidence", "mitigation", "expiry"), label, errors)
            if severity != "MINOR":
                invalid_accepted_risk_count += 1
                errors.append(f"{label}: only MINOR may be accepted risk")

    release_plan = data.get("release_plan") or {}
    require_fields(release_plan, ("destination", "schedule", "dependencies", "monitoring", "correction_route", "rollback_trigger", "rollback_action", "rollback_owner", "archive_evidence"), "release_plan", errors)
    if release_plan.get("execution_status") in FORBIDDEN_CANDIDATE_STATES:
        unauthorized_publication_count += 1
        errors.append(f"release_plan: forbidden execution state {release_plan.get('execution_status')}")

    tests = data.get("tests") or []
    present_tests = {str(item.get("test_type", "")) for item in tests}
    missing_tests = sorted(TEST_TYPES - present_tests)
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

    final_pass = any(r.get("review_type") == "FINAL_RELEASE" and r.get("required") is True and r.get("status") == "PASS" and not blank(r.get("evidence_ref")) for r in reviews)
    nonfinal_pass = all(r.get("status") == "PASS" for r in reviews if r.get("required") is True and r.get("review_type") != "FINAL_RELEASE")
    all_pass = bool(reviews) and all(r.get("status") == "PASS" for r in reviews if r.get("required") is True)

    hard_error_count = len(errors)
    if hard_error_count:
        state = "NOT_READY"
    elif open_minor_count or pending_control_count:
        state = "READY_FOR_REMEDIATION"
    elif all_pass and final_pass:
        state = "READY_FOR_AUTHORIZED_RELEASE"
        warnings.append("Authorized execution remains human-owned; the engine does not publish")
    elif nonfinal_pass:
        state = "READY_FOR_HUMAN_RELEASE_DECISION"
        warnings.append("FINAL_RELEASE review remains; the engine does not approve or publish")
    else:
        state = "NOT_READY"
        errors.append("reviews: non-final required reviews are incomplete")

    return {
        "gate_id": contract.get("gate_id", ""),
        "state": state,
        "metrics": {
            "sources": len(source_ids), "active_sources": len(active_sources), "claims": len(claim_ids),
            "rights_records": len(rights_ids), "disclosures": len(disclosure_ids),
            "control_types": len(present_controls & CONTROL_TYPES), "failed_controls": failed_control_count,
            "pending_controls": pending_control_count, "defects": len(defect_ids),
            "open_blocker_major": open_blocker_major_count, "open_minor": open_minor_count,
            "invalid_accepted_risk": invalid_accepted_risk_count, "test_types": len(present_tests & TEST_TYPES),
            "candidate_identity_valid": candidate_identity_valid, "unsupported_claims": unsupported_claim_count,
            "forbidden_claims": forbidden_claim_count, "rights_violations": rights_violation_count,
            "disclosure_violations": disclosure_violation_count,
            "unauthorized_publication": unauthorized_publication_count, "critical_defects": len(errors),
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

