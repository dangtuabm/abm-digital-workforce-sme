#!/usr/bin/env python3
"""Kiểm Bảng việc sau họp dạng CSV (mẫu: templates/bang-viec-sau-hop.csv).

Mỗi việc phải đủ 4 mục (người thực hiện + việc, hạn là ngày cụ thể, đo bằng gì,
báo cáo ai) và người thực hiện đã nhận việc. Chỉ đọc file, không tạo việc.
Dùng:
    python -I -X utf8 kiem_bang_viec.py <file.csv>
Trả mã 0 khi mọi việc đủ điều kiện, 1 khi còn việc CHỜ XÁC NHẬN.
"""
import csv
import re
import sys
from datetime import datetime

BAT_BUOC = ["ma", "nguoi_thuc_hien", "viec", "han", "do_bang_gi", "bao_cao_ai", "da_nhan_viec"]
TU_PHONG_BAN = re.compile(r"^(phòng|ban|bộ phận|nhóm|team)\b", re.I)
TU_MO_HO = re.compile(r"theo dõi tiếp|sẽ xem|tiếp tục theo dõi", re.I)


def la_ngay(s):
    for fmt in ("%d/%m/%Y", "%Y-%m-%d"):
        try:
            datetime.strptime(s.strip(), fmt)
            return True
        except ValueError:
            pass
    return False


def kiem(rows):
    ket_qua = []
    for r in rows:
        van_de = []
        for k in BAT_BUOC:
            if not (r.get(k) or "").strip():
                van_de.append(f"thiếu {k}")
        nguoi = (r.get("nguoi_thuc_hien") or "").strip()
        if nguoi and TU_PHONG_BAN.match(nguoi):
            van_de.append("người thực hiện là phòng ban, cần một người cụ thể")
        han = (r.get("han") or "").strip()
        if han and not la_ngay(han):
            van_de.append(f"hạn '{han}' không phải ngày cụ thể")
        if TU_MO_HO.search(r.get("viec") or ""):
            van_de.append("việc mơ hồ kiểu 'sẽ theo dõi tiếp'")
        if (r.get("da_nhan_viec") or "").strip().upper() != "CO":
            van_de.append("người thực hiện chưa nhận việc")
        ket_qua.append({"ma": r.get("ma"), "tinh_trang": "ĐỦ" if not van_de else "CHỜ XÁC NHẬN",
                        "van_de": van_de})
    return ket_qua


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    with open(sys.argv[1], encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    thieu_cot = [c for c in BAT_BUOC if rows and c not in rows[0]]
    if thieu_cot:
        print("Thiếu cột:", ", ".join(thieu_cot))
        return 2
    kq = kiem(rows)
    cho = 0
    for x in kq:
        print(f"{x['ma']}: {x['tinh_trang']}" + (f" — {'; '.join(x['van_de'])}" if x["van_de"] else ""))
        cho += x["tinh_trang"] != "ĐỦ"
    print(f"Tổng {len(kq)} việc · đủ {len(kq) - cho} · chờ xác nhận {cho}")
    return 1 if cho else 0


if __name__ == "__main__":
    raise SystemExit(main())
