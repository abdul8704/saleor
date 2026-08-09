## Purpose

`saleor/graphql/core/tests/garbage_collection` (`saleor/graphql/core/tests/garbage_collection`) groups 9 source file(s) exposing 15 top-level declaration(s).

## Public surface

**`saleor/graphql/core/tests/garbage_collection/test_asgiref.py`**

- `test_thread_critical_Local_remove_all_reference_cycles` (function) — [saleor/graphql/core/tests/garbage_collection/test_asgiref.py:16]

**`saleor/graphql/core/tests/garbage_collection/test_django.py`**

- `test_django_connection_remove_all_reference_cycles` (function) — [saleor/graphql/core/tests/garbage_collection/test_django.py:16]

**`saleor/graphql/core/tests/garbage_collection/test_errors.py`**

- `raise_graphql_error` (function) — [saleor/graphql/core/tests/garbage_collection/test_errors.py:19]
- `test_permission_error` (function) — [saleor/graphql/core/tests/garbage_collection/test_errors.py:44]
- `test_query_cost_error` (function) — [saleor/graphql/core/tests/garbage_collection/test_errors.py:104]
- `test_exception_in_resolver` (function) — [saleor/graphql/core/tests/garbage_collection/test_errors.py:144]
- `test_exception_in_dataloader` (function) — [saleor/graphql/core/tests/garbage_collection/test_errors.py:189]
- `test_input_validation_error` (function) — [saleor/graphql/core/tests/garbage_collection/test_errors.py:250]

**`saleor/graphql/core/tests/garbage_collection/test_gzip.py`**

- `test_GzipFile_with_BytesIO_buffer_remove_all_reference_cycles` (function) — [saleor/graphql/core/tests/garbage_collection/test_gzip.py:17]

**`saleor/graphql/core/tests/garbage_collection/test_oauth2.py`**

- `test_OAuth2Session_remove_all_reference_cycles` (function) — [saleor/graphql/core/tests/garbage_collection/test_oauth2.py:16]

**`saleor/graphql/core/tests/garbage_collection/test_promise.py`**

- `test_query_remove_all_memory_cycles_in_promise` (function) — [saleor/graphql/core/tests/garbage_collection/test_promise.py:36]

**`saleor/graphql/core/tests/garbage_collection/test_saleor_context.py`**

- `test_query_remove_SaleorContext_memory_cycles` (function) — [saleor/graphql/core/tests/garbage_collection/test_saleor_context.py:37]
- `test_query_with_site_settings_no_memory_cycles` (function) — [saleor/graphql/core/tests/garbage_collection/test_saleor_context.py:77]

**`saleor/graphql/core/tests/garbage_collection/utils.py`**

- `disable_gc_for_garbage_collection_test` (function) — [saleor/graphql/core/tests/garbage_collection/utils.py:4]
- `clean_up_after_garbage_collection_test` (function) — [saleor/graphql/core/tests/garbage_collection/utils.py:22]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/core/tests/garbage_collection/__init__.py` (1 lines)
- `saleor/graphql/core/tests/garbage_collection/test_asgiref.py` (39 lines)
- `saleor/graphql/core/tests/garbage_collection/test_django.py` (37 lines)
- `saleor/graphql/core/tests/garbage_collection/test_errors.py` (284 lines)
- `saleor/graphql/core/tests/garbage_collection/test_gzip.py` (40 lines)
- `saleor/graphql/core/tests/garbage_collection/test_oauth2.py` (36 lines)
- `saleor/graphql/core/tests/garbage_collection/test_promise.py` (67 lines)
- `saleor/graphql/core/tests/garbage_collection/test_saleor_context.py` (103 lines)
- `saleor/graphql/core/tests/garbage_collection/utils.py` (27 lines)

## Interactions

- Imports from: `saleor/webhook`, `saleor/graphql`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....core.jwt.create_access_token`
- `....api.backend`
- `....api.schema`
- `....tests.utils.get_graphql_content`
- `....views.GraphQLView`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `8d724293afdc` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
