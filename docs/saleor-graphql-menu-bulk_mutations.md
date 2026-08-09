## Purpose

`saleor/graphql/menu/bulk_mutations` (`saleor/graphql/menu/bulk_mutations`) groups 3 source file(s) exposing 8 top-level declaration(s).

## Public surface

**`saleor/graphql/menu/bulk_mutations/menu_bulk_delete.py`**

- `MenuBulkDelete` (class) — [saleor/graphql/menu/bulk_mutations/menu_bulk_delete.py:16]
- `Arguments` (class) — [saleor/graphql/menu/bulk_mutations/menu_bulk_delete.py:17]
- `Meta` (class) — [saleor/graphql/menu/bulk_mutations/menu_bulk_delete.py:27]
- `bulk_action` (function) — [saleor/graphql/menu/bulk_mutations/menu_bulk_delete.py:43]

**`saleor/graphql/menu/bulk_mutations/menu_item_bulk_delete.py`**

- `MenuItemBulkDelete` (class) — [saleor/graphql/menu/bulk_mutations/menu_item_bulk_delete.py:16]
- `Arguments` (class) — [saleor/graphql/menu/bulk_mutations/menu_item_bulk_delete.py:17]
- `Meta` (class) — [saleor/graphql/menu/bulk_mutations/menu_item_bulk_delete.py:27]
- `bulk_action` (function) — [saleor/graphql/menu/bulk_mutations/menu_item_bulk_delete.py:43]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/menu/bulk_mutations/menu_bulk_delete.py` (49 lines)
- `saleor/graphql/menu/bulk_mutations/menu_item_bulk_delete.py` (49 lines)
- `saleor/graphql/menu/bulk_mutations/__init__.py` (7 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: `saleor/graphql/menu/tests/bulk_mutations`

Internal dependencies named in the source:

- `....menu.models`
- `....permission.enums.MenuPermissions`
- `....webhook.event_types.WebhookEventAsyncType`
- `....webhook.utils.get_webhooks_for_event`
- `...core.ResolveInfo`
- `...core.mutations.ModelBulkDeleteMutation`
- `...core.types.MenuError`
- `...core.types.NonNullList`
- `...core.utils.WebhookEventInfo`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `..types.Menu`
- `..types.MenuItem`
- `.menu_bulk_delete.MenuBulkDelete`
- `.menu_item_bulk_delete.MenuItemBulkDelete`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `904eca8e35df` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
