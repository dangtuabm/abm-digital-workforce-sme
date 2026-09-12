#!/usr/bin/env python3
"""Deterministic improvement-contract linter and decision gate."""
import argparse, json, sys
from pathlib import Path

OPS={"<":lambda a,b:a<b,"<=":lambda a,b:a<=b,">":lambda a,b:a>b,">=":lambda a,b:a>=b,"==":lambda a,b:a==b}

def run(d):
    issues=[]; warnings=[]
    if not d.get("process_version") or not d.get("owner"): issues.append("missing process_version/owner")
    b=d.get("baseline",{})
    for k in ("metric","value","source_id","window","measurement_check","stable"):
        if b.get(k) is None or b.get(k)=="": issues.append(f"baseline missing {k}")
    h=d.get("hypothesis",{})
    for k in ("id","mechanism","prediction","falsification","alternatives"):
        if not h.get(k): issues.append(f"hypothesis missing {k}")
    e=d.get("experiment",{}); primary=e.get("primary",{})
    for k in ("change_version","owner","scope","comparison","sample","window","stop_rule","rollback"):
        if not e.get(k): issues.append(f"experiment missing {k}")
    if primary.get("operator") not in OPS or primary.get("threshold") is None or not primary.get("metric"): issues.append("primary acceptance invalid")
    cids=set()
    for c in e.get("countermetrics",[]):
        if not c.get("id") or c["id"] in cids or c.get("operator") not in OPS or c.get("threshold") is None: issues.append("countermetric invalid/duplicate")
        cids.add(c.get("id"))
    if issues: return {"improvement_id":d.get("improvement_id"),"state":"NOT_READY","issues":sorted(set(issues)),"warnings":warnings}
    if not b["stable"] or b["measurement_check"]!="passed": return {"improvement_id":d.get("improvement_id"),"state":"NOT_READY","issues":["baseline unstable or measurement check not passed"],"warnings":[]}
    r=d.get("result")
    if not r: return {"improvement_id":d.get("improvement_id"),"state":"RUNNING","issues":[],"warnings":[]}
    if r.get("primary_value") is None or not r.get("source_id"): return {"improvement_id":d.get("improvement_id"),"state":"INCONCLUSIVE","issues":["result missing primary/source"],"warnings":[]}
    cv=r.get("counter_values",{}); violations=[]; missing=[]
    for c in e.get("countermetrics",[]):
        if c["id"] not in cv: missing.append(c["id"])
        elif not OPS[c["operator"]](cv[c["id"]],c["threshold"]): violations.append(c["id"])
    if violations: state="ROLLBACK"
    elif missing or not r.get("window_complete"): state="INCONCLUSIVE"
    elif OPS[primary["operator"]](r["primary_value"],primary["threshold"]): state="ADOPT"
    else: state="REJECT"
    return {"improvement_id":d.get("improvement_id"),"state":state,"primary_pass":OPS[primary["operator"]](r["primary_value"],primary["threshold"]),"countermetric_violations":violations,"missing_countermetrics":missing,"issues":[],"warnings":warnings}

def main():
    p=argparse.ArgumentParser(); p.add_argument("input",type=Path); p.add_argument("--output",type=Path); a=p.parse_args()
    try: result=run(json.loads(a.input.read_text(encoding="utf-8")))
    except (OSError,TypeError,ValueError,json.JSONDecodeError) as e: print(f"ERROR: {e}",file=sys.stderr); return 2
    text=json.dumps(result,ensure_ascii=False,indent=2); a.output.write_text(text+"\n",encoding="utf-8") if a.output else print(text); return 0
if __name__=="__main__": raise SystemExit(main())
