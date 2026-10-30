"""Pareto lỗi, lỗi lặp lại và lỗi quay lại sau khi đóng CAPA.

Dùng:
  python -I -X utf8 pareto-loi.py <so-ghi-loi.csv> [--theo ma_loi] [--capa so-capa.csv] [--he-so 10,3,1]

Đầu vào: CSV theo templates/so-ghi-loi.csv; tùy chọn sổ CAPA theo templates/so-capa.csv.
--theo: cột để gom (mặc định ma_loi; có thể cong_doan, ca, san_pham_dich_vu, diem_kiem).
--he-so: hệ số mức độ NGHIÊM TRỌNG, NẶNG, NHẸ cho bảng Pareto theo mức độ (mặc định 10,3,1 là giả định,
         người phụ trách chất lượng chỉnh).
Chỉ đọc file và in kết quả. Không sửa file, không gửi dữ liệu đi đâu.
"""
import argparse
import csv
import datetime as dt
import sys
import unicodedata


def bo_dau(s):
    s = unicodedata.normalize("NFD", s or "")
    s = "".join(c for c in s if unicodedata.category(c) != "Mn")
    return s.replace("đ", "d").replace("Đ", "D").lower().strip()


def la_trong(v):
    v = (v or "").strip()
    return v == "" or (v.startswith("[") and v.endswith("]"))


def doc_ngay(v):
    try:
        return dt.date.fromisoformat((v or "").strip()[:10])
    except ValueError:
        return None


def doc_so(v):
    if la_trong(v):
        return 1.0
    try:
        return float(str(v).replace(",", "."))
    except ValueError:
        return None


def muc(v):
    b = bo_dau(v)
    if b.startswith("nghiem"):
        return 0
    if b.startswith("nang"):
        return 1
    if b.startswith("nhe"):
        return 2
    return None


def bang(nhom, khoa_so, tieu_de):
    tong = sum(n[khoa_so] for n in nhom.values())
    print(f"\n== {tieu_de} (tổng {tong:g})")
    if tong == 0:
        print("  không có dữ liệu")
        return set()
    print("nhom | so_luong | phan_tram | cong_don | nhom_80 | nghiem_trong | so_tuan | lap_sau_capa")
    cd, trong80, truoc = 0.0, set(), 0.0
    for k, n in sorted(nhom.items(), key=lambda kv: -kv[1][khoa_so]):
        pt = 100 * n[khoa_so] / tong
        cd += pt
        thuoc = truoc < 80
        truoc = cd
        if thuoc:
            trong80.add(k)
        print(f"{k} | {n[khoa_so]:g} | {pt:.1f} | {cd:.1f} | {'co' if thuoc else 'khong'} | "
              f"{n['nt']:g} | {len(n['tuan'])} | {';'.join(sorted(n['capa'])) or '-'}")
    return trong80


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file")
    ap.add_argument("--theo", default="ma_loi")
    ap.add_argument("--capa", default="")
    ap.add_argument("--he-so", default="10,3,1")
    a = ap.parse_args()
    hs = [float(x) for x in a.he_so.split(",")]
    if len(hs) != 3:
        sys.exit("LỖI: --he-so cần 3 số cho NGHIÊM TRỌNG, NẶNG, NHẸ")

    with open(a.file, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        sys.exit("LỖI: sổ lỗi không có dòng dữ liệu")
    for c in (a.theo, "ngay", "ma_loi", "muc_do", "so_luong_loi"):
        if c not in rows[0]:
            sys.exit(f"LỖI: thiếu cột {c}")

    capa_dong = {}
    if a.capa:
        with open(a.capa, encoding="utf-8-sig", newline="") as f:
            for r in csv.DictReader(f):
                if bo_dau(r.get("trang_thai", "")) == "da dong":
                    nd = doc_ngay(r.get("ngay_dong"))
                    if nd and not la_trong(r.get("ma_loi")):
                        capa_dong.setdefault(r["ma_loi"].strip(), []).append((r.get("ma_capa", "?"), nd))

    nhom, bo_qua, canh_bao_nt = {}, [], []
    for i, r in enumerate(rows, start=2):
        k = (r.get(a.theo) or "").strip()
        ngay = doc_ngay(r.get("ngay"))
        sl = doc_so(r.get("so_luong_loi"))
        m = muc(r.get("muc_do"))
        if la_trong(k) or ngay is None or sl is None:
            bo_qua.append(i)
            continue
        n = nhom.setdefault(k, {"sl": 0.0, "ts": 0.0, "nt": 0.0, "tuan": set(), "capa": set(), "khong_muc": 0})
        n["sl"] += sl
        n["ts"] += sl * (hs[m] if m is not None else hs[2])
        if m is None:
            n["khong_muc"] += 1
        if m == 0:
            n["nt"] += sl
            canh_bao_nt.append(f"dòng {i}: {r.get('ma_loi','')} {r.get('ten_loi','')} ({r.get('lo_hoac_don','')})")
        n["tuan"].add(ngay.isocalendar()[:2])
        for ma_capa, nd in capa_dong.get((r.get("ma_loi") or "").strip(), []):
            if ngay > nd:
                n["capa"].add(ma_capa)

    if not nhom:
        print("Không có dòng hợp lệ (thiếu nhóm, ngày hoặc số lượng). Số dòng trong file bị bỏ qua:", bo_qua)
        return
    ngay_all = [doc_ngay(r.get("ngay")) for r in rows if doc_ngay(r.get("ngay"))]
    print(f"Sổ lỗi: {a.file} · gom theo: {a.theo} · kỳ: {min(ngay_all)} → {max(ngay_all)}")
    print(f"Dòng hợp lệ: {len(rows) - len(bo_qua)} · bỏ qua: {len(bo_qua)}" + (f" (số dòng trong file: {bo_qua})" if bo_qua else ""))
    print(f"Hệ số mức độ (giả định, chỉnh được): NGHIÊM TRỌNG {hs[0]:g} · NẶNG {hs[1]:g} · NHẸ {hs[2]:g}")

    bang(nhom, "sl", "PARETO THEO SỐ LƯỢNG")
    bang(nhom, "ts", "PARETO THEO MỨC ĐỘ")

    print("\n== CẦN CHÚ Ý")
    print("Lỗi NGHIÊM TRỌNG (báo ngay, mở CAPA dù ít):" + ("" if canh_bao_nt else " không có"))
    for x in canh_bao_nt:
        print("  " + x)
    lap = [k for k, n in nhom.items() if len(n["tuan"]) >= 2]
    print("Lặp lại từ 2 tuần trở lên:", ", ".join(sorted(lap)) or "không có")
    sau = {k: n["capa"] for k, n in nhom.items() if n["capa"]}
    print("Quay lại sau khi đóng CAPA (đề xuất MỞ LẠI):" + ("" if sau else " không có"))
    for k, c in sorted(sau.items()):
        print(f"  {k}: {', '.join(sorted(c))}")
    km = [k for k, n in nhom.items() if n["khong_muc"]]
    if km:
        print("Thiếu hoặc sai mức độ (đã tính như NHẸ, cần sửa sổ):", ", ".join(sorted(km)))
    print("\nLưu ý: bảng này đếm số lỗi. Tỷ lệ lỗi cần số đã kiểm (mẫu số) từ phiếu kiểm.")


if __name__ == "__main__":
    main()
