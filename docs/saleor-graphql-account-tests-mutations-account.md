## Purpose

`saleor/graphql/account/tests/mutations/account` (`saleor/graphql/account/tests/mutations/account`) groups 14 source file(s) exposing 110 top-level declaration(s).

## Public surface

**`saleor/graphql/account/tests/mutations/account/conftest.py`**

- `throttling_disabled` (function) — [saleor/graphql/account/tests/mutations/account/conftest.py:44]

**`saleor/graphql/account/tests/mutations/account/test_account_address_create.py`**

- `test_customer_create_address` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_create.py:44]
- `test_customer_create_address_trigger_webhook` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_create.py:71]
- `test_account_address_create_return_user` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_create.py:103]
- `test_customer_create_default_address` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_create.py:112]
- `test_customer_create_address_the_oldest_address_is_deleted` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_create.py:147]
- `test_anonymous_user_create_address` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_create.py:173]
- `test_address_not_created_after_validation_fails` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_create.py:180]
- `test_customer_create_address_skip_validation` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_create.py:205]
- `test_account_address_create_by_app` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_create.py:223]
- `test_account_address_create_by_app_no_permissions` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_create.py:246]
- `test_account_address_create_by_user_with_customer_id` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_create.py:260]
- `test_account_address_create_by_app_invalid_customer_id` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_create.py:283]
- `test_account_address_create_by_app_no_customer_id` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_create.py:307]
- `test_account_address_create_by_app_skip_validation` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_create.py:330]
- `test_account_address_create_by_app_skip_validation_no_permissions` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_create.py:365]

**`saleor/graphql/account/tests/mutations/account/test_account_address_delete.py`**

- `test_customer_delete_own_address` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_delete.py:25]
- `test_customer_delete_address_trigger_webhook` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_delete.py:43]
- `test_customer_delete_address_for_other` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_delete.py:75]

**`saleor/graphql/account/tests/mutations/account/test_account_address_update.py`**

- `test_customer_update_own_address` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_update.py:33]
- `test_customer_address_update_trigger_webhook` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_update.py:63]
- `test_update_address_as_anonymous_user` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_update.py:104]
- `test_customer_update_own_address_not_updated_when_validation_fails` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_update.py:118]
- `test_customer_update_address_for_other` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_update.py:138]
- `test_customer_update_address_skip_validation` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_update.py:153]
- `test_account_address_update_by_app` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_update.py:175]
- `test_account_address_update_by_app_skip_validation` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_update.py:205]
- `test_account_address_update_by_app_skip_validation_no_permissions` (function) — [saleor/graphql/account/tests/mutations/account/test_account_address_update.py:237]

**`saleor/graphql/account/tests/mutations/account/test_account_delete.py`**

- `test_account_delete` (function) — [saleor/graphql/account/tests/mutations/account/test_account_delete.py:32]
- `test_account_delete_user_never_log_in` (function) — [saleor/graphql/account/tests/mutations/account/test_account_delete.py:71]
- `test_account_delete_log_out_after_deletion_request` (function) — [saleor/graphql/account/tests/mutations/account/test_account_delete.py:84]
- `test_account_delete_invalid_token` (function) — [saleor/graphql/account/tests/mutations/account/test_account_delete.py:104]
- `test_account_delete_rejects_token_for_other_mutation` (function) — [saleor/graphql/account/tests/mutations/account/test_account_delete.py:116]
- `test_account_delete_accepts_legacy_account_delete_token` (function) — [saleor/graphql/account/tests/mutations/account/test_account_delete.py:150]
- `test_account_delete_anonymous_user` (function) — [saleor/graphql/account/tests/mutations/account/test_account_delete.py:168]
- `test_account_delete_staff_user` (function) — [saleor/graphql/account/tests/mutations/account/test_account_delete.py:175]
- `test_account_delete_other_customer_token` (function) — [saleor/graphql/account/tests/mutations/account/test_account_delete.py:188]
- `test_account_delete_webhook_event_triggered` (function) — [saleor/graphql/account/tests/mutations/account/test_account_delete.py:205]

**`saleor/graphql/account/tests/mutations/account/test_account_register.py`**

- `test_customer_register` (function) — [saleor/graphql/account/tests/mutations/account/test_account_register.py:109]
- `test_customer_register_twice` (function) — [saleor/graphql/account/tests/mutations/account/test_account_register.py:187]
- `test_customer_register_generates_valid_token` (function) — [saleor/graphql/account/tests/mutations/account/test_account_register.py:293]
- `test_customer_register_disabled_email_confirmation` (function) — [saleor/graphql/account/tests/mutations/account/test_account_register.py:334]
- `test_customer_register_no_redirect_url` (function) — [saleor/graphql/account/tests/mutations/account/test_account_register.py:358]
- `test_customer_register_upper_case_email` (function) — [saleor/graphql/account/tests/mutations/account/test_account_register.py:375]
- `test_customer_register_no_channel_email_confirmation_unset` (function) — [saleor/graphql/account/tests/mutations/account/test_account_register.py:394]
- `test_account_register_properly_filter_errors` (function) — [saleor/graphql/account/tests/mutations/account/test_account_register.py:427]
- `test_account_register_returns_empty_id` (function) — [saleor/graphql/account/tests/mutations/account/test_account_register.py:455]
- `test_customer_register_race_codition` (function) — [saleor/graphql/account/tests/mutations/account/test_account_register.py:489]
- `create_new_user` (function) — [saleor/graphql/account/tests/mutations/account/test_account_register.py:513]
- `test_validates_password_length` (function) — [saleor/graphql/account/tests/mutations/account/test_account_register.py:541]

**`saleor/graphql/account/tests/mutations/account/test_account_request_deletion.py`**

- `test_account_request_deletion` (function) — [saleor/graphql/account/tests/mutations/account/test_account_request_deletion.py:30]
- `test_account_request_deletion_send_account_delete_requested_event` (function) — [saleor/graphql/account/tests/mutations/account/test_account_request_deletion.py:71]
- `test_account_request_deletion_token_validation` (function) — [saleor/graphql/account/tests/mutations/account/test_account_request_deletion.py:101]
- `test_account_request_deletion_anonymous_user` (function) — [saleor/graphql/account/tests/mutations/account/test_account_request_deletion.py:141]
- `test_account_request_deletion_storefront_hosts_not_allowed` (function) — [saleor/graphql/account/tests/mutations/account/test_account_request_deletion.py:149]
- `test_account_request_deletion_all_storefront_hosts_allowed` (function) — [saleor/graphql/account/tests/mutations/account/test_account_request_deletion.py:169]
- `test_account_request_deletion_subdomain` (function) — [saleor/graphql/account/tests/mutations/account/test_account_request_deletion.py:215]

**`saleor/graphql/account/tests/mutations/account/test_account_set_default_address.py`**

- `test_customer_set_address_as_default` (function) — [saleor/graphql/account/tests/mutations/account/test_account_set_default_address.py:18]
- `test_customer_change_default_address` (function) — [saleor/graphql/account/tests/mutations/account/test_account_set_default_address.py:53]
- `test_customer_change_default_address_invalid_address` (function) — [saleor/graphql/account/tests/mutations/account/test_account_set_default_address.py:83]

**`saleor/graphql/account/tests/mutations/account/test_account_update.py`**

- `test_logged_customer_updates_language_code` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:59]
- `test_logged_customer_update_names` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:76]
- `test_logged_customer_update_addresses` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:94]
- `test_logged_customer_update_addresses_invalid_shipping_address` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:142]
- `test_logged_customer_update_addresses_invalid_billing_address` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:166]
- `test_logged_customer_update_anonymous_user` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:190]
- `test_logged_customer_updates_metadata` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:197]
- `test_logged_customer_update_names_trigger_gift_card_search_vector_update` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:216]
- `test_logged_customer_update_address_skip_validation` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:243]
- `test_account_update_by_app` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:266]
- `test_account_update_by_app_no_permissions` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:295]
- `test_account_update_by_user_with_customer_id` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:312]
- `test_account_address_create_by_app_invalid_customer_id` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:335]
- `test_account_address_create_by_app_no_customer_id` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:362]
- `test_account_update_address_by_app_skip_validation` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:385]
- `test_account_update_address_by_app_skip_validation_no_permissions` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:423]
- `test_account_update_sends_customer_updated_webhook` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:452]
- `test_account_metadata_update_with_legacy_webhook_on` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:484]
- `test_account_metadata_update_with_legacy_webhook_off` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:516]
- `test_account_metadata_and_data_update_sends_both_webhooks` (function) — [saleor/graphql/account/tests/mutations/account/test_account_update.py:549]

**`saleor/graphql/account/tests/mutations/account/test_confirm_account.py`**

- `account_merging_enabled` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_account.py:42]
- `test_account_confirmation` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_account.py:58]
- `test_account_confirmation_invalid_user` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_account.py:119]
- `test_account_confirmation_requires_valid_password_when_require_password_mode` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_account.py:194]
- `test_account_confirmation_no_password_required_when_merging_disabled` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_account.py:273]
- `test_account_confirmation_rate_limits_password` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_account.py:326]
- `test_account_confirmation_invalid_token` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_account.py:374]
- `test_account_confirmation_rejects_token_for_wrong_scope` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_account.py:405]
- `test_account_confirmation_accepts_legacy_account_confirm_token` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_account.py:471]
- `test_account_confirmation_rejects_disabled_accounts` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_account.py:516]
- `test_account_confirmation_rejects_already_confirmed` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_account.py:585]

**`saleor/graphql/account/tests/mutations/account/test_confirm_email_change.py`**

- `request_email_change` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_email_change.py:14]
- `test_email_update` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_email_change.py:55]
- `test_email_update_to_existing_email` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_email_change.py:89]
- `test_account_email_changed_webhook_event_triggered` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_email_change.py:117]
- `test_confirm_email_change_other_user_token` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_email_change.py:154]
- `test_cannot_confirm_email_change_if_old_email_mismatches` (function) — [saleor/graphql/account/tests/mutations/account/test_confirm_email_change.py:198]

**`saleor/graphql/account/tests/mutations/account/test_request_email_change.py`**

- `test_account_request_email_change_with_upper_case_email` (function) — [saleor/graphql/account/tests/mutations/account/test_request_email_change.py:21]
- `test_request_email_change` (function) — [saleor/graphql/account/tests/mutations/account/test_request_email_change.py:88]
- `test_request_email_change_to_existing_email` (function) — [saleor/graphql/account/tests/mutations/account/test_request_email_change.py:102]
- `test_request_email_change_with_invalid_redirect_url` (function) — [saleor/graphql/account/tests/mutations/account/test_request_email_change.py:179]
- `test_request_email_change_with_invalid_password` (function) — [saleor/graphql/account/tests/mutations/account/test_request_email_change.py:201]
- `test_request_email_change_send_event` (function) — [saleor/graphql/account/tests/mutations/account/test_request_email_change.py:217]
- `test_request_email_change_but_no_channels_exist` (function) — [saleor/graphql/account/tests/mutations/account/test_request_email_change.py:247]

**`saleor/graphql/account/tests/mutations/account/test_send_confirmation_email.py`**

- `test_send_confirmation_email` (function) — [saleor/graphql/account/tests/mutations/account/test_send_confirmation_email.py:34]
- `test_send_confirmation_email_on_cooldown` (function) — [saleor/graphql/account/tests/mutations/account/test_send_confirmation_email.py:85]
- `test_send_confirmation_email_after_cooldown` (function) — [saleor/graphql/account/tests/mutations/account/test_send_confirmation_email.py:116]
- `test_send_confirmation_email_user_already_confirmed` (function) — [saleor/graphql/account/tests/mutations/account/test_send_confirmation_email.py:141]
- `test_send_confirmation_email_confirmation_disabled` (function) — [saleor/graphql/account/tests/mutations/account/test_send_confirmation_email.py:170]
- `test_send_confirmation_email_generates_valid_token` (function) — [saleor/graphql/account/tests/mutations/account/test_send_confirmation_email.py:201]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/account/tests/mutations/account/__init__.py` (1 lines)
- `saleor/graphql/account/tests/mutations/account/conftest.py` (48 lines)
- `saleor/graphql/account/tests/mutations/account/test_account_address_create.py` (384 lines)
- `saleor/graphql/account/tests/mutations/account/test_account_address_delete.py` (83 lines)
- `saleor/graphql/account/tests/mutations/account/test_account_address_update.py` (256 lines)
- `saleor/graphql/account/tests/mutations/account/test_account_delete.py` (227 lines)
- `saleor/graphql/account/tests/mutations/account/test_account_register.py` (586 lines)
- `saleor/graphql/account/tests/mutations/account/test_account_request_deletion.py` (252 lines)
- `saleor/graphql/account/tests/mutations/account/test_account_set_default_address.py` (98 lines)
- `saleor/graphql/account/tests/mutations/account/test_account_update.py` (585 lines)
- `saleor/graphql/account/tests/mutations/account/test_confirm_account.py` (642 lines)
- `saleor/graphql/account/tests/mutations/account/test_confirm_email_change.py` (234 lines)
- `saleor/graphql/account/tests/mutations/account/test_request_email_change.py` (264 lines)
- `saleor/graphql/account/tests/mutations/account/test_send_confirmation_email.py` (229 lines)

## Interactions

- Imports from: `saleor/graphql/account/mutations/account`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `......account.error_codes.AccountErrorCode`
- `......account.error_codes.SendConfirmationEmailErrorCode`
- `......account.events`
- `......account.models.Address`
- `......account.models.User`
- `......account.notifications.get_default_user_payload`
- `......account.tasks.finish_creating_user`
- `......channel.models.Channel`
- `......checkout.AddressType`
- `......core.jwt.JWT_CONFIRM_CHANGE_EMAIL_TYPE`
- `......core.jwt.create_token`
- `......core.jwt.jwt_decode`
- `......core.notify.NotifyEventType`
- `......core.tests.utils.get_site_context_payload`
- `......core.tokens.account_confirm_token_generator`
- `......core.tokens.account_delete_token_generator`
- `......core.utils.url.prepare_url`
- `......giftcard.search.update_gift_cards_search_vector`
- `......settings.AUTH_PASSWORD_VALIDATORS`
- `......site.AccountConfirmMode`
- `......tests.race_condition`
- `......thumbnail.models.Thumbnail`
- `......webhook.event_types.WebhookEventAsyncType`
- `.....tests.fixtures.ApiClient`
- `.....tests.utils.assert_no_permission`
- `.....tests.utils.get_graphql_content`
- `..utils.generate_address_webhook_call_args`
- `.conftest.CONFIRM_EMAIL_UPDATE_QUERY`
- `.conftest.REQUEST_EMAIL_CHANGE_QUERY`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `24a92c1e21d7` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
