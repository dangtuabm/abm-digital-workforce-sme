#!/usr/bin/env python3
"""Kiểm bảng chỉ số khảo sát: mã trùng, tử số/mẫu số hợp lệ, tỷ lệ báo cáo khớp phép tính, cỡ mẫu nhỏ.

Dùng:
    python -I -X utf8 kiem_chi_so_khao_sat.py <bang-chi-so.csv> [--sai-so 0.05] [--co-mau-nho 30]
    python -I -X utf8 kiem_chi_so_khao_sat.py --tu-kiem

Cột bắt buộc: ma_chi_so, tu_so, mau_so, ty_le_bao_cao, n_chua_gia_quyen.
Kết quả in ra dạng JSON; mã thoát 0 khi không có lỗi, 1 khi có lỗi.
Script chỉ đọc file, không ghi, không gọi mạng.
"""

from __future__ import annotations

import argparse
import csv
import json
import sys
import tempfile
from decimal import Decimal, InvalidOperation
from pathlib import Path

COT_BAT_BUOC = {"ma_chi_so", "tu_so", "mau_so", "ty_le_bao_cao", "n_chua_gia_quyen"}


def so(gia_tri: str) -> Decimal:
    return Decimal((gia_tri or "").strip().replace(",", "."))


def kiem(duong_dan: Path, sai_so: Decimal = Decimal("0.05"), co_mau_nho: int = 30) -> dict:
    loi: list[dict] = []
    nhac: list[dict] = []
    da_gap: set[str] = set()
    so_dong = 0
    with duong_dan.open("r", encoding="utf-8-sig", newline="") as f:
        doc = csv.DictReader(f)
        thieu = sorted(COT_BAT_BUOC - set(doc.fieldnames or []))
        if thieu:
            return {"dat": False, "so_dong": 0, "loi": [{"loai": "thieu_cot", "cot": thieu}], "nhac": []}
        for dong, hang in enumerate(doc, start=2):
            so_dong += 1
            ma = (hang.get("ma_chi_so") or "").strip()
            if not ma:
                loi.append({"dong": dong, "loai": "thieu_ma_chi_so"})
            elif ma in da_gap:
                loi.append({"dong": dong, "ma_chi_so": ma, "loai": "trung_ma_chi_so"})
            da_gap.add(ma)
            try:
                tu = so(hang["tu_so"])
                mau = so(hang["mau_so"])
                bao_cao = so(hang["ty_le_bao_cao"])
                n = so(hang["n_chua_gia_quyen"])
            except (InvalidOperation, KeyError):
                loi.append({"dong": dong, "ma_chi_so": ma, "loai": "khong_phai_so"})
                continue
            if mau <= 0 or tu < 0 or tu > mau:
                loi.append({"dong": dong, "ma_chi_so": ma, "loai": "tu_so_mau_so_khong_hop_le",
                            "tu_so": str(tu), "mau_so": str(mau)})
                continue
            tinh_ra = tu / mau * Decimal(100)
            if abs(tinh_ra - bao_cao) > sai_so:
                loi.append({"dong": dong, "ma_chi_so": ma, "loai": "ty_le_khong_khop",
                            "tinh_ra": str(round(tinh_ra, 2)), "bao_cao": str(bao_cao)})
            if n <= 0:
                loi.append({"dong": dong, "ma_chi_so": ma, "loai": "co_mau_khong_hop_le"})
            elif n < co_mau_nho:
                nhac.append({"dong": dong, "ma_chi_so": ma, "loai": "co_mau_nho", "n_chua_gia_quyen": str(n)})
    return {"dat": not loi, "so_dong": so_dong, "so_ma": len(da_gap), "loi": loi, "nhac": nhac}


def tu_kiem() -> dict:
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "mau.csv"
        p.write_text(
            "ma_chi_so,tu_so,mau_so,ty_le_bao_cao,n_chua_gia_quyen\n"
            "CS-001,70,100,70,100\n"
            "CS-002,45,60,75,60\n"
            "CS-003,9,12,75,12\n",
            encoding="utf-8",
        )
        ket_qua = kiem(p)
        ket_qua["tu_kiem"] = True
        ket_qua["mong_doi"] = "dat=true, 1 dong nhac co_mau_nho (CS-003)"
        return ket_qua


def main() -> int:
    ap = argparse.ArgumentParser(description="Kiểm bảng chỉ số khảo sát")
    ap.add_argument("duong_dan", nargs="?", type=Path)
    ap.add_argument("--sai-so", default="0.05", help="Sai số cho phép giữa tỷ lệ tính ra và tỷ lệ báo cáo (điểm %)")
    ap.add_argument("--co-mau-nho", type=int, default=30, help="Dưới ngưỡng này thì nhắc cỡ mẫu nhỏ (mặc định 30, doanh nghiệp tự chỉnh)")
    ap.add_argument("--tu-kiem", action="store_true")
    a = ap.parse_args()
    if a.tu_kiem:
        kq = tu_kiem()
    elif a.duong_dan:
        kq = kiem(a.duong_dan, Decimal(a.sai_so), a.co_mau_nho)
    else:
        ap.error("cần đường dẫn file CSV hoặc --tu-kiem")
        return 2
    print(json.dumps(kq, ensure_ascii=False, separators=(",", ":")))
    return 0 if kq["dat"] else 1


if __name__ == "__main__":
    sys.exit(main())
