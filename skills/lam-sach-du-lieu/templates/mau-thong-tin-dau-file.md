# MẪU THÔNG TIN ĐẦU FILE

Đặt khối dưới đây ở dòng đầu tiên của mỗi file `.md`. Năm trường đầu là bắt buộc. Doanh nghiệp có thể dùng tên trường khác, miễn thống nhất trong cả kho.

```yaml
---
tieu_de: "Quy trình nhập kho hàng mua"
loai: "quy-trinh"            # quy-trinh / chinh-sach / hop-dong-mau / bao-gia / bien-ban / huong-dan / khac
ngay: "15/09/2026"           # ngày ban hành hoặc ngày tài liệu
phong_ban: "Kho vận"
trang_thai: "chinh-thuc"     # nhap / chinh-thuc / het-hieu-luc
# Nên có:
nguoi_phu_trach: "Trưởng kho"
nhan_du_lieu: "xanh"         # xanh / vang / do
file_goc: "QUY-TRINH-NHAP-KHO-15-09-2026.pdf"
phien_ban: "v2"
---
```

Kiểm nhanh trước khi đưa vào A.I:
- [ ] Đủ 5 trường bắt buộc, không để trống.
- [ ] `trang_thai` đúng — bản hết hiệu lực không nằm trong thư mục dùng cho A.I.
- [ ] Tên file trùng với quy ước, khớp `file_goc` nếu có.

*[A.I Generated — Claude Code — 30/10/2026]*
