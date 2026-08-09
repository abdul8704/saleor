## Purpose

`saleor/tests/e2e` (`saleor/tests/e2e`) groups 8 source file(s) exposing 19 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/conftest.py`**

- `E2eApiClient` (class) — [saleor/tests/e2e/conftest.py:13]
- `post_graphql` (function) — [saleor/tests/e2e/conftest.py:14]
- `post_multipart` (function) — [saleor/tests/e2e/conftest.py:35]
- `e2e_staff_api_client` (function) — [saleor/tests/e2e/conftest.py:49]
- `e2e_logged_api_client` (function) — [saleor/tests/e2e/conftest.py:61]
- `e2e_not_logged_api_client` (function) — [saleor/tests/e2e/conftest.py:74]
- `e2e_app_api_client` (function) — [saleor/tests/e2e/conftest.py:79]
- `e2e_no_permission_staff_api_client` (function) — [saleor/tests/e2e/conftest.py:89]

**`saleor/tests/e2e/test_utils.py`**

- `test_equal_dicts` (function) — [saleor/tests/e2e/test_utils.py:7]
- `test_unequal_dicts` (function) — [saleor/tests/e2e/test_utils.py:23]
- `test_missing_key_in_r2` (function) — [saleor/tests/e2e/test_utils.py:39]
- `test_extra_key_in_r2` (function) — [saleor/tests/e2e/test_utils.py:51]
- `test_different_sorting_order_in_r2` (function) — [saleor/tests/e2e/test_utils.py:71]
- `test_nested_keys` (function) — [saleor/tests/e2e/test_utils.py:87]

**`saleor/tests/e2e/translations/utils.py`**

- `get_translations` (function) — [saleor/tests/e2e/translations/utils.py:44]

**`saleor/tests/e2e/utils.py`**

- `assign_permissions` (function) — [saleor/tests/e2e/utils.py:10]
- `request_matcher` (function) — [saleor/tests/e2e/utils.py:25]
- `assert_address_data` (function) — [saleor/tests/e2e/utils.py:45]

**`saleor/tests/e2e/webhooks/utils.py`**

- `create_webhook` (function) — [saleor/tests/e2e/webhooks/utils.py:31]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/__init__.py` (38 lines)
- `saleor/tests/e2e/conftest.py` (97 lines)
- `saleor/tests/e2e/test_utils.py` (124 lines)
- `saleor/tests/e2e/translations/__init__.py` (1 lines)
- `saleor/tests/e2e/translations/utils.py` (65 lines)
- `saleor/tests/e2e/utils.py` (54 lines)
- `saleor/tests/e2e/webhooks/__init__.py` (1 lines)
- `saleor/tests/e2e/webhooks/utils.py` (50 lines)

## Interactions

- Imports from: `saleor/webhook`, `saleor/plugins/openid_connect`
- Imported by: `saleor/tests/e2e/orders`, `saleor/tests/e2e/checkout`

Internal dependencies named in the source:

- `...account.models.Group`
- `...account.tests.fixtures.user.dangerously_create_test_user`
- `...app.models.App`
- `...graphql.tests.fixtures.BaseApiClient`
- `..utils.get_graphql_content`
- `.utils.request_matcher`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `7d0d04ca94ae` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
