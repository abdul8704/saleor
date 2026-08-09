## Purpose

`saleor/checkout` (`saleor/checkout`) groups 15 source file(s) exposing 190 top-level declaration(s).

## Public surface

**`saleor/checkout/__init__.py`**

- `AddressType` (class) — [saleor/checkout/__init__.py:6]
- `CheckoutChargeStatus` (class) — [saleor/checkout/__init__.py:16]
- `CheckoutAuthorizeStatus` (class) — [saleor/checkout/__init__.py:46]

**`saleor/checkout/actions.py`**

- `call_checkout_event` (function) — [saleor/checkout/actions.py:41]
- `call_checkout_events` (function) — [saleor/checkout/actions.py:56]
- `call_checkout_info_event` (function) — [saleor/checkout/actions.py:76]
- `update_last_transaction_modified_at_for_checkout` (function) — [saleor/checkout/actions.py:97]
- `transaction_amounts_for_checkout_updated` (function) — [saleor/checkout/actions.py:108]
- `transaction_amounts_for_checkout_updated_without_price_recalculation` (function) — [saleor/checkout/actions.py:134]

**`saleor/checkout/base_calculations.py`**

- `calculate_base_line_unit_price` (function) — [saleor/checkout/base_calculations.py:23]
- `calculate_base_line_total_price` (function) — [saleor/checkout/base_calculations.py:38]
- `calculate_undiscounted_base_line_total_price` (function) — [saleor/checkout/base_calculations.py:68]
- `calculate_undiscounted_base_line_unit_price` (function) — [saleor/checkout/base_calculations.py:80]
- `base_checkout_delivery_price` (function) — [saleor/checkout/base_calculations.py:89]
- `base_checkout_undiscounted_delivery_price` (function) — [saleor/checkout/base_calculations.py:115]
- `calculate_base_price_for_shipping_method` (function) — [saleor/checkout/base_calculations.py:133]
- `base_checkout_total` (function) — [saleor/checkout/base_calculations.py:159]
- `base_checkout_subtotal` (function) — [saleor/checkout/base_calculations.py:176]
- `checkout_total` (function) — [saleor/checkout/base_calculations.py:199]
- `get_line_total_price_with_propagated_checkout_discount` (function) — [saleor/checkout/base_calculations.py:227]

**`saleor/checkout/calculations.py`**

- `checkout_shipping_price` (function) — [saleor/checkout/calculations.py:52]
- `checkout_shipping_tax_rate` (function) — [saleor/checkout/calculations.py:76]
- `checkout_subtotal` (function) — [saleor/checkout/calculations.py:99]
- `calculate_checkout_total_with_gift_cards` (function) — [saleor/checkout/calculations.py:123]
- `calculate_checkout_total` (function) — [saleor/checkout/calculations.py:165]
- `checkout_line_total` (function) — [saleor/checkout/calculations.py:194]
- `checkout_line_unit_price` (function) — [saleor/checkout/calculations.py:220]
- `checkout_line_tax_rate` (function) — [saleor/checkout/calculations.py:247]
- `checkout_line_undiscounted_unit_price` (function) — [saleor/checkout/calculations.py:272]
- `checkout_line_undiscounted_total_price` (function) — [saleor/checkout/calculations.py:287]
- `update_undiscounted_unit_price_for_lines` (function) — [saleor/checkout/calculations.py:299]
- `update_prior_unit_price_for_lines` (function) — [saleor/checkout/calculations.py:311]
- `promise_calculate_taxes_with_error_handling` (function) — [saleor/checkout/calculations.py:329]
- `process_error` (function) — [saleor/checkout/calculations.py:344]
- `remove_tax_if_needed` (function) — [saleor/checkout/calculations.py:423]
- `process_calculation_result` (function) — [saleor/checkout/calculations.py:431]
- `recalculate_discounts` (function) — [saleor/checkout/calculations.py:513]
- `process_flat_taxes` (function) — [saleor/checkout/calculations.py:573]
- `recalculate_with_tax_app_data` (function) — [saleor/checkout/calculations.py:596]
- `recalculate_with_plugins` (function) — [saleor/checkout/calculations.py:623]
- `recalculate_with_tax_app_data` (function) — [saleor/checkout/calculations.py:646]
- `process_error` (function) — [saleor/checkout/calculations.py:672]
- `process_response` (function) — [saleor/checkout/calculations.py:677]
- `fetch_checkout_data` (function) — [saleor/checkout/calculations.py:843]
- `process_refreshed_prices` (function) — [saleor/checkout/calculations.py:862]

**`saleor/checkout/checkout_cleaner.py`**

- `clean_checkout_shipping` (function) — [saleor/checkout/checkout_cleaner.py:25]
- `clean_billing_address` (function) — [saleor/checkout/checkout_cleaner.py:68]
- `clean_checkout_payment` (function) — [saleor/checkout/checkout_cleaner.py:87]
- `validate_checkout_email` (function) — [saleor/checkout/checkout_cleaner.py:105]
- `validate_checkout` (function) — [saleor/checkout/checkout_cleaner.py:146]

**`saleor/checkout/complete_checkout.py`**

- `complete_checkout_pre_payment_part` (function) — [saleor/checkout/complete_checkout.py:1089]
- `complete_checkout_post_payment_part` (function) — [saleor/checkout/complete_checkout.py:1139]
- `create_order_from_checkout` (function) — [saleor/checkout/complete_checkout.py:1562]
- `assign_checkout_user` (function) — [saleor/checkout/complete_checkout.py:1687]
- `complete_checkout` (function) — [saleor/checkout/complete_checkout.py:1700]
- `complete_checkout_with_transaction` (function) — [saleor/checkout/complete_checkout.py:1776]
- `complete_checkout_with_payment` (function) — [saleor/checkout/complete_checkout.py:1824]

**`saleor/checkout/delivery_context.py`**

- `DeliveryMethodBase` (class) — [saleor/checkout/delivery_context.py:41]
- `warehouse_pk` (function) — [saleor/checkout/delivery_context.py:47]
- `delivery_method_order_field` (function) — [saleor/checkout/delivery_context.py:51]
- `is_local_collection_point` (function) — [saleor/checkout/delivery_context.py:55]
- `delivery_method_name` (function) — [saleor/checkout/delivery_context.py:59]
- `get_warehouse_filter_lookup` (function) — [saleor/checkout/delivery_context.py:62]
- `is_valid_delivery_method` (function) — [saleor/checkout/delivery_context.py:65]
- `is_method_in_valid_methods` (function) — [saleor/checkout/delivery_context.py:68]
- `is_delivery_method_set` (function) — [saleor/checkout/delivery_context.py:71]
- `get_details_for_conversion_to_order` (function) — [saleor/checkout/delivery_context.py:74]
- `ShippingMethodInfo` (class) — [saleor/checkout/delivery_context.py:79]
- `delivery_method_name` (function) — [saleor/checkout/delivery_context.py:85]
- `delivery_method_order_field` (function) — [saleor/checkout/delivery_context.py:89]
- `is_valid_delivery_method` (function) — [saleor/checkout/delivery_context.py:94]
- `is_method_in_valid_methods` (function) — [saleor/checkout/delivery_context.py:97]
- `get_details_for_conversion_to_order` (function) — [saleor/checkout/delivery_context.py:100]
- `CollectionPointInfo` (class) — [saleor/checkout/delivery_context.py:122]
- `warehouse_pk` (function) — [saleor/checkout/delivery_context.py:127]
- `delivery_method_order_field` (function) — [saleor/checkout/delivery_context.py:131]
- `is_local_collection_point` (function) — [saleor/checkout/delivery_context.py:135]
- `delivery_method_name` (function) — [saleor/checkout/delivery_context.py:142]
- `get_warehouse_filter_lookup` (function) — [saleor/checkout/delivery_context.py:145]
- `is_valid_delivery_method` (function) — [saleor/checkout/delivery_context.py:152]
- `is_method_in_valid_methods` (function) — [saleor/checkout/delivery_context.py:158]
- `get_details_for_conversion_to_order` (function) — [saleor/checkout/delivery_context.py:164]
- `is_shipping_required` (function) — [saleor/checkout/delivery_context.py:171]
- `get_valid_internal_shipping_methods_for_checkout_info` (function) — [saleor/checkout/delivery_context.py:176]
- `get_valid_collection_points_for_checkout` (function) — [saleor/checkout/delivery_context.py:223]
- `assign_shipping_method_to_checkout` (function) — [saleor/checkout/delivery_context.py:272]
- `assign_collection_point_to_checkout` (function) — [saleor/checkout/delivery_context.py:291]
- `remove_shipping_method_from_checkout` (function) — [saleor/checkout/delivery_context.py:308]
- `remove_click_and_collect_from_checkout` (function) — [saleor/checkout/delivery_context.py:319]
- `remove_delivery_method_from_checkout` (function) — [saleor/checkout/delivery_context.py:332]
- `clear_cc_delivery_method` (function) — [saleor/checkout/delivery_context.py:340]
- `is_delivery_changed` (function) — [saleor/checkout/delivery_context.py:359]
- `get_available_built_in_shipping_methods_for_checkout_info` (function) — [saleor/checkout/delivery_context.py:539]
- `fetch_shipping_methods_for_checkout` (function) — [saleor/checkout/delivery_context.py:598]
- `with_external_methods` (function) — [saleor/checkout/delivery_context.py:625]
- `with_excluded_methods` (function) — [saleor/checkout/delivery_context.py:644]
- `fetch_external_shipping_methods_for_checkout_info` (function) — [saleor/checkout/delivery_context.py:723]
- _…and 2 more in this file_

**`saleor/checkout/error_codes.py`**

- `CheckoutErrorCode` (class) — [saleor/checkout/error_codes.py:4]
- `OrderCreateFromCheckoutErrorCode` (class) — [saleor/checkout/error_codes.py:40]
- `CheckoutCreateFromOrderErrorCode` (class) — [saleor/checkout/error_codes.py:57]
- `CheckoutCreateFromOrderUnavailableVariantErrorCode` (class) — [saleor/checkout/error_codes.py:65]

**`saleor/checkout/fetch.py`**

- `CheckoutLineInfo` (class) — [saleor/checkout/fetch.py:54]
- `variant_discounted_price` (function) — [saleor/checkout/fetch.py:66]
- `undiscounted_unit_price` (function) — [saleor/checkout/fetch.py:95]
- `prior_unit_price_amount` (function) — [saleor/checkout/fetch.py:108]
- `CheckoutInfo` (class) — [saleor/checkout/fetch.py:116]
- `valid_pick_up_points` (function) — [saleor/checkout/fetch.py:134]
- `get_delivery_method_info` (function) — [saleor/checkout/fetch.py:141]
- `get_country` (function) — [saleor/checkout/fetch.py:156]
- `get_customer_email` (function) — [saleor/checkout/fetch.py:162]
- `fetch_checkout_lines` (function) — [saleor/checkout/fetch.py:170]
- `get_variant_channel_listing` (function) — [saleor/checkout/fetch.py:282]
- `fetch_checkout_info` (function) — [saleor/checkout/fetch.py:339]
- `find_checkout_line_info` (function) — [saleor/checkout/fetch.py:379]

**`saleor/checkout/lock_objects.py`**

- `checkout_qs_select_for_update` (function) — [saleor/checkout/lock_objects.py:6]
- `checkout_lines_qs_select_for_update` (function) — [saleor/checkout/lock_objects.py:10]

**`saleor/checkout/models.py`**

- `get_default_country` (function) — [saleor/checkout/models.py:34]
- `CheckoutDelivery` (class) — [saleor/checkout/models.py:38]
- `shipping_method_id` (function) — [saleor/checkout/models.py:91]
- `Meta` (class) — [saleor/checkout/models.py:94]
- `Checkout` (class) — [saleor/checkout/models.py:110]
- `Meta` (class) — [saleor/checkout/models.py:320]
- `safe_update` (function) — [saleor/checkout/models.py:343]
- `get_customer_email` (function) — [saleor/checkout/models.py:368]
- `is_shipping_required` (function) — [saleor/checkout/models.py:375]
- `is_checkout_locked` (function) — [saleor/checkout/models.py:379]
- `get_total_gift_cards_balance` (function) — [saleor/checkout/models.py:388]
- `get_line` (function) — [saleor/checkout/models.py:403]
- `get_last_active_payment` (function) — [saleor/checkout/models.py:408]
- `set_country` (function) — [saleor/checkout/models.py:412]
- `get_country` (function) — [saleor/checkout/models.py:422]
- `CheckoutLine` (class) — [saleor/checkout/models.py:434]
- `Meta` (class) — [saleor/checkout/models.py:503]
- `is_shipping_required` (function) — [saleor/checkout/models.py:529]
- `CheckoutMetadata` (class) — [saleor/checkout/models.py:536]

**`saleor/checkout/payment_utils.py`**

- `update_checkout_payment_statuses` (function) — [saleor/checkout/payment_utils.py:82]
- `update_refundable_for_checkout` (function) — [saleor/checkout/payment_utils.py:122]
- `apply_loyalty_discount` (function) — [saleor/checkout/payment_utils.py:140]

**`saleor/checkout/problems.py`**

- `CheckoutLineProblemInsufficientStock` (class) — [saleor/checkout/problems.py:14]
- `CheckoutLineProblemVariantNotAvailable` (class) — [saleor/checkout/problems.py:21]
- `CheckoutProblemDeliveryMethodStale` (class) — [saleor/checkout/problems.py:26]
- `CheckoutProblemDeliveryMethodInvalid` (class) — [saleor/checkout/problems.py:31]
- `get_insufficient_stock_lines` (function) — [saleor/checkout/problems.py:53]
- `line_is_not_available` (function) — [saleor/checkout/problems.py:90]
- `get_not_available_lines` (function) — [saleor/checkout/problems.py:123]
- `get_checkout_lines_problems` (function) — [saleor/checkout/problems.py:142]
- `get_checkout_problems` (function) — [saleor/checkout/problems.py:194]

**`saleor/checkout/tasks.py`**

- `delete_expired_checkouts` (function) — [saleor/checkout/tasks.py:41]
- `trigger_automatic_checkout_completion_task` (function) — [saleor/checkout/tasks.py:140]
- `automatic_checkout_completion_task` (function) — [saleor/checkout/tasks.py:213]
- `update_checkouts_search_vector_task` (function) — [saleor/checkout/tasks.py:318]
- `update_checkouts_search_vector_task_batch_process` (function) — [saleor/checkout/tasks.py:351]

**`saleor/checkout/utils.py`**

- `invalidate_checkout` (function) — [saleor/checkout/utils.py:76]
- `recalculate_checkout_discounts` (function) — [saleor/checkout/utils.py:92]
- `invalidate_checkout_prices` (function) — [saleor/checkout/utils.py:106]
- `checkout_lines_bulk_update` (function) — [saleor/checkout/utils.py:125]
- `checkout_lines_bulk_delete` (function) — [saleor/checkout/utils.py:138]
- `delete_checkouts` (function) — [saleor/checkout/utils.py:148]
- `get_user_checkout` (function) — [saleor/checkout/utils.py:165]
- `calculate_checkout_quantity` (function) — [saleor/checkout/utils.py:175]
- `add_variants_to_checkout` (function) — [saleor/checkout/utils.py:179]
- `change_billing_address_in_checkout` (function) — [saleor/checkout/utils.py:385]
- `change_shipping_address_in_checkout` (function) — [saleor/checkout/utils.py:409]
- `get_prices_of_discounted_specific_product` (function) — [saleor/checkout/utils.py:464]
- `get_base_lines_prices` (function) — [saleor/checkout/utils.py:481]
- `get_voucher_discount_for_checkout` (function) — [saleor/checkout/utils.py:492]
- `get_voucher_for_checkout` (function) — [saleor/checkout/utils.py:541]
- `get_voucher_for_checkout_info` (function) — [saleor/checkout/utils.py:597]
- `check_voucher_for_checkout` (function) — [saleor/checkout/utils.py:610]
- `recalculate_checkout_discount` (function) — [saleor/checkout/utils.py:633]
- `add_promo_code_to_checkout` (function) — [saleor/checkout/utils.py:689]
- `add_voucher_code_to_checkout` (function) — [saleor/checkout/utils.py:728]
- `add_voucher_to_checkout` (function) — [saleor/checkout/utils.py:754]
- `remove_promo_code_from_checkout_or_error` (function) — [saleor/checkout/utils.py:806]
- `remove_voucher_code_from_checkout_or_error` (function) — [saleor/checkout/utils.py:826]
- `remove_voucher_from_checkout` (function) — [saleor/checkout/utils.py:846]
- `is_fully_paid` (function) — [saleor/checkout/utils.py:864]
- `cancel_active_payments` (function) — [saleor/checkout/utils.py:889]
- `activate_payments` (function) — [saleor/checkout/utils.py:896]
- `create_checkout_metadata` (function) — [saleor/checkout/utils.py:901]
- `get_or_create_checkout_metadata` (function) — [saleor/checkout/utils.py:921]
- `get_checkout_metadata` (function) — [saleor/checkout/utils.py:929]
- `calculate_checkout_weight` (function) — [saleor/checkout/utils.py:936]
- `get_checkout_line_weight` (function) — [saleor/checkout/utils.py:946]
- `log_address_if_validation_skipped_for_checkout` (function) — [saleor/checkout/utils.py:954]
- `get_address_for_checkout_taxes` (function) — [saleor/checkout/utils.py:966]
- `checkout_info_for_logs` (function) — [saleor/checkout/utils.py:973]
- `log_unknown_discount_reason` (function) — [saleor/checkout/utils.py:1050]

## How it works

The module's files, as provided to this run:

- `saleor/checkout/__init__.py` (69 lines)
- `saleor/checkout/actions.py` (224 lines)
- `saleor/checkout/complete_checkout.py` (2034 lines)
- `saleor/checkout/models.py` (539 lines)
- `saleor/checkout/base_calculations.py` (327 lines)
- `saleor/checkout/calculations.py` (906 lines)
- `saleor/checkout/checkout_cleaner.py` (210 lines)
- `saleor/checkout/delivery_context.py` (811 lines)
- `saleor/checkout/error_codes.py` (71 lines)
- `saleor/checkout/fetch.py` (387 lines)
- `saleor/checkout/lock_objects.py` (11 lines)
- `saleor/checkout/payment_utils.py` (148 lines)
- `saleor/checkout/problems.py` (229 lines)
- `saleor/checkout/tasks.py` (369 lines)
- `saleor/checkout/utils.py` (1068 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/graphql/product/types`, `saleor/plugins/openid_connect`, `saleor/graphql`
- Imported by: `saleor/checkout/tests`, `saleor/checkout/migrations`, `saleor/checkout/webhooks`, `saleor/graphql/checkout/mutations`

Internal dependencies named in the source:

- `..account.error_codes.AccountErrorCode`
- `..account.models.Address`
- `..account.models.User`
- `..account.utils.retrieve_user_by_email`
- `..account.utils.store_user_address`
- `..AddressType`
- `..app.models.App`
- `..base_calculations`
- `..calculations`
- `..celeryconf.app`
- `..channel.MarkAsPaidStrategy`
- `..channel.models.Channel`
- `..checkout.calculations`
- `..checkout.CheckoutAuthorizeStatus`
- `..checkout.error_codes.CheckoutErrorCode`
- `..CheckoutAuthorizeStatus`
- `..CheckoutChargeStatus`
- `..core.db.connection.allow_writer`
- `..core.db.fields.MoneyField`
- `..core.db.fields.TaxedMoneyField`
- `..core.exceptions.GiftCardNotApplicable`
- `..core.exceptions.InsufficientStock`
- `..core.models.ModelWithMetadata`
- `..core.postgres.FlatConcatSearchVector`
- `..core.prices.quantize_price`
- `..core.pricing.interface.LineInfo`
- `..core.taxes.TAX_ERROR_FIELD_LENGTH`
- `..core.taxes.TaxDataError`
- `..core.taxes.TaxError`
- `..core.taxes.zero_money`
- `..core.taxes.zero_taxed_money`
- `..core.tracing.traced_atomic_transaction`
- `..core.transactions.transaction_with_commit_on_errors`
- `..core.utils.get_domain`
- `..core.utils.json_serializer.CustomJsonEncoder`
- `..core.utils.translations.get_translation`
- `..core.utils.url.validate_storefront_url`
- `..core.weight.zero_weight`
- `..discount.DiscountType`
- `..discount.DiscountValueType`
- `..discount.interface.fetch_voucher_info`
- `..discount.models.CheckoutDiscount`
- `..discount.models.NotApplicable`
- `..discount.models.OrderLineDiscount`
- `..discount.models.Voucher`
- `..discount.models.VoucherChannelListing`
- `..discount.models.VoucherCode`
- `..discount.utils.promotion.delete_gift_line`
- `..discount.utils.promotion.get_sale_id`
- `..discount.utils.shared.discount_info_for_logs`
- `..discount.utils.voucher.attach_voucher_to_line_info`
- `..discount.utils.voucher.calculate_line_discount_amount_from_voucher`
- `..discount.utils.voucher.is_order_level_voucher`
- `..discount.VoucherType`
- `..giftcard.models.GiftCard`
- `..graphql.core.context.ChannelContext`
- `..models`
- `..order.actions.order_created`
- `..order.delivery_context`
- `..order.fetch.OrderInfo`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `88a16c6cac09` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
