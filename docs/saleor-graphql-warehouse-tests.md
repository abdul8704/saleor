## Purpose

`saleor/graphql/warehouse/tests` (`saleor/graphql/warehouse/tests`) groups 3 source file(s) exposing 11 top-level declaration(s).

## Public surface

**`saleor/graphql/warehouse/tests/bulk_mutations/test_stock_bulk_update.py`**

- `test_stocks_bulk_update_using_ids` (function) — [saleor/graphql/warehouse/tests/bulk_mutations/test_stock_bulk_update.py:28]
- `test_stocks_bulk_update_send_stock_updated_event` (function) — [saleor/graphql/warehouse/tests/bulk_mutations/test_stock_bulk_update.py:86]
- `test_stocks_bulk_update_send_stock_updated_event_only_for_changed_stocks` (function) — [saleor/graphql/warehouse/tests/bulk_mutations/test_stock_bulk_update.py:135]
- `test_stocks_bulk_update_using_external_refs` (function) — [saleor/graphql/warehouse/tests/bulk_mutations/test_stock_bulk_update.py:190]
- `test_stocks_bulk_update_using_variant_id_and_warehouse_external_ref` (function) — [saleor/graphql/warehouse/tests/bulk_mutations/test_stock_bulk_update.py:241]
- `test_stocks_bulk_update_using_variant_external_ref_and_warehouse_id` (function) — [saleor/graphql/warehouse/tests/bulk_mutations/test_stock_bulk_update.py:292]
- `test_stocks_bulk_update_when_no_variant_args_provided` (function) — [saleor/graphql/warehouse/tests/bulk_mutations/test_stock_bulk_update.py:344]
- `test_stocks_bulk_update_when_invalid_variant_id_provided` (function) — [saleor/graphql/warehouse/tests/bulk_mutations/test_stock_bulk_update.py:377]
- `test_stocks_bulk_update_when_no_warehouse_args_provided` (function) — [saleor/graphql/warehouse/tests/bulk_mutations/test_stock_bulk_update.py:407]
- `test_stocks_bulk_update_when_invalid_warehouse_id_provided` (function) — [saleor/graphql/warehouse/tests/bulk_mutations/test_stock_bulk_update.py:438]
- `test_stocks_bulk_update_when_stock_not_exists` (function) — [saleor/graphql/warehouse/tests/bulk_mutations/test_stock_bulk_update.py:466]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/warehouse/tests/__init__.py` (1 lines)
- `saleor/graphql/warehouse/tests/bulk_mutations/__init__.py` (1 lines)
- `saleor/graphql/warehouse/tests/bulk_mutations/test_stock_bulk_update.py` (493 lines)

## Interactions

- Imports from: `saleor/graphql/warehouse`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....warehouse.error_codes.StockBulkUpdateErrorCode`
- `....tests.utils.get_graphql_content`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `0186de76b610` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
