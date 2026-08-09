## Purpose

`saleor/tests/e2e/account/utils` (`saleor/tests/e2e/account/utils`) groups 12 source file(s) exposing 12 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/account/utils/account_address_delete.py`**

- `account_address_delete` (function) — [saleor/tests/e2e/account/utils/account_address_delete.py:22]

**`saleor/tests/e2e/account/utils/account_register.py`**

- `raw_account_register` (function) — [saleor/tests/e2e/account/utils/account_register.py:22]
- `account_register` (function) — [saleor/tests/e2e/account/utils/account_register.py:47]

**`saleor/tests/e2e/account/utils/create_customer.py`**

- `create_customer` (function) — [saleor/tests/e2e/account/utils/create_customer.py:30]

**`saleor/tests/e2e/account/utils/customer_bulk_update.py`**

- `customer_bulk_update` (function) — [saleor/tests/e2e/account/utils/customer_bulk_update.py:36]

**`saleor/tests/e2e/account/utils/customer_update.py`**

- `customer_update` (function) — [saleor/tests/e2e/account/utils/customer_update.py:31]

**`saleor/tests/e2e/account/utils/me.py`**

- `get_own_data` (function) — [saleor/tests/e2e/account/utils/me.py:27]

**`saleor/tests/e2e/account/utils/staff_create.py`**

- `create_staff` (function) — [saleor/tests/e2e/account/utils/staff_create.py:26]

**`saleor/tests/e2e/account/utils/staff_update.py`**

- `update_staff` (function) — [saleor/tests/e2e/account/utils/staff_update.py:27]

**`saleor/tests/e2e/account/utils/token_create.py`**

- `raw_token_create` (function) — [saleor/tests/e2e/account/utils/token_create.py:24]
- `token_create` (function) — [saleor/tests/e2e/account/utils/token_create.py:39]

**`saleor/tests/e2e/account/utils/user.py`**

- `get_user` (function) — [saleor/tests/e2e/account/utils/user.py:41]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/account/utils/__init__.py` (25 lines)
- `saleor/tests/e2e/account/utils/account_address_delete.py` (39 lines)
- `saleor/tests/e2e/account/utils/account_register.py` (67 lines)
- `saleor/tests/e2e/account/utils/create_customer.py` (47 lines)
- `saleor/tests/e2e/account/utils/customer_bulk_update.py` (54 lines)
- `saleor/tests/e2e/account/utils/customer_update.py` (50 lines)
- `saleor/tests/e2e/account/utils/fragments.py` (18 lines)
- `saleor/tests/e2e/account/utils/me.py` (38 lines)
- `saleor/tests/e2e/account/utils/staff_create.py` (42 lines)
- `saleor/tests/e2e/account/utils/staff_update.py` (45 lines)
- `saleor/tests/e2e/account/utils/token_create.py` (59 lines)
- `saleor/tests/e2e/account/utils/user.py` (52 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...utils.get_graphql_content`
- `.account_address_delete.account_address_delete`
- `.account_register.account_register`
- `.account_register.raw_account_register`
- `.create_customer.create_customer`
- `.customer_bulk_update.customer_bulk_update`
- `.customer_update.customer_update`
- `.fragments.ADDRESS_FRAGMENT`
- `.me.get_own_data`
- `.staff_create.create_staff`
- `.staff_update.update_staff`
- `.token_create.raw_token_create`
- `.token_create.token_create`
- `.user.get_user`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `9b97f7e25897` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
