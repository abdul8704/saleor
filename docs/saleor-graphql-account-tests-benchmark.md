## Purpose

`saleor/graphql/account/tests/benchmark` (`saleor/graphql/account/tests/benchmark`) groups 3 source file(s) exposing 13 top-level declaration(s).

## Public surface

**`saleor/graphql/account/tests/benchmark/test_account.py`**

- `test_query_staff_user` (function) — [saleor/graphql/account/tests/benchmark/test_account.py:13]
- `test_staff_create` (function) — [saleor/graphql/account/tests/benchmark/test_account.py:119]
- `test_staff_update_groups_and_permissions` (function) — [saleor/graphql/account/tests/benchmark/test_account.py:185]
- `test_delete_staff_members` (function) — [saleor/graphql/account/tests/benchmark/test_account.py:273]
- `test_customers_query` (function) — [saleor/graphql/account/tests/benchmark/test_account.py:354]
- `test_users_for_federation_query_count` (function) — [saleor/graphql/account/tests/benchmark/test_account.py:370]
- `test_addresses_for_federation_query_count` (function) — [saleor/graphql/account/tests/benchmark/test_account.py:449]

**`saleor/graphql/account/tests/benchmark/test_permission_group.py`**

- `test_permission_group_create` (function) — [saleor/graphql/account/tests/benchmark/test_permission_group.py:11]
- `test_permission_group_update` (function) — [saleor/graphql/account/tests/benchmark/test_permission_group.py:73]
- `test_permission_group_update_remove_users_with_manage_staff` (function) — [saleor/graphql/account/tests/benchmark/test_permission_group.py:146]
- `test_permission_group_delete` (function) — [saleor/graphql/account/tests/benchmark/test_permission_group.py:221]
- `test_permission_group_query` (function) — [saleor/graphql/account/tests/benchmark/test_permission_group.py:282]
- `test_groups_for_federation_query_count` (function) — [saleor/graphql/account/tests/benchmark/test_permission_group.py:318]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/account/tests/benchmark/__init__.py` (1 lines)
- `saleor/graphql/account/tests/benchmark/test_account.py` (515 lines)
- `saleor/graphql/account/tests/benchmark/test_permission_group.py` (369 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....account.models.Group`
- `.....account.models.User`
- `.....permission.enums.AccountPermissions`
- `.....permission.enums.OrderPermissions`
- `....tests.utils.get_graphql_content`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `ae965d0ab534` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
