## Purpose

`saleor/discount/tests/test_utils` (`saleor/discount/tests/test_utils`) groups 14 source file(s) exposing 107 top-level declaration(s).

## Public surface

**`saleor/discount/tests/test_utils/test_calculate_discounted_price_for_promotions.py`**

- `test_variant_discounts_multiple_promotions` (function) — [saleor/discount/tests/test_utils/test_calculate_discounted_price_for_promotions.py:10]
- `test_variant_discounts_multiple_promotions_and_rules` (function) — [saleor/discount/tests/test_utils/test_calculate_discounted_price_for_promotions.py:83]

**`saleor/discount/tests/test_utils/test_copy_unit_discount_data_to_order_line.py`**

- `test_copy_unit_discount_data_to_order_line_multiple_discounts` (function) — [saleor/discount/tests/test_utils/test_copy_unit_discount_data_to_order_line.py:11]
- `test_copy_unit_discount_data_to_order_line_single_discount` (function) — [saleor/discount/tests/test_utils/test_copy_unit_discount_data_to_order_line.py:52]
- `test_copy_unit_discount_data_to_order_line_no_discount` (function) — [saleor/discount/tests/test_utils/test_copy_unit_discount_data_to_order_line.py:81]

**`saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py`**

- `test_create_or_update_discount_objects_from_promotion_for_checkout_no_discount` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:33]
- `test_create_fixed_discount` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:48]
- `test_update_catalogue_discount` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:146]
- `test_create_fixed_discount_multiple_quantity_in_lines` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:220]
- `test_create_fixed_discount_multiple_quantity_in_lines_discount_bigger_than_total` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:309]
- `test_create_percentage_discount` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:383]
- `test_create_percentage_discount_multiple_quantity_in_lines` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:472]
- `test_two_promotions_applied_to_two_different_lines` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:561]
- `test_create_percentage_discount_1_cent_variant_on_10_percentage_discount` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:736]
- `test_promotion_not_valid_anymore` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:835]
- `test_one_of_promotion_rule_not_valid_anymore_one_updated` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:881]
- `test_gift_promotion_not_valid_anymore` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:1004]
- `test_create_discount_with_promotion_translation` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:1036]
- `test_create_discount_with_rule_translation` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:1100]
- `test_create_discount_with_promotion_and_rule_translation` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:1164]
- `test_create_or_update_discount_for_gift_promotion_line` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:1229]
- `test_create_or_update_discount_objects_from_promotion_for_checkout_voucher_set` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:1289]
- `test_create_or_update_discount_objects_from_promotion_no_applicable_rules` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:1308]
- `test_create_or_update_discount_objects_from_promotion` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:1334]
- `test_create_or_update_discount_objects_from_promotion_best_rule_applies` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:1406]
- `test_create_or_update_discount_objects_from_promotion_subtotal_price_discount` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:1512]
- `test_create_gift_discount` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:1576]
- `test_update_gift_discount` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:1619]
- `test_create_or_update_discount_objects_from_promotion_gift_rule_applies` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:1674]
- `test_create_or_update_discount_objects_from_promotion_gift_line_removed` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:1782]
- `test_create_or_update_discount_from_promotion_voucher_code_set_checkout_discount` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:1880]
- `test_create_or_update_discount_from_promotion_checkout_discount_updated` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:1940]
- `test_create_or_update_discount_from_promotion_rule_not_applies_anymore` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:2005]
- `test_create_discount_objects_for_order_promotions_race_condition` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:2063]
- `call_before_creating_discount_object` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:2103]
- `test_create_discount_objects_for_order_promotions_missing_rule_on_discount_object` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:2128]
- `test_create_or_update_order_discount_race_condition` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:2169]
- `call_update` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:2193]
- `test_create_or_update_order_discount_gift_reward_race_condition` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:2210]
- `call_update` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:2218]
- `test_get_best_gift_reward` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:2237]
- `test_get_best_gift_reward_insufficient_stock` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:2276]
- `test_get_best_gift_reward_no_available_for_purchase_variants` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:2295]
- `test_get_best_gift_reward_no_variants_in_channel` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:2317]
- `test_create_checkout_line_discount_objects_for_catalogue_promotions_race_condition` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py:2333]
- _…and 3 more in this file_

**`saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_order.py`**

- `test_create_catalogue_discount_fixed` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_order.py:20]
- `test_create_catalogue_discount_percentage` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_order.py:78]
- `test_create_order_discount_subtotal_fixed` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_order.py:138]
- `test_create_order_discount_subtotal_percentage` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_order.py:178]
- `test_create_order_discount_gift` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_order.py:218]
- `test_multiple_rules_subtotal_and_catalogue_discount_applied` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_order.py:279]
- `test_multiple_rules_gift_and_catalogue_discount_applied` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_order.py:317]
- `test_multiple_rules_no_discount_applied` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_order.py:361]
- `test_update_order_discount_subtotal` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_order.py:401]
- `test_update_gift_discount_new_gift_available` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_order.py:439]
- `test_create_multiple_catalogue_discounts_for_the_same_line_is_not_allowed` (function) — [saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_order.py:480]

**`saleor/discount/tests/test_utils/test_create_voucher_discount_object_for_order.py`**

- `test_create_discount_for_voucher_specific_product_fixed` (function) — [saleor/discount/tests/test_utils/test_create_voucher_discount_object_for_order.py:14]
- `test_create_discount_for_voucher_specific_product_percentage` (function) — [saleor/discount/tests/test_utils/test_create_voucher_discount_object_for_order.py:116]
- `test_create_discount_for_voucher_apply_once_per_order_percentage` (function) — [saleor/discount/tests/test_utils/test_create_voucher_discount_object_for_order.py:223]
- `test_create_discount_for_voucher_apply_once_per_order_fixed` (function) — [saleor/discount/tests/test_utils/test_create_voucher_discount_object_for_order.py:335]
- `test_create_discount_for_voucher_entire_order_fixed` (function) — [saleor/discount/tests/test_utils/test_create_voucher_discount_object_for_order.py:441]
- `test_create_discount_for_voucher_entire_order_multiple_lines` (function) — [saleor/discount/tests/test_utils/test_create_voucher_discount_object_for_order.py:557]
- `test_create_discount_for_voucher_entire_order_percentage` (function) — [saleor/discount/tests/test_utils/test_create_voucher_discount_object_for_order.py:654]
- `test_create_discount_for_voucher_shipping_fixed` (function) — [saleor/discount/tests/test_utils/test_create_voucher_discount_object_for_order.py:765]
- `test_create_discount_for_voucher_shipping_percentage` (function) — [saleor/discount/tests/test_utils/test_create_voucher_discount_object_for_order.py:843]
- `test_create_discount_for_voucher_specific_product_line_with_catalogue_discount` (function) — [saleor/discount/tests/test_utils/test_create_voucher_discount_object_for_order.py:921]

**`saleor/discount/tests/test_utils/test_fetch_promotion_rules_for_checkout.py`**

- `test_fetch_promotion_rules_for_checkout` (function) — [saleor/discount/tests/test_utils/test_fetch_promotion_rules_for_checkout.py:8]
- `test_fetch_promotion_rules_for_checkout_no_matching_rule` (function) — [saleor/discount/tests/test_utils/test_fetch_promotion_rules_for_checkout.py:33]
- `test_fetch_promotion_rules_for_checkout_relevant_channel_only` (function) — [saleor/discount/tests/test_utils/test_fetch_promotion_rules_for_checkout.py:57]
- `test_fetch_promotion_rules_for_checkout_inner_or_operator` (function) — [saleor/discount/tests/test_utils/test_fetch_promotion_rules_for_checkout.py:87]

**`saleor/discount/tests/test_utils/test_fetch_promotion_rules_for_order.py`**

- `test_fetch_promotion_rules_for_order` (function) — [saleor/discount/tests/test_utils/test_fetch_promotion_rules_for_order.py:8]
- `test_fetch_promotion_rules_for_order_no_matching_rule` (function) — [saleor/discount/tests/test_utils/test_fetch_promotion_rules_for_order.py:24]
- `test_fetch_promotion_rules_for_order_relevant_channel_only` (function) — [saleor/discount/tests/test_utils/test_fetch_promotion_rules_for_order.py:41]
- `test_fetch_promotion_rules_for_checkout_inner_or_operator` (function) — [saleor/discount/tests/test_utils/test_fetch_promotion_rules_for_order.py:72]

**`saleor/discount/tests/test_utils/test_get_customer_email_for_voucher_usage.py`**

- `test_get_customer_email_for_voucher_usage_for_checkout_info_without_user_data` (function) — [saleor/discount/tests/test_utils/test_get_customer_email_for_voucher_usage.py:4]
- `test_get_customer_email_for_voucher_usage_for_checkout_info_with_user` (function) — [saleor/discount/tests/test_utils/test_get_customer_email_for_voucher_usage.py:19]
- `test_get_customer_email_for_voucher_usage_for_checkout_info_without_user` (function) — [saleor/discount/tests/test_utils/test_get_customer_email_for_voucher_usage.py:33]
- `test_get_customer_email_for_voucher_usage_for_checkout_with_user` (function) — [saleor/discount/tests/test_utils/test_get_customer_email_for_voucher_usage.py:48]
- `test_get_customer_email_for_voucher_usage_for_checkout_without_user` (function) — [saleor/discount/tests/test_utils/test_get_customer_email_for_voucher_usage.py:64]
- `test_get_customer_email_for_voucher_usage_for_checkout_without_user_details` (function) — [saleor/discount/tests/test_utils/test_get_customer_email_for_voucher_usage.py:78]
- `test_get_customer_email_for_voucher_usage_for_order_with_user` (function) — [saleor/discount/tests/test_utils/test_get_customer_email_for_voucher_usage.py:93]
- `test_get_customer_email_for_voucher_usage_for_order_without_user` (function) — [saleor/discount/tests/test_utils/test_get_customer_email_for_voucher_usage.py:107]
- `test_get_customer_email_for_voucher_usage_for_order_without_user_details` (function) — [saleor/discount/tests/test_utils/test_get_customer_email_for_voucher_usage.py:121]

**`saleor/discount/tests/test_utils/test_get_variants_to_promotions_map.py`**

- `test_get_variants_to_promotions_map` (function) — [saleor/discount/tests/test_utils/test_get_variants_to_promotions_map.py:12]
- `test_get_variants_to_promotions_map_from_different_promotions` (function) — [saleor/discount/tests/test_utils/test_get_variants_to_promotions_map.py:65]
- `test_get_variants_to_promotions_map_no_active_rules` (function) — [saleor/discount/tests/test_utils/test_get_variants_to_promotions_map.py:118]
- `test_get_variants_to_promotions_map_no_matching_rules` (function) — [saleor/discount/tests/test_utils/test_get_variants_to_promotions_map.py:130]

**`saleor/discount/tests/test_utils/test_mark_active_promotion_rules_as_dirty.py`**

- `test_mark_active_catalogue_promotion_rules_as_dirty_with_empty_channel_list` (function) — [saleor/discount/tests/test_utils/test_mark_active_promotion_rules_as_dirty.py:13]
- `test_mark_active_catalogue_promotion_rules_as_dirty_with_single_channel` (function) — [saleor/discount/tests/test_utils/test_mark_active_promotion_rules_as_dirty.py:23]
- `test_mark_active_catalogue_promotion_rules_as_dirty_with_multiple_channels` (function) — [saleor/discount/tests/test_utils/test_mark_active_promotion_rules_as_dirty.py:42]
- `test_mark_active_promotion_rules_as_dirty_with_multiple_promotions_and_channels` (function) — [saleor/discount/tests/test_utils/test_mark_active_promotion_rules_as_dirty.py:90]

**`saleor/discount/tests/test_utils/test_mark_promotion_rules_as_dirty.py`**

- `test_mark_catalogue_promotion_rules_as_dirty_with_empty_list_as_input` (function) — [saleor/discount/tests/test_utils/test_mark_promotion_rules_as_dirty.py:13]
- `test_mark_catalogue_promotion_rules_as_dirty_single_promotion` (function) — [saleor/discount/tests/test_utils/test_mark_promotion_rules_as_dirty.py:23]
- `test_mark_catalogue_promotion_rules_as_dirty_multiple_promotion` (function) — [saleor/discount/tests/test_utils/test_mark_promotion_rules_as_dirty.py:61]

**`saleor/discount/tests/test_utils/test_update_rule_variant_relation.py`**

- `test_update_rule_variant_relation` (function) — [saleor/discount/tests/test_utils/test_update_rule_variant_relation.py:10]

**`saleor/discount/tests/test_utils/test_update_voucher_discount_object_for_order.py`**

- `test_update_voucher_discount_specific_product_with_different_variants` (function) — [saleor/discount/tests/test_utils/test_update_voucher_discount_object_for_order.py:15]
- `test_update_voucher_discount_specific_product_with_apply_once_per_order` (function) — [saleor/discount/tests/test_utils/test_update_voucher_discount_object_for_order.py:143]
- `test_update_voucher_discount_apply_once_per_order_with_specific_product` (function) — [saleor/discount/tests/test_utils/test_update_voucher_discount_object_for_order.py:281]
- `test_update_voucher_discount_specific_product_with_entire_order` (function) — [saleor/discount/tests/test_utils/test_update_voucher_discount_object_for_order.py:406]
- `test_update_voucher_discount_shipping_with_specific_product` (function) — [saleor/discount/tests/test_utils/test_update_voucher_discount_object_for_order.py:563]
- `test_update_voucher_discount_specific_product_with_shipping` (function) — [saleor/discount/tests/test_utils/test_update_voucher_discount_object_for_order.py:695]
- `test_update_voucher_discount_shipping_with_entire_order` (function) — [saleor/discount/tests/test_utils/test_update_voucher_discount_object_for_order.py:820]
- `test_update_voucher_discount_entire_order_with_shipping` (function) — [saleor/discount/tests/test_utils/test_update_voucher_discount_object_for_order.py:972]
- `test_update_voucher_discount_entire_order_with_specific_product` (function) — [saleor/discount/tests/test_utils/test_update_voucher_discount_object_for_order.py:1093]

## How it works

The module's files, as provided to this run:

- `saleor/discount/tests/test_utils/__init__.py` (1 lines)
- `saleor/discount/tests/test_utils/test_calculate_discounted_price_for_promotions.py` (168 lines)
- `saleor/discount/tests/test_utils/test_copy_unit_discount_data_to_order_line.py` (96 lines)
- `saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_checkout.py` (2392 lines)
- `saleor/discount/tests/test_utils/test_create_or_update_discount_objects_from_promotion_for_order.py` (544 lines)
- `saleor/discount/tests/test_utils/test_create_voucher_discount_object_for_order.py` (1085 lines)
- `saleor/discount/tests/test_utils/test_fetch_promotion_rules_for_checkout.py` (118 lines)
- `saleor/discount/tests/test_utils/test_fetch_promotion_rules_for_order.py` (96 lines)
- `saleor/discount/tests/test_utils/test_get_customer_email_for_voucher_usage.py` (131 lines)
- `saleor/discount/tests/test_utils/test_get_variants_to_promotions_map.py` (157 lines)
- `saleor/discount/tests/test_utils/test_mark_active_promotion_rules_as_dirty.py` (135 lines)
- `saleor/discount/tests/test_utils/test_mark_promotion_rules_as_dirty.py` (93 lines)
- `saleor/discount/tests/test_utils/test_update_rule_variant_relation.py` (52 lines)
- `saleor/discount/tests/test_utils/test_update_voucher_discount_object_for_order.py` (1220 lines)

## Interactions

- Imports from: `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....DiscountType`
- `....DiscountValueType`
- `....PromotionRuleInfo`
- `....RewardType`
- `....RewardValueType`
- `....VoucherType`
- `....checkout.base_calculations.base_checkout_total`
- `....checkout.fetch.fetch_checkout_info`
- `....checkout.fetch.fetch_checkout_lines`
- `....core.prices.Money`
- `....core.prices.quantize_price`
- `....core.taxes.zero_money`
- `....discount.interface.VariantPromotionRuleInfo`
- `....order.OrderStatus`
- `....order.calculations.fetch_order_prices_if_expired`
- `....order.fetch.fetch_draft_order_lines_info`
- `....plugins.manager.get_plugins_manager`
- `....product.models.ProductVariant`
- `....product.utils.variants.fetch_variants_for_promotion_rules`
- `....tests.race_condition`
- `....warehouse.models.Stock`
- `...interface.VariantPromotionRuleInfo`
- `...interface.fetch_variant_rules_info`
- `...models.CheckoutDiscount`
- `...models.CheckoutLineDiscount`
- `...models.OrderDiscount`
- `...models.OrderLineDiscount`
- `...models.Promotion`
- `...models.PromotionRule`
- `...models.Voucher`
- `...utils.order.update_unit_discount_data_on_order_lines_info`
- `...utils.promotion.calculate_discounted_price_for_promotions`
- `...utils.promotion.fetch_promotion_rules_for_checkout_or_order`
- `...utils.promotion.get_variants_to_promotion_rules_map`
- `...utils.promotion.mark_active_catalogue_promotion_rules_as_dirty`
- `...utils.promotion.mark_catalogue_promotion_rules_as_dirty`
- `...utils.promotion.update_rule_variant_relation`
- `...utils.voucher.create_or_update_voucher_discount_objects_for_order`
- `...utils.voucher.get_customer_email_for_voucher_usage`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `963ce9603ab4` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
