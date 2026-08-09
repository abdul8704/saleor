## Purpose

`saleor/account/tests` (`saleor/account/tests`) groups 9 source file(s) exposing 70 top-level declaration(s).

## Public surface

**`saleor/account/tests/fixtures/user.py`**

- `dangerously_get_or_create_superuser` (function) — [saleor/account/tests/fixtures/user.py:9]
- `dangerously_create_test_user` (function) — [saleor/account/tests/fixtures/user.py:29]
- `customer_user` (function) — [saleor/account/tests/fixtures/user.py:60]
- `customer_user2` (function) — [saleor/account/tests/fixtures/user.py:79]
- `customer_users` (function) — [saleor/account/tests/fixtures/user.py:96]
- `admin_user` (function) — [saleor/account/tests/fixtures/user.py:113]
- `staff_user` (function) — [saleor/account/tests/fixtures/user.py:125]
- `staff_users` (function) — [saleor/account/tests/fixtures/user.py:136]

**`saleor/account/tests/test_account_command.py`**

- `test_createsuperuser_command` (function) — [saleor/account/tests/test_account_command.py:9]
- `test_createsuperuser_command_dont_override_group` (function) — [saleor/account/tests/test_account_command.py:24]
- `test_createsuperuser_command_email_from_settings` (function) — [saleor/account/tests/test_account_command.py:41]

**`saleor/account/tests/test_account.py`**

- `test_address_form_for_country` (function) — [saleor/account/tests/test_account.py:19]
- `test_address_form_postal_code_validation` (function) — [saleor/account/tests/test_account.py:57]
- `test_address_form_Japanese_city_is_excluded_from_normalization` (function) — [saleor/account/tests/test_account.py:73]
- `test_city_is_allowed_in_Japanese_addresses` (function) — [saleor/account/tests/test_account.py:94]
- `test_address_form_long_street_address_validation` (function) — [saleor/account/tests/test_account.py:106]
- `test_address_form_phone_number_validation` (function) — [saleor/account/tests/test_account.py:143]
- `test_get_address_form` (function) — [saleor/account/tests/test_account.py:178]
- `test_get_address_form_no_country_code` (function) — [saleor/account/tests/test_account.py:189]
- `test_country_aware_form_has_only_supported_countries` (function) — [saleor/account/tests/test_account.py:194]
- `test_validate_possible_number` (function) — [saleor/account/tests/test_account.py:226]
- `test_address_as_data` (function) — [saleor/account/tests/test_account.py:234]
- `test_copy_address` (function) — [saleor/account/tests/test_account.py:254]
- `test_compare_addresses_with_country_object` (function) — [saleor/account/tests/test_account.py:260]
- `test_compare_addresses_different_country` (function) — [saleor/account/tests/test_account.py:267]
- `test_get_full_name_user_with_names` (function) — [saleor/account/tests/test_account.py:283]
- `test_get_full_name_user_with_address` (function) — [saleor/account/tests/test_account.py:299]
- `test_get_full_name` (function) — [saleor/account/tests/test_account.py:317]
- `test_customers_doesnt_return_duplicates` (function) — [saleor/account/tests/test_account.py:329]
- `test_customers_show_staff_with_order` (function) — [saleor/account/tests/test_account.py:347]
- `test_substitute_invalid_values` (function) — [saleor/account/tests/test_account.py:373]
- `test_validate_address_switzerland_preserves_country_area_when_flag_enabled` (function) — [saleor/account/tests/test_account.py:397]
- `test_validate_address_switzerland_removes_country_area_when_flag_disabled` (function) — [saleor/account/tests/test_account.py:421]

**`saleor/account/tests/test_notifications.py`**

- `test_get_default_user_payload` (function) — [saleor/account/tests/test_notifications.py:15]
- `test_send_email_request_change` (function) — [saleor/account/tests/test_notifications.py:30]
- `test_send_email_changed_notification` (function) — [saleor/account/tests/test_notifications.py:72]
- `test_send_password_reset_notification` (function) — [saleor/account/tests/test_notifications.py:109]

**`saleor/account/tests/test_search.py`**

- `test_update_user_search_vector` (function) — [saleor/account/tests/test_search.py:4]
- `test_update_user_search_vector_no_addresses` (function) — [saleor/account/tests/test_search.py:17]
- `test_update_user_search_vector_without_save` (function) — [saleor/account/tests/test_search.py:30]

**`saleor/account/tests/test_throttling.py`**

- `test_get_delay_time` (function) — [saleor/account/tests/test_throttling.py:41]
- `test_authenticate_successful_first_attempt` (function) — [saleor/account/tests/test_throttling.py:51]
- `test_authenticate_successful_subsequent_attempt` (function) — [saleor/account/tests/test_throttling.py:86]
- `test_authenticate_incorrect_password_non_existing_email_first_attempt` (function) — [saleor/account/tests/test_throttling.py:126]
- `test_authenticate_incorrect_password_non_existing_email_subsequent_attempt` (function) — [saleor/account/tests/test_throttling.py:162]
- `test_authenticate_incorrect_password_existing_email_first_attempt` (function) — [saleor/account/tests/test_throttling.py:203]
- `test_authenticate_incorrect_password_existing_email_subsequent_attempt` (function) — [saleor/account/tests/test_throttling.py:237]
- `test_authenticate_unidentified_ip_address` (function) — [saleor/account/tests/test_throttling.py:277]
- `test_authenticate_login_attempt_delayed` (function) — [saleor/account/tests/test_throttling.py:292]
- `test_authenticate_race_condition` (function) — [saleor/account/tests/test_throttling.py:331]
- `login_attempt` (function) — [saleor/account/tests/test_throttling.py:349]
- `test_authenticate_incorrect_credentials_max_attempts` (function) — [saleor/account/tests/test_throttling.py:368]

**`saleor/account/tests/test_utils.py`**

- `test_is_user_address_limit_reached_true` (function) — [saleor/account/tests/test_utils.py:22]
- `test_is_user_address_limit_reached_false` (function) — [saleor/account/tests/test_utils.py:36]
- `test_store_user_address_uses_existing_one` (function) — [saleor/account/tests/test_utils.py:47]
- `test_store_user_address_uses_existing_one_despite_duplicated` (function) — [saleor/account/tests/test_utils.py:60]
- `test_store_user_address_create_new_address_if_not_associated` (function) — [saleor/account/tests/test_utils.py:74]
- `test_store_user_address_address_not_saved` (function) — [saleor/account/tests/test_utils.py:86]
- `test_remove_the_oldest_user_address` (function) — [saleor/account/tests/test_utils.py:100]
- `test_remove_the_oldest_user_address_if_address_limit_is_reached_limit_not_reached` (function) — [saleor/account/tests/test_utils.py:128]
- `test_remove_the_oldest_user_address_if_address_limit_is_reached_limit_reached` (function) — [saleor/account/tests/test_utils.py:143]
- `users_with_similar_emails` (function) — [saleor/account/tests/test_utils.py:158]
- `test_email_case_sensitivity` (function) — [saleor/account/tests/test_utils.py:188]
- `get_user_groups_permissions_user_without_any_group` (function) — [saleor/account/tests/test_utils.py:197]
- `get_user_groups_permissions_user` (function) — [saleor/account/tests/test_utils.py:205]
- `test_send_user_event_no_webhook_sent` (function) — [saleor/account/tests/test_utils.py:224]
- `test_send_user_event_customer_created_event` (function) — [saleor/account/tests/test_utils.py:247]
- `test_send_user_event_customer_updated_event` (function) — [saleor/account/tests/test_utils.py:270]
- `test_send_user_event_staff_created_event` (function) — [saleor/account/tests/test_utils.py:293]
- `test_send_user_event_staff_updated_event` (function) — [saleor/account/tests/test_utils.py:316]

## How it works

The module's files, as provided to this run:

- `saleor/account/tests/__init__.py` (1 lines)
- `saleor/account/tests/fixtures/__init__.py` (1 lines)
- `saleor/account/tests/fixtures/user.py` (154 lines)
- `saleor/account/tests/test_account_command.py` (53 lines)
- `saleor/account/tests/test_account.py` (442 lines)
- `saleor/account/tests/test_notifications.py` (150 lines)
- `saleor/account/tests/test_search.py` (41 lines)
- `saleor/account/tests/test_throttling.py` (408 lines)
- `saleor/account/tests/test_utils.py` (332 lines)

## Interactions

- Imports from: `saleor/account`, `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....account.models.Group`
- `....account.models.User`
- `....account.models.UserManager`
- `....permission.enums.get_permissions`
- `...checkout.AddressType`
- `...core.notify.NotifyEventType`
- `...core.notify.UserNotifyEvent`
- `...core.tests.utils.get_site_context_payload`
- `...core.utils.url.prepare_url`
- `...forms`
- `...graphql.core.utils.to_global_id_or_none`
- `...i18n`
- `...notifications`
- `...order.models.Order`
- `...plugins.manager.get_plugins_manager`
- `...tests.race_condition`
- `..error_codes.AccountErrorCode`
- `..i18n_valid_address_extension.VALID_ADDRESS_EXTENSION_MAP`
- `..models.Address`
- `..models.Group`
- `..models.User`
- `..notifications.get_default_user_payload`
- `..search.update_user_search_vector`
- `..validators.validate_possible_number`
- `.fixtures.user.dangerously_create_test_user`
- `.user.*  # noqa: F403`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c131a9ad9f11` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
