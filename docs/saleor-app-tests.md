## Purpose

`saleor/app/tests` (`saleor/app/tests`) groups 20 source file(s) exposing 140 top-level declaration(s).

## Public surface

**`saleor/app/tests/tasks/test_saleor3_23.py`**

- `test_skip_settings_if_filled` (function) — [saleor/app/tests/tasks/test_saleor3_23.py:7]
- `test_fill_settings_json_for_new_tab_target` (function) — [saleor/app/tests/tasks/test_saleor3_23.py:32]
- `test_fill_settings_json_skips_non_widget_non_new_tab_targets` (function) — [saleor/app/tests/tasks/test_saleor3_23.py:56]

**`saleor/app/tests/test_app_actions.py`**

- `test_delete_app_soft_deletes_and_calls_app_deleted` (function) — [saleor/app/tests/test_app_actions.py:13]
- `test_delete_app_force_sync_renders_subscription_inline` (function) — [saleor/app/tests/test_app_actions.py:33]
- `test_delete_app_force_sync_skips_legacy_webhooks_without_subscription` (function) — [saleor/app/tests/test_app_actions.py:70]
- `test_delete_app_force_sync_with_no_webhooks_does_not_create_deliveries` (function) — [saleor/app/tests/test_app_actions.py:98]

**`saleor/app/tests/test_app_commands.py`**

- `test_creates_app_from_manifest` (function) — [saleor/app/tests/test_app_commands.py:21]
- `test_creates_app_from_manifest_activate_app` (function) — [saleor/app/tests/test_app_commands.py:35]
- `test_creates_app_from_manifest_app_has_all_required_permissions` (function) — [saleor/app/tests/test_app_commands.py:48]
- `test_creates_app_from_manifest_sends_token_when_target_url_provided` (function) — [saleor/app/tests/test_app_commands.py:58]
- `test_creates_app_from_manifest_skips_sending_token_when_target_url_not_provided` (function) — [saleor/app/tests/test_app_commands.py:108]
- `test_creates_app_from_manifest_installation_failed` (function) — [saleor/app/tests/test_app_commands.py:150]
- `installed_app` (function) — [saleor/app/tests/test_app_commands.py:162]
- `test_creates_app_from_manifest_fails_on_already_installed_app` (function) — [saleor/app/tests/test_app_commands.py:187]
- `test_creates_app_from_manifest_quiet_skips_already_installed_app` (function) — [saleor/app/tests/test_app_commands.py:195]
- `test_creates_app_object` (function) — [saleor/app/tests/test_app_commands.py:204]
- `test_app_has_all_required_permissions` (function) — [saleor/app/tests/test_app_commands.py:219]
- `test_sends_data_to_target_url` (function) — [saleor/app/tests/test_app_commands.py:232]
- `test_create_app_command_rejects_manage_apps_permission` (function) — [saleor/app/tests/test_app_commands.py:260]
- `test_creates_app_with_identifier` (function) — [saleor/app/tests/test_app_commands.py:272]
- `test_app_delete_all_deletes_every_installed_app` (function) — [saleor/app/tests/test_app_commands.py:304]
- `test_app_delete_all_skips_already_removed_apps` (function) — [saleor/app/tests/test_app_commands.py:328]
- `test_app_delete_all_with_no_apps_does_not_call_manager` (function) — [saleor/app/tests/test_app_commands.py:354]
- `test_app_delete_all_without_force_sync_calls_app_deleted_on_manager` (function) — [saleor/app/tests/test_app_commands.py:367]
- `test_app_delete_all_with_force_sync_dispatches_sync_webhooks` (function) — [saleor/app/tests/test_app_commands.py:391]

**`saleor/app/tests/test_app_tasks.py`**

- `test_install_app_task` (function) — [saleor/app/tests/test_app_tasks.py:18]
- `test_install_app_task_job_id_does_not_exist` (function) — [saleor/app/tests/test_app_tasks.py:27]
- `test_install_app_task_wrong_format_of_target_token_url` (function) — [saleor/app/tests/test_app_tasks.py:47]
- `test_install_app_task_request_timeout` (function) — [saleor/app/tests/test_app_tasks.py:60]
- `test_install_app_task_wrong_response_code` (function) — [saleor/app/tests/test_app_tasks.py:75]
- `test_install_app_task_installation_error` (function) — [saleor/app/tests/test_app_tasks.py:90]
- `test_install_app_task_undefined_error` (function) — [saleor/app/tests/test_app_tasks.py:102]
- `test_remove_app_task` (function) — [saleor/app/tests/test_app_tasks.py:116]
- `test_remove_app_task_not_remove_not_own_payloads` (function) — [saleor/app/tests/test_app_tasks.py:147]
- `test_remove_app_task_no_app_to_remove` (function) — [saleor/app/tests/test_app_tasks.py:161]
- `test_remove_app_task_delete_period_in_progress` (function) — [saleor/app/tests/test_app_tasks.py:172]

**`saleor/app/tests/test_installation_utils.py`**

- `test_validate_app_install_response` (function) — [saleor/app/tests/test_installation_utils.py:31]
- `test_validate_app_install_response_when_wrong_error_message` (function) — [saleor/app/tests/test_installation_utils.py:44]
- `test_install_app_created_app` (function) — [saleor/app/tests/test_installation_utils.py:53]
- `test_install_app_created_app_with_audience` (function) — [saleor/app/tests/test_installation_utils.py:105]
- `test_install_app_with_required_saleor_version` (function) — [saleor/app/tests/test_installation_utils.py:124]
- `test_install_app_when_saleor_version_unsupported` (function) — [saleor/app/tests/test_installation_utils.py:141]
- `test_install_app_with_author` (function) — [saleor/app/tests/test_installation_utils.py:161]
- `test_install_app_with_empty_author` (function) — [saleor/app/tests/test_installation_utils.py:177]
- `test_install_app_with_brand_data` (function) — [saleor/app/tests/test_installation_utils.py:195]
- `test_install_app_created_app_trigger_webhook` (function) — [saleor/app/tests/test_installation_utils.py:221]
- `test_install_app_with_extension` (function) — [saleor/app/tests/test_installation_utils.py:266]
- `test_install_app_with_extension_identifier` (function) — [saleor/app/tests/test_installation_utils.py:312]
- `test_install_app_with_extension_blank_identifier_stored_as_none` (function) — [saleor/app/tests/test_installation_utils.py:340]
- `test_install_app_with_extension_widget` (function) — [saleor/app/tests/test_installation_utils.py:367]
- `test_install_app_extension_permission_out_of_scope` (function) — [saleor/app/tests/test_installation_utils.py:422]
- `test_install_app_with_extension_new_tab_target` (function) — [saleor/app/tests/test_installation_utils.py:453]
- `test_install_app_extension_incorrect_url` (function) — [saleor/app/tests/test_installation_utils.py:506]
- `test_install_app_extension_invalid_permission` (function) — [saleor/app/tests/test_installation_utils.py:532]
- `test_install_app_extension_incorrect_values` (function) — [saleor/app/tests/test_installation_utils.py:571]
- `test_install_app_with_extension_post_method` (function) — [saleor/app/tests/test_installation_utils.py:603]
- `test_install_app_with_webhook` (function) — [saleor/app/tests/test_installation_utils.py:648]
- `test_install_app_with_webhook_identifier` (function) — [saleor/app/tests/test_installation_utils.py:678]
- `test_install_app_with_webhook_blank_identifier_stored_as_none` (function) — [saleor/app/tests/test_installation_utils.py:699]
- `test_install_app_webhook_incorrect_url` (function) — [saleor/app/tests/test_installation_utils.py:719]
- `test_install_app_with_webhook_is_active` (function) — [saleor/app/tests/test_installation_utils.py:740]
- `test_install_app_with_webhook_incorrect_is_active_value` (function) — [saleor/app/tests/test_installation_utils.py:760]
- `test_install_app_webhook_incorrect_query` (function) — [saleor/app/tests/test_installation_utils.py:782]
- `test_install_app_webhook_incorrect_custom_headers` (function) — [saleor/app/tests/test_installation_utils.py:814]
- `test_install_app_manifest_data_without_token_target_url` (function) — [saleor/app/tests/test_installation_utils.py:838]
- `image_response_mock` (function) — [saleor/app/tests/test_installation_utils.py:862]
- `test_fetch_icon_image` (function) — [saleor/app/tests/test_installation_utils.py:877]
- `test_fetch_icon_image_invalid_type` (function) — [saleor/app/tests/test_installation_utils.py:900]
- `test_fetch_icon_image_content_length` (function) — [saleor/app/tests/test_installation_utils.py:913]
- `test_fetch_icon_image_file_too_big` (function) — [saleor/app/tests/test_installation_utils.py:924]
- `content_chunks` (function) — [saleor/app/tests/test_installation_utils.py:925]
- `test_fetch_brand_data_task` (function) — [saleor/app/tests/test_installation_utils.py:940]
- `test_fetch_brand_data_task_terminated` (function) — [saleor/app/tests/test_installation_utils.py:969]
- `test_fetch_brand_data_task_for_removed_app` (function) — [saleor/app/tests/test_installation_utils.py:978]
- `test_fetch_brand_data_task_terminated_when_brand_data_fetched` (function) — [saleor/app/tests/test_installation_utils.py:986]
- `test_fetch_brand_data_task_retry` (function) — [saleor/app/tests/test_installation_utils.py:996]
- _…and 3 more in this file_

**`saleor/app/tests/test_manifest_validations.py`**

- `test_manifest_schema_valid_minimal` (function) — [saleor/app/tests/test_manifest_validations.py:22]
- `test_manifest_schema_missing_required_fields` (function) — [saleor/app/tests/test_manifest_validations.py:32]
- `test_manifest_schema_invalid_token_target_url` (function) — [saleor/app/tests/test_manifest_validations.py:48]
- `test_manifest_schema_valid_token_target_url` (function) — [saleor/app/tests/test_manifest_validations.py:66]
- `test_manifest_schema_invalid_author_empty_string` (function) — [saleor/app/tests/test_manifest_validations.py:80]
- `test_manifest_schema_valid_author_none` (function) — [saleor/app/tests/test_manifest_validations.py:98]
- `test_manifest_schema_valid_author_strips_whitespace` (function) — [saleor/app/tests/test_manifest_validations.py:112]
- `test_manifest_schema_brand_missing_logo_default` (function) — [saleor/app/tests/test_manifest_validations.py:126]
- `test_manifest_schema_brand_invalid_url` (function) — [saleor/app/tests/test_manifest_validations.py:142]
- `test_manifest_schema_brand_invalid_mime_type` (function) — [saleor/app/tests/test_manifest_validations.py:159]
- `test_manifest_schema_brand_valid_png` (function) — [saleor/app/tests/test_manifest_validations.py:177]
- `test_manifest_schema_extensions_null_defaults_to_empty_list` (function) — [saleor/app/tests/test_manifest_validations.py:192]
- `test_manifest_schema_webhooks_null_defaults_to_empty_list` (function) — [saleor/app/tests/test_manifest_validations.py:206]
- `test_manifest_schema_extension_missing_required_fields` (function) — [saleor/app/tests/test_manifest_validations.py:220]
- `test_manifest_schema_webhook_missing_required_fields` (function) — [saleor/app/tests/test_manifest_validations.py:238]
- `test_manifest_schema_webhook_is_active_defaults_to_true` (function) — [saleor/app/tests/test_manifest_validations.py:256]
- `test_manifest_schema_full_input` (function) — [saleor/app/tests/test_manifest_validations.py:276]
- `test_manifest_schema_extra_fields_ignored` (function) — [saleor/app/tests/test_manifest_validations.py:298]
- `test_clean_manifest_data_rejects_manage_apps_permission` (function) — [saleor/app/tests/test_manifest_validations.py:314]
- `test_clean_manifest_data_rejects_manage_apps_permission_alongside_others` (function) — [saleor/app/tests/test_manifest_validations.py:338]
- `test_clean_manifest_data_rejects_manage_apps_permission_on_extension` (function) — [saleor/app/tests/test_manifest_validations.py:360]
- `test_clean_manifest_data_rejects_manage_apps_permission_on_extension_alongside_others` (function) — [saleor/app/tests/test_manifest_validations.py:393]
- `test_clean_manifest_data_accepts_unique_extension_identifiers` (function) — [saleor/app/tests/test_manifest_validations.py:451]
- `test_clean_manifest_data_rejects_duplicate_extension_identifiers` (function) — [saleor/app/tests/test_manifest_validations.py:470]
- `test_clean_manifest_data_allows_multiple_extensions_without_identifier` (function) — [saleor/app/tests/test_manifest_validations.py:494]
- `test_clean_manifest_data_coerces_blank_identifier_to_none` (function) — [saleor/app/tests/test_manifest_validations.py:513]
- `test_clean_manifest_data_strips_surrounding_whitespace_from_identifier` (function) — [saleor/app/tests/test_manifest_validations.py:532]
- `test_clean_manifest_data_accepts_identifier_at_max_length` (function) — [saleor/app/tests/test_manifest_validations.py:547]
- `test_clean_manifest_data_rejects_too_long_identifier` (function) — [saleor/app/tests/test_manifest_validations.py:563]
- `test_clean_manifest_data_length_check_ignores_surrounding_whitespace` (function) — [saleor/app/tests/test_manifest_validations.py:588]
- `test_clean_manifest_data_accepts_unique_webhook_identifiers` (function) — [saleor/app/tests/test_manifest_validations.py:605]
- `test_clean_manifest_data_rejects_duplicate_webhook_identifiers` (function) — [saleor/app/tests/test_manifest_validations.py:624]
- `test_clean_manifest_data_allows_multiple_webhooks_without_identifier` (function) — [saleor/app/tests/test_manifest_validations.py:648]
- `test_clean_manifest_data_coerces_blank_webhook_identifier_to_none` (function) — [saleor/app/tests/test_manifest_validations.py:664]
- `test_clean_manifest_data_strips_surrounding_whitespace_from_webhook_identifier` (function) — [saleor/app/tests/test_manifest_validations.py:683]
- `test_clean_manifest_data_accepts_webhook_identifier_at_max_length` (function) — [saleor/app/tests/test_manifest_validations.py:698]
- `test_clean_manifest_data_rejects_too_long_webhook_identifier` (function) — [saleor/app/tests/test_manifest_validations.py:714]
- `test_clean_manifest_data_webhook_length_check_ignores_surrounding_whitespace` (function) — [saleor/app/tests/test_manifest_validations.py:739]
- `test_manifest_schema_deprecated_fields_accepted` (function) — [saleor/app/tests/test_manifest_validations.py:755]

**`saleor/app/tests/test_models.py`**

- `test_qs_for_event_type` (function) — [saleor/app/tests/test_models.py:10]
- `test_qs_for_event_type_no_payment_permissions` (function) — [saleor/app/tests/test_models.py:16]
- `test_qs_for_event_type_inactive_app` (function) — [saleor/app/tests/test_models.py:22]
- `test_qs_for_event_type_no_webhook_event` (function) — [saleor/app/tests/test_models.py:29]
- `test_qs_for_event_type_inactive_webhook` (function) — [saleor/app/tests/test_models.py:39]
- `test_app_extension_identifier_must_be_unique_per_app` (function) — [saleor/app/tests/test_models.py:47]
- `test_app_extension_identifier_can_be_reused_across_apps` (function) — [saleor/app/tests/test_models.py:69]
- `test_app_extension_allows_multiple_null_identifiers_per_app` (function) — [saleor/app/tests/test_models.py:94]
- `test_app_extension_identifier_cannot_be_blank` (function) — [saleor/app/tests/test_models.py:114]
- `test_app_installation_set_message_truncates` (function) — [saleor/app/tests/test_models.py:126]

**`saleor/app/tests/test_utils.py`**

- `test_get_active_tax_apps` (function) — [saleor/app/tests/test_utils.py:6]
- `test_get_active_tax_app_no_permission` (function) — [saleor/app/tests/test_utils.py:27]
- `test_get_active_tax_app_only_one_webhook` (function) — [saleor/app/tests/test_utils.py:42]

**`saleor/app/tests/test_validators.py`**

- `test_validate_url` (function) — [saleor/app/tests/test_validators.py:16]
- `test_validate_invalid_url` (function) — [saleor/app/tests/test_validators.py:22]
- `test_parse_version` (function) — [saleor/app/tests/test_validators.py:29]
- `test_clean_required_saleor_version` (function) — [saleor/app/tests/test_validators.py:44]
- `test_clean_required_saleor_version_optional` (function) — [saleor/app/tests/test_validators.py:49]
- `test_clean_required_saleor_version_with_invalid_range` (function) — [saleor/app/tests/test_validators.py:56]
- `test_clean_required_saleor_version_raise_for_saleor_version` (function) — [saleor/app/tests/test_validators.py:62]
- `test_new_tab_relative_url_without_app_url` (function) — [saleor/app/tests/test_validators.py:68]

## How it works

The module's files, as provided to this run:

- `saleor/app/tests/__init__.py` (1 lines)
- `saleor/app/tests/cassettes/test_app_commands/test_creates_app_from_manifest_activate_app.yaml` (163 lines)
- `saleor/app/tests/cassettes/test_app_commands/test_creates_app_from_manifest_app_has_all_required_permissions.yaml` (163 lines)
- `saleor/app/tests/cassettes/test_app_commands/test_creates_app_from_manifest_installation_failed.yaml` (100 lines)
- `saleor/app/tests/cassettes/test_app_commands/test_creates_app_from_manifest.yaml` (163 lines)
- `saleor/app/tests/cassettes/test_app_tasks/test_install_app_task_request_timeout.yaml` (53 lines)
- `saleor/app/tests/cassettes/test_app_tasks/test_install_app_task_wrong_format_of_target_token_url.yaml` (51 lines)
- `saleor/app/tests/cassettes/test_app_tasks/test_install_app_task_wrong_response_code.yaml` (46 lines)
- `saleor/app/tests/cassettes/test_app_tasks/test_install_app_task.yaml` (112 lines)
- `saleor/app/tests/cassettes/test_sends_data_to_target_url.yaml` (52 lines)
- `saleor/app/tests/tasks/__init__.py` (1 lines)
- `saleor/app/tests/tasks/test_saleor3_23.py` (79 lines)
- `saleor/app/tests/test_app_actions.py` (115 lines)
- `saleor/app/tests/test_app_commands.py` (428 lines)
- `saleor/app/tests/test_app_tasks.py` (181 lines)
- `saleor/app/tests/test_installation_utils.py` (1059 lines)
- `saleor/app/tests/test_manifest_validations.py` (772 lines)
- `saleor/app/tests/test_models.py` (134 lines)
- `saleor/app/tests/test_utils.py` (54 lines)
- `saleor/app/tests/test_validators.py` (81 lines)

## Interactions

- Imports from: `saleor/app`, `saleor/account`, `saleor/core`, `saleor/webhook/response_schemas`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....__version__`
- `....schema_version`
- `...app.models.App`
- `...app.utils.get_active_tax_apps`
- `...core.JobStatus`
- `...core.models.EventDelivery`
- `...core.models.EventDeliveryAttempt`
- `...core.models.EventPayload`
- `...core.private_storage`
- `...core.tests.test_taxes.app_factory`
- `...core.tests.test_taxes.tax_app_factory  # noqa: F401`
- `...core.utils.json_serializer.CustomJsonEncoder`
- `...permission.enums.AppPermission`
- `...permission.enums.ProductPermissions`
- `...permission.enums.get_permissions`
- `...webhook.event_types.WebhookEventAsyncType`
- `...webhook.event_types.WebhookEventSyncType`
- `...webhook.models.Webhook`
- `...webhook.payloads.generate_meta`
- `...webhook.payloads.generate_requestor`
- `..actions.delete_app`
- `..error_codes.AppErrorCode`
- `..installation_utils.AppInstallationError`
- `..manifest_validations.clean_manifest_data`
- `..models.App`
- `..models.AppExtension`
- `..models.AppInstallation`
- `..models.AppToken`
- `..tasks.install_app_task`
- `..tasks.remove_apps_task`
- `..types.AppType`
- `saleor.app.models.App`
- `saleor.app.models.AppExtension`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `8b5e47810424` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
