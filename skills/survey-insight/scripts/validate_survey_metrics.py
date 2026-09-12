#!/usr/bin/env python3
"""Validate survey metric bases and reported percentages."""

from __future__ import annotations

import argparse
import csv
import json
import math
import sys
import tempfile
from decimal import Decimal, InvalidOperation
from pathlib import Path

REQUIRED = {"metric_id", "numerator", "denominator", "percent_reported", "unweighted_n"}


def number(value: str) -> Decimal:
    return Decimal((value or "").strip())


def validate(path: Path, tolerance: Decimal = Decimal("0.05")) -> dict:
    errors: list[dict] = []
    warnings: list[dict] = []
    ids: set[str] = set()
    rows = 0
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        missing = sorted(REQUIRED - set(reader.fieldnames or []))
        if missing:
            return {"passed": False, "rows": 0, "errors": [{"type": "missing_headers", "fields": missing}], "warnings": []}
        for line_no, row in enumerate(reader, start=2):
            rows += 1
            metric = (row.get("metric_id") or "").strip()
            if not metric:
                errors.append({"line": line_no, "type": "missing_metric_id"})
            elif metric in ids:
                errors.append({"line": line_no, "metric_id": metric, "type": "duplicate_metric_id"})
            ids.add(metric)
            try:
                numerator = number(row["numerator"])
                denominator = number(row["denominator"])
                reported = number(row["percent_reported"])
                unweighted_n = number(row["unweighted_n"])
            except (InvalidOperation, KeyError):
                errors.append({"line": line_no, "metric_id": metric, "type": "invalid_number"})
                continue
            if denominator <= 0 or numerator < 0 or numerator > denominator:
                errors.append({"line": line_no, "metric_id": metric, "type": "invalid_base", "numerator": str(numerator), "denominator": str(denominator)})
                continue
            expected = numerator / denominator * Decimal(100)
            if abs(expected - reported) > tolerance:
                errors.append({"line": line_no, "metric_id": metric, "type": "percent_mismatch", "expected": str(expected), "reported": str(reported)})
            if unweighted_n <= 0:
                errors.append({"line": line_no, "metric_id": metric, "type": "invalid_unweighted_n"})
            if unweighted_n < 30:
                warnings.append({"line": line_no, "metric_id": metric, "type": "small_base", "unweighted_n": str(unweighted_n)})
    return {"passed": not errors, "rows": rows, "unique_ids": len(ids), "errors": errors, "warnings": warnings}


def self_test() -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "metrics.csv"
        path.write_text(
            "metric_id,numerator,denominator,percent_reported,unweighted_n\n"
            "MET-001,70,100,70,100\n"
            "MET-002,45,60,75,60\n",
            encoding="utf-8",
        )
        result = validate(path)
        result["self_test"] = True
        return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", nargs="?", type=Path)
    parser.add_argument("--tolerance", default="0.05")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    result = self_test() if args.self_test else validate(args.csv_path, Decimal(args.tolerance)) if args.csv_path else None
    if result is None:
        parser.error("provide csv_path or --self-test")
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())

