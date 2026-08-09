## Purpose

`saleor/graphql/account/mutations/account` (`saleor/graphql/account/mutations/account`) groups 15 source file(s) exposing 64 top-level declaration(s).

## Public surface

**`saleor/graphql/account/mutations/account/account_address_create.py`**

- `AccountAddressCreate` (class) — [saleor/graphql/account/mutations/account/account_address_create.py:24]
- `Arguments` (class) — [saleor/graphql/account/mutations/account/account_address_create.py:31]
- `Meta` (class) — [saleor/graphql/account/mutations/account/account_address_create.py:52]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/account/account_address_create.py:80]
- `save` (function) — [saleor/graphql/account/mutations/account/account_address_create.py:101]

**`saleor/graphql/account/mutations/account/account_address_delete.py`**

- `AccountAddressDelete` (class) — [saleor/graphql/account/mutations/account/account_address_delete.py:10]
- `Meta` (class) — [saleor/graphql/account/mutations/account/account_address_delete.py:11]

**`saleor/graphql/account/mutations/account/account_address_update.py`**

- `AccountAddressUpdate` (class) — [saleor/graphql/account/mutations/account/account_address_update.py:11]
- `Meta` (class) — [saleor/graphql/account/mutations/account/account_address_update.py:12]

**`saleor/graphql/account/mutations/account/account_delete.py`**

- `AccountDelete` (class) — [saleor/graphql/account/mutations/account/account_delete.py:27]
- `Arguments` (class) — [saleor/graphql/account/mutations/account/account_delete.py:28]
- `Meta` (class) — [saleor/graphql/account/mutations/account/account_delete.py:37]
- `clean_instance` (function) — [saleor/graphql/account/mutations/account/account_delete.py:53]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/account/account_delete.py:62]
- `post_save_action` (function) — [saleor/graphql/account/mutations/account/account_delete.py:101]

**`saleor/graphql/account/mutations/account/account_register.py`**

- `AccountRegisterInput` (class) — [saleor/graphql/account/mutations/account/account_register.py:26]
- `Meta` (class) — [saleor/graphql/account/mutations/account/account_register.py:55]
- `AccountRegister` (class) — [saleor/graphql/account/mutations/account/account_register.py:60]
- `Arguments` (class) — [saleor/graphql/account/mutations/account/account_register.py:70]
- `Meta` (class) — [saleor/graphql/account/mutations/account/account_register.py:79]
- `mutate` (function) — [saleor/graphql/account/mutations/account/account_register.py:106]
- `clean_redirect_url` (function) — [saleor/graphql/account/mutations/account/account_register.py:118]
- `clean_input` (function) — [saleor/graphql/account/mutations/account/account_register.py:140]
- `clean_instance` (function) — [saleor/graphql/account/mutations/account/account_register.py:162]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/account/account_register.py:176]
- `save_and_create_task` (function) — [saleor/graphql/account/mutations/account/account_register.py:232]

**`saleor/graphql/account/mutations/account/account_request_deletion.py`**

- `AccountRequestDeletion` (class) — [saleor/graphql/account/mutations/account/account_request_deletion.py:23]
- `Arguments` (class) — [saleor/graphql/account/mutations/account/account_request_deletion.py:24]
- `Meta` (class) — [saleor/graphql/account/mutations/account/account_request_deletion.py:39]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/account/account_request_deletion.py:59]

**`saleor/graphql/account/mutations/account/account_set_default_address.py`**

- `AccountSetDefaultAddress` (class) — [saleor/graphql/account/mutations/account/account_set_default_address.py:21]
- `Arguments` (class) — [saleor/graphql/account/mutations/account/account_set_default_address.py:24]
- `Meta` (class) — [saleor/graphql/account/mutations/account/account_set_default_address.py:30]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/account/account_set_default_address.py:44]

**`saleor/graphql/account/mutations/account/account_update.py`**

- `AccountInput` (class) — [saleor/graphql/account/mutations/account/account_update.py:25]
- `Meta` (class) — [saleor/graphql/account/mutations/account/account_update.py:41]
- `AccountUpdate` (class) — [saleor/graphql/account/mutations/account/account_update.py:46]
- `Arguments` (class) — [saleor/graphql/account/mutations/account/account_update.py:47]
- `Meta` (class) — [saleor/graphql/account/mutations/account/account_update.py:61]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/account/account_update.py:92]
- `save` (function) — [saleor/graphql/account/mutations/account/account_update.py:101]

**`saleor/graphql/account/mutations/account/base.py`**

- `AccountBaseInput` (class) — [saleor/graphql/account/mutations/account/base.py:7]

**`saleor/graphql/account/mutations/account/confirm_account.py`**

- `ConfirmAccount` (class) — [saleor/graphql/account/mutations/account/confirm_account.py:35]
- `Arguments` (class) — [saleor/graphql/account/mutations/account/confirm_account.py:38]
- `Meta` (class) — [saleor/graphql/account/mutations/account/confirm_account.py:56]
- `maybe_merge_account` (function) — [saleor/graphql/account/mutations/account/confirm_account.py:71]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/account/confirm_account.py:146]
- `post_save_action` (function) — [saleor/graphql/account/mutations/account/confirm_account.py:191]

**`saleor/graphql/account/mutations/account/confirm_email_change.py`**

- `ConfirmEmailChange` (class) — [saleor/graphql/account/mutations/account/confirm_email_change.py:27]
- `Arguments` (class) — [saleor/graphql/account/mutations/account/confirm_email_change.py:30]
- `Meta` (class) — [saleor/graphql/account/mutations/account/confirm_email_change.py:41]
- `get_token_payload` (function) — [saleor/graphql/account/mutations/account/confirm_email_change.py:63]
- `reject_token` (function) — [saleor/graphql/account/mutations/account/confirm_email_change.py:78]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/account/confirm_email_change.py:88]
- `post_save_action` (function) — [saleor/graphql/account/mutations/account/confirm_email_change.py:142]

**`saleor/graphql/account/mutations/account/request_email_change.py`**

- `RequestEmailChange` (class) — [saleor/graphql/account/mutations/account/request_email_change.py:24]
- `Arguments` (class) — [saleor/graphql/account/mutations/account/request_email_change.py:27]
- `Meta` (class) — [saleor/graphql/account/mutations/account/request_email_change.py:44]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/account/request_email_change.py:62]

**`saleor/graphql/account/mutations/account/send_confirmation_email.py`**

- `SendConfirmationEmail` (class) — [saleor/graphql/account/mutations/account/send_confirmation_email.py:26]
- `Arguments` (class) — [saleor/graphql/account/mutations/account/send_confirmation_email.py:27]
- `Meta` (class) — [saleor/graphql/account/mutations/account/send_confirmation_email.py:39]
- `clean_user` (function) — [saleor/graphql/account/mutations/account/send_confirmation_email.py:59]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/account/send_confirmation_email.py:92]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/account/mutations/account/confirm_account.py` (193 lines)
- `saleor/graphql/account/mutations/account/confirm_email_change.py` (150 lines)
- `saleor/graphql/account/mutations/account/account_register.py` (294 lines)
- `saleor/graphql/account/mutations/account/__init__.py` (27 lines)
- `saleor/graphql/account/mutations/account/account_address_create.py` (109 lines)
- `saleor/graphql/account/mutations/account/account_address_delete.py` (27 lines)
- `saleor/graphql/account/mutations/account/account_address_update.py` (28 lines)
- `saleor/graphql/account/mutations/account/account_delete.py` (103 lines)
- `saleor/graphql/account/mutations/account/account_request_deletion.py` (90 lines)
- `saleor/graphql/account/mutations/account/account_set_default_address.py` (68 lines)
- `saleor/graphql/account/mutations/account/account_update.py` (134 lines)
- `saleor/graphql/account/mutations/account/base.py` (12 lines)
- `saleor/graphql/account/mutations/account/request_email_change.py` (133 lines)
- `saleor/graphql/account/mutations/account/send_confirmation_email.py` (127 lines)
- `saleor/graphql/account/mutations/account/utils.py` (24 lines)

## Interactions

- Imports from: `saleor/core`
- Imported by: `saleor/graphql/account/tests/mutations/account`

Internal dependencies named in the source:

- `.....account.error_codes.AccountErrorCode`
- `.....account.error_codes.SendConfirmationEmailErrorCode`
- `.....account.models`
- `.....account.models.User`
- `.....account.notifications`
- `.....account.notifications.send_account_confirmation`
- `.....account.search`
- `.....account.search.update_user_search_vector`
- `.....account.tasks.finish_creating_user`
- `.....account.throttling.authenticate_with_throttling`
- `.....account.utils`
- `.....account.utils.RequestorAwareContext`
- `.....checkout.AddressType`
- `.....core.jwt.JWT_CONFIRM_CHANGE_EMAIL_TYPE`
- `.....core.jwt.create_token`
- `.....core.jwt.jwt_decode`
- `.....core.tokens.account_confirm_token_generator`
- `.....core.tokens.account_delete_token_generator`
- `.....core.tracing.traced_atomic_transaction`
- `.....core.utils.url.prepare_url`
- `.....core.utils.url.validate_storefront_url`
- `.....giftcard.utils.assign_user_gift_cards`
- `.....giftcard.utils.deactivate_assigned_gift_cards`
- `.....order.utils.match_orders_with_new_user`
- `.....permission.auth_filters.AuthorizationFilters`
- `.....site.AccountConfirmMode`
- `.....site.models.SiteSettings`
- `.....webhook.event_types.WebhookEventAsyncType`
- `....account.mixins.AddressMetadataMixin`
- `....channel.utils.clean_channel`
- `....core.ResolveInfo`
- `....core.SaleorContext`
- `....core.doc_category.DOC_CATEGORY_USERS`
- `....core.enums.LanguageCodeEnum`
- `....core.mutations.BaseMutation`
- `....core.mutations.DeprecatedModelMutation`
- `....core.mutations.ModelDeleteMutation`
- `....core.types.AccountError`
- `....core.types.BaseInputObjectType`
- `....core.types.NonNullList`
- `....core.types.SendConfirmationEmailError`
- `....core.utils.WebhookEventInfo`
- `....meta.inputs.MetadataInput`
- `....meta.inputs.MetadataInputDescription`
- `....plugins.dataloaders.get_plugin_manager_promise`
- `....site.dataloaders.get_site_promise`
- `...enums.AddressTypeEnum`
- `...i18n.I18nMixin`
- `...mixins.AddressMetadataMixin`
- `...mixins.AppImpersonateMixin`
- `...types.Address`
- `...types.AddressInput`
- `...types.User`
- `..base.BaseAddressDelete`
- `..base.BaseAddressUpdate`
- `..base.BaseCustomerCreate`
- `..base.INVALID_TOKEN`
- `.account_address_create.AccountAddressCreate`
- `.account_address_delete.AccountAddressDelete`
- `.account_address_update.AccountAddressUpdate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `582f6a463798` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
