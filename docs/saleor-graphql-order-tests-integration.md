## Purpose

`saleor/graphql/order/tests/integration` (`saleor/graphql/order/tests/integration`) groups 4 source file(s) exposing 8 top-level declaration(s).

## Public surface

**`saleor/graphql/order/tests/integration/test_bulk_order.py`**

- `test_create_order_from_imported_draft_order` (function) — [saleor/graphql/order/tests/integration/test_bulk_order.py:32]
- `test_fulfill_imported_order` (function) — [saleor/graphql/order/tests/integration/test_bulk_order.py:78]
- `test_return_and_refund_imported_order` (function) — [saleor/graphql/order/tests/integration/test_bulk_order.py:140]
- `test_filter_imported_orders` (function) — [saleor/graphql/order/tests/integration/test_bulk_order.py:226]
- `test_refresh_order_prices_from_imported_draft_order_with_unit_discount` (function) — [saleor/graphql/order/tests/integration/test_bulk_order.py:310]

**`saleor/graphql/order/tests/integration/test_draft_order.py`**

- `test_create_order_by_staff_in_accessible_channel` (function) — [saleor/graphql/order/tests/integration/test_draft_order.py:18]
- `test_user_cannot_manage_draft_order_after_losing_access_to_channel` (function) — [saleor/graphql/order/tests/integration/test_draft_order.py:89]

**`saleor/graphql/order/tests/integration/test_order.py`**

- `test_user_cannot_manage_order_after_losing_access_to_channel` (function) — [saleor/graphql/order/tests/integration/test_order.py:13]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/order/tests/integration/__init__.py` (1 lines)
- `saleor/graphql/order/tests/integration/test_bulk_order.py` (410 lines)
- `saleor/graphql/order/tests/integration/test_draft_order.py` (158 lines)
- `saleor/graphql/order/tests/integration/test_order.py` (78 lines)

## Interactions

- Imports from: `saleor/order`, `saleor/payment`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....order.OrderStatus`
- `.....order.calculations.fetch_order_prices_if_expired`
- `.....plugins.manager.get_plugins_manager`
- `....discount.enums.DiscountValueTypeEnum`
- `....order.enums.OrderStatusEnum`
- `....payment.enums.TransactionActionEnum`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `...enums.StockUpdatePolicyEnum`
- `..mutations.test_draft_order_complete.DRAFT_ORDER_COMPLETE_MUTATION`
- `..mutations.test_draft_order_create.DRAFT_ORDER_CREATE_MUTATION`
- `..mutations.test_draft_order_update.DRAFT_ORDER_UPDATE_MUTATION`
- `..mutations.test_fulfillment_cancel.CANCEL_FULFILLMENT_MUTATION`
- `..mutations.test_fulfillment_return_products.ORDER_FULFILL_RETURN_MUTATION`
- `..mutations.test_order_fulfill.ORDER_FULFILL_MUTATION`
- `..mutations.test_order_lines_create.ORDER_LINES_CREATE_MUTATION`
- `..mutations.test_order_mark_as_paid.MARK_ORDER_AS_PAID_MUTATION`
- `..queries.test_order.QUERY_ORDER_BY_ID`
- `saleor.order.OrderEvents`
- `saleor.order.models.Order`
- `saleor.order.models.OrderLine`
- `saleor.payment.models.TransactionItem`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c251dca485f4` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
