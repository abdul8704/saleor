## Purpose

`saleor/graphql/core/utils` (`saleor/graphql/core/utils`) groups 4 source file(s) exposing 29 top-level declaration(s).

## Public surface

**`saleor/graphql/core/utils/__init__.py`**

- `snake_to_camel_case` (function) — [saleor/graphql/core/utils/__init__.py:19]
- `str_to_enum` (function) — [saleor/graphql/core/utils/__init__.py:27]
- `get_duplicates_items` (function) — [saleor/graphql/core/utils/__init__.py:32]
- `get_duplicated_values` (function) — [saleor/graphql/core/utils/__init__.py:39]
- `from_global_id_or_error` (function) — [saleor/graphql/core/utils/__init__.py:47]
- `from_global_id_or_error` (function) — [saleor/graphql/core/utils/__init__.py:55]
- `from_global_id_or_error` (function) — [saleor/graphql/core/utils/__init__.py:62]
- `from_global_id_or_none` (function) — [saleor/graphql/core/utils/__init__.py:101]
- `to_global_id_or_none` (function) — [saleor/graphql/core/utils/__init__.py:110]
- `add_hash_to_file_name` (function) — [saleor/graphql/core/utils/__init__.py:117]
- `raise_validation_error` (function) — [saleor/graphql/core/utils/__init__.py:126]
- `ext_ref_to_global_id_or_error` (function) — [saleor/graphql/core/utils/__init__.py:130]
- `WebhookEventInfo` (class) — [saleor/graphql/core/utils/__init__.py:152]
- `message_webhook_events` (function) — [saleor/graphql/core/utils/__init__.py:162]
- `validate_and_apply_search_rank_sorting` (function) — [saleor/graphql/core/utils/__init__.py:172]
- `search_string_in_kwargs` (function) — [saleor/graphql/core/utils/__init__.py:211]
- `sort_field_from_kwargs` (function) — [saleor/graphql/core/utils/__init__.py:222]

**`saleor/graphql/core/utils/error_codes.py`**

- `get_error_code_from_error` (function) — [saleor/graphql/core/utils/error_codes.py:31]

**`saleor/graphql/core/utils/reordering.py`**

- `FinalSortOrder` (class) — [saleor/graphql/core/utils/reordering.py:12]
- `Reordering` (class) — [saleor/graphql/core/utils/reordering.py:28]
- `ordered_node_map` (function) — [saleor/graphql/core/utils/reordering.py:46]
- `calculate_new_sort_order` (function) — [saleor/graphql/core/utils/reordering.py:73]
- `process_move_operation` (function) — [saleor/graphql/core/utils/reordering.py:99]
- `add_to_sort_value_if_in_range` (function) — [saleor/graphql/core/utils/reordering.py:128]
- `commit` (function) — [saleor/graphql/core/utils/reordering.py:135]
- `run` (function) — [saleor/graphql/core/utils/reordering.py:155]
- `perform_reordering` (function) — [saleor/graphql/core/utils/reordering.py:166]

**`saleor/graphql/core/utils/resolvers.py`**

- `resolve_by_global_id_or_ext_ref` (function) — [saleor/graphql/core/utils/resolvers.py:6]
- `resolve_by_global_id_slug_or_ext_ref` (function) — [saleor/graphql/core/utils/resolvers.py:22]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/core/utils/__init__.py` (229 lines)
- `saleor/graphql/core/utils/error_codes.py` (50 lines)
- `saleor/graphql/core/utils/reordering.py` (187 lines)
- `saleor/graphql/core/utils/resolvers.py` (43 lines)

## Interactions

- Imports from: `saleor/plugins/openid_connect`, `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....plugins.const.APP_ID_PREFIX`
- `....thumbnail.FILE_NAME_MAX_LENGTH`
- `....webhook.event_types.WebhookEventAsyncType`
- `...core.context.get_database_connection_name`
- `...core.validators.validate_one_of_args_is_in_query`
- `..from_global_id_or_error`
- `..validators.validate_if_int_or_uuid`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `eed316d3b79c` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
