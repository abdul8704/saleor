## Purpose

`saleor/tests/e2e/checkout/discounts/promotions` (`saleor/tests/e2e/checkout/discounts/promotions`) groups 9 source file(s) exposing 12 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/checkout/discounts/promotions/test_checkout_custom_price_and_fixed_promotion.py`**

- `test_checkout_custom_price_and_fixed_promotion_core_2138` (function) — [saleor/tests/e2e/checkout/discounts/promotions/test_checkout_custom_price_and_fixed_promotion.py:18]

**`saleor/tests/e2e/checkout/discounts/promotions/test_checkout_custom_price_and_percentage_promotion.py`**

- `test_checkout_custom_price_and_percentage_promotion_core_2139` (function) — [saleor/tests/e2e/checkout/discounts/promotions/test_checkout_custom_price_and_percentage_promotion.py:18]

**`saleor/tests/e2e/checkout/discounts/promotions/test_checkout_products_on_fixed_promotion.py`**

- `test_checkout_products_on_fixed_promotion_core_2102` (function) — [saleor/tests/e2e/checkout/discounts/promotions/test_checkout_products_on_fixed_promotion.py:17]

**`saleor/tests/e2e/checkout/discounts/promotions/test_checkout_products_on_percentage_promotion.py`**

- `test_checkout_products_on_percentage_promotion_core_2104` (function) — [saleor/tests/e2e/checkout/discounts/promotions/test_checkout_products_on_percentage_promotion.py:17]

**`saleor/tests/e2e/checkout/discounts/promotions/test_checkout_with_fixed_promotion_should_not_result_in_negative_price.py`**

- `test_checkout_with_fixed_promotion_should_not_result_in_negative_price_CORE_2111` (function) — [saleor/tests/e2e/checkout/discounts/promotions/test_checkout_with_fixed_promotion_should_not_result_in_negative_price.py:13]

**`saleor/tests/e2e/checkout/discounts/promotions/test_promotion_applied_on_checkout_with_specific_subtotal.py`**

- `prepare_promotion` (function) — [saleor/tests/e2e/checkout/discounts/promotions/test_promotion_applied_on_checkout_with_specific_subtotal.py:20]
- `test_promotion_applied_on_checkout_with_specific_subtotal_CORE_2133` (function) — [saleor/tests/e2e/checkout/discounts/promotions/test_promotion_applied_on_checkout_with_specific_subtotal.py:68]

**`saleor/tests/e2e/checkout/discounts/promotions/test_promotion_applied_on_checkout_with_subtotal_within_specified_range.py`**

- `prepare_promotion` (function) — [saleor/tests/e2e/checkout/discounts/promotions/test_promotion_applied_on_checkout_with_subtotal_within_specified_range.py:23]
- `test_promotion_applied_on_checkout_with_subtotal_with_specified_gte_range_CORE_2136` (function) — [saleor/tests/e2e/checkout/discounts/promotions/test_promotion_applied_on_checkout_with_subtotal_within_specified_range.py:47]
- `test_promotion_applied_on_checkout_with_subtotal_with_specified_lte_range_CORE_2136` (function) — [saleor/tests/e2e/checkout/discounts/promotions/test_promotion_applied_on_checkout_with_subtotal_within_specified_range.py:176]

**`saleor/tests/e2e/checkout/discounts/promotions/test_promotion_discount_applied_on_checkout_with_specific_total_and_subtotal.py`**

- `prepare_promotion` (function) — [saleor/tests/e2e/checkout/discounts/promotions/test_promotion_discount_applied_on_checkout_with_specific_total_and_subtotal.py:20]
- `test_promotion_discount_applied_on_checkout_with_specific_total_and_subtotal_CORE_2134` (function) — [saleor/tests/e2e/checkout/discounts/promotions/test_promotion_discount_applied_on_checkout_with_specific_total_and_subtotal.py:82]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/checkout/discounts/promotions/__init__.py` (1 lines)
- `saleor/tests/e2e/checkout/discounts/promotions/test_checkout_custom_price_and_fixed_promotion.py` (147 lines)
- `saleor/tests/e2e/checkout/discounts/promotions/test_checkout_custom_price_and_percentage_promotion.py` (145 lines)
- `saleor/tests/e2e/checkout/discounts/promotions/test_checkout_products_on_fixed_promotion.py` (128 lines)
- `saleor/tests/e2e/checkout/discounts/promotions/test_checkout_products_on_percentage_promotion.py` (125 lines)
- `saleor/tests/e2e/checkout/discounts/promotions/test_checkout_with_fixed_promotion_should_not_result_in_negative_price.py` (109 lines)
- `saleor/tests/e2e/checkout/discounts/promotions/test_promotion_applied_on_checkout_with_specific_subtotal.py` (166 lines)
- `saleor/tests/e2e/checkout/discounts/promotions/test_promotion_applied_on_checkout_with_subtotal_within_specified_range.py` (301 lines)
- `saleor/tests/e2e/checkout/discounts/promotions/test_promotion_discount_applied_on_checkout_with_specific_total_and_subtotal.py` (180 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `......checkout.models.Checkout`
- `......discount.DiscountType`
- `......discount.RewardValueType`
- `......product.tasks.recalculate_discounted_price_for_products_task`
- `....checkout.utils.checkout_lines_update`
- `....product.utils.get_product`
- `....product.utils.preparing_product.prepare_product`
- `....promotions.utils.create_promotion`
- `....promotions.utils.create_promotion_rule`
- `....shop.utils.prepare_default_shop`
- `....shop.utils.preparing_shop.prepare_default_shop`
- `....utils.assign_permissions`
- `...utils.checkout_create`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `e6b5f851885c` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
