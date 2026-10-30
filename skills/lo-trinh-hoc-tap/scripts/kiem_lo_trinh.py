"""Kiểm bảng chặng của lộ trình học tập (templates/bang-chang.csv).

Dùng: python -I -X utf8 kiem_lo_trinh.py <bang-chang.csv> <gio-cho-phep>
Kiểm: đủ trường, mã chặng trùng, điều kiện trước không tồn tại hoặc tự trỏ, vòng lặp,
giờ công không đọc được, tổng giờ so với giờ cho phép.
Chỉ đọc file CSV, in kết quả; không ghi file, không gọi mạng. Kết quả chỉ kiểm cấu trúc,
không thay người duyệt và không chứng minh người học đã thành thạo.
"""
import csv
import sys

BAT_BUOC = ["ma_chang", "ket_qua", "thuc_hanh", "san_pham", "phan_hoi", "cong_dat", "gio_cong", "du_phong"]


def main():
    if len(sys.argv) < 3:
        print(__doc__)
        return 2
    gio_cho_phep = float(sys.argv[2])
    loi, chang = [], {}
    with open(sys.argv[1], encoding="utf-8-sig", newline="") as f:
        r = csv.DictReader(f)
        thieu_cot = [c for c in BAT_BUOC + ["dieu_kien_truoc"] if c not in (r.fieldnames or [])]
        if thieu_cot:
            print("LỖI: thiếu cột", ", ".join(thieu_cot))
            return 1
        for d in r:
            ma = (d["ma_chang"] or "").strip()
            if not ma:
                loi.append("có dòng thiếu mã chặng")
                continue
            if ma in chang:
                loi.append(f"{ma}: mã chặng trùng")
            for c in BAT_BUOC:
                v = (d[c] or "").strip()
                if not v or v.startswith("["):
                    loi.append(f"{ma}: thiếu '{c}'")
            try:
                gio = float((d["gio_cong"] or "").replace(",", "."))
            except ValueError:
                gio = 0.0
            truoc = [x.strip() for x in (d["dieu_kien_truoc"] or "").replace(";", ",").split(",") if x.strip()]
            chang[ma] = {"gio": gio, "truoc": truoc}
    for ma, c in chang.items():
        for t in c["truoc"]:
            if t == ma:
                loi.append(f"{ma}: điều kiện trước tự trỏ về chính nó")
            elif t not in chang:
                loi.append(f"{ma}: điều kiện trước '{t}' không tồn tại")
    # tìm vòng lặp
    trang_thai = {}

    def duyet(ma, duong):
        trang_thai[ma] = 1
        for t in chang[ma]["truoc"]:
            if t not in chang or t == ma:
                continue
            if trang_thai.get(t) == 1:
                loi.append("vòng lặp: " + " -> ".join(duong + [t]))
            elif t not in trang_thai:
                duyet(t, duong + [t])
        trang_thai[ma] = 2

    for ma in chang:
        if ma not in trang_thai:
            duyet(ma, [ma])
    tong = sum(c["gio"] for c in chang.values())
    print(f"Số chặng: {len(chang)} | Tổng giờ: {tong:g} | Giờ cho phép: {gio_cho_phep:g}")
    if tong > gio_cho_phep:
        loi.append(f"tổng giờ {tong:g} vượt giờ cho phép {gio_cho_phep:g}: đưa phương án cho quản lý chọn")
    for l in loi:
        print("LỖI:", l)
    print("TRẠNG THÁI GỢI Ý:", "CẦN SỬA" if loi else "ĐẠT KIỂM CẤU TRÚC (người duyệt vẫn phải xem)")
    print("TỔNG LỖI:", len(loi))
    return 1 if loi else 0


if __name__ == "__main__":
    sys.exit(main())
