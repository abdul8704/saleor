## Purpose

`saleor/order/tests/fixtures` (`saleor/order/tests/fixtures`) groups 6 source file(s) exposing 60 top-level declaration(s).

## Public surface

**`saleor/order/tests/fixtures/benchmark.py`**

- `users_for_order_benchmarks` (function) — [saleor/order/tests/fixtures/benchmark.py:85]
- `orders_for_benchmarks` (function) — [saleor/order/tests/fixtures/benchmark.py:101]
- `draft_orders_for_benchmarks` (function) — [saleor/order/tests/fixtures/benchmark.py:166]

**`saleor/order/tests/fixtures/draft_order.py`**

- `draft_order` (function) — [saleor/order/tests/fixtures/draft_order.py:28]
- `draft_order_with_fixed_discount_order` (function) — [saleor/order/tests/fixtures/draft_order.py:37]
- `draft_order_with_voucher` (function) — [saleor/order/tests/fixtures/draft_order.py:53]
- `draft_order_with_free_shipping_voucher` (function) — [saleor/order/tests/fixtures/draft_order.py:76]
- `draft_order_without_inventory_tracking` (function) — [saleor/order/tests/fixtures/draft_order.py:109]
- `draft_order_with_preorder_lines` (function) — [saleor/order/tests/fixtures/draft_order.py:117]
- `draft_order_list_with_multiple_use_voucher` (function) — [saleor/order/tests/fixtures/draft_order.py:128]
- `draft_order_list_with_single_use_voucher` (function) — [saleor/order/tests/fixtures/draft_order.py:137]
- `draft_order_list` (function) — [saleor/order/tests/fixtures/draft_order.py:150]
- `draft_orders_in_different_channels` (function) — [saleor/order/tests/fixtures/draft_order.py:160]
- `draft_order_and_promotions` (function) — [saleor/order/tests/fixtures/draft_order.py:172]

**`saleor/order/tests/fixtures/fulfillment.py`**

- `fulfillment` (function) — [saleor/order/tests/fixtures/fulfillment.py:11]
- `full_fulfillment_awaiting_approval` (function) — [saleor/order/tests/fixtures/fulfillment.py:16]
- `partial_fulfillment_awaiting_approval` (function) — [saleor/order/tests/fixtures/fulfillment.py:42]
- `order_fulfill_data` (function) — [saleor/order/tests/fixtures/fulfillment.py:66]
- `FulfillmentData` (class) — [saleor/order/tests/fixtures/fulfillment.py:67]

**`saleor/order/tests/fixtures/order_line.py`**

- `order_line` (function) — [saleor/order/tests/fixtures/order_line.py:14]
- `order_line_on_promotion` (function) — [saleor/order/tests/fixtures/order_line.py:44]
- `order_line_JPY` (function) — [saleor/order/tests/fixtures/order_line.py:108]
- `order_line_with_allocation_in_many_stocks` (function) — [saleor/order/tests/fixtures/order_line.py:141]
- `order_line_with_one_allocation` (function) — [saleor/order/tests/fixtures/order_line.py:200]
- `lines_info` (function) — [saleor/order/tests/fixtures/order_line.py:252]
- `gift_card_non_shippable_order_line` (function) — [saleor/order/tests/fixtures/order_line.py:265]
- `gift_card_shippable_order_line` (function) — [saleor/order/tests/fixtures/order_line.py:300]

**`saleor/order/tests/fixtures/order.py`**

- `recalculate_order` (function) — [saleor/order/tests/fixtures/order.py:46]
- `get_voucher_discount_for_order` (function) — [saleor/order/tests/fixtures/order.py:74]
- `get_products_voucher_discount_for_order` (function) — [saleor/order/tests/fixtures/order.py:94]
- `orders` (function) — [saleor/order/tests/fixtures/order.py:106]
- `orders_from_checkout` (function) — [saleor/order/tests/fixtures/order.py:150]
- `order_generator` (function) — [saleor/order/tests/fixtures/order.py:186]
- `create_order` (function) — [saleor/order/tests/fixtures/order.py:189]
- `order` (function) — [saleor/order/tests/fixtures/order.py:230]
- `order_with_gift_card` (function) — [saleor/order/tests/fixtures/order.py:235]
- `order_unconfirmed` (function) — [saleor/order/tests/fixtures/order.py:241]
- `order_list` (function) — [saleor/order/tests/fixtures/order.py:248]
- `draft_order_list` (function) — [saleor/order/tests/fixtures/order.py:266]
- `order_list_with_cc_orders` (function) — [saleor/order/tests/fixtures/order.py:274]
- `order_lines_generator` (function) — [saleor/order/tests/fixtures/order.py:292]
- `create_order_line` (function) — [saleor/order/tests/fixtures/order.py:293]
- `order_with_lines` (function) — [saleor/order/tests/fixtures/order.py:361]
- `order_with_lines_untaxed` (function) — [saleor/order/tests/fixtures/order.py:459]
- `order_with_lines_for_cc` (function) — [saleor/order/tests/fixtures/order.py:485]
- `order_with_lines_and_catalogue_promotion` (function) — [saleor/order/tests/fixtures/order.py:546]
- `order_with_lines_and_order_promotion` (function) — [saleor/order/tests/fixtures/order.py:608]
- `order_with_lines_and_gift_promotion` (function) — [saleor/order/tests/fixtures/order.py:638]
- `order_with_lines_and_events` (function) — [saleor/order/tests/fixtures/order.py:684]
- `order_with_lines_channel_PLN` (function) — [saleor/order/tests/fixtures/order.py:714]
- `order_with_line_without_inventory_tracking` (function) — [saleor/order/tests/fixtures/order.py:862]
- `order_with_preorder_lines` (function) — [saleor/order/tests/fixtures/order.py:902]
- `order_events` (function) — [saleor/order/tests/fixtures/order.py:981]
- `fulfilled_order` (function) — [saleor/order/tests/fixtures/order.py:991]
- `unconfirmed_order_with_lines` (function) — [saleor/order/tests/fixtures/order.py:1026]
- `fulfilled_order_without_inventory_tracking` (function) — [saleor/order/tests/fixtures/order.py:1034]
- `fulfilled_order_with_cancelled_fulfillment` (function) — [saleor/order/tests/fixtures/order.py:1055]
- `fulfilled_order_with_all_cancelled_fulfillments` (function) — [saleor/order/tests/fixtures/order.py:1067]
- `order_without_shipping_required` (function) — [saleor/order/tests/fixtures/order.py:1083]
- `preorders` (function) — [saleor/order/tests/fixtures/order.py:1117]

## How it works

The module's files, as provided to this run:

- `saleor/order/tests/fixtures/__init__.py` (5 lines)
- `saleor/order/tests/fixtures/benchmark.py` (172 lines)
- `saleor/order/tests/fixtures/draft_order.py` (267 lines)
- `saleor/order/tests/fixtures/fulfillment.py` (97 lines)
- `saleor/order/tests/fixtures/order_line.py` (329 lines)
- `saleor/order/tests/fixtures/order.py` (1156 lines)

## Interactions

- Imports from: `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....OrderEvents`
- `....OrderOrigin`
- `....OrderStatus`
- `....account.models.User`
- `....checkout.utils.get_prices_of_discounted_specific_product`
- `....core.JobStatus`
- `....core.prices.quantize_price`
- `....core.taxes.zero_money`
- `....discount.DiscountType`
- `....discount.DiscountValueType`
- `....discount.RewardType`
- `....discount.RewardValueType`
- `....discount.VoucherType`
- `....discount.interface.fetch_variant_rules_info`
- `....discount.models.NotApplicable`
- `....discount.models.Voucher`
- `....discount.models.VoucherCode`
- `....discount.utils.order.update_unit_discount_data_on_order_line`
- `....payment.ChargeStatus`
- `....payment.model_helpers.get_subtotal`
- `....payment.models.Payment`
- `....payment.models.Transaction`
- `....plugins.manager.get_plugins_manager`
- `....product.models.VariantChannelListingPromotionRule`
- `....tax.utils.calculate_tax_rate`
- `....tax.utils.get_tax_class_kwargs_for_order_line`
- `....warehouse.models.Allocation`
- `....warehouse.models.PreorderAllocation`
- `....warehouse.models.Stock`
- `....warehouse.models.Warehouse`
- `...actions.cancel_fulfillment`
- `...actions.fulfill_order_lines`
- `...base_calculations.base_order_subtotal`
- `...calculations.remove_tax`
- `...fetch.OrderLineInfo`
- `...models.Fulfillment`
- `...models.FulfillmentLine`
- `...models.FulfillmentStatus`
- `...models.Order`
- `...models.OrderEvent`
- `...models.OrderLine`
- `...search.prepare_order_search_vector_value`
- `...utils.get_voucher_discount_assigned_to_order`
- `.benchmark.*  # noqa: F403`
- `.draft_order.*  # noqa: F403`
- `.fulfillment.*  # noqa: F403`
- `.order.*  # noqa: F403`
- `.order_line.*  # noqa: F403`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `68c20f32afa5` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
