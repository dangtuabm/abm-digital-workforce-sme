#!/usr/bin/env python3
"""Kiểm cấu trúc tối thiểu của file CSV trích xuất dữ liệu.

Dùng:
  python -I -X utf8 kiem_file_trich_xuat.py <file.csv>
  python -I -X utf8 kiem_file_trich_xuat.py <file.csv> --bat-buoc ma_ban_ghi,vi_tri_nguon,trang_thai_trich,so_hoa_don

Chỉ đọc file, không sửa dữ liệu. In báo cáo JSON; mã thoát 0 = ĐẠT, 1 = CÓ LỖI, 2 = không đọc được file.
"""

import argparse
import csv
import json
import sys
from pathlib import Path

TRANG_THAI_HOP_LE = {"KHỚP NGUỒN", "CẦN SOÁT", "MƠ HỒ", "THIẾU", "SAI ĐỊNH DẠNG"}
MAC_DINH_BAT_BUOC = "ma_ban_ghi,vi_tri_nguon,trang_thai_trich"


def kiem(stream, bat_buoc, cot_ma, cot_nguon, cot_trang_thai):
    reader = csv.DictReader(stream)
    tieu_de = reader.fieldnames or []
    loi, nhac = [], []
    if not tieu_de:
        return {"ket_qua": "CÓ LỖI", "so_dong": 0, "loi": [{"ma": "KHONG_CO_TIEU_DE"}], "nhac": []}

    trung = sorted({h for h in tieu_de if tieu_de.count(h) > 1})
    if trung:
        loi.append({"ma": "TIEU_DE_TRUNG", "cot": trung})
    for cot in bat_buoc:
        if cot not in tieu_de:
            loi.append({"ma": "THIEU_COT", "cot": cot})

    da_thay, so_dong, dem_trang_thai = set(), 0, {}
    for dong, row in enumerate(reader, start=2):
        so_dong += 1
        for cot in bat_buoc:
            if cot in tieu_de and not (row.get(cot) or "").strip():
                trang_thai = (row.get(cot_trang_thai) or "").strip()
                # Ô trống ở trường nghiệp vụ được chấp nhận khi dòng đã được đánh dấu THIẾU/MƠ HỒ
                if cot not in (cot_ma, cot_nguon, cot_trang_thai) and trang_thai in {"THIẾU", "MƠ HỒ"}:
                    continue
                loi.append({"ma": "O_BAT_BUOC_TRONG", "dong": dong, "cot": cot})
        ma = (row.get(cot_ma) or "").strip()
        if ma:
            if ma in da_thay:
                loi.append({"ma": "TRUNG_MA_BAN_GHI", "dong": dong, "gia_tri": ma})
            da_thay.add(ma)
        tt = (row.get(cot_trang_thai) or "").strip()
        if cot_trang_thai in tieu_de and tt:
            if tt not in TRANG_THAI_HOP_LE:
                loi.append({"ma": "TRANG_THAI_SAI", "dong": dong, "gia_tri": tt})
            dem_trang_thai[tt] = dem_trang_thai.get(tt, 0) + 1

    if so_dong == 0:
        nhac.append({"ma": "KHONG_CO_DONG_DU_LIEU"})
    can_xu_ly = sum(v for k, v in dem_trang_thai.items() if k != "KHỚP NGUỒN")
    if can_xu_ly:
        nhac.append({"ma": "CON_DONG_CAN_XU_LY", "so_dong": can_xu_ly,
                     "ghi_chu": "Đưa các dòng này vào Sổ ngoại lệ trước khi bàn giao"})
    return {
        "ket_qua": "ĐẠT" if not loi else "CÓ LỖI",
        "so_dong": so_dong,
        "so_ma_khac_nhau": len(da_thay),
        "dem_theo_trang_thai": dem_trang_thai,
        "loi": loi,
        "nhac": nhac,
    }


def main():
    p = argparse.ArgumentParser(description="Kiểm file CSV trích xuất dữ liệu")
    p.add_argument("file_csv", type=Path)
    p.add_argument("--bat-buoc", default=MAC_DINH_BAT_BUOC, help="các cột bắt buộc, cách nhau bằng dấu phẩy")
    p.add_argument("--cot-ma", default="ma_ban_ghi")
    p.add_argument("--cot-nguon", default="vi_tri_nguon")
    p.add_argument("--cot-trang-thai", default="trang_thai_trich")
    a = p.parse_args()
    try:
        with a.file_csv.open("r", encoding="utf-8-sig", newline="") as f:
            bao_cao = kiem(f, [c.strip() for c in a.bat_buoc.split(",") if c.strip()],
                           a.cot_ma, a.cot_nguon, a.cot_trang_thai)
    except OSError as exc:
        print(json.dumps({"ket_qua": "KHÔNG ĐỌC ĐƯỢC FILE", "chi_tiet": str(exc)}, ensure_ascii=False))
        return 2
    print(json.dumps(bao_cao, ensure_ascii=False, indent=2))
    return 0 if bao_cao["ket_qua"] == "ĐẠT" else 1


if __name__ == "__main__":
    sys.exit(main())
