## Purpose

`saleor/discount/tests` (`saleor/discount/tests`) groups 4 source file(s) exposing 55 top-level declaration(s).

## Public surface

**`saleor/discount/tests/test_discounts.py`**

- `test_valid_voucher_min_spent_amount` (function) — [saleor/discount/tests/test_discounts.py:39]
- `test_valid_voucher_min_spent_amount_not_reached` (function) — [saleor/discount/tests/test_discounts.py:56]
- `test_valid_voucher_min_spent_amount_voucher_not_assigned_to_channel` (function) — [saleor/discount/tests/test_discounts.py:74]
- `test_valid_voucher_min_checkout_items_quantity` (function) — [saleor/discount/tests/test_discounts.py:94]
- `test_percentage_discounts` (function) — [saleor/discount/tests/test_discounts.py:109]
- `test_fixed_discounts` (function) — [saleor/discount/tests/test_discounts.py:142]
- `test_voucher_queryset_active` (function) — [saleor/discount/tests/test_discounts.py:173]
- `test_voucher_queryset_active_in_channel` (function) — [saleor/discount/tests/test_discounts.py:182]
- `test_voucher_queryset_active_in_other_channel` (function) — [saleor/discount/tests/test_discounts.py:191]
- `test_increase_voucher_usage` (function) — [saleor/discount/tests/test_discounts.py:200]
- `test_decrease_voucher_usage` (function) — [saleor/discount/tests/test_discounts.py:218]
- `test_decrease_voucher_usage_used_0` (function) — [saleor/discount/tests/test_discounts.py:236]
- `test_deactivate_voucher_code` (function) — [saleor/discount/tests/test_discounts.py:259]
- `test_activate_voucher_code` (function) — [saleor/discount/tests/test_discounts.py:271]
- `test_add_voucher_usage_by_customer` (function) — [saleor/discount/tests/test_discounts.py:285]
- `test_add_voucher_usage_by_customer_raise_not_applicable` (function) — [saleor/discount/tests/test_discounts.py:300]
- `test_add_voucher_usage_by_customer_without_customer_email` (function) — [saleor/discount/tests/test_discounts.py:311]
- `test_remove_voucher_usage_by_customer` (function) — [saleor/discount/tests/test_discounts.py:320]
- `test_remove_voucher_usage_by_customer_not_exists` (function) — [saleor/discount/tests/test_discounts.py:333]
- `test_validate_voucher` (function) — [saleor/discount/tests/test_discounts.py:356]
- `test_validate_staff_voucher_for_anonymous` (function) — [saleor/discount/tests/test_discounts.py:382]
- `test_validate_staff_voucher_for_normal_customer` (function) — [saleor/discount/tests/test_discounts.py:402]
- `test_validate_staff_voucher_for_staff_customer` (function) — [saleor/discount/tests/test_discounts.py:422]
- `test_validate_voucher_not_applicable` (function) — [saleor/discount/tests/test_discounts.py:455]
- `test_validate_voucher_not_applicable_once_per_customer` (function) — [saleor/discount/tests/test_discounts.py:484]
- `test_get_discount_name_only_rule_name` (function) — [saleor/discount/tests/test_discounts.py:514]
- `test_get_discount_name_only_rule_promotion_name` (function) — [saleor/discount/tests/test_discounts.py:529]
- `test_get_discount_name_rule_and_promotion_name` (function) — [saleor/discount/tests/test_discounts.py:543]
- `test_get_discount_name_empty_names` (function) — [saleor/discount/tests/test_discounts.py:555]
- `test_get_discount_translated_name_only_rule_translation` (function) — [saleor/discount/tests/test_discounts.py:573]
- `test_get_discount_translated_name_only_rule_promotion_translation` (function) — [saleor/discount/tests/test_discounts.py:586]
- `test_get_discount_translated_name_rule_and_promotion_translations` (function) — [saleor/discount/tests/test_discounts.py:599]
- `test_get_discount_translated_name_no_translations` (function) — [saleor/discount/tests/test_discounts.py:610]
- `test_is_order_level_voucher` (function) — [saleor/discount/tests/test_discounts.py:624]
- `test_is_order_level_voucher_apply_once_per_order` (function) — [saleor/discount/tests/test_discounts.py:636]
- `test_is_order_level_voucher_no_voucher` (function) — [saleor/discount/tests/test_discounts.py:649]
- `test_is_order_level_voucher_another_type` (function) — [saleor/discount/tests/test_discounts.py:660]
- `test_get_the_cheapest_line_no_lines_provided` (function) — [saleor/discount/tests/test_discounts.py:672]
- `test_get_the_cheapest_line` (function) — [saleor/discount/tests/test_discounts.py:679]
- `test_split_manual_discount` (function) — [saleor/discount/tests/test_discounts.py:729]
- _…and 1 more in this file_

**`saleor/discount/tests/test_rounding_issue.py`**

- `test_rounding_issue_with_percentage_promotion` (function) — [saleor/discount/tests/test_rounding_issue.py:31]

**`saleor/discount/tests/test_tasks.py`**

- `test_fetch_promotion_variants_and_product_ids` (function) — [saleor/discount/tests/test_tasks.py:35]
- `test_handle_promotion_toggle` (function) — [saleor/discount/tests/test_tasks.py:79]
- `test_clear_promotion_rule_variants_task` (function) — [saleor/discount/tests/test_tasks.py:206]
- `test_clear_promotion_rule_variants_task_marks_products_as_dirty` (function) — [saleor/discount/tests/test_tasks.py:231]
- `test_set_promotion_rule_variants_task` (function) — [saleor/discount/tests/test_tasks.py:258]
- `test_decrease_voucher_code_usage_of_draft_orders_multiple_use` (function) — [saleor/discount/tests/test_tasks.py:273]
- `test_decrease_voucher_code_usage_task_multiple_use` (function) — [saleor/discount/tests/test_tasks.py:298]
- `test_decrease_voucher_code_usage_task_single_use` (function) — [saleor/discount/tests/test_tasks.py:326]
- `test_disconnect_voucher_codes_from_draft_orders` (function) — [saleor/discount/tests/test_tasks.py:344]
- `test_release_voucher_code_usage_of_draft_orders_single_use` (function) — [saleor/discount/tests/test_tasks.py:381]
- `test_release_voucher_code_usage_of_draft_orders_multiple_use` (function) — [saleor/discount/tests/test_tasks.py:407]
- `test_release_voucher_code_usage_of_draft_orders_clears_voucher_customers` (function) — [saleor/discount/tests/test_tasks.py:429]
- `test_release_voucher_code_usage_of_draft_orders_no_codes` (function) — [saleor/discount/tests/test_tasks.py:466]

## How it works

The module's files, as provided to this run:

- `saleor/discount/tests/__init__.py` (1 lines)
- `saleor/discount/tests/test_discounts.py` (803 lines)
- `saleor/discount/tests/test_rounding_issue.py` (113 lines)
- `saleor/discount/tests/test_tasks.py` (476 lines)

## Interactions

- Imports from: `saleor/discount`, `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...DiscountType`
- `...DiscountValueType`
- `...RewardValueType`
- `...VoucherType`
- `...checkout.fetch.CheckoutLineInfo`
- `...checkout.fetch.fetch_checkout_info`
- `...checkout.fetch.fetch_checkout_lines`
- `...checkout.tests.utils.add_variant_to_checkout`
- `...discount.interface.VariantPromotionRuleInfo`
- `...discount.models.PromotionRule`
- `...order.OrderStatus`
- `...order.models.Order`
- `...plugins.manager.get_plugins_manager`
- `...product.models.Product`
- `...product.models.ProductChannelListing`
- `...product.models.ProductVariant`
- `...product.models.ProductVariantChannelListing`
- `...product.utils.variant_prices.update_discounted_prices_for_promotion`
- `...product.utils.variants.fetch_variants_for_promotion_rules`
- `..utils.manual_discount.split_manual_discount`
- `..utils.promotion.mark_catalogue_promotion_rules_as_dirty`
- `..utils.shared.discount_info_for_logs`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c79520f6a2b3` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
