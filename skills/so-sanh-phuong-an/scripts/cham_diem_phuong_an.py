#!/usr/bin/env python3
"""Tính điểm có trọng số cho các phương án — chỉ tính, không chọn.

Dùng:
  python -I -X utf8 cham_diem_phuong_an.py <file_dau_vao.json> [--ghi <file_ket_qua.json>]

Đầu vào: xem templates/mau-dau-vao-cham-diem.json. Điểm phải đã được quy về thang 0–100
theo mốc neo đã duyệt; trọng số các tiêu chí chấm điểm cộng lại bằng 1,00.
Mã thoát: 0 = tính xong, 2 = đầu vào sai.
"""
import argparse
import json
import sys
from decimal import Decimal, InvalidOperation
from pathlib import Path


def loi(thong_bao):
    raise ValueError(thong_bao)


def so(gia_tri, nhan):
    try:
        return Decimal(str(gia_tri))
    except (InvalidOperation, ValueError):
        loi(f"{nhan} phải là số")


def lam_tron(gia_tri):
    return float(gia_tri.quantize(Decimal("0.01")))


def tinh(du_lieu):
    tieu_chi = du_lieu.get("tieu_chi")
    phuong_an = du_lieu.get("phuong_an")
    if not isinstance(tieu_chi, list) or not tieu_chi:
        loi("tieu_chi phải là danh sách không rỗng")
    if not isinstance(phuong_an, list) or not phuong_an:
        loi("phuong_an phải là danh sách không rỗng")

    ma = [t.get("ma") for t in tieu_chi]
    if None in ma or len(ma) != len(set(ma)):
        loi("mã tiêu chí phải có và không trùng")
    cong = [t for t in tieu_chi if t.get("loai") == "cong"]
    diem = [t for t in tieu_chi if t.get("loai") == "diem"]
    if len(cong) + len(diem) != len(tieu_chi) or not diem:
        loi("loai của tiêu chí chỉ được là 'cong' (cổng bắt buộc) hoặc 'diem', và phải có ít nhất một tiêu chí 'diem'")
    trong_so = {t["ma"]: so(t.get("trong_so"), f"trọng số {t['ma']}") for t in diem}
    if any(w < 0 for w in trong_so.values()) or abs(sum(trong_so.values()) - Decimal("1")) > Decimal("0.000001"):
        loi("trọng số không âm và cộng lại phải bằng 1,00")

    ket_qua, da_co = [], set()
    for pa in phuong_an:
        ma_pa = pa.get("ma")
        if not ma_pa or ma_pa in da_co:
            loi("mã phương án phải có và không trùng")
        da_co.add(ma_pa)
        gia_tri_cong = pa.get("cong", {})
        truot = [c["ma"] for c in cong if gia_tri_cong.get(c["ma"]) is False]
        chua_ro = [c["ma"] for c in cong if gia_tri_cong.get(c["ma"]) is not True and c["ma"] not in truot]
        dong = {"ma": ma_pa, "cong_truot": truot, "cong_chua_ro": chua_ro}
        if truot:
            dong["trang_thai"] = "TRƯỢT CỔNG"
            ket_qua.append(dong)
            continue
        if chua_ro:
            dong["trang_thai"] = "CHƯA SO SÁNH ĐƯỢC"
            ket_qua.append(dong)
            continue
        bang_diem = pa.get("diem", {})
        thieu = [t["ma"] for t in diem if t["ma"] not in bang_diem]
        if thieu:
            dong.update({"trang_thai": "CHƯA SO SÁNH ĐƯỢC", "thieu_diem": thieu})
            ket_qua.append(dong)
            continue
        tong = {"thap": Decimal("0"), "co_so": Decimal("0"), "cao": Decimal("0")}
        for t in diem:
            o = bang_diem[t["ma"]]
            if not o.get("ma_can_cu"):
                loi(f"{ma_pa}/{t['ma']} thiếu ma_can_cu")
            thap, co_so, cao = (so(o.get(k), f"{ma_pa}/{t['ma']}/{k}") for k in ("thap", "co_so", "cao"))
            if not (Decimal("0") <= thap <= co_so <= cao <= Decimal("100")):
                loi(f"{ma_pa}/{t['ma']} cần 0 <= thap <= co_so <= cao <= 100")
            for k, v in (("thap", thap), ("co_so", co_so), ("cao", cao)):
                tong[k] += trong_so[t["ma"]] * v
        dong.update({"trang_thai": "SO SÁNH ĐƯỢC", "diem_trong_so": {k: lam_tron(v) for k, v in tong.items()}})
        ket_qua.append(dong)

    so_duoc = sorted((r for r in ket_qua if r["trang_thai"] == "SO SÁNH ĐƯỢC"),
                     key=lambda r: (-r["diem_trong_so"]["co_so"], r["ma"]))
    for hang, r in enumerate(so_duoc, 1):
        r["hang_theo_diem_co_so"] = hang
    if len(so_duoc) < 2:
        do_vung = "KHÔNG ĐỦ PHƯƠNG ÁN ĐỂ SO"
    else:
        dau = so_duoc[0]
        vung = dau["diem_trong_so"]["thap"] > max(r["diem_trong_so"]["cao"] for r in so_duoc[1:])
        do_vung = "VỮNG" if vung else "CHƯA VỮNG — dải điểm chồng lấn, không có phương án thắng chắc chắn"
    return {
        "ma_quyet_dinh": du_lieu.get("ma_quyet_dinh"),
        "do_vung_thu_hang": do_vung,
        "ket_qua": ket_qua,
        "ghi_chu": "Điểm chỉ là căn cứ; người có thẩm quyền mới chọn phương án.",
    }


def main():
    p = argparse.ArgumentParser(description="Tính điểm có trọng số cho các phương án")
    p.add_argument("file_dau_vao", type=Path)
    p.add_argument("--ghi", type=Path, help="ghi kết quả ra file JSON")
    a = p.parse_args()
    try:
        kq = tinh(json.loads(a.file_dau_vao.read_text(encoding="utf-8")))
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        print(f"LỖI ĐẦU VÀO: {exc}", file=sys.stderr)
        return 2
    van_ban = json.dumps(kq, ensure_ascii=False, indent=2)
    if a.ghi:
        a.ghi.write_text(van_ban + "\n", encoding="utf-8")
    print(van_ban)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
