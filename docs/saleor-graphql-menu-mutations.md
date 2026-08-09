## Purpose

`saleor/graphql/menu/mutations` (`saleor/graphql/menu/mutations`) groups 9 source file(s) exposing 50 top-level declaration(s).

## Public surface

**`saleor/graphql/menu/mutations/assign_navigation.py`**

- `AssignNavigation` (class) — [saleor/graphql/menu/mutations/assign_navigation.py:14]
- `Arguments` (class) — [saleor/graphql/menu/mutations/assign_navigation.py:17]
- `Meta` (class) — [saleor/graphql/menu/mutations/assign_navigation.py:24]
- `perform_mutation` (function) — [saleor/graphql/menu/mutations/assign_navigation.py:32]

**`saleor/graphql/menu/mutations/menu_create.py`**

- `MenuCreateInput` (class) — [saleor/graphql/menu/mutations/menu_create.py:21]
- `MenuCreate` (class) — [saleor/graphql/menu/mutations/menu_create.py:30]
- `Arguments` (class) — [saleor/graphql/menu/mutations/menu_create.py:31]
- `Meta` (class) — [saleor/graphql/menu/mutations/menu_create.py:36]
- `clean_input` (function) — [saleor/graphql/menu/mutations/menu_create.py:51]
- `post_save_action` (function) — [saleor/graphql/menu/mutations/menu_create.py:111]
- `success_response` (function) — [saleor/graphql/menu/mutations/menu_create.py:116]

**`saleor/graphql/menu/mutations/menu_delete.py`**

- `MenuDelete` (class) — [saleor/graphql/menu/mutations/menu_delete.py:15]
- `Arguments` (class) — [saleor/graphql/menu/mutations/menu_delete.py:16]
- `Meta` (class) — [saleor/graphql/menu/mutations/menu_delete.py:19]
- `post_save_action` (function) — [saleor/graphql/menu/mutations/menu_delete.py:34]
- `success_response` (function) — [saleor/graphql/menu/mutations/menu_delete.py:39]

**`saleor/graphql/menu/mutations/menu_item_create.py`**

- `MenuItemInput` (class) — [saleor/graphql/menu/mutations/menu_item_create.py:20]
- `MenuItemCreateInput` (class) — [saleor/graphql/menu/mutations/menu_item_create.py:32]
- `MenuItemCreate` (class) — [saleor/graphql/menu/mutations/menu_item_create.py:43]
- `Arguments` (class) — [saleor/graphql/menu/mutations/menu_item_create.py:44]
- `Meta` (class) — [saleor/graphql/menu/mutations/menu_item_create.py:53]
- `post_save_action` (function) — [saleor/graphql/menu/mutations/menu_item_create.py:68]
- `success_response` (function) — [saleor/graphql/menu/mutations/menu_item_create.py:73]
- `clean_input` (function) — [saleor/graphql/menu/mutations/menu_item_create.py:78]

**`saleor/graphql/menu/mutations/menu_item_delete.py`**

- `MenuItemDelete` (class) — [saleor/graphql/menu/mutations/menu_item_delete.py:15]
- `Arguments` (class) — [saleor/graphql/menu/mutations/menu_item_delete.py:16]
- `Meta` (class) — [saleor/graphql/menu/mutations/menu_item_delete.py:19]
- `post_save_action` (function) — [saleor/graphql/menu/mutations/menu_item_delete.py:34]
- `success_response` (function) — [saleor/graphql/menu/mutations/menu_item_delete.py:39]

**`saleor/graphql/menu/mutations/menu_item_move.py`**

- `MenuItemMove` (class) — [saleor/graphql/menu/mutations/menu_item_move.py:31]
- `Arguments` (class) — [saleor/graphql/menu/mutations/menu_item_move.py:34]
- `Meta` (class) — [saleor/graphql/menu/mutations/menu_item_move.py:40]
- `success_response` (function) — [saleor/graphql/menu/mutations/menu_item_move.py:57]
- `clean_move` (function) — [saleor/graphql/menu/mutations/menu_item_move.py:62]
- `clean_operation` (function) — [saleor/graphql/menu/mutations/menu_item_move.py:76]
- `get_operation` (function) — [saleor/graphql/menu/mutations/menu_item_move.py:94]
- `clean_moves` (function) — [saleor/graphql/menu/mutations/menu_item_move.py:138]
- `perform_change_parent_operation` (function) — [saleor/graphql/menu/mutations/menu_item_move.py:156]
- `perform_mutation` (function) — [saleor/graphql/menu/mutations/menu_item_move.py:176]

**`saleor/graphql/menu/mutations/menu_item_update.py`**

- `MenuItemUpdate` (class) — [saleor/graphql/menu/mutations/menu_item_update.py:14]
- `Arguments` (class) — [saleor/graphql/menu/mutations/menu_item_update.py:15]
- `Meta` (class) — [saleor/graphql/menu/mutations/menu_item_update.py:25]
- `construct_instance` (function) — [saleor/graphql/menu/mutations/menu_item_update.py:40]
- `post_save_action` (function) — [saleor/graphql/menu/mutations/menu_item_update.py:49]

**`saleor/graphql/menu/mutations/menu_update.py`**

- `MenuInput` (class) — [saleor/graphql/menu/mutations/menu_update.py:15]
- `MenuUpdate` (class) — [saleor/graphql/menu/mutations/menu_update.py:20]
- `Arguments` (class) — [saleor/graphql/menu/mutations/menu_update.py:21]
- `Meta` (class) — [saleor/graphql/menu/mutations/menu_update.py:27]
- `post_save_action` (function) — [saleor/graphql/menu/mutations/menu_update.py:42]
- `success_response` (function) — [saleor/graphql/menu/mutations/menu_update.py:47]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/menu/mutations/__init__.py` (19 lines)
- `saleor/graphql/menu/mutations/assign_navigation.py` (48 lines)
- `saleor/graphql/menu/mutations/menu_create.py` (118 lines)
- `saleor/graphql/menu/mutations/menu_delete.py` (41 lines)
- `saleor/graphql/menu/mutations/menu_item_create.py` (119 lines)
- `saleor/graphql/menu/mutations/menu_item_delete.py` (41 lines)
- `saleor/graphql/menu/mutations/menu_item_move.py` (201 lines)
- `saleor/graphql/menu/mutations/menu_item_update.py` (51 lines)
- `saleor/graphql/menu/mutations/menu_update.py` (49 lines)

## Interactions

- Imports from: `saleor/plugins/openid_connect`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....core.tracing.traced_atomic_transaction`
- `....menu.error_codes.MenuErrorCode`
- `....menu.models`
- `....page.models`
- `....permission.enums.MenuPermissions`
- `....permission.enums.SitePermissions`
- `....product.models`
- `....webhook.event_types.WebhookEventAsyncType`
- `...core.ResolveInfo`
- `...core.context.ChannelContext`
- `...core.doc_category.DOC_CATEGORY_MENU`
- `...core.mutations.BaseMutation`
- `...core.mutations.DeprecatedModelMutation`
- `...core.mutations.ModelDeleteMutation`
- `...core.types.MenuError`
- `...core.types.NonNullList`
- `...core.utils.WebhookEventInfo`
- `...core.utils.reordering.perform_reordering`
- `...core.validators.validate_slug_and_generate_if_needed`
- `...page.types.Page`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `...product.types.Category`
- `...product.types.Collection`
- `...site.dataloaders.get_site_promise`
- `..dataloaders.MenuItemsByParentMenuLoader`
- `..enums.NavigationType`
- `..types.Menu`
- `..types.MenuItem`
- `..types.MenuItemMoveInput`
- `.assign_navigation.AssignNavigation`
- `.menu_create.MenuCreate`
- `.menu_delete.MenuDelete`
- `.menu_item_create.MenuItemCreate`
- `.menu_item_create.MenuItemInput`
- `.menu_item_delete.MenuItemDelete`
- `.menu_item_move.MenuItemMove`
- `.menu_item_update.MenuItemUpdate`
- `.menu_update.MenuUpdate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `36c581059e0d` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
