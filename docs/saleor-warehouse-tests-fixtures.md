## Purpose

`saleor/warehouse/tests/fixtures` (`saleor/warehouse/tests/fixtures`) groups 5 source file(s) exposing 14 top-level declaration(s).

## Public surface

**`saleor/warehouse/tests/fixtures/allocation.py`**

- `allocation` (function) — [saleor/warehouse/tests/fixtures/allocation.py:14]
- `allocations` (function) — [saleor/warehouse/tests/fixtures/allocation.py:21]

**`saleor/warehouse/tests/fixtures/preorder_allocation.py`**

- `preorder_allocation` (function) — [saleor/warehouse/tests/fixtures/preorder_allocation.py:7]

**`saleor/warehouse/tests/fixtures/stock.py`**

- `stock` (function) — [saleor/warehouse/tests/fixtures/stock.py:7]
- `stocks_for_cc` (function) — [saleor/warehouse/tests/fixtures/stock.py:14]

**`saleor/warehouse/tests/fixtures/warehouse.py`**

- `warehouse` (function) — [saleor/warehouse/tests/fixtures/warehouse.py:8]
- `warehouse_with_external_ref` (function) — [saleor/warehouse/tests/fixtures/warehouse.py:21]
- `warehouse_JPY` (function) — [saleor/warehouse/tests/fixtures/warehouse.py:35]
- `warehouses` (function) — [saleor/warehouse/tests/fixtures/warehouse.py:48]
- `warehouses_for_cc` (function) — [saleor/warehouse/tests/fixtures/warehouse.py:73]
- `warehouse_for_cc` (function) — [saleor/warehouse/tests/fixtures/warehouse.py:114]
- `warehouses_with_shipping_zone` (function) — [saleor/warehouse/tests/fixtures/warehouse.py:142]
- `warehouses_with_different_shipping_zone` (function) — [saleor/warehouse/tests/fixtures/warehouse.py:149]
- `warehouse_no_shipping_zone` (function) — [saleor/warehouse/tests/fixtures/warehouse.py:156]

## How it works

The module's files, as provided to this run:

- `saleor/warehouse/tests/fixtures/__init__.py` (4 lines)
- `saleor/warehouse/tests/fixtures/allocation.py` (96 lines)
- `saleor/warehouse/tests/fixtures/preorder_allocation.py` (16 lines)
- `saleor/warehouse/tests/fixtures/stock.py` (63 lines)
- `saleor/warehouse/tests/fixtures/warehouse.py` (165 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....WarehouseClickAndCollectOption`
- `....core.postgres.FlatConcatSearchVector`
- `....core.prices.Money`
- `....core.prices.TaxedMoney`
- `....order.models.Order`
- `....order.models.OrderLine`
- `....order.search.prepare_order_search_vector_value`
- `....tax.utils.get_tax_class_kwargs_for_order_line`
- `...models.Allocation`
- `...models.PreorderAllocation`
- `...models.Stock`
- `...models.Warehouse`
- `.allocation.*  # noqa: F403`
- `.preorder_allocation.*  # noqa: F403`
- `.stock.*  # noqa: F403`
- `.warehouse.*  # noqa: F403`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `29197de27d8c` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
