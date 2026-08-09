## Purpose

`saleor/tax/calculations` (`saleor/tax/calculations`) groups 3 source file(s) exposing 5 top-level declaration(s).

## Public surface

**`saleor/tax/calculations/__init__.py`**

- `calculate_flat_rate_tax` (function) — [saleor/tax/calculations/__init__.py:8]
- `get_taxed_undiscounted_price` (function) — [saleor/tax/calculations/__init__.py:25]

**`saleor/tax/calculations/checkout.py`**

- `update_checkout_prices_with_flat_rates` (function) — [saleor/tax/calculations/checkout.py:24]

**`saleor/tax/calculations/order.py`**

- `update_order_prices_with_flat_rates` (function) — [saleor/tax/calculations/order.py:26]
- `update_taxes_for_order_lines` (function) — [saleor/tax/calculations/order.py:125]

## How it works

The module's files, as provided to this run:

- `saleor/tax/calculations/__init__.py` (46 lines)
- `saleor/tax/calculations/checkout.py` (117 lines)
- `saleor/tax/calculations/order.py` (189 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...checkout.base_calculations`
- `...checkout.fetch.CheckoutInfo`
- `...checkout.fetch.CheckoutLineInfo`
- `...checkout.models.Checkout`
- `...core.prices.quantize_price`
- `...core.taxes.zero_taxed_money`
- `...order.base_calculations`
- `...order.models.Order`
- `...order.models.OrderLine`
- `...order.utils.get_order_country`
- `..calculate_flat_rate_tax`
- `..models.TaxClassCountryRate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `511483aec71b` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
