## Purpose

`saleor/order/tests/webhooks` (`saleor/order/tests/webhooks`) groups 9 source file(s) exposing 44 top-level declaration(s).

## Public surface

**`saleor/order/tests/webhooks/static_payloads/test_order_calculate_taxes.py`**

- `order_for_payload` (function) — [saleor/order/tests/webhooks/static_payloads/test_order_calculate_taxes.py:19]
- `test_generate_order_payload_for_tax_calculation` (function) — [saleor/order/tests/webhooks/static_payloads/test_order_calculate_taxes.py:52]
- `test_generate_order_payload_for_tax_calculation_entire_order_voucher` (function) — [saleor/order/tests/webhooks/static_payloads/test_order_calculate_taxes.py:154]
- `test_generate_order_payload_for_tax_calculation_line_level_voucher_excluded` (function) — [saleor/order/tests/webhooks/static_payloads/test_order_calculate_taxes.py:232]
- `test_order_lines_for_tax_calculation_with_removed_variant` (function) — [saleor/order/tests/webhooks/static_payloads/test_order_calculate_taxes.py:263]
- `test_order_lines_for_tax_calculation_have_all_required_fields` (function) — [saleor/order/tests/webhooks/static_payloads/test_order_calculate_taxes.py:313]

**`saleor/order/tests/webhooks/subscriptions/test_exclude_shipping.py`**

- `subscription_with_filter_shipping_methods_webhook` (function) — [saleor/order/tests/webhooks/subscriptions/test_exclude_shipping.py:46]
- `subscription_with_shipping_methods` (function) — [saleor/order/tests/webhooks/subscriptions/test_exclude_shipping.py:54]
- `test_order_filter_shipping_methods` (function) — [saleor/order/tests/webhooks/subscriptions/test_exclude_shipping.py:63]
- `test_order_filter_shipping_methods_no_methods_in_channel` (function) — [saleor/order/tests/webhooks/subscriptions/test_exclude_shipping.py:107]
- `test_order_filter_shipping_methods_with_circular_call_for_shipping_methods` (function) — [saleor/order/tests/webhooks/subscriptions/test_exclude_shipping.py:131]

**`saleor/order/tests/webhooks/subscriptions/test_order_calculate_taxes.py`**

- `subscription_order_calculate_taxes` (function) — [saleor/order/tests/webhooks/subscriptions/test_order_calculate_taxes.py:107]
- `test_order_calculate_taxes` (function) — [saleor/order/tests/webhooks/subscriptions/test_order_calculate_taxes.py:115]
- `test_draft_order_calculate_taxes_line_discount` (function) — [saleor/order/tests/webhooks/subscriptions/test_order_calculate_taxes.py:197]
- `test_draft_order_calculate_taxes_entire_order_voucher` (function) — [saleor/order/tests/webhooks/subscriptions/test_order_calculate_taxes.py:295]
- `test_draft_order_calculate_taxes_apply_once_per_order_voucher` (function) — [saleor/order/tests/webhooks/subscriptions/test_order_calculate_taxes.py:392]
- `test_order_calculate_taxes_specific_product_voucher` (function) — [saleor/order/tests/webhooks/subscriptions/test_order_calculate_taxes.py:485]
- `test_draft_order_calculate_taxes_free_shipping_voucher` (function) — [saleor/order/tests/webhooks/subscriptions/test_order_calculate_taxes.py:589]
- `test_order_calculate_taxes_with_manual_discount` (function) — [saleor/order/tests/webhooks/subscriptions/test_order_calculate_taxes.py:635]
- `test_order_calculate_taxes_empty_order` (function) — [saleor/order/tests/webhooks/subscriptions/test_order_calculate_taxes.py:743]
- `test_order_calculate_taxes_order_promotion` (function) — [saleor/order/tests/webhooks/subscriptions/test_order_calculate_taxes.py:790]
- `test_order_calculate_taxes_order_voucher_and_manual_discount` (function) — [saleor/order/tests/webhooks/subscriptions/test_order_calculate_taxes.py:889]
- `test_order_calculate_taxes_order_promotion_and_manual_discount` (function) — [saleor/order/tests/webhooks/subscriptions/test_order_calculate_taxes.py:1004]
- `test_order_calculate_taxes_free_shipping_voucher_and_manual_discount_fixed` (function) — [saleor/order/tests/webhooks/subscriptions/test_order_calculate_taxes.py:1123]
- `test_order_calculate_taxes_free_shipping_voucher_and_manual_discount_percentage` (function) — [saleor/order/tests/webhooks/subscriptions/test_order_calculate_taxes.py:1233]

**`saleor/order/tests/webhooks/test_exclude_shipping_cache.py`**

- `available_shipping_methods` (function) — [saleor/order/tests/webhooks/test_exclude_shipping_cache.py:22]
- `test_excluded_shipping_methods_for_order_use_cache` (function) — [saleor/order/tests/webhooks/test_exclude_shipping_cache.py:51]
- `test_excluded_shipping_methods_for_order_stores_in_cache_when_empty` (function) — [saleor/order/tests/webhooks/test_exclude_shipping_cache.py:97]
- `test_excluded_shipping_methods_for_order_stores_in_cache_when_payload_is_different` (function) — [saleor/order/tests/webhooks/test_exclude_shipping_cache.py:181]

**`saleor/order/tests/webhooks/test_exclude_shipping.py`**

- `available_shipping_methods` (function) — [saleor/order/tests/webhooks/test_exclude_shipping.py:39]
- `test_excluded_shipping_methods_for_order_dont_run_webhook_on_missing_shipping_methods` (function) — [saleor/order/tests/webhooks/test_exclude_shipping.py:57]
- `test_excluded_shipping_methods_for_order` (function) — [saleor/order/tests/webhooks/test_exclude_shipping.py:82]
- `test_multiple_app_with_excluded_shipping_methods_for_order` (function) — [saleor/order/tests/webhooks/test_exclude_shipping.py:179]
- `test_multiple_webhooks_on_the_same_app_with_excluded_shipping_methods_for_order` (function) — [saleor/order/tests/webhooks/test_exclude_shipping.py:338]
- `test_generate_excluded_shipping_methods_for_order_payload` (function) — [saleor/order/tests/webhooks/test_exclude_shipping.py:484]
- `test_generate_excluded_shipping_methods_for_order` (function) — [saleor/order/tests/webhooks/test_exclude_shipping.py:509]

**`saleor/order/tests/webhooks/test_order_calculate_taxes.py`**

- `test_get_taxes_for_order` (function) — [saleor/order/tests/webhooks/test_order_calculate_taxes.py:23]
- `test_get_taxes_for_order_with_sync_subscription` (function) — [saleor/order/tests/webhooks/test_order_calculate_taxes.py:66]
- `test_get_taxes_for_order_with_app_identifier_app_missing` (function) — [saleor/order/tests/webhooks/test_order_calculate_taxes.py:107]
- `test_get_taxes_for_order_with_app_identifier_webhook_is_missing` (function) — [saleor/order/tests/webhooks/test_order_calculate_taxes.py:116]
- `test_get_taxes_for_order_with_app_identifier_invalid_response` (function) — [saleor/order/tests/webhooks/test_order_calculate_taxes.py:125]
- `test_get_taxes_for_order_with_app_identifier_empty_response` (function) — [saleor/order/tests/webhooks/test_order_calculate_taxes.py:146]
- `test_get_taxes_for_order_with_app_identifier` (function) — [saleor/order/tests/webhooks/test_order_calculate_taxes.py:171]
- `test_get_taxes_for_order_sets_issuing_principal` (function) — [saleor/order/tests/webhooks/test_order_calculate_taxes.py:215]

## How it works

The module's files, as provided to this run:

- `saleor/order/tests/webhooks/__init__.py` (1 lines)
- `saleor/order/tests/webhooks/static_payloads/__init__.py` (1 lines)
- `saleor/order/tests/webhooks/static_payloads/test_order_calculate_taxes.py` (365 lines)
- `saleor/order/tests/webhooks/subscriptions/__init__.py` (1 lines)
- `saleor/order/tests/webhooks/subscriptions/test_exclude_shipping.py` (155 lines)
- `saleor/order/tests/webhooks/subscriptions/test_order_calculate_taxes.py` (1345 lines)
- `saleor/order/tests/webhooks/test_exclude_shipping_cache.py` (254 lines)
- `saleor/order/tests/webhooks/test_exclude_shipping.py` (536 lines)
- `saleor/order/tests/webhooks/test_order_calculate_taxes.py` (248 lines)

## Interactions

- Imports from: `saleor/order/webhooks`, `saleor/core`, `saleor/graphql`, `saleor/webhook/transport/synchronous`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....OrderStatus`
- `.....core.prices.quantize_price`
- `.....discount.DiscountType`
- `.....discount.DiscountValueType`
- `.....discount.VoucherType`
- `.....graphql.core.utils.to_global_id_or_none`
- `.....plugins.manager.get_plugins_manager`
- `.....shipping.models.ShippingMethodChannelListing`
- `.....tax.TaxableObjectDiscountType`
- `.....webhook.event_types.WebhookEventSyncType`
- `.....webhook.models.Webhook`
- `.....webhook.serializers.serialize_variant_full_name`
- `....calculations.fetch_order_prices_if_expired`
- `....core.EventDeliveryStatus`
- `....core.models.EventDelivery`
- `....core.prices.quantize_price`
- `....core.taxes.TaxDataError`
- `....delivery_context.get_all_shipping_methods_for_order`
- `....models.Order`
- `....shipping.interface.ShippingMethodData`
- `....shipping.webhooks.shared.CACHE_EXCLUDED_SHIPPING_TIME`
- `....tax.webhooks.parser.parse_tax_data`
- `....webhook.event_types.WebhookEventSyncType`
- `....webhook.models.Webhook`
- `....webhook.transport.utils.generate_cache_key_for_webhook`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `412ea798db72` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
