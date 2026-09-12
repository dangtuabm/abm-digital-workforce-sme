# Market Intelligence Control Rules

## Boundary and sources

- Market = customer/job + category/substitute + geography + channel + period + currency/base year + inclusions/exclusions.
- Material claim phải có source locator, publisher, published/event date, access/rights, freshness, type/tier và confidence.
- Official/primary ưu tiên; secondary dùng corroboration; rumor/review/job post chỉ là signal, không tự thành fact.
- Không bypass paywall/login, scrape trái terms, dùng confidential/inside data hoặc profile cá nhân.

## Claims and estimates

- Phân `FACT`, `ESTIMATE`, `HYPOTHESIS`, `COMPANY_CLAIM`; contradictions không bị xóa.
- Market size cần formula, inputs, denominator, top-down/bottom-up range, currency/base year, sensitivity và reconciliation.
- Share cần cùng market denominator. Price phải chuẩn pack/unit/channel/tax/contract term và list/realized basis.
- Không suy market conclusion từ vài mẫu hoặc coi absence of evidence là zero.

## Competitor, signals and scenarios

- Entity resolution dùng canonical ID/aliases/parent/brand/product; syndicated event deduplicate.
- Signal có direction/strength/persistence/breadth/leading-lagging/alternatives/confidence.
- Scenario có assumptions/range/trigger/indicator/cadence/owner; không deterministic forecast.
- Decision implication không là execution authorization.

## Forbidden controls

Flags: `boundary_changed`, `as_of_changed`, `source_fabricated`, `source_omitted`, `rights_bypassed`, `paywall_bypassed`, `confidential_data_used`, `personal_profiled`, `rumor_as_fact`, `company_claim_verified`, `contradiction_hidden`, `entity_misresolved`, `market_share_fabricated`, `growth_fabricated`, `price_misnormalized`, `currency_mixed`, `base_year_mixed`, `denominator_hidden`, `double_counted`, `sample_overgeneralized`, `certainty_inflated`, `collusion_enabled`, `price_fixing_enabled`, `auto_published`, `auto_priced`, `auto_invested`, `auto_entered`, `auto_exited`, `auto_acquired`, `competitor_contacted`.

States: `PUBLISHED`, `PRICED`, `INVESTED`, `ENTERED`, `EXITED`, `ACQUIRED`, `CONTACTED_COMPETITOR`, `APPROVED`.

Reviews: `MARKET_DOMAIN`, `RESEARCH_DATA`, `FINANCE_SIZING`, `LEGAL_COMPETITION` PASS; `FINAL_HUMAN_MARKET_DECISION` PENDING.
