## Purpose

`saleor/graphql/account/mutations/permission_group` (`saleor/graphql/account/mutations/permission_group`) groups 4 source file(s) exposing 43 top-level declaration(s).

## Public surface

**`saleor/graphql/account/mutations/permission_group/permission_group_create.py`**

- `PermissionGroupInput` (class) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:27]
- `Meta` (class) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:42]
- `PermissionGroupCreateInput` (class) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:46]
- `Meta` (class) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:56]
- `PermissionGroupCreate` (class) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:60]
- `Arguments` (class) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:61]
- `Meta` (class) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:66]
- `post_save_action` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:99]
- `clean_input` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:104]
- `clean_permissions` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:123]
- `check_permissions` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:140]
- `ensure_can_manage_permissions` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:151]
- `clean_users` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:171]
- `ensure_users_are_staff` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:183]
- `clean_channels` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:201]
- `ensure_can_manage_channels` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:237]
- `update_errors` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_create.py:262]

**`saleor/graphql/account/mutations/permission_group/permission_group_delete.py`**

- `PermissionGroupDelete` (class) — [saleor/graphql/account/mutations/permission_group/permission_group_delete.py:25]
- `Arguments` (class) — [saleor/graphql/account/mutations/permission_group/permission_group_delete.py:26]
- `Meta` (class) — [saleor/graphql/account/mutations/permission_group/permission_group_delete.py:29]
- `post_save_action` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_delete.py:46]
- `clean_instance` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_delete.py:51]
- `check_permissions` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_delete.py:69]
- `check_if_group_can_be_removed` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_delete.py:80]
- `ensure_deleting_not_left_not_manageable_permissions` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_delete.py:85]
- `ensure_not_removing_requestor_last_group` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_delete.py:102]

**`saleor/graphql/account/mutations/permission_group/permission_group_update.py`**

- `PermissionGroupUpdateInput` (class) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:33]
- `Meta` (class) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:53]
- `PermissionGroupUpdate` (class) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:57]
- `Arguments` (class) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:58]
- `Meta` (class) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:64]
- `post_save_action` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:94]
- `clean_input` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:99]
- `ensure_requestor_can_manage_group` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:120]
- `clean_channels` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:139]
- `clean_permissions` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:166]
- `ensure_permissions_can_be_removed` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:185]
- `clean_users` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:206]
- `ensure_can_manage_users` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:222]
- `clean_remove_users` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:249]
- `check_if_removing_user_last_group` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:260]
- `check_if_users_can_be_removed` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:273]
- `check_duplicates` (function) — [saleor/graphql/account/mutations/permission_group/permission_group_update.py:310]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/account/mutations/permission_group/__init__.py` (9 lines)
- `saleor/graphql/account/mutations/permission_group/permission_group_create.py` (272 lines)
- `saleor/graphql/account/mutations/permission_group/permission_group_delete.py` (107 lines)
- `saleor/graphql/account/mutations/permission_group/permission_group_update.py` (324 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....account.error_codes.PermissionGroupErrorCode`
- `.....account.models`
- `.....account.models.User`
- `.....channel.models.Channel`
- `.....core.exceptions.PermissionDenied`
- `.....core.tracing.traced_atomic_transaction`
- `.....permission.enums.AccountPermissions`
- `.....permission.enums.get_permissions`
- `.....webhook.event_types.WebhookEventAsyncType`
- `....account.utils.get_out_of_scope_permissions`
- `....account.utils.get_user_accessible_channels`
- `....app.dataloaders.get_app_promise`
- `....core.ResolveInfo`
- `....core.doc_category.DOC_CATEGORY_USERS`
- `....core.enums.PermissionEnum`
- `....core.mutations.DeprecatedModelMutation`
- `....core.mutations.ModelDeleteMutation`
- `....core.types.BaseInputObjectType`
- `....core.types.NonNullList`
- `....core.types.PermissionGroupError`
- `....core.utils.WebhookEventInfo`
- `....plugins.dataloaders.get_plugin_manager_promise`
- `....utils.validators.check_for_duplicates`
- `...dataloaders.AccessibleChannelsByGroupIdLoader`
- `...types.Group`
- `.permission_group_create.PermissionGroupCreate`
- `.permission_group_create.PermissionGroupInput`
- `.permission_group_delete.PermissionGroupDelete`
- `.permission_group_update.PermissionGroupUpdate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `a3a3cc0ad0cb` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
