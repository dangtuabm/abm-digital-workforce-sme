#!/usr/bin/env python3
"""Deterministic ABM option scoring. Input scores must already be approved/normalized."""
import argparse
import json
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path


def fail(message):
    raise ValueError(message)


def dec(value, label):
    try:
        return Decimal(str(value))
    except (InvalidOperation, ValueError):
        fail(f"{label} must be numeric")


def q(value):
    return float(value.quantize(Decimal("0.0001")))


def score(data):
    criteria = data.get("criteria")
    options = data.get("options")
    if not isinstance(criteria, list) or not criteria:
        fail("criteria must be a non-empty list")
    if not isinstance(options, list) or not options:
        fail("options must be a non-empty list")

    ids = [c.get("id") for c in criteria]
    if None in ids or len(ids) != len(set(ids)):
        fail("criterion ids must be present and unique")
    gates = [c for c in criteria if c.get("kind") == "gate"]
    scored = [c for c in criteria if c.get("kind") == "score"]
    if len(gates) + len(scored) != len(criteria) or not scored:
        fail("criterion kind must be gate or score, with at least one score")
    weights = {c["id"]: dec(c.get("weight"), f"weight {c['id']}") for c in scored}
    if any(w < 0 for w in weights.values()) or abs(sum(weights.values()) - Decimal("1")) > Decimal("0.000001"):
        fail("score weights must be non-negative and sum to 1.00")

    results = []
    option_ids = set()
    for option in options:
        oid = option.get("id")
        if not oid or oid in option_ids:
            fail("option ids must be present and unique")
        option_ids.add(oid)
        gate_values = option.get("gates", {})
        failed = [g["id"] for g in gates if gate_values.get(g["id"]) is False]
        unknown = [g["id"] for g in gates if gate_values.get(g["id"]) is not True and g["id"] not in failed]
        result = {"id": oid, "failed_gates": failed, "unknown_gates": unknown}
        if failed:
            result["state"] = "GATE_FAIL"
            results.append(result)
            continue
        if unknown:
            result["state"] = "NOT_COMPARABLE"
            results.append(result)
            continue

        values = option.get("scores", {})
        missing = [c["id"] for c in scored if c["id"] not in values]
        if missing:
            result.update({"state": "NOT_COMPARABLE", "missing_scores": missing})
            results.append(result)
            continue
        totals = {"low": Decimal("0"), "base": Decimal("0"), "high": Decimal("0")}
        for criterion in scored:
            cid = criterion["id"]
            cell = values[cid]
            if not cell.get("evidence_id"):
                fail(f"{oid}/{cid} missing evidence_id")
            low, base, high = (dec(cell.get(k), f"{oid}/{cid}/{k}") for k in ("low", "base", "high"))
            if not (Decimal("0") <= low <= base <= high <= Decimal("100")):
                fail(f"{oid}/{cid} requires 0 <= low <= base <= high <= 100")
            for key, value in (("low", low), ("base", base), ("high", high)):
                totals[key] += weights[cid] * value
        result.update({"state": "COMPARABLE", "weighted": {k: q(v) for k, v in totals.items()}})
        results.append(result)

    comparable = sorted((r for r in results if r["state"] == "COMPARABLE"), key=lambda r: (-r["weighted"]["base"], r["id"]))
    for rank, item in enumerate(comparable, 1):
        item["base_rank"] = rank
    if len(comparable) < 2:
        stability = "NO_COMPARISON"
    else:
        top = comparable[0]
        stability = "STABLE" if top["weighted"]["low"] > max(r["weighted"]["high"] for r in comparable[1:]) else "UNSTABLE"
    return {"decision_id": data.get("decision_id"), "rank_stability": stability, "results": results}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    try:
        result = score(json.loads(args.input.read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    rendered = json.dumps(result, ensure_ascii=False, indent=2)
    if args.output:
        args.output.write_text(rendered + "\n", encoding="utf-8")
    else:
        print(rendered)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
