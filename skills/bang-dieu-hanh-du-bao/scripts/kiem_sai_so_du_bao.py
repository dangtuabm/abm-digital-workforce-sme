#!/usr/bin/env python3
"""Kiểm sai số dự báo so với mốc đơn giản (mẫu: templates/mau-sai-so-du-bao.csv).

Cột bắt buộc: ky, thuc_te, du_bao. Cột tùy chọn: can_duoi, can_tren (khoảng dao động).
Cột du_bao phải là số đã dự báo TRƯỚC khi biết thực tế của kỳ đó.
Mốc đơn giản: thực tế của kỳ cách đó --mua-vu kỳ (mặc định 1 = lấy kỳ trước;
12 = cùng kỳ năm trước với dữ liệu tháng; 52 với dữ liệu tuần).
Chỉ đọc file. Dùng:
    python -I -X utf8 kiem_sai_so_du_bao.py <file.csv> [--mua-vu N]
"""
import csv
import sys


def so(x):
    x = (x or "").strip().replace(",", ".")
    if not x:
        return None
    try:
        return float(x)
    except ValueError:
        return None


def chi_so(cap):
    """cap: danh sách (thuc_te, du_bao)."""
    if not cap:
        return None
    sai = [abs(d - t) for t, d in cap]
    tong_tt = sum(abs(t) for t, _ in cap)
    return {
        "so_ky": len(cap),
        "sai_so_trung_binh": round(sum(sai) / len(sai), 4),
        "ty_le_sai_so_theo_tong_pct": round(100 * sum(sai) / tong_tt, 2) if tong_tt else None,
        "do_lech_pct": round(100 * sum(d - t for t, d in cap) / tong_tt, 2) if tong_tt else None,
    }


def main():
    args = sys.argv[1:]
    if not args or args[0].startswith("-"):
        print(__doc__)
        return 2
    path = args[0]
    m = 1
    if "--mua-vu" in args:
        try:
            m = int(args[args.index("--mua-vu") + 1])
        except (IndexError, ValueError):
            print("--mua-vu cần một số nguyên dương")
            return 2
    if m < 1:
        print("--mua-vu cần một số nguyên dương")
        return 2

    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows or any(c not in rows[0] for c in ("ky", "thuc_te", "du_bao")):
        print("Thiếu cột ky, thuc_te hoặc du_bao")
        return 2

    tt = [so(r.get("thuc_te")) for r in rows]
    db = [so(r.get("du_bao")) for r in rows]
    cd = [so(r.get("can_duoi")) for r in rows]
    ct = [so(r.get("can_tren")) for r in rows]

    # Chỉ so trên các kỳ có đủ: thực tế, dự báo và mốc đơn giản
    idx = [i for i in range(len(rows)) if i >= m and tt[i] is not None and db[i] is not None and tt[i - m] is not None]
    if len(idx) < 3:
        print(f"Chỉ có {len(idx)} kỳ so được (cần ≥ 3). Chưa đủ để kết luận.")
        return 1

    kq_db = chi_so([(tt[i], db[i]) for i in idx])
    kq_moc = chi_so([(tt[i], tt[i - m]) for i in idx])

    co_khoang = [i for i in idx if cd[i] is not None and ct[i] is not None]
    trung = sum(1 for i in co_khoang if cd[i] <= tt[i] <= ct[i])

    ten_moc = "lấy kỳ trước" if m == 1 else f"lấy kỳ cách {m} kỳ (mùa vụ)"
    print(f"Số kỳ so: {len(idx)} ({rows[idx[0]]['ky']} → {rows[idx[-1]]['ky']})")
    print(f"Dự báo      : sai số TB {kq_db['sai_so_trung_binh']} · tỷ lệ sai số theo tổng {kq_db['ty_le_sai_so_theo_tong_pct']}% · độ lệch {kq_db['do_lech_pct']}%")
    print(f"Mốc đơn giản ({ten_moc}): sai số TB {kq_moc['sai_so_trung_binh']} · tỷ lệ sai số theo tổng {kq_moc['ty_le_sai_so_theo_tong_pct']}% · độ lệch {kq_moc['do_lech_pct']}%")
    if co_khoang:
        print(f"Khoảng dao động: thực tế nằm trong khoảng {trung}/{len(co_khoang)} kỳ ({round(100 * trung / len(co_khoang), 1)}%) — so với mức khoảng đã đặt (ví dụ 80%)")

    if kq_db["ty_le_sai_so_theo_tong_pct"] < kq_moc["ty_le_sai_so_theo_tong_pct"]:
        print("Kết luận: dự báo TỐT HƠN mốc đơn giản trên các kỳ đã so.")
        rc = 0
    else:
        print("Kết luận: dự báo KHÔNG tốt hơn mốc đơn giản — dùng mốc đơn giản hoặc ghi rõ hạn chế.")
        rc = 1
    if abs(kq_db["do_lech_pct"] or 0) > 5:
        print("Nhắc: độ lệch vượt 5% — dự báo đang cao hoặc thấp đều đặn, xem lại giả định.")
    print("Lưu ý: kết quả chỉ đúng khi cột du_bao là số dự báo thật tại thời điểm đó (không nhìn trước).")
    return rc


if __name__ == "__main__":
    raise SystemExit(main())
