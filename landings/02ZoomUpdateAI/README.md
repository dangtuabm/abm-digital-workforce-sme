# Landing Zoom 02 buổi: Bộ Não Thứ 2 & Nhân Sự Số

- **Link đích:** `https://pb.abmedu.vn/02ZoomUpdateAI/`
- **Google Sheet hứng lead:** [ABM - Đăng ký Zoom 02 buổi](https://docs.google.com/spreadsheets/d/1hDdsO8Nx1HYpkWpSNp4TlUt15wysgtQQ_Via4gJFzUs/edit)
- **Phiên bản:** v1.2 (24/09/2026): nâng cấp từ v1.1, thêm form đăng ký đẩy về Google Sheet

```
02ZoomUpdateAI/
├── site/                  ← UPLOAD toàn bộ nội dung thư mục này lên hosting
│   ├── index.html
│   └── assets/dang-tu-abm.jpg
└── google-apps-script/
    └── Code.gs            ← dán vào Apps Script của Google Sheet (KHÔNG upload lên hosting)
```

## Bước 1: Nối form với Google Sheet (khoảng 5 phút)

1. Mở Google Sheet ở link trên → **Tiện ích mở rộng → Apps Script**.
2. Xóa code mẫu, dán toàn bộ `google-apps-script/Code.gs` → **Lưu**.
3. Chọn hàm `setup` → **Chạy** → cấp quyền (Google cảnh báo "ứng dụng chưa xác minh" → Nâng cao → Tiếp tục). Hàng tiêu đề sẽ được tô Navy.
4. (Tùy chọn) Chọn hàm `testPost` → **Chạy** → kiểm tra Sheet có 1 dòng TEST → xóa dòng đó.
5. **Triển khai → Tùy chọn triển khai mới → Loại: Ứng dụng web**
   - Thực thi với tư cách: **Tôi**
   - Người có quyền truy cập: **Bất kỳ ai**
6. Copy **URL ứng dụng web** (dạng `https://script.google.com/macros/s/.../exec`).
7. Mở `site/index.html`, tìm dòng
   `var FORM_ENDPOINT = "PASTE_GOOGLE_APPS_SCRIPT_WEB_APP_URL_HERE";`
   và thay bằng URL vừa copy.

> Sửa `Code.gs` về sau: **Triển khai → Quản lý triển khai → Sửa → Phiên bản mới** để giữ nguyên URL.
> Muốn nhận email khi có lead: điền `NOTIFY_EMAIL` trong `Code.gs`.

## Bước 2: Upload lên hosting pb.abmedu.vn

**Cách A, cPanel File Manager (nhanh nhất):**
1. Đăng nhập cPanel → File Manager → thư mục gốc web của `pb.abmedu.vn` (cùng cấp với `CAMNANGHOCVIENCUABM/`).
2. Tạo thư mục `02ZoomUpdateAI`.
3. Upload `index.html` và thư mục `assets/` (hoặc upload file zip rồi **Extract**).

**Cách B, FTP (FileZilla):**

| Trường | Giá trị |
|---|---|
| Host | `pb.abmedu.vn` (hoặc `ftp.pb.abmedu.vn`) |
| Username | `dangtu@pb.abmedu.vn` |
| Password | mật khẩu tài khoản FTP (không lưu trong repo) |
| Port | 21 (FTPES nếu hosting hỗ trợ) |

Kéo nội dung `site/` vào thư mục `02ZoomUpdateAI/` trên server.

## Bước 3: Kiểm thử sau khi lên
- [ ] Mở `https://pb.abmedu.vn/02ZoomUpdateAI/` trên điện thoại và máy tính
- [ ] Gửi 3 bản ghi TEST → xác nhận 3 dòng về Sheet đúng cột (SĐT giữ số 0 đầu)
- [ ] Thử link có UTM: `?utm_source=facebook&utm_campaign=zoom0930` → cột utm có dữ liệu
- [ ] Xóa các dòng TEST trước khi chạy quảng cáo

## Luồng dữ liệu
Form (trình duyệt) → POST → Apps Script Web App (kiểm tra hợp lệ, chặn bot bằng honeypot, chống gửi trùng theo `submission_id`, chặn chèn công thức) → 1 dòng mới trong Sheet, cột "Trạng thái xử lý" = `Mới` để đội sales cập nhật.

Dữ liệu lead thuộc nhóm **Vàng**: chỉ chia sẻ Sheet cho người phụ trách, không copy ra nơi khác.
