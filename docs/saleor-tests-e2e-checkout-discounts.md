## Purpose

`saleor/tests/e2e/checkout/discounts` (`saleor/tests/e2e/checkout/discounts`) groups 3 source file(s) exposing 10 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/checkout/discounts/test_checkout_calculate_correct_discount_for_sale_and_voucher.py`**

- `prepare_sale_for_products` (function) — [saleor/tests/e2e/checkout/discounts/test_checkout_calculate_correct_discount_for_sale_and_voucher.py:21]
- `prepare_voucher` (function) — [saleor/tests/e2e/checkout/discounts/test_checkout_calculate_correct_discount_for_sale_and_voucher.py:57]
- `test_checkout_calculate_discount_for_percentage_sale_and_percentage_voucher_CORE_0114` (function) — [saleor/tests/e2e/checkout/discounts/test_checkout_calculate_correct_discount_for_sale_and_voucher.py:91]
- `test_checkout_calculate_discount_for_fixed_sale_and_fixed_voucher_CORE_0114` (function) — [saleor/tests/e2e/checkout/discounts/test_checkout_calculate_correct_discount_for_sale_and_voucher.py:535]
- `test_checkout_calculate_discount_for_fixed_sale_and_percentage_voucher_CORE_0114` (function) — [saleor/tests/e2e/checkout/discounts/test_checkout_calculate_correct_discount_for_sale_and_voucher.py:979]
- `test_checkout_calculate_discount_for_percentage_sale_and_fixed_voucher_CORE_0114` (function) — [saleor/tests/e2e/checkout/discounts/test_checkout_calculate_correct_discount_for_sale_and_voucher.py:1420]

**`saleor/tests/e2e/checkout/discounts/test_checkout_with_promotion_and_voucher.py`**

- `prepare_promotion` (function) — [saleor/tests/e2e/checkout/discounts/test_checkout_with_promotion_and_voucher.py:23]
- `prepare_voucher` (function) — [saleor/tests/e2e/checkout/discounts/test_checkout_with_promotion_and_voucher.py:69]
- `test_checkout_with_promotion_and_voucher_legacy_propagation_CORE_2107` (function) — [saleor/tests/e2e/checkout/discounts/test_checkout_with_promotion_and_voucher.py:126]
- `test_checkout_with_promotion_and_voucher_CORE_2107` (function) — [saleor/tests/e2e/checkout/discounts/test_checkout_with_promotion_and_voucher.py:291]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/checkout/discounts/__init__.py` (1 lines)
- `saleor/tests/e2e/checkout/discounts/test_checkout_calculate_correct_discount_for_sale_and_voucher.py` (1855 lines)
- `saleor/tests/e2e/checkout/discounts/test_checkout_with_promotion_and_voucher.py` (435 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....product.tasks.recalculate_discounted_price_for_products_task`
- `...product.utils.preparing_product.prepare_product`
- `...product.utils.preparing_product.prepare_products`
- `...promotions.utils.create_promotion`
- `...promotions.utils.create_promotion_rule`
- `...sales.utils.create_sale`
- `...sales.utils.create_sale_channel_listing`
- `...sales.utils.sale_catalogues_add`
- `...shop.utils.prepare_default_shop`
- `...shop.utils.preparing_shop.prepare_default_shop`
- `...utils.assign_permissions`
- `...vouchers.utils.create_voucher`
- `...vouchers.utils.create_voucher_channel_listing`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `60ddcff50a8e` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
