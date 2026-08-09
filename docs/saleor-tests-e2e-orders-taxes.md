## Purpose

`saleor/tests/e2e/orders/taxes` (`saleor/tests/e2e/orders/taxes`) groups 6 source file(s) exposing 6 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/orders/taxes/test_draft_order_complete_return_tax_error.py`**

- `test_draft_order_complte_return_tax_error_when_app_not_respond_CORE_2015` (function) — [saleor/tests/e2e/orders/taxes/test_draft_order_complete_return_tax_error.py:19]

**`saleor/tests/e2e/orders/taxes/test_order_calculate_simple_taxes_based_on_shipping_address.py`**

- `test_order_calculate_simple_tax_based_on_shipping_address_CORE_2002` (function) — [saleor/tests/e2e/orders/taxes/test_order_calculate_simple_taxes_based_on_shipping_address.py:17]

**`saleor/tests/e2e/orders/taxes/test_order_calculate_simple_taxes_based_on_shipping_tax_class.py`**

- `test_order_calculate_simple_tax_based_on_shipping_tax_class_CORE_2010` (function) — [saleor/tests/e2e/orders/taxes/test_order_calculate_simple_taxes_based_on_shipping_tax_class.py:18]

**`saleor/tests/e2e/orders/taxes/test_order_calculate_simple_taxes_product_tax_class.py`**

- `test_order_calculate_simple_tax_based_on_product_tax_class_CORE_2006` (function) — [saleor/tests/e2e/orders/taxes/test_order_calculate_simple_taxes_product_tax_class.py:18]

**`saleor/tests/e2e/orders/taxes/test_order_calculate_simple_taxes_product_type_tax_class.py`**

- `prepare_product` (function) — [saleor/tests/e2e/orders/taxes/test_order_calculate_simple_taxes_product_type_tax_class.py:24]
- `test_order_calculate_simple_tax_based_on_product_type_tax_class_CORE_2004` (function) — [saleor/tests/e2e/orders/taxes/test_order_calculate_simple_taxes_product_type_tax_class.py:78]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/orders/taxes/__init__.py` (1 lines)
- `saleor/tests/e2e/orders/taxes/test_draft_order_complete_return_tax_error.py` (134 lines)
- `saleor/tests/e2e/orders/taxes/test_order_calculate_simple_taxes_based_on_shipping_address.py` (183 lines)
- `saleor/tests/e2e/orders/taxes/test_order_calculate_simple_taxes_based_on_shipping_tax_class.py` (175 lines)
- `saleor/tests/e2e/orders/taxes/test_order_calculate_simple_taxes_product_tax_class.py` (152 lines)
- `saleor/tests/e2e/orders/taxes/test_order_calculate_simple_taxes_product_type_tax_class.py` (214 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....ADDRESS_DE`
- `....DEFAULT_ADDRESS`
- `...apps.utils.add_app`
- `...product.utils.preparing_product.prepare_product`
- `...product.utils.update_product`
- `...shipping_zone.utils.update_shipping_price`
- `...shop.utils.prepare_shop`
- `...shop.utils.preparing_shop.prepare_default_shop`
- `...shop.utils.preparing_shop.prepare_shop`
- `...taxes.utils.get_tax_configurations`
- `...taxes.utils.update_country_tax_rates`
- `...taxes.utils.update_tax_configuration`
- `...utils.assign_permissions`
- `...webhooks.utils.create_webhook`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `9bfc1b556f06` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
