## Purpose

`saleor/tests/e2e/checkout/discounts/sales` (`saleor/tests/e2e/checkout/discounts/sales`) groups 6 source file(s) exposing 8 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/checkout/discounts/sales/test_checkout_custom_price_and_fixed_sale.py`**

- `test_checkout_custom_price_and_fixed_sale_CORE_1006` (function) — [saleor/tests/e2e/checkout/discounts/sales/test_checkout_custom_price_and_fixed_sale.py:22]

**`saleor/tests/e2e/checkout/discounts/sales/test_checkout_custom_price_and_percentage_sale.py`**

- `test_checkout_custom_price_and_percentage_sale_CORE_1007` (function) — [saleor/tests/e2e/checkout/discounts/sales/test_checkout_custom_price_and_percentage_sale.py:22]

**`saleor/tests/e2e/checkout/discounts/sales/test_checkout_product_on_fixed_sale.py`**

- `prepare_sale_for_products` (function) — [saleor/tests/e2e/checkout/discounts/sales/test_checkout_product_on_fixed_sale.py:23]
- `test_checkout_products_on_fixed_sale_core_1002` (function) — [saleor/tests/e2e/checkout/discounts/sales/test_checkout_product_on_fixed_sale.py:59]

**`saleor/tests/e2e/checkout/discounts/sales/test_checkout_product_on_percentage_sale.py`**

- `prepare_sale_for_products` (function) — [saleor/tests/e2e/checkout/discounts/sales/test_checkout_product_on_percentage_sale.py:23]
- `test_checkout_products_on_percentage_sale_core_1004` (function) — [saleor/tests/e2e/checkout/discounts/sales/test_checkout_product_on_percentage_sale.py:59]

**`saleor/tests/e2e/checkout/discounts/sales/test_checkout_with_fixed_sale_should_not_result_in_negative_price.py`**

- `prepare_sale_for_products` (function) — [saleor/tests/e2e/checkout/discounts/sales/test_checkout_with_fixed_sale_should_not_result_in_negative_price.py:23]
- `test_checkout_with_fixed_sale_should_not_result_in_negative_price_CORE_1005` (function) — [saleor/tests/e2e/checkout/discounts/sales/test_checkout_with_fixed_sale_should_not_result_in_negative_price.py:59]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/checkout/discounts/sales/__init__.py` (1 lines)
- `saleor/tests/e2e/checkout/discounts/sales/test_checkout_custom_price_and_fixed_sale.py` (149 lines)
- `saleor/tests/e2e/checkout/discounts/sales/test_checkout_custom_price_and_percentage_sale.py` (149 lines)
- `saleor/tests/e2e/checkout/discounts/sales/test_checkout_product_on_fixed_sale.py` (401 lines)
- `saleor/tests/e2e/checkout/discounts/sales/test_checkout_product_on_percentage_sale.py` (406 lines)
- `saleor/tests/e2e/checkout/discounts/sales/test_checkout_with_fixed_sale_should_not_result_in_negative_price.py` (335 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `......product.tasks.recalculate_discounted_price_for_products_task`
- `....checkout.utils.checkout_lines_update`
- `....product.utils.get_product`
- `....product.utils.preparing_product.prepare_product`
- `....product.utils.preparing_product.prepare_products`
- `....shop.utils.prepare_default_shop`
- `....utils.assign_permissions`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `dee3f6d6aab2` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
