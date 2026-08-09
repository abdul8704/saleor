## Purpose

`saleor/graphql/app/tests` (`saleor/graphql/app/tests`) groups 3 source file(s) exposing 14 top-level declaration(s).

## Public surface

**`saleor/graphql/app/tests/test_app_by_token_loader_use_cache.py`**

- `test_app_by_token_loader_cache_token_calculation` (function) — [saleor/graphql/app/tests/test_app_by_token_loader_use_cache.py:11]
- `test_app_by_token_loader_invalid_token` (function) — [saleor/graphql/app/tests/test_app_by_token_loader_use_cache.py:37]
- `test_app_by_token_loader_use_cached_app` (function) — [saleor/graphql/app/tests/test_app_by_token_loader_use_cache.py:57]
- `test_app_by_token_loader_cached_app_not_active` (function) — [saleor/graphql/app/tests/test_app_by_token_loader_use_cache.py:86]
- `test_app_by_token_loader_cached_app_marked_as_removed` (function) — [saleor/graphql/app/tests/test_app_by_token_loader_use_cache.py:121]
- `test_app_by_token_loader_missing_app` (function) — [saleor/graphql/app/tests/test_app_by_token_loader_use_cache.py:156]
- `test_app_by_token_loader_removed_token` (function) — [saleor/graphql/app/tests/test_app_by_token_loader_use_cache.py:190]
- `test_app_by_token_loader_one_of_tokens_in_cache` (function) — [saleor/graphql/app/tests/test_app_by_token_loader_use_cache.py:224]
- `test_app_by_token_loader_tokens_with_same_last_4` (function) — [saleor/graphql/app/tests/test_app_by_token_loader_use_cache.py:264]

**`saleor/graphql/app/tests/test_utils.py`**

- `test_ensure_app_permissions_allowed_passes_when_no_manage_apps` (function) — [saleor/graphql/app/tests/test_utils.py:14]
- `test_ensure_app_permissions_allowed_passes_with_empty_list` (function) — [saleor/graphql/app/tests/test_utils.py:24]
- `test_ensure_app_permissions_allowed_rejects_manage_apps` (function) — [saleor/graphql/app/tests/test_utils.py:29]
- `test_ensure_app_permissions_allowed_rejects_manage_apps_alongside_others` (function) — [saleor/graphql/app/tests/test_utils.py:42]
- `test_ensure_app_permissions_allowed_does_not_match_enum_name` (function) — [saleor/graphql/app/tests/test_utils.py:60]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/app/tests/__init__.py` (1 lines)
- `saleor/graphql/app/tests/test_app_by_token_loader_use_cache.py` (301 lines)
- `saleor/graphql/app/tests/test_utils.py` (67 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....app.error_codes.AppErrorCode`
- `....app.models.App`
- `....app.models.AppToken`
- `...context.SaleorContext`
- `..dataloaders.app.AppByTokenLoader`
- `..dataloaders.app.create_app_cache_key_from_token`
- `..utils.ensure_app_permissions_allowed`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `70312a5dd1ac` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
