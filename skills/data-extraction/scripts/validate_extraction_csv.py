#!/usr/bin/env python3
"""Validate minimum structural controls for an extraction CSV."""

from __future__ import annotations

import argparse
import csv
import io
import json
import sys
from pathlib import Path

ALLOWED_STATUSES = {
    "EXACT",
    "OCR_REVIEW",
    "AMBIGUOUS",
    "MISSING",
    "INVALID_FORMAT",
}


def validate_stream(stream, required, id_column, source_column, status_column):
    reader = csv.DictReader(stream)
    headers = reader.fieldnames or []
    errors = []
    warnings = []

    if not headers:
        errors.append({"code": "NO_HEADER", "message": "CSV has no header"})
        return {"passed": False, "rows": 0, "errors": errors, "warnings": warnings}

    duplicates = sorted({h for h in headers if headers.count(h) > 1})
    if duplicates:
        errors.append({"code": "DUPLICATE_HEADER", "fields": duplicates})

    for field in required:
        if field not in headers:
            errors.append({"code": "MISSING_HEADER", "field": field})

    seen_ids = set()
    row_count = 0
    for line_number, row in enumerate(reader, start=2):
        row_count += 1
        for field in required:
            if field in headers and not (row.get(field) or "").strip():
                errors.append(
                    {"code": "EMPTY_REQUIRED", "line": line_number, "field": field}
                )

        record_id = (row.get(id_column) or "").strip()
        if record_id:
            if record_id in seen_ids:
                errors.append(
                    {"code": "DUPLICATE_ID", "line": line_number, "value": record_id}
                )
            seen_ids.add(record_id)

        if source_column in headers and not (row.get(source_column) or "").strip():
            errors.append(
                {"code": "MISSING_SOURCE_POINTER", "line": line_number}
            )

        status = (row.get(status_column) or "").strip()
        if status_column in headers and status and status not in ALLOWED_STATUSES:
            errors.append(
                {"code": "INVALID_STATUS", "line": line_number, "value": status}
            )

    if row_count == 0:
        warnings.append({"code": "NO_DATA_ROWS"})

    return {
        "passed": not errors,
        "rows": row_count,
        "unique_ids": len(seen_ids),
        "errors": errors,
        "warnings": warnings,
    }


def self_test():
    sample = io.StringIO(
        "record_id,source_pointer,extraction_status,amount\n"
        "R-001,invoice-001.pdf#page=1,EXACT,1250000\n"
        "R-002,invoice-002.pdf#page=1,OCR_REVIEW,\n"
    )
    report = validate_stream(
        sample,
        ["record_id", "source_pointer", "extraction_status"],
        "record_id",
        "source_pointer",
        "extraction_status",
    )
    report["self_test"] = True
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", type=Path)
    parser.add_argument("--required", default="record_id,source_pointer,extraction_status")
    parser.add_argument("--id-column", default="record_id")
    parser.add_argument("--source-column", default="source_pointer")
    parser.add_argument("--status-column", default="extraction_status")
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()

    if args.self_test:
        report = self_test()
    elif args.input:
        with args.input.open("r", encoding="utf-8-sig", newline="") as stream:
            report = validate_stream(
                stream,
                [x.strip() for x in args.required.split(",") if x.strip()],
                args.id_column,
                args.source_column,
                args.status_column,
            )
    else:
        parser.error("provide --input or --self-test")

    print(json.dumps(report, ensure_ascii=False, indent=2))
    return 0 if report["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())


