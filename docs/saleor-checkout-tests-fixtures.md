## Purpose

`saleor/checkout/tests/fixtures` (`saleor/checkout/tests/fixtures`) groups 10 source file(s) exposing 79 top-level declaration(s).

## Public surface

**`saleor/checkout/tests/fixtures/benchmark.py`**

- `checkouts_for_benchmarks` (function) — [saleor/checkout/tests/fixtures/benchmark.py:10]

**`saleor/checkout/tests/fixtures/checkout_info.py`**

- `checkout_info` (function) — [saleor/checkout/tests/fixtures/checkout_info.py:8]
- `checkout_with_items_and_shipping_info` (function) — [saleor/checkout/tests/fixtures/checkout_info.py:16]

**`saleor/checkout/tests/fixtures/checkout_line_info.py`**

- `checkout_lines_info` (function) — [saleor/checkout/tests/fixtures/checkout_line_info.py:7]
- `checkout_lines_with_multiple_quantity_info` (function) — [saleor/checkout/tests/fixtures/checkout_line_info.py:26]

**`saleor/checkout/tests/fixtures/checkout_line.py`**

- `checkout_line` (function) — [saleor/checkout/tests/fixtures/checkout_line.py:13]
- `checkout_lines` (function) — [saleor/checkout/tests/fixtures/checkout_line.py:18]
- `checkout_line_with_reservation_in_many_stocks` (function) — [saleor/checkout/tests/fixtures/checkout_line.py:23]
- `checkout_line_with_one_reservation` (function) — [saleor/checkout/tests/fixtures/checkout_line.py:59]
- `checkout_line_with_preorder_item` (function) — [saleor/checkout/tests/fixtures/checkout_line.py:85]
- `checkout_line_with_reserved_preorder_item` (function) — [saleor/checkout/tests/fixtures/checkout_line.py:96]

**`saleor/checkout/tests/fixtures/checkout_with_discount.py`**

- `checkout_with_item_on_promotion` (function) — [saleor/checkout/tests/fixtures/checkout_with_discount.py:18]
- `checkout_with_item_and_order_discount` (function) — [saleor/checkout/tests/fixtures/checkout_with_discount.py:70]
- `checkout_with_item_and_gift_promotion` (function) — [saleor/checkout/tests/fixtures/checkout_with_discount.py:103]
- `checkout_with_item_and_voucher` (function) — [saleor/checkout/tests/fixtures/checkout_with_discount.py:137]
- `checkout_with_item_and_voucher_specific_products` (function) — [saleor/checkout/tests/fixtures/checkout_with_discount.py:149]
- `checkout_with_item_and_voucher_once_per_order` (function) — [saleor/checkout/tests/fixtures/checkout_with_discount.py:167]
- `checkout_with_item_and_voucher_and_shipping_method` (function) — [saleor/checkout/tests/fixtures/checkout_with_discount.py:181]
- `checkout_with_voucher` (function) — [saleor/checkout/tests/fixtures/checkout_with_discount.py:192]
- `checkout_with_voucher_percentage` (function) — [saleor/checkout/tests/fixtures/checkout_with_discount.py:205]
- `checkout_with_voucher_percentage_and_shipping` (function) — [saleor/checkout/tests/fixtures/checkout_with_discount.py:218]
- `checkout_with_voucher_free_shipping` (function) — [saleor/checkout/tests/fixtures/checkout_with_discount.py:229]

**`saleor/checkout/tests/fixtures/checkout_with_payment.py`**

- `checkout_with_payments` (function) — [saleor/checkout/tests/fixtures/checkout_with_payment.py:12]
- `checkout_with_charged_payment` (function) — [saleor/checkout/tests/fixtures/checkout_with_payment.py:27]
- `checkout_with_charged_payment_for_cc` (function) — [saleor/checkout/tests/fixtures/checkout_with_payment.py:60]
- `checkout_preorder_with_charged_payment` (function) — [saleor/checkout/tests/fixtures/checkout_with_payment.py:94]

**`saleor/checkout/tests/fixtures/checkout_with_prices.py`**

- `checkout_with_prices` (function) — [saleor/checkout/tests/fixtures/checkout_with_prices.py:14]
- `priced_checkout_factory` (function) — [saleor/checkout/tests/fixtures/checkout_with_prices.py:96]
- `factory` (function) — [saleor/checkout/tests/fixtures/checkout_with_prices.py:97]
- `priced_checkout_with_item` (function) — [saleor/checkout/tests/fixtures/checkout_with_prices.py:143]
- `priced_checkout_with_items` (function) — [saleor/checkout/tests/fixtures/checkout_with_prices.py:148]
- `priced_checkout_with_voucher_percentage` (function) — [saleor/checkout/tests/fixtures/checkout_with_prices.py:153]

**`saleor/checkout/tests/fixtures/checkout_with_transaction.py`**

- `checkout_with_item_and_transaction_item` (function) — [saleor/checkout/tests/fixtures/checkout_with_transaction.py:9]

**`saleor/checkout/tests/fixtures/checkout.py`**

- `checkout_delivery` (function) — [saleor/checkout/tests/fixtures/checkout.py:15]
- `wrap` (function) — [saleor/checkout/tests/fixtures/checkout.py:16]
- `checkout` (function) — [saleor/checkout/tests/fixtures/checkout.py:45]
- `checkout_JPY` (function) — [saleor/checkout/tests/fixtures/checkout.py:58]
- `checkout_with_item` (function) — [saleor/checkout/tests/fixtures/checkout.py:68]
- `checkout_with_item_and_tax_exemption` (function) — [saleor/checkout/tests/fixtures/checkout.py:79]
- `checkout_with_same_items_in_multiple_lines` (function) — [saleor/checkout/tests/fixtures/checkout.py:86]
- `checkout_with_item_total_0` (function) — [saleor/checkout/tests/fixtures/checkout.py:98]
- `checkout_JPY_with_item` (function) — [saleor/checkout/tests/fixtures/checkout.py:109]
- `checkouts_list` (function) — [saleor/checkout/tests/fixtures/checkout.py:120]
- `checkouts_assigned_to_customer` (function) — [saleor/checkout/tests/fixtures/checkout.py:138]
- `checkout_ready_to_complete` (function) — [saleor/checkout/tests/fixtures/checkout.py:156]
- `checkout_with_shipping_required` (function) — [saleor/checkout/tests/fixtures/checkout.py:175]
- `checkout_with_item_and_shipping_method` (function) — [saleor/checkout/tests/fixtures/checkout.py:187]
- `checkout_with_shipping_method` (function) — [saleor/checkout/tests/fixtures/checkout.py:198]
- `checkout_without_shipping_required` (function) — [saleor/checkout/tests/fixtures/checkout.py:210]
- `checkout_with_single_item` (function) — [saleor/checkout/tests/fixtures/checkout.py:221]
- `checkout_with_variant_without_inventory_tracking` (function) — [saleor/checkout/tests/fixtures/checkout.py:232]
- `checkout_with_variants` (function) — [saleor/checkout/tests/fixtures/checkout.py:256]
- `checkout_with_shipping_address` (function) — [saleor/checkout/tests/fixtures/checkout.py:283]
- `checkout_with_billing_address` (function) — [saleor/checkout/tests/fixtures/checkout.py:293]
- `checkout_with_variants_for_cc` (function) — [saleor/checkout/tests/fixtures/checkout.py:303]
- `checkout_with_shipping_address_for_cc` (function) — [saleor/checkout/tests/fixtures/checkout.py:350]
- `checkout_with_billing_address_for_cc` (function) — [saleor/checkout/tests/fixtures/checkout.py:360]
- `checkout_with_delivery_method_for_cc` (function) — [saleor/checkout/tests/fixtures/checkout.py:370]
- `checkout_with_delivery_method_for_external_shipping` (function) — [saleor/checkout/tests/fixtures/checkout.py:382]
- `checkout_with_items` (function) — [saleor/checkout/tests/fixtures/checkout.py:397]
- `checkout_with_items_and_shipping` (function) — [saleor/checkout/tests/fixtures/checkout.py:412]
- `checkout_with_item_and_shipping` (function) — [saleor/checkout/tests/fixtures/checkout.py:421]
- `checkout_with_gift_card` (function) — [saleor/checkout/tests/fixtures/checkout.py:434]
- `checkout_with_preorders_only` (function) — [saleor/checkout/tests/fixtures/checkout.py:441]
- `checkout_with_preorders_and_regular_variant` (function) — [saleor/checkout/tests/fixtures/checkout.py:459]
- `checkout_with_gift_card_items` (function) — [saleor/checkout/tests/fixtures/checkout.py:474]
- `checkout_with_item_and_preorder_item` (function) — [saleor/checkout/tests/fixtures/checkout.py:489]
- `checkout_with_problems` (function) — [saleor/checkout/tests/fixtures/checkout.py:500]
- `user_checkout` (function) — [saleor/checkout/tests/fixtures/checkout.py:543]
- `user_checkout_for_cc` (function) — [saleor/checkout/tests/fixtures/checkout.py:557]
- `user_checkout_PLN` (function) — [saleor/checkout/tests/fixtures/checkout.py:572]
- `user_checkout_with_items` (function) — [saleor/checkout/tests/fixtures/checkout.py:585]
- `user_checkout_with_items_for_cc` (function) — [saleor/checkout/tests/fixtures/checkout.py:597]
- _…and 6 more in this file_

## How it works

The module's files, as provided to this run:

- `saleor/checkout/tests/fixtures/__init__.py` (9 lines)
- `saleor/checkout/tests/fixtures/benchmark.py` (29 lines)
- `saleor/checkout/tests/fixtures/checkout_info.py` (34 lines)
- `saleor/checkout/tests/fixtures/checkout_line_info.py` (44 lines)
- `saleor/checkout/tests/fixtures/checkout_line.py` (114 lines)
- `saleor/checkout/tests/fixtures/checkout_with_discount.py` (244 lines)
- `saleor/checkout/tests/fixtures/checkout_with_payment.py` (132 lines)
- `saleor/checkout/tests/fixtures/checkout_with_prices.py` (156 lines)
- `saleor/checkout/tests/fixtures/checkout_with_transaction.py` (18 lines)
- `saleor/checkout/tests/fixtures/checkout.py` (716 lines)

## Interactions

- Imports from: `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....base_calculations`
- `....calculations`
- `....checkout.models.Checkout`
- `....discount.DiscountType`
- `....discount.DiscountValueType`
- `....discount.RewardType`
- `....discount.RewardValueType`
- `....discount.models.CheckoutDiscount`
- `....discount.models.CheckoutLineDiscount`
- `....discount.models.Promotion`
- `....payment.ChargeStatus`
- `....payment.TransactionKind`
- `....payment.models.Payment`
- `....payment.models.TransactionItem`
- `....plugins.manager.get_plugins_manager`
- `....product.models.ProductVariantChannelListing`
- `....warehouse.models.PreorderReservation`
- `....warehouse.models.Reservation`
- `...fetch.CheckoutInfo`
- `...fetch.fetch_checkout_info`
- `...fetch.fetch_checkout_lines`
- `...models.Checkout`
- `...models.CheckoutDelivery`
- `...models.CheckoutLine`
- `...models.CheckoutMetadata`
- `...utils.add_voucher_to_checkout`
- `..utils.add_variant_to_checkout`
- `.benchmark.*  # noqa: F403`
- `.checkout.*  # noqa: F403`
- `.checkout_info.*  # noqa: F403`
- `.checkout_line.*  # noqa: F403`
- `.checkout_line_info.*  # noqa: F403`
- `.checkout_with_discount.*  # noqa: F403`
- `.checkout_with_payment.*  # noqa: F403`
- `.checkout_with_prices.*  # noqa: F403`
- `.checkout_with_transaction.*  # noqa: F403`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `f1870f723c63` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
