#!/usr/bin/env python3
"""Kiểm tính toàn vẹn của dữ liệu hậu kiểm quyết định.

Dùng: python -I -X utf8 kiem-hau-kiem.py <file.json> [--ghi <file_ket_qua.json>]
Chỉ đọc file đầu vào; không chạy mã, không mở mạng, không đọc file khác.
Mẫu đầu vào: templates/du-lieu-hau-kiem-mau.json
"""
import argparse
import json
import sys
from pathlib import Path

NHAN_NGUYEN_NHAN = {"LOGIC QUYẾT ĐỊNH", "THỰC THI", "GIẢ ĐỊNH SAI", "YẾU TỐ BÊN NGOÀI", "ĐO LƯỜNG", "MAY RỦI – CHƯA RÕ"}
TRANG_THAI_BAI_HOC = {"BÀI HỌC RIÊNG CA", "GIẢ THUYẾT", "ỨNG VIÊN TÁI SỬ DỤNG", "ĐÃ ĐƯA VÀO KHO"}


def trong(v):
    return v is None or v == "" or v == [] or v == {}


def kiem(d):
    loi, nhac = [], []
    goc = d.get("ho_so_goc", {})
    for k in ("ma_quyet_dinh", "phien_ban", "ngay_quyet", "nguoi_quyet", "ma_kiem_tra"):
        if trong(goc.get(k)):
            loi.append(f"hồ sơ gốc thiếu {k}")
    ds_kv = d.get("ky_vong", [])
    ky_vong = {x.get("ma"): x for x in ds_kv if x.get("ma")}
    if not ky_vong or len(ky_vong) != len(ds_kv):
        loi.append("kỳ vọng trống hoặc trùng/thiếu mã")
    thuc_te = {x.get("ma_ky_vong"): x for x in d.get("thuc_te", []) if x.get("ma_ky_vong")}
    for ma, kv in ky_vong.items():
        for k in ("chi_so", "muc_tieu", "nguon", "tinh_den"):
            if trong(kv.get(k)):
                loi.append(f"{ma}: kỳ vọng thiếu {k}")
        tt = thuc_te.get(ma)
        if not tt:
            loi.append(f"{ma}: chưa có kết quả thực tế")
            continue
        if tt.get("chi_so") != kv.get("chi_so"):
            loi.append(f"{ma}: chỉ số thực tế khác chỉ số kỳ vọng — không so được")
        if tt.get("gia_tri") is None or trong(tt.get("nguon")) or trong(tt.get("tinh_den")):
            loi.append(f"{ma}: kết quả thực tế thiếu giá trị/nguồn/ngày")
    for ma in set(thuc_te) - set(ky_vong):
        nhac.append(f"thực tế {ma} không có kỳ vọng ghi từ trước")
    chenh_lech = []
    for ma, kv in ky_vong.items():
        tt = thuc_te.get(ma)
        if tt and isinstance(tt.get("gia_tri"), (int, float)) and isinstance(kv.get("muc_tieu"), (int, float)):
            trong_khoang = None
            if isinstance(kv.get("thap"), (int, float)) and isinstance(kv.get("cao"), (int, float)):
                trong_khoang = kv["thap"] <= tt["gia_tri"] <= kv["cao"]
            chenh_lech.append({"ma": ma, "ky_vong": kv["muc_tieu"], "thuc_te": tt["gia_tri"],
                               "chenh": round(tt["gia_tri"] - kv["muc_tieu"], 4), "trong_khoang_du_kien": trong_khoang})
    da_co = set()
    for x in d.get("phan_bo_nguyen_nhan", []):
        ma = x.get("ma")
        if not ma or ma in da_co:
            loi.append("phân bổ nguyên nhân thiếu hoặc trùng mã")
        da_co.add(ma)
        if x.get("ma_ky_vong") not in ky_vong or x.get("nhan") not in NHAN_NGUYEN_NHAN or trong(x.get("co_che")) or trong(x.get("can_cu")):
            loi.append(f"{ma or 'nguyên nhân'}: thiếu kỳ vọng/nhãn hợp lệ/cơ chế/căn cứ")
    for c in chenh_lech:
        if c["trong_khoang_du_kien"] is False and not any(x.get("ma_ky_vong") == c["ma"] for x in d.get("phan_bo_nguyen_nhan", [])):
            nhac.append(f"{c['ma']}: nằm ngoài khoảng dự kiến nhưng chưa phân bổ nguyên nhân")
    da_co = set()
    for x in d.get("bai_hoc", []):
        ma = x.get("ma")
        if not ma or ma in da_co:
            loi.append("bài học thiếu hoặc trùng mã")
        da_co.add(ma)
        if x.get("trang_thai") not in TRANG_THAI_BAI_HOC:
            loi.append(f"{ma}: trạng thái bài học không hợp lệ")
        for k in ("noi_dung", "pham_vi_ap_dung", "nguoi_phu_trach", "khi_nao_xem_lai"):
            if trong(x.get(k)):
                loi.append(f"{ma}: bài học thiếu {k}")
        if x.get("trang_thai") == "ĐÃ ĐƯA VÀO KHO":
            for k in ("nguon_goc", "gioi_han", "nguoi_phu_trach_duyet", "nguoi_ra_duyet"):
                if trong(x.get(k)):
                    loi.append(f"{ma}: đưa vào kho nhưng thiếu {k}")
    if loi:
        trang_thai = "KHÔNG ĐỦ ĐIỀU KIỆN HẬU KIỂM"
    elif nhac:
        trang_thai = "TẠM THỜI"
    else:
        trang_thai = "HOÀN TẤT"
    return {"ma_hau_kiem": d.get("ma_hau_kiem"), "trang_thai": trang_thai,
            "so_luong": {"ky_vong": len(ky_vong), "thuc_te": len(thuc_te),
                         "nguyen_nhan": len(d.get("phan_bo_nguyen_nhan", [])), "bai_hoc": len(d.get("bai_hoc", []))},
            "chenh_lech": chenh_lech, "loi": sorted(set(loi)), "nhac": sorted(set(nhac))}


def main():
    p = argparse.ArgumentParser(description="Kiểm dữ liệu hậu kiểm quyết định")
    p.add_argument("dau_vao", type=Path)
    p.add_argument("--ghi", type=Path)
    a = p.parse_args()
    try:
        kq = kiem(json.loads(a.dau_vao.read_text(encoding="utf-8")))
    except (OSError, TypeError, ValueError, AttributeError) as e:
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
