## Purpose

`saleor/product/management` (`saleor/product/management`) groups 3 source file(s) exposing 3 top-level declaration(s).

## Public surface

**`saleor/product/management/commands/update_all_products_discounted_prices.py`**

- `Command` (class) — [saleor/product/management/commands/update_all_products_discounted_prices.py:13]
- `handle` (function) — [saleor/product/management/commands/update_all_products_discounted_prices.py:16]
- `queryset_in_batches` (function) — [saleor/product/management/commands/update_all_products_discounted_prices.py:26]

## How it works

The module's files, as provided to this run:

- `saleor/product/management/__init__.py` (1 lines)
- `saleor/product/management/commands/__init__.py` (1 lines)
- `saleor/product/management/commands/update_all_products_discounted_prices.py` (42 lines)

## Interactions

- Imports from: `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...models.Product`
- `...utils.variant_prices.update_discounted_prices_for_promotion`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `90f9fe375fe3` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
