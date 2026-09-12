#!/usr/bin/env python3
"""Deterministic capacity-constrained portfolio allocator for small portfolios."""
import argparse, itertools, json, sys
from pathlib import Path

def run(d):
    caps={k:v["total"]-v.get("committed",0)-v.get("operations",0)-v.get("buffer",0) for k,v in d["capacities"].items()}
    if any(v<0 for v in caps.values()): return {"allocation_id":d.get("allocation_id"),"state":"INFEASIBLE","reason":"negative usable capacity","usable":caps}
    items={x["id"]:x for x in d["items"]}
    if len(items)!=len(d["items"]): raise ValueError("item ids must be unique")
    for x in items.values():
        if not x.get("value_source"): raise ValueError(f"{x['id']} missing value_source")
        if any(r not in caps or v<0 for r,v in x.get("resources",{}).items()): raise ValueError(f"{x['id']} invalid resources")
        if any(y not in items for y in x.get("dependencies",[])): raise ValueError(f"{x['id']} unknown dependency")
    mandatory={x["id"] for x in items.values() if x.get("mandatory")}
    def close(sel):
        sel=set(sel); changed=True
        while changed:
            changed=False
            for i in list(sel):
                for dep in items[i].get("dependencies",[]):
                    if dep not in sel: sel.add(dep); changed=True
        return sel
    mandatory=close(mandatory)
    optional=sorted(set(items)-mandatory)
    if len(optional)>22: raise ValueError("more than 22 optional items; use approved optimization solver")
    limits=d.get("category_limits",{}); max_selected=d.get("max_selected",len(items))
    def check(sel):
        sel=close(sel)
        if len(sel)>max_selected: return None
        for i in sel:
            if set(items[i].get("excludes",[])) & sel: return None
        used={r:sum(items[i].get("resources",{}).get(r,0) for i in sel) for r in caps}
        if any(used[r]>caps[r] for r in caps): return None
        counts={c:sum(items[i].get("category")==c for i in sel) for c in limits}
        if any(counts[c]<v.get("min",0) or counts[c]>v.get("max",len(items)) for c,v in limits.items()): return None
        value=sum(items[i]["approved_value"] for i in sel)
        load=sum(used[r]/caps[r] for r in caps if caps[r]>0)
        return sel,used,value,load
    base=check(mandatory)
    if base is None: return {"allocation_id":d.get("allocation_id"),"state":"INFEASIBLE","reason":"mandatory/constraints exceed capacity","mandatory":sorted(mandatory),"usable":caps}
    best=None
    for n in range(len(optional)+1):
        for combo in itertools.combinations(optional,n):
            candidate=check(mandatory|set(combo))
            if candidate is None: continue
            key=(candidate[2],-candidate[3],tuple(sorted(candidate[0])))
            if best is None or key>best[0]: best=(key,candidate)
    sel,used,value,_=best[1]
    remaining={r:caps[r]-used[r] for r in caps}
    deferred=sorted(set(items)-sel,key=lambda i:(-items[i]["approved_value"],i))
    return {"allocation_id":d.get("allocation_id"),"state":"FEASIBLE","selected":sorted(sel),"deferred":deferred,"total_value":value,"usable":caps,"used":used,"remaining":remaining,"best_deferred":deferred[0] if deferred else None}

def main():
    p=argparse.ArgumentParser(); p.add_argument("input",type=Path); p.add_argument("--output",type=Path); a=p.parse_args()
    try: result=run(json.loads(a.input.read_text(encoding="utf-8")))
    except (OSError,KeyError,TypeError,ValueError,json.JSONDecodeError) as e: print(f"ERROR: {e}",file=sys.stderr); return 2
    text=json.dumps(result,ensure_ascii=False,indent=2); a.output.write_text(text+"\n",encoding="utf-8") if a.output else print(text); return 0
if __name__=="__main__": raise SystemExit(main())
