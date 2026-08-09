## Purpose

`saleor/discount/utils` (`saleor/discount/utils`) groups 7 source file(s) exposing 73 top-level declaration(s).

## Public surface

**`saleor/discount/utils/checkout.py`**

- `create_or_update_discount_objects_from_promotion_for_checkout` (function) — [saleor/discount/utils/checkout.py:34]
- `create_checkout_line_discount_objects_for_catalogue_promotions` (function) — [saleor/discount/utils/checkout.py:50]
- `prepare_checkout_line_discount_objects_for_catalogue_promotions` (function) — [saleor/discount/utils/checkout.py:104]
- `create_checkout_discount_objects_for_order_promotions` (function) — [saleor/discount/utils/checkout.py:214]
- `has_checkout_order_promotion` (function) — [saleor/discount/utils/checkout.py:320]

**`saleor/discount/utils/manual_discount.py`**

- `apply_discount_to_value` (function) — [saleor/discount/utils/manual_discount.py:15]
- `split_manual_discount` (function) — [saleor/discount/utils/manual_discount.py:35]

**`saleor/discount/utils/order.py`**

- `create_order_line_discount_objects` (function) — [saleor/discount/utils/order.py:38]
- `update_catalogue_promotion_discount_amount_for_order` (function) — [saleor/discount/utils/order.py:100]
- `update_unit_discount_data_on_order_line` (function) — [saleor/discount/utils/order.py:124]
- `update_unit_discount_data_on_order_lines_info` (function) — [saleor/discount/utils/order.py:158]
- `handle_order_promotion` (function) — [saleor/discount/utils/order.py:166]
- `create_order_discount_objects_for_order_promotions` (function) — [saleor/discount/utils/order.py:181]
- `create_order_line_discount_objects_for_catalogue_promotions` (function) — [saleor/discount/utils/order.py:280]
- `refresh_order_line_discount_objects_for_catalogue_promotions` (function) — [saleor/discount/utils/order.py:303]
- `prepare_order_line_discount_objects_for_catalogue_promotions` (function) — [saleor/discount/utils/order.py:313]
- `refresh_manual_line_discount_object` (function) — [saleor/discount/utils/order.py:396]

**`saleor/discount/utils/promotion.py`**

- `prepare_promotion_discount_reason` (function) — [saleor/discount/utils/promotion.py:70]
- `get_sale_id` (function) — [saleor/discount/utils/promotion.py:76]
- `calculate_discounted_price_for_rules` (function) — [saleor/discount/utils/promotion.py:84]
- `calculate_discounted_price_for_promotions` (function) — [saleor/discount/utils/promotion.py:99]
- `get_best_promotion_discount` (function) — [saleor/discount/utils/promotion.py:116]
- `get_product_promotion_discounts` (function) — [saleor/discount/utils/promotion.py:147]
- `get_product_discount_on_promotion` (function) — [saleor/discount/utils/promotion.py:160]
- `is_discounted_line_by_catalogue_promotion` (function) — [saleor/discount/utils/promotion.py:170]
- `get_discount_name` (function) — [saleor/discount/utils/promotion.py:222]
- `get_discount_translated_name` (function) — [saleor/discount/utils/promotion.py:228]
- `update_promotion_discount` (function) — [saleor/discount/utils/promotion.py:240]
- `get_best_rule` (function) — [saleor/discount/utils/promotion.py:272]
- `RuleDiscount` (class) — [saleor/discount/utils/promotion.py:279]
- `delete_gift_lines_qs` (function) — [saleor/discount/utils/promotion.py:418]
- `delete_gift_line` (function) — [saleor/discount/utils/promotion.py:434]
- `create_gift_line` (function) — [saleor/discount/utils/promotion.py:455]
- `get_variants_to_promotion_rules_map` (function) — [saleor/discount/utils/promotion.py:518]
- `fetch_promotion_rules_for_checkout_or_order` (function) — [saleor/discount/utils/promotion.py:566]
- `get_current_products_for_rules` (function) — [saleor/discount/utils/promotion.py:624]
- `update_rule_variant_relation` (function) — [saleor/discount/utils/promotion.py:652]
- `create_discount_objects_for_order_promotions` (function) — [saleor/discount/utils/promotion.py:718]
- `get_active_catalogue_promotion_rules` (function) — [saleor/discount/utils/promotion.py:907]
- `mark_active_catalogue_promotion_rules_as_dirty` (function) — [saleor/discount/utils/promotion.py:925]
- `mark_catalogue_promotion_rules_as_dirty` (function) — [saleor/discount/utils/promotion.py:954]

**`saleor/discount/utils/shared.py`**

- `update_discount` (function) — [saleor/discount/utils/shared.py:21]
- `update_line_info_cached_discounts` (function) — [saleor/discount/utils/shared.py:71]
- `is_order_level_discount` (function) — [saleor/discount/utils/shared.py:91]
- `discount_info_for_logs` (function) — [saleor/discount/utils/shared.py:100]

**`saleor/discount/utils/voucher.py`**

- `VoucherDenormalizedInfo` (class) — [saleor/discount/utils/voucher.py:41]
- `is_order_level_voucher` (function) — [saleor/discount/utils/voucher.py:51]
- `is_shipping_voucher` (function) — [saleor/discount/utils/voucher.py:59]
- `is_line_level_voucher` (function) — [saleor/discount/utils/voucher.py:63]
- `increase_voucher_usage` (function) — [saleor/discount/utils/voucher.py:69]
- `increase_voucher_code_usage_value` (function) — [saleor/discount/utils/voucher.py:83]
- `decrease_voucher_code_usage_value` (function) — [saleor/discount/utils/voucher.py:89]
- `deactivate_voucher_code` (function) — [saleor/discount/utils/voucher.py:100]
- `activate_voucher_code` (function) — [saleor/discount/utils/voucher.py:106]
- `add_voucher_usage_by_customer` (function) — [saleor/discount/utils/voucher.py:112]
- `remove_voucher_usage_by_customer` (function) — [saleor/discount/utils/voucher.py:125]
- `release_voucher_code_usage` (function) — [saleor/discount/utils/voucher.py:133]
- `get_voucher_code_instance` (function) — [saleor/discount/utils/voucher.py:148]
- `get_active_voucher_code` (function) — [saleor/discount/utils/voucher.py:177]
- `attach_voucher_to_line_info` (function) — [saleor/discount/utils/voucher.py:194]
- `get_discounted_lines` (function) — [saleor/discount/utils/voucher.py:220]
- `get_the_cheapest_line` (function) — [saleor/discount/utils/voucher.py:256]
- `get_customer_email_for_voucher_usage` (function) — [saleor/discount/utils/voucher.py:264]
- `validate_voucher_for_checkout` (function) — [saleor/discount/utils/voucher.py:280]
- `validate_voucher_in_order` (function) — [saleor/discount/utils/voucher.py:307]
- `validate_voucher` (function) — [saleor/discount/utils/voucher.py:327]
- `get_products_voucher_discount` (function) — [saleor/discount/utils/voucher.py:343]
- `create_or_update_voucher_discount_objects_for_order` (function) — [saleor/discount/utils/voucher.py:354]
- `create_or_update_discount_object_from_order_level_voucher` (function) — [saleor/discount/utils/voucher.py:387]
- `create_or_update_line_discount_objects_from_voucher` (function) — [saleor/discount/utils/voucher.py:484]
- `prepare_line_discount_objects_for_voucher` (function) — [saleor/discount/utils/voucher.py:512]
- `calculate_line_discount_amount_from_voucher` (function) — [saleor/discount/utils/voucher.py:622]
- `calculate_order_line_discount_amount_from_denormalized_voucher` (function) — [saleor/discount/utils/voucher.py:664]

## How it works

The module's files, as provided to this run:

- `saleor/discount/utils/__init__.py` (1 lines)
- `saleor/discount/utils/checkout.py` (328 lines)
- `saleor/discount/utils/manual_discount.py` (55 lines)
- `saleor/discount/utils/order.py` (421 lines)
- `saleor/discount/utils/promotion.py` (971 lines)
- `saleor/discount/utils/shared.py` (133 lines)
- `saleor/discount/utils/voucher.py` (719 lines)

## Interactions

- Imports from: `saleor/discount`, `saleor/graphql/product/types`, `saleor/core`, `saleor/plugins/openid_connect`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....settings`
- `...DiscountType`
- `...DiscountValueType`
- `...VoucherType`
- `...account.models.User`
- `...channel.models.Channel`
- `...checkout.base_calculations`
- `...checkout.fetch.CheckoutInfo`
- `...checkout.fetch.CheckoutLineInfo`
- `...checkout.models.Checkout`
- `...checkout.models.CheckoutLine`
- `...checkout.utils.calculate_checkout_quantity`
- `...core.db.connection.allow_writer`
- `...core.exceptions.InsufficientStock`
- `...core.prices.quantize_price`
- `...core.pricing.interface.LineInfo`
- `...core.taxes.zero_money`
- `...core.utils.promo_code.InvalidPromoCode`
- `...graphql.core.utils.to_global_id_or_none`
- `...graphql.discount.utils.PredicateObjectType`
- `...graphql.discount.utils.filter_qs_by_predicate`
- `...order.base_calculations.base_order_subtotal`
- `...order.fetch.EditableOrderLineInfo`
- `...order.fetch.fetch_draft_order_lines_info`
- `...order.lock_objects.order_qs_select_for_update`
- `...order.models.Order`
- `...order.models.OrderLine`
- `...order.utils.get_order_country`
- `...order.utils.get_total_quantity`
- `...plugins.manager.PluginsManager`
- `...product.managers.ProductVariantQueryset`
- `...warehouse.availability.check_stock_quantity_bulk`
- `..interface.DiscountInfo`
- `..interface.VariantPromotionRuleInfo`
- `..interface.VoucherInfo`
- `..interface.get_rule_translations`
- `..models.DiscountValueType`
- `..models.OrderDiscount`
- `..models.OrderLineDiscount`
- `..models.Voucher`
- `.manual_discount.apply_discount_to_value`
- `.shared.update_discount`
- `.shared.update_line_info_cached_discounts`
- `.voucher.is_order_level_voucher`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `a8f26e1e3eee` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
