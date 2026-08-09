## Purpose

`saleor/graphql/csv` (`saleor/graphql/csv`) groups 8 source file(s) exposing 37 top-level declaration(s).

## Public surface

**`saleor/graphql/csv/dataloaders.py`**

- `EventsByExportFileIdLoader` (class) — [saleor/graphql/csv/dataloaders.py:7]
- `batch_load` (function) — [saleor/graphql/csv/dataloaders.py:10]
- `events_by_export_file_id` (function) — [saleor/graphql/csv/dataloaders.py:16]

**`saleor/graphql/csv/enums.py`**

- `ExportScope` (class) — [saleor/graphql/csv/enums.py:14]
- `Meta` (class) — [saleor/graphql/csv/enums.py:19]
- `description` (function) — [saleor/graphql/csv/enums.py:23]
- `ProductFieldEnum` (class) — [saleor/graphql/csv/enums.py:35]
- `Meta` (class) — [saleor/graphql/csv/enums.py:49]

**`saleor/graphql/csv/filters.py`**

- `filter_user` (function) — [saleor/graphql/csv/filters.py:9]
- `filter_app` (function) — [saleor/graphql/csv/filters.py:22]
- `ExportFileFilter` (class) — [saleor/graphql/csv/filters.py:27]
- `ExportFileFilterInput` (class) — [saleor/graphql/csv/filters.py:32]
- `Meta` (class) — [saleor/graphql/csv/filters.py:33]

**`saleor/graphql/csv/resolvers.py`**

- `resolve_export_file` (function) — [saleor/graphql/csv/resolvers.py:5]
- `resolve_export_files` (function) — [saleor/graphql/csv/resolvers.py:13]

**`saleor/graphql/csv/schema.py`**

- `CsvQueries` (class) — [saleor/graphql/csv/schema.py:16]
- `resolve_export_file` (function) — [saleor/graphql/csv/schema.py:33]
- `resolve_export_files` (function) — [saleor/graphql/csv/schema.py:37]
- `CsvMutations` (class) — [saleor/graphql/csv/schema.py:45]

**`saleor/graphql/csv/sorters.py`**

- `ExportFileSortField` (class) — [saleor/graphql/csv/sorters.py:6]
- `description` (function) — [saleor/graphql/csv/sorters.py:13]
- `deprecation_reason` (function) — [saleor/graphql/csv/sorters.py:27]
- `ExportFileSortingInput` (class) — [saleor/graphql/csv/sorters.py:36]
- `Meta` (class) — [saleor/graphql/csv/sorters.py:37]

**`saleor/graphql/csv/types.py`**

- `ExportEvent` (class) — [saleor/graphql/csv/types.py:20]
- `Meta` (class) — [saleor/graphql/csv/types.py:49]
- `resolve_user` (function) — [saleor/graphql/csv/types.py:55]
- `resolve_app` (function) — [saleor/graphql/csv/types.py:63]
- `resolve_message` (function) — [saleor/graphql/csv/types.py:71]
- `ExportFile` (class) — [saleor/graphql/csv/types.py:75]
- `Meta` (class) — [saleor/graphql/csv/types.py:85]
- `resolve_url` (function) — [saleor/graphql/csv/types.py:91]
- `resolve_user` (function) — [saleor/graphql/csv/types.py:98]
- `resolve_app` (function) — [saleor/graphql/csv/types.py:106]
- `resolve_events` (function) — [saleor/graphql/csv/types.py:114]
- `ExportFileCountableConnection` (class) — [saleor/graphql/csv/types.py:121]
- `Meta` (class) — [saleor/graphql/csv/types.py:122]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/csv/__init__.py` (1 lines)
- `saleor/graphql/csv/dataloaders.py` (20 lines)
- `saleor/graphql/csv/enums.py` (50 lines)
- `saleor/graphql/csv/filters.py` (34 lines)
- `saleor/graphql/csv/resolvers.py` (16 lines)
- `saleor/graphql/csv/schema.py` (54 lines)
- `saleor/graphql/csv/sorters.py` (39 lines)
- `saleor/graphql/csv/types.py` (123 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...account.models.User`
- `...app.models.App`
- `...core.utils.build_absolute_uri`
- `...csv.ExportEvents`
- `...csv.FileTypes`
- `...csv.models`
- `...csv.models.ExportEvent`
- `...permission.auth_filters.AuthorizationFilters`
- `...permission.enums.AccountPermissions`
- `...permission.enums.AppPermission`
- `...permission.enums.ProductPermissions`
- `..account.types.User`
- `..account.utils.check_is_owner_or_has_one_of_perms`
- `..app.dataloaders.AppByIdLoader`
- `..app.types.App`
- `..core.ResolveInfo`
- `..core.connection.CountableConnection`
- `..core.connection.create_connection_slice`
- `..core.connection.filter_connection_queryset`
- `..core.context.get_database_connection_name`
- `..core.dataloaders.DataLoader`
- `..core.descriptions.DEPRECATED_EXPORT_MUTATIONS`
- `..core.doc_category.DOC_CATEGORY_PRODUCTS`
- `..core.enums.to_enum`
- `..core.fields.FilterConnectionField`
- `..core.fields.PermissionsField`
- `..core.filters.BaseJobFilter`
- `..core.filters.FilterInputObjectType`
- `..core.scalars.DateTime`
- `..core.types.BaseEnum`
- `..core.types.Job`
- `..core.types.ModelObjectType`
- `..core.types.NonNullList`
- `..core.types.SortInputObjectType`
- `..core.utils.from_global_id_or_error`
- `..utils.get_user_or_app_from_context`
- `.dataloaders.EventsByExportFileIdLoader`
- `.enums.ExportEventEnum`
- `.filters.ExportFileFilterInput`
- `.mutations.ExportGiftCards`
- `.mutations.ExportProducts`
- `.mutations.ExportVoucherCodes`
- `.resolvers.resolve_export_file`
- `.resolvers.resolve_export_files`
- `.sorters.ExportFileSortingInput`
- `.types.ExportFile`
- `.types.ExportFileCountableConnection`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `e0df99a00133` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
