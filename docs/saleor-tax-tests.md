## Purpose

`saleor/tax/tests` (`saleor/tax/tests`) groups 11 source file(s) exposing 84 top-level declaration(s).

## Public surface

**`saleor/tax/tests/fixtures/tax_class.py`**

- `default_tax_class` (function) — [saleor/tax/tests/fixtures/tax_class.py:14]
- `tax_classes` (function) — [saleor/tax/tests/fixtures/tax_class.py:38]
- `tax_class_zero_rates` (function) — [saleor/tax/tests/fixtures/tax_class.py:59]

**`saleor/tax/tests/fixtures/utils.py`**

- `create_channel_tax_configuration` (function) — [saleor/tax/tests/fixtures/utils.py:5]

**`saleor/tax/tests/test_calculations.py`**

- `test_calculate_flat_tax_rate` (function) — [saleor/tax/tests/test_calculations.py:17]

**`saleor/tax/tests/test_checkout_calculations.py`**

- `test_calculate_checkout_total_with_gift_cards` (function) — [saleor/tax/tests/test_checkout_calculations.py:56]
- `test_calculate_checkout_total` (function) — [saleor/tax/tests/test_checkout_calculations.py:111]
- `test_calculate_checkout_total_with_multiple_tax_rates` (function) — [saleor/tax/tests/test_checkout_calculations.py:172]
- `test_calculate_checkout_shipping_with_not_weighted_taxes` (function) — [saleor/tax/tests/test_checkout_calculations.py:229]
- `test_calculate_checkout_shipping_with_weighted_taxes` (function) — [saleor/tax/tests/test_checkout_calculations.py:288]
- `test_calculate_checkout_total_with_sale` (function) — [saleor/tax/tests/test_checkout_calculations.py:352]
- `test_calculate_checkout_total_no_tax_rates` (function) — [saleor/tax/tests/test_checkout_calculations.py:397]
- `test_calculate_checkout_total_default_tax_rate_for_country` (function) — [saleor/tax/tests/test_checkout_calculations.py:429]
- `test_calculate_checkout_total_with_shipping_voucher` (function) — [saleor/tax/tests/test_checkout_calculations.py:469]
- `test_calculate_checkout_total_with_shipping_voucher_and_sale` (function) — [saleor/tax/tests/test_checkout_calculations.py:519]
- `test_calculate_checkout_subtotal` (function) — [saleor/tax/tests/test_checkout_calculations.py:572]
- `test_calculate_checkout_subtotal_with_promotion_prices_entered_with_tax` (function) — [saleor/tax/tests/test_checkout_calculations.py:613]
- `test_calculate_checkout_subtotal_with_promotion_prices_not_entered_with_tax` (function) — [saleor/tax/tests/test_checkout_calculations.py:658]
- `test_calculate_checkout_subtotal_with_order_promotion` (function) — [saleor/tax/tests/test_checkout_calculations.py:703]
- `test_calculate_checkout_subtotal_with_gift_promotion` (function) — [saleor/tax/tests/test_checkout_calculations.py:745]
- `test_calculate_checkout_line_total` (function) — [saleor/tax/tests/test_checkout_calculations.py:787]
- `test_calculate_checkout_line_total_voucher_on_entire_order` (function) — [saleor/tax/tests/test_checkout_calculations.py:821]
- `test_calculate_checkout_line_total_with_voucher_one_line` (function) — [saleor/tax/tests/test_checkout_calculations.py:870]
- `test_calculate_checkout_line_total_with_voucher_multiple_lines` (function) — [saleor/tax/tests/test_checkout_calculations.py:922]
- `test_calculate_checkout_line_total_with_voucher_multiple_lines_last_line` (function) — [saleor/tax/tests/test_checkout_calculations.py:991]
- `test_calculate_checkout_line_total_with_voucher_for_multiple_lines` (function) — [saleor/tax/tests/test_checkout_calculations.py:1067]
- `test_calculate_checkout_line_total_with_shipping_voucher` (function) — [saleor/tax/tests/test_checkout_calculations.py:1166]
- `test_calculate_checkout_line_total_discount_from_order_promotion` (function) — [saleor/tax/tests/test_checkout_calculations.py:1219]
- `test_calculate_checkout_line_total_discount_for_gift_line` (function) — [saleor/tax/tests/test_checkout_calculations.py:1265]
- `test_calculate_checkout_shipping` (function) — [saleor/tax/tests/test_checkout_calculations.py:1302]
- `test_calculate_checkout_shipping_no_shipping_price` (function) — [saleor/tax/tests/test_checkout_calculations.py:1335]
- `test_calculate_checkout_shipping_voucher_on_shipping` (function) — [saleor/tax/tests/test_checkout_calculations.py:1366]
- `test_calculate_checkout_shipping_free_shipping_voucher` (function) — [saleor/tax/tests/test_checkout_calculations.py:1411]
- `test_calculate_checkout_shipping_free_entire_order_voucher` (function) — [saleor/tax/tests/test_checkout_calculations.py:1449]

**`saleor/tax/tests/test_order_calculations.py`**

- `test_calculations_calculate_order_total` (function) — [saleor/tax/tests/test_order_calculations.py:37]
- `test_calculate_order_total_with_multiple_tax_rates` (function) — [saleor/tax/tests/test_order_calculations.py:69]
- `test_calculate_order_shipping_with_not_weighted_taxes` (function) — [saleor/tax/tests/test_order_calculations.py:115]
- `test_calculate_order_shipping_with_weighted_taxes` (function) — [saleor/tax/tests/test_order_calculations.py:165]
- `test_calculations_calculate_order_undiscounted_total` (function) — [saleor/tax/tests/test_order_calculations.py:214]
- `test_calculations_calculate_order_total_use_product_type_tax_class` (function) — [saleor/tax/tests/test_order_calculations.py:251]
- `test_calculations_calculate_order_total_no_rates` (function) — [saleor/tax/tests/test_order_calculations.py:275]
- `test_calculations_calculate_order_total_default_country_rate` (function) — [saleor/tax/tests/test_order_calculations.py:293]
- `test_calculations_calculate_order_total_voucher` (function) — [saleor/tax/tests/test_order_calculations.py:315]
- `test_calculations_calculate_order_total_with_manual_discount` (function) — [saleor/tax/tests/test_order_calculations.py:344]
- `test_calculations_calculate_order_total_with_discount_for_order_total` (function) — [saleor/tax/tests/test_order_calculations.py:373]
- `test_calculations_calculate_order_total_with_discount_for_subtotal_and_shipping` (function) — [saleor/tax/tests/test_order_calculations.py:399]
- `test_calculations_calculate_order_total_with_discount_for_more_than_order_total` (function) — [saleor/tax/tests/test_order_calculations.py:428]
- `test_calculations_calculate_order_total_with_manual_discount_and_voucher` (function) — [saleor/tax/tests/test_order_calculations.py:454]
- `test_calculate_order_shipping` (function) — [saleor/tax/tests/test_order_calculations.py:493]
- `test_calculate_order_shipping_for_order_without_shipping` (function) — [saleor/tax/tests/test_order_calculations.py:521]
- `test_calculate_order_shipping_voucher_on_shipping` (function) — [saleor/tax/tests/test_order_calculations.py:539]
- `test_calculate_order_shipping_free_shipping_voucher` (function) — [saleor/tax/tests/test_order_calculations.py:587]
- `test_update_taxes_for_order_lines` (function) — [saleor/tax/tests/test_order_calculations.py:628]
- `test_update_taxes_for_order_lines_voucher_on_entire_order` (function) — [saleor/tax/tests/test_order_calculations.py:659]
- `test_update_taxes_for_order_lines_voucher_on_shipping` (function) — [saleor/tax/tests/test_order_calculations.py:723]
- `test_update_taxes_for_order_line_on_promotion` (function) — [saleor/tax/tests/test_order_calculations.py:770]
- `test_use_original_tax_rate_when_tax_class_is_removed_from_order_line` (function) — [saleor/tax/tests/test_order_calculations.py:819]
- `test_use_default_country_rate_when_no_tax_class_was_set_before` (function) — [saleor/tax/tests/test_order_calculations.py:848]

**`saleor/tax/tests/test_utils.py`**

- `test_get_display_gross_prices` (function) — [saleor/tax/tests/test_utils.py:20]
- `test_get_charge_taxes` (function) — [saleor/tax/tests/test_utils.py:40]
- `test_get_tax_app_id` (function) — [saleor/tax/tests/test_utils.py:57]
- `test_get_tax_app_id_country` (function) — [saleor/tax/tests/test_utils.py:71]
- `test_get_tax_country_use_shipping_address` (function) — [saleor/tax/tests/test_utils.py:84]
- `test_get_tax_country_use_billing_address` (function) — [saleor/tax/tests/test_utils.py:98]
- `test_get_tax_country_fallbacks_to_channel_country` (function) — [saleor/tax/tests/test_utils.py:113]
- `test_get_tax_country_use_address_data` (function) — [saleor/tax/tests/test_utils.py:125]
- `test_get_tax_country_fallbacks_to_channel_country_address_data_with_empty_country` (function) — [saleor/tax/tests/test_utils.py:139]
- `test_get_shipping_tax_rate_for_checkout_weighted_tax` (function) — [saleor/tax/tests/test_utils.py:153]
- `test_get_shipping_tax_rate_for_checkout_weighted_tax_with_multiple_tax_rates` (function) — [saleor/tax/tests/test_utils.py:192]
- `test_get_shipping_tax_rate_for_checkout_when_weighted_tax_is_disabled` (function) — [saleor/tax/tests/test_utils.py:265]
- `test_get_shipping_tax_rate_for_order_weighted_tax` (function) — [saleor/tax/tests/test_utils.py:305]
- `test_get_shipping_tax_rate_for_order_weighted_tax_with_multiple_tax_rates` (function) — [saleor/tax/tests/test_utils.py:343]
- `test_get_shipping_tax_rate_for_order_when_weighted_tax_is_disabled` (function) — [saleor/tax/tests/test_utils.py:404]

**`saleor/tax/tests/webhooks/test_parser.py`**

- `test_parse_tax_data_success` (function) — [saleor/tax/tests/webhooks/test_parser.py:8]
- `test_parse_tax_data_keyerror` (function) — [saleor/tax/tests/webhooks/test_parser.py:21]
- `test_parse_tax_data_decimalexception` (function) — [saleor/tax/tests/webhooks/test_parser.py:34]
- `test_parse_tax_data_malformed` (function) — [saleor/tax/tests/webhooks/test_parser.py:63]

**`saleor/tax/tests/webhooks/test_shared.py`**

- `tax_webhooks` (function) — [saleor/tax/tests/webhooks/test_shared.py:41]
- `test_get_taxes_from_all_webhooks` (function) — [saleor/tax/tests/webhooks/test_shared.py:66]
- `test_get_taxes_from_all_webhooks_multiple_webhooks` (function) — [saleor/tax/tests/webhooks/test_shared.py:129]
- `test_get_taxes_from_all_webhooks_multiple_invalid_webhooks` (function) — [saleor/tax/tests/webhooks/test_shared.py:191]
- `test_get_taxes_for_app_identifier` (function) — [saleor/tax/tests/webhooks/test_shared.py:253]
- `test_get_taxes_for_app_identifier_multiple_webhooks` (function) — [saleor/tax/tests/webhooks/test_shared.py:316]
- `test_get_taxes_for_app_identifier_invalid_response` (function) — [saleor/tax/tests/webhooks/test_shared.py:378]

## How it works

The module's files, as provided to this run:

- `saleor/tax/tests/__init__.py` (1 lines)
- `saleor/tax/tests/fixtures/__init__.py` (1 lines)
- `saleor/tax/tests/fixtures/tax_class.py` (74 lines)
- `saleor/tax/tests/fixtures/utils.py` (20 lines)
- `saleor/tax/tests/test_calculations.py` (22 lines)
- `saleor/tax/tests/test_checkout_calculations.py` (1486 lines)
- `saleor/tax/tests/test_order_calculations.py` (905 lines)
- `saleor/tax/tests/test_utils.py` (439 lines)
- `saleor/tax/tests/webhooks/__init__.py` (1 lines)
- `saleor/tax/tests/webhooks/test_parser.py` (65 lines)
- `saleor/tax/tests/webhooks/test_shared.py` (432 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/tax`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....core.EventDeliveryStatus`
- `....core.models.EventDelivery`
- `....core.taxes.TaxData`
- `....core.taxes.TaxDataError`
- `....tax.TaxCalculationStrategy`
- `....tax.models.TaxConfiguration`
- `....webhook.event_types.WebhookEventSyncType`
- `....webhook.models.Webhook`
- `....webhook.models.WebhookEvent`
- `...TaxCalculationStrategy`
- `...checkout.calculations`
- `...checkout.fetch.fetch_checkout_info`
- `...checkout.fetch.fetch_checkout_lines`
- `...checkout.tests.utils.add_variant_to_checkout`
- `...core.prices.Money`
- `...core.prices.TaxedMoney`
- `...core.prices.quantize_price`
- `...core.taxes.zero_money`
- `...core.taxes.zero_taxed_money`
- `...core.utils.country.get_active_country`
- `...discount.DiscountType`
- `...discount.DiscountValueType`
- `...graphql.tax.enums.TaxCalculationStrategy`
- `...models.TaxClass`
- `...models.TaxClassCountryRate`
- `...order.OrderStatus`
- `...order.base_calculations.calculate_prices`
- `...order.calculations.fetch_order_prices_if_expired`
- `...order.models.OrderLine`
- `...order.utils.get_order_country`
- `...payment.model_helpers.get_subtotal`
- `...plugins.manager.get_plugins_manager`
- `...product.models.ProductVariantChannelListing`
- `...tax.models.TaxClassCountryRate`
- `...webhooks.parser.parse_tax_data`
- `..calculations.calculate_flat_rate_tax`
- `.tax_class.*  # noqa: F403`
- `saleor.core.taxes.TaxDataError`
- `saleor.tax.models.TaxClass`
- `saleor.tax.models.TaxClassCountryRate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `0c46a6e90fe7` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
