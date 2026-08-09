## Purpose

`saleor/tests/e2e/checkout/zero_total` (`saleor/tests/e2e/checkout/zero_total`) groups 5 source file(s) exposing 4 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/checkout/zero_total/test_0_total_checkout_catalog_promotion_and_shipping_voucher.py`**

- `test_complete_0_total_checkout_with_catalog_promotion_and_free_shipping_voucher_CORE_0126` (function) — [saleor/tests/e2e/checkout/zero_total/test_0_total_checkout_catalog_promotion_and_shipping_voucher.py:27]

**`saleor/tests/e2e/checkout/zero_total/test_0_total_checkout_line_voucher_and_click_and_collect.py`**

- `test_complete_0_total_checkout_with_lines_voucher_and_click_and_collect_CORE_0125` (function) — [saleor/tests/e2e/checkout/zero_total/test_0_total_checkout_line_voucher_and_click_and_collect.py:26]

**`saleor/tests/e2e/checkout/zero_total/test_0_total_checkout_with_order_promotion_and_free_shipping.py`**

- `test_complete_0_total_checkout_with_order_promotion_and_free_shipping_method_CORE_0124` (function) — [saleor/tests/e2e/checkout/zero_total/test_0_total_checkout_with_order_promotion_and_free_shipping.py:24]

**`saleor/tests/e2e/checkout/zero_total/test_pay_for_total_checkout_with_gift_card.py`**

- `test_gift_card_total_payment_for_checkout_core_1101` (function) — [saleor/tests/e2e/checkout/zero_total/test_pay_for_total_checkout_with_gift_card.py:26]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/checkout/zero_total/__init__.py` (1 lines)
- `saleor/tests/e2e/checkout/zero_total/test_0_total_checkout_catalog_promotion_and_shipping_voucher.py` (208 lines)
- `saleor/tests/e2e/checkout/zero_total/test_0_total_checkout_line_voucher_and_click_and_collect.py` (216 lines)
- `saleor/tests/e2e/checkout/zero_total/test_0_total_checkout_with_order_promotion_and_free_shipping.py` (257 lines)
- `saleor/tests/e2e/checkout/zero_total/test_pay_for_total_checkout_with_gift_card.py` (154 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....product.tasks.recalculate_discounted_price_for_products_task`
- `...channel.utils.update_channel`
- `...gift_cards.utils.create_gift_card`
- `...orders.utils.order_query.order_query`
- `...product.utils.preparing_product.prepare_products`
- `...promotions.utils.create_promotion`
- `...promotions.utils.create_promotion_rule`
- `...shop.utils.preparing_shop.prepare_default_shop`
- `...shop.utils.preparing_shop.prepare_shop`
- `...utils.assign_permissions`
- `...vouchers.utils.prepare_voucher.prepare_voucher`
- `...warehouse.utils.update_warehouse`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `04d511481839` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
