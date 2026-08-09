## Purpose

`saleor/graphql/menu` (`saleor/graphql/menu`) groups 8 source file(s) exposing 59 top-level declaration(s).

## Public surface

**`saleor/graphql/menu/dataloaders.py`**

- `MenuByIdLoader` (class) — [saleor/graphql/menu/dataloaders.py:7]
- `batch_load` (function) — [saleor/graphql/menu/dataloaders.py:10]
- `MenuItemByIdLoader` (class) — [saleor/graphql/menu/dataloaders.py:15]
- `batch_load` (function) — [saleor/graphql/menu/dataloaders.py:18]
- `MenuItemsByParentMenuLoader` (class) — [saleor/graphql/menu/dataloaders.py:23]
- `batch_load` (function) — [saleor/graphql/menu/dataloaders.py:26]
- `MenuItemChildrenLoader` (class) — [saleor/graphql/menu/dataloaders.py:36]
- `batch_load` (function) — [saleor/graphql/menu/dataloaders.py:39]

**`saleor/graphql/menu/enums.py`**

- `NavigationType` (class) — [saleor/graphql/menu/enums.py:4]
- `description` (function) — [saleor/graphql/menu/enums.py:9]

**`saleor/graphql/menu/filters.py`**

- `filter_menu_search` (function) — [saleor/graphql/menu/filters.py:14]
- `filter_menu_slug` (function) — [saleor/graphql/menu/filters.py:18]
- `filter_menu_item_search` (function) — [saleor/graphql/menu/filters.py:22]
- `MenuFilter` (class) — [saleor/graphql/menu/filters.py:26]
- `Meta` (class) — [saleor/graphql/menu/filters.py:31]
- `MenuItemFilter` (class) — [saleor/graphql/menu/filters.py:36]
- `Meta` (class) — [saleor/graphql/menu/filters.py:39]
- `MenuFilterInput` (class) — [saleor/graphql/menu/filters.py:44]
- `Meta` (class) — [saleor/graphql/menu/filters.py:45]
- `MenuItemFilterInput` (class) — [saleor/graphql/menu/filters.py:49]
- `Meta` (class) — [saleor/graphql/menu/filters.py:50]

**`saleor/graphql/menu/resolvers.py`**

- `resolve_menu` (function) — [saleor/graphql/menu/resolvers.py:12]
- `resolve_menus` (function) — [saleor/graphql/menu/resolvers.py:37]
- `resolve_menu_item` (function) — [saleor/graphql/menu/resolvers.py:44]
- `resolve_menu_items` (function) — [saleor/graphql/menu/resolvers.py:53]

**`saleor/graphql/menu/schema.py`**

- `MenuQueries` (class) — [saleor/graphql/menu/schema.py:32]
- `resolve_menu` (function) — [saleor/graphql/menu/schema.py:75]
- `resolve_menus` (function) — [saleor/graphql/menu/schema.py:85]
- `resolve_menu_item` (function) — [saleor/graphql/menu/schema.py:97]
- `resolve_menu_items` (function) — [saleor/graphql/menu/schema.py:106]
- `MenuMutations` (class) — [saleor/graphql/menu/schema.py:119]

**`saleor/graphql/menu/sorters.py`**

- `MenuSortField` (class) — [saleor/graphql/menu/sorters.py:7]
- `description` (function) — [saleor/graphql/menu/sorters.py:12]
- `qs_with_items_count` (function) — [saleor/graphql/menu/sorters.py:19]
- `MenuSortingInput` (class) — [saleor/graphql/menu/sorters.py:23]
- `Meta` (class) — [saleor/graphql/menu/sorters.py:24]
- `MenuItemsSortField` (class) — [saleor/graphql/menu/sorters.py:29]
- `description` (function) — [saleor/graphql/menu/sorters.py:33]
- `MenuItemSortingInput` (class) — [saleor/graphql/menu/sorters.py:40]
- `Meta` (class) — [saleor/graphql/menu/sorters.py:41]

**`saleor/graphql/menu/types.py`**

- `Menu` (class) — [saleor/graphql/menu/types.py:35]
- `Meta` (class) — [saleor/graphql/menu/types.py:43]
- `resolve_items` (function) — [saleor/graphql/menu/types.py:53]
- `MenuCountableConnection` (class) — [saleor/graphql/menu/types.py:63]
- `Meta` (class) — [saleor/graphql/menu/types.py:64]
- `MenuItem` (class) — [saleor/graphql/menu/types.py:69]
- `Meta` (class) — [saleor/graphql/menu/types.py:116]
- `resolve_category` (function) — [saleor/graphql/menu/types.py:126]
- `resolve_children` (function) — [saleor/graphql/menu/types.py:132]
- `resolve_collection` (function) — [saleor/graphql/menu/types.py:142]
- `calculate_collection_availability` (function) — [saleor/graphql/menu/types.py:169]
- `calculate_collection_availability_with_channel` (function) — [saleor/graphql/menu/types.py:170]
- `resolve_menu` (function) — [saleor/graphql/menu/types.py:201]
- `resolve_parent` (function) — [saleor/graphql/menu/types.py:210]
- `resolve_page` (function) — [saleor/graphql/menu/types.py:219]
- `resolve_page_with_channel` (function) — [saleor/graphql/menu/types.py:228]
- `MenuItemCountableConnection` (class) — [saleor/graphql/menu/types.py:241]
- `Meta` (class) — [saleor/graphql/menu/types.py:242]
- `MenuItemMoveInput` (class) — [saleor/graphql/menu/types.py:247]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/menu/__init__.py` (1 lines)
- `saleor/graphql/menu/dataloaders.py` (46 lines)
- `saleor/graphql/menu/enums.py` (14 lines)
- `saleor/graphql/menu/filters.py` (51 lines)
- `saleor/graphql/menu/resolvers.py` (56 lines)
- `saleor/graphql/menu/schema.py` (132 lines)
- `saleor/graphql/menu/sorters.py` (43 lines)
- `saleor/graphql/menu/types.py` (258 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...menu.models`
- `...menu.models.Menu`
- `...menu.models.MenuItem`
- `...permission.enums.PagePermissions`
- `...permission.utils.has_one_of_permissions`
- `...product.models.ALL_PRODUCTS_PERMISSIONS`
- `..channel.dataloaders.by_self.ChannelBySlugLoader`
- `..channel.utils.get_default_channel_slug_or_graphql_error`
- `..core.ResolveInfo`
- `..core.connection.CountableConnection`
- `..core.connection.create_connection_slice`
- `..core.connection.filter_connection_queryset`
- `..core.context.ChannelContext`
- `..core.context.ChannelQsContext`
- `..core.dataloaders.DataLoader`
- `..core.doc_category.DOC_CATEGORY_MENU`
- `..core.fields.FilterConnectionField`
- `..core.types.NonNullList`
- `..core.types.SortInputObjectType`
- `..core.types.context.ChannelContextType`
- `..core.utils.from_global_id_or_error`
- `..core.validators.validate_one_of_args_is_in_query`
- `..meta.types.ObjectWithMetadata`
- `..page.dataloaders.PageByIdLoader`
- `..page.types.Page`
- `..product.types.Category`
- `..product.types.Collection`
- `..translations.fields.TranslationField`
- `..translations.mutations.MenuItemTranslate`
- `..translations.types.MenuItemTranslation`
- `..utils.filters.filter_slug_list`
- `..utils.get_user_or_app_from_context`
- `.bulk_mutations.MenuBulkDelete`
- `.bulk_mutations.MenuItemBulkDelete`
- `.filters.MenuFilterInput`
- `.filters.MenuItemFilterInput`
- `.sorters.MenuItemSortingInput`
- `.sorters.MenuSortingInput`
- `.types.Menu`
- `.types.MenuCountableConnection`
- `.types.MenuItem`
- `.types.MenuItemCountableConnection`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `e463530f9a9c` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
