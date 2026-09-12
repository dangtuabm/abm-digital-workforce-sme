# DIGITAL WORKFORCE MANAGEMENT — CONTROL RULES

## 1. Registry scope

Quản trị danh mục/vòng đời Agent, không thiết kế một Task Contract hay một lần orchestration. Mỗi Agent có immutable ID, display label không mạo danh người, business/technical/risk owners, mission/scope, work/use-case refs, skills, knowledge, tools/connectors, permissions, triggers, outputs, authority, approval/escalation, SLO/cost/capacity, dependencies, version và state.

## 2. Lifecycle

`CANDIDATE → DESIGN → PILOT → ACTIVE`; nhánh kiểm soát `LIMITED/SUSPENDED`; kết thúc `RETIRED → ARCHIVED`. Mọi transition có trigger, evidence, owner/approver, effective time, expiry/review và rollback/manual coverage. Không auto-activate.

## 3. Admission gate

Phải có business need, không duplicate vô ích, Agent/Task contract, owners, data/tool/permission approval, risk classification, tests/UAT, SLO/runbook/monitoring, cost/capacity cap, incident/fallback/kill và offboarding plan.

## 4. Operations

Theo dõi demand/queue/WIP/capacity, quality/acceptance, SLO/error/retry/fallback/escalation, incident, permission/connector recertification, cost, drift, change/version và realized value evidence. Output volume ≠ value.

## 5. Portfolio review

Đánh dấu duplicate/overlap/gap/dependency/single-point-of-failure, ownerless/orphaned, over-broad scope/permission, unused/low-value hoặc unstable Agent. PROPOSE `BUILD/MERGE/LIMIT/SUSPEND/REMEDIATE/RETIRE`; không tự thực thi.

## 6. Offboarding

Drain/cancel queue; stop triggers; revoke identities/scopes/connectors/secrets; reconcile open work; transfer ownership/manual coverage; archive evidence/version; apply retention/delete approval; update dependencies/routes/registry; test rollback/recovery. Không xóa thẳng.

