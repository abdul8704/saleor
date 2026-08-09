## Purpose

`saleor/graphql/menu/tests/queries` (`saleor/graphql/menu/tests/queries`) groups 7 source file(s) exposing 29 top-level declaration(s).

## Public surface

**`saleor/graphql/menu/tests/queries/test_menu_item.py`**

- `test_menu_item_query` (function) — [saleor/graphql/menu/tests/queries/test_menu_item.py:28]
- `test_menu_item_query_with_invalid_channel` (function) — [saleor/graphql/menu/tests/queries/test_menu_item.py:52]
- `test_staff_query_menu_item_by_invalid_id` (function) — [saleor/graphql/menu/tests/queries/test_menu_item.py:78]
- `test_staff_query_menu_item_with_invalid_object_type` (function) — [saleor/graphql/menu/tests/queries/test_menu_item.py:88]
- `test_menu_items_collection_in_other_channel` (function) — [saleor/graphql/menu/tests/queries/test_menu_item.py:95]
- `test_menu_item_query_static_url` (function) — [saleor/graphql/menu/tests/queries/test_menu_item.py:160]
- `test_menu_item_query_staff_with_permission_gets_all_pages` (function) — [saleor/graphql/menu/tests/queries/test_menu_item.py:179]
- `test_menu_item_query_staff_without_permission_gets_only_published_pages` (function) — [saleor/graphql/menu/tests/queries/test_menu_item.py:204]

**`saleor/graphql/menu/tests/queries/test_menu_items.py`**

- `menu_items_for_pagination` (function) — [saleor/graphql/menu/tests/queries/test_menu_items.py:8]
- `test_menu_items_pagination_with_sorting` (function) — [saleor/graphql/menu/tests/queries/test_menu_items.py:57]
- `test_menu_items_pagination_with_filtering` (function) — [saleor/graphql/menu/tests/queries/test_menu_items.py:90]

**`saleor/graphql/menu/tests/queries/test_menu.py`**

- `test_menu_query_by_id` (function) — [saleor/graphql/menu/tests/queries/test_menu.py:23]
- `test_staff_query_menu_by_invalid_id` (function) — [saleor/graphql/menu/tests/queries/test_menu.py:40]
- `test_staff_query_menu_with_invalid_object_type` (function) — [saleor/graphql/menu/tests/queries/test_menu.py:55]
- `test_menu_query_by_name` (function) — [saleor/graphql/menu/tests/queries/test_menu.py:67]
- `test_menu_query_by_slug` (function) — [saleor/graphql/menu/tests/queries/test_menu.py:84]
- `test_menu_query_error_when_id_and_name_provided` (function) — [saleor/graphql/menu/tests/queries/test_menu.py:100]
- `test_menu_query_error_when_no_param` (function) — [saleor/graphql/menu/tests/queries/test_menu.py:125]
- `test_menu_query` (function) — [saleor/graphql/menu/tests/queries/test_menu.py:146]
- `test_menu_items_query` (function) — [saleor/graphql/menu/tests/queries/test_menu.py:175]

**`saleor/graphql/menu/tests/queries/test_menus_filtering.py`**

- `test_menus_query_with_filter` (function) — [saleor/graphql/menu/tests/queries/test_menus_filtering.py:31]
- `test_menus_query_with_slug_filter` (function) — [saleor/graphql/menu/tests/queries/test_menus_filtering.py:48]
- `test_menus_query_with_slug_list_filter` (function) — [saleor/graphql/menu/tests/queries/test_menus_filtering.py:65]
- `test_menu_items_query_with_filter` (function) — [saleor/graphql/menu/tests/queries/test_menus_filtering.py:89]

**`saleor/graphql/menu/tests/queries/test_menus_sorting.py`**

- `test_query_menus_with_sort` (function) — [saleor/graphql/menu/tests/queries/test_menus_sorting.py:29]
- `test_query_menu_items_with_sort` (function) — [saleor/graphql/menu/tests/queries/test_menus_sorting.py:72]

**`saleor/graphql/menu/tests/queries/test_menus.py`**

- `menus_for_pagination` (function) — [saleor/graphql/menu/tests/queries/test_menus.py:8]
- `test_menus_pagination_with_sorting` (function) — [saleor/graphql/menu/tests/queries/test_menus.py:53]
- `test_menus_pagination_with_filtering` (function) — [saleor/graphql/menu/tests/queries/test_menus.py:86]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/menu/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/menu/tests/queries/test_menu_item.py` (225 lines)
- `saleor/graphql/menu/tests/queries/test_menu_items.py` (112 lines)
- `saleor/graphql/menu/tests/queries/test_menu.py` (222 lines)
- `saleor/graphql/menu/tests/queries/test_menus_filtering.py` (117 lines)
- `saleor/graphql/menu/tests/queries/test_menus_sorting.py` (90 lines)
- `saleor/graphql/menu/tests/queries/test_menus.py` (108 lines)

## Interactions

- Imports from: `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....menu.models.Menu`
- `.....menu.models.MenuItem`
- `....tests.utils.get_graphql_content`
- `....tests.utils.get_graphql_content_from_response`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `d4588c3f4e14` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
