# CÂY RANH GIỚI ĐỎ A.I — [Tên doanh nghiệp]

**Phiên bản:** v[1] · **Ngày:** [dd/mm/yyyy] · **Người lập:** [...] · **Phạm vi:** [công ty / chi nhánh / phòng ban]
**Mức sẵn sàng:** [CHƯA SẴN SÀNG / CHỜ RÀ SOÁT / SẴN SÀNG CHỜ DUYỆT]
**Ban hành:** [để trống — người có quyền ký] · **Ngày hiệu lực:** [...] · **Rà lại:** [...]

## 1. Khung chung
- Mục tiêu dùng A.I: [...] · Mức chấp nhận rủi ro: [...] · Người bảo trợ: [...] · Người duyệt: [...]
- Nguyên tắc: mọi việc gửi ra ngoài tối thiểu ở ngưỡng 2; dữ liệu Đỏ ở ngưỡng 3; A.I không tự duyệt chính mình.

## 2. Cây Ranh giới Đỏ theo phòng ban
### [Phòng ...]
| Việc | Ngưỡng 1 TỰ LÀM | Ngưỡng 2 SOẠN NHÁP CHỜ DUYỆT | Ngưỡng 3 CẤM | Người duyệt ngưỡng 2 | Ghi chú |
|---|---|---|---|---|---|
| [Việc 1] | | | | | |

(Lặp lại cho từng phòng.)

## 3. Phần điều chỉnh so với khung mặc định
| Việc | Ngưỡng mặc định | Ngưỡng mới | Lý do | Rủi ro | Người duyệt | Ngày |
|---|---|---|---|---|---|---|

## 4. Sơ đồ luồng duyệt
```
[Yêu cầu] → A.I xác định ngưỡng
   ├─ Ngưỡng 1 → A.I làm → ghi nhật ký
   ├─ Ngưỡng 2 → A.I soạn nháp + nhãn → người duyệt → chính thức
   └─ Ngưỡng 3 → A.I dừng → báo người phụ trách
```

## 5. Kèm theo
- Danh mục A.I: `danh-muc-a-i.csv` · Ma trận quyền: `ma-tran-quyen.csv` · Bảng kiểm soát: `bang-kiem-soat.csv`
- Quy chuẩn nhãn và nhật ký · Quy trình sự cố 3 cấp · Sổ ngoại lệ
- Tài liệu phổ biến cho nhân viên: [tên file] — gồm cách đọc nhãn, 3 ngưỡng của phòng mình, cách báo sự cố

## 6. Xác nhận
| Vai trò | Họ tên | Ngày | Ý kiến |
|---|---|---|---|
| Người lập | | | |
| Trưởng các phòng | | | |
| Người có quyền ban hành | | | |

*[A.I Generated — Tên Nhân sự số — dd/mm/yyyy]*
