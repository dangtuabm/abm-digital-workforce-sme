# VERSION CONTROL — RULES REFERENCE

## Quy tắc bắt buộc

1. Một asset có một canonical ID và một System of Record (SoR — hệ thống lưu bản chuẩn); aliases chỉ trỏ về canonical record.
2. “Mới nhất”, “được sửa gần nhất”, “được gửi qua chat” không đồng nghĩa “hiệu lực”.
3. Released artifact là immutable: thay đổi tạo candidate/version mới, không sửa tại chỗ.
4. Hash xác nhận bytes; owner/approval/effective record xác nhận thẩm quyền; cần cả hai.
5. Version scheme được khai báo theo asset type. SemVer chỉ dùng khi có compatibility contract rõ.
6. Mọi change nối source → request → diff → impact → tests → candidate hash → approvals → release/effective/supersedes → rollback/audit.
7. Approval chỉ có hiệu lực với đúng candidate hash, scope và window; kiểm tra Separation of Duties (SoD — phân tách nhiệm vụ).
8. Rollback là controlled change: target/backup/authority/trigger/recovery/reconciliation/evidence, không phải xóa lịch sử.
9. Archive/disposal theo retention policy và records owner; không tự động.
10. Audit append-only với timestamp/actor/action/target/before/after/evidence/result/correlation.

## Trạng thái cấm suy diễn

Không tự gán APPROVED, RELEASED, EFFECTIVE, SUPERSEDED, DEPRECATED, ARCHIVED, DISPOSED, MERGED hoặc ROLLED_BACK. Thiếu external evidence thì PENDING.

## Nguồn tham chiếu kiểm tra 22/08/2026

- Semantic Versioning 2.0.0: https://semver.org/spec/v2.0.0.html
- Git documentation: https://git-scm.com/docs/git
- NIST SP 800-53 Rev. 5 Update 1: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
- W3C PROV-O: https://www.w3.org/TR/prov-o/
- ISO 15489-1:2016: https://www.iso.org/standard/62542.html

Tailor theo asset, policy, SoR, access, records and dependency thực tế. Không nguồn nào tự chứng nhận compliance, integrity, compatibility hay release authority.

