## Purpose

`saleor/checkout/migrations/tasks` (`saleor/checkout/migrations/tasks`) groups 4 source file(s) exposing 3 top-level declaration(s).

## Public surface

**`saleor/checkout/migrations/tasks/saleor3_20.py`**

- `clean_duplicated_gift_lines_task` (function) — [saleor/checkout/migrations/tasks/saleor3_20.py:18]

**`saleor/checkout/migrations/tasks/saleor3_21.py`**

- `fix_shared_address_instances_task` (function) — [saleor/checkout/migrations/tasks/saleor3_21.py:22]

**`saleor/checkout/migrations/tasks/saleor3_23.py`**

- `propagate_checkout_deliveries_task` (function) — [saleor/checkout/migrations/tasks/saleor3_23.py:20]

## How it works

The module's files, as provided to this run:

- `saleor/checkout/migrations/tasks/__init__.py` (1 lines)
- `saleor/checkout/migrations/tasks/saleor3_20.py` (61 lines)
- `saleor/checkout/migrations/tasks/saleor3_21.py` (59 lines)
- `saleor/checkout/migrations/tasks/saleor3_23.py` (103 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....account.models.Address`
- `....celeryconf.app`
- `....checkout.lock_objects.checkout_qs_select_for_update`
- `....checkout.models.Checkout`
- `....core.db.connection.allow_writer`
- `....discount.DiscountType`
- `....discount.models.CheckoutLineDiscount`
- `....order.models.Order`
- `....shipping.models.ShippingMethod`
- `....tax.models.TaxClass`
- `...lock_objects.checkout_lines_qs_select_for_update`
- `...lock_objects.checkout_qs_select_for_update`
- `...models.Checkout`
- `...models.CheckoutDelivery`
- `...models.CheckoutLine`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `ef098e113fba` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
