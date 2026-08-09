## Purpose

`saleor/graphql/order/tests/deprecated` (`saleor/graphql/order/tests/deprecated`) groups 3 source file(s) exposing 11 top-level declaration(s).

## Public surface

**`saleor/graphql/order/tests/deprecated/test_discount_order.py`**

- `test_delete_order_discount_from_order_with_old_id` (function) — [saleor/graphql/order/tests/deprecated/test_discount_order.py:38]
- `test_update_percentage_order_discount_by_old_id` (function) — [saleor/graphql/order/tests/deprecated/test_discount_order.py:115]

**`saleor/graphql/order/tests/deprecated/test_order.py`**

- `assert_proper_webhook_called_once` (function) — [saleor/graphql/order/tests/deprecated/test_order.py:25]
- `test_orders_total` (function) — [saleor/graphql/order/tests/deprecated/test_order.py:50]
- `test_order_line_remove_by_old_line_id` (function) — [saleor/graphql/order/tests/deprecated/test_order.py:96]
- `test_order_line_update_by_old_line_id` (function) — [saleor/graphql/order/tests/deprecated/test_order.py:154]
- `test_order_fulfill_old_line_id` (function) — [saleor/graphql/order/tests/deprecated/test_order.py:226]
- `test_fulfillment_refund_products_order_lines_by_old_id` (function) — [saleor/graphql/order/tests/deprecated/test_order.py:323]
- `test_fulfillment_return_products_order_lines_by_old_line_id` (function) — [saleor/graphql/order/tests/deprecated/test_order.py:432]
- `test_update_order_line_discount_old_id` (function) — [saleor/graphql/order/tests/deprecated/test_order.py:580]
- `test_delete_discount_from_order_line_by_old_id` (function) — [saleor/graphql/order/tests/deprecated/test_order.py:695]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/order/tests/deprecated/__init__.py` (1 lines)
- `saleor/graphql/order/tests/deprecated/test_discount_order.py` (182 lines)
- `saleor/graphql/order/tests/deprecated/test_order.py` (755 lines)

## Interactions

- Imports from: `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....channel.utils.DEPRECATION_WARNING_MESSAGE`
- `.....core.prices.quantize_price`
- `.....discount.DiscountValueType`
- `.....order.OrderEvents`
- `.....order.OrderOrigin`
- `.....order.OrderStatus`
- `.....order.events`
- `.....order.fetch.OrderLineInfo`
- `.....order.interface.OrderTaxedPricesData`
- `.....order.models.FulfillmentStatus`
- `.....order.models.Order`
- `.....order.models.OrderEvent`
- `.....order.models.OrderLine`
- `.....payment.ChargeStatus`
- `.....payment.interface.RefundData`
- `....core.enums.ReportingPeriod`
- `....discount.enums.DiscountValueTypeEnum`
- `....tests.utils.get_graphql_content`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `cbf0ae93ca91` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
