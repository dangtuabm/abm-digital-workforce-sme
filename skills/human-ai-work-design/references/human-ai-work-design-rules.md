# HUMAN–A.I WORK DESIGN — CONTROL RULES

## 1. Unit of design

Thiết kế ở cấp task, decision hoặc work moment; không mặc định tự động hóa cả job. Giữ trace outcome → workflow → role → task/decision → input → action/output → consumer → evidence → authority/risk.

## 2. Seven dispositions

`ELIMINATE`, `HUMAN_ONLY`, `A.I_ASSIST`, `A.I_EXECUTE_HUMAN_APPROVE`, `A.I_BOUNDED_AUTONOMY`, `A.I_MONITOR_ALERT`, `EXCEPTION_TO_HUMAN`. Mỗi disposition phải có evidence, reason, acceptance và owner. `ELIMINATE` là loại task/waste, không phải loại người.

## 3. Human authority

Giữ người chịu trách nhiệm tại mục tiêu, policy, ngoại lệ, quyền, quyết định tác động cao và hiệu lực bên ngoài. Tách maker/checker khi rủi ro cần segregation of duties; A.I không tự review hành động của chính nó như kiểm soát độc lập.

## 4. Autonomy envelope

Mọi A.I action có allowed input/data/system/action/output, thresholds, rate/volume/time limit, confidence/abstain, approval, prohibited actions, logging, expiry, retry, fallback, escalation, kill switch và rollback.

## 5. Work and people impact

Rà workload chuyển dịch, cognitive load, exception burden, deskilling, capability/training, role clarity, adoption, accessibility, fairness và feedback. Không dùng protected attribute/proxy, surveillance hoặc headcount target để phân loại.

## 6. Test and handoff

Test normal/edge/exception/adversarial/security/SoD/fallback/recovery/kill/UAT. Chỉ bàn giao design proposal; permission, production, policy, staffing và rollout vẫn human-approved downstream.

