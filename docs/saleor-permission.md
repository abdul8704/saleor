## Purpose

`saleor/permission` (`saleor/permission`) groups 15 source file(s) exposing 87 top-level declaration(s).

## Public surface

**`saleor/permission/apps.py`**

- `AccountAppConfig` (class) — [saleor/permission/apps.py:7]
- `ready` (function) — [saleor/permission/apps.py:10]

**`saleor/permission/auth_filters.py`**

- `is_app` (function) — [saleor/permission/auth_filters.py:4]
- `is_user` (function) — [saleor/permission/auth_filters.py:8]
- `is_staff_user` (function) — [saleor/permission/auth_filters.py:13]
- `AuthorizationFilters` (class) — [saleor/permission/auth_filters.py:17]
- `resolve_authorization_filter_fn` (function) — [saleor/permission/auth_filters.py:40]

**`saleor/permission/enums.py`**

- `BasePermissionEnum` (class) — [saleor/permission/enums.py:10]
- `codename` (function) — [saleor/permission/enums.py:12]
- `AccountPermissions` (class) — [saleor/permission/enums.py:16]
- `AppPermission` (class) — [saleor/permission/enums.py:22]
- `ChannelPermissions` (class) — [saleor/permission/enums.py:27]
- `DiscountPermissions` (class) — [saleor/permission/enums.py:31]
- `PluginsPermissions` (class) — [saleor/permission/enums.py:35]
- `GiftcardPermissions` (class) — [saleor/permission/enums.py:39]
- `MenuPermissions` (class) — [saleor/permission/enums.py:43]
- `CheckoutPermissions` (class) — [saleor/permission/enums.py:47]
- `OrderPermissions` (class) — [saleor/permission/enums.py:54]
- `PaymentPermissions` (class) — [saleor/permission/enums.py:59]
- `PagePermissions` (class) — [saleor/permission/enums.py:63]
- `PageTypePermissions` (class) — [saleor/permission/enums.py:67]
- `ProductPermissions` (class) — [saleor/permission/enums.py:71]
- `ProductTypePermissions` (class) — [saleor/permission/enums.py:75]
- `ShippingPermissions` (class) — [saleor/permission/enums.py:79]
- `SitePermissions` (class) — [saleor/permission/enums.py:83]
- `get_permissions_codename` (function) — [saleor/permission/enums.py:108]
- `get_permissions_enum_list` (function) — [saleor/permission/enums.py:117]
- `get_permissions_enum_dict` (function) — [saleor/permission/enums.py:126]
- `get_permissions_from_names` (function) — [saleor/permission/enums.py:134]
- `get_permission_names` (function) — [saleor/permission/enums.py:140]
- `split_permission_codename` (function) — [saleor/permission/enums.py:151]
- `get_permissions` (function) — [saleor/permission/enums.py:155]
- `get_permissions_from_codenames` (function) — [saleor/permission/enums.py:166]

**`saleor/permission/management.py`**

- `create_permissions` (function) — [saleor/permission/management.py:28]

**`saleor/permission/migrations/0001_initial.py`**

- `rename_permission_table` (function) — [saleor/permission/migrations/0001_initial.py:37]
- `rename_permission_table_reverse` (function) — [saleor/permission/migrations/0001_initial.py:76]
- `Migration` (class) — [saleor/permission/migrations/0001_initial.py:85]

**`saleor/permission/migrations/0002_alter_permission_content_type.py`**

- `Migration` (class) — [saleor/permission/migrations/0002_alter_permission_content_type.py:7]

**`saleor/permission/models.py`**

- `PermissionManager` (class) — [saleor/permission/models.py:30]
- `get_by_natural_key` (function) — [saleor/permission/models.py:33]
- `Permission` (class) — [saleor/permission/models.py:42]
- `Meta` (class) — [saleor/permission/models.py:75]
- `natural_key` (function) — [saleor/permission/models.py:84]
- `PermissionsMixin` (class) — [saleor/permission/models.py:90]
- `Meta` (class) — [saleor/permission/models.py:121]
- `get_user_permissions` (function) — [saleor/permission/models.py:124]
- `get_group_permissions` (function) — [saleor/permission/models.py:132]
- `get_all_permissions` (function) — [saleor/permission/models.py:140]
- `has_perm` (function) — [saleor/permission/models.py:143]
- `has_perms` (function) — [saleor/permission/models.py:158]

**`saleor/permission/tests/fixtures/permission.py`**

- `permission_manage_discounts` (function) — [saleor/permission/tests/fixtures/permission.py:7]
- `permission_manage_gift_card` (function) — [saleor/permission/tests/fixtures/permission.py:12]
- `permission_manage_orders` (function) — [saleor/permission/tests/fixtures/permission.py:17]
- `permission_manage_orders_import` (function) — [saleor/permission/tests/fixtures/permission.py:22]
- `permission_manage_checkouts` (function) — [saleor/permission/tests/fixtures/permission.py:27]
- `permission_handle_checkouts` (function) — [saleor/permission/tests/fixtures/permission.py:32]
- `permission_manage_plugins` (function) — [saleor/permission/tests/fixtures/permission.py:37]
- `permission_manage_apps` (function) — [saleor/permission/tests/fixtures/permission.py:42]
- `permission_handle_taxes` (function) — [saleor/permission/tests/fixtures/permission.py:47]
- `permission_manage_observability` (function) — [saleor/permission/tests/fixtures/permission.py:52]
- `permission_manage_taxes` (function) — [saleor/permission/tests/fixtures/permission.py:57]
- `permission_manage_staff` (function) — [saleor/permission/tests/fixtures/permission.py:62]
- `permission_manage_products` (function) — [saleor/permission/tests/fixtures/permission.py:67]
- `permission_manage_product_types_and_attributes` (function) — [saleor/permission/tests/fixtures/permission.py:72]
- `permission_manage_shipping` (function) — [saleor/permission/tests/fixtures/permission.py:77]
- `permission_manage_users` (function) — [saleor/permission/tests/fixtures/permission.py:82]
- `permission_impersonate_user` (function) — [saleor/permission/tests/fixtures/permission.py:87]
- `permission_manage_settings` (function) — [saleor/permission/tests/fixtures/permission.py:92]
- `permission_manage_menus` (function) — [saleor/permission/tests/fixtures/permission.py:97]
- `permission_manage_pages` (function) — [saleor/permission/tests/fixtures/permission.py:102]
- `permission_manage_page_types_and_attributes` (function) — [saleor/permission/tests/fixtures/permission.py:107]
- `permission_manage_translations` (function) — [saleor/permission/tests/fixtures/permission.py:112]
- `permission_manage_webhooks` (function) — [saleor/permission/tests/fixtures/permission.py:117]
- `permission_manage_channels` (function) — [saleor/permission/tests/fixtures/permission.py:122]
- `permission_manage_payments` (function) — [saleor/permission/tests/fixtures/permission.py:127]

**`saleor/permission/tests/test_all_permissions_required.py`**

- `test_permissions_for_app` (function) — [saleor/permission/tests/test_all_permissions_required.py:62]
- `test_permissions_for_staff_user` (function) — [saleor/permission/tests/test_all_permissions_required.py:130]
- `test_permissions_for_customer` (function) — [saleor/permission/tests/test_all_permissions_required.py:198]

**`saleor/permission/tests/test_one_of_permissions_or_auth_filter_required.py`**

- `test_permissions_for_app` (function) — [saleor/permission/tests/test_one_of_permissions_or_auth_filter_required.py:80]
- `test_permissions_for_staff_user` (function) — [saleor/permission/tests/test_one_of_permissions_or_auth_filter_required.py:178]
- `test_permissions_for_customer` (function) — [saleor/permission/tests/test_one_of_permissions_or_auth_filter_required.py:278]
- `test_permissions_for_anonymous_user` (function) — [saleor/permission/tests/test_one_of_permissions_or_auth_filter_required.py:303]

**`saleor/permission/utils.py`**

- `all_permissions_required` (function) — [saleor/permission/utils.py:12]
- `one_of_permissions_or_auth_filter_required` (function) — [saleor/permission/utils.py:32]
- `permission_required` (function) — [saleor/permission/utils.py:83]
- `has_one_of_permissions` (function) — [saleor/permission/utils.py:98]
- `message_one_of_permissions_required` (function) — [saleor/permission/utils.py:111]

## How it works

The module's files, as provided to this run:

- `saleor/permission/models.py` (163 lines)
- `saleor/permission/tests/fixtures/permission.py` (128 lines)
- `saleor/permission/__init__.py` (1 lines)
- `saleor/permission/apps.py` (14 lines)
- `saleor/permission/auth_filters.py` (41 lines)
- `saleor/permission/enums.py` (175 lines)
- `saleor/permission/management.py` (97 lines)
- `saleor/permission/migrations/__init__.py` (1 lines)
- `saleor/permission/migrations/0001_initial.py` (152 lines)
- `saleor/permission/migrations/0002_alter_permission_content_type.py` (25 lines)
- `saleor/permission/tests/__init__.py` (1 lines)
- `saleor/permission/tests/fixtures/__init__.py` (1 lines)
- `saleor/permission/tests/test_all_permissions_required.py` (208 lines)
- `saleor/permission/tests/test_one_of_permissions_or_auth_filter_required.py` (315 lines)
- `saleor/permission/utils.py` (115 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core`, `saleor/attribute/tests`
- Imported by: `saleor/graphql/payment/mutations/transaction`, `saleor/auth`

Internal dependencies named in the source:

- `...models.Permission`
- `..account.models.User`
- `..app.models.App`
- `..auth_filters.AuthorizationFilters`
- `..enums.CheckoutPermissions`
- `..enums.OrderPermissions`
- `..utils.all_permissions_required`
- `..utils.one_of_permissions_or_auth_filter_required`
- `.auth_filters.AuthorizationFilters`
- `.auth_filters.resolve_authorization_filter_fn`
- `.enums.AccountPermissions`
- `.enums.BasePermissionEnum`
- `.management.create_permissions`
- `.models.Permission`
- `.permission.*  # noqa: F403`
- `saleor.graphql.utils.get_user_or_app_from_context`
- `saleor.permission.models`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `e8912edd73ae` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
