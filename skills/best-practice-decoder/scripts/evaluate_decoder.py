#!/usr/bin/env python3
"""Deterministic structural gate for a Best-Practice Transfer Blueprint."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any


def nonempty(value: Any) -> bool:
    return value not in (None, "", [], {})


def evaluate(data: dict[str, Any]) -> dict[str, Any]:
    contract = data.get("contract") or {}
    standards = contract.get("standards") or {}
    issues: list[str] = []
    warnings: list[str] = []
    guardrails = list(data.get("guardrails") or [])
    required = ("decoder_id", "exemplar_scope", "target_context", "target_outcome", "baseline", "identity_constraints", "owner", "risk_level")
    missing = [key for key in required if not nonempty(contract.get(key))]
    for key in ("min_evidence_items", "required_layers"):
        if not nonempty(standards.get(key)):
            missing.append(f"standards.{key}")
    if missing:
        return {"state": "NOT_READY", "issues": [f"missing:{x}" for x in missing], "warnings": [], "guardrails": guardrails}

    evidence = data.get("evidence") or []
    components = data.get("components") or []
    if not evidence or not components:
        return {"state": "DRAFT", "issues": ["no_evidence_or_components"], "warnings": [], "guardrails": guardrails}

    evidence_ids: set[str] = set()
    evidence_fields = ("id", "source_ref", "date_or_version", "source_type", "claim", "observed_result", "denominator_or_scope", "rights_status", "confidence", "limitations")
    for index, item in enumerate(evidence, start=1):
        label = item.get("id") or f"row_{index}"
        absent = [key for key in evidence_fields if not nonempty(item.get(key))]
        if absent:
            issues.append(f"evidence_fields:{label}:{','.join(absent)}")
        if nonempty(item.get("id")):
            if item["id"] in evidence_ids:
                issues.append(f"duplicate_evidence:{item['id']}")
            evidence_ids.add(item["id"])
        if item.get("rights_status") in {None, "", "unknown", "denied"}:
            issues.append(f"rights_unresolved:{label}")

    component_ids: set[str] = set()
    layers: set[str] = set()
    component_fields = ("id", "layer", "description", "evidence_refs", "causal_confidence", "context_dependency", "decision_rule", "exceptions", "copy_risk")
    for index, component in enumerate(components, start=1):
        label = component.get("id") or f"row_{index}"
        absent = [key for key in component_fields if not nonempty(component.get(key))]
        if absent:
            issues.append(f"component_fields:{label}:{','.join(absent)}")
        if nonempty(component.get("id")):
            if component["id"] in component_ids:
                issues.append(f"duplicate_component:{component['id']}")
            component_ids.add(component["id"])
        if nonempty(component.get("layer")):
            layers.add(component["layer"])
        unknown = set(component.get("evidence_refs") or []) - evidence_ids
        if unknown:
            issues.append(f"unknown_evidence_refs:{label}:{','.join(sorted(unknown))}")
        if component.get("causal_confidence") == "high" and len(component.get("evidence_refs") or []) < int(standards["min_evidence_items"]):
            issues.append(f"unsupported_high_confidence:{label}")
    for layer in standards["required_layers"]:
        if layer not in layers:
            issues.append(f"missing_layer:{layer}")

    if not nonempty(data.get("rival_explanations")):
        issues.append("missing_rival_explanations")

    transfer_by_component: set[str] = set()
    valid_decisions = {"retain", "adapt", "drop", "test"}
    transfer_fields = ("component_id", "decision", "target_fit", "adaptation", "owner", "validation_needed")
    for index, transfer in enumerate(data.get("transfers") or [], start=1):
        label = transfer.get("component_id") or f"row_{index}"
        absent = [key for key in transfer_fields if not nonempty(transfer.get(key))]
        if absent:
            issues.append(f"transfer_fields:{label}:{','.join(absent)}")
        if transfer.get("component_id") not in component_ids:
            issues.append(f"unknown_component:{label}")
        else:
            transfer_by_component.add(transfer["component_id"])
        if transfer.get("decision") not in valid_decisions:
            issues.append(f"invalid_decision:{label}")
    for component_id in sorted(component_ids - transfer_by_component):
        issues.append(f"missing_transfer:{component_id}")

    pilot = data.get("pilot") or {}
    pilot_fields = ("hypothesis", "baseline", "leading_metric", "outcome_metric", "data_source", "success_threshold", "stop_threshold", "review_window", "owner", "rollback")
    for key in pilot_fields:
        if not nonempty(pilot.get(key)):
            issues.append(f"pilot_missing:{key}")

    below_minimum = len(evidence) < int(standards["min_evidence_items"])
    if issues:
        state = "REVISE"
    elif below_minimum:
        state = "HYPOTHESIS_ONLY"
        warnings.append(f"evidence_below_minimum:{len(evidence)}<{standards['min_evidence_items']}")
    else:
        state = "READY_FOR_PILOT"
    if not issues and (contract.get("risk_level") == "high" or data.get("expert_review") != "approved" or guardrails):
        state = "READY_WITH_GUARDRAILS"
        if data.get("expert_review") != "approved":
            warnings.append("expert_review_pending")
    return {
        "state": state,
        "issues": sorted(set(issues)),
        "warnings": sorted(set(warnings)),
        "guardrails": guardrails,
        "metrics": {
            "evidence_count": len(evidence),
            "component_count": len(components),
            "layers": sorted(layers),
            "transfer_decisions": sorted({item.get("decision") for item in data.get("transfers") or [] if item.get("decision")}),
            "below_evidence_minimum": below_minimum,
        },
    }


def selftest() -> dict[str, Any]:
    evidence = [{"id": f"E{i}", "source_ref": f"case-{i}", "date_or_version": "2026-v1", "source_type": "verified case", "claim": "mechanism contributed", "observed_result": "measured improvement", "denominator_or_scope": "defined cohort/window", "rights_status": "approved", "confidence": "medium", "limitations": "non-random comparison"} for i in range(1, 4)]
    layers = ["mechanism", "enablers", "constraints", "exceptions", "failure_modes"]
    components = [{"id": f"C{i+1}", "layer": layer, "description": f"{layer} component", "evidence_refs": ["E1", "E2", "E3"], "causal_confidence": "medium", "context_dependency": "documented", "decision_rule": "if condition then action", "exceptions": "defined", "copy_risk": "low"} for i, layer in enumerate(layers)]
    decisions = ["retain", "adapt", "test", "drop", "test"]
    transfers = [{"component_id": component["id"], "decision": decisions[i], "target_fit": "assessed", "adaptation": "target-specific expression", "owner": "pilot-owner", "validation_needed": "pilot evidence"} for i, component in enumerate(components)]
    data = {
        "contract": {"decoder_id": "DEC-T", "exemplar_scope": "three cases", "target_context": "business unit", "target_outcome": "operating result", "baseline": "approved", "identity_constraints": "preserve brand", "owner": "business-owner", "risk_level": "medium", "standards": {"min_evidence_items": 3, "required_layers": layers}},
        "evidence": evidence, "components": components,
        "rival_explanations": ["selection effect", "market timing"],
        "transfers": transfers,
        "pilot": {"hypothesis": "adapted mechanism improves outcome", "baseline": "current rate", "leading_metric": "process signal", "outcome_metric": "business result", "data_source": "approved system", "success_threshold": "contract value", "stop_threshold": "contract limit", "review_window": "defined window", "owner": "pilot-owner", "rollback": "restore prior process"},
        "guardrails": [], "expert_review": "approved",
    }
    result = evaluate(data)
    assert result["state"] == "READY_FOR_PILOT", result
    assert result["metrics"]["evidence_count"] == 3, result
    assert len(result["metrics"]["layers"]) == 5, result
    return result


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("input", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    result = selftest() if args.self_test else evaluate(json.loads(args.input.read_text(encoding="utf-8")))
    print(json.dumps(result, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
