## Purpose

`saleor/order/migrations/tasks` (`saleor/order/migrations/tasks`) groups 3 source file(s) exposing 3 top-level declaration(s).

## Public surface

**`saleor/order/migrations/tasks/saleor3_20.py`**

- `clean_duplicated_gift_lines_task` (function) — [saleor/order/migrations/tasks/saleor3_20.py:14]

**`saleor/order/migrations/tasks/saleor3_22.py`**

- `populate_order_line_product_type_id_task` (function) — [saleor/order/migrations/tasks/saleor3_22.py:14]

**`saleor/order/migrations/tasks/saleor3_23.py`**

- `delete_digital_order_events` (function) — [saleor/order/migrations/tasks/saleor3_23.py:20]

## How it works

The module's files, as provided to this run:

- `saleor/order/migrations/tasks/saleor3_20.py` (49 lines)
- `saleor/order/migrations/tasks/saleor3_22.py` (56 lines)
- `saleor/order/migrations/tasks/saleor3_23.py` (61 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....celeryconf.app`
- `....core.db.connection.allow_writer`
- `....product.models.Product`
- `....product.models.ProductVariant`
- `...models.Order`
- `...models.OrderEvent`
- `...models.OrderLine`
- `...models.OrderStatus`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `25a269529b26` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
