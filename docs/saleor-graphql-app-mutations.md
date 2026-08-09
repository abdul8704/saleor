## Purpose

`saleor/graphql/app/mutations` (`saleor/graphql/app/mutations`) groups 16 source file(s) exposing 96 top-level declaration(s).

## Public surface

**`saleor/graphql/app/mutations/app_activate.py`**

- `AppActivate` (class) — [saleor/graphql/app/mutations/app_activate.py:13]
- `Arguments` (class) — [saleor/graphql/app/mutations/app_activate.py:14]
- `Meta` (class) — [saleor/graphql/app/mutations/app_activate.py:17]
- `perform_mutation` (function) — [saleor/graphql/app/mutations/app_activate.py:32]

**`saleor/graphql/app/mutations/app_create.py`**

- `AppInput` (class) — [saleor/graphql/app/mutations/app_create.py:18]
- `Meta` (class) — [saleor/graphql/app/mutations/app_create.py:31]
- `AppCreate` (class) — [saleor/graphql/app/mutations/app_create.py:35]
- `Arguments` (class) — [saleor/graphql/app/mutations/app_create.py:40]
- `Meta` (class) — [saleor/graphql/app/mutations/app_create.py:46]
- `clean_input` (function) — [saleor/graphql/app/mutations/app_create.py:65]
- `perform_mutation` (function) — [saleor/graphql/app/mutations/app_create.py:78]
- `save` (function) — [saleor/graphql/app/mutations/app_create.py:93]

**`saleor/graphql/app/mutations/app_deactivate.py`**

- `AppDeactivate` (class) — [saleor/graphql/app/mutations/app_deactivate.py:13]
- `Arguments` (class) — [saleor/graphql/app/mutations/app_deactivate.py:14]
- `Meta` (class) — [saleor/graphql/app/mutations/app_deactivate.py:17]
- `perform_mutation` (function) — [saleor/graphql/app/mutations/app_deactivate.py:32]

**`saleor/graphql/app/mutations/app_delete_failed_installation.py`**

- `AppDeleteFailedInstallation` (class) — [saleor/graphql/app/mutations/app_delete_failed_installation.py:14]
- `Arguments` (class) — [saleor/graphql/app/mutations/app_delete_failed_installation.py:15]
- `Meta` (class) — [saleor/graphql/app/mutations/app_delete_failed_installation.py:20]
- `clean_instance` (function) — [saleor/graphql/app/mutations/app_delete_failed_installation.py:29]

**`saleor/graphql/app/mutations/app_delete.py`**

- `AppDelete` (class) — [saleor/graphql/app/mutations/app_delete.py:19]
- `Arguments` (class) — [saleor/graphql/app/mutations/app_delete.py:20]
- `Meta` (class) — [saleor/graphql/app/mutations/app_delete.py:23]
- `get_instance` (function) — [saleor/graphql/app/mutations/app_delete.py:38]
- `clean_instance` (function) — [saleor/graphql/app/mutations/app_delete.py:44]
- `perform_mutation` (function) — [saleor/graphql/app/mutations/app_delete.py:54]

**`saleor/graphql/app/mutations/app_fetch_manifest.py`**

- `AppFetchManifest` (class) — [saleor/graphql/app/mutations/app_fetch_manifest.py:18]
- `Arguments` (class) — [saleor/graphql/app/mutations/app_fetch_manifest.py:21]
- `Meta` (class) — [saleor/graphql/app/mutations/app_fetch_manifest.py:26]
- `success_response` (function) — [saleor/graphql/app/mutations/app_fetch_manifest.py:34]
- `fetch_manifest` (function) — [saleor/graphql/app/mutations/app_fetch_manifest.py:39]
- `construct_instance` (function) — [saleor/graphql/app/mutations/app_fetch_manifest.py:68]
- `clean_manifest_data` (function) — [saleor/graphql/app/mutations/app_fetch_manifest.py:91]
- `perform_mutation` (function) — [saleor/graphql/app/mutations/app_fetch_manifest.py:115]

**`saleor/graphql/app/mutations/app_install.py`**

- `AppInstallInput` (class) — [saleor/graphql/app/mutations/app_install.py:19]
- `Meta` (class) — [saleor/graphql/app/mutations/app_install.py:34]
- `AppInstall` (class) — [saleor/graphql/app/mutations/app_install.py:44]
- `Arguments` (class) — [saleor/graphql/app/mutations/app_install.py:45]
- `Meta` (class) — [saleor/graphql/app/mutations/app_install.py:51]
- `clean_input` (function) — [saleor/graphql/app/mutations/app_install.py:64]
- `perform_mutation` (function) — [saleor/graphql/app/mutations/app_install.py:80]
- `post_save_action` (function) — [saleor/graphql/app/mutations/app_install.py:84]

**`saleor/graphql/app/mutations/app_problem_create.py`**

- `AppProblemCreateError` (class) — [saleor/graphql/app/mutations/app_problem_create.py:28]
- `AppProblemCreateValidatedInput` (class) — [saleor/graphql/app/mutations/app_problem_create.py:32]
- `truncate_message` (function) — [saleor/graphql/app/mutations/app_problem_create.py:44]
- `default_aggregation_period` (function) — [saleor/graphql/app/mutations/app_problem_create.py:52]
- `AppProblemCreateInput` (class) — [saleor/graphql/app/mutations/app_problem_create.py:59]
- `AppProblemCreate` (class) — [saleor/graphql/app/mutations/app_problem_create.py:93]
- `Arguments` (class) — [saleor/graphql/app/mutations/app_problem_create.py:98]
- `Meta` (class) — [saleor/graphql/app/mutations/app_problem_create.py:103]
- `perform_mutation` (function) — [saleor/graphql/app/mutations/app_problem_create.py:110]

**`saleor/graphql/app/mutations/app_problem_dismiss.py`**

- `AppProblemDismissError` (class) — [saleor/graphql/app/mutations/app_problem_dismiss.py:30]
- `AppProblemDismissByAppInput` (class) — [saleor/graphql/app/mutations/app_problem_dismiss.py:34]
- `Meta` (class) — [saleor/graphql/app/mutations/app_problem_dismiss.py:48]
- `AppProblemDismissByStaffWithIdsInput` (class) — [saleor/graphql/app/mutations/app_problem_dismiss.py:52]
- `Meta` (class) — [saleor/graphql/app/mutations/app_problem_dismiss.py:61]
- `AppProblemDismissByStaffWithKeysInput` (class) — [saleor/graphql/app/mutations/app_problem_dismiss.py:65]
- `Meta` (class) — [saleor/graphql/app/mutations/app_problem_dismiss.py:78]
- `AppProblemDismissInput` (class) — [saleor/graphql/app/mutations/app_problem_dismiss.py:82]
- `Meta` (class) — [saleor/graphql/app/mutations/app_problem_dismiss.py:98]
- `AppProblemDismiss` (class) — [saleor/graphql/app/mutations/app_problem_dismiss.py:102]
- `Arguments` (class) — [saleor/graphql/app/mutations/app_problem_dismiss.py:103]
- `Meta` (class) — [saleor/graphql/app/mutations/app_problem_dismiss.py:109]
- `perform_mutation` (function) — [saleor/graphql/app/mutations/app_problem_dismiss.py:119]

**`saleor/graphql/app/mutations/app_reenable_sync_webhooks.py`**

- `AppReenableSyncWebhooks` (class) — [saleor/graphql/app/mutations/app_reenable_sync_webhooks.py:27]
- `Arguments` (class) — [saleor/graphql/app/mutations/app_reenable_sync_webhooks.py:33]
- `Meta` (class) — [saleor/graphql/app/mutations/app_reenable_sync_webhooks.py:38]
- `perform_mutation` (function) — [saleor/graphql/app/mutations/app_reenable_sync_webhooks.py:50]

**`saleor/graphql/app/mutations/app_retry_install.py`**

- `AppRetryInstall` (class) — [saleor/graphql/app/mutations/app_retry_install.py:17]
- `Arguments` (class) — [saleor/graphql/app/mutations/app_retry_install.py:18]
- `Meta` (class) — [saleor/graphql/app/mutations/app_retry_install.py:26]
- `save` (function) — [saleor/graphql/app/mutations/app_retry_install.py:41]
- `clean_instance` (function) — [saleor/graphql/app/mutations/app_retry_install.py:48]
- `perform_mutation` (function) — [saleor/graphql/app/mutations/app_retry_install.py:55]

**`saleor/graphql/app/mutations/app_token_create.py`**

- `AppTokenInput` (class) — [saleor/graphql/app/mutations/app_token_create.py:18]
- `Meta` (class) — [saleor/graphql/app/mutations/app_token_create.py:22]
- `AppTokenCreate` (class) — [saleor/graphql/app/mutations/app_token_create.py:26]
- `Arguments` (class) — [saleor/graphql/app/mutations/app_token_create.py:31]
- `Meta` (class) — [saleor/graphql/app/mutations/app_token_create.py:36]
- `perform_mutation` (function) — [saleor/graphql/app/mutations/app_token_create.py:45]
- `clean_input` (function) — [saleor/graphql/app/mutations/app_token_create.py:60]

**`saleor/graphql/app/mutations/app_token_delete.py`**

- `AppTokenDelete` (class) — [saleor/graphql/app/mutations/app_token_delete.py:18]
- `Arguments` (class) — [saleor/graphql/app/mutations/app_token_delete.py:19]
- `Meta` (class) — [saleor/graphql/app/mutations/app_token_delete.py:22]
- `get_instance` (function) — [saleor/graphql/app/mutations/app_token_delete.py:31]
- `clean_instance` (function) — [saleor/graphql/app/mutations/app_token_delete.py:40]

**`saleor/graphql/app/mutations/app_token_verify.py`**

- `AppTokenVerify` (class) — [saleor/graphql/app/mutations/app_token_verify.py:11]
- `Arguments` (class) — [saleor/graphql/app/mutations/app_token_verify.py:18]
- `Meta` (class) — [saleor/graphql/app/mutations/app_token_verify.py:21]
- `perform_mutation` (function) — [saleor/graphql/app/mutations/app_token_verify.py:28]

**`saleor/graphql/app/mutations/app_update.py`**

- `AppUpdate` (class) — [saleor/graphql/app/mutations/app_update.py:20]
- `Arguments` (class) — [saleor/graphql/app/mutations/app_update.py:21]
- `Meta` (class) — [saleor/graphql/app/mutations/app_update.py:28]
- `get_instance` (function) — [saleor/graphql/app/mutations/app_update.py:43]
- `clean_input` (function) — [saleor/graphql/app/mutations/app_update.py:49]
- `post_save_action` (function) — [saleor/graphql/app/mutations/app_update.py:69]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/app/mutations/app_fetch_manifest.py` (122 lines)
- `saleor/graphql/app/mutations/__init__.py` (33 lines)
- `saleor/graphql/app/mutations/app_activate.py` (43 lines)
- `saleor/graphql/app/mutations/app_create.py` (99 lines)
- `saleor/graphql/app/mutations/app_deactivate.py` (43 lines)
- `saleor/graphql/app/mutations/app_delete_failed_installation.py` (33 lines)
- `saleor/graphql/app/mutations/app_delete.py` (61 lines)
- `saleor/graphql/app/mutations/app_install.py` (86 lines)
- `saleor/graphql/app/mutations/app_problem_create.py` (202 lines)
- `saleor/graphql/app/mutations/app_problem_dismiss.py` (327 lines)
- `saleor/graphql/app/mutations/app_reenable_sync_webhooks.py` (75 lines)
- `saleor/graphql/app/mutations/app_retry_install.py` (62 lines)
- `saleor/graphql/app/mutations/app_token_create.py` (69 lines)
- `saleor/graphql/app/mutations/app_token_delete.py` (46 lines)
- `saleor/graphql/app/mutations/app_token_verify.py` (36 lines)
- `saleor/graphql/app/mutations/app_update.py` (71 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/graphql/core/types`
- Imported by: `saleor/graphql/app/tests/mutations`

Internal dependencies named in the source:

- `....account.models.User`
- `....app.actions.delete_app`
- `....app.error_codes.AppErrorCode`
- `....app.installation_utils.fetch_brand_data`
- `....app.installation_utils.fetch_manifest`
- `....app.lock_objects.app_problem_qs_select_for_update`
- `....app.lock_objects.app_qs_select_for_update`
- `....app.manifest_validations.clean_manifest_data`
- `....app.manifest_validations.clean_manifest_url`
- `....app.models`
- `....app.models.App`
- `....app.models.AppProblem`
- `....app.tasks.install_app_task`
- `....core.JobStatus`
- `....core.tracing.traced_atomic_transaction`
- `....graphql.app.enums.CircuitBreakerState`
- `....graphql.app.types.App`
- `....permission.auth_filters.AuthorizationFilters`
- `....permission.enums.AppPermission`
- `....permission.enums.get_permissions`
- `....webhook.event_types.WebhookEventAsyncType`
- `...account.utils.can_manage_app`
- `...core.ResolveInfo`
- `...core.descriptions.ADDED_IN_322`
- `...core.doc_category.DOC_CATEGORY_APPS`
- `...core.enums.PermissionEnum`
- `...core.mutations.BaseMutation`
- `...core.mutations.DeprecatedModelMutation`
- `...core.mutations.ModelDeleteMutation`
- `...core.scalars.Minute`
- `...core.scalars.PositiveInt`
- `...core.types`
- `...core.types.AppError`
- `...core.types.BaseInputObjectType`
- `...core.types.Error`
- `...core.types.NonNullList`
- `...core.utils.WebhookEventInfo`
- `...core.utils.from_global_id_or_error`
- `...core.validators.validate_one_of_args_is_in_mutation`
- `...decorators.staff_member_required`
- `...error.pydantic_to_validation_error`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `...utils.get_user_or_app_from_context`
- `...utils.requestor_is_superuser`
- `..enums.AppProblemCreateErrorCode`
- `..enums.AppProblemDismissErrorCode`
- `..types.App`
- `..types.AppInstallation`
- `..types.AppProblem`
- `..types.AppToken`
- `..types.Manifest`
- `..utils.ensure_app_permissions_allowed`
- `..utils.ensure_can_manage_permissions`
- `..utils.validate_app_is_not_removed`
- `.app_activate.AppActivate`
- `.app_create.AppCreate`
- `.app_create.AppInput`
- `.app_deactivate.AppDeactivate`
- `.app_delete.AppDelete`
- `.app_delete_failed_installation.AppDeleteFailedInstallation`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `b1cded4e0014` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
