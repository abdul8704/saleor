## Purpose

`saleor/graphql/account/tests/mutations/permission_group` (`saleor/graphql/account/tests/mutations/permission_group`) groups 4 source file(s) exposing 58 top-level declaration(s).

## Public surface

**`saleor/graphql/account/tests/mutations/permission_group/test_permission_group_create.py`**

- `test_permission_group_create_mutation` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_create.py:51]
- `test_permission_group_create_mutation_trigger_webhook` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_create.py:110]
- `test_permission_group_create_app_no_permission` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_create.py:172]
- `test_permission_group_create_no_channel_access` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_create.py:202]
- `test_permission_group_create_mutation_only_required_fields` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_create.py:245]
- `test_permission_group_create_mutation_only_required_fields_not_none` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_create.py:273]
- `test_permission_group_create_mutation_lack_of_permission` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_create.py:307]
- `test_permission_group_create_mutation_group_exists` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_create.py:366]
- `test_permission_group_create_mutation_add_customer_user` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_create.py:402]
- `test_permission_group_create_mutation_lack_of_permission_and_customer_user` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_create.py:465]
- `test_permission_group_create_mutation_requestor_does_not_have_all_users_perms` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_create.py:510]
- `test_permission_group_create_mutation_restricted_access_to_channels` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_create.py:559]
- `test_permission_group_create_mutation_not_restricted_channels` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_create.py:597]
- `test_permission_group_create_mutation_not_restricted_channels_no_access` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_create.py:634]

**`saleor/graphql/account/tests/mutations/permission_group/test_permission_group_delete.py`**

- `test_group_delete_mutation` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_delete.py:41]
- `test_group_delete_mutation_trigger_webhook` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_delete.py:84]
- `test_group_delete_mutation_app_no_permission` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_delete.py:146]
- `test_group_delete_mutation_out_of_scope_permission` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_delete.py:178]
- `test_group_delete_mutation_left_not_manageable_permission` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_delete.py:214]
- `test_group_delete_mutation_delete_last_group` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_delete.py:278]
- `test_group_delete_mutation_delete_last_group_with_manage_staff` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_delete.py:307]
- `test_group_delete_mutation_cannot_remove_requestor_last_group` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_delete.py:348]
- `test_group_delete_mutation_no_channel_access` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_delete.py:385]

**`saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py`**

- `test_permission_group_update_mutation` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:52]
- `test_permission_group_update_mutation_trigger_webhook` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:134]
- `test_permission_group_update_mutation_to_not_restricted_channels` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:203]
- `test_permission_group_update_mutation_to_not_restricted_channels_no_access` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:245]
- `test_permission_group_update_mutation_to_not_restricted_channels_superuser` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:283]
- `test_permission_group_update_mutation_not_restricted_channels` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:319]
- `test_permission_group_update_mutation_no_channel_access` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:355]
- `test_permission_group_update_mutation_out_of_scope_channel` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:391]
- `test_permission_group_update_mutation_removing_perm_left_not_manageable_perms` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:426]
- `test_permission_group_update_mutation_superuser_can_remove_any_perms` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:471]
- `test_permission_group_update_mutation_app_no_permission` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:523]
- `test_permission_group_update_mutation_remove_me_from_last_group` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:552]
- `test_permission_group_update_mutation_remove_me_from_not_last_group` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:591]
- `test_permission_group_update_mutation_remove_last_user_from_group` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:634]
- `test_permission_group_update_mutation_only_name` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:680]
- `test_permission_group_update_mutation_only_name_other_fields_with_none` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:726]
- `test_permission_group_update_mutation_with_name_which_exists` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:778]
- `test_permission_group_update_mutation_only_permissions` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:812]
- `test_permission_group_update_mutation_no_input_data` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:846]
- `test_permission_group_update_mutation_user_cannot_manage_group` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:872]
- `test_permission_group_update_mutation_user_in_list_to_add_and_remove` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:924]
- `test_permission_group_update_mutation_permissions_in_list_to_add_and_remove` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:962]
- `test_permission_group_update_mutation_permissions_and_users_duplicated` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:1004]
- `test_permission_group_update_mutation_user_add_customer_user` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:1057]
- `test_permission_group_update_mutation_lack_of_permission` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:1110]
- `test_permission_group_update_mutation_out_of_scope_users` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:1168]
- `test_permission_group_update_mutation_duplicated_channels` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:1246]
- `test_permission_group_update_mutation_multiple_errors` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:1302]
- `test_permission_group_update_mutation_remove_all_users_manageable_perms` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:1369]
- `test_permission_group_update_mutation_remove_all_group_users_not_manageable_perms` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:1418]
- `test_permission_group_update_mutation_remove_group_users_add_with_manage_stuff` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:1483]
- `test_group_update_mutation_remove_some_users_from_group_with_manage_staff` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:1529]
- `test_group_update_mutation_remove_some_users_from_group_user_with_manage_stuff` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:1563]
- `test_permission_group_update_mutation_remove_user_with_manage_staff` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:1604]
- `test_permission_group_update_mutation_remove_user_with_manage_staff_add_user` (function) — [saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py:1654]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/account/tests/mutations/permission_group/__init__.py` (1 lines)
- `saleor/graphql/account/tests/mutations/permission_group/test_permission_group_create.py` (664 lines)
- `saleor/graphql/account/tests/mutations/permission_group/test_permission_group_delete.py` (421 lines)
- `saleor/graphql/account/tests/mutations/permission_group/test_permission_group_update.py` (1700 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `......account.error_codes.PermissionGroupErrorCode`
- `......account.models.Group`
- `......account.models.User`
- `......account.tests.fixtures.user.dangerously_create_test_user`
- `......channel.models.Channel`
- `......core.utils.json_serializer.CustomJsonEncoder`
- `......permission.enums.AccountPermissions`
- `......permission.enums.AppPermission`
- `......permission.enums.OrderPermissions`
- `......webhook.event_types.WebhookEventAsyncType`
- `......webhook.payloads.generate_meta`
- `......webhook.payloads.generate_requestor`
- `.....tests.utils.assert_no_permission`
- `.....tests.utils.get_graphql_content`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `2ee5a23b6674` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
