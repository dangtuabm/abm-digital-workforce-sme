#!/usr/bin/env python3
"""Chấm điểm sản phẩm ứng viên trên sàn thương mại điện tử theo thang 100 điểm.

Dùng: python -I -X utf8 cham-diem-ung-vien.py <bang-ung-vien.csv> [--ra bao-cao.md]
      [--nguong-gia-1 300000] [--nguong-gia-2 700000]

Đầu vào: file CSV theo mẫu templates/bang-ung-vien-san-pham.csv (mã hóa UTF-8).
Chỉ chấm dòng đã có chứng cứ thật; dòng có tên bắt đầu bằng "[VÍ DỤ]" được đánh dấu
là dòng ví dụ, không dùng cho báo cáo thật.
"""
import argparse
import csv
import re
import sys
from pathlib import Path

COT_BAT_BUOC = ["ten", "duong_dan", "gia", "da_ban", "diem_danh_gia", "so_danh_gia", "nguon_chung_cu"]


def so(v, mac_dinh=0.0):
    if v is None:
        return mac_dinh
    s = str(v).strip().replace("đ", "").replace("₫", "").replace("%", "").replace(" ", "")
    if not s or s.startswith("["):
        return mac_dinh
    # Dấu phân cách hàng nghìn kiểu Việt Nam (12.500 hoặc 12,500) khác dấu thập phân (4.8 hoặc 4,8)
    if re.fullmatch(r"\d{1,3}([.,]\d{3})+", s):
        s = s.replace(".", "").replace(",", "")
    else:
        s = s.replace(",", ".")
    try:
        return float(s)
    except ValueError:
        return mac_dinh


def diem_nhu_cau(da_ban, da_ban_thang, so_danh_gia):
    m, t, r = so(da_ban_thang), so(da_ban), so(so_danh_gia)
    if m >= 3000 or t >= 50000:
        return 30
    if m >= 1000 or t >= 10000:
        return 25
    if m >= 200 or t >= 2000:
        return 19
    if m >= 50 or t >= 500 or r >= 100:
        return 12
    if t > 0 or r > 0:
        return 7
    return 0


def diem_kinh_te(gia, hoa_hong, bien, ng1, ng2):
    p = so(gia)
    c = max(so(hoa_hong), so(bien))
    d = 8
    if p and p <= ng1:
        d += 5
    elif p and p <= ng2:
        d += 3
    elif p:
        d += 1
    if c >= 20:
        d += 7
    elif c >= 12:
        d += 5
    elif c >= 6:
        d += 3
    else:
        d += 1
    return min(20, d)


def ket_luan(tong):
    if tong >= 80:
        return "THỬ NGAY"
    if tong >= 65:
        return "THEO DÕI / THỬ NHỎ"
    if tong >= 50:
        return "CHỈ THỬ NẾU CÓ GÓC NỘI DUNG MẠNH"
    return "LOẠI"


def kep(v, thap, cao, mac_dinh):
    return min(cao, max(thap, so(v, mac_dinh)))


def canh_bao(dong):
    cb = []
    url = (dong.get("duong_dan") or "").strip().lower()
    if not url or url.startswith("["):
        cb.append("thiếu đường dẫn sản phẩm")
    elif "search" in url or "keyword=" in url or "/tim-kiem" in url:
        cb.append("đường dẫn là trang tìm kiếm, chưa phải trang sản phẩm cụ thể")
    if not (dong.get("nguon_chung_cu") or "").strip() or (dong.get("nguon_chung_cu") or "").startswith("["):
        cb.append("thiếu nguồn chứng cứ")
    if (dong.get("ten") or "").startswith("[VÍ DỤ]"):
        cb.append("dòng ví dụ, không dùng cho báo cáo thật")
    return cb


def cham(dong, ng1, ng2):
    nc = diem_nhu_cau(dong.get("da_ban"), dong.get("da_ban_thang"), dong.get("so_danh_gia"))
    xh = kep(dong.get("diem_xu_huong"), 0, 20, 10)
    kt = diem_kinh_te(dong.get("gia"), dong.get("hoa_hong_phan_tram"), dong.get("bien_loi_nhuan_phan_tram"), ng1, ng2)
    nd = kep(dong.get("diem_noi_dung"), 0, 15, 10)
    ct = kep(dong.get("diem_canh_tranh"), 0, 10, 5)
    rr = kep(dong.get("diem_rui_ro"), 0, 5, 0)
    dg = so(dong.get("diem_danh_gia"))
    if dg and dg < 4.6:
        rr = max(rr, 3)
    tong = round(nc + xh + kt + nd + ct - rr, 1)
    return tong, {"nhu_cau": nc, "xu_huong": xh, "kinh_te": kt, "noi_dung": nd, "canh_tranh": ct, "tru_rui_ro": rr}


def doc(duong_dan):
    with Path(duong_dan).open(newline="", encoding="utf-8-sig") as f:
        doc_csv = csv.DictReader(f)
        thieu = [c for c in COT_BAT_BUOC if c not in (doc_csv.fieldnames or [])]
        if thieu:
            sys.exit("Thiếu cột bắt buộc: " + ", ".join(thieu))
        return list(doc_csv)


def xuat(ds):
    dong_ra = ["# BẢNG XẾP HẠNG SẢN PHẨM ỨNG VIÊN", "",
               "Điểm là ước lượng theo thang trong references/soi-nganh-bang-chung-cu.md; không phải cam kết bán được.", ""]
    for i, d in enumerate(ds, 1):
        p = d["_phan"]
        dong_ra += [
            f"## {i}. {d.get('ten', '(chưa có tên)')} — {d['_tong']}/100 — {d['_ket_luan']}",
            f"- Đường dẫn: {d.get('duong_dan', '')}",
            f"- Chứng cứ: đã bán {d.get('da_ban') or 'chưa rõ'}; đã bán/tháng {d.get('da_ban_thang') or 'chưa rõ'}; "
            f"điểm đánh giá {d.get('diem_danh_gia') or 'chưa rõ'}; số đánh giá {d.get('so_danh_gia') or 'chưa rõ'}; giá {d.get('gia') or 'chưa rõ'}",
            f"- Nguồn: {d.get('nguon_chung_cu', '')}",
            f"- Điểm thành phần: nhu cầu {p['nhu_cau']}, xu hướng {p['xu_huong']}, kinh tế {p['kinh_te']}, "
            f"nội dung {p['noi_dung']}, cạnh tranh {p['canh_tranh']}, trừ rủi ro -{p['tru_rui_ro']}",
        ]
        if d["_canh_bao"]:
            dong_ra.append("- CẢNH BÁO: " + "; ".join(d["_canh_bao"]))
        dong_ra += [f"- Ghi chú: {d.get('ghi_chu', '')}", ""]
    return "\n".join(dong_ra)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("dau_vao")
    ap.add_argument("--ra")
    ap.add_argument("--nguong-gia-1", type=float, default=300000)
    ap.add_argument("--nguong-gia-2", type=float, default=700000)
    a = ap.parse_args()
    ds = doc(a.dau_vao)
    for d in ds:
        d["_tong"], d["_phan"] = cham(d, a.nguong_gia_1, a.nguong_gia_2)
        d["_ket_luan"] = ket_luan(d["_tong"])
        d["_canh_bao"] = canh_bao(d)
        if d["_canh_bao"] and d["_ket_luan"] != "LOẠI":
            d["_ket_luan"] += " (CHƯA ĐỦ CHỨNG CỨ)"
    ds.sort(key=lambda x: x["_tong"], reverse=True)
    van_ban = xuat(ds)
    if a.ra:
        Path(a.ra).write_text(van_ban, encoding="utf-8")
    print(van_ban)


if __name__ == "__main__":
    main()
