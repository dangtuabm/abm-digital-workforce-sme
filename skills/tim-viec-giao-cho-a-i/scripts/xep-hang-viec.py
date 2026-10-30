#!/usr/bin/env python3
"""Xếp hạng việc giao cho A.I: cổng trước điểm, điểm có trọng số đã duyệt, khoảng điểm khi có CHƯA BIẾT,
giữ hòa, thử độ nhạy theo từng tiêu chí, đề xuất 4 nhóm.

Dùng: python -I -X utf8 xep-hang-viec.py <file.json> [--ghi <file_ket_qua.json>]
Mẫu đầu vào: templates/du-lieu-xep-hang-mau.json
Kết quả là ĐỀ XUẤT; người có quyền quyết danh sách ngắn. Script chỉ đọc file đầu vào, không chạy mã, không mở mạng.
"""
import argparse
import json
import sys
from pathlib import Path

SAU_CONG = ["PHẠM VI – NGƯỜI PHỤ TRÁCH", "ĐỦ CĂN CỨ", "QUYỀN DỮ LIỆU", "KIỂM ĐƯỢC ĐẦU RA",
            "CON NGƯỜI KIỂM SOÁT", "TÁC HẠI – BẢO MẬT – DỮ LIỆU CÁ NHÂN"]
CHUA_BIET = "CHƯA BIẾT"


def diem_co_trong_so(uv, trong_so, thap, cao):
    """Trả về (điểm thấp, điểm cao) trên thang 0–100; CHƯA BIẾT lấy cận thấp/cao của thang."""
    lo = hi = 0.0
    tong = sum(trong_so.values())
    for ma, w in trong_so.items():
        s = uv["diem"].get(ma)
        if s == CHUA_BIET:
            lo += w * 0
            hi += w * 1
        else:
            r = (s - thap) / (cao - thap)
            lo += w * r
            hi += w * r
    return round(lo / tong * 100, 1), round(hi / tong * 100, 1)


def xep(diem):
    """diem: {ma: điểm thấp}; trả {ma: hạng}, hòa cùng hạng."""
    thu_tu = sorted(diem, key=lambda m: (-diem[m], m))
    hang, truoc, h = {}, None, 0
    for i, m in enumerate(thu_tu, 1):
        if diem[m] != truoc:
            h = i
            truoc = diem[m]
        hang[m] = h
    return hang


def chay(d):
    loi, nhac = [], []
    if not d.get("phien_ban_danh_sach"):
        loi.append("thiếu phiên bản danh sách cơ hội")
    if not d.get("nguoi_duyet_tieu_chi"):
        loi.append("bộ tiêu chí và trọng số chưa có người duyệt")
    thang = d.get("thang", {"thap_nhat": 0, "cao_nhat": 4})
    thap, cao = thang["thap_nhat"], thang["cao_nhat"]
    tieu_chi = d.get("tieu_chi", [])
    trong_so = {t["ma"]: t["trong_so"] for t in tieu_chi}
    if len(trong_so) != len(tieu_chi):
        loi.append("mã tiêu chí bị trùng")
    if round(sum(trong_so.values()), 6) != 100:
        loi.append(f"tổng trọng số là {sum(trong_so.values())}, phải bằng 100")
    ung_vien = d.get("ung_vien", [])
    ket_qua, qua_cong = {}, {}
    for uv in ung_vien:
        m = uv.get("ma")
        cong = uv.get("cong", {})
        thieu_cong = [c for c in SAU_CONG if c not in cong]
        if thieu_cong:
            loi.append(f"{m}: thiếu cổng {', '.join(thieu_cong)}")
        trang_thai_cong = "ĐẠT"
        if any(cong.get(c) == "KHÔNG ĐẠT" for c in SAU_CONG):
            trang_thai_cong = "KHÔNG ĐẠT"
        elif any(cong.get(c) != "ĐẠT" for c in SAU_CONG):
            trang_thai_cong = CHUA_BIET
        for t in trong_so:
            s = uv.get("diem", {}).get(t)
            if s != CHUA_BIET and not (isinstance(s, (int, float)) and not isinstance(s, bool) and thap <= s <= cao):
                loi.append(f"{m}: điểm tiêu chí {t} phải là {thap}–{cao} hoặc {CHUA_BIET}")
        ket_qua[m] = {"ten": uv.get("ten"), "cong": trang_thai_cong,
                      "cong_chua_dat": [c for c in SAU_CONG if cong.get(c) != "ĐẠT"],
                      "cong_suc": uv.get("cong_suc"), "rui_ro": uv.get("rui_ro")}
        if trang_thai_cong == "ĐẠT":
            qua_cong[m] = uv
    if loi:
        return {"ma_xep_hang": d.get("ma_xep_hang"), "trang_thai": "CHƯA SẴN SÀNG", "loi": sorted(set(loi))}
    n = d.get("danh_sach_ngan_toi_da", 3)
    delta = d.get("do_nhay_diem_trong_so", 5)

    def tinh(ts):
        diem = {m: diem_co_trong_so(uv, ts, thap, cao) for m, uv in qua_cong.items()}
        hang = xep({m: v[0] for m, v in diem.items()})
        ngan = {m for m, h in hang.items() if h <= n}
        return diem, hang, ngan

    diem, hang, ngan = tinh(trong_so)
    kich_ban_doi = []
    hang_min = dict(hang)
    hang_max = dict(hang)
    for t in trong_so:
        for dau in (+1, -1):
            moi = max(0, trong_so[t] + dau * delta)
            con_lai = sum(w for k, w in trong_so.items() if k != t)
            if con_lai == 0:
                continue
            he_so = (100 - moi) / con_lai
            ts = {k: (moi if k == t else w * he_so) for k, w in trong_so.items()}
            _, h2, n2 = tinh(ts)
            for m in h2:
                hang_min[m] = min(hang_min[m], h2[m])
                hang_max[m] = max(hang_max[m], h2[m])
            if n2 != ngan:
                kich_ban_doi.append(f"{t} {'+' if dau > 0 else '-'}{delta}")
    on_dinh = not kich_ban_doi
    if not on_dinh:
        nhac.append("danh sách ngắn đổi khi trọng số dịch: " + ", ".join(kich_ban_doi))
    if len(ngan) > n:
        nhac.append(f"có hòa ở ranh giới danh sách ngắn: {len(ngan)} việc cho {n} chỗ — cần người quyết phá hòa")
    de_xuat = []
    for m, k in ket_qua.items():
        if k["cong"] == "KHÔNG ĐẠT":
            nhom, ly_do = "LOẠI", "cổng KHÔNG ĐẠT: " + ", ".join(k["cong_chua_dat"])
        elif k["cong"] == CHUA_BIET:
            nhom, ly_do = "HOÃN", "cổng CHƯA BIẾT: " + ", ".join(k["cong_chua_dat"])
        elif m in ngan:
            nhom, ly_do = "DANH SÁCH NGẮN", "qua cổng, thứ hạng trong nhóm đầu"
        else:
            nhom, ly_do = "DỰ BỊ", "qua cổng, ngoài nhóm đầu"
        dong = {"ma": m, "ten": k["ten"], "cong": k["cong"], "nhom_de_xuat": nhom, "ly_do": ly_do,
                "cong_suc": k["cong_suc"], "rui_ro": k["rui_ro"]}
        if m in diem:
            lo, hi = diem[m]
            dong.update({"diem": lo if lo == hi else f"{lo}–{hi}", "hang": hang[m],
                         "hang_khi_doi_trong_so": f"{hang_min[m]}–{hang_max[m]}",
                         "co_chua_biet": lo != hi})
            if nhom == "DANH SÁCH NGẮN" and not on_dinh:
                dong["canh_bao"] = "KHÔNG ỔN ĐỊNH"
        de_xuat.append(dong)
    de_xuat.sort(key=lambda x: (x.get("hang", 10 ** 6), x["ma"]))
    return {"ma_xep_hang": d.get("ma_xep_hang"), "trang_thai": "SẴN SÀNG CHO NGƯỜI QUYẾT",
            "do_on_dinh": "ỔN ĐỊNH" if on_dinh else "KHÔNG ỔN ĐỊNH", "de_xuat": de_xuat,
            "nhac": nhac, "luu_y": "Đề xuất, chưa phải lựa chọn; công sức và rủi ro xem riêng, không cộng vào điểm."}


def main():
    p = argparse.ArgumentParser(description="Xếp hạng việc giao cho A.I")
    p.add_argument("dau_vao", type=Path)
    p.add_argument("--ghi", type=Path)
    a = p.parse_args()
    try:
        kq = chay(json.loads(a.dau_vao.read_text(encoding="utf-8")))
    except (OSError, KeyError, TypeError, ValueError, AttributeError, ZeroDivisionError) as e:
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
