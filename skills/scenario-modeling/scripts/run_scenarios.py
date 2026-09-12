#!/usr/bin/env python3
"""Safe deterministic scenario evaluator using Python standard library only."""
import argparse, ast, json, math, sys
from pathlib import Path

OPS={ast.Add:lambda a,b:a+b,ast.Sub:lambda a,b:a-b,ast.Mult:lambda a,b:a*b,ast.Div:lambda a,b:a/b,ast.Pow:lambda a,b:a**b,ast.USub:lambda a:-a,ast.UAdd:lambda a:+a}

def expr(text,env):
    def ev(n):
        if isinstance(n,ast.Expression): return ev(n.body)
        if isinstance(n,ast.Constant) and isinstance(n.value,(int,float)): return float(n.value)
        if isinstance(n,ast.Name) and n.id in env: return env[n.id]
        if isinstance(n,ast.BinOp) and type(n.op) in OPS: return OPS[type(n.op)](ev(n.left),ev(n.right))
        if isinstance(n,ast.UnaryOp) and type(n.op) in OPS: return OPS[type(n.op)](ev(n.operand))
        raise ValueError("unsafe or unknown formula element")
    value=ev(ast.parse(text,mode="eval"))
    if not math.isfinite(value): raise ValueError("non-finite result")
    return value

def evaluate(values,equations,outputs):
    env={k:float(v) for k,v in values.items()}
    for eq in equations:
        if eq["id"] in env: raise ValueError(f"duplicate name {eq['id']}")
        env[eq["id"]]=expr(eq["formula"],env)
    return {k:env[k] for k in outputs},env

def run(data):
    drivers=data["drivers"]; equations=data["equations"]; outputs=data["outputs"]
    scenarios={s["id"]:s for s in data["scenarios"]}
    results=[]
    opmap={"<":lambda a,b:a<b,"<=":lambda a,b:a<=b,">":lambda a,b:a>b,">=":lambda a,b:a>=b}
    for sid,s in scenarios.items():
        if set(s["values"])!=set(drivers): raise ValueError(f"{sid} driver set mismatch")
        for k,v in s["values"].items():
            d=drivers[k]
            if not d.get("source_id") or not d["min"]<=v<=d["max"]: raise ValueError(f"{sid}/{k} missing source or outside range")
        out,_=evaluate(s["values"],equations,outputs)
        hits=[t["id"] for t in data.get("triggers",[]) if t["operator"] in opmap and opmap[t["operator"]](out[t["metric"]],t["threshold"])]
        results.append({"id":sid,"outputs":out,"triggers":hits})
    sensitivity=[]
    for test in data.get("sensitivity",[]):
        base=dict(scenarios[test["scenario"]]["values"]); rows=[]
        for value in test["values"]:
            base[test["driver"]]=value
            out,_=evaluate(base,equations,outputs); rows.append({"value":value,"outputs":out})
        sensitivity.append({"scenario":test["scenario"],"driver":test["driver"],"rows":rows})
    breaks=[]
    for test in data.get("break_even",[]):
        base=dict(scenarios[test["scenario"]]["values"]); lo=float(test["low"]); hi=float(test["high"]); target=float(test["target"])
        def f(x): base[test["driver"]]=x; return evaluate(base,equations,outputs)[0][test["output"]]-target
        flo,fhi=f(lo),f(hi)
        if flo==0: root,status=lo,"FOUND"
        elif fhi==0: root,status=hi,"FOUND"
        elif flo*fhi>0: root,status=None,"NOT_BRACKETED"
        else:
            for _ in range(80):
                mid=(lo+hi)/2; fm=f(mid)
                if abs(fm)<1e-8: break
                if flo*fm<=0: hi=mid
                else: lo=mid; flo=fm
            root,status=(lo+hi)/2,"FOUND"
        breaks.append({"driver":test["driver"],"output":test["output"],"target":target,"status":status,"value":root})
    return {"model_id":data.get("model_id"),"scenarios":results,"sensitivity":sensitivity,"break_even":breaks}

def main():
    p=argparse.ArgumentParser(); p.add_argument("input",type=Path); p.add_argument("--output",type=Path); a=p.parse_args()
    try: result=run(json.loads(a.input.read_text(encoding="utf-8")))
    except (OSError,KeyError,ValueError,ZeroDivisionError,json.JSONDecodeError,SyntaxError) as e: print(f"ERROR: {e}",file=sys.stderr); return 2
    text=json.dumps(result,ensure_ascii=False,indent=2)
    a.output.write_text(text+"\n",encoding="utf-8") if a.output else print(text)
    return 0

if __name__=="__main__": raise SystemExit(main())
