#!/usr/bin/env python3
"""Chạy mô phỏng kịch bản an toàn, tái lập được (chỉ dùng thư viện chuẩn Python).

Cách dùng:
    python -I -X utf8 chay-kich-ban.py <file-dau-vao.json> [--ghi <file-ket-qua.json>]

Đầu vào (tên trường tiếng Việt không dấu) — xem templates/dau-vao-mau-*.json:
    ma_mo_hinh, bien_dau_vao{ten: {don_vi, thap, cao, nguon}}, cong_thuc[{ma, bieu_thuc}],
    dau_ra[...], kich_ban[{ma, gia_tri{...}}], do_nhay[{kich_ban, bien, cac_gia_tri}],
    xep_hang_do_nhay[{kich_ban, dau_ra}], hoa_von[{kich_ban, bien, dau_ra, muc_tieu, thap, cao}],
    nguong[{ma, chi_so, phep_so, nguong}]

Công thức chỉ được dùng số, tên biến/công thức đã khai báo, + - * / ** và ngoặc.
Không chạy hàm, không đọc file, không mạng. Kết quả là số liệu mô hình, không phải phê duyệt.
"""
import argparse
import ast
import hashlib
import json
import math
import sys
from pathlib import Path

PHEP_TINH = {
    ast.Add: lambda a, b: a + b, ast.Sub: lambda a, b: a - b,
    ast.Mult: lambda a, b: a * b, ast.Div: lambda a, b: a / b,
    ast.Pow: lambda a, b: a ** b, ast.USub: lambda a: -a, ast.UAdd: lambda a: +a,
}
PHEP_SO = {"<": lambda a, b: a < b, "<=": lambda a, b: a <= b,
           ">": lambda a, b: a > b, ">=": lambda a, b: a >= b}


def tinh_bieu_thuc(text, env):
    def ev(n):
        if isinstance(n, ast.Expression):
            return ev(n.body)
        if isinstance(n, ast.Constant) and isinstance(n.value, (int, float)) and not isinstance(n.value, bool):
            return float(n.value)
        if isinstance(n, ast.Name):
            if n.id in env:
                return env[n.id]
            raise ValueError(f"tên chưa khai báo hoặc tính sau: {n.id}")
        if isinstance(n, ast.BinOp) and type(n.op) in PHEP_TINH:
            return PHEP_TINH[type(n.op)](ev(n.left), ev(n.right))
        if isinstance(n, ast.UnaryOp) and type(n.op) in PHEP_TINH:
            return PHEP_TINH[type(n.op)](ev(n.operand))
        raise ValueError(f"thành phần không được phép trong công thức: {ast.dump(n)[:60]}")
    v = ev(ast.parse(text, mode="eval"))
    if not math.isfinite(v):
        raise ValueError("kết quả không hữu hạn")
    return v


def tinh(gia_tri, cong_thuc, dau_ra):
    env = {k: float(v) for k, v in gia_tri.items()}
    for ct in cong_thuc:
        if ct["ma"] in env:
            raise ValueError(f"trùng tên: {ct['ma']}")
        env[ct["ma"]] = tinh_bieu_thuc(ct["bieu_thuc"], env)
    thieu = [k for k in dau_ra if k not in env]
    if thieu:
        raise ValueError(f"đầu ra chưa có công thức: {thieu}")
    return {k: env[k] for k in dau_ra}


def kiem_kich_ban(ma, gia_tri, bien):
    if set(gia_tri) != set(bien):
        thieu = sorted(set(bien) - set(gia_tri))
        thua = sorted(set(gia_tri) - set(bien))
        raise ValueError(f"{ma}: bộ biến không khớp (thiếu {thieu}, thừa {thua}) — thiếu không được coi là 0")
    for k, v in gia_tri.items():
        b = bien[k]
        if not b.get("nguon"):
            raise ValueError(f"{ma}/{k}: biến chưa có nguồn")
        if not (b["thap"] <= v <= b["cao"]):
            raise ValueError(f"{ma}/{k}={v} nằm ngoài dải đã duyệt [{b['thap']}, {b['cao']}]")


def chay(d):
    bien, cong_thuc, dau_ra = d["bien_dau_vao"], d["cong_thuc"], d["dau_ra"]
    kich_ban = {k["ma"]: k for k in d["kich_ban"]}
    ket_qua = []
    for ma, kb in kich_ban.items():
        kiem_kich_ban(ma, kb["gia_tri"], bien)
        out = tinh(kb["gia_tri"], cong_thuc, dau_ra)
        cham = [n["ma"] for n in d.get("nguong", [])
                if n["phep_so"] in PHEP_SO and PHEP_SO[n["phep_so"]](out[n["chi_so"]], n["nguong"])]
        ket_qua.append({"kich_ban": ma, "dau_ra": out, "nguong_bi_cham": cham})

    do_nhay = []
    for t in d.get("do_nhay", []):
        goc = dict(kich_ban[t["kich_ban"]]["gia_tri"])
        dong = []
        for v in t["cac_gia_tri"]:
            goc[t["bien"]] = v
            dong.append({"gia_tri": v, "dau_ra": tinh(goc, cong_thuc, dau_ra)})
        do_nhay.append({"kich_ban": t["kich_ban"], "bien": t["bien"], "ket_qua": dong})

    xep_hang = []
    for t in d.get("xep_hang_do_nhay", []):
        goc = kich_ban[t["kich_ban"]]["gia_tri"]
        hang = []
        for ten, b in bien.items():
            thu = dict(goc)
            thu[ten] = b["thap"]
            o_thap = tinh(thu, cong_thuc, dau_ra)[t["dau_ra"]]
            thu[ten] = b["cao"]
            o_cao = tinh(thu, cong_thuc, dau_ra)[t["dau_ra"]]
            hang.append({"bien": ten, "khi_bien_thap": o_thap, "khi_bien_cao": o_cao,
                         "do_rong": abs(o_cao - o_thap)})
        hang.sort(key=lambda x: x["do_rong"], reverse=True)
        xep_hang.append({"kich_ban": t["kich_ban"], "dau_ra": t["dau_ra"], "xep_hang": hang,
                         "luu_y": "Thay từng biến một trong dải đã duyệt, giữ các biến khác; có thể phá quan hệ giữa các biến."})

    hoa_von = []
    for t in d.get("hoa_von", []):
        goc = dict(kich_ban[t["kich_ban"]]["gia_tri"])
        lo, hi, muc_tieu = float(t["thap"]), float(t["cao"]), float(t["muc_tieu"])

        def f(x):
            goc[t["bien"]] = x
            return tinh(goc, cong_thuc, dau_ra)[t["dau_ra"]] - muc_tieu
        flo, fhi = f(lo), f(hi)
        if flo == 0:
            goc_tim, tt = lo, "TÌM ĐƯỢC"
        elif fhi == 0:
            goc_tim, tt = hi, "TÌM ĐƯỢC"
        elif flo * fhi > 0:
            goc_tim, tt = None, "KHÔNG NẰM TRONG KHOẢNG"
        else:
            for _ in range(100):
                mid = (lo + hi) / 2
                fm = f(mid)
                if abs(fm) < 1e-9:
                    break
                if flo * fm <= 0:
                    hi = mid
                else:
                    lo, flo = mid, fm
            goc_tim, tt = (lo + hi) / 2, "TÌM ĐƯỢC"
        hoa_von.append({"kich_ban": t["kich_ban"], "bien": t["bien"], "dau_ra": t["dau_ra"],
                        "muc_tieu": muc_tieu, "trang_thai": tt, "gia_tri": goc_tim})

    return {"ma_mo_hinh": d.get("ma_mo_hinh"), "ket_qua_kich_ban": ket_qua, "do_nhay": do_nhay,
            "xep_hang_do_nhay": xep_hang, "hoa_von": hoa_von,
            "ghi_chu": "Kết quả mô hình, không phải xác suất, không phải phê duyệt."}


def main():
    p = argparse.ArgumentParser(description="Chạy mô phỏng kịch bản")
    p.add_argument("dau_vao", type=Path)
    p.add_argument("--ghi", type=Path, help="ghi kết quả ra file JSON")
    a = p.parse_args()
    try:
        raw = a.dau_vao.read_bytes()
        kq = chay(json.loads(raw.decode("utf-8")))
        kq["ma_bam_dau_vao_sha256"] = hashlib.sha256(raw).hexdigest()
    except (OSError, KeyError, ValueError, TypeError, ZeroDivisionError, json.JSONDecodeError, SyntaxError) as e:
        print(f"LỖI: {e}", file=sys.stderr)
        return 2
    text = json.dumps(kq, ensure_ascii=False, indent=2)
    if a.ghi:
        a.ghi.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
