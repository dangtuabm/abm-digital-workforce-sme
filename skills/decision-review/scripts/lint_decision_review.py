#!/usr/bin/env python3
"""Integrity linter for frozen decision reviews and memory-promotion controls."""
import argparse, json, sys
from pathlib import Path

ATTR={"DECISION_LOGIC","EXECUTION","ASSUMPTION","EXOGENOUS","MEASUREMENT","LUCK_OR_UNRESOLVED"}
LESSON={"CASE_LESSON","HYPOTHESIS","REUSABLE_PATTERN_CANDIDATE","PROMOTED_ASSET"}

def run(d):
    issues=[]; warnings=[]
    f=d.get("frozen_decision",{})
    for k in ("decision_id","version","decided_at","owner","record_hash"):
        if not f.get(k): issues.append(f"frozen decision missing {k}")
    expected={x.get("id"):x for x in d.get("expected",[]) if x.get("id")}
    if len(expected)!=len(d.get("expected",[])) or not expected: issues.append("expected outcomes missing or duplicate ids")
    actual_by={x.get("outcome_id"):x for x in d.get("actual",[]) if x.get("outcome_id")}
    for oid,e in expected.items():
        for k in ("metric","target","source_id","as_of"):
            if e.get(k) is None or e.get(k)=="": issues.append(f"{oid} expected missing {k}")
        a=actual_by.get(oid)
        if not a: issues.append(f"{oid} missing actual")
        else:
            if a.get("metric")!=e.get("metric"): issues.append(f"{oid} metric mismatch")
            if a.get("value") is None or not a.get("source_id") or not a.get("as_of"): issues.append(f"{oid} actual incomplete")
    for oid in set(actual_by)-set(expected): warnings.append(f"actual {oid} has no frozen expectation")
    ids=set()
    for a in d.get("attributions",[]):
        aid=a.get("id")
        if not aid or aid in ids: issues.append("attribution id missing or duplicate")
        ids.add(aid)
        if a.get("outcome_id") not in expected or a.get("label") not in ATTR or not a.get("mechanism") or not a.get("evidence_id"): issues.append(f"{aid or 'attribution'} incomplete/invalid")
    lesson_ids=set()
    for x in d.get("lessons",[]):
        lid=x.get("id")
        if not lid or lid in lesson_ids: issues.append("lesson id missing or duplicate")
        lesson_ids.add(lid)
        if x.get("state") not in LESSON or not x.get("text") or not x.get("applicability") or not x.get("owner") or not x.get("review_trigger"): issues.append(f"{lid or 'lesson'} incomplete")
        if x.get("state")=="PROMOTED_ASSET":
            for k in ("provenance","limits","owner_approval","reviewer_approval"):
                if not x.get(k): issues.append(f"{lid} promoted asset missing {k}")
    return {"review_id":d.get("review_id"),"state":"NOT_REVIEWABLE" if issues else ("PROVISIONAL" if warnings else "COMPLETE"),"counts":{"expected":len(expected),"actual":len(actual_by),"attributions":len(d.get("attributions",[])),"lessons":len(d.get("lessons",[]))},"issues":sorted(set(issues)),"warnings":sorted(set(warnings))}

def main():
    p=argparse.ArgumentParser(); p.add_argument("input",type=Path); p.add_argument("--output",type=Path); a=p.parse_args()
    try: result=run(json.loads(a.input.read_text(encoding="utf-8")))
    except (OSError,TypeError,ValueError,json.JSONDecodeError) as e: print(f"ERROR: {e}",file=sys.stderr); return 2
    text=json.dumps(result,ensure_ascii=False,indent=2); a.output.write_text(text+"\n",encoding="utf-8") if a.output else print(text); return 0
if __name__=="__main__": raise SystemExit(main())
