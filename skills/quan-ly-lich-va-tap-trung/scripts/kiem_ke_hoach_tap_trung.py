#!/usr/bin/env python3
"""Kiểm Kế hoạch tập trung dạng JSON (mẫu: templates/mau-du-lieu-lich.json).

Chỉ đọc file, không đổi lịch hay việc. Dùng:
    python -I -X utf8 kiem_ke_hoach_tap_trung.py <file.json>
Trả mã 0 khi không có lỗi, 1 khi CHƯA SẴN SÀNG.
"""
import json
import sys

UU_TIEN = {"PHAI XONG", "NEN XONG", "HO TRO", "CHUA LAM"}
TINH_TRANG = {"DANG LAM", "SAN SANG", "BI CHAN", "XONG", "HUY"}
CACH = {"LAM", "GIAO", "HOAN", "BO", "XIN Y KIEN"}


def so_khong_am(v):
    return isinstance(v, (int, float)) and not isinstance(v, bool) and v >= 0


def kiem(d):
    loi, nhac = [], []
    khung = d.get("khung") or {}
    for k in ("khoang_thoi_gian", "mui_gio", "muc_tieu", "nguoi_duyet", "gioi_han_viec_lam_do"):
        if not khung.get(k):
            loi.append(f"khung: thiếu {k}")

    sc = d.get("suc_chua") or {}
    vals = [sc.get(k) for k in ("gio_lam_phut", "viec_co_dinh_phut", "nghi_phut", "du_phong_phut")]
    suc_chua = 0
    if not all(so_khong_am(v) for v in vals):
        loi.append("sức chứa: các số phút phải có và không âm")
    else:
        suc_chua = vals[0] - vals[1] - vals[2] - vals[3]
        if suc_chua < 0:
            loi.append(f"sức chứa âm ({suc_chua} phút): lịch đã quá tải")
        if vals[2] == 0:
            nhac.append("không có giờ nghỉ: kiểm lại, không lấy giờ nghỉ làm phần dư")

    cks = d.get("cam_ket") or []
    ma_ck = set()
    dang_lam = 0
    for i, c in enumerate(cks):
        ma = c.get("ma") or f"#{i+1}"
        if ma in ma_ck:
            loi.append(f"cam kết {ma}: trùng mã")
        ma_ck.add(ma)
        for k in ("viec", "muc_tieu", "nguoi_chiu_trach_nhiem", "han", "uoc_luong_phut", "uu_tien", "tinh_trang"):
            if c.get(k) in (None, "", []):
                nhac.append(f"cam kết {ma}: thiếu {k} (ghi CHƯA RÕ, không tự bỏ)")
        if c.get("uu_tien") and c["uu_tien"] not in UU_TIEN:
            loi.append(f"cam kết {ma}: mức ưu tiên không hợp lệ")
        if c.get("tinh_trang") and c["tinh_trang"] not in TINH_TRANG:
            loi.append(f"cam kết {ma}: tình trạng không hợp lệ")
        if c.get("tinh_trang") == "DANG LAM":
            dang_lam += 1
    gh = khung.get("gioi_han_viec_lam_do")
    if isinstance(gh, int) and dang_lam > gh:
        loi.append(f"việc làm dở {dang_lam} > giới hạn {gh}: phải nhả bớt")

    for i, x in enumerate(d.get("de_xuat") or []):
        if x.get("ma_cam_ket") not in ma_ck:
            loi.append(f"đề xuất #{i+1}: không khớp cam kết nào")
        if x.get("cach_xu_ly") not in CACH:
            loi.append(f"đề xuất #{i+1}: cách xử lý không hợp lệ")
        if not x.get("ly_do"):
            loi.append(f"đề xuất #{i+1}: thiếu lý do")
        if x.get("cach_xu_ly") != "LAM" and x.get("da_duyet") is not True:
            nhac.append(f"đề xuất #{i+1} ({x.get('cach_xu_ly')}): chưa được duyệt — giữ CHỜ DUYỆT")

    tong = 0
    for i, b in enumerate(d.get("khoi_tap_trung") or []):
        if b.get("ma_cam_ket") not in ma_ck:
            loi.append(f"khối {b.get('ma', i+1)}: không nối với cam kết nào")
        if not so_khong_am(b.get("thoi_luong_phut")):
            loi.append(f"khối {b.get('ma', i+1)}: thời lượng không hợp lệ")
        else:
            tong += b["thoi_luong_phut"]
        for k in ("bat_dau_khi", "dung_khi"):
            if not b.get(k):
                nhac.append(f"khối {b.get('ma', i+1)}: thiếu {k}")
    if tong > suc_chua:
        loi.append(f"tổng khối tập trung {tong} phút > sức chứa {suc_chua} phút")

    mo = [x.get("ma") for x in (d.get("xung_dot") or []) if x.get("muc_do") == "NGHIEM TRONG" and not x.get("da_xu_ly")]
    if mo:
        loi.append(f"xung đột nghiêm trọng còn mở: {', '.join(map(str, mo))}")

    if not (d.get("quy_tac_gian_doan") or {}).get("khan"):
        nhac.append("chưa có quy tắc gián đoạn")

    chua_duyet = any("chưa được duyệt" in n for n in nhac)
    if loi:
        tt = "CHƯA SẴN SÀNG"
    elif chua_duyet:
        tt = "CHỜ DUYỆT KẾ HOẠCH"
    else:
        tt = "SẴN SÀNG CẬP NHẬT LỊCH (người có quyền tự cập nhật)"
    return {"trang_thai": tt, "suc_chua_phut": suc_chua, "tong_khoi_tap_trung_phut": tong,
            "viec_lam_do": dang_lam, "loi": loi, "nhac": nhac}


def main():
    if len(sys.argv) != 2:
        print(__doc__)
        return 2
    with open(sys.argv[1], encoding="utf-8-sig") as f:
        d = json.load(f)
    kq = kiem(d)
    print(json.dumps(kq, ensure_ascii=False, indent=2))
    return 1 if kq["loi"] else 0


if __name__ == "__main__":
    raise SystemExit(main())
