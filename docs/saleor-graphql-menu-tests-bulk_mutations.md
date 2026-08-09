## Purpose

`saleor/graphql/menu/tests/bulk_mutations` (`saleor/graphql/menu/tests/bulk_mutations`) groups 3 source file(s) exposing 6 top-level declaration(s).

## Public surface

**`saleor/graphql/menu/tests/bulk_mutations/test_menu_bulk_delete.py`**

- `menu_list` (function) — [saleor/graphql/menu/tests/bulk_mutations/test_menu_bulk_delete.py:11]
- `test_delete_menus` (function) — [saleor/graphql/menu/tests/bulk_mutations/test_menu_bulk_delete.py:27]
- `test_delete_menus_trigger_webhook` (function) — [saleor/graphql/menu/tests/bulk_mutations/test_menu_bulk_delete.py:51]

**`saleor/graphql/menu/tests/bulk_mutations/test_menu_item_bulk_delete.py`**

- `test_delete_menu_items` (function) — [saleor/graphql/menu/tests/bulk_mutations/test_menu_item_bulk_delete.py:17]
- `test_delete_menu_items_trigger_webhook` (function) — [saleor/graphql/menu/tests/bulk_mutations/test_menu_item_bulk_delete.py:45]
- `test_delete_empty_list_of_ids` (function) — [saleor/graphql/menu/tests/bulk_mutations/test_menu_item_bulk_delete.py:78]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/menu/tests/bulk_mutations/__init__.py` (1 lines)
- `saleor/graphql/menu/tests/bulk_mutations/test_menu_bulk_delete.py` (79 lines)
- `saleor/graphql/menu/tests/bulk_mutations/test_menu_item_bulk_delete.py` (97 lines)

## Interactions

- Imports from: `saleor/graphql/menu/bulk_mutations`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....menu.models.Menu`
- `.....menu.models.MenuItem`
- `....tests.utils.get_graphql_content`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `cff10ecb4853` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
