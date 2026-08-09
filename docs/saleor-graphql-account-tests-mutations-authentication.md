## Purpose

`saleor/graphql/account/tests/mutations/authentication` (`saleor/graphql/account/tests/mutations/authentication`) groups 13 source file(s) exposing 86 top-level declaration(s).

## Public surface

**`saleor/graphql/account/tests/mutations/authentication/test_external_authentication.py`**

- `test_external_authentication_url_plugin_not_active` (function) — [saleor/graphql/account/tests/mutations/authentication/test_external_authentication.py:19]
- `test_external_authentication_url` (function) — [saleor/graphql/account/tests/mutations/authentication/test_external_authentication.py:30]

**`saleor/graphql/account/tests/mutations/authentication/test_external_logout.py`**

- `test_external_logout_plugin_not_active` (function) — [saleor/graphql/account/tests/mutations/authentication/test_external_logout.py:19]
- `test_external_logout` (function) — [saleor/graphql/account/tests/mutations/authentication/test_external_logout.py:30]

**`saleor/graphql/account/tests/mutations/authentication/test_external_obtain_access_tokens.py`**

- `test_external_obtain_access_tokens_plugin_not_active` (function) — [saleor/graphql/account/tests/mutations/authentication/test_external_obtain_access_tokens.py:28]
- `test_external_obtain_access_tokens` (function) — [saleor/graphql/account/tests/mutations/authentication/test_external_obtain_access_tokens.py:43]
- `test_external_obtain_access_tokens_do_not_update_last_login_when_in_threshold` (function) — [saleor/graphql/account/tests/mutations/authentication/test_external_obtain_access_tokens.py:78]
- `test_external_obtain_access_tokens_do_update_last_login_when_out_of_threshold` (function) — [saleor/graphql/account/tests/mutations/authentication/test_external_obtain_access_tokens.py:124]

**`saleor/graphql/account/tests/mutations/authentication/test_external_refresh.py`**

- `test_external_refresh_plugin_not_active` (function) — [saleor/graphql/account/tests/mutations/authentication/test_external_refresh.py:28]
- `test_external_refresh` (function) — [saleor/graphql/account/tests/mutations/authentication/test_external_refresh.py:41]
- `test_external_refresh_do_not_update_last_login_when_in_threshold` (function) — [saleor/graphql/account/tests/mutations/authentication/test_external_refresh.py:75]
- `test_external_refresh_do_update_last_login_when_out_of_threshold` (function) — [saleor/graphql/account/tests/mutations/authentication/test_external_refresh.py:118]

**`saleor/graphql/account/tests/mutations/authentication/test_external_verify.py`**

- `test_external_verify_plugin_not_active` (function) — [saleor/graphql/account/tests/mutations/authentication/test_external_verify.py:23]
- `test_external_verify` (function) — [saleor/graphql/account/tests/mutations/authentication/test_external_verify.py:31]

**`saleor/graphql/account/tests/mutations/authentication/test_password_change.py`**

- `test_password_change` (function) — [saleor/graphql/account/tests/mutations/authentication/test_password_change.py:21]
- `test_password_change_incorrect_old_password` (function) — [saleor/graphql/account/tests/mutations/authentication/test_password_change.py:40]
- `test_password_change_invalid_new_password` (function) — [saleor/graphql/account/tests/mutations/authentication/test_password_change.py:52]
- `test_password_change_user_unusable_password_fails_if_old_password_is_set` (function) — [saleor/graphql/account/tests/mutations/authentication/test_password_change.py:78]
- `test_password_change_user_unusable_password_if_old_password_is_omitted` (function) — [saleor/graphql/account/tests/mutations/authentication/test_password_change.py:98]
- `test_password_change_user_usable_password_fails_if_old_password_is_omitted` (function) — [saleor/graphql/account/tests/mutations/authentication/test_password_change.py:122]
- `test_password_change_disabled_password_login` (function) — [saleor/graphql/account/tests/mutations/authentication/test_password_change.py:141]

**`saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py`**

- `test_account_reset_password` (function) — [saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py:36]
- `test_account_reset_password_on_cooldown` (function) — [saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py:91]
- `test_account_reset_password_after_cooldown` (function) — [saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py:116]
- `test_account_reset_password_with_upper_case_email` (function) — [saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py:142]
- `test_request_password_reset_email_for_staff` (function) — [saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py:189]
- `test_account_reset_password_invalid_email` (function) — [saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py:235]
- `test_account_reset_password_user_is_inactive` (function) — [saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py:254]
- `test_account_reset_password_storefront_hosts_not_allowed` (function) — [saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py:279]
- `test_account_reset_password_all_storefront_hosts_allowed` (function) — [saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py:302]
- `test_account_reset_password_subdomain` (function) — [saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py:351]
- `test_account_reset_password_event_triggered` (function) — [saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py:394]
- `test_account_reset_password_for_not_confirmed_user` (function) — [saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py:422]
- `test_account_reset_password_no_channel_provided_multiple_channels` (function) — [saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py:483]
- `test_account_reset_password_no_channel_provided_one_channel` (function) — [saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py:545]
- `test_request_password_reset_disabled_password_login` (function) — [saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py:602]

**`saleor/graphql/account/tests/mutations/authentication/test_set_password.py`**

- `test_set_password` (function) — [saleor/graphql/account/tests/mutations/authentication/test_set_password.py:42]
- `test_set_password_confirm_user_and_match_orders` (function) — [saleor/graphql/account/tests/mutations/authentication/test_set_password.py:76]
- `test_set_password_invalid_token` (function) — [saleor/graphql/account/tests/mutations/authentication/test_set_password.py:113]
- `test_set_password_rejects_account_confirm_token` (function) — [saleor/graphql/account/tests/mutations/authentication/test_set_password.py:134]
- `test_set_password_accepts_legacy_password_reset_token` (function) — [saleor/graphql/account/tests/mutations/authentication/test_set_password.py:182]
- `test_set_password_invalid_email` (function) — [saleor/graphql/account/tests/mutations/authentication/test_set_password.py:211]
- `test_set_password_invalid_password` (function) — [saleor/graphql/account/tests/mutations/authentication/test_set_password.py:236]
- `test_set_password_disabled_password_login` (function) — [saleor/graphql/account/tests/mutations/authentication/test_set_password.py:271]

**`saleor/graphql/account/tests/mutations/authentication/test_token_create.py`**

- `test_create_token` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:51]
- `test_create_token_with_audience` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:103]
- `test_create_token_sets_cookie` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:161]
- `test_create_token_invalid_password` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:193]
- `test_create_token_invalid_email` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:210]
- `test_create_token_unconfirmed_email` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:227]
- `test_create_token_unconfirmed_user_unconfirmed_login_enabled` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:246]
- `test_create_token_deactivated_user` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:304]
- `test_create_token_active_user_logged_before` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:325]
- `test_create_token_email_case_insensitive` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:381]
- `test_create_token_do_not_update_last_login_when_in_threshold` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:403]
- `test_create_token_do_update_last_login_when_out_of_threshold` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:436]
- `test_create_token_throttling_login_attempt_delay` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:469]
- `test_create_token_throttling_unidentified_ip_address` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:511]
- `test_create_token_disabled_password_login` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:535]
- `test_create_token_disabled_password_login_for_staff` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:556]
- `test_create_token_customers_only_mode_for_customer` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:577]
- `test_create_token_enabled_mode_for_staff` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_create.py:601]

**`saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py`**

- `test_refresh_token_with_audience` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py:35]
- `test_refresh_token_get_token_from_cookie` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py:72]
- `test_refresh_token_get_token_from_input` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py:102]
- `test_refresh_token_get_token_missing_token` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py:127]
- `test_access_token_used_as_a_refresh_token` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py:142]
- `test_access_app_token_used_as_a_refresh_token` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py:160]
- `test_refresh_token_get_token_missing_csrf_token` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py:178]
- `test_refresh_token_get_token_incorrect_csrf_token` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py:198]
- `test_refresh_token_when_expired` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py:217]
- `test_refresh_token_when_incorrect_token` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py:240]
- `test_refresh_token_when_user_deactivated_token` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py:262]
- `test_refresh_token_incorrect_token_provided` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py:283]
- `test_refresh_token_do_not_update_last_login_when_in_threshold` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py:305]
- `test_refresh_token_do_update_last_login_when_out_of_threshold` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py:341]
- `test_refresh_token_for_staff_user` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py:379]
- `test_refresh_token_when_password_login_disabled` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py:399]

**`saleor/graphql/account/tests/mutations/authentication/test_token_verify.py`**

- `test_verify_access_token` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_verify.py:27]
- `test_verify_access_token_with_permissions` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_verify.py:37]
- `test_verify_access_app_token` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_verify.py:56]
- `test_verify_token_incorrect_token` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_verify.py:66]
- `test_verify_token_invalidated_by_user` (function) — [saleor/graphql/account/tests/mutations/authentication/test_token_verify.py:78]

**`saleor/graphql/account/tests/mutations/authentication/test_tokens_deactivate_all.py`**

- `test_deactivate_all_user_tokens` (function) — [saleor/graphql/account/tests/mutations/authentication/test_tokens_deactivate_all.py:26]
- `test_deactivate_all_user_tokens_access_token` (function) — [saleor/graphql/account/tests/mutations/authentication/test_tokens_deactivate_all.py:46]
- `test_deactivate_all_user_token_refresh_token` (function) — [saleor/graphql/account/tests/mutations/authentication/test_tokens_deactivate_all.py:65]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/account/tests/mutations/authentication/__init__.py` (1 lines)
- `saleor/graphql/account/tests/mutations/authentication/test_external_authentication.py` (46 lines)
- `saleor/graphql/account/tests/mutations/authentication/test_external_logout.py` (42 lines)
- `saleor/graphql/account/tests/mutations/authentication/test_external_obtain_access_tokens.py` (167 lines)
- `saleor/graphql/account/tests/mutations/authentication/test_external_refresh.py` (158 lines)
- `saleor/graphql/account/tests/mutations/authentication/test_external_verify.py` (45 lines)
- `saleor/graphql/account/tests/mutations/authentication/test_password_change.py` (156 lines)
- `saleor/graphql/account/tests/mutations/authentication/test_request_password_reset.py` (622 lines)
- `saleor/graphql/account/tests/mutations/authentication/test_set_password.py` (296 lines)
- `saleor/graphql/account/tests/mutations/authentication/test_token_create.py` (620 lines)
- `saleor/graphql/account/tests/mutations/authentication/test_token_refresh.py` (421 lines)
- `saleor/graphql/account/tests/mutations/authentication/test_token_verify.py` (89 lines)
- `saleor/graphql/account/tests/mutations/authentication/test_tokens_deactivate_all.py` (88 lines)

## Interactions

- Imports from: `saleor/graphql/account/mutations/authentication`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `......account.error_codes.AccountErrorCode`
- `......account.events`
- `......account.notifications.get_default_user_payload`
- `......account.tests.fixtures.user.dangerously_create_test_user`
- `......core.jwt.create_access_token`
- `......core.jwt.create_refresh_token`
- `......core.jwt.jwt_decode`
- `......core.notify.NotifyEventType`
- `......core.tests.utils.get_site_context_payload`
- `......core.tokens.password_reset_token_generator`
- `......core.utils.build_absolute_uri`
- `......core.utils.url.prepare_url`
- `......plugins.base_plugin.ExternalAccessTokens`
- `......site.PasswordLoginMode`
- `.....core.utils.str_to_enum`
- `.....tests.utils.get_graphql_content`
- `.....tests.utils.get_graphql_content_from_response`
- `....mutations.authentication.utils._get_new_csrf_token`
- `....mutations.base.INVALID_TOKEN`
- `.test_token_refresh.MUTATION_TOKEN_REFRESH`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `005e728eee1b` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
