#!/usr/bin/env python3
"""Phân bổ nguồn lực cho danh mục việc nhỏ (tối đa 22 việc không bắt buộc), có ràng buộc.

Dùng: python -I -X utf8 phan-bo-nguon-luc.py <file.json> [--ghi <file_ket_qua.json>]
Mẫu đầu vào: templates/du-lieu-phan-bo-mau.json
Quy tắc: nguồn lực dùng được = tổng - đã cam kết - vận hành thường xuyên - dự phòng;
việc bắt buộc và việc tiên quyết của nó luôn được chọn trước; không chọn hai việc loại trừ nhau;
tôn trọng số việc tối đa và giới hạn theo nhóm; trong các tổ hợp hợp lệ chọn tổ hợp có tổng giá trị
đã duyệt cao nhất. Nếu có "nguon_luc_can_cao", kiểm lại tổ hợp đã chọn theo ước tính cao.
Kết quả chỉ là ĐỀ XUẤT, không phải cam kết. Script chỉ đọc file đầu vào, không chạy mã, không mở mạng.
"""
import argparse
import itertools
import json
import sys
from pathlib import Path


def chay(d):
    dung_duoc = {k: v["tong"] - v.get("da_cam_ket", 0) - v.get("van_hanh_thuong_xuyen", 0) - v.get("du_phong", 0)
                 for k, v in d["nguon_luc"].items()}
    if any(v < 0 for v in dung_duoc.values()):
        return {"ma_phan_bo": d.get("ma_phan_bo"), "trang_thai": "KHÔNG KHẢ THI",
                "ly_do": "nguồn lực dùng được bị âm", "dung_duoc": dung_duoc}
    viec = {x["ma"]: x for x in d["danh_muc"]}
    if len(viec) != len(d["danh_muc"]):
        raise ValueError("mã việc bị trùng")
    for x in viec.values():
        if not x.get("nguon_gia_tri"):
            raise ValueError(f"{x['ma']} thiếu nguồn của giá trị đã duyệt")
        for r, v in x.get("nguon_luc_can", {}).items():
            if r not in dung_duoc or v < 0:
                raise ValueError(f"{x['ma']} khai nguồn lực không hợp lệ: {r}")
        if any(y not in viec for y in x.get("phu_thuoc", [])):
            raise ValueError(f"{x['ma']} phụ thuộc vào việc không có trong danh mục")

    def khep(chon):
        chon = set(chon)
        doi = True
        while doi:
            doi = False
            for i in list(chon):
                for p in viec[i].get("phu_thuoc", []):
                    if p not in chon:
                        chon.add(p)
                        doi = True
        return chon

    bat_buoc = khep({x["ma"] for x in viec.values() if x.get("bat_buoc")})
    tuy_chon = sorted(set(viec) - bat_buoc)
    if len(tuy_chon) > 22:
        raise ValueError("quá 22 việc không bắt buộc; cần công cụ tối ưu chuyên dụng đã được duyệt")
    gioi_han = d.get("gioi_han_nhom", {})
    toi_da = d.get("so_viec_toi_da", len(viec))

    def dung(chon, khoa="nguon_luc_can"):
        return {r: sum(viec[i].get(khoa, viec[i].get("nguon_luc_can", {})).get(r, 0) for i in chon) for r in dung_duoc}

    def hop_le(chon):
        chon = khep(chon)
        if len(chon) > toi_da:
            return None
        for i in chon:
            if set(viec[i].get("loai_tru", [])) & chon:
                return None
        da_dung = dung(chon)
        if any(da_dung[r] > dung_duoc[r] for r in dung_duoc):
            return None
        dem = {n: sum(viec[i].get("nhom") == n for i in chon) for n in gioi_han}
        for n, g in gioi_han.items():
            if dem[n] < g.get("toi_thieu", 0) or dem[n] > g.get("toi_da", len(viec)):
                return None
        gia_tri = sum(viec[i]["gia_tri_da_duyet"] for i in chon)
        tai = sum(da_dung[r] / dung_duoc[r] for r in dung_duoc if dung_duoc[r] > 0)
        return chon, da_dung, gia_tri, tai

    goc = hop_le(bat_buoc)
    if goc is None:
        return {"ma_phan_bo": d.get("ma_phan_bo"), "trang_thai": "KHÔNG KHẢ THI",
                "ly_do": "việc bắt buộc và ràng buộc vượt nguồn lực dùng được", "viec_bat_buoc": sorted(bat_buoc),
                "dung_duoc": dung_duoc}
    tot_nhat = None
    for n in range(len(tuy_chon) + 1):
        for to_hop in itertools.combinations(tuy_chon, n):
            ung_vien = hop_le(bat_buoc | set(to_hop))
            if ung_vien is None:
                continue
            khoa = (ung_vien[2], -ung_vien[3], tuple(sorted(ung_vien[0])))
            if tot_nhat is None or khoa > tot_nhat[0]:
                tot_nhat = (khoa, ung_vien)
    chon, da_dung, gia_tri, _ = tot_nhat[1]
    con_lai = {r: dung_duoc[r] - da_dung[r] for r in dung_duoc}
    hoan = sorted(set(viec) - chon, key=lambda i: (-viec[i]["gia_tri_da_duyet"], i))
    trang_thai = "KHẢ THI"
    nhac = []
    if any("nguon_luc_can_cao" in viec[i] for i in chon):
        cao = dung(chon, "nguon_luc_can_cao")
        vuot = [r for r in dung_duoc if cao[r] > dung_duoc[r]]
        if vuot:
            trang_thai = "CÓ ĐIỀU KIỆN"
            nhac.append("theo ước tính cao, vượt nguồn lực dùng được ở: " + ", ".join(vuot))
    return {"ma_phan_bo": d.get("ma_phan_bo"), "trang_thai": trang_thai, "de_xuat_chon": sorted(chon),
            "viec_bat_buoc": sorted(bat_buoc), "de_xuat_hoan": hoan, "tong_gia_tri": gia_tri,
            "dung_duoc": dung_duoc, "da_dung": da_dung, "con_lai": con_lai,
            "viec_hoan_gia_tri_cao_nhat": hoan[0] if hoan else None, "nhac": nhac,
            "luu_y": "Đây là đề xuất, chưa phải cam kết; người có quyền duyệt phân bổ."}


def main():
    p = argparse.ArgumentParser(description="Phân bổ nguồn lực có ràng buộc")
    p.add_argument("dau_vao", type=Path)
    p.add_argument("--ghi", type=Path)
    a = p.parse_args()
    try:
        kq = chay(json.loads(a.dau_vao.read_text(encoding="utf-8")))
    except (OSError, KeyError, TypeError, ValueError) as e:
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
