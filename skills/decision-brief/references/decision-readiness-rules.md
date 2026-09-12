# DECISION READINESS RULES

## 1. Ba trạng thái

| State | Điều kiện tối thiểu | Hành động |
|---|---|---|
| READY | Một decision/owner/deadline; options và status quo rõ; hard gates pass; material claims có evidence; upstream analysis/challenge phù hợp mức rủi ro; authority và next owner rõ | Trình người có thẩm quyền quyết định |
| CONDITIONAL | Có thể quyết định an toàn nếu một số điều kiện cụ thể được đáp ứng; downside giới hạn hoặc quyết định đủ reversible; condition có owner/deadline/verification | Trình phương án có điều kiện, không gọi approved |
| NOT_READY | Thiếu owner/question/options/hard gate; evidence mâu thuẫn hoặc stale; high-impact/irreversible nhưng thiếu challenge; authority không rõ | Dừng quyết định, nêu minimum evidence và handoff |

## 2. Hard gate trước điểm tổng

- Legal, ethics, safety, security, privacy, solvency, authority và brand red line là non-compensatory: điểm tốt ở tiêu chí khác không bù được.
- Không tự tạo threshold/weight. Nếu owner chưa khóa, ghi `NOT SET` và hạ readiness.
- Status quo là option để nhìn cost-of-delay, không mặc định là an toàn.

## 3. Reversibility và độ sâu bằng chứng

- Irreversible/high-downside/high-exposure: cần evidence mạnh hơn, challenge độc lập, approval rõ và rollback/containment nếu khả thi.
- Reversible/bounded experiment: có thể `CONDITIONAL` với guardrail, stop rule và review point.
- Urgency không biến evidence yếu thành mạnh; ghi riêng cost-of-delay và cost-of-error.

## 4. Điều kiện chuyển trạng thái

Mỗi gap material phải có: `GAP-ID`, evidence/decision cần có, owner, deadline, verification, state unlocked. Không dùng “bổ sung thêm dữ liệu” chung chung.
