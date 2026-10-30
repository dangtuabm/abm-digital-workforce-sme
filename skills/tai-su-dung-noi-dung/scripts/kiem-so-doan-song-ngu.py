#!/usr/bin/env python3
"""Kiểm sổ đoạn song ngữ (CSV): trùng mã, đoạn đích rỗng, thiếu/thừa biến và thẻ, vượt giới hạn ký tự.

Cách chạy:
    python -I -X utf8 kiem-so-doan-song-ngu.py <so-doan.csv>
    python -I -X utf8 kiem-so-doan-song-ngu.py --tu-kiem

Cột bắt buộc: ma_doan, ban_goc, ban_dich.
Cột tùy chọn: gioi_han_ky_tu, trang_thai_kiem (KHÓA / LOẠI TRỪ thì được phép để trống bản dịch).
Kết quả in ra dạng JSON; mã thoát 0 khi không có lỗi chặn, 1 khi có lỗi.
Script chỉ đọc file, không sửa, không gửi đi đâu.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import tempfile
from collections import Counter
from pathlib import Path

COT_BAT_BUOC = {"ma_doan", "ban_goc", "ban_dich"}
TRANG_THAI_DUOC_TRONG = {"KHÓA", "KHOA", "LOẠI TRỪ", "LOAI TRU"}
MAU_BIEN_THE = re.compile(
    r"\{\{[^{}]+\}\}|\$\{[^{}]+\}|\{[A-Za-z_][A-Za-z0-9_.-]*\}|%(?:\d+\$)?[sdif]|</?[A-Za-z][^>]*>"
)


def bien_va_the(chuoi: str) -> Counter:
    return Counter(MAU_BIEN_THE.findall(chuoi or ""))


def kiem(duong_dan: Path) -> dict:
    loi: list[dict] = []
    canh_bao: list[dict] = []
    so_dong = 0
    da_gap: set[str] = set()
    with duong_dan.open("r", encoding="utf-8-sig", newline="") as f:
        doc = csv.DictReader(f)
        cot = set(doc.fieldnames or [])
        thieu = sorted(COT_BAT_BUOC - cot)
        if thieu:
            return {"dat": False, "so_dong": 0, "loi": [{"loai": "thieu_cot", "cot": thieu}], "canh_bao": []}
        for dong, hang in enumerate(doc, start=2):
            so_dong += 1
            ma = (hang.get("ma_doan") or "").strip()
            goc = hang.get("ban_goc") or ""
            dich = hang.get("ban_dich") or ""
            trang_thai = (hang.get("trang_thai_kiem") or "").strip().upper()
            if not ma:
                loi.append({"dong": dong, "loai": "thieu_ma_doan"})
            elif ma in da_gap:
                loi.append({"dong": dong, "ma_doan": ma, "loai": "trung_ma_doan"})
            da_gap.add(ma)
            if goc and not dich and trang_thai not in TRANG_THAI_DUOC_TRONG:
                loi.append({"dong": dong, "ma_doan": ma, "loai": "ban_dich_rong"})
            if dich:
                bt_goc, bt_dich = bien_va_the(goc), bien_va_the(dich)
                if bt_goc != bt_dich:
                    loi.append({
                        "dong": dong,
                        "ma_doan": ma,
                        "loai": "lech_bien_hoac_the",
                        "thieu_o_ban_dich": list((bt_goc - bt_dich).elements()),
                        "thua_o_ban_dich": list((bt_dich - bt_goc).elements()),
                    })
            gioi_han = (hang.get("gioi_han_ky_tu") or "").strip()
            if gioi_han:
                try:
                    if len(dich) > int(gioi_han):
                        canh_bao.append({"dong": dong, "ma_doan": ma, "loai": "vuot_gioi_han_ky_tu",
                                         "thuc_te": len(dich), "gioi_han": int(gioi_han)})
                except ValueError:
                    loi.append({"dong": dong, "ma_doan": ma, "loai": "gioi_han_ky_tu_khong_hop_le", "gia_tri": gioi_han})
    return {"dat": not loi, "so_dong": so_dong, "so_ma_khac_nhau": len(da_gap), "loi": loi, "canh_bao": canh_bao}


def tu_kiem() -> dict:
    """Chạy hai ca: một file đạt và một file cố tình sai, kiểm script bắt đúng lỗi."""
    with tempfile.TemporaryDirectory() as thu_muc:
        dat = Path(thu_muc) / "dat.csv"
        dat.write_text(
            "ma_doan,ban_goc,ban_dich,gioi_han_ky_tu,trang_thai_kiem\n"
            'SEG-001,"Xin chào {name}","Hello {name}",30,CHỜ KIỂM\n'
            'SEG-002,"Mở <b>${file}</b>","Open <b>${file}</b>",30,CHỜ KIỂM\n'
            'SEG-003,"Tên sản phẩm","",,KHÓA\n',
            encoding="utf-8",
        )
        sai = Path(thu_muc) / "sai.csv"
        sai.write_text(
            "ma_doan,ban_goc,ban_dich,gioi_han_ky_tu,trang_thai_kiem\n"
            'SEG-001,"Thanh toán %s cho {name}","Pay for {name}",10,CHỜ KIỂM\n'
            'SEG-001,"Đóng","",,CHỜ KIỂM\n',
            encoding="utf-8",
        )
        kq_dat, kq_sai = kiem(dat), kiem(sai)
        loai_sai = sorted({x["loai"] for x in kq_sai["loi"]})
        mong_doi = ["ban_dich_rong", "lech_bien_hoac_the", "trung_ma_doan"]
        return {
            "tu_kiem": True,
            "dat": kq_dat["dat"] and not kq_sai["dat"] and loai_sai == mong_doi and len(kq_sai["canh_bao"]) == 1,
            "ca_dat": kq_dat,
            "ca_sai_bat_duoc": loai_sai,
        }


def main() -> int:
    p = argparse.ArgumentParser(description="Kiểm sổ đoạn song ngữ")
    p.add_argument("duong_dan_csv", nargs="?", type=Path)
    p.add_argument("--tu-kiem", action="store_true")
    a = p.parse_args()
    if a.tu_kiem:
        kq = tu_kiem()
    elif a.duong_dan_csv:
        kq = kiem(a.duong_dan_csv)
    else:
        p.error("cần đường dẫn file CSV hoặc --tu-kiem")
    print(json.dumps(kq, ensure_ascii=False, separators=(",", ":")))
    return 0 if kq["dat"] else 1


if __name__ == "__main__":
    sys.exit(main())
