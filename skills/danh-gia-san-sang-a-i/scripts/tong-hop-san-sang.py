#!/usr/bin/env python3
"""Tổng hợp hồ sơ mức sẵn sàng A.I theo 08 YẾU TỐ.

Dùng: python -I -X utf8 tong-hop-san-sang.py <file.json> [--ghi <file_ket_qua.json>]
Mẫu đầu vào: templates/du-lieu-danh-gia-mau.json
Kiểm: đủ 08 YẾU TỐ đúng tên; điểm là số trong thang hoặc "CHƯA BIẾT" (không đổi thành 0);
điểm số phải trỏ tới căn cứ có thật; tỷ lệ căn cứ tự khai; cổng quan trọng chưa đạt; vai rà.
Chỉ tính điểm tổng khi có trọng số đã duyệt. Script chỉ đọc file đầu vào, không chạy mã, không mở mạng.
"""
import argparse
import json
import sys
from pathlib import Path

TAM_YEU_TO = ["BÀI TOÁN – MỤC TIÊU", "CÔNG CỤ – MODEL", "DATA – DỮ LIỆU", "SKILL – KỸ NĂNG",
              "WORKFLOW – QUY TRÌNH", "OUTPUT – ĐẦU RA", "SỬ DỤNG – TƯƠNG TÁC – QUẢN TRỊ", "CON NGƯỜI – VĂN HÓA"]
LOAI_CAN_CU = {"QUAN SÁT", "TÀI LIỆU", "TỪ HỆ THỐNG", "TỰ KHAI", "ƯỚC TÍNH", "CHƯA KIỂM"}
TRANG_THAI_CONG = {"ĐẠT", "KHÔNG ĐẠT", "CHƯA BIẾT"}
SAU_VAI_RA = {"CHIẾN LƯỢC – KINH DOANH", "CHỦ DỮ LIỆU", "KỸ THUẬT – BẢO MẬT", "CHỦ QUY TRÌNH",
              "CON NGƯỜI – THAY ĐỔI", "TÀI CHÍNH – RỦI RO"}


def trong(v):
    return v is None or v == "" or v == [] or v == {}


def chay(d, diem_toi_da=4):
    loi, nhac = [], []
    pv = d.get("pham_vi", {})
    for k in ("cau_hoi", "don_vi", "nguoi_bao_tro", "moc_du_lieu"):
        if trong(pv.get(k)):
            loi.append(f"phạm vi thiếu {k}")
    thang = d.get("thang_danh_gia", {})
    if trong(thang.get("nguoi_duyet")):
        loi.append("thang đánh giá chưa có người duyệt — chỉ dùng được cho soi nhanh")
    can_cu = {x.get("ma"): x for x in d.get("can_cu", []) if x.get("ma")}
    for m, x in can_cu.items():
        if x.get("loai") not in LOAI_CAN_CU:
            loi.append(f"{m}: loại căn cứ không hợp lệ")
        for k in ("nguon", "nguoi_so_huu", "ngay"):
            if trong(x.get(k)):
                loi.append(f"{m}: căn cứ thiếu {k}")
    yt = {}
    for x in d.get("yeu_to", []):
        ten = x.get("ten")
        if ten not in TAM_YEU_TO:
            loi.append(f"yếu tố không thuộc 08 YẾU TỐ: {ten}")
            continue
        if ten in yt:
            loi.append(f"yếu tố bị lặp: {ten}")
        yt[ten] = x
    for ten in TAM_YEU_TO:
        if ten not in yt:
            loi.append(f"thiếu yếu tố: {ten}")
    phan_bo, chua_biet = {}, []
    for ten in TAM_YEU_TO:
        x = yt.get(ten)
        if not x:
            continue
        diem = x.get("diem")
        if diem == "CHƯA BIẾT":
            chua_biet.append(ten)
            phan_bo[ten] = "CHƯA BIẾT"
        elif isinstance(diem, (int, float)) and not isinstance(diem, bool) and 0 <= diem <= diem_toi_da:
            phan_bo[ten] = diem
            if not x.get("can_cu"):
                loi.append(f"{ten}: có điểm nhưng không có căn cứ")
            loai = [can_cu[c].get("loai") for c in x.get("can_cu", []) if c in can_cu]
            if loai and all(l in {"TỰ KHAI", "ƯỚC TÍNH", "CHƯA KIỂM"} for l in loai):
                nhac.append(f"{ten}: điểm chỉ dựa trên căn cứ tự khai/ước tính — độ tin thấp")
        else:
            loi.append(f"{ten}: điểm không hợp lệ (phải là 0–{diem_toi_da} hoặc CHƯA BIẾT)")
        for c in x.get("can_cu", []):
            if c not in can_cu:
                loi.append(f"{ten}: trỏ tới căn cứ không có: {c}")
        if trong(x.get("nguoi_phu_trach")):
            loi.append(f"{ten}: thiếu người phụ trách")
    so_tu_khai = sum(1 for x in can_cu.values() if x.get("loai") in {"TỰ KHAI", "ƯỚC TÍNH", "CHƯA KIỂM"})
    ty_le_tu_khai = round(so_tu_khai / len(can_cu) * 100, 1) if can_cu else None
    cong_chua_dat = []
    for x in d.get("cong", []):
        if x.get("trang_thai") not in TRANG_THAI_CONG:
            loi.append(f"{x.get('ma')}: trạng thái cổng không hợp lệ")
        for c in x.get("can_cu", []):
            if c not in can_cu:
                loi.append(f"{x.get('ma')}: trỏ tới căn cứ không có: {c}")
        if x.get("quan_trong") is True and x.get("trang_thai") != "ĐẠT":
            cong_chua_dat.append(f"{x.get('ma')} ({x.get('trang_thai')})")
    diem_tong = None
    ts = thang.get("trong_so")
    if isinstance(ts, dict) and ts:
        biet = {t: v for t, v in phan_bo.items() if v != "CHƯA BIẾT" and t in ts}
        tong_ts = sum(ts[t] for t in biet)
        if tong_ts > 0:
            diem_tong = {"gia_tri": round(sum(biet[t] * ts[t] for t in biet) / tong_ts, 2),
                         "do_phu_yeu_to": f"{len(biet)}/8",
                         "luu_y": "Điểm tổng không thay cho cổng; xem cổng quan trọng trước."}
    vai_dat = {x.get("vai") for x in d.get("ra_soat", []) if x.get("trang_thai") == "ĐẠT"}
    vai_thieu = sorted(SAU_VAI_RA - vai_dat)
    if loi:
        trang_thai = "CHƯA SẴN SÀNG ĐÁNH GIÁ"
    elif chua_biet or (ty_le_tu_khai is not None and ty_le_tu_khai > 50):
        trang_thai = "SẴN SÀNG THU THẬP CĂN CỨ"
    elif vai_thieu:
        trang_thai = "SẴN SÀNG RÀ SOÁT"
    else:
        trang_thai = "SẴN SÀNG CHO NGƯỜI QUYẾT"
    ket_luan_cong = ("CÒN CỔNG QUAN TRỌNG CHƯA ĐẠT — chưa đề xuất thử nghiệm/mở rộng ở phạm vi liên quan"
                     if cong_chua_dat else "CÁC CỔNG QUAN TRỌNG ĐÃ KHAI ĐỀU ĐẠT")
    return {"ma_danh_gia": d.get("ma_danh_gia"), "trang_thai_ho_so": trang_thai, "ket_luan_cong": ket_luan_cong,
            "phan_bo_diem_theo_yeu_to": phan_bo, "yeu_to_chua_biet": chua_biet,
            "ty_le_can_cu_tu_khai_phan_tram": ty_le_tu_khai, "cong_quan_trong_chua_dat": cong_chua_dat,
            "diem_tong": diem_tong, "vai_ra_soat_con_thieu": vai_thieu,
            "loi": sorted(set(loi)), "nhac": sorted(set(nhac)),
            "luu_y": "Kết quả là căn cứ để người có quyền quyết, không phải chứng nhận."}


def main():
    p = argparse.ArgumentParser(description="Tổng hợp mức sẵn sàng A.I theo 08 YẾU TỐ")
    p.add_argument("dau_vao", type=Path)
    p.add_argument("--ghi", type=Path)
    a = p.parse_args()
    try:
        kq = chay(json.loads(a.dau_vao.read_text(encoding="utf-8")))
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
