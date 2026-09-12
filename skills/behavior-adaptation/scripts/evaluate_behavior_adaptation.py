#!/usr/bin/env python3
"""Deterministic gate for a Behavior-Adaptive Interaction Experiment Pack.

Reads one local JSON file. It does not open sources, enrich identity, call APIs,
message, target, coach, negotiate, make decisions, or grant approval.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any


MODES = {"presentation", "delegation", "feedback", "coaching", "negotiation", "objection"}
DIMENSIONS = {
    "pace_latency", "detail_structure", "task_people_focus", "autonomy_control",
    "risk_uncertainty", "decision_style", "channel_feedback",
}
REQUIRED_TESTS = {
    "observation_trace", "hypothesis_humility", "interaction_fit",
    "outcome_action_accuracy", "dignity_nonmanipulation",
    "accessibility_channel", "update_transfer_boundary",
}
BANNED_KEYS = {
    "deep_fear", "deep_motivation", "personality_identity", "mental_state",
    "protected_trait", "diagnosis", "inferred_intent",
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


def find_banned_keys(value: Any, path: str = "payload") -> list[str]:
    found: list[str] = []
    if isinstance(value, dict):
        for key, child in value.items():
            if key in BANNED_KEYS:
                found.append(f"{path}.{key}")
            found.extend(find_banned_keys(child, f"{path}.{key}"))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            found.extend(find_banned_keys(child, f"{path}[{index}]"))
    return found


def main(input_path: str) -> int:
    payload = json.loads(Path(input_path).read_text(encoding="utf-8"))
    errors: list[str] = []
    warnings: list[str] = []
    guardrails = ["HUMAN_APPROVAL_REQUIRED_BEFORE_INTERACTION_TARGETING_OR_OPERATION"]

    banned_paths = find_banned_keys(payload)
    if banned_paths:
        errors.append("banned inference fields: " + ", ".join(banned_paths))

    contract = payload.get("contract")
    require_fields(contract, [
        "id", "subject_pseudonym", "subject_role", "relationship", "mode",
        "context", "channel", "objective", "stakes", "data_classification",
        "consent_basis", "allowed_uses", "prohibited_uses", "retention_expiry",
        "non_negotiables", "owner", "reviewer", "approval_route", "status",
    ], "contract", errors)
    require_list_keys(contract, ["allowed_uses", "prohibited_uses", "non_negotiables"], "contract", errors)
    mode = str(contract.get("mode", "")) if isinstance(contract, dict) else ""
    if mode not in MODES:
        errors.append("contract.mode is not supported")

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

    observations = payload.get("observations", [])
    if not isinstance(observations, list) or not observations:
        errors.append("observations must be a non-empty list")
        observations = []
    observation_ids = unique_ids(observations, "observations", errors)
    observation_by_id: dict[str, dict[str, Any]] = {}
    for index, observation in enumerate(observations):
        require_fields(observation, [
            "id", "source_ref", "date", "context", "channel", "exact_behavior",
            "dimension", "counterexample", "quality", "status",
        ], f"observations[{index}]", errors)
        observation_by_id[str(observation.get("id", ""))] = observation
        if observation.get("source_ref") not in source_ids:
            errors.append(f"observations[{index}] unknown source_ref")
        if observation.get("dimension") not in DIMENSIONS:
            errors.append(f"observations[{index}] unsupported dimension")
        if observation.get("authorized") is not True:
            errors.append(f"observations[{index}] is not authorized")

    hypotheses = payload.get("hypotheses", [])
    if not isinstance(hypotheses, list) or not hypotheses:
        errors.append("hypotheses must be a non-empty list")
        hypotheses = []
    hypothesis_ids = unique_ids(hypotheses, "hypotheses", errors)
    hypothesis_by_id: dict[str, dict[str, Any]] = {}
    untraced_hypotheses = 0
    for index, hypothesis in enumerate(hypotheses):
        require_fields(hypothesis, [
            "id", "text", "confidence", "scope", "expiry_review", "falsifier",
            "next_evidence", "status",
        ], f"hypotheses[{index}]", errors)
        require_list_keys(hypothesis, ["observation_refs", "alternative_explanations"], f"hypotheses[{index}]", errors)
        hypothesis_by_id[str(hypothesis.get("id", ""))] = hypothesis
        refs = set(hypothesis.get("observation_refs", []))
        bad_refs = sorted(refs - observation_ids)
        if bad_refs:
            errors.append(f"hypotheses[{index}] unknown observation refs: {', '.join(bad_refs)}")
        if not refs or not hypothesis.get("alternative_explanations"):
            untraced_hypotheses += 1
        confidence = hypothesis.get("confidence")
        if confidence not in {"low", "medium", "high"}:
            errors.append(f"hypotheses[{index}] invalid confidence")
        if confidence == "high":
            source_refs = {observation_by_id.get(ref, {}).get("source_ref") for ref in refs}
            if len(refs) < 3 or len(source_refs - {None}) < 2:
                errors.append(f"hypotheses[{index}] high confidence lacks independent evidence")

    assessments = payload.get("model_assessments", [])
    if not isinstance(assessments, list):
        errors.append("model_assessments must be a list")
        assessments = []
    for index, assessment in enumerate(assessments):
        require_fields(assessment, ["id", "model", "purpose", "confidence", "status"], f"model_assessments[{index}]", errors)
        require_list_keys(assessment, ["hypothesis_refs"], f"model_assessments[{index}]", errors)
        refs = set(assessment.get("hypothesis_refs", []))
        bad_refs = sorted(refs - hypothesis_ids)
        if bad_refs:
            errors.append(f"model_assessments[{index}] unknown hypothesis refs: {', '.join(bad_refs)}")
        if assessment.get("context_only") is not True or assessment.get("prohibited_use_ack") is not True:
            errors.append(f"model_assessments[{index}] lacks context/prohibited-use guardrail")
        if str(assessment.get("model", "")).upper() == "DISC":
            observation_refs: set[str] = set()
            for ref in refs:
                observation_refs |= set(hypothesis_by_id.get(ref, {}).get("observation_refs", []))
            dimensions = {observation_by_id.get(ref, {}).get("dimension") for ref in observation_refs}
            if len(dimensions - {None}) < 2:
                errors.append(f"model_assessments[{index}] DISC lacks two evidence dimensions")

    playbooks = payload.get("playbooks", [])
    if not isinstance(playbooks, list) or not playbooks:
        errors.append("playbooks must be a non-empty list")
        playbooks = []
    playbook_ids = unique_ids(playbooks, "playbooks", errors)
    playbook_by_id: dict[str, dict[str, Any]] = {}
    covered_hypotheses: set[str] = set()
    for index, playbook in enumerate(playbooks):
        require_fields(playbook, [
            "id", "mode", "objective", "baseline_fallback", "opening",
            "information_structure", "pace", "questions", "evidence_style",
            "action_close", "comprehension_check", "stop_escalation", "status",
        ], f"playbooks[{index}]", errors)
        require_list_keys(playbook, ["hypothesis_refs", "do", "avoid"], f"playbooks[{index}]", errors)
        playbook_by_id[str(playbook.get("id", ""))] = playbook
        if playbook.get("mode") not in MODES:
            errors.append(f"playbooks[{index}] unsupported mode")
        refs = set(playbook.get("hypothesis_refs", []))
        covered_hypotheses |= refs
        bad_refs = sorted(refs - hypothesis_ids)
        if bad_refs:
            errors.append(f"playbooks[{index}] unknown hypothesis refs: {', '.join(bad_refs)}")
    missing_playbook_hypotheses = sorted(hypothesis_ids - covered_hypotheses)
    if missing_playbook_hypotheses:
        warnings.append("hypotheses without playbook: " + ", ".join(missing_playbook_hypotheses))

    experiments = payload.get("experiments", [])
    if not isinstance(experiments, list) or not experiments:
        errors.append("experiments must be a non-empty list")
        experiments = []
    experiment_ids = unique_ids(experiments, "experiments", errors)
    experiment_by_id: dict[str, dict[str, Any]] = {}
    covered_playbooks: set[str] = set()
    trial_defects = 0
    for index, experiment in enumerate(experiments):
        require_fields(experiment, [
            "id", "playbook_id", "hypothesis_id", "lever", "baseline", "adaptation",
            "prediction", "success_metric", "threshold", "sample_or_window", "risk",
            "consent", "owner", "stop_rule", "rollback", "status",
        ], f"experiments[{index}]", errors)
        experiment_by_id[str(experiment.get("id", ""))] = experiment
        playbook_id = str(experiment.get("playbook_id", ""))
        hypothesis_id = str(experiment.get("hypothesis_id", ""))
        covered_playbooks.add(playbook_id)
        if playbook_id not in playbook_ids:
            errors.append(f"experiments[{index}] unknown playbook_id")
        if hypothesis_id not in hypothesis_ids:
            errors.append(f"experiments[{index}] unknown hypothesis_id")
        if hypothesis_id not in set(playbook_by_id.get(playbook_id, {}).get("hypothesis_refs", [])):
            trial_defects += 1
        if experiment.get("status") not in {"planned", "approved_for_trial", "completed", "stopped", "rolled_back"}:
            errors.append(f"experiments[{index}] invalid status")
    missing_trial_playbooks = sorted(playbook_ids - covered_playbooks)
    if missing_trial_playbooks:
        warnings.append("playbooks without trial: " + ", ".join(missing_trial_playbooks))

    updates = payload.get("response_updates", [])
    if not isinstance(updates, list):
        errors.append("response_updates must be a list")
        updates = []
    for index, update in enumerate(updates):
        require_fields(update, [
            "id", "experiment_id", "observed_response", "outcome_metric", "counterevidence",
            "unintended_effect", "context", "decision", "confidence_change", "reviewer", "status",
        ], f"response_updates[{index}]", errors)
        if update.get("experiment_id") not in experiment_ids:
            errors.append(f"response_updates[{index}] unknown experiment_id")
        if update.get("decision") not in {"retain", "revise", "reject"}:
            errors.append(f"response_updates[{index}] invalid decision")

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
        "source_data_check", "privacy_consent_check", "hypothesis_check",
        "fairness_nonmanipulation_check", "accessibility_check",
        "experiment_design_check", "validation_state",
    ], "review", errors)
    require_list_keys(review, ["required_specialist_reviews", "completed_specialist_reviews"], "review", errors)
    review_gaps: list[str] = []
    missing_specialist_reviews: list[str] = []
    if isinstance(review, dict):
        for field in [
            "source_data_check", "privacy_consent_check", "hypothesis_check",
            "fairness_nonmanipulation_check", "accessibility_check", "experiment_design_check",
        ]:
            if review.get(field) is not True:
                review_gaps.append(field)
        missing_specialist_reviews = sorted(set(review.get("required_specialist_reviews", [])) - set(review.get("completed_specialist_reviews", [])))
        if review.get("operation_approved") is True:
            guardrails.append("ENGINE_CANNOT_GRANT_OR_VERIFY_OPERATION_APPROVAL")

    behavior_defects = untraced_hypotheses + len(missing_playbook_hypotheses) + len(missing_trial_playbooks) + trial_defects
    if errors:
        state = "NOT_READY"
        next_action = "resolve_errors_and_rerun"
    elif behavior_defects or review_gaps or "failed" in test_statuses:
        state = "PLAYBOOK_READY" if playbooks else "OBSERVATION_READY"
        next_action = "close_trace_playbook_trial_review_or_test_gaps"
    elif updates and test_statuses and all(status == "passed" for status in test_statuses) and not missing_specialist_reviews and review.get("validation_state") == "passed":
        state = "VALIDATED_FOR_OWNER_REVIEW"
        next_action = "obtain_human_operational_approval"
    else:
        state = "READY_FOR_CONSENTED_TRIAL"
        next_action = "run_human_trial_and_response_tests"

    if missing_specialist_reviews:
        warnings.append("missing specialist reviews: " + ", ".join(missing_specialist_reviews))

    result = {
        "state": state,
        "errors": errors,
        "warnings": warnings,
        "guardrails": guardrails,
        "metrics": {
            "source_count": len(sources), "active_source_count": active_sources,
            "observation_count": len(observation_ids), "hypothesis_count": len(hypothesis_ids),
            "model_assessment_count": len(assessments), "playbook_count": len(playbook_ids),
            "experiment_count": len(experiment_ids), "response_update_count": len(updates),
            "behavior_defect_count": behavior_defects, "banned_inference_count": len(banned_paths),
            "unresolved_material_conflict_count": unresolved_conflicts,
            "test_type_coverage": sorted(test_types), "review_gap_count": len(review_gaps),
        },
        "next_action": next_action,
    }
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: evaluate_behavior_adaptation.py INPUT.json", file=sys.stderr)
        raise SystemExit(2)
    raise SystemExit(main(sys.argv[1]))
