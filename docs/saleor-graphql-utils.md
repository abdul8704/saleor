## Purpose

`saleor/graphql/utils` (`saleor/graphql/utils`) groups 4 source file(s) exposing 29 top-level declaration(s).

## Public surface

**`saleor/graphql/utils/__init__.py`**

- `resolve_global_ids_to_primary_keys` (function) — [saleor/graphql/utils/__init__.py:60]
- `get_nodes` (function) — [saleor/graphql/utils/__init__.py:100]
- `format_permissions_for_display` (function) — [saleor/graphql/utils/__init__.py:184]
- `get_user_or_app_from_context` (function) — [saleor/graphql/utils/__init__.py:204]
- `requestor_is_superuser` (function) — [saleor/graphql/utils/__init__.py:210]
- `query_identifier` (function) — [saleor/graphql/utils/__init__.py:215]
- `query_fingerprint` (function) — [saleor/graphql/utils/__init__.py:262]
- `format_error` (function) — [saleor/graphql/utils/__init__.py:280]
- `get_source_service_name_value` (function) — [saleor/graphql/utils/__init__.py:322]

**`saleor/graphql/utils/filters.py`**

- `reporting_period_to_date` (function) — [saleor/graphql/utils/filters.py:17]
- `filter_by_period` (function) — [saleor/graphql/utils/filters.py:28]
- `filter_range_field` (function) — [saleor/graphql/utils/filters.py:33]
- `filter_by_id` (function) — [saleor/graphql/utils/filters.py:44]
- `inner` (function) — [saleor/graphql/utils/filters.py:51]
- `filter_by_ids` (function) — [saleor/graphql/utils/filters.py:60]
- `inner` (function) — [saleor/graphql/utils/filters.py:67]
- `filter_where_range_field_with_conditions` (function) — [saleor/graphql/utils/filters.py:74]
- `filter_where_by_range_field` (function) — [saleor/graphql/utils/filters.py:98]
- `filter_where_by_value_field` (function) — [saleor/graphql/utils/filters.py:116]
- `filter_where_by_id_field` (function) — [saleor/graphql/utils/filters.py:131]
- `filter_where_by_numeric_field` (function) — [saleor/graphql/utils/filters.py:147]
- `filter_where_by_price_field` (function) — [saleor/graphql/utils/filters.py:176]
- `filter_slug_list` (function) — [saleor/graphql/utils/filters.py:184]

**`saleor/graphql/utils/sorting.py`**

- `sort_queryset_for_connection` (function) — [saleor/graphql/utils/sorting.py:25]
- `sort_queryset` (function) — [saleor/graphql/utils/sorting.py:44]
- `get_model_default_ordering` (function) — [saleor/graphql/utils/sorting.py:94]
- `sort_queryset_by_default` (function) — [saleor/graphql/utils/sorting.py:106]

**`saleor/graphql/utils/validators.py`**

- `check_for_duplicates` (function) — [saleor/graphql/utils/validators.py:14]
- `check_if_query_contains_only_schema` (function) — [saleor/graphql/utils/validators.py:88]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/utils/__init__.py` (328 lines)
- `saleor/graphql/utils/filters.py` (185 lines)
- `saleor/graphql/utils/sorting.py` (128 lines)
- `saleor/graphql/utils/validators.py` (110 lines)

## Interactions

- Imports from: `saleor/graphql`, `saleor/graphql/product/types`, `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...account.models.User`
- `...app.models.App`
- `...core.exceptions.CircularSubscriptionSyncEvent`
- `...core.exceptions.PermissionDenied`
- `..channel.utils.get_default_channel_slug_or_graphql_error`
- `..core.SaleorContext`
- `..core.enums.OrderDirection`
- `..core.enums.PermissionEnum`
- `..core.enums.ReportingPeriod`
- `..core.types.Permission`
- `..core.types.SortInputObjectType`
- `..core.types.TYPES_WITH_DOUBLE_ID_AVAILABLE`
- `..core.utils.from_global_id_or_error`
- `..core.utils.get_duplicates_items`
- `..core.validators.query_cost.QueryCostError`
- `..resolve_global_ids_to_primary_keys`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `4000362a4390` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
