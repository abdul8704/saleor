## Purpose

`saleor/graphql/account/mutations/authentication` (`saleor/graphql/account/mutations/authentication`) groups 14 source file(s) exposing 61 top-level declaration(s).

## Public surface

**`saleor/graphql/account/mutations/authentication/create_token.py`**

- `CreateToken` (class) — [saleor/graphql/account/mutations/authentication/create_token.py:22]
- `Arguments` (class) — [saleor/graphql/account/mutations/authentication/create_token.py:25]
- `Meta` (class) — [saleor/graphql/account/mutations/authentication/create_token.py:36]
- `get_user` (function) — [saleor/graphql/account/mutations/authentication/create_token.py:52]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/authentication/create_token.py:91]

**`saleor/graphql/account/mutations/authentication/deactivate_all_user_tokens.py`**

- `DeactivateAllUserTokens` (class) — [saleor/graphql/account/mutations/authentication/deactivate_all_user_tokens.py:13]
- `Meta` (class) — [saleor/graphql/account/mutations/authentication/deactivate_all_user_tokens.py:14]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/authentication/deactivate_all_user_tokens.py:22]

**`saleor/graphql/account/mutations/authentication/external_authentication_url.py`**

- `ExternalAuthenticationUrl` (class) — [saleor/graphql/account/mutations/authentication/external_authentication_url.py:11]
- `Arguments` (class) — [saleor/graphql/account/mutations/authentication/external_authentication_url.py:18]
- `Meta` (class) — [saleor/graphql/account/mutations/authentication/external_authentication_url.py:29]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/authentication/external_authentication_url.py:36]

**`saleor/graphql/account/mutations/authentication/external_logout.py`**

- `ExternalLogout` (class) — [saleor/graphql/account/mutations/authentication/external_logout.py:11]
- `Arguments` (class) — [saleor/graphql/account/mutations/authentication/external_logout.py:16]
- `Meta` (class) — [saleor/graphql/account/mutations/authentication/external_logout.py:25]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/authentication/external_logout.py:32]

**`saleor/graphql/account/mutations/authentication/external_obtain_access_tokens.py`**

- `ExternalObtainAccessTokens` (class) — [saleor/graphql/account/mutations/authentication/external_obtain_access_tokens.py:13]
- `Arguments` (class) — [saleor/graphql/account/mutations/authentication/external_obtain_access_tokens.py:25]
- `Meta` (class) — [saleor/graphql/account/mutations/authentication/external_obtain_access_tokens.py:34]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/authentication/external_obtain_access_tokens.py:41]

**`saleor/graphql/account/mutations/authentication/external_refresh.py`**

- `ExternalRefresh` (class) — [saleor/graphql/account/mutations/authentication/external_refresh.py:13]
- `Arguments` (class) — [saleor/graphql/account/mutations/authentication/external_refresh.py:25]
- `Meta` (class) — [saleor/graphql/account/mutations/authentication/external_refresh.py:34]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/authentication/external_refresh.py:41]

**`saleor/graphql/account/mutations/authentication/external_verify.py`**

- `ExternalVerify` (class) — [saleor/graphql/account/mutations/authentication/external_verify.py:12]
- `Arguments` (class) — [saleor/graphql/account/mutations/authentication/external_verify.py:21]
- `Meta` (class) — [saleor/graphql/account/mutations/authentication/external_verify.py:30]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/authentication/external_verify.py:37]

**`saleor/graphql/account/mutations/authentication/password_change.py`**

- `PasswordChange` (class) — [saleor/graphql/account/mutations/authentication/password_change.py:21]
- `Arguments` (class) — [saleor/graphql/account/mutations/authentication/password_change.py:24]
- `Meta` (class) — [saleor/graphql/account/mutations/authentication/password_change.py:30]
- `raise_invalid_credentials` (function) — [saleor/graphql/account/mutations/authentication/password_change.py:38]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/authentication/password_change.py:49]

**`saleor/graphql/account/mutations/authentication/refresh_token.py`**

- `RefreshToken` (class) — [saleor/graphql/account/mutations/authentication/refresh_token.py:25]
- `Arguments` (class) — [saleor/graphql/account/mutations/authentication/refresh_token.py:31]
- `Meta` (class) — [saleor/graphql/account/mutations/authentication/refresh_token.py:41]
- `get_refresh_token_payload` (function) — [saleor/graphql/account/mutations/authentication/refresh_token.py:53]
- `get_refresh_token` (function) — [saleor/graphql/account/mutations/authentication/refresh_token.py:61]
- `clean_refresh_token` (function) — [saleor/graphql/account/mutations/authentication/refresh_token.py:70]
- `clean_csrf_token` (function) — [saleor/graphql/account/mutations/authentication/refresh_token.py:93]
- `get_user` (function) — [saleor/graphql/account/mutations/authentication/refresh_token.py:116]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/authentication/refresh_token.py:124]

**`saleor/graphql/account/mutations/authentication/request_password_reset.py`**

- `RequestPasswordReset` (class) — [saleor/graphql/account/mutations/authentication/request_password_reset.py:21]
- `Arguments` (class) — [saleor/graphql/account/mutations/authentication/request_password_reset.py:22]
- `Meta` (class) — [saleor/graphql/account/mutations/authentication/request_password_reset.py:42]
- `clean_user` (function) — [saleor/graphql/account/mutations/authentication/request_password_reset.py:65]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/authentication/request_password_reset.py:84]

**`saleor/graphql/account/mutations/authentication/set_password.py`**

- `SetPassword` (class) — [saleor/graphql/account/mutations/authentication/set_password.py:26]
- `Arguments` (class) — [saleor/graphql/account/mutations/authentication/set_password.py:27]
- `Meta` (class) — [saleor/graphql/account/mutations/authentication/set_password.py:34]
- `mutate` (function) — [saleor/graphql/account/mutations/authentication/set_password.py:45]

**`saleor/graphql/account/mutations/authentication/utils.py`**

- `get_user` (function) — [saleor/graphql/account/mutations/authentication/utils.py:22]
- `get_payload` (function) — [saleor/graphql/account/mutations/authentication/utils.py:37]
- `check_password_login_not_disabled` (function) — [saleor/graphql/account/mutations/authentication/utils.py:66]
- `update_user_last_login_if_required` (function) — [saleor/graphql/account/mutations/authentication/utils.py:75]

**`saleor/graphql/account/mutations/authentication/verify_token.py`**

- `VerifyToken` (class) — [saleor/graphql/account/mutations/authentication/verify_token.py:13]
- `Arguments` (class) — [saleor/graphql/account/mutations/authentication/verify_token.py:24]
- `Meta` (class) — [saleor/graphql/account/mutations/authentication/verify_token.py:27]
- `get_payload` (function) — [saleor/graphql/account/mutations/authentication/verify_token.py:34]
- `get_user` (function) — [saleor/graphql/account/mutations/authentication/verify_token.py:42]
- `perform_mutation` (function) — [saleor/graphql/account/mutations/authentication/verify_token.py:50]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/account/mutations/authentication/__init__.py` (27 lines)
- `saleor/graphql/account/mutations/authentication/set_password.py` (98 lines)
- `saleor/graphql/account/mutations/authentication/create_token.py` (123 lines)
- `saleor/graphql/account/mutations/authentication/deactivate_all_user_tokens.py` (27 lines)
- `saleor/graphql/account/mutations/authentication/external_authentication_url.py` (45 lines)
- `saleor/graphql/account/mutations/authentication/external_logout.py` (37 lines)
- `saleor/graphql/account/mutations/authentication/external_obtain_access_tokens.py` (61 lines)
- `saleor/graphql/account/mutations/authentication/external_refresh.py` (59 lines)
- `saleor/graphql/account/mutations/authentication/external_verify.py` (43 lines)
- `saleor/graphql/account/mutations/authentication/password_change.py` (76 lines)
- `saleor/graphql/account/mutations/authentication/refresh_token.py` (145 lines)
- `saleor/graphql/account/mutations/authentication/request_password_reset.py` (111 lines)
- `saleor/graphql/account/mutations/authentication/utils.py` (83 lines)
- `saleor/graphql/account/mutations/authentication/verify_token.py` (55 lines)

## Interactions

- Imports from: `saleor/core`
- Imported by: `saleor/graphql/account/tests/mutations/authentication`

Internal dependencies named in the source:

- `.....account.error_codes.AccountErrorCode`
- `.....account.events`
- `.....account.models`
- `.....account.models.User`
- `.....account.tasks.trigger_send_password_reset_notification`
- `.....account.throttling.authenticate_with_throttling`
- `.....account.utils.RequestorAwareContext`
- `.....account.utils.retrieve_user_by_email`
- `.....core.db.connection.allow_writer`
- `.....core.jwt.PERMISSIONS_FIELD`
- `.....core.jwt.create_access_token`
- `.....core.jwt.create_refresh_token`
- `.....core.jwt.get_user_from_payload`
- `.....core.jwt.jwt_decode`
- `.....core.utils.url.validate_storefront_url`
- `.....order.utils.match_orders_with_new_user`
- `.....permission.auth_filters.AuthorizationFilters`
- `.....permission.enums.get_permissions_from_names`
- `.....site.PasswordLoginMode`
- `.....site.models.SiteSettings`
- `.....webhook.event_types.WebhookEventAsyncType`
- `....channel.utils.clean_channel`
- `....core.ResolveInfo`
- `....core.context.disallow_replica_in_context`
- `....core.doc_category.DOC_CATEGORY_AUTH`
- `....core.doc_category.DOC_CATEGORY_USERS`
- `....core.fields.JSONString`
- `....core.mutations.BaseMutation`
- `....core.mutations.validation_error_to_error_type`
- `....core.types.AccountError`
- `....core.utils.WebhookEventInfo`
- `....plugins.dataloaders.get_plugin_manager_promise`
- `....site.dataloaders.get_site_promise`
- `...types.User`
- `..CreateToken`
- `..base.INVALID_TOKEN`
- `.create_token.CreateToken`
- `.deactivate_all_user_tokens.DeactivateAllUserTokens`
- `.external_authentication_url.ExternalAuthenticationUrl`
- `.external_logout.ExternalLogout`
- `.external_obtain_access_tokens.ExternalObtainAccessTokens`
- `.external_refresh.ExternalRefresh`
- `.external_verify.ExternalVerify`
- `.password_change.PasswordChange`
- `.refresh_token.RefreshToken`
- `.request_password_reset.RequestPasswordReset`
- `.set_password.SetPassword`
- `.utils.check_password_login_not_disabled`
- `.utils.get_payload`
- `.utils.get_user`
- `.utils.update_user_last_login_if_required`
- `.verify_token.VerifyToken`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `6157c0358b67` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
