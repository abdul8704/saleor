## Purpose

`saleor/graphql/menu/tests/mutations` (`saleor/graphql/menu/tests/mutations`) groups 9 source file(s) exposing 31 top-level declaration(s).

## Public surface

**`saleor/graphql/menu/tests/mutations/test_assign_navigation.py`**

- `test_assign_menu` (function) — [saleor/graphql/menu/tests/mutations/test_assign_navigation.py:7]

**`saleor/graphql/menu/tests/mutations/test_menu_create.py`**

- `test_validate_menu_item_instance` (function) — [saleor/graphql/menu/tests/mutations/test_menu_create.py:19]
- `test_create_menu` (function) — [saleor/graphql/menu/tests/mutations/test_menu_create.py:53]
- `test_create_menu_trigger_webhook` (function) — [saleor/graphql/menu/tests/mutations/test_menu_create.py:84]
- `test_create_menu_slug_already_exists` (function) — [saleor/graphql/menu/tests/mutations/test_menu_create.py:142]
- `test_create_menu_provided_slug` (function) — [saleor/graphql/menu/tests/mutations/test_menu_create.py:175]

**`saleor/graphql/menu/tests/mutations/test_menu_delete.py`**

- `test_delete_menu` (function) — [saleor/graphql/menu/tests/mutations/test_menu_delete.py:25]
- `test_delete_menu_trigger_webhook` (function) — [saleor/graphql/menu/tests/mutations/test_menu_delete.py:45]

**`saleor/graphql/menu/tests/mutations/test_menu_item_create.py`**

- `test_create_menu_item` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_create.py:29]
- `test_create_menu_item_trigger_webhook` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_create.py:52]

**`saleor/graphql/menu/tests/mutations/test_menu_item_delete.py`**

- `test_delete_menu_item` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_delete.py:25]
- `test_delete_menu_item_trigger_webhook` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_delete.py:46]

**`saleor/graphql/menu/tests/mutations/test_menu_item_move.py`**

- `test_menu_reorder` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_move.py:40]
- `test_menu_reorder_trigger_webhook` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_move.py:86]
- `test_menu_reorder_move_the_same_item_multiple_times` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_move.py:128]
- `test_menu_reorder_move_without_effect` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_move.py:174]
- `test_menu_reorder_assign_parent` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_move.py:219]
- `test_menu_reorder_assign_and_unassign_parent` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_move.py:293]
- `test_menu_reorder_unassign_and_assign_parent` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_move.py:369]
- `test_menu_reorder_assign_parent_to_top_level` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_move.py:447]
- `test_menu_reorder_cannot_assign_to_ancestor` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_move.py:504]
- `test_menu_reorder_cannot_assign_to_itself` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_move.py:548]
- `test_menu_cannot_get_menu_item_not_from_same_menu` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_move.py:571]
- `test_menu_cannot_pass_an_invalid_menu_item_node_type` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_move.py:601]

**`saleor/graphql/menu/tests/mutations/test_menu_item_update.py`**

- `test_update_menu_item` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_update.py:26]
- `test_update_menu_item_trigger_webhook` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_update.py:51]
- `test_add_more_than_one_item` (function) — [saleor/graphql/menu/tests/mutations/test_menu_item_update.py:103]

**`saleor/graphql/menu/tests/mutations/test_menu_update.py`**

- `test_update_menu` (function) — [saleor/graphql/menu/tests/mutations/test_menu_update.py:31]
- `test_update_menu_with_slug` (function) — [saleor/graphql/menu/tests/mutations/test_menu_update.py:61]
- `test_update_menu_trigger_webhook` (function) — [saleor/graphql/menu/tests/mutations/test_menu_update.py:84]
- `test_update_menu_with_slug_already_exists` (function) — [saleor/graphql/menu/tests/mutations/test_menu_update.py:133]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/menu/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/menu/tests/mutations/test_assign_navigation.py` (58 lines)
- `saleor/graphql/menu/tests/mutations/test_menu_create.py` (203 lines)
- `saleor/graphql/menu/tests/mutations/test_menu_delete.py` (87 lines)
- `saleor/graphql/menu/tests/mutations/test_menu_item_create.py` (98 lines)
- `saleor/graphql/menu/tests/mutations/test_menu_item_delete.py` (89 lines)
- `saleor/graphql/menu/tests/mutations/test_menu_item_move.py` (630 lines)
- `saleor/graphql/menu/tests/mutations/test_menu_item_update.py` (134 lines)
- `saleor/graphql/menu/tests/mutations/test_menu_update.py` (153 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....core.utils.json_serializer.CustomJsonEncoder`
- `.....menu.error_codes.MenuErrorCode`
- `.....menu.models.Menu`
- `.....menu.models.MenuItem`
- `.....product.models.Category`
- `.....webhook.event_types.WebhookEventAsyncType`
- `.....webhook.payloads.generate_meta`
- `.....webhook.payloads.generate_requestor`
- `....menu.enums.NavigationType`
- `....menu.mutations.menu_item_create._validate_menu_item_instance`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `965b11d0745d` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
