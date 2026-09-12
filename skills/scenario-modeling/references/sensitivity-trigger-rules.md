# SENSITIVITY, BREAK-EVEN & TRIGGER RULES

- One-way sensitivity thay một driver trong BASE, giữ các biến khác; ghi rõ giới hạn vì có thể phá correlation.
- Break-even dùng bracket đã duyệt và chỉ hợp lệ khi target được bracket; nếu không trả `NOT_BRACKETED`, không extrapolate.
- Non-monotonic output cần phương pháp/chuyên gia khác; bisection không chứng minh unique root.
- Trigger có metric, operator, threshold/unit, direction, data source/frequency, owner, action authority và hysteresis/review để tránh bật tắt nhiễu.
- Signpost là observable evidence; scenario label không phải trigger.
- Robust conclusion đứng vững qua plausible configurations/ranges; fragile conclusion đổi bởi perturbation nhỏ hoặc gap material.

Luôn tách cost-of-error, cost-of-delay và reversibility. Engine result là model output, không là approval hay action.
