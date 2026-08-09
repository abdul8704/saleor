## Purpose

`saleor/checkout/tests/webhooks` (`saleor/checkout/tests/webhooks`) groups 11 source file(s) exposing 57 top-level declaration(s).

## Public surface

**`saleor/checkout/tests/webhooks/static_payloads/test_calculate_taxes.py`**

- `mocked_fetch_checkout` (function) — [saleor/checkout/tests/webhooks/static_payloads/test_calculate_taxes.py:31]
- `mocked_fetch_side_effect` (function) — [saleor/checkout/tests/webhooks/static_payloads/test_calculate_taxes.py:32]
- `test_generate_checkout_payload_for_tax_calculation_entire_order_voucher` (function) — [saleor/checkout/tests/webhooks/static_payloads/test_calculate_taxes.py:48]
- `test_generate_checkout_payload_for_tax_calculation_specific_product_voucher` (function) — [saleor/checkout/tests/webhooks/static_payloads/test_calculate_taxes.py:144]
- `test_generate_checkout_payload_for_tax_calculation_shipping_voucher` (function) — [saleor/checkout/tests/webhooks/static_payloads/test_calculate_taxes.py:241]
- `test_generate_checkout_payload_for_tax_calculation_order_discount` (function) — [saleor/checkout/tests/webhooks/static_payloads/test_calculate_taxes.py:341]
- `test_generate_checkout_payload_for_tax_calculation_gift_promotion` (function) — [saleor/checkout/tests/webhooks/static_payloads/test_calculate_taxes.py:449]
- `test_generate_checkout_payload_for_tax_calculation_no_discount` (function) — [saleor/checkout/tests/webhooks/static_payloads/test_calculate_taxes.py:538]
- `test_serialize_checkout_lines_for_tax_calculation` (function) — [saleor/checkout/tests/webhooks/static_payloads/test_calculate_taxes.py:636]
- `test_serialize_checkout_lines_for_tax_calculation_with_promotion` (function) — [saleor/checkout/tests/webhooks/static_payloads/test_calculate_taxes.py:690]
- `test_serialize_checkout_lines_for_tax_calculation_with_order_discount` (function) — [saleor/checkout/tests/webhooks/static_payloads/test_calculate_taxes.py:759]
- `test_serialize_checkout_lines_for_tax_calculation_with_gift_promotion` (function) — [saleor/checkout/tests/webhooks/static_payloads/test_calculate_taxes.py:806]

**`saleor/checkout/tests/webhooks/static_payloads/test_exclude_shipping.py`**

- `test_generate_excluded_shipping_methods_for_checkout` (function) — [saleor/checkout/tests/webhooks/static_payloads/test_exclude_shipping.py:14]
- `test_generate_excluded_shipping_methods_for_checkout_payload` (function) — [saleor/checkout/tests/webhooks/static_payloads/test_exclude_shipping.py:45]

**`saleor/checkout/tests/webhooks/subscriptions/test_calculate_taxes.py`**

- `subscription_order_calculate_taxes` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_calculate_taxes.py:105]
- `test_checkout_calculate_taxes` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_calculate_taxes.py:113]
- `test_checkout_calculate_taxes_with_free_shipping_voucher` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_calculate_taxes.py:192]
- `test_checkout_calculate_taxes_with_entire_order_voucher` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_calculate_taxes.py:243]
- `test_checkout_calculate_taxes_with_entire_order_voucher_once_per_order` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_calculate_taxes.py:316]
- `test_checkout_calculate_taxes_with_shipping_voucher` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_calculate_taxes.py:383]
- `test_checkout_calculate_taxes_with_order_promotion` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_calculate_taxes.py:455]
- `test_checkout_calculate_taxes_empty_checkout` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_calculate_taxes.py:530]

**`saleor/checkout/tests/webhooks/subscriptions/test_exclude_shipping.py`**

- `subscription_checkout_filter_shipping_methods_webhook` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_exclude_shipping.py:77]
- `subscription_checkout_filter_shipping_method_webhook_with_shipping_methods` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_exclude_shipping.py:85]
- `subscription_checkout_filter_shipping_method_webhook_with_available_ship_methods` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_exclude_shipping.py:95]
- `subscription_checkout_filter_shipping_method_webhook_with_payment_gateways` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_exclude_shipping.py:105]
- `test_checkout_filter_shipping_methods` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_exclude_shipping.py:114]
- `test_checkout_filter_shipping_methods_no_methods_in_channel` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_exclude_shipping.py:157]
- `test_checkout_filter_shipping_methods_with_circular_call_for_shipping_methods` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_exclude_shipping.py:181]
- `test_checkout_filter_shipping_methods_with_available_shipping_methods_field` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_exclude_shipping.py:207]
- `test_checkout_filter_shipping_methods_with_circular_call_for_available_gateways` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_exclude_shipping.py:233]

**`saleor/checkout/tests/webhooks/subscriptions/test_list_shipping_methods.py`**

- `subscription_shipping_list_methods_for_checkout_webhook` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_list_shipping_methods.py:35]
- `subscription_checkout_shipping_filter_and_list_missing_one_in_definition` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_list_shipping_methods.py:43]
- `test_shipping_list_methods_for_checkout` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_list_shipping_methods.py:56]
- `test_checkout_list_methods_mismatch_in_subscription_query_definition` (function) — [saleor/checkout/tests/webhooks/subscriptions/test_list_shipping_methods.py:99]

**`saleor/checkout/tests/webhooks/test_calculate_taxes.py`**

- `test_get_taxes_no_permission` (function) — [saleor/checkout/tests/webhooks/test_calculate_taxes.py:20]
- `test_get_taxes_with_sync_subscription` (function) — [saleor/checkout/tests/webhooks/test_calculate_taxes.py:46]
- `test_get_taxes_with_app_identifier_app_missing` (function) — [saleor/checkout/tests/webhooks/test_calculate_taxes.py:95]
- `test_get_taxes_with_app_identifier_webhook_is_missing` (function) — [saleor/checkout/tests/webhooks/test_calculate_taxes.py:106]
- `test_get_taxes_with_app_identifier_invalid_response` (function) — [saleor/checkout/tests/webhooks/test_calculate_taxes.py:122]
- `test_get_taxes_with_app_identifier` (function) — [saleor/checkout/tests/webhooks/test_calculate_taxes.py:153]
- `test_get_taxes_with_app_identifier_empty_response` (function) — [saleor/checkout/tests/webhooks/test_calculate_taxes.py:207]
- `tax_checkout_webhooks` (function) — [saleor/checkout/tests/webhooks/test_calculate_taxes.py:234]

**`saleor/checkout/tests/webhooks/test_exclude_shipping.py`**

- `available_shipping_methods` (function) — [saleor/checkout/tests/webhooks/test_exclude_shipping.py:41]
- `test_checkout_deliveries` (function) — [saleor/checkout/tests/webhooks/test_exclude_shipping.py:67]
- `test_checkout_available_shipping_methods` (function) — [saleor/checkout/tests/webhooks/test_exclude_shipping.py:111]
- `test_checkout_deliveries_webhook_called_once` (function) — [saleor/checkout/tests/webhooks/test_exclude_shipping.py:146]
- `test_excluded_shipping_methods_for_checkout_webhook_with_subscription` (function) — [saleor/checkout/tests/webhooks/test_exclude_shipping.py:176]
- `test_multiple_app_with_excluded_shipping_methods_for_checkout` (function) — [saleor/checkout/tests/webhooks/test_exclude_shipping.py:233]
- `test_multiple_webhooks_on_the_same_app_with_excluded_shipping_methods_for_checkout` (function) — [saleor/checkout/tests/webhooks/test_exclude_shipping.py:323]
- `test_excluded_shipping_methods_for_checkout` (function) — [saleor/checkout/tests/webhooks/test_exclude_shipping.py:417]

**`saleor/checkout/tests/webhooks/test_list_shipping_methods.py`**

- `test_list_shipping_methods_for_checkout_webhook_response_none` (function) — [saleor/checkout/tests/webhooks/test_list_shipping_methods.py:11]
- `test_parse_list_shipping_methods_response_response_incorrect_format` (function) — [saleor/checkout/tests/webhooks/test_list_shipping_methods.py:33]
- `test_parse_list_shipping_methods_with_metadata` (function) — [saleor/checkout/tests/webhooks/test_list_shipping_methods.py:51]
- `test_parse_list_shipping_methods_with_metadata_in_incorrect_format` (function) — [saleor/checkout/tests/webhooks/test_list_shipping_methods.py:76]
- `test_parse_list_shipping_methods_metadata_absent_in_response` (function) — [saleor/checkout/tests/webhooks/test_list_shipping_methods.py:100]
- `test_parse_list_shipping_methods_metadata_is_none` (function) — [saleor/checkout/tests/webhooks/test_list_shipping_methods.py:123]

## How it works

The module's files, as provided to this run:

- `saleor/checkout/tests/webhooks/__init__.py` (1 lines)
- `saleor/checkout/tests/webhooks/static_payloads/__init__.py` (1 lines)
- `saleor/checkout/tests/webhooks/static_payloads/test_calculate_taxes.py` (876 lines)
- `saleor/checkout/tests/webhooks/static_payloads/test_exclude_shipping.py` (72 lines)
- `saleor/checkout/tests/webhooks/subscriptions/__init__.py` (1 lines)
- `saleor/checkout/tests/webhooks/subscriptions/test_calculate_taxes.py` (575 lines)
- `saleor/checkout/tests/webhooks/subscriptions/test_exclude_shipping.py` (256 lines)
- `saleor/checkout/tests/webhooks/subscriptions/test_list_shipping_methods.py` (113 lines)
- `saleor/checkout/tests/webhooks/test_calculate_taxes.py` (257 lines)
- `saleor/checkout/tests/webhooks/test_exclude_shipping.py` (448 lines)
- `saleor/checkout/tests/webhooks/test_list_shipping_methods.py` (144 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/checkout/webhooks`, `saleor/graphql`, `saleor/webhook/transport/synchronous`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....base_calculations`
- `.....core.prices.quantize_price`
- `.....discount.DiscountType`
- `.....discount.RewardValueType`
- `.....discount.models.CheckoutDiscount`
- `.....discount.models.CheckoutLineDiscount`
- `.....discount.models.PromotionRule`
- `.....graphql.core.utils.to_global_id_or_none`
- `.....plugins.manager.get_plugins_manager`
- `.....product.models.Product`
- `.....product.models.ProductVariantChannelListing`
- `.....product.utils.variant_prices.update_discounted_prices_for_promotion`
- `.....product.utils.variants.fetch_variants_for_promotion_rules`
- `.....shipping.interface.ShippingMethodData`
- `.....shipping.models.ShippingMethod`
- `.....shipping.utils.convert_to_shipping_method_data`
- `.....tax.TaxableObjectDiscountType`
- `.....webhook.event_types.WebhookEventSyncType`
- `.....webhook.models.Webhook`
- `.....webhook.serializers.serialize_variant_full_name`
- `....checkout.fetch.fetch_checkout_info`
- `....checkout.fetch.fetch_checkout_lines`
- `....checkout.webhooks.calculate_taxes`
- `....core.EventDeliveryStatus`
- `....core.models.EventDelivery`
- `....core.taxes.TaxDataError`
- `....fetch.fetch_checkout_info`
- `....fetch.fetch_checkout_lines`
- `....graphql.core.utils.to_global_id_or_none`
- `....graphql.tests.utils.get_graphql_content`
- `....models.CheckoutLine`
- `....plugins.manager.get_plugins_manager`
- `....shipping.interface.ExcludedShippingMethod`
- `....shipping.interface.ShippingMethodData`
- `....shipping.models.ShippingMethod`
- `....tax.webhooks.parser.parse_tax_data`
- `....utils.add_voucher_to_checkout`
- `....webhook.event_types.WebhookEventSyncType`
- `....webhook.models.Webhook`
- `....webhook.models.WebhookEvent`
- `....webhook.response_schemas.utils.annotations.logger`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c5d7e7f049aa` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
