## Purpose

`saleor/plugins/avatax` (`saleor/plugins/avatax`) groups 99 source file(s) exposing 53 top-level declaration(s).

## Public surface

**`saleor/plugins/avatax/__init__.py`**

- `AvataxConfiguration` (class) — [saleor/plugins/avatax/__init__.py:61]
- `TransactionType` (class) — [saleor/plugins/avatax/__init__.py:75]
- `CustomerErrors` (class) — [saleor/plugins/avatax/__init__.py:80]
- `get_error_msg` (function) — [saleor/plugins/avatax/__init__.py:85]
- `get_api_url` (function) — [saleor/plugins/avatax/__init__.py:92]
- `api_post_request` (function) — [saleor/plugins/avatax/__init__.py:99]
- `api_get_request` (function) — [saleor/plugins/avatax/__init__.py:129]
- `taxes_need_new_fetch` (function) — [saleor/plugins/avatax/__init__.py:218]
- `append_line_to_data` (function) — [saleor/plugins/avatax/__init__.py:233]
- `append_shipping_to_data` (function) — [saleor/plugins/avatax/__init__.py:268]
- `generate_request_data_from_checkout_lines` (function) — [saleor/plugins/avatax/__init__.py:287]
- `get_order_lines_data` (function) — [saleor/plugins/avatax/__init__.py:375]
- `generate_request_data` (function) — [saleor/plugins/avatax/__init__.py:457]
- `generate_request_data_from_checkout` (function) — [saleor/plugins/avatax/__init__.py:505]
- `get_cached_response_or_fetch` (function) — [saleor/plugins/avatax/__init__.py:582]
- `iter_checkout_lines` (function) — [saleor/plugins/avatax/__init__.py:604]
- `iter_order_lines` (function) — [saleor/plugins/avatax/__init__.py:611]
- `convert_response_lines_list_to_dict` (function) — [saleor/plugins/avatax/__init__.py:620]
- `get_checkout_tax_data` (function) — [saleor/plugins/avatax/__init__.py:647]
- `get_order_request_data` (function) — [saleor/plugins/avatax/__init__.py:664]
- `get_order_tax_data` (function) — [saleor/plugins/avatax/__init__.py:694]
- `generate_tax_codes_dict` (function) — [saleor/plugins/avatax/__init__.py:726]
- `get_cached_tax_codes_or_fetch` (function) — [saleor/plugins/avatax/__init__.py:734]
- `retrieve_tax_code_from_meta` (function) — [saleor/plugins/avatax/__init__.py:766]

**`saleor/plugins/avatax/plugin.py`**

- `DeprecatedAvataxPlugin` (class) — [saleor/plugins/avatax/plugin.py:79]
- `calculate_checkout_total` (function) — [saleor/plugins/avatax/plugin.py:211]
- `calculate_checkout_shipping` (function) — [saleor/plugins/avatax/plugin.py:291]
- `preprocess_order_creation` (function) — [saleor/plugins/avatax/plugin.py:309]
- `order_confirmed` (function) — [saleor/plugins/avatax/plugin.py:369]
- `calculate_checkout_line_total` (function) — [saleor/plugins/avatax/plugin.py:402]
- `calculate_order_line_total` (function) — [saleor/plugins/avatax/plugin.py:469]
- `calculate_checkout_line_unit_price` (function) — [saleor/plugins/avatax/plugin.py:539]
- `calculate_order_line_unit` (function) — [saleor/plugins/avatax/plugin.py:573]
- `calculate_order_shipping` (function) — [saleor/plugins/avatax/plugin.py:626]
- `calculate_order_total` (function) — [saleor/plugins/avatax/plugin.py:634]
- `get_tax_rate_type_choices` (function) — [saleor/plugins/avatax/plugin.py:673]
- `get_checkout_line_tax_rate` (function) — [saleor/plugins/avatax/plugin.py:681]
- `get_order_line_tax_rate` (function) — [saleor/plugins/avatax/plugin.py:702]
- `get_checkout_shipping_tax_rate` (function) — [saleor/plugins/avatax/plugin.py:724]
- `get_order_shipping_tax_rate` (function) — [saleor/plugins/avatax/plugin.py:740]
- `get_tax_code_from_object_meta` (function) — [saleor/plugins/avatax/plugin.py:882]
- `validate_authentication` (function) — [saleor/plugins/avatax/plugin.py:907]
- `validate_plugin_configuration` (function) — [saleor/plugins/avatax/plugin.py:927]
- `validate_tax_data` (function) — [saleor/plugins/avatax/plugin.py:966]
- `check_negative_values_in_plugin_tax_data` (function) — [saleor/plugins/avatax/plugin.py:979]
- `check_overflows_in_plugin_tax_data` (function) — [saleor/plugins/avatax/plugin.py:991]

**`saleor/plugins/avatax/tasks.py`**

- `api_post_request_task` (function) — [saleor/plugins/avatax/tasks.py:21]

**`saleor/plugins/avatax/tests/conftest.py`**

- `vcr_config` (function) — [saleor/plugins/avatax/tests/conftest.py:12]
- `plugin_configuration` (function) — [saleor/plugins/avatax/tests/conftest.py:19]
- `set_configuration` (function) — [saleor/plugins/avatax/tests/conftest.py:23]

**`saleor/plugins/avatax/tests/test_avatax_caching.py`**

- `test_calculate_checkout_total_use_cache` (function) — [saleor/plugins/avatax/tests/test_avatax_caching.py:17]

**`saleor/plugins/avatax/tests/test_tasks.py`**

- `test_api_post_request_task_sends_request` (function) — [saleor/plugins/avatax/tests/test_tasks.py:14]
- `test_api_post_request_task_creates_order_event` (function) — [saleor/plugins/avatax/tests/test_tasks.py:47]

## How it works

The module's files, as provided to this run:

- `saleor/plugins/avatax/__init__.py` (770 lines)
- `saleor/plugins/avatax/plugin.py` (1000 lines)
- `saleor/plugins/avatax/tasks.py` (58 lines)
- `saleor/plugins/avatax/tests/__init__.py` (1 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_total_gift_promotion_line.yaml` (78 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_total_with_order_promotion[20.33-25.00-True].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_total_with_order_promotion[25.00-30.75-False].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_total_with_promotion[12.20-15.00-True].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_total_with_promotion[15.00-18.45-False].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_total_with_variant_on_promotion_and_voucher_only_once.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_total_with_variant_on_promotion_and_voucher.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_total_with_variant_on_promotion.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_total_with_voucher_once_per_order.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_total_with_voucher.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_total[24.39-30.00-True].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_total[30.00-36.90-False].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_unit_price_gift_promotion_line.yaml` (78 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_unit_price_in_JPY.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_unit_price_order_promotion_charge_taxes.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_unit_price_variant_on_promotion_and_voucher_only_once.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_unit_price_with_variant_on_promotion_and_voucher.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_unit_price_with_variant_on_promotion.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_unit_price_with_voucher_once_per_order.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_unit_price_with_voucher.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_unit_price[True].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_without_sku_total_with_promotion[12.20-15.00-True].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_without_sku_total_with_promotion[15.00-18.45-False].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_without_sku_total[24.39-30.00-True].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_line_without_sku_total[30.00-36.90-False].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_shipping.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_subtotal_voucher_on_entire_order[False].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_subtotal_voucher_on_entire_order[True].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_subtotal_voucher_on_shipping[24.39-30.00-True].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_subtotal_voucher_on_shipping[30.00-36.90-False].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_subtotal_with_promotion[20.33-25.00-True].yaml` (78 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_subtotal_with_promotion[25.00-30.75-False].yaml` (78 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_subtotal[40.65-50.00-True].yaml` (78 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_subtotal[50.00-61.50-False].yaml` (78 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_for_JPY_with_promotion[3484-4285-0.0-True].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_for_JPY_with_promotion[4280-5264-5.0-False].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_for_JPY[3493-4297-3.0-True].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_for_JPY[4300-5289-0.0-False].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_uses_default_calculation_with_promotion[21.99-26.73-5.0-False].yaml` (78 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_uses_default_calculation_with_promotion[22.32-26.99-0.0-True].yaml` (78 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_uses_default_calculation[32.04-38.99-3.0-True].yaml` (78 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_uses_default_calculation[41.99-51.19-0.0-False].yaml` (78 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_voucher_on_entire_order_applied_once_per_order.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_voucher_on_entire_order_product_without_taxes.yaml` (76 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_voucher_on_entire_order[10.00-12.30-False].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_voucher_on_entire_order[8.13-10.00-True].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_voucher_on_shipping[24.39-30.00-True].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_voucher_on_shipping[30.00-36.90-False].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_with_gift_promotion.yaml` (78 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_with_order_promotion.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total_with_promotion[22.32-26.99-0.0-True].yaml` (78 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total[32.04-38.99-3.0-True].yaml` (78 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_checkout_total[41.99-51.19-0.0-False].yaml` (78 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_line_total_entire_order_voucher[16.26-20.00-True].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_line_total_entire_order_voucher[20.00-24.60-False].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_line_total_shipping_voucher[24.39-30.00-True].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_line_total_shipping_voucher[30.00-36.90-False].yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_line_total_with_discount.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_line_total.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_line_unit_in_JPY.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_line_unit_with_discount.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_line_unit.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_line_without_sku_total.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_shipping_entire_order_voucher.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_shipping_free_shipping_voucher.yaml` (71 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_shipping_not_shippable_order.yaml` (71 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_shipping_voucher_on_shipping.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_shipping_zero_shipping_amount.yaml` (71 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_shipping.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_total_for_JPY.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_total_gift_promotion.yaml` (35 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_total_order_promotion.yaml` (33 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_calculate_order_total.yaml` (32 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_get_cached_tax_codes_or_fetch_wrong_response.yaml` (74 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_get_checkout_line_tax_rate_for_product_type_with_non_taxable_product.yaml` (34 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_get_checkout_line_tax_rate_for_product_with_charge_taxes_set_to_false.yaml` (32 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_get_checkout_line_tax_rate.yaml` (32 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_get_checkout_shipping_tax_rate.yaml` (32 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_get_order_line_tax_rate.yaml` (32 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_get_order_shipping_tax_rate_shipping_with_tax_class.yaml` (32 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_get_order_shipping_tax_rate.yaml` (32 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_get_order_tax_data_address_error_logging.yaml` (53 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_get_order_tax_data_with_single_location.yaml` (28 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_plugin_uses_configuration_from_db.yaml` (32 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_preprocess_order_creation_address_error_logging.yaml` (45 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_preprocess_order_creation_no_lines_data.yaml` (32 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_preprocess_order_creation_shipping_voucher_no_tax_class_on_delivery_method.yaml` (32 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_preprocess_order_creation_wrong_data.yaml` (57 lines)
- `saleor/plugins/avatax/tests/cassettes/test_avatax/test_preprocess_order_creation.yaml` (32 lines)
- `saleor/plugins/avatax/tests/cassettes/test_tasks/test_api_post_request_task_creates_order_event.yaml` (32 lines)
- `saleor/plugins/avatax/tests/cassettes/test_tasks/test_api_post_request_task_sends_request.yaml` (32 lines)
- `saleor/plugins/avatax/tests/conftest.py` (59 lines)
- `saleor/plugins/avatax/tests/test_avatax_caching.py` (59 lines)
- `saleor/plugins/avatax/tests/test_avatax.py` (60 lines)
- `saleor/plugins/avatax/tests/test_tasks.py` (62 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/plugins/openid_connect`, `saleor/graphql/product/types`, `saleor/core/utils`, `saleor/plugins`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....account.models.Address`
- `....checkout.fetch.CheckoutInfo`
- `....checkout.fetch.fetch_checkout_info`
- `....checkout.fetch.fetch_checkout_lines`
- `....checkout.tests.utils.add_variant_to_checkout`
- `....core.prices.quantize_price`
- `....core.taxes.TaxError`
- `....discount.DiscountType`
- `....discount.DiscountValueType`
- `....discount.RewardValueType`
- `....discount.VoucherType`
- `....discount.models.CheckoutLineDiscount`
- `....discount.models.Promotion`
- `....discount.models.PromotionRule`
- `....order.OrderEvents`
- `....order.OrderStatus`
- `....product.ProductTypeKind`
- `....product.models.Product`
- `....product.models.ProductType`
- `....product.models.ProductVariant`
- `....product.utils.variant_prices.update_discounted_prices_for_promotion`
- `....product.utils.variants.fetch_variants_for_promotion_rules`
- `....tax.TaxCalculationStrategy`
- `....tax.models.TaxClass`
- `...AvataxConfiguration`
- `...CACHE_KEY`
- `...PLUGIN_IDENTIFIER_PREFIX`
- `...account.models.Address`
- `...celeryconf.app`
- `...checkout.base_calculations`
- `...checkout.fetch.CheckoutInfo`
- `...checkout.fetch.CheckoutLineInfo`
- `...checkout.fetch.fetch_checkout_lines`
- `...checkout.utils.get_address_for_checkout_taxes`
- `...checkout.utils.is_shipping_required`
- `...checkout.utils.log_address_if_validation_skipped_for_checkout`
- `...core.db.connection.allow_writer`
- `...core.http_client.HTTPClient`
- `...core.prices.MAXIMUM_PRICE`
- `...core.taxes.TaxDataErrorMessage`
- `...core.taxes.TaxError`
- `...core.taxes.TaxType`
- `...core.taxes.zero_taxed_money`
- `...core.telemetry.saleor_attributes`
- `...core.telemetry.tracer`
- `...discount.DiscountType`
- `...discount.VoucherType`
- `...discount.utils.voucher.is_order_level_voucher`
- `...generate_request_data_from_checkout`
- `...get_api_url`
- `...get_order_request_data`
- `...manager.get_plugins_manager`
- `...models.PluginConfiguration`
- `...order.base_calculations`
- `...order.events.external_notification_event`
- `...order.interface.OrderTaxedPricesData`
- `...order.models.Order`
- `...order.models.OrderLine`
- `...product.models.Product`
- `...product.models.ProductType`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `bdd852977565` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
