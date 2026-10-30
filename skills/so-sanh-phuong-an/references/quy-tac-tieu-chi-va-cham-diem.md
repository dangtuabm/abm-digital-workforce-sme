# QUY TẮC TIÊU CHÍ VÀ CHẤM ĐIỂM

## 1. Hồ sơ mỗi tiêu chí

Mỗi tiêu chí có: mã, định nghĩa, liên quan gì tới quyết định, chiều tốt (càng cao càng tốt hay ngược lại), đơn vị gốc, phạm vi và thời gian áp dụng, mốc neo 0 / 50 / 100, trọng số, ngưỡng căn cứ tối thiểu, người duyệt và phiên bản. **Khóa trước khi thấy tổng điểm.**

- **Cổng bắt buộc** (ví dụ: xuất được hóa đơn điện tử hợp lệ, có giấy phép kinh doanh ngành nghề, đáp ứng an toàn thực phẩm): không bù trừ, để riêng, không có trọng số.
- **Tránh đếm hai lần**: hai tiêu chí cùng đo một kết quả (ví dụ "giá rẻ" và "chi phí thấp") thì gộp, hoặc giải thích rõ khác nhau ở đâu.
- **Trọng số** thể hiện đánh đổi đã duyệt; tổng các trọng số phải bằng 1,00.
- **Tiêu chí định tính** (ví dụ "thái độ hỗ trợ") cần mốc neo bằng hành vi quan sát được, không đổi tính từ thành số tùy ý.

Ví dụ mốc neo cho "Thời gian giao hàng nội thành":
- 100 điểm: giao trong ngày, đúng hẹn từ 98% trở lên trong 3 tháng gần nhất;
- 50 điểm: giao trong 2 ngày, đúng hẹn khoảng 90%;
- 0 điểm: trên 3 ngày hoặc đúng hẹn dưới 80%.
(Các mức này là ví dụ minh họa; doanh nghiệp tự đặt theo yêu cầu của mình.)

## 2. Từ căn cứ sang điểm

- Giữ giá trị gốc và cách quy đổi; điểm chuẩn hóa chỉ trong thang 0–100.
- Ô thiếu / chưa rõ **không phải 0** và không tự điền thay.
- Mỗi điểm có mã căn cứ, mức thấp / cơ sở / cao với `0 ≤ thấp ≤ cơ sở ≤ cao ≤ 100`.
- Chỉ phương án qua mọi cổng và đủ điểm cho các tiêu chí trọng yếu mới ở trạng thái SO SÁNH ĐƯỢC.

## 3. Tính tổng có trọng số

`tổng = Σ(trọng số × điểm chuẩn hóa)`, tính riêng cho mức thấp, cơ sở, cao với cùng một bộ trọng số.

Lưu đầu vào, phiên bản công cụ và kết quả; không làm tròn ở bước trung gian để đổi thứ hạng. Dùng `scripts/cham_diem_phuong_an.py`, không tính nhẩm.

## 4. Trường dữ liệu của file đầu vào script

| Trường | Ý nghĩa |
|---|---|
| `ma_quyet_dinh` | Mã và tên quyết định |
| `tieu_chi[].ma`, `ten` | Mã, tên tiêu chí |
| `tieu_chi[].loai` | `cong` (cổng bắt buộc) hoặc `diem` (chấm điểm) |
| `tieu_chi[].trong_so` | Chỉ cho loại `diem`; tổng bằng 1,00 |
| `phuong_an[].ma` | Mã phương án |
| `phuong_an[].cong` | Mỗi cổng: `true` (ĐẠT), `false` (TRƯỢT), `null` hoặc bỏ trống (CHƯA RÕ) |
| `phuong_an[].diem` | Mỗi tiêu chí: `thap`, `co_so`, `cao`, `ma_can_cu` |

*[A.I Generated — Claude Code — 30/10/2026]*
