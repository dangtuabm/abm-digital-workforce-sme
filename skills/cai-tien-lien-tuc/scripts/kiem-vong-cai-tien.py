#!/usr/bin/env python3
"""Kiểm hồ sơ một vòng cải tiến và đề xuất trạng thái.

Dùng: python -I -X utf8 kiem-vong-cai-tien.py <file-dau-vao.json> [--ra <file-ket-qua.json>]
Chỉ đọc file JSON đầu vào; không chạy mã, không mở mạng, không ghi vào hệ thống nào.
Trạng thái trả về là ĐỀ XUẤT, người có quyền mới quyết định.
"""
import argparse
import json
import sys
from pathlib import Path

PHEP_SO = {
    "<": lambda a, b: a < b,
    "<=": lambda a, b: a <= b,
    ">": lambda a, b: a > b,
    ">=": lambda a, b: a >= b,
    "==": lambda a, b: a == b,
}


def thieu(v):
    return v is None or v == "" or v == []


def kiem(d):
    loi = []
    if thieu(d.get("phien_ban_quy_trinh")) or thieu(d.get("nguoi_phu_trach")):
        loi.append("thiếu phiên bản quy trình hoặc người phụ trách")

    nen = d.get("so_lieu_nen", {})
    for k in ("chi_so", "gia_tri", "ma_nguon", "ky_do", "kiem_do_luong", "on_dinh"):
        if thieu(nen.get(k)):
            loi.append(f"số liệu nền thiếu {k}")

    gt = d.get("gia_thuyet", {})
    for k in ("ma", "co_che", "du_doan", "dieu_kien_bac_bo", "giai_thich_khac"):
        if thieu(gt.get(k)):
            loi.append(f"giả thuyết thiếu {k}")

    tn = d.get("thu_nghiem", {})
    for k in ("phien_ban_thay_doi", "nguoi_phu_trach", "pham_vi", "doi_chung",
              "co_mau", "thoi_gian", "dieu_kien_dung", "cach_quay_lai"):
        if thieu(tn.get(k)):
            loi.append(f"thử nghiệm thiếu {k}")

    chinh = tn.get("chi_so_chinh", {})
    if chinh.get("phep_so") not in PHEP_SO or chinh.get("nguong") is None or thieu(chinh.get("chi_so")):
        loi.append("chỉ số chính chưa có phép so hoặc ngưỡng hợp lệ")

    canh_bao = tn.get("chi_so_canh_bao", [])
    if not canh_bao:
        loi.append("chưa có chỉ số cảnh báo tác dụng phụ")
    da_co = set()
    for c in canh_bao:
        if thieu(c.get("ma")) or c.get("ma") in da_co or c.get("phep_so") not in PHEP_SO or c.get("nguong") is None:
            loi.append("chỉ số cảnh báo thiếu mã, trùng mã hoặc sai phép so/ngưỡng")
        da_co.add(c.get("ma"))

    ma = d.get("ma_cai_tien")
    if loi:
        return {"ma_cai_tien": ma, "trang_thai_de_xuat": "CHƯA SẴN SÀNG", "loi": sorted(set(loi))}

    if nen["on_dinh"] is not True or nen["kiem_do_luong"] != "dat":
        return {"ma_cai_tien": ma, "trang_thai_de_xuat": "CHƯA SẴN SÀNG",
                "loi": ["số liệu nền chưa ổn định hoặc cách đo chưa được kiểm"]}

    kq = d.get("ket_qua")
    if not kq:
        return {"ma_cai_tien": ma, "trang_thai_de_xuat": "ĐANG CHẠY", "loi": []}

    if kq.get("gia_tri_chinh") is None or thieu(kq.get("ma_nguon")):
        return {"ma_cai_tien": ma, "trang_thai_de_xuat": "CHƯA KẾT LUẬN",
                "loi": ["kết quả thiếu giá trị chỉ số chính hoặc nguồn"]}

    gia_tri_cb = kq.get("gia_tri_canh_bao", {})
    vi_pham, chua_co = [], []
    for c in canh_bao:
        if c["ma"] not in gia_tri_cb:
            chua_co.append(c["ma"])
        elif not PHEP_SO[c["phep_so"]](gia_tri_cb[c["ma"]], c["nguong"]):
            vi_pham.append(c["ma"])

    dat_chinh = PHEP_SO[chinh["phep_so"]](kq["gia_tri_chinh"], chinh["nguong"])
    if vi_pham:
        tt = "QUAY LẠI CÁCH CŨ"
    elif chua_co or kq.get("du_thoi_gian") is not True:
        tt = "CHƯA KẾT LUẬN"
    elif dat_chinh:
        tt = "ĐỀ XUẤT ÁP DỤNG"
    else:
        tt = "LOẠI BỎ"

    return {
        "ma_cai_tien": ma,
        "trang_thai_de_xuat": tt,
        "dat_chi_so_chinh": dat_chinh,
        "chi_so_canh_bao_vi_pham": vi_pham,
        "chi_so_canh_bao_chua_co_so": chua_co,
        "loi": [],
        "ghi_chu": "Đây là đề xuất của bộ kiểm, không phải quyết định. Người có quyền duyệt mới được áp dụng, quay lại hay mở rộng.",
    }


def main():
    p = argparse.ArgumentParser(description="Kiểm hồ sơ vòng cải tiến")
    p.add_argument("dau_vao", type=Path)
    p.add_argument("--ra", type=Path)
    a = p.parse_args()
    try:
        kq = kiem(json.loads(a.dau_vao.read_text(encoding="utf-8")))
    except (OSError, TypeError, ValueError, KeyError) as e:
        print(f"LỖI: {e}", file=sys.stderr)
        return 2
    text = json.dumps(kq, ensure_ascii=False, indent=2)
    if a.ra:
        a.ra.write_text(text + "\n", encoding="utf-8")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
