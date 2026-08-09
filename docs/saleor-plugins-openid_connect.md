## Purpose

`saleor/plugins/openid_connect` (`saleor/plugins/openid_connect`) groups 20 source file(s) exposing 160 top-level declaration(s).

## Public surface

**`saleor/plugins/openid_connect/client.py`**

- `OAuth2Client` (class) — [saleor/plugins/openid_connect/client.py:7]

**`saleor/plugins/openid_connect/dataclasses.py`**

- `OpenIDConnectConfig` (class) — [saleor/plugins/openid_connect/dataclasses.py:5]

**`saleor/plugins/openid_connect/exceptions.py`**

- `AuthenticationError` (class) — [saleor/plugins/openid_connect/exceptions.py:1]

**`saleor/plugins/openid_connect/plugin.py`**

- `OpenIDConnectPlugin` (class) — [saleor/plugins/openid_connect/plugin.py:52]
- `validate_plugin_configuration` (function) — [saleor/plugins/openid_connect/plugin.py:206]
- `external_obtain_access_tokens` (function) — [saleor/plugins/openid_connect/plugin.py:284]
- `is_staff_user_email` (function) — [saleor/plugins/openid_connect/plugin.py:377]
- `external_authentication_url` (function) — [saleor/plugins/openid_connect/plugin.py:383]
- `external_refresh` (function) — [saleor/plugins/openid_connect/plugin.py:418]
- `get_and_update_user_permissions` (function) — [saleor/plugins/openid_connect/plugin.py:480]
- `external_logout` (function) — [saleor/plugins/openid_connect/plugin.py:493]
- `external_verify` (function) — [saleor/plugins/openid_connect/plugin.py:508]
- `authenticate_user` (function) — [saleor/plugins/openid_connect/plugin.py:540]

**`saleor/plugins/openid_connect/tests/conftest.py`**

- `plugin_configuration` (function) — [saleor/plugins/openid_connect/tests/conftest.py:9]
- `fun` (function) — [saleor/plugins/openid_connect/tests/conftest.py:10]
- `openid_plugin` (function) — [saleor/plugins/openid_connect/tests/conftest.py:49]
- `fun` (function) — [saleor/plugins/openid_connect/tests/conftest.py:50]
- `decoded_access_token` (function) — [saleor/plugins/openid_connect/tests/conftest.py:96]
- `user_info_response` (function) — [saleor/plugins/openid_connect/tests/conftest.py:112]
- `id_payload` (function) — [saleor/plugins/openid_connect/tests/conftest.py:128]
- `id_token` (function) — [saleor/plugins/openid_connect/tests/conftest.py:148]

**`saleor/plugins/openid_connect/tests/test_ip_filtering.py`**

- `test_rejects_private_ips` (function) — [saleor/plugins/openid_connect/tests/test_ip_filtering.py:8]

**`saleor/plugins/openid_connect/tests/test_plugin.py`**

- `test_get_oauth_session_adds_refresh_scope_when_enabled` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:34]
- `test_get_oauth_session_dont_add_refresh_scope_when_disabled` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:40]
- `test_get_oauth_session_dont_add_refresh_scope_when_enabled_and_configured_with_aws_cognito` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:46]
- `test_get_oauth_session_dont_add_refresh_scope_when_enabled_and_configured_with_google` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:57]
- `test_google_auth_url_includes_access_type_offline` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:71]
- `test_google_auth_url_without_refresh_token_does_not_include_access_type` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:90]
- `test_non_google_auth_url_does_not_include_access_type` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:111]
- `test_external_authentication_url_returns_redirect_url` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:127]
- `test_external_authentication_plugin_disabled` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:150]
- `test_external_authentication_raises_error_when_missing_redirect` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:158]
- `test_external_authentication_raises_error_when_redirect_is_wrong` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:166]
- `test_external_refresh_from_cookie` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:176]
- `test_external_refresh_from_input` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:229]
- `test_external_refresh_with_scope_permissions` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:280]
- `test_external_refresh_raises_error_when_token_is_invalid` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:352]
- `test_external_refresh_disabled_refreshing` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:391]
- `test_external_refresh_when_plugin_is_disabled` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:402]
- `test_external_refresh_raises_error` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:412]
- `test_external_refresh_incorrect_csrf` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:431]
- `test_external_obtain_access_tokens` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:451]
- `test_external_obtain_access_tokens_with_permissions` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:522]
- `test_external_obtain_access_tokens_with_saleor_staff` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:602]
- `test_external_obtain_access_tokens_with_staff_user_domain_but_no_scope` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:681]
- `test_external_obtain_access_tokens_user_which_is_no_more_staff` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:766]
- `test_external_obtain_access_tokens_user_created` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:839]
- `test_external_obtain_access_tokens_plugin_disabled` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:914]
- `test_external_obtain_access_tokens_missing_code` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:927]
- `test_external_obtain_access_tokens_missing_state` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:938]
- `test_external_obtain_access_tokens_missing_redirect_uri_in_state` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:948]
- `test_external_obtain_access_tokens_fetch_token_raises_error` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:958]
- `test_external_obtain_access_tokens_get_parsed_id_token_raises_error` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:988]
- `test_external_obtain_access_tokens_get_or_create_user_from_payload_raises_error` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:1033]
- `test_validate_plugin_configuration_raises_error` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:1104]
- `test_validate_plugin_configuration` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:1129]
- `test_external_logout_missing_logout_url` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:1143]
- `test_external_logout_plugin_inactive` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:1149]
- `test_external_logout` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:1155]
- `test_external_verify_plugin_disabled` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:1173]
- `test_external_verify_missing_token` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:1181]
- `test_external_verify_wrong_token_owner` (function) — [saleor/plugins/openid_connect/tests/test_plugin.py:1189]
- _…and 25 more in this file_

**`saleor/plugins/openid_connect/tests/test_utils.py`**

- `test_fetch_jwks_raises_error` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:63]
- `test_fetch_jwks` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:75]
- `test_is_jwt_shaped` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:99]
- `test_decode_access_token_opaque_token_skips_decode_and_logging` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:107]
- `test_decode_access_token_invalid_signature_returns_none_and_logs` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:126]
- `test_decode_access_token_valid_jwt_returns_payload` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:147]
- `test_get_or_create_user_from_token_missing_email` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:161]
- `test_get_or_create_user_from_token_user_not_active` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:167]
- `test_get_user_from_token_missing_email` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:174]
- `test_get_user_from_token_missing_user` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:180]
- `test_get_user_from_token_user_not_active` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:186]
- `test_create_tokens_from_oauth_payload` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:194]
- `test_validate_refresh_token_missing_csrf_token` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:244]
- `test_validate_refresh_token_missing_csrf_token_in_token_payload` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:250]
- `test_validate_refresh_token_missing_token` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:264]
- `test_get_saleor_permissions_from_scope` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:270]
- `test_get_user_info_raises_decode_error` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:285]
- `test_get_user_info_raises_http_error` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:294]
- `test_get_or_create_user_from_payload_retrieve_user_by_sub` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:305]
- `test_get_or_create_user_from_payload_updates_sub` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:333]
- `test_get_or_create_user_from_payload_assigns_sub` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:362]
- `test_get_or_create_user_from_payload_clears_password_for_existing_user` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:391]
- `test_get_or_create_user_from_payload_keeps_password_for_returning_oidc_user` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:420]
- `test_get_or_create_user_from_payload_creates_user_with_sub` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:450]
- `test_get_or_create_user_from_payload_does_not_match_orders_for_existing_user` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:481]
- `test_get_or_create_user_from_payload_match_orders_for_new_user` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:549]
- `test_get_or_create_user_from_payload_match_orders_when_changing_email` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:581]
- `test_get_or_create_user_from_payload_multiple_subs` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:615]
- `test_get_or_create_user_from_payload_different_email` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:640]
- `test_get_or_create_user_from_payload_with_last_login` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:674]
- `test_get_or_create_user_from_payload_update_last_login` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:714]
- `test_get_or_create_user_from_payload_set_is_confirmed` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:745]
- `test_get_or_create_user_from_payload_last_login_stays_same` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:775]
- `test_get_or_create_user_from_payload_last_login_modifies` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:800]
- `test_jwt_token_without_expiration_claim` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:830]
- `test_jwt_token_without_expiration_claim_mixed_permissions_from_group` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:871]
- `test_jwt_token_without_expiration_claim_email_not_match_staff_user_domains` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:923]
- `test_jwt_token_without_expiration_claim_default_channel_group` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:966]
- `test_jwt_token_without_expiration_claim_with_existing_default_channel_group` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:1013]
- `test_jwt_token_without_expiration_claim_empty_default_channel_group` (function) — [saleor/plugins/openid_connect/tests/test_utils.py:1067]
- _…and 8 more in this file_

**`saleor/plugins/openid_connect/utils.py`**

- `fetch_jwks` (function) — [saleor/plugins/openid_connect/utils.py:63]
- `get_jwks_keys_from_cache_or_fetch` (function) — [saleor/plugins/openid_connect/utils.py:96]
- `get_user_info_from_cache_or_fetch` (function) — [saleor/plugins/openid_connect/utils.py:103]
- `get_user_info` (function) — [saleor/plugins/openid_connect/utils.py:125]
- `is_jwt_shaped` (function) — [saleor/plugins/openid_connect/utils.py:155]
- `decode_access_token` (function) — [saleor/plugins/openid_connect/utils.py:172]
- `get_user_from_oauth_access_token_in_jwt_format` (function) — [saleor/plugins/openid_connect/utils.py:191]
- `get_user_from_oauth_access_token` (function) — [saleor/plugins/openid_connect/utils.py:282]
- `assign_staff_to_default_group_and_update_permissions` (function) — [saleor/plugins/openid_connect/utils.py:334]
- `create_jwt_token` (function) — [saleor/plugins/openid_connect/utils.py:354]
- `create_jwt_refresh_token` (function) — [saleor/plugins/openid_connect/utils.py:378]
- `get_decoded_token` (function) — [saleor/plugins/openid_connect/utils.py:394]
- `get_parsed_id_token` (function) — [saleor/plugins/openid_connect/utils.py:400]
- `get_or_create_user_from_payload` (function) — [saleor/plugins/openid_connect/utils.py:431]
- `get_domain_from_email` (function) — [saleor/plugins/openid_connect/utils.py:503]
- `get_staff_user_domains` (function) — [saleor/plugins/openid_connect/utils.py:571]
- `get_user_from_token` (function) — [saleor/plugins/openid_connect/utils.py:583]
- `is_owner_of_token_valid` (function) — [saleor/plugins/openid_connect/utils.py:595]
- `create_tokens_from_oauth_payload` (function) — [saleor/plugins/openid_connect/utils.py:603]
- `validate_refresh_token` (function) — [saleor/plugins/openid_connect/utils.py:625]
- `get_incorrect_or_missing_urls` (function) — [saleor/plugins/openid_connect/utils.py:679]
- `get_incorrect_fields` (function) — [saleor/plugins/openid_connect/utils.py:690]
- `get_saleor_permissions_qs_from_scope` (function) — [saleor/plugins/openid_connect/utils.py:733]
- `get_saleor_permissions_from_list` (function) — [saleor/plugins/openid_connect/utils.py:738]
- `get_saleor_permission_names` (function) — [saleor/plugins/openid_connect/utils.py:752]

## How it works

The module's files, as provided to this run:

- `saleor/plugins/openid_connect/dataclasses.py` (17 lines)
- `saleor/plugins/openid_connect/client.py` (12 lines)
- `saleor/plugins/openid_connect/__init__.py` (1 lines)
- `saleor/plugins/openid_connect/const.py` (1 lines)
- `saleor/plugins/openid_connect/exceptions.py` (2 lines)
- `saleor/plugins/openid_connect/plugin.py` (577 lines)
- `saleor/plugins/openid_connect/tests/__init__.py` (1 lines)
- `saleor/plugins/openid_connect/tests/cassettes/test_plugin/test_external_obtain_access_tokens_user_which_is_not_more_staff.yaml` (114 lines)
- `saleor/plugins/openid_connect/tests/cassettes/test_plugin/test_external_obtain_access_tokens_with_saleor_staff.yaml` (114 lines)
- `saleor/plugins/openid_connect/tests/cassettes/test_plugin/test_external_obtain_access_tokens.yaml` (238 lines)
- `saleor/plugins/openid_connect/tests/cassettes/test_plugin/test_external_refresh_from_cookie.yaml` (119 lines)
- `saleor/plugins/openid_connect/tests/cassettes/test_plugin/test_external_refresh_from_input.yaml` (119 lines)
- `saleor/plugins/openid_connect/tests/cassettes/test_plugin/test_external_refresh_raises_error_when_token_is_invalid.yaml` (121 lines)
- `saleor/plugins/openid_connect/tests/cassettes/test_plugin/test_external_refresh_raises_error.yaml` (84 lines)
- `saleor/plugins/openid_connect/tests/cassettes/test_utils/test_fetch_jwks.yaml` (119 lines)
- `saleor/plugins/openid_connect/tests/conftest.py` (180 lines)
- `saleor/plugins/openid_connect/tests/test_ip_filtering.py` (20 lines)
- `saleor/plugins/openid_connect/tests/test_plugin.py` (2146 lines)
- `saleor/plugins/openid_connect/tests/test_utils.py` (1349 lines)
- `saleor/plugins/openid_connect/utils.py` (754 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/core/utils`, `saleor/graphql/core/types`
- Imported by: `saleor/order`, `saleor/plugins/sendgrid`, `saleor/checkout`, `saleor/core`, `saleor/plugins/avatax`, `saleor/discount`, `saleor/discount/utils`, `saleor/graphql/core/utils`, `saleor/graphql/product/types`, `saleor/order/tests`, `saleor/payment`, `saleor/plugins/admin_email`, `saleor/plugins`, `saleor/plugins/user_email`, `saleor/product/utils`, `saleor/warehouse`, `saleor/webhook/transport/asynchronous`, `saleor/account`, `saleor/core/cleaners`, `saleor/core/db`, `saleor/core/telemetry`, `saleor/core/utils`, `saleor/csv/utils`, `saleor/discount/migrations`, `saleor/giftcard`, `saleor/graphql/app/dataloaders`, `saleor/graphql/attribute/mutations`, `saleor/graphql/attribute/utils`, `saleor/graphql/checkout/mutations`, `saleor/graphql/core`, `saleor/graphql/menu/mutations`, `saleor/graphql/meta`, `saleor/graphql/order/bulk_mutations`, `saleor/graphql/order`, `saleor/graphql/product`, `saleor/graphql/tests`, `saleor/graphql/webhook/mutations`, `saleor/product`, `saleor/product/migrations`, `saleor/shipping`, `saleor/tests/e2e`, `saleor/webhook/observability`, `saleor/webhook`, `saleor/webhook/tests`, `saleor/webhook/transport`

Internal dependencies named in the source:

- `....account.models.Group`
- `....account.models.User`
- `....account.search.update_user_search_vector`
- `....core.http_client.HTTPClient`
- `....core.jwt_manager.get_jwt_manager`
- `....graphql.account.mutations.authentication.utils._get_new_csrf_token`
- `....permission.models.Permission`
- `...account.models.Group`
- `...account.models.User`
- `...account.search.update_user_search_vector`
- `...account.utils.get_user_groups_permissions`
- `...account.utils.send_user_event`
- `...base_plugin.ExternalAccessTokens`
- `...core.auth.get_token_from_request`
- `...core.http_client.HTTPClient`
- `...core.http_client.HTTPConfig`
- `...graphql.core.SaleorContext`
- `...manager.get_plugins_manager`
- `...models.PluginConfiguration`
- `...order.utils.match_orders_with_new_user`
- `...permission.enums.get_permission_names`
- `...permission.enums.get_permissions_codename`
- `...permission.enums.get_permissions_from_codenames`
- `...permission.enums.get_permissions_from_names`
- `...permission.models.Permission`
- `...site.models.Site`
- `..PLUGIN_ID`
- `..base_plugin.BasePlugin`
- `..base_plugin.ConfigurationTypeField`
- `..base_plugin.ExternalAccessTokens`
- `..error_codes.PluginErrorCode`
- `..exceptions.AuthenticationError`
- `..models.PluginConfiguration`
- `..plugin.OpenIDConnectPlugin`
- `.client.OAuth2Client`
- `.const.SALEOR_STAFF_PERMISSION`
- `.dataclasses.OpenIDConnectConfig`
- `.exceptions.AuthenticationError`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `7d38869976af` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
