#!/usr/bin/env python3
"""Deterministic integrity linter for Strategy Execution Control Packs."""
import argparse, json, sys
from pathlib import Path

ALLOWED={"NOT_STARTED","ON_TRACK","AT_RISK","OFF_TRACK","BLOCKED","DONE"}

def unique(rows,label,issues):
    ids=[x.get("id") for x in rows]
    if any(not x for x in ids) or len(ids)!=len(set(ids)): issues.append(f"{label} ids missing or duplicate")
    return {x.get("id"):x for x in rows if x.get("id")}

def run(d):
    issues=[]; warnings=[]
    if not d.get("strategy_version"): issues.append("missing strategy_version")
    if not d.get("allocation_version"): issues.append("missing allocation_version")
    obs=unique(d.get("objectives",[]),"objective",issues); krs=unique(d.get("krs",[]),"kr",issues); ins=unique(d.get("initiatives",[]),"initiative",issues)
    for oid,o in obs.items():
        if not o.get("outcome") or not o.get("owner"): issues.append(f"{oid} missing outcome/owner")
    for kid,k in krs.items():
        if k.get("objective_id") not in obs: issues.append(f"{kid} orphan objective")
        need=("baseline","target","source_id","owner","as_of","direction")
        if any(k.get(x) is None or k.get(x)=="" for x in need): issues.append(f"{kid} incomplete contract")
        elif k["baseline"]==k["target"]: issues.append(f"{kid} baseline equals target")
    for iid,x in ins.items():
        if not x.get("owner") or not x.get("resource_envelope") or not x.get("acceptance") or not x.get("stop_rule"): issues.append(f"{iid} incomplete charter")
        if not x.get("objective_ids") or any(o not in obs for o in x.get("objective_ids",[])): issues.append(f"{iid} orphan objective link")
        if not x.get("kr_ids") or any(k not in krs for k in x.get("kr_ids",[])): issues.append(f"{iid} orphan KR link")
        if any(dep not in ins for dep in x.get("dependencies",[])): issues.append(f"{iid} unknown dependency")
        status=x.get("status")
        if status not in ALLOWED: issues.append(f"{iid} invalid status")
        if status!="NOT_STARTED" and (not x.get("evidence_id") or not x.get("as_of")): issues.append(f"{iid} status lacks evidence/as_of")
    visiting=set(); done=set()
    def visit(i):
        if i in visiting: issues.append(f"dependency cycle at {i}"); return
        if i in done or i not in ins: return
        visiting.add(i)
        for dep in ins[i].get("dependencies",[]): visit(dep)
        visiting.remove(i); done.add(i)
    for i in ins: visit(i)
    linked={k for x in ins.values() for k in x.get("kr_ids",[])}
    for k in set(krs)-linked: warnings.append(f"{k} has no initiative")
    return {"execution_id":d.get("execution_id"),"state":"INVALID" if issues else ("PROVISIONAL" if warnings else "VALID"),"counts":{"objectives":len(obs),"krs":len(krs),"initiatives":len(ins)},"issues":sorted(set(issues)),"warnings":sorted(set(warnings))}

def main():
    p=argparse.ArgumentParser(); p.add_argument("input",type=Path); p.add_argument("--output",type=Path); a=p.parse_args()
    try: result=run(json.loads(a.input.read_text(encoding="utf-8")))
    except (OSError,TypeError,ValueError,json.JSONDecodeError) as e: print(f"ERROR: {e}",file=sys.stderr); return 2
    text=json.dumps(result,ensure_ascii=False,indent=2); a.output.write_text(text+"\n",encoding="utf-8") if a.output else print(text); return 0
if __name__=="__main__": raise SystemExit(main())
