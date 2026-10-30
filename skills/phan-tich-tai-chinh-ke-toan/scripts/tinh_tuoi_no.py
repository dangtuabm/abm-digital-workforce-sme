"""Tính số ngày quá hạn và nhóm tuổi nợ từ bảng tuổi nợ (templates/bang-tuoi-no.csv).

Dùng: python -I -X utf8 tinh_tuoi_no.py <file.csv> <ngay-chot YYYY-MM-DD> [moc1,moc2,moc3]
- moc mặc định 30,60,90 ngày (nhóm mặc định, phải được kế toán trưởng chốt).
- Chỉ đọc file CSV, in kết quả ra màn hình; không ghi đè file gốc, không gọi mạng.
"""
import csv
import sys
from datetime import date

CAN_CO = ["ma_dong", "loai_no", "doi_tuong", "ngay_chung_tu", "ngay_den_han", "so_tien", "trang_thai"]


def doc_ngay(s):
    s = (s or "").strip()
    if not s or s.startswith("YYYY"):
        return None
    return date.fromisoformat(s)


def nhom_tuoi(so_ngay, moc):
    if so_ngay <= 0:
        return "CHUA_DEN_HAN"
    truoc = 0
    for m in moc:
        if so_ngay <= m:
            return f"QUA_HAN_{truoc + 1}_{m}"
        truoc = m
    return f"QUA_HAN_TREN_{moc[-1]}"


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    ngay_chot = date.fromisoformat(sys.argv[2])
    moc = [int(x) for x in sys.argv[3].split(",")] if len(sys.argv) > 3 else [30, 60, 90]
    loi, dong_ra = [], []
    with open(sys.argv[1], encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        thieu = [c for c in CAN_CO if c not in (r.fieldnames or [])]
        if thieu:
            print("LỖI: thiếu cột", ", ".join(thieu))
            return 1
        for d in r:
            ma = d["ma_dong"]
            try:
                tien = float((d["so_tien"] or "").replace(",", ""))
            except ValueError:
                loi.append(f"{ma}: số tiền không đọc được '{d['so_tien']}'")
                continue
            try:
                han = doc_ngay(d["ngay_den_han"])
                ct = doc_ngay(d["ngay_chung_tu"])
            except ValueError as e:
                loi.append(f"{ma}: ngày sai định dạng ({e})")
                continue
            ghi_chu = ""
            if han is None:
                if ct is None:
                    loi.append(f"{ma}: thiếu cả ngày đến hạn và ngày chứng từ")
                    continue
                han, ghi_chu = ct, "tính theo ngày chứng từ"
            so_ngay = (ngay_chot - han).days
            dong_ra.append((ma, d["loai_no"], d["doi_tuong"], tien, so_ngay, nhom_tuoi(so_ngay, moc),
                            d["trang_thai"], ghi_chu))
    tong = {}
    print("ma_dong,loai_no,doi_tuong,so_tien,so_ngay_qua_han,nhom_tuoi,trang_thai,ghi_chu")
    for ma, loai, dt, tien, n, nhom, tt, gc in dong_ra:
        print(f"{ma},{loai},{dt},{tien:.0f},{max(n, 0)},{nhom},{tt},{gc}")
        khoa = (loai, nhom if tt == "BINH_THUONG" else f"TACH_RIENG_{tt}")
        tong[khoa] = tong.get(khoa, 0) + tien
    print("\nTỔNG THEO NHÓM (khoản không BINH_THUONG tách riêng):")
    for (loai, nhom), tien in sorted(tong.items()):
        print(f"  {loai} | {nhom} | {tien:,.0f}")
    print(f"\nMốc nhóm tuổi dùng: {moc} — [GIẢ ĐỊNH] nếu chưa có chính sách công nợ đã duyệt.")
    for l in loi:
        print("LỖI:", l)
    print("TỔNG LỖI:", len(loi))
    return 1 if loi else 0


if __name__ == "__main__":
    sys.exit(main())
