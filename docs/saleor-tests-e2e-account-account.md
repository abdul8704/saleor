## Purpose

`saleor/tests/e2e/account/account` (`saleor/tests/e2e/account/account`) groups 8 source file(s) exposing 7 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/account/account/test_login_throttling.py`**

- `test_customer_should_not_be_able_to_perform_credential_guessing_attacks_core_1519` (function) — [saleor/tests/e2e/account/account/test_login_throttling.py:25]

**`saleor/tests/e2e/account/account/test_should_create_account_without_email_confirmation.py`**

- `test_should_create_account_without_email_confirmation_core_1502` (function) — [saleor/tests/e2e/account/account/test_should_create_account_without_email_confirmation.py:14]

**`saleor/tests/e2e/account/account/test_should_login_before_email_confirmation.py`**

- `test_should_login_before_email_confirmation_core_1510` (function) — [saleor/tests/e2e/account/account/test_should_login_before_email_confirmation.py:14]

**`saleor/tests/e2e/account/account/test_should_not_be_able_to_create_account_with_existing_email.py`**

- `test_should_not_be_able_to_create_account_with_existing_email_core_1503` (function) — [saleor/tests/e2e/account/account/test_should_not_be_able_to_create_account_with_existing_email.py:10]

**`saleor/tests/e2e/account/account/test_should_not_be_able_to_login_with_invalid_credentials.py`**

- `test_should_not_be_able_to_login_with_invalid_credentials_core_1506` (function) — [saleor/tests/e2e/account/account/test_should_not_be_able_to_login_with_invalid_credentials.py:15]

**`saleor/tests/e2e/account/account/test_staff_login_customers_only_mode.py`**

- `test_staff_token_has_no_permissions_in_customers_only_mode` (function) — [saleor/tests/e2e/account/account/test_staff_login_customers_only_mode.py:28]

**`saleor/tests/e2e/account/account/test_staff_login_disabled_mode.py`**

- `test_staff_token_is_rejected_in_disabled_mode` (function) — [saleor/tests/e2e/account/account/test_staff_login_disabled_mode.py:28]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/account/account/__init__.py` (1 lines)
- `saleor/tests/e2e/account/account/test_login_throttling.py` (160 lines)
- `saleor/tests/e2e/account/account/test_should_create_account_without_email_confirmation.py` (73 lines)
- `saleor/tests/e2e/account/account/test_should_login_before_email_confirmation.py` (78 lines)
- `saleor/tests/e2e/account/account/test_should_not_be_able_to_create_account_with_existing_email.py` (64 lines)
- `saleor/tests/e2e/account/account/test_should_not_be_able_to_login_with_invalid_credentials.py` (93 lines)
- `saleor/tests/e2e/account/account/test_staff_login_customers_only_mode.py` (105 lines)
- `saleor/tests/e2e/account/account/test_staff_login_disabled_mode.py` (109 lines)

## Interactions

- Imports from: `saleor/account`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....account.error_codes.AccountErrorCode`
- `.....account.models.User`
- `.....graphql.core.utils.to_global_id_or_none`
- `.....site.PasswordLoginMode`
- `...account.utils.token_create.raw_token_create`
- `...conftest.E2eApiClient`
- `...product.utils.category.create_category`
- `...product.utils.product.PRODUCT_CREATE_MUTATION`
- `...product.utils.product_type.create_product_type`
- `...shop.utils.prepare_shop`
- `...utils.assign_permissions`
- `...utils.get_graphql_content`
- `..utils.account_register`
- `..utils.raw_account_register`
- `..utils.raw_token_create`
- `..utils.token_create`
- `saleor.account.throttling.get_cache_key_blocked_ip`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `f911803dd00d` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
