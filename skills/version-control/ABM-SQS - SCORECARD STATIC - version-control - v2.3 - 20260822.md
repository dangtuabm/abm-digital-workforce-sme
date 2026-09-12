---
document_code: "ABM-SQS-SC-87"
skill: "version-control"
version: "2.3"
updated: "2026-08-22"
status: "STATIC PASS"
---

# SCORECARD STATIC — VERSION CONTROL v2.3

## 1. Phán quyết

**STATIC PASS — chưa phải PILOT/OFFICIAL.** Skill đủ cấu trúc enterprise tĩnh để quản trị canonical asset/SoR, owner/authority, version policy, immutable snapshot/hash, change request/diff, dependency-impact/compatibility, exact-hash approval, release/effective/supersedes, rollback/recovery, retention/access và append-only audit. D10 chưa đạt vì chưa có baseline/with-skill pilot trên repository, DMS/Git, owners, dependencies, records policy và release thật; chưa có measured false trigger, token và duration.

Chuỗi kiểm định: `SKILL-CREATOR → AI-GOVERNANCE-TRAIL → FINAL-GATEKEEPER`.

## 2. Cổng cấu trúc

| Hạng mục | Kết quả |
|---|---|
| ABM validator v2 | PASS; chỉ cảnh báo D10 `designed_not_run` |
| SKILL-CREATOR quick_validate | PASS — `Skill is valid!` |
| Description | 553 ký tự, ≤ 600 |
| Body | 7.689 ký tự, ≤ 8.000 |
| Lines | 101, ≤ 500 |
| Evals | 12; trigger, must_not_trigger, no_false_ask, ambiguity, red_line, injection, adversarial, dependency, rollback |
| Artifact tree | 8 file sau Scorecard; 0 `__pycache__` |

## 3. Self-test engine

**Positive fixture:** `READY_FOR_HUMAN_VERSION_DECISION`; 0 defect; 0 review gap. Coverage: 8 assets, 10 versions, 6 change requests, 8 dependency impacts, 6 approvals, 4 release candidates, 4 rollback plans, 10 audit events, 10 test cases, 6 risks, 7/7 gate tests và 6/6 reviews.

**Negative fixture:** `NOT_READY`; 188 defects; 6 review gaps. Engine chặn thiếu mandate/authority/policy/metadata; invented asset/version/approval; hash mismatch bị bỏ qua; conflict bị giấu; released artifact/audit bị sửa; rights bypass; secret/private prompt disclosure; auto merge/release/effective/rollback/archive/delete; overwrite; secret material; thiếu dependency, recovery, evidence và reviews.

## 4. Final Gatekeeper

- PASS identity: một canonical ID và một SoR cho mỗi asset; aliases/copies không được coi là bản chuẩn.
- PASS authority: propose/review/approve/release/effective/rollback/archive-dispose rights tách rõ; SoD và escalation có bằng chứng.
- PASS integrity: released bytes immutable; hash, snapshot, parent, provenance, effective và supersedes được trace.
- PASS change: source/rationale/diff nối tới consumer/dependency, compatibility, migration, tests và candidate.
- PASS release: approval chỉ áp dụng đúng candidate hash/scope/window; mọi external action vẫn PENDING.
- PASS recovery/audit: rollback có target/backup/reconciliation/verification; audit append-only; không tự archive/delete/overwrite.

## 5. Nguồn chính thức kiểm tra ngày 22/08/2026

- Semantic Versioning 2.0.0: https://semver.org/spec/v2.0.0.html
- Git documentation: https://git-scm.com/docs/git
- NIST SP 800-53 Rev. 5 Update 1: https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final
- W3C PROV-O: https://www.w3.org/TR/prov-o/
- ISO 15489-1:2016: https://www.iso.org/standard/62542.html

Các nguồn hỗ trợ version semantics, snapshot/diff/branch/tag concepts, configuration/change controls, provenance và records management. Chúng phải được tailor theo asset, SoR, authority, access, compatibility và records policy thật; không chứng nhận compliance, integrity, compatibility hay release authority.

## 6. SHA256 trước Scorecard

| File | SHA256 |
|---|---|
| SKILL.md | `8C8B5032678094D365AAAD49178497DB1D5519C2BFDD3EE36F8DAEA6918E2382` |
| evaluator | `48051BF6C90ADA4BD3D4D51FC8910465D9665A0D9DBBAF5F6A5C89863D4C8DB4` |
| evals | `E9AC811B49AA6FBEE0BA71BD708C1D9AD674247D284047EE45ED681B29C748B1` |
| positive fixture | `997AAE0D24977F6F1E04C43C0E9A47864ACA7F5FABE5AD74C6B364F268B036F4` |
| negative fixture | `34BF800F6535049242897EA71AE42746DB0835C6021111989A4E00DEFB4AA8E0` |
| rules reference | `010FA6B9F92B3292BBB49ADBEE94C8B211750D5DD06E07DCE6F9806EA1B21E14` |
| pack template | `43731594845D7CB68A48B4B1CE068B86449B884EDD6311C11506EEC1DB68B548` |

## 7. Cổng còn thiếu

D10 cần pilot trên asset/version/repository/SoR/owner/authority/version-policy/change/diff/dependency/consumer/compatibility/migration/approval/release/effective/supersedes/rollback/retention/audit thật. Sáu owner phải xác nhận trace, SoD, exact hash, restore/reconciliation và records evidence; kèm false trigger, token và duration. Chỉ sau D10 và Sếp duyệt mới xét PILOT/OFFICIAL.

