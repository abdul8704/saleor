## Purpose

`saleor/auth` (`saleor/auth`) groups 15 source file(s) exposing 15 top-level declaration(s).

## Public surface

**`saleor/auth/migrations/0001_initial.py`**

- `Migration` (class) — [saleor/auth/migrations/0001_initial.py:9]

**`saleor/auth/migrations/0002_alter_permission_name_max_length.py`**

- `Migration` (class) — [saleor/auth/migrations/0002_alter_permission_name_max_length.py:4]

**`saleor/auth/migrations/0003_alter_user_email_max_length.py`**

- `Migration` (class) — [saleor/auth/migrations/0003_alter_user_email_max_length.py:4]

**`saleor/auth/migrations/0004_alter_user_username_opts.py`**

- `Migration` (class) — [saleor/auth/migrations/0004_alter_user_username_opts.py:5]

**`saleor/auth/migrations/0005_alter_user_last_login_null.py`**

- `Migration` (class) — [saleor/auth/migrations/0005_alter_user_last_login_null.py:4]

**`saleor/auth/migrations/0006_require_contenttypes_0002.py`**

- `Migration` (class) — [saleor/auth/migrations/0006_require_contenttypes_0002.py:4]

**`saleor/auth/migrations/0007_alter_validators_add_error_messages.py`**

- `Migration` (class) — [saleor/auth/migrations/0007_alter_validators_add_error_messages.py:5]

**`saleor/auth/migrations/0008_alter_user_username_max_length.py`**

- `Migration` (class) — [saleor/auth/migrations/0008_alter_user_username_max_length.py:5]

**`saleor/auth/migrations/0009_alter_user_last_name_max_length.py`**

- `Migration` (class) — [saleor/auth/migrations/0009_alter_user_last_name_max_length.py:4]

**`saleor/auth/migrations/0010_alter_group_name_max_length.py`**

- `Migration` (class) — [saleor/auth/migrations/0010_alter_group_name_max_length.py:4]

**`saleor/auth/migrations/0011_update_proxy_permissions.py`**

- `update_proxy_model_permissions` (function) — [saleor/auth/migrations/0011_update_proxy_permissions.py:17]
- `revert_proxy_model_permissions` (function) — [saleor/auth/migrations/0011_update_proxy_permissions.py:56]
- `Migration` (class) — [saleor/auth/migrations/0011_update_proxy_permissions.py:61]

**`saleor/auth/migrations/0012_alter_user_first_name_max_length.py`**

- `Migration` (class) — [saleor/auth/migrations/0012_alter_user_first_name_max_length.py:4]

**`saleor/auth/migrations/0013_auto_20221214_1224.py`**

- `Migration` (class) — [saleor/auth/migrations/0013_auto_20221214_1224.py:6]

## How it works

The module's files, as provided to this run:

- `saleor/auth/__init__.py` (2 lines)
- `saleor/auth/migrations/__init__.py` (1 lines)
- `saleor/auth/migrations/0001_initial.py` (199 lines)
- `saleor/auth/migrations/0002_alter_permission_name_max_length.py` (15 lines)
- `saleor/auth/migrations/0003_alter_user_email_max_length.py` (17 lines)
- `saleor/auth/migrations/0004_alter_user_username_opts.py` (24 lines)
- `saleor/auth/migrations/0005_alter_user_last_login_null.py` (17 lines)
- `saleor/auth/migrations/0006_require_contenttypes_0002.py` (13 lines)
- `saleor/auth/migrations/0007_alter_validators_add_error_messages.py` (23 lines)
- `saleor/auth/migrations/0008_alter_user_username_max_length.py` (23 lines)
- `saleor/auth/migrations/0009_alter_user_last_name_max_length.py` (17 lines)
- `saleor/auth/migrations/0010_alter_group_name_max_length.py` (15 lines)
- `saleor/auth/migrations/0011_update_proxy_permissions.py` (70 lines)
- `saleor/auth/migrations/0012_alter_user_first_name_max_length.py` (17 lines)
- `saleor/auth/migrations/0013_auto_20221214_1224.py` (25 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/account`, `saleor/permission`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `saleor.account.models.GroupManager`
- `saleor.account.models.UserManager`
- `saleor.permission.models.PermissionManager`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `9b86963ac7c8` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
