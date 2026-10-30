#!/usr/bin/env python3
"""Kiểm kế hoạch thực thi và ngân sách: truy vết mục tiêu → chỉ số → sáng kiến → dòng ngân sách,
phụ thuộc vòng, trạng thái có căn cứ, ngân sách không vượt mức đã duyệt, chênh lệch kế hoạch – thực tế.

Dùng: python -I -X utf8 kiem-ke-hoach-ngan-sach.py <file.json> [--ghi <file_ket_qua.json>]
Mẫu đầu vào: templates/du-lieu-ke-hoach-mau.json
Script chỉ đọc file đầu vào, không chạy mã, không mở mạng, không ghi vào phần mềm kế toán.
"""
import argparse
import json
import sys
from pathlib import Path

TRANG_THAI = {"CHƯA BẮT ĐẦU", "ĐÚNG HƯỚNG", "CÓ RỦI RO", "CHỆCH HƯỚNG", "BỊ CHẶN", "HOÀN THÀNH"}


def trong(v):
    return v is None or v == "" or v == [] or v == {}


def theo_ma(ds, nhan, loi):
    ma = [x.get("ma") for x in ds]
    if any(not m for m in ma) or len(ma) != len(set(ma)):
        loi.append(f"{nhan}: thiếu hoặc trùng mã")
    return {x.get("ma"): x for x in ds if x.get("ma")}


def kiem(d):
    loi, nhac = [], []
    for k in ("phien_ban_muc_tieu", "phien_ban_phan_bo"):
        if trong(d.get(k)):
            loi.append(f"thiếu {k}")
    mt = theo_ma(d.get("muc_tieu", []), "mục tiêu", loi)
    cs = theo_ma(d.get("chi_so", []), "chỉ số", loi)
    sk = theo_ma(d.get("sang_kien", []), "sáng kiến", loi)
    for m, x in mt.items():
        if trong(x.get("ket_qua")) or trong(x.get("nguoi_phu_trach")):
            loi.append(f"{m}: thiếu kết quả mong muốn hoặc người phụ trách")
    for m, x in cs.items():
        if x.get("ma_muc_tieu") not in mt:
            loi.append(f"{m}: không gắn với mục tiêu nào")
        if any(trong(x.get(k)) for k in ("dau_ky", "muc_tieu", "chieu", "nguon", "nguoi_phu_trach", "tinh_den")):
            loi.append(f"{m}: chỉ số thiếu đầu kỳ/mục tiêu/chiều/nguồn/người phụ trách/ngày")
        elif x["dau_ky"] == x["muc_tieu"]:
            loi.append(f"{m}: mục tiêu bằng đầu kỳ")
    for m, x in sk.items():
        for k in ("nguoi_phu_trach", "tieu_chi_nghiem_thu", "quy_tac_dung"):
            if trong(x.get(k)):
                loi.append(f"{m}: sáng kiến thiếu {k}")
        if x.get("ngan_sach_duoc_phan_bo") is None:
            loi.append(f"{m}: chưa có ngân sách được phân bổ")
        if not x.get("ma_muc_tieu") or any(o not in mt for o in x.get("ma_muc_tieu", [])):
            loi.append(f"{m}: không truy được về mục tiêu")
        if not x.get("ma_chi_so") or any(k not in cs for k in x.get("ma_chi_so", [])):
            loi.append(f"{m}: không truy được về chỉ số")
        if any(p not in sk for p in x.get("phu_thuoc", [])):
            loi.append(f"{m}: phụ thuộc vào sáng kiến không có")
        tt = x.get("trang_thai")
        if tt not in TRANG_THAI:
            loi.append(f"{m}: trạng thái không hợp lệ")
        elif tt != "CHƯA BẮT ĐẦU" and (trong(x.get("can_cu")) or trong(x.get("tinh_den"))):
            loi.append(f"{m}: trạng thái {tt} nhưng thiếu căn cứ hoặc ngày")
    dang_xet, xong = set(), set()

    def tham(i):
        if i in dang_xet:
            loi.append(f"phụ thuộc vòng tại {i}")
            return
        if i in xong or i not in sk:
            return
        dang_xet.add(i)
        for p in sk[i].get("phu_thuoc", []):
            tham(p)
        dang_xet.discard(i)
        xong.add(i)

    for i in sk:
        tham(i)
    co_sk = {k for x in sk.values() for k in x.get("ma_chi_so", [])}
    for k in set(cs) - co_sk:
        nhac.append(f"{k}: chưa có sáng kiến nào đóng góp (ghi rõ nếu chỉ theo dõi)")

    ns = d.get("ngan_sach", {})
    tong_duyet = ns.get("tong_da_duyet")
    nguong = ns.get("nguong_canh_bao_phan_tram")
    if tong_duyet is None:
        loi.append("ngân sách: thiếu tổng đã duyệt")
    if nguong is None:
        nhac.append("ngân sách: chưa đặt ngưỡng cảnh báo chênh lệch")
    dong = theo_ma(ns.get("dong", []), "dòng ngân sách", loi)
    ke_hoach_theo_sk, thuc_te_theo_sk, chenh = {}, {}, []
    for m, x in dong.items():
        s = x.get("ma_sang_kien")
        if s not in sk:
            loi.append(f"{m}: dòng ngân sách không gắn với sáng kiến nào")
        if any(trong(x.get(k)) for k in ("khoan_muc", "ky")) or not isinstance(x.get("ke_hoach"), (int, float)):
            loi.append(f"{m}: thiếu khoản mục/kỳ/số kế hoạch")
            continue
        ke_hoach_theo_sk[s] = ke_hoach_theo_sk.get(s, 0) + x["ke_hoach"]
        if x.get("thuc_te") is not None:
            if trong(x.get("nguon_thuc_te")):
                loi.append(f"{m}: có số thực tế nhưng thiếu nguồn")
                continue
            thuc_te_theo_sk[s] = thuc_te_theo_sk.get(s, 0) + x["thuc_te"]
            c = x["thuc_te"] - x["ke_hoach"]
            pt = round(c / x["ke_hoach"] * 100, 1) if x["ke_hoach"] else None
            vuot = nguong is not None and pt is not None and abs(pt) > nguong
            chenh.append({"ma": m, "sang_kien": s, "khoan_muc": x["khoan_muc"], "ky": x["ky"],
                          "ke_hoach": x["ke_hoach"], "thuc_te": x["thuc_te"], "chenh": round(c, 4),
                          "phan_tram": pt, "vuot_nguong": vuot})
            if vuot and trong(x.get("giai_thich")):
                nhac.append(f"{m}: chênh lệch {pt}% vượt ngưỡng, chưa có giải thích")
    for s, v in ke_hoach_theo_sk.items():
        duoc = sk.get(s, {}).get("ngan_sach_duoc_phan_bo")
        if isinstance(duoc, (int, float)) and v > duoc:
            loi.append(f"{s}: tổng dòng ngân sách {v} vượt mức được phân bổ {duoc}")
    tong_ke_hoach = sum(ke_hoach_theo_sk.values())
    tong_phan_bo = sum(x.get("ngan_sach_duoc_phan_bo") or 0 for x in sk.values())
    if isinstance(tong_duyet, (int, float)):
        if tong_phan_bo > tong_duyet:
            loi.append(f"tổng phân bổ {tong_phan_bo} vượt tổng ngân sách đã duyệt {tong_duyet}")
        if tong_ke_hoach > tong_duyet:
            loi.append(f"tổng dòng ngân sách {tong_ke_hoach} vượt tổng đã duyệt {tong_duyet}")
    trang_thai = "KHÔNG HỢP LỆ" if loi else ("TẠM THỜI" if nhac else "HỢP LỆ")
    return {"ma_ke_hoach": d.get("ma_ke_hoach"), "trang_thai": trang_thai,
            "so_luong": {"muc_tieu": len(mt), "chi_so": len(cs), "sang_kien": len(sk), "dong_ngan_sach": len(dong)},
            "ngan_sach": {"tong_da_duyet": tong_duyet, "tong_phan_bo": tong_phan_bo, "tong_ke_hoach": tong_ke_hoach,
                          "ke_hoach_theo_sang_kien": ke_hoach_theo_sk, "thuc_te_theo_sang_kien": thuc_te_theo_sk},
            "chenh_lech": chenh, "loi": sorted(set(loi)), "nhac": sorted(set(nhac))}


def main():
    p = argparse.ArgumentParser(description="Kiểm kế hoạch thực thi và ngân sách")
    p.add_argument("dau_vao", type=Path)
    p.add_argument("--ghi", type=Path)
    a = p.parse_args()
    try:
        kq = kiem(json.loads(a.dau_vao.read_text(encoding="utf-8")))
    except (OSError, TypeError, ValueError, AttributeError) as e:
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
