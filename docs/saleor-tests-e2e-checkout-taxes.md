## Purpose

`saleor/tests/e2e/checkout/taxes` (`saleor/tests/e2e/checkout/taxes`) groups 9 source file(s) exposing 10 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/checkout/taxes/test_checkout_calculate_simple_taxes_based_on_shipping_country.py`**

- `test_checkout_calculate_simple_tax_based_on_shipping_country_CORE_2001` (function) — [saleor/tests/e2e/checkout/taxes/test_checkout_calculate_simple_taxes_based_on_shipping_country.py:20]

**`saleor/tests/e2e/checkout/taxes/test_checkout_calculate_simple_taxes_based_on_shipping_tax_class.py`**

- `test_checkout_calculate_simple_tax_based_on_shipping_tax_class_CORE_2009` (function) — [saleor/tests/e2e/checkout/taxes/test_checkout_calculate_simple_taxes_based_on_shipping_tax_class.py:17]

**`saleor/tests/e2e/checkout/taxes/test_checkout_calculate_simple_taxes_for_products_without_shipping.py`**

- `test_no_shipping_checkout_calculate_simple_tax_based_on_billing_country_CORE_2007` (function) — [saleor/tests/e2e/checkout/taxes/test_checkout_calculate_simple_taxes_for_products_without_shipping.py:17]

**`saleor/tests/e2e/checkout/taxes/test_checkout_calculate_simple_taxes_product_tax_class.py`**

- `test_checkout_calculate_simple_tax_based_on_product_tax_class_CORE_2005` (function) — [saleor/tests/e2e/checkout/taxes/test_checkout_calculate_simple_taxes_product_tax_class.py:17]

**`saleor/tests/e2e/checkout/taxes/test_checkout_calculate_simple_taxes_product_type_tax_class.py`**

- `prepare_product` (function) — [saleor/tests/e2e/checkout/taxes/test_checkout_calculate_simple_taxes_product_type_tax_class.py:23]
- `test_checkout_calculate_simple_tax_based_on_product_type_tax_class_CORE_2003` (function) — [saleor/tests/e2e/checkout/taxes/test_checkout_calculate_simple_taxes_product_type_tax_class.py:77]

**`saleor/tests/e2e/checkout/taxes/test_checkout_complete_return_tax_error.py`**

- `test_checkout_calculate_return_tax_error_when_app_not_respond_CORE_2013` (function) — [saleor/tests/e2e/checkout/taxes/test_checkout_complete_return_tax_error.py:18]

**`saleor/tests/e2e/checkout/taxes/test_checkout_with_click_and_collect_calculate_simple_taxes_based_on_shipping_address.py`**

- `test_calculate_simple_taxes_order_with_click_and_collect_with_prices_entered_with_tax_true_CORE_2012` (function) — [saleor/tests/e2e/checkout/taxes/test_checkout_with_click_and_collect_calculate_simple_taxes_based_on_shipping_address.py:20]
- `test_calculate_simple_taxes_order_with_click_and_collect_with_prices_entered_with_tax_false_CORE_2012` (function) — [saleor/tests/e2e/checkout/taxes/test_checkout_with_click_and_collect_calculate_simple_taxes_based_on_shipping_address.py:179]

**`saleor/tests/e2e/checkout/taxes/test_order_create_from_checkout_return_tax_error.py`**

- `test_order_create_from_checkout_return_tax_error_when_app_not_respond_CORE_2014` (function) — [saleor/tests/e2e/checkout/taxes/test_order_create_from_checkout_return_tax_error.py:17]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/checkout/taxes/__init__.py` (1 lines)
- `saleor/tests/e2e/checkout/taxes/test_checkout_calculate_simple_taxes_based_on_shipping_country.py` (216 lines)
- `saleor/tests/e2e/checkout/taxes/test_checkout_calculate_simple_taxes_based_on_shipping_tax_class.py` (173 lines)
- `saleor/tests/e2e/checkout/taxes/test_checkout_calculate_simple_taxes_for_products_without_shipping.py` (158 lines)
- `saleor/tests/e2e/checkout/taxes/test_checkout_calculate_simple_taxes_product_tax_class.py` (159 lines)
- `saleor/tests/e2e/checkout/taxes/test_checkout_calculate_simple_taxes_product_type_tax_class.py` (213 lines)
- `saleor/tests/e2e/checkout/taxes/test_checkout_complete_return_tax_error.py` (137 lines)
- `saleor/tests/e2e/checkout/taxes/test_checkout_with_click_and_collect_calculate_simple_taxes_based_on_shipping_address.py` (328 lines)
- `saleor/tests/e2e/checkout/taxes/test_order_create_from_checkout_return_tax_error.py` (134 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....ADDRESS_DE`
- `...apps.utils.add_app`
- `...orders.utils.raw_order_create_from_checkout`
- `...product.utils.preparing_product.prepare_product`
- `...product.utils.update_product`
- `...shipping_zone.utils.update_shipping_price`
- `...shop.utils.prepare_default_shop`
- `...shop.utils.prepare_shop`
- `...shop.utils.preparing_shop.prepare_shop`
- `...taxes.utils.get_tax_configurations`
- `...taxes.utils.update_country_tax_rates`
- `...taxes.utils.update_tax_configuration`
- `...utils.assign_permissions`
- `...warehouse.utils.update_warehouse`
- `...webhooks.utils.create_webhook`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `d0498d9dea8f` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
