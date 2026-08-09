## Purpose

`saleor/app` (`saleor/app`) groups 16 source file(s) exposing 60 top-level declaration(s).

## Public surface

**`saleor/app/actions.py`**

- `delete_app` (function) — [saleor/app/actions.py:19]

**`saleor/app/apps.py`**

- `AppConfig` (class) — [saleor/app/apps.py:5]
- `ready` (function) — [saleor/app/apps.py:8]

**`saleor/app/error_codes.py`**

- `AppErrorCode` (class) — [saleor/app/error_codes.py:4]
- `AppProblemCreateErrorCode` (class) — [saleor/app/error_codes.py:24]
- `AppProblemDismissErrorCode` (class) — [saleor/app/error_codes.py:31]

**`saleor/app/headers.py`**

- `AppHeaders` (class) — [saleor/app/headers.py:1]
- `DeprecatedAppHeaders` (class) — [saleor/app/headers.py:9]

**`saleor/app/installation_utils.py`**

- `AppInstallationError` (class) — [saleor/app/installation_utils.py:39]
- `validate_app_install_response` (function) — [saleor/app/installation_utils.py:43]
- `send_app_token` (function) — [saleor/app/installation_utils.py:56]
- `fetch_icon_image` (function) — [saleor/app/installation_utils.py:77]
- `fetch_brand_data` (function) — [saleor/app/installation_utils.py:117]
- `fetch_brand_data_task` (function) — [saleor/app/installation_utils.py:152]
- `fetch_brand_data_async` (function) — [saleor/app/installation_utils.py:192]
- `fetch_manifest` (function) — [saleor/app/installation_utils.py:206]
- `install_app` (function) — [saleor/app/installation_utils.py:239]

**`saleor/app/lock_objects.py`**

- `app_qs_select_for_update` (function) — [saleor/app/lock_objects.py:6]
- `app_problem_qs_select_for_update` (function) — [saleor/app/lock_objects.py:10]

**`saleor/app/manifest_schema.py`**

- `ManifestBrandLogoSchema` (class) — [saleor/app/manifest_schema.py:24]
- `validate_logo_url` (function) — [saleor/app/manifest_schema.py:31]
- `ManifestBrandSchema` (class) — [saleor/app/manifest_schema.py:50]
- `ManifestExtensionSchema` (class) — [saleor/app/manifest_schema.py:56]
- `ManifestWebhookSchema` (class) — [saleor/app/manifest_schema.py:68]
- `validate_target_url` (function) — [saleor/app/manifest_schema.py:82]
- `ManifestSchema` (class) — [saleor/app/manifest_schema.py:95]
- `validate_token_target_url` (function) — [saleor/app/manifest_schema.py:117]
- `validate_author` (function) — [saleor/app/manifest_schema.py:133]

**`saleor/app/manifest_validations.py`**

- `RequiredSaleorVersionSpec` (class) — [saleor/app/manifest_validations.py:41]
- `Parser` (class) — [saleor/app/manifest_validations.py:42]
- `range` (function) — [saleor/app/manifest_validations.py:44]
- `clean_manifest_url` (function) — [saleor/app/manifest_validations.py:79]
- `clean_manifest_data` (function) — [saleor/app/manifest_validations.py:118]

**`saleor/app/models.py`**

- `AppQueryset` (class) — [saleor/app/models.py:21]
- `for_event_type` (function) — [saleor/app/models.py:22]
- `not_removed` (function) — [saleor/app/models.py:38]
- `marked_to_be_removed` (function) — [saleor/app/models.py:41]
- `App` (class) — [saleor/app/models.py:48]
- `Meta` (class) — [saleor/app/models.py:82]
- `get_permissions` (function) — [saleor/app/models.py:98]
- `has_perms` (function) — [saleor/app/models.py:109]
- `has_perm` (function) — [saleor/app/models.py:122]
- `AppTokenManager` (class) — [saleor/app/models.py:131]
- `create` (function) — [saleor/app/models.py:132]
- `AppToken` (class) — [saleor/app/models.py:142]
- `set_auth_token` (function) — [saleor/app/models.py:150]
- `AppExtension` (class) — [saleor/app/models.py:155]
- `Meta` (class) — [saleor/app/models.py:177]
- `AppProblem` (class) — [saleor/app/models.py:190]
- `Meta` (class) — [saleor/app/models.py:213]
- `is_dismissed_by_user` (function) — [saleor/app/models.py:216]
- `AppInstallation` (class) — [saleor/app/models.py:229]
- `set_message` (function) — [saleor/app/models.py:244]

**`saleor/app/signals.py`**

- `delete_brand_images` (function) — [saleor/app/signals.py:4]

**`saleor/app/tasks.py`**

- `install_app_task` (function) — [saleor/app/tasks.py:23]
- `remove_apps_task` (function) — [saleor/app/tasks.py:91]

**`saleor/app/types.py`**

- `AppType` (class) — [saleor/app/types.py:1]
- `DeprecatedAppExtensionHttpMethod` (class) — [saleor/app/types.py:9]

**`saleor/app/utils.py`**

- `get_active_tax_apps` (function) — [saleor/app/utils.py:5]

**`saleor/app/validators.py`**

- `AppURLValidator` (class) — [saleor/app/validators.py:8]

## How it works

The module's files, as provided to this run:

- `saleor/app/headers.py` (12 lines)
- `saleor/app/models.py` (251 lines)
- `saleor/app/__init__.py` (1 lines)
- `saleor/app/actions.py` (75 lines)
- `saleor/app/app_manifest_sample.json` (37 lines)
- `saleor/app/apps.py` (22 lines)
- `saleor/app/error_codes.py` (36 lines)
- `saleor/app/installation_utils.py` (339 lines)
- `saleor/app/lock_objects.py` (11 lines)
- `saleor/app/manifest_schema.py` (142 lines)
- `saleor/app/manifest_validations.py` (378 lines)
- `saleor/app/signals.py` (6 lines)
- `saleor/app/tasks.py` (123 lines)
- `saleor/app/types.py` (25 lines)
- `saleor/app/utils.py` (18 lines)
- `saleor/app/validators.py` (25 lines)

## Interactions

- Imports from: `saleor/core`, `saleor`, `saleor/graphql/product/types`, `saleor/webhook`, `saleor/core/utils`, `saleor/graphql/core/types`
- Imported by: `saleor/app/tests`, `saleor/asgi`

Internal dependencies named in the source:

- `...__version__`
- `...celeryconf`
- `...schema_version`
- `..app.headers.AppHeaders`
- `..app.headers.DeprecatedAppHeaders`
- `..celeryconf.app`
- `..core.JobStatus`
- `..core.db.connection.allow_writer`
- `..core.http_client.HTTPClient`
- `..core.models.EventDelivery`
- `..core.models.EventDeliveryAttempt`
- `..core.models.EventPayload`
- `..core.models.Job`
- `..core.models.ModelWithMetadata`
- `..core.tasks.delete_files_from_private_storage_task`
- `..core.tasks.delete_from_storage_task`
- `..core.telemetry.get_task_context`
- `..core.utils.build_absolute_uri`
- `..core.utils.events.call_event`
- `..core.utils.get_domain`
- `..giftcard.const.GIFT_CARD_PAYMENT_GATEWAY_ID`
- `..graphql.core.utils.str_to_enum`
- `..graphql.error.pydantic_to_validation_error`
- `..graphql.webhook.subscription_query.SubscriptionQuery`
- `..permission.enums.AppPermission`
- `..permission.enums.BasePermissionEnum`
- `..permission.enums.get_permission_names`
- `..permission.models.Permission`
- `..plugins.manager.PluginsManager`
- `..thumbnail.ICON_MIME_TYPES`
- `..thumbnail.utils.get_filename_from_url`
- `..thumbnail.validators.validate_icon_image`
- `..webhook.event_types.WebhookEventAsyncType`
- `..webhook.event_types.WebhookEventSyncType`
- `..webhook.models.Webhook`
- `..webhook.models.WebhookEvent`
- `..webhook.response_schemas.utils.annotations.DefaultIfNone`
- `..webhook.utils.get_webhooks_for_app_lifecycle_event`
- `..webhook.utils.get_webhooks_for_event`
- `..webhook.validators.custom_headers_validator`
- `.error_codes.AppErrorCode`
- `.installation_utils.AppInstallationError`
- `.installation_utils.install_app`
- `.manifest_validations.clean_manifest_data`
- `.models.App`
- `.models.AppExtension`
- `.models.AppInstallation`
- `.models.AppProblem`
- `.models.AppToken`
- `.signals.delete_brand_images`
- `.types.AppType`
- `.types.DEFAULT_APP_TARGET`
- `.validators.AppURLValidator`
- `.validators.image_url_validator`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `10c91d8c6ba2` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
