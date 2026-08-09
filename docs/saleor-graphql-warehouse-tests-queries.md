## Purpose

`saleor/graphql/warehouse/tests/queries` (`saleor/graphql/warehouse/tests/queries`) groups 8 source file(s) exposing 42 top-level declaration(s).

## Public surface

**`saleor/graphql/warehouse/tests/queries/test_stock.py`**

- `test_query_stock_requires_permission` (function) — [saleor/graphql/warehouse/tests/queries/test_stock.py:34]
- `test_query_stock` (function) — [saleor/graphql/warehouse/tests/queries/test_stock.py:46]
- `test_query_stock_use_denormalized_quantity_allocated` (function) — [saleor/graphql/warehouse/tests/queries/test_stock.py:67]
- `test_query_stock_with_reservations` (function) — [saleor/graphql/warehouse/tests/queries/test_stock.py:87]
- `test_query_stock_with_expired_reservations` (function) — [saleor/graphql/warehouse/tests/queries/test_stock.py:114]
- `test_staff_query_stock_by_invalid_id` (function) — [saleor/graphql/warehouse/tests/queries/test_stock.py:144]
- `test_staff_query_stock_with_invalid_object_type` (function) — [saleor/graphql/warehouse/tests/queries/test_stock.py:163]

**`saleor/graphql/warehouse/tests/queries/test_stocks_filtering.py`**

- `test_query_stocks_with_filters_quantity` (function) — [saleor/graphql/warehouse/tests/queries/test_stocks_filtering.py:18]
- `test_query_stocks_with_filters_warehouse` (function) — [saleor/graphql/warehouse/tests/queries/test_stocks_filtering.py:46]
- `test_query_stocks_with_filters_product_variant` (function) — [saleor/graphql/warehouse/tests/queries/test_stocks_filtering.py:64]
- `test_query_stocks_with_filters_product_variant__product` (function) — [saleor/graphql/warehouse/tests/queries/test_stocks_filtering.py:86]

**`saleor/graphql/warehouse/tests/queries/test_stocks.py`**

- `test_query_stocks_requires_permissions` (function) — [saleor/graphql/warehouse/tests/queries/test_stocks.py:30]
- `test_query_stocks` (function) — [saleor/graphql/warehouse/tests/queries/test_stocks.py:41]

**`saleor/graphql/warehouse/tests/queries/test_warehouse.py`**

- `test_warehouse_query` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouse.py:46]
- `test_warehouse_query_as_staff_with_manage_orders` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouse.py:83]
- `test_warehouse_query_as_staff_with_manage_shipping` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouse.py:151]
- `test_warehouse_query_as_staff_with_manage_shipping_no_access_to_stocks` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouse.py:184]
- `test_warehouse_query_as_staff_with_manage_apps` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouse.py:201]
- `test_warehouse_query_as_customer` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouse.py:218]
- `test_staff_query_warehouse_by_invalid_id` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouse.py:232]
- `test_staff_query_warehouse_with_invalid_object_type` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouse.py:251]
- `test_warehouse_query_by_external_reference` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouse.py:275]

**`saleor/graphql/warehouse/tests/queries/test_warehouses_filtering.py`**

- `test_query_warehouses_with_filters_name` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses_filtering.py:44]
- `test_query_warehouse_with_filters_email` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses_filtering.py:71]
- `test_query_warehouse_with_filters_by_ids` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses_filtering.py:99]
- `test_query_warehouse_with_filters_by_id` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses_filtering.py:125]
- `test_query_warehouse_with_filters_by_is_private` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses_filtering.py:150]
- `test_query_warehouse_with_filters_by_click_and_collect_option` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses_filtering.py:182]
- `test_query_warehouses_with_filters_and_no_id` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses_filtering.py:205]
- `test_query_warehouses_with_filters_by_channels` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses_filtering.py:233]
- `test_query_warehouses_with_filters_by_channels_no_warehouse_returned` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses_filtering.py:268]
- `test_query_warehouses_with_filtering` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses_filtering.py:296]
- `test_query_warehouses_with_filters_metadata` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses_filtering.py:315]

**`saleor/graphql/warehouse/tests/queries/test_warehouses_pagination.py`**

- `warehouses_for_pagination` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses_pagination.py:9]
- `test_warehouses_pagination_with_sorting` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses_pagination.py:79]
- `test_warehouses_pagination_with_filtering` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses_pagination.py:115]
- `test_warehouses_pagination_with_filtering_by_id` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses_pagination.py:140]

**`saleor/graphql/warehouse/tests/queries/test_warehouses.py`**

- `test_query_warehouses_as_staff_with_manage_orders` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses.py:41]
- `test_query_warehouses_as_staff_with_manage_shipping` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses.py:63]
- `test_query_warehouses_as_staff_with_manage_apps` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses.py:85]
- `test_query_warehouses_as_customer` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses.py:97]
- `test_query_warehouses` (function) — [saleor/graphql/warehouse/tests/queries/test_warehouses.py:107]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/warehouse/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/warehouse/tests/queries/test_stock.py` (176 lines)
- `saleor/graphql/warehouse/tests/queries/test_stocks_filtering.py` (104 lines)
- `saleor/graphql/warehouse/tests/queries/test_stocks.py` (51 lines)
- `saleor/graphql/warehouse/tests/queries/test_warehouse.py` (295 lines)
- `saleor/graphql/warehouse/tests/queries/test_warehouses_filtering.py` (336 lines)
- `saleor/graphql/warehouse/tests/queries/test_warehouses_pagination.py` (166 lines)
- `saleor/graphql/warehouse/tests/queries/test_warehouses.py` (124 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....permission.enums.ProductPermissions`
- `.....warehouse.WarehouseClickAndCollectOption`
- `.....warehouse.models.Reservation`
- `.....warehouse.models.Stock`
- `.....warehouse.models.Warehouse`
- `.....warehouse.tests.utils.get_quantity_allocated_for_stock`
- `....core.utils.from_global_id_or_error`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `b5d697bb0532` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
