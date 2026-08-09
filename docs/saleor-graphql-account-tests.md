## Purpose

`saleor/graphql/account/tests` (`saleor/graphql/account/tests`) groups 4 source file(s) exposing 66 top-level declaration(s).

## Public surface

**`saleor/graphql/account/tests/test_account_utils.py`**

- `test_can_user_manage_group_is_true` (function) — [saleor/graphql/account/tests/test_account_utils.py:32]
- `test_can_user_manage_group_superuser` (function) — [saleor/graphql/account/tests/test_account_utils.py:48]
- `test_can_user_manage_group_no_channel_access` (function) — [saleor/graphql/account/tests/test_account_utils.py:60]
- `test_can_user_manage_group_no_permissions` (function) — [saleor/graphql/account/tests/test_account_utils.py:76]
- `test_can_manage_group_user_without_permissions` (function) — [saleor/graphql/account/tests/test_account_utils.py:94]
- `test_can_manage_group_user_with_different_permissions` (function) — [saleor/graphql/account/tests/test_account_utils.py:103]
- `test_can_manage_group_permissions` (function) — [saleor/graphql/account/tests/test_account_utils.py:116]
- `test_can_manage_group_permissions_user_superuser` (function) — [saleor/graphql/account/tests/test_account_utils.py:129]
- `test_can_user_manage_group_channels` (function) — [saleor/graphql/account/tests/test_account_utils.py:138]
- `test_can_user_manage_group_channels_user_with_restricted_channel_access` (function) — [saleor/graphql/account/tests/test_account_utils.py:156]
- `test_can_user_manage_group_channels_superuser` (function) — [saleor/graphql/account/tests/test_account_utils.py:180]
- `test_can_user_manage_group_channels_no_channel_access` (function) — [saleor/graphql/account/tests/test_account_utils.py:192]
- `test_get_out_of_scope_permissions_user_has_all_permissions` (function) — [saleor/graphql/account/tests/test_account_utils.py:210]
- `test_get_out_of_scope_permissions_user_does_not_have_all_permissions` (function) — [saleor/graphql/account/tests/test_account_utils.py:220]
- `test_get_out_of_scope_permissions_user_without_permissions` (function) — [saleor/graphql/account/tests/test_account_utils.py:230]
- `test_get_out_of_scope_permissions_app_has_all_permissions` (function) — [saleor/graphql/account/tests/test_account_utils.py:238]
- `test_get_out_of_scope_permissions_app_does_not_have_all_permissions` (function) — [saleor/graphql/account/tests/test_account_utils.py:249]
- `test_get_group_permission_codes` (function) — [saleor/graphql/account/tests/test_account_utils.py:260]
- `test_get_group_permission_codes_group_without_permissions` (function) — [saleor/graphql/account/tests/test_account_utils.py:274]
- `test_get_user_permissions` (function) — [saleor/graphql/account/tests/test_account_utils.py:285]
- `test_get_user_permissions_only_group_permissions` (function) — [saleor/graphql/account/tests/test_account_utils.py:298]
- `test_get_user_permissions_only_permissions` (function) — [saleor/graphql/account/tests/test_account_utils.py:309]
- `test_get_user_permissions_no_permissions` (function) — [saleor/graphql/account/tests/test_account_utils.py:320]
- `test_get_groups_which_user_can_manage` (function) — [saleor/graphql/account/tests/test_account_utils.py:326]
- `test_get_groups_which_user_can_manage_admin_user` (function) — [saleor/graphql/account/tests/test_account_utils.py:356]
- `test_get_groups_which_user_can_manage_customer_user` (function) — [saleor/graphql/account/tests/test_account_utils.py:380]
- `test_get_out_of_scope_users_user_has_rights_to_manage_all_users` (function) — [saleor/graphql/account/tests/test_account_utils.py:391]
- `test_get_out_of_scope_users_for_admin_user` (function) — [saleor/graphql/account/tests/test_account_utils.py:419]
- `test_get_out_of_scope_users_return_some_users` (function) — [saleor/graphql/account/tests/test_account_utils.py:442]
- `test_get_group_to_permissions_and_users_mapping` (function) — [saleor/graphql/account/tests/test_account_utils.py:471]
- `test_get_users_and_look_for_permissions_in_groups_with_manage_staff` (function) — [saleor/graphql/account/tests/test_account_utils.py:518]
- `test_look_for_permission_in_users_with_manage_staff` (function) — [saleor/graphql/account/tests/test_account_utils.py:554]
- `test_get_not_manageable_permissions_after_group_deleting` (function) — [saleor/graphql/account/tests/test_account_utils.py:594]
- `test_get_not_manageable_permissions_after_group_deleting_some_cannot_be_manage` (function) — [saleor/graphql/account/tests/test_account_utils.py:635]
- `test_get_not_manageable_permissions_removing_users_from_group` (function) — [saleor/graphql/account/tests/test_account_utils.py:677]
- `test_get_not_manageable_perms_removing_users_from_group_user_from_group_can_manage` (function) — [saleor/graphql/account/tests/test_account_utils.py:691]
- `test_get_notmanageable_perms_removing_users_from_group_user_out_of_group_can_manage` (function) — [saleor/graphql/account/tests/test_account_utils.py:713]
- `test_get_not_manageable_perms_removing_users_from_group_some_cannot_be_manage` (function) — [saleor/graphql/account/tests/test_account_utils.py:735]
- `test_get_not_manageable_permissions_when_deactivate_or_remove_user_no_permissions` (function) — [saleor/graphql/account/tests/test_account_utils.py:766]
- `test_get_not_manageable_permissions_when_deactivate_or_remove_users_some_perms` (function) — [saleor/graphql/account/tests/test_account_utils.py:797]
- _…and 14 more in this file_

**`saleor/graphql/account/tests/test_i18n.py`**

- `test_validate_address` (function) — [saleor/graphql/account/tests/test_i18n.py:16]
- `test_validate_address_invalid_postal_code` (function) — [saleor/graphql/account/tests/test_i18n.py:39]
- `test_validate_address_no_country_code` (function) — [saleor/graphql/account/tests/test_i18n.py:64]
- `test_validate_address_no_city` (function) — [saleor/graphql/account/tests/test_i18n.py:89]
- `test_skip_address_validation_mutation_not_supported` (function) — [saleor/graphql/account/tests/test_i18n.py:137]
- `test_skip_validation_multiple_invalid_fields` (function) — [saleor/graphql/account/tests/test_i18n.py:168]
- `test_skip_address_validation_missing_required_fields` (function) — [saleor/graphql/account/tests/test_i18n.py:211]
- `test_skip_address_validation_with_correct_input_run_normalization` (function) — [saleor/graphql/account/tests/test_i18n.py:240]
- `test_skip_address_validation_with_incorrect_input_skip_normalization` (function) — [saleor/graphql/account/tests/test_i18n.py:271]
- `test_skip_address_validation_logging` (function) — [saleor/graphql/account/tests/test_i18n.py:306]
- `test_address_validation_no_logging` (function) — [saleor/graphql/account/tests/test_i18n.py:340]

**`saleor/graphql/account/tests/utils.py`**

- `convert_dict_keys_to_camel_case` (function) — [saleor/graphql/account/tests/utils.py:4]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/account/tests/__init__.py` (1 lines)
- `saleor/graphql/account/tests/test_account_utils.py` (1079 lines)
- `saleor/graphql/account/tests/test_i18n.py` (369 lines)
- `saleor/graphql/account/tests/utils.py` (14 lines)

## Interactions

- Imports from: `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....account.models.Address`
- `....account.models.Group`
- `....account.models.User`
- `....account.tests.fixtures.user.dangerously_create_test_user`
- `....app.models.App`
- `....channel.models.Channel`
- `....checkout.AddressType`
- `...core.utils.snake_to_camel_case`
- `...tests.utils.get_graphql_content`
- `..i18n.I18nMixin`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `f49d9e58cac2` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
