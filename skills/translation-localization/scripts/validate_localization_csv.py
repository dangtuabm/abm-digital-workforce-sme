#!/usr/bin/env python3
"""Validate localization CSV coverage and placeholder/tag parity."""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import tempfile
from collections import Counter
from pathlib import Path

REQUIRED = {"segment_id", "source_text", "target_text"}
TOKEN_RE = re.compile(
    r"\{\{[^{}]+\}\}|\$\{[^{}]+\}|\{[A-Za-z_][A-Za-z0-9_.-]*\}|%(?:\d+\$)?[sdif]|</?[A-Za-z][^>]*>"
)


def tokens(text: str) -> Counter[str]:
    return Counter(TOKEN_RE.findall(text or ""))


def validate(path: Path) -> dict:
    errors: list[dict] = []
    warnings: list[dict] = []
    rows = 0
    ids: set[str] = set()
    with path.open("r", encoding="utf-8-sig", newline="") as handle:
        reader = csv.DictReader(handle)
        headers = set(reader.fieldnames or [])
        missing = sorted(REQUIRED - headers)
        if missing:
            return {"passed": False, "rows": 0, "errors": [{"type": "missing_headers", "fields": missing}], "warnings": []}
        for line_no, row in enumerate(reader, start=2):
            rows += 1
            seg = (row.get("segment_id") or "").strip()
            source = row.get("source_text") or ""
            target = row.get("target_text") or ""
            if not seg:
                errors.append({"line": line_no, "type": "missing_segment_id"})
            elif seg in ids:
                errors.append({"line": line_no, "segment_id": seg, "type": "duplicate_segment_id"})
            ids.add(seg)
            if source and not target and (row.get("qa_status") or "").upper() not in {"LOCKED", "EXCLUDED"}:
                errors.append({"line": line_no, "segment_id": seg, "type": "empty_target"})
            src_tokens, tgt_tokens = tokens(source), tokens(target)
            if src_tokens != tgt_tokens:
                errors.append({
                    "line": line_no,
                    "segment_id": seg,
                    "type": "token_parity",
                    "missing_in_target": list((src_tokens - tgt_tokens).elements()),
                    "extra_in_target": list((tgt_tokens - src_tokens).elements()),
                })
            limit = (row.get("char_limit") or "").strip()
            if limit:
                try:
                    if len(target) > int(limit):
                        warnings.append({"line": line_no, "segment_id": seg, "type": "char_limit", "actual": len(target), "limit": int(limit)})
                except ValueError:
                    errors.append({"line": line_no, "segment_id": seg, "type": "invalid_char_limit", "value": limit})
    return {"passed": not errors, "rows": rows, "unique_ids": len(ids), "errors": errors, "warnings": warnings}


def self_test() -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "segments.csv"
        path.write_text(
            "segment_id,source_text,target_text,char_limit,qa_status\n"
            'SEG-001,"Hello {name}","Xin chào {name}",30,PENDING\n'
            'SEG-002,"Open <b>${file}</b>","Mở <b>${file}</b>",30,PENDING\n',
            encoding="utf-8",
        )
        result = validate(path)
        result["self_test"] = True
        return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("csv_path", nargs="?", type=Path)
    parser.add_argument("--self-test", action="store_true")
    args = parser.parse_args()
    if args.self_test:
        result = self_test()
    elif args.csv_path:
        result = validate(args.csv_path)
    else:
        parser.error("provide csv_path or --self-test")
    print(json.dumps(result, ensure_ascii=False, separators=(",", ":")))
    return 0 if result["passed"] else 1


if __name__ == "__main__":
    sys.exit(main())

