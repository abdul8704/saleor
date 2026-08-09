## Purpose

`saleor/graphql/app/tests/mutations` (`saleor/graphql/app/tests/mutations`) groups 30 source file(s) exposing 162 top-level declaration(s).

## Public surface

**`saleor/graphql/app/tests/mutations/test_app_activate.py`**

- `test_activate_app` (function) — [saleor/graphql/app/tests/mutations/test_app_activate.py:32]
- `test_activate_app_trigger_webhook` (function) — [saleor/graphql/app/tests/mutations/test_app_activate.py:57]
- `test_activate_app_by_app` (function) — [saleor/graphql/app/tests/mutations/test_app_activate.py:109]
- `test_activate_app_missing_permission` (function) — [saleor/graphql/app/tests/mutations/test_app_activate.py:129]
- `test_activate_app_by_app_missing_permission` (function) — [saleor/graphql/app/tests/mutations/test_app_activate.py:153]
- `test_app_has_more_permission_than_user_requestor` (function) — [saleor/graphql/app/tests/mutations/test_app_activate.py:174]
- `test_app_has_more_permission_than_app_requestor` (function) — [saleor/graphql/app/tests/mutations/test_app_activate.py:204]
- `test_app_activate_mutation_removed_app` (function) — [saleor/graphql/app/tests/mutations/test_app_activate.py:233]

**`saleor/graphql/app/tests/mutations/test_app_create.py`**

- `test_app_create_mutation` (function) — [saleor/graphql/app/tests/mutations/test_app_create.py:48]
- `test_app_create_no_identifier_mutation` (function) — [saleor/graphql/app/tests/mutations/test_app_create.py:80]
- `test_app_create_without_permissions` (function) — [saleor/graphql/app/tests/mutations/test_app_create.py:122]
- `test_app_create_trigger_webhook` (function) — [saleor/graphql/app/tests/mutations/test_app_create.py:150]
- `test_app_is_not_allowed_to_call_create_mutation_for_app` (function) — [saleor/graphql/app/tests/mutations/test_app_create.py:202]
- `test_app_create_mutation_out_of_scope_permissions` (function) — [saleor/graphql/app/tests/mutations/test_app_create.py:225]
- `test_app_create_mutation_superuser_can_create_app_with_any_perms` (function) — [saleor/graphql/app/tests/mutations/test_app_create.py:256]
- `test_app_create_mutation_no_permissions` (function) — [saleor/graphql/app/tests/mutations/test_app_create.py:281]
- `test_app_create_rejects_manage_apps_permission` (function) — [saleor/graphql/app/tests/mutations/test_app_create.py:296]

**`saleor/graphql/app/tests/mutations/test_app_deactivate.py`**

- `test_deactivate_app` (function) — [saleor/graphql/app/tests/mutations/test_app_deactivate.py:32]
- `test_deactivate_app_trigger_webhook` (function) — [saleor/graphql/app/tests/mutations/test_app_deactivate.py:57]
- `test_deactivate_app_by_app` (function) — [saleor/graphql/app/tests/mutations/test_app_deactivate.py:109]
- `test_deactivate_app_missing_permission` (function) — [saleor/graphql/app/tests/mutations/test_app_deactivate.py:129]
- `test_activate_app_by_app_missing_permission` (function) — [saleor/graphql/app/tests/mutations/test_app_deactivate.py:153]
- `test_app_has_more_permission_than_user_requestor` (function) — [saleor/graphql/app/tests/mutations/test_app_deactivate.py:174]
- `test_app_has_more_permission_than_app_requestor` (function) — [saleor/graphql/app/tests/mutations/test_app_deactivate.py:204]
- `test_deactivate_app_for_removed_app` (function) — [saleor/graphql/app/tests/mutations/test_app_deactivate.py:233]

**`saleor/graphql/app/tests/mutations/test_app_delete_failed_installation.py`**

- `test_drop_failed_installation_mutation` (function) — [saleor/graphql/app/tests/mutations/test_app_delete_failed_installation.py:22]
- `test_drop_failed_installation_mutation_by_app` (function) — [saleor/graphql/app/tests/mutations/test_app_delete_failed_installation.py:52]
- `test_drop_failed_installation_mutation_app_has_more_permission_than_user_requestor` (function) — [saleor/graphql/app/tests/mutations/test_app_delete_failed_installation.py:83]
- `test_drop_failed_installation_mutation_app_has_more_permission_than_app_requestor` (function) — [saleor/graphql/app/tests/mutations/test_app_delete_failed_installation.py:115]
- `test_cannot_drop_installation_if_status_is_different_than_failed` (function) — [saleor/graphql/app/tests/mutations/test_app_delete_failed_installation.py:141]

**`saleor/graphql/app/tests/mutations/test_app_delete.py`**

- `test_app_delete` (function) — [saleor/graphql/app/tests/mutations/test_app_delete.py:31]
- `test_app_delete_trigger_webhook` (function) — [saleor/graphql/app/tests/mutations/test_app_delete.py:61]
- `test_app_delete_for_app` (function) — [saleor/graphql/app/tests/mutations/test_app_delete.py:112]
- `test_app_delete_out_of_scope_app` (function) — [saleor/graphql/app/tests/mutations/test_app_delete.py:139]
- `test_app_delete_superuser_can_delete_any_app` (function) — [saleor/graphql/app/tests/mutations/test_app_delete.py:167]
- `test_app_delete_for_app_out_of_scope_app` (function) — [saleor/graphql/app/tests/mutations/test_app_delete.py:192]
- `test_app_delete_with_removed_app` (function) — [saleor/graphql/app/tests/mutations/test_app_delete.py:217]

**`saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py`**

- `test_app_fetch_manifest` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:73]
- `test_app_fetch_manifest_custom_saleor_headers` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:107]
- `test_app_fetch_manifest_with_audience` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:135]
- `test_app_fetch_manifest_missing_permission` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:155]
- `test_app_fetch_manifest_incorrect_permission_in_manifest` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:169]
- `test_app_fetch_manifest_unable_to_connect` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:195]
- `test_app_fetch_manifest_timeout` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:219]
- `test_app_fetch_manifest_wrong_format_of_response` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:247]
- `test_app_fetch_manifest_handle_exception` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:271]
- `test_app_fetch_manifest_missing_fields` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:307]
- `test_app_fetch_manifest_missing_extension_fields` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:347]
- `test_app_fetch_manifest_extensions_permission_out_of_scope` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:394]
- `test_app_fetch_manifest_extensions_invalid_permission` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:440]
- `test_app_fetch_manifest_with_extensions` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:481]
- `test_app_fetch_manifest_with_extension_identifier` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:534]
- `test_app_fetch_manifest_with_widget_extension_settings` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:571]
- `test_app_fetch_manifest_with_new_tab_extension_settings` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:620]
- `test_app_fetch_manifest_with_required_saleor_version` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:669]
- `test_app_fetch_manifest_with_invalid_required_saleor_version` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:696]
- `test_app_fetch_manifest_with_author` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:721]
- `test_app_fetch_manifest_with_empty_author` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:744]
- `test_app_fetch_manifest_with_brand_data` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:776]
- `test_app_fetch_manifest_with_invalid_brand_data` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:821]
- `test_fetch_manifest_fail_when_app_with_same_identifier_already_installed` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:846]
- `test_fetch_manifest_app_with_same_identifier_installed_but_marked_to_be_removed` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:880]
- `test_app_fetch_manifest_extension_without_options` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:918]
- `test_app_fetch_manifest_extension_with_relative_url` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:959]
- `test_app_fetch_manifest_extension_with_absolute_url` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:1008]
- `test_app_fetch_manifest_extension_with_invalid_absolute_url` (function) — [saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py:1048]

**`saleor/graphql/app/tests/mutations/test_app_install.py`**

- `test_install_app_mutation` (function) — [saleor/graphql/app/tests/mutations/test_app_install.py:40]
- `test_install_app_mutation_with_another_app_installed_but_marked_to_be_removed` (function) — [saleor/graphql/app/tests/mutations/test_app_install.py:73]
- `test_app_is_not_allowed_to_install_app` (function) — [saleor/graphql/app/tests/mutations/test_app_install.py:108]
- `test_app_install_mutation_out_of_scope_permissions` (function) — [saleor/graphql/app/tests/mutations/test_app_install.py:128]
- `test_install_app_mutation_with_the_same_identifier_twice` (function) — [saleor/graphql/app/tests/mutations/test_app_install.py:155]
- `test_install_app_mutation_with_invalid_manifest_url_returns_error` (function) — [saleor/graphql/app/tests/mutations/test_app_install.py:196]
- `test_install_app_mutation_with_null_permissions` (function) — [saleor/graphql/app/tests/mutations/test_app_install.py:221]
- `test_app_install_rejects_manage_apps_permission` (function) — [saleor/graphql/app/tests/mutations/test_app_install.py:242]

**`saleor/graphql/app/tests/mutations/test_app_problem_create_aggregation.py`**

- `test_app_problem_create_aggregates_within_period` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_aggregation.py:29]
- `test_app_problem_create_new_when_period_expired` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_aggregation.py:62]
- `test_app_problem_create_zero_aggregation_period_always_creates_new` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_aggregation.py:97]
- `test_app_problem_create_default_aggregation_period_aggregates` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_aggregation.py:123]
- `test_app_problem_create_dismissed_problem_not_aggregated` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_aggregation.py:151]
- `test_app_problem_create_message_updates_on_aggregation` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_aggregation.py:185]

**`saleor/graphql/app/tests/mutations/test_app_problem_create_critical.py`**

- `test_app_problem_create_critical_threshold_reached` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_critical.py:29]
- `test_app_problem_create_critical_threshold_not_reached` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_critical.py:62]
- `test_app_problem_create_critical_threshold_reached_via_aggregation` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_critical.py:95]
- `test_app_problem_create_critical_threshold_de_escalates` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_critical.py:128]
- `test_app_problem_create_critical_threshold_not_reached_due_to_expired_aggregation` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_critical.py:162]
- `test_app_problem_create_critical_on_first_problem` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_critical.py:204]

**`saleor/graphql/app/tests/mutations/test_app_problem_create_eviction.py`**

- `test_app_problem_create_limit_eviction` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_eviction.py:33]
- `test_app_problem_create_bulk_eviction_when_over_limit` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_eviction.py:63]

**`saleor/graphql/app/tests/mutations/test_app_problem_create_validation.py`**

- `test_app_problem_create_negative_aggregation_period_fails` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_validation.py:30]
- `test_app_problem_create_zero_critical_threshold_fails` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_validation.py:52]
- `test_app_problem_create_negative_critical_threshold_fails` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_validation.py:73]
- `test_app_problem_create_null_aggregation_period_defaults_to_60` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_validation.py:94]
- `test_app_problem_create_message_too_short_fails` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_validation.py:128]
- `test_app_problem_create_message_too_long_is_truncated` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_validation.py:150]
- `test_app_problem_create_key_too_short_fails` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_validation.py:172]
- `test_app_problem_create_key_too_long_fails` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_validation.py:194]
- `test_app_problem_create_message_at_2048_chars_is_not_truncated` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_validation.py:216]
- `test_app_problem_create_key_at_max_length_succeeds` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create_validation.py:238]

**`saleor/graphql/app/tests/mutations/test_app_problem_create.py`**

- `test_app_problem_create` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create.py:25]
- `test_app_problem_create_by_staff_user_fails` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_create.py:48]

**`saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_app.py`**

- `test_app_problem_dismiss_by_ids_as_app` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_app.py:20]
- `test_app_problem_dismiss_by_keys_as_app` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_app.py:47]
- `test_app_problem_dismiss_by_ids_and_keys_as_app_fails` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_app.py:69]
- `test_app_problem_dismiss_idempotent` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_app.py:95]
- `test_app_cannot_dismiss_other_apps_problems` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_app.py:113]
- `test_app_caller_cannot_use_by_staff_with_ids` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_app.py:140]
- `test_app_caller_cannot_use_by_staff_with_keys` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_app.py:166]
- `test_app_problem_dismiss_by_app_with_too_many_ids_fails` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_app.py:192]
- `test_app_problem_dismiss_by_app_with_too_many_keys_fails` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_app.py:211]

**`saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_staff_with_ids.py`**

- `test_app_problem_dismiss_by_ids_as_staff` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_staff_with_ids.py:20]
- `test_staff_can_dismiss_problems_from_multiple_apps` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_staff_with_ids.py:47]
- `test_user_caller_cannot_use_by_app` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_staff_with_ids.py:82]
- `test_app_problem_dismiss_by_staff_with_too_many_ids_fails` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_staff_with_ids.py:104]

**`saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_staff_with_keys.py`**

- `test_app_problem_dismiss_by_keys_as_staff` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_staff_with_keys.py:20]
- `test_app_problem_dismiss_by_staff_with_too_many_keys_fails` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_staff_with_keys.py:48]

**`saleor/graphql/app/tests/mutations/test_app_problem_dismiss.py`**

- `test_app_problem_dismiss_multiple_inputs_fails` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss.py:21]
- `test_app_problem_dismiss_no_input_fails` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss.py:50]
- `test_app_problem_dismiss_empty_by_app_fails` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss.py:69]
- `test_app_problem_dismiss_without_permission` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss.py:88]
- `test_app_problem_dismiss_with_non_integer_id_fails` (function) — [saleor/graphql/app/tests/mutations/test_app_problem_dismiss.py:106]

**`saleor/graphql/app/tests/mutations/test_app_retry_install.py`**

- `test_retry_install_app_mutation` (function) — [saleor/graphql/app/tests/mutations/test_app_retry_install.py:38]
- `test_retry_install_app_mutation_with_another_app_installed_but_marked_to_be_removed` (function) — [saleor/graphql/app/tests/mutations/test_app_retry_install.py:73]
- `test_retry_install_app_mutation_by_app` (function) — [saleor/graphql/app/tests/mutations/test_app_retry_install.py:110]
- `test_retry_install_app_mutation_app_has_more_permission_than_user_requestor` (function) — [saleor/graphql/app/tests/mutations/test_app_retry_install.py:145]
- `test_retry_install_app_mutation_app_has_more_permission_than_app_requestor` (function) — [saleor/graphql/app/tests/mutations/test_app_retry_install.py:184]
- `test_cannot_retry_installation_if_status_is_different_than_failed` (function) — [saleor/graphql/app/tests/mutations/test_app_retry_install.py:222]
- `test_install_retry_app_mutation_with_the_same_identifier_twice` (function) — [saleor/graphql/app/tests/mutations/test_app_retry_install.py:263]

**`saleor/graphql/app/tests/mutations/test_app_token_create.py`**

- `test_app_token_create` (function) — [saleor/graphql/app/tests/mutations/test_app_token_create.py:26]
- `test_app_token_create_for_app` (function) — [saleor/graphql/app/tests/mutations/test_app_token_create.py:54]
- `test_app_token_create_out_of_scope_app` (function) — [saleor/graphql/app/tests/mutations/test_app_token_create.py:87]
- `test_app_token_create_superuser_can_create_token_for_any_app` (function) — [saleor/graphql/app/tests/mutations/test_app_token_create.py:120]
- `test_app_token_create_as_app_out_of_scope_app` (function) — [saleor/graphql/app/tests/mutations/test_app_token_create.py:148]
- `test_app_token_create_no_permissions` (function) — [saleor/graphql/app/tests/mutations/test_app_token_create.py:180]
- `test_app_token_create_for_removed_app` (function) — [saleor/graphql/app/tests/mutations/test_app_token_create.py:194]

**`saleor/graphql/app/tests/mutations/test_app_token_delete.py`**

- `test_app_token_delete` (function) — [saleor/graphql/app/tests/mutations/test_app_token_delete.py:24]
- `test_app_token_delete_for_app` (function) — [saleor/graphql/app/tests/mutations/test_app_token_delete.py:45]
- `test_app_token_delete_no_permissions` (function) — [saleor/graphql/app/tests/mutations/test_app_token_delete.py:67]
- `test_app_token_delete_out_of_scope_app` (function) — [saleor/graphql/app/tests/mutations/test_app_token_delete.py:78]
- `test_app_token_delete_superuser_can_delete_token_for_any_app` (function) — [saleor/graphql/app/tests/mutations/test_app_token_delete.py:109]
- `test_app_token_delete_for_app_out_of_scope_app` (function) — [saleor/graphql/app/tests/mutations/test_app_token_delete.py:135]
- `test_app_token_delete_for_removed_app` (function) — [saleor/graphql/app/tests/mutations/test_app_token_delete.py:163]

**`saleor/graphql/app/tests/mutations/test_app_token_verify.py`**

- `test_app_token_verify_valid_token` (function) — [saleor/graphql/app/tests/mutations/test_app_token_verify.py:17]
- `test_app_token_verify_invalid_token` (function) — [saleor/graphql/app/tests/mutations/test_app_token_verify.py:31]
- `test_app_token_verify_app_turned_off` (function) — [saleor/graphql/app/tests/mutations/test_app_token_verify.py:46]
- `test_app_token_verify_removed_app` (function) — [saleor/graphql/app/tests/mutations/test_app_token_verify.py:64]

**`saleor/graphql/app/tests/mutations/test_app_update.py`**

- `test_app_update_mutation` (function) — [saleor/graphql/app/tests/mutations/test_app_update.py:44]
- `test_app_update_trigger_mutation` (function) — [saleor/graphql/app/tests/mutations/test_app_update.py:86]
- `test_app_update_mutation_for_app` (function) — [saleor/graphql/app/tests/mutations/test_app_update.py:144]
- `test_app_update_mutation_out_of_scope_permissions` (function) — [saleor/graphql/app/tests/mutations/test_app_update.py:190]
- `test_app_update_mutation_superuser_can_add_any_permissions_to_app` (function) — [saleor/graphql/app/tests/mutations/test_app_update.py:224]
- `test_app_update_mutation_for_app_out_of_scope_permissions` (function) — [saleor/graphql/app/tests/mutations/test_app_update.py:262]
- `test_app_update_mutation_out_of_scope_app` (function) — [saleor/graphql/app/tests/mutations/test_app_update.py:300]
- `test_app_update_mutation_superuser_can_update_any_app` (function) — [saleor/graphql/app/tests/mutations/test_app_update.py:339]
- `test_app_update_mutation_for_app_out_of_scope_app` (function) — [saleor/graphql/app/tests/mutations/test_app_update.py:379]
- `test_app_update_no_permission` (function) — [saleor/graphql/app/tests/mutations/test_app_update.py:416]
- `test_app_update_mutation_removed_app` (function) — [saleor/graphql/app/tests/mutations/test_app_update.py:427]
- `test_app_update_null_permissions_leaves_them_untouched` (function) — [saleor/graphql/app/tests/mutations/test_app_update.py:470]
- `test_app_update_empty_permissions_clears_them` (function) — [saleor/graphql/app/tests/mutations/test_app_update.py:502]
- `test_app_update_rejects_manage_apps_permission` (function) — [saleor/graphql/app/tests/mutations/test_app_update.py:530]

**`saleor/graphql/app/tests/mutations/test_reenable_sync_webhooks.py`**

- `test_reenable_sync_webhooks` (function) — [saleor/graphql/app/tests/mutations/test_reenable_sync_webhooks.py:25]
- `test_reenable_sync_webhooks_id_not_in_storage` (function) — [saleor/graphql/app/tests/mutations/test_reenable_sync_webhooks.py:54]
- `test_reenable_sync_webhooks_non_existing_app_id` (function) — [saleor/graphql/app/tests/mutations/test_reenable_sync_webhooks.py:80]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/app/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/app/tests/mutations/cassettes/test_app_fetch_manifest/test_app_fetch_manifest_incorrect_permission_in_manifest.yaml` (53 lines)
- `saleor/graphql/app/tests/mutations/cassettes/test_app_fetch_manifest/test_app_fetch_manifest_unable_to_connect.yaml` (46 lines)
- `saleor/graphql/app/tests/mutations/cassettes/test_app_fetch_manifest/test_app_fetch_manifest_with_audience.yaml` (53 lines)
- `saleor/graphql/app/tests/mutations/cassettes/test_app_fetch_manifest/test_app_fetch_manifest_wrong_format_of_response.yaml` (46 lines)
- `saleor/graphql/app/tests/mutations/cassettes/test_app_fetch_manifest/test_app_fetch_manifest.yaml` (53 lines)
- `saleor/graphql/app/tests/mutations/cassettes/test_app_fetch_manifest/test_fetch_manifest_app_with_same_identifier_installed_but_marked_to_be_removed.yaml` (95 lines)
- `saleor/graphql/app/tests/mutations/cassettes/test_app_fetch_manifest/test_fetch_manifest_fail_when_app_with_same_identifier_already_installed.yaml` (95 lines)
- `saleor/graphql/app/tests/mutations/test_app_activate.py` (255 lines)
- `saleor/graphql/app/tests/mutations/test_app_create.py` (317 lines)
- `saleor/graphql/app/tests/mutations/test_app_deactivate.py` (253 lines)
- `saleor/graphql/app/tests/mutations/test_app_delete_failed_installation.py` (173 lines)
- `saleor/graphql/app/tests/mutations/test_app_delete.py` (237 lines)
- `saleor/graphql/app/tests/mutations/test_app_fetch_manifest.py` (1084 lines)
- `saleor/graphql/app/tests/mutations/test_app_install.py` (261 lines)
- `saleor/graphql/app/tests/mutations/test_app_problem_create_aggregation.py` (214 lines)
- `saleor/graphql/app/tests/mutations/test_app_problem_create_critical.py` (223 lines)
- `saleor/graphql/app/tests/mutations/test_app_problem_create_eviction.py` (98 lines)
- `saleor/graphql/app/tests/mutations/test_app_problem_create_validation.py` (255 lines)
- `saleor/graphql/app/tests/mutations/test_app_problem_create.py` (59 lines)
- `saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_app.py` (225 lines)
- `saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_staff_with_ids.py` (123 lines)
- `saleor/graphql/app/tests/mutations/test_app_problem_dismiss_by_staff_with_keys.py` (72 lines)
- `saleor/graphql/app/tests/mutations/test_app_problem_dismiss.py` (122 lines)
- `saleor/graphql/app/tests/mutations/test_app_retry_install.py` (304 lines)
- `saleor/graphql/app/tests/mutations/test_app_token_create.py` (221 lines)
- `saleor/graphql/app/tests/mutations/test_app_token_delete.py` (190 lines)
- `saleor/graphql/app/tests/mutations/test_app_token_verify.py` (77 lines)
- `saleor/graphql/app/tests/mutations/test_app_update.py` (558 lines)
- `saleor/graphql/app/tests/mutations/test_reenable_sync_webhooks.py` (101 lines)

## Interactions

- Imports from: `saleor/graphql/app/mutations`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `......schema_version`
- `.....app.error_codes.AppErrorCode`
- `.....app.error_codes.AppProblemCreateErrorCode`
- `.....app.error_codes.AppProblemDismissErrorCode`
- `.....app.models.App`
- `.....app.models.AppInstallation`
- `.....app.models.AppProblem`
- `.....app.models.AppToken`
- `.....app.tasks.install_app_task`
- `.....core.JobStatus`
- `.....core.utils.json_serializer.CustomJsonEncoder`
- `.....thumbnail.IconThumbnailFormat`
- `.....webhook.event_types.WebhookEventAsyncType`
- `.....webhook.payloads.generate_meta`
- `.....webhook.payloads.generate_requestor`
- `....core.enums.AppErrorCode`
- `....core.enums.PermissionEnum`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `...mutations.app_problem_dismiss.MAX_ITEMS_LIMIT`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `db0f78f37983` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
