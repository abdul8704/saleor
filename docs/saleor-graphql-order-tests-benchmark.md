## Purpose

`saleor/graphql/order/tests/benchmark` (`saleor/graphql/order/tests/benchmark`) groups 8 source file(s) exposing 13 top-level declaration(s).

## Public surface

**`saleor/graphql/order/tests/benchmark/test_draft_order_update.py`**

- `test_draft_order_update` (function) — [saleor/graphql/order/tests/benchmark/test_draft_order_update.py:32]

**`saleor/graphql/order/tests/benchmark/test_fulfillment_refund_and_return_products.py`**

- `test_fulfillment_refund_products_order_lines` (function) — [saleor/graphql/order/tests/benchmark/test_fulfillment_refund_and_return_products.py:14]
- `test_fulfillment_return_products_order_lines` (function) — [saleor/graphql/order/tests/benchmark/test_fulfillment_refund_and_return_products.py:75]

**`saleor/graphql/order/tests/benchmark/test_fulfillment.py`**

- `test_fulfillment_query` (function) — [saleor/graphql/order/tests/benchmark/test_fulfillment.py:34]

**`saleor/graphql/order/tests/benchmark/test_order_bulk_create.py`**

- `test_order_bulk_create` (function) — [saleor/graphql/order/tests/benchmark/test_order_bulk_create.py:18]

**`saleor/graphql/order/tests/benchmark/test_order_fulfill.py`**

- `test_order_fulfill` (function) — [saleor/graphql/order/tests/benchmark/test_order_fulfill.py:30]
- `test_order_fulfill_with_gift_cards` (function) — [saleor/graphql/order/tests/benchmark/test_order_fulfill.py:71]

**`saleor/graphql/order/tests/benchmark/test_order_lines_create.py`**

- `test_order_lines_create` (function) — [saleor/graphql/order/tests/benchmark/test_order_lines_create.py:40]
- `test_order_lines_create_variants_on_promotion` (function) — [saleor/graphql/order/tests/benchmark/test_order_lines_create.py:76]

**`saleor/graphql/order/tests/benchmark/test_order.py`**

- `test_user_order_details` (function) — [saleor/graphql/order/tests/benchmark/test_order.py:119]
- `test_staff_order_details` (function) — [saleor/graphql/order/tests/benchmark/test_order.py:185]
- `test_staff_multiple_orders` (function) — [saleor/graphql/order/tests/benchmark/test_order.py:226]
- `test_staff_multiple_draft_orders` (function) — [saleor/graphql/order/tests/benchmark/test_order.py:260]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/order/tests/benchmark/__init__.py` (1 lines)
- `saleor/graphql/order/tests/benchmark/test_draft_order_update.py` (100 lines)
- `saleor/graphql/order/tests/benchmark/test_fulfillment_refund_and_return_products.py` (176 lines)
- `saleor/graphql/order/tests/benchmark/test_fulfillment.py` (46 lines)
- `saleor/graphql/order/tests/benchmark/test_order_bulk_create.py` (89 lines)
- `saleor/graphql/order/tests/benchmark/test_order_fulfill.py` (116 lines)
- `saleor/graphql/order/tests/benchmark/test_order_lines_create.py` (143 lines)
- `saleor/graphql/order/tests/benchmark/test_order.py` (273 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....discount.RewardValueType`
- `.....order.OrderStatus`
- `.....payment.ChargeStatus`
- `.....warehouse.models.Stock`
- `....core.enums.LanguageCodeEnum`
- `....discount.enums.DiscountValueTypeEnum`
- `....tests.utils.get_graphql_content`
- `..mutations.test_order_bulk_create.# noqa: F401`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `ef6b330db3af` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
