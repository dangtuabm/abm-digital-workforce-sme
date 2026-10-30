#!/usr/bin/env python3
"""Kiểm Hồ sơ chuẩn bị họp dạng JSON (mẫu: templates/mau-du-lieu-cuoc-hop.json).

Chỉ đọc file, không gửi lời mời. Dùng:
    python -I -X utf8 kiem_chuong_trinh_hop.py <file.json>
Trả mã 0 khi không có lỗi, 1 khi CHƯA SẴN SÀNG.
"""
import json
import sys

LOAI = {"QUYET DINH", "THONG NHAT", "GIAI QUYET VAN DE", "RA SOAT", "SANG TAO"}
CACH = {"BAO", "BAN", "QUYET", "NHAN VIEC"}


def kiem(d):
    loi, nhac = [], []
    tt = d.get("thong_tin_hop") or {}
    for k in ("loai_hop", "muc_dich", "bat_dau", "ket_thuc", "thoi_luong_phut", "nguoi_chu_tri"):
        if not tt.get(k):
            loi.append(f"thông tin họp: thiếu {k}")
    loai = tt.get("loai_hop")
    if loai and loai not in LOAI:
        loi.append("loại họp không hợp lệ")
    if loai == "QUYET DINH" and not tt.get("nguoi_quyet"):
        loi.append("họp QUYẾT ĐỊNH nhưng chưa có người quyết")

    for i, n in enumerate(d.get("nguon") or []):
        if n.get("tinh_trang") in ("CU", "MAU THUAN"):
            nhac.append(f"nguồn '{n.get('ten', i+1)}' đang {n['tinh_trang']}: ghi rõ trong hồ sơ")
        for k in ("phien_ban", "ngay_cap_nhat", "nguoi_giu"):
            if not n.get(k):
                nhac.append(f"nguồn '{n.get('ten', i+1)}': thiếu {k}")

    for c in d.get("cam_ket_cu") or []:
        if c.get("tinh_trang") == "TRE":
            nhac.append(f"cam kết trễ phải hiện trong hồ sơ: {c.get('viec')}")

    for i, q in enumerate(d.get("cau_hoi_can_quyet") or []):
        if len(q.get("phuong_an") or []) < 2:
            loi.append(f"câu hỏi #{i+1}: cần ít nhất 2 phương án")
        for k in ("khuyen_nghi", "can_cu", "cach_quyet", "han"):
            if not q.get(k):
                loi.append(f"câu hỏi #{i+1}: thiếu {k}")
    if loai == "QUYET DINH" and not d.get("cau_hoi_can_quyet"):
        loi.append("họp QUYẾT ĐỊNH nhưng chưa có câu hỏi cần quyết")

    nguoi_quyet = tt.get("nguoi_quyet")
    du = [p for p in (d.get("nguoi_du") or []) if p.get("ten") == nguoi_quyet]
    if loai == "QUYET DINH" and nguoi_quyet and not (du and du[0].get("co_mat") is True):
        loi.append("người quyết không có mặt: chưa đủ người quyết")
    for p in d.get("nguoi_du") or []:
        if p.get("vai_tro") == "DUOC BAO" and p.get("can_du"):
            nhac.append(f"{p.get('ten')}: chỉ cần được báo, cân nhắc không mời dự")

    tong = 0
    for i, m in enumerate(d.get("chuong_trinh") or []):
        if m.get("cach") not in CACH:
            loi.append(f"mục #{i+1}: cách làm không hợp lệ")
        for k in ("nguoi_dan", "dau_ra"):
            if not m.get(k):
                loi.append(f"mục #{i+1}: thiếu {k}")
        p = m.get("phut")
        if not isinstance(p, (int, float)) or isinstance(p, bool) or p <= 0:
            loi.append(f"mục #{i+1}: thời lượng không hợp lệ")
        else:
            tong += p
    tl = tt.get("thoi_luong_phut") or 0
    if tong > tl:
        loi.append(f"chương trình {tong} phút > thời lượng họp {tl} phút")
    elif tong == tl:
        nhac.append("chương trình kín 100% thời gian: cân nhắc chừa dự phòng")

    trang_thai = "CHƯA SẴN SÀNG" if loi else "CHỜ CHỦ TRÌ DUYỆT"
    return {"trang_thai": trang_thai, "tong_chuong_trinh_phut": tong, "thoi_luong_hop_phut": tl,
            "loi": loi, "nhac": nhac}


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
