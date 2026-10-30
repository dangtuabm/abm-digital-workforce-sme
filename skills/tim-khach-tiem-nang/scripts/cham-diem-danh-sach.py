"""Chấm điểm ưu tiên và gắn cờ cho danh sách khách tiềm năng.

Dùng:
  python -I -X utf8 cham-diem-danh-sach.py <danh-sach.csv> [--trong-so 35,30,20,15] [--top 20] [--ra ket-qua.csv]

Đầu vào: CSV theo templates/danh-sach-khach-tiem-nang.csv (tiêu đề cột tiếng Việt không dấu).
Không gửi dữ liệu đi đâu, không sửa file gốc. Chỉ đọc file và in kết quả (hoặc ghi file --ra).
"""
import argparse
import csv
import re
import sys
import unicodedata

CHIEU = ["diem_phu_hop", "diem_tin_hieu", "diem_tiep_can", "diem_gia_tri"]
CO_CHAN = {"TU_CHOI_LIEN_HE", "THIEU_NGUON", "KHONG_KENH_HOP_LE", "TRUNG", "CHUA_DOI_CHIEU_CRM"}
TU_BO = r"\b(cong ty|cty|tnhh|co phan|cp|mtv|jsc|ltd|chi nhanh|cn|tap doan|hkd|ho kinh doanh)\b"


def bo_dau(s):
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("đ", "d").replace("Đ", "D").lower()


def khoa_ten(ten):
    s = re.sub(TU_BO, " ", bo_dau(ten))
    return re.sub(r"[^a-z0-9]+", "", s)


def la_trong(v):
    v = (v or "").strip()
    return v == "" or (v.startswith("[") and v.endswith("]"))


def doc_diem(v):
    if la_trong(v):
        return None
    try:
        d = float(v)
    except ValueError:
        return None
    return d if 0 <= d <= 3 else None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--trong-so", default="35,30,20,15")
    ap.add_argument("--top", type=int, default=0)
    ap.add_argument("--ra", default="")
    a = ap.parse_args()

    ts = [float(x) for x in a.trong_so.split(",")]
    if len(ts) != 4 or abs(sum(ts) - 100) > 0.01:
        sys.exit("LỖI: --trong-so cần 4 số, tổng 100 (phù hợp, tín hiệu, tiếp cận, giá trị)")

    with open(a.file, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("LỖI: file không có dòng dữ liệu")
    thieu_cot = [c for c in CHIEU + ["ten_doanh_nghiep", "nguon", "ngay_lay", "kenh_lien_he_hop_le",
                                     "co_trong_crm", "tu_choi_lien_he"] if c not in rows[0]]
    if thieu_cot:
        sys.exit("LỖI: thiếu cột " + ", ".join(thieu_cot))

    gap_ten, gap_mst = {}, {}
    for i, r in enumerate(rows):
        r["_co"] = []
        k = khoa_ten(r.get("ten_doanh_nghiep", ""))
        mst = re.sub(r"\D", "", r.get("ma_so_thue", "") or "")
        for khoa, so in ((k, gap_ten), (mst, gap_mst)):
            if khoa and not la_trong(r.get("ten_doanh_nghiep")):
                if khoa in so:
                    r["_co"].append("TRUNG")
                    r["_trung_voi"] = rows[so[khoa]].get("ma", str(so[khoa] + 1))
                    break
                so[khoa] = i

    for r in rows:
        co = r["_co"]
        if bo_dau(r.get("tu_choi_lien_he", "")).strip() in ("co", "x", "yes"):
            co.append("TU_CHOI_LIEN_HE")
        if la_trong(r.get("nguon")) or la_trong(r.get("ngay_lay")):
            co.append("THIEU_NGUON")
        if la_trong(r.get("kenh_lien_he_hop_le")):
            co.append("KHONG_KENH_HOP_LE")
        crm = bo_dau(r.get("co_trong_crm", "")).strip()
        if crm in ("co", "x", "yes"):
            co.append("DA_CO_TRONG_CRM")
        elif crm not in ("khong", "no"):
            co.append("CHUA_DOI_CHIEU_CRM")
        diem = [doc_diem(r.get(c)) for c in CHIEU]
        if any(d is None for d in diem):
            co.append("THIEU_DIEM")
            r["diem_uu_tien"] = ""
        else:
            r["diem_uu_tien"] = round(sum(w * d / 3 for w, d in zip(ts, diem)), 1)
        r["co_canh_bao"] = ";".join(dict.fromkeys(co))
        r["duoc_giao_goi"] = "khong" if (set(co) & CO_CHAN or "THIEU_DIEM" in co) else "co"

    xep = sorted(rows, key=lambda r: (r["duoc_giao_goi"] != "co",
                                      -(r["diem_uu_tien"] if r["diem_uu_tien"] != "" else -1)))
    n_goi = sum(r["duoc_giao_goi"] == "co" for r in rows)
    print(f"Trọng số: phù hợp {ts[0]:g} · tín hiệu {ts[1]:g} · tiếp cận {ts[2]:g} · giá trị {ts[3]:g}")
    print(f"Tổng dòng: {len(rows)} · Được giao gọi: {n_goi} · Bị chặn/thiếu: {len(rows) - n_goi}")
    dem = {}
    for r in rows:
        for c in filter(None, r["co_canh_bao"].split(";")):
            dem[c] = dem.get(c, 0) + 1
    for c, n in sorted(dem.items()):
        print(f"  cờ {c}: {n}")
    print("ma | ten_doanh_nghiep | diem_uu_tien | duoc_giao_goi | co_canh_bao")
    hien = xep[: a.top] if a.top else xep
    for r in hien:
        print(f"{r.get('ma','')} | {r.get('ten_doanh_nghiep','')} | {r['diem_uu_tien']} | "
              f"{r['duoc_giao_goi']} | {r['co_canh_bao']}")

    if a.ra:
        cot = [c for c in rows[0].keys() if not c.startswith("_")]
        for c in ("diem_uu_tien", "co_canh_bao", "duoc_giao_goi"):
            if c not in cot:
                cot.append(c)
        with open(a.ra, "w", encoding="utf-8-sig", newline="") as f:
            w = csv.DictWriter(f, fieldnames=cot, extrasaction="ignore")
            w.writeheader()
            w.writerows(xep)
        print(f"Đã ghi: {a.ra}")


if __name__ == "__main__":
    main()
