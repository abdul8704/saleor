## Purpose

`saleor/account/migrations/tasks` (`saleor/account/migrations/tasks`) groups 3 source file(s) exposing 2 top-level declaration(s).

## Public surface

**`saleor/account/migrations/tasks/saleor3_22.py`**

- `populate_user_number_of_orders_task` (function) — [saleor/account/migrations/tasks/saleor3_22.py:17]

**`saleor/account/migrations/tasks/saleor3_23.py`**

- `delete_digital_customer_events` (function) — [saleor/account/migrations/tasks/saleor3_23.py:20]

## How it works

The module's files, as provided to this run:

- `saleor/account/migrations/tasks/__init__.py` (1 lines)
- `saleor/account/migrations/tasks/saleor3_22.py` (53 lines)
- `saleor/account/migrations/tasks/saleor3_23.py` (59 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....celeryconf.app`
- `....core.db.connection.allow_writer`
- `....order.OrderStatus`
- `....order.models.Order`
- `...models.CustomerEvent`
- `...models.User`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `488f6db81682` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
