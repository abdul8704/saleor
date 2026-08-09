## Purpose

`saleor/graphql/account/mutations/staff` (`saleor/graphql/account/mutations/staff`) groups 15 source file(s) exposing 70 top-level declaration(s).

## Public surface

**`saleor/graphql/account/mutations/staff/address_create.py`**

- `AddressCreate` (class) — [saleor/graphql/account/mutations/staff/address_create.py:22]
- `Arguments` (class) — [saleor/graphql/account/mutations/staff/address_create.py:27]
- `Meta` (class) — [saleor/graphql/account/mutations/staff/address_create.py:35]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/staff/address_create.py:51]
- `post_save_action` (function) — [saleor/graphql/account/mutations/staff/address_create.py:70]

**`saleor/graphql/account/mutations/staff/address_delete.py`**

- `AddressDelete` (class) — [saleor/graphql/account/mutations/staff/address_delete.py:11]
- `Meta` (class) — [saleor/graphql/account/mutations/staff/address_delete.py:12]

**`saleor/graphql/account/mutations/staff/address_set_default.py`**

- `AddressSetDefault` (class) — [saleor/graphql/account/mutations/staff/address_set_default.py:19]
- `Arguments` (class) — [saleor/graphql/account/mutations/staff/address_set_default.py:22]
- `Meta` (class) — [saleor/graphql/account/mutations/staff/address_set_default.py:29]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/staff/address_set_default.py:43]

**`saleor/graphql/account/mutations/staff/address_update.py`**

- `AddressUpdate` (class) — [saleor/graphql/account/mutations/staff/address_update.py:12]
- `Meta` (class) — [saleor/graphql/account/mutations/staff/address_update.py:13]

**`saleor/graphql/account/mutations/staff/base.py`**

- `UserDelete` (class) — [saleor/graphql/account/mutations/staff/base.py:5]
- `Meta` (class) — [saleor/graphql/account/mutations/staff/base.py:6]

**`saleor/graphql/account/mutations/staff/customer_create.py`**

- `CustomerCreate` (class) — [saleor/graphql/account/mutations/staff/customer_create.py:27]
- `Meta` (class) — [saleor/graphql/account/mutations/staff/customer_create.py:28]
- `save` (function) — [saleor/graphql/account/mutations/staff/customer_create.py:102]
- `post_save_action` (function) — [saleor/graphql/account/mutations/staff/customer_create.py:133]

**`saleor/graphql/account/mutations/staff/customer_delete.py`**

- `CustomerDelete` (class) — [saleor/graphql/account/mutations/staff/customer_delete.py:18]
- `Meta` (class) — [saleor/graphql/account/mutations/staff/customer_delete.py:19]
- `Arguments` (class) — [saleor/graphql/account/mutations/staff/customer_delete.py:34]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/staff/customer_delete.py:42]
- `clean_instance` (function) — [saleor/graphql/account/mutations/staff/customer_delete.py:49]
- `post_save_action` (function) — [saleor/graphql/account/mutations/staff/customer_delete.py:56]

**`saleor/graphql/account/mutations/staff/customer_update.py`**

- `CustomerUpdate` (class) — [saleor/graphql/account/mutations/staff/customer_update.py:30]
- `Arguments` (class) — [saleor/graphql/account/mutations/staff/customer_update.py:31]
- `Meta` (class) — [saleor/graphql/account/mutations/staff/customer_update.py:41]
- `generate_events` (function) — [saleor/graphql/account/mutations/staff/customer_update.py:66]
- `update_gift_card_search_vector` (function) — [saleor/graphql/account/mutations/staff/customer_update.py:116]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/staff/customer_update.py:135]
- `get_instance` (function) — [saleor/graphql/account/mutations/staff/customer_update.py:229]

**`saleor/graphql/account/mutations/staff/staff_create.py`**

- `StaffInput` (class) — [saleor/graphql/account/mutations/staff/staff_create.py:31]
- `StaffCreateInput` (class) — [saleor/graphql/account/mutations/staff/staff_create.py:39]
- `Meta` (class) — [saleor/graphql/account/mutations/staff/staff_create.py:47]
- `StaffCreate` (class) — [saleor/graphql/account/mutations/staff/staff_create.py:52]
- `Arguments` (class) — [saleor/graphql/account/mutations/staff/staff_create.py:53]
- `Meta` (class) — [saleor/graphql/account/mutations/staff/staff_create.py:58]
- `check_permissions` (function) — [saleor/graphql/account/mutations/staff/staff_create.py:89]
- `clean_input` (function) — [saleor/graphql/account/mutations/staff/staff_create.py:100]
- `clean_groups` (function) — [saleor/graphql/account/mutations/staff/staff_create.py:128]
- `ensure_requestor_can_manage_groups` (function) — [saleor/graphql/account/mutations/staff/staff_create.py:135]
- `clean_is_active` (function) — [saleor/graphql/account/mutations/staff/staff_create.py:160]
- `save` (function) — [saleor/graphql/account/mutations/staff/staff_create.py:164]
- `post_save_action` (function) — [saleor/graphql/account/mutations/staff/staff_create.py:204]
- `get_instance` (function) — [saleor/graphql/account/mutations/staff/staff_create.py:209]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/staff/staff_create.py:226]

**`saleor/graphql/account/mutations/staff/staff_delete.py`**

- `StaffDelete` (class) — [saleor/graphql/account/mutations/staff/staff_delete.py:18]
- `Meta` (class) — [saleor/graphql/account/mutations/staff/staff_delete.py:19]
- `Arguments` (class) — [saleor/graphql/account/mutations/staff/staff_delete.py:36]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/staff/staff_delete.py:40]

**`saleor/graphql/account/mutations/staff/staff_update.py`**

- `StaffUpdateInput` (class) — [saleor/graphql/account/mutations/staff/staff_update.py:28]
- `Meta` (class) — [saleor/graphql/account/mutations/staff/staff_update.py:37]
- `StaffUpdate` (class) — [saleor/graphql/account/mutations/staff/staff_update.py:42]
- `Arguments` (class) — [saleor/graphql/account/mutations/staff/staff_update.py:43]
- `Meta` (class) — [saleor/graphql/account/mutations/staff/staff_update.py:49]
- `clean_input` (function) — [saleor/graphql/account/mutations/staff/staff_update.py:71]
- `clean_groups` (function) — [saleor/graphql/account/mutations/staff/staff_update.py:90]
- `clean_is_active` (function) — [saleor/graphql/account/mutations/staff/staff_update.py:101]
- `check_if_deactivating_superuser_or_own_account` (function) — [saleor/graphql/account/mutations/staff/staff_update.py:120]
- `check_if_deactivating_left_not_manageable_permissions` (function) — [saleor/graphql/account/mutations/staff/staff_update.py:145]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/staff/staff_update.py:182]
- `post_save_action` (function) — [saleor/graphql/account/mutations/staff/staff_update.py:200]

**`saleor/graphql/account/mutations/staff/user_avatar_delete.py`**

- `UserAvatarDelete` (class) — [saleor/graphql/account/mutations/staff/user_avatar_delete.py:15]
- `Meta` (class) — [saleor/graphql/account/mutations/staff/user_avatar_delete.py:18]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/staff/user_avatar_delete.py:26]

**`saleor/graphql/account/mutations/staff/user_avatar_update.py`**

- `UserAvatarUpdate` (class) — [saleor/graphql/account/mutations/staff/user_avatar_update.py:17]
- `Arguments` (class) — [saleor/graphql/account/mutations/staff/user_avatar_update.py:20]
- `Meta` (class) — [saleor/graphql/account/mutations/staff/user_avatar_update.py:26]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/staff/user_avatar_update.py:38]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/account/mutations/staff/__init__.py` (27 lines)
- `saleor/graphql/account/mutations/staff/address_create.py` (72 lines)
- `saleor/graphql/account/mutations/staff/address_delete.py` (25 lines)
- `saleor/graphql/account/mutations/staff/address_set_default.py` (68 lines)
- `saleor/graphql/account/mutations/staff/address_update.py` (26 lines)
- `saleor/graphql/account/mutations/staff/base.py` (7 lines)
- `saleor/graphql/account/mutations/staff/customer_create.py` (174 lines)
- `saleor/graphql/account/mutations/staff/customer_delete.py` (58 lines)
- `saleor/graphql/account/mutations/staff/customer_update.py` (240 lines)
- `saleor/graphql/account/mutations/staff/staff_create.py` (251 lines)
- `saleor/graphql/account/mutations/staff/staff_delete.py` (61 lines)
- `saleor/graphql/account/mutations/staff/staff_update.py` (202 lines)
- `saleor/graphql/account/mutations/staff/user_avatar_delete.py` (31 lines)
- `saleor/graphql/account/mutations/staff/user_avatar_update.py` (49 lines)
- `saleor/graphql/account/mutations/staff/utils.py` (12 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....account.error_codes.AccountErrorCode`
- `.....account.events`
- `.....account.models`
- `.....account.notifications.send_set_password_notification`
- `.....account.search.USER_SEARCH_FIELDS`
- `.....account.search.update_user_search_vector`
- `.....account.utils`
- `.....checkout.AddressType`
- `.....core.exceptions.PermissionDenied`
- `.....core.tokens.password_reset_token_generator`
- `.....core.tracing.traced_atomic_transaction`
- `.....core.utils.update_mutation_manager.InstanceTracker`
- `.....core.utils.url.prepare_url`
- `.....core.utils.url.validate_storefront_url`
- `.....giftcard.search.mark_gift_cards_search_index_as_dirty`
- `.....giftcard.utils.assign_user_gift_cards`
- `.....giftcard.utils.deactivate_assigned_gift_cards`
- `.....giftcard.utils.get_user_gift_cards`
- `.....order.utils.match_orders_with_new_user`
- `.....permission.auth_filters.AuthorizationFilters`
- `.....permission.enums.AccountPermissions`
- `.....plugins.manager.PluginsManager`
- `.....thumbnail.models`
- `.....webhook.event_types.WebhookEventAsyncType`
- `....account.enums.AddressTypeEnum`
- `....account.mixins.AddressMetadataMixin`
- `....account.types.Address`
- `....account.types.AddressInput`
- `....account.types.User`
- `....app.dataloaders.get_app_promise`
- `....channel.utils.clean_channel`
- `....channel.utils.validate_channel`
- `....core.ResolveInfo`
- `....core.doc_category.DOC_CATEGORY_USERS`
- `....core.enums.AccountErrorCode`
- `....core.mutations.BaseMutation`
- `....core.mutations.DeprecatedModelMutation`
- `....core.mutations.ModelDeleteMutation`
- `....core.mutations.ModelWithExtRefMutation`
- `....core.types.AccountError`
- `....core.types.NonNullList`
- `....core.types.StaffError`
- `....core.types.Upload`
- `....core.utils.WebhookEventInfo`
- `....core.validators.file.clean_image_file`
- `....meta.inputs.MetadataInput`
- `....plugins.dataloaders.get_plugin_manager_promise`
- `....site.dataloaders.get_site_promise`
- `....utils.validators.check_for_duplicates`
- `...i18n.I18nMixin`
- `...mixins.AddressMetadataMixin`
- `...utils.get_groups_which_user_can_manage`
- `..base.BILLING_ADDRESS_FIELD`
- `..base.BaseAddressDelete`
- `..base.BaseAddressUpdate`
- `..base.BaseCustomerCreate`
- `..base.CustomerDeleteMixin`
- `..base.CustomerInput`
- `..base.SHIPPING_ADDRESS_FIELD`
- `..base.StaffDeleteMixin`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `8cb220154c93` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
