## Purpose

`saleor/graphql/app/tests/queries` (`saleor/graphql/app/tests/queries`) groups 8 source file(s) exposing 96 top-level declaration(s).

## Public surface

**`saleor/graphql/app/tests/queries/test_app_extension.py`**

- `test_app_extension_staff_user` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:31]
- `test_app_extension_by_app` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:71]
- `test_app_extensions_app_removed_app` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:108]
- `test_app_extension_normal_user` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:134]
- `test_app_extension_staff_user_without_all_permissions` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:156]
- `test_app_extension_staff_user_fetching_access_token` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:184]
- `test_app_extension_access_token_with_audience` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:223]
- `test_app_extension_staff_user_partial_permission` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:265]
- `test_app_extension_access_token_errors_when_parent_app_has_manage_apps` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:299]
- `test_app_extension_access_token_errors_via_app_extensions_connection` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:355]
- `test_app_extension_with_app_query_by_staff_without_permissions` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:419]
- `test_app_extension_with_app_query_by_app_without_permissions` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:445]
- `test_app_extension_with_app_query_by_app_without_permissions_other_app` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:472]
- `test_app_extension_with_app_query_by_owner_app` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:512]
- `test_app_extension_with_app_query_by_staff_with_permissions` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:536]
- `test_app_extension_with_app_query_by_customer_without_permissions` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:561]
- `test_app_extension_type_settings_from_http_target_method` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:591]
- `test_app_extension_identifier_returned` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:639]
- `test_app_extension_identifier_null_when_not_set` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:664]
- `test_app_extension_type_settings_from_native_settings` (function) — [saleor/graphql/app/tests/queries/test_app_extension.py:687]

**`saleor/graphql/app/tests/queries/test_app_extensions.py`**

- `test_app_extensions` (function) — [saleor/graphql/app/tests/queries/test_app_extensions.py:29]
- `test_app_extensions_app_not_active` (function) — [saleor/graphql/app/tests/queries/test_app_extensions.py:74]
- `test_app_extensions_app_removed_app` (function) — [saleor/graphql/app/tests/queries/test_app_extensions.py:103]
- `test_app_extensions_user_not_staff` (function) — [saleor/graphql/app/tests/queries/test_app_extensions.py:130]
- `test_app_extensions_with_filter` (function) — [saleor/graphql/app/tests/queries/test_app_extensions.py:182]
- `test_app_extensions_with_name_filter` (function) — [saleor/graphql/app/tests/queries/test_app_extensions.py:293]
- `test_app_extensions_case_insensitive_filter` (function) — [saleor/graphql/app/tests/queries/test_app_extensions.py:385]

**`saleor/graphql/app/tests/queries/test_app_problems.py`**

- `test_app_problems_empty` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:96]
- `test_app_problems_returns_problems` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:109]
- `test_app_problems_ordered_by_created_at_desc` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:135]
- `test_app_problems_count_and_critical` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:156]
- `test_app_problems_dismissed_null_when_not_dismissed` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:183]
- `test_app_problems_dismissed_by_app` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:200]
- `test_app_problems_dismissed_by_user` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:223]
- `test_app_problems_dismissed_by_user_returns_null_when_user_deleted` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:254]
- `test_app_cannot_see_dismissed_user_email` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:288]
- `test_authenticated_user_can_see_dismissed_user_email` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:314]
- `test_app_without_manage_staff_cannot_see_dismissed_user_email` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:342]
- `test_app_can_see_dismissed_by_when_dismissed_by_app` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:371]
- `test_authenticated_user_can_see_dismissed_by_when_dismissed_by_app` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:394]
- `test_by_field_accessible_to_app_when_dismissed_by_user` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:423]
- `test_user_with_manage_staff_can_see_dismissed_user` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:449]
- `test_user_without_manage_staff_cannot_see_dismissed_user` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:479]
- `test_app_cannot_see_dismissed_user` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:505]
- `test_dismissed_user_returns_null_when_dismissed_by_app` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:531]
- `test_dismissed_user_returns_null_when_user_deleted` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:558]
- `test_app_problems_limit_negative` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:588]
- `test_app_problems_limit_zero` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:605]
- `test_app_problems_limit_one` (function) — [saleor/graphql/app/tests/queries/test_app_problems.py:622]

**`saleor/graphql/app/tests/queries/test_app.py`**

- `test_app_query` (function) — [saleor/graphql/app/tests/queries/test_app.py:82]
- `test_app_query_no_permission` (function) — [saleor/graphql/app/tests/queries/test_app.py:147]
- `test_app_with_access_to_resources` (function) — [saleor/graphql/app/tests/queries/test_app.py:165]
- `test_app_without_id_as_staff` (function) — [saleor/graphql/app/tests/queries/test_app.py:190]
- `test_own_app_without_id` (function) — [saleor/graphql/app/tests/queries/test_app.py:203]
- `test_own_app_without_id_as_removed_app` (function) — [saleor/graphql/app/tests/queries/test_app.py:245]
- `test_app_query_without_permission` (function) — [saleor/graphql/app/tests/queries/test_app.py:260]
- `test_app_query_without_permission_and_id` (function) — [saleor/graphql/app/tests/queries/test_app.py:280]
- `test_app_with_extensions_query` (function) — [saleor/graphql/app/tests/queries/test_app.py:296]
- `test_app_query_pending_installation` (function) — [saleor/graphql/app/tests/queries/test_app.py:329]
- `test_app_query_app_marked_as_removed` (function) — [saleor/graphql/app/tests/queries/test_app.py:344]
- `test_app_query_for_staff_without_manage_apps` (function) — [saleor/graphql/app/tests/queries/test_app.py:409]
- `test_app_query_access_token_with_audience` (function) — [saleor/graphql/app/tests/queries/test_app.py:454]
- `test_app_query_access_token_errors_when_app_has_manage_apps` (function) — [saleor/graphql/app/tests/queries/test_app.py:484]
- `test_app_query_logo_thumbnail_with_size_and_format_url_returned` (function) — [saleor/graphql/app/tests/queries/test_app.py:526]
- `test_app_query_logo_thumbnail_with_zero_size_value_original_image_url_returned` (function) — [saleor/graphql/app/tests/queries/test_app.py:571]
- `test_app_query_for_normal_user` (function) — [saleor/graphql/app/tests/queries/test_app.py:591]
- `test_app_query_with_metadata_staff_user_without_permissions` (function) — [saleor/graphql/app/tests/queries/test_app.py:617]
- `test_app_query_with_metafield_staff_user_without_permissions` (function) — [saleor/graphql/app/tests/queries/test_app.py:647]
- `test_app_query_with_metafields_staff_user_without_permissions` (function) — [saleor/graphql/app/tests/queries/test_app.py:677]
- `test_app_query_breaker_state` (function) — [saleor/graphql/app/tests/queries/test_app.py:708]
- `test_app_query_breaker_state_board_disabled` (function) — [saleor/graphql/app/tests/queries/test_app.py:735]
- `test_app_query_breaker_last_change_board_disabled` (function) — [saleor/graphql/app/tests/queries/test_app.py:756]
- `test_app_query_breaker_last_change` (function) — [saleor/graphql/app/tests/queries/test_app.py:779]

**`saleor/graphql/app/tests/queries/test_apps_installations.py`**

- `test_apps_installation` (function) — [saleor/graphql/app/tests/queries/test_apps_installations.py:17]
- `test_apps_installation_by_app` (function) — [saleor/graphql/app/tests/queries/test_apps_installations.py:29]
- `test_apps_installation_by_app_missing_permission` (function) — [saleor/graphql/app/tests/queries/test_apps_installations.py:43]
- `test_apps_installation_missing_permission` (function) — [saleor/graphql/app/tests/queries/test_apps_installations.py:48]
- `test_apps_installations_query_logo_thumbnail_with_size_and_format_url_returned` (function) — [saleor/graphql/app/tests/queries/test_apps_installations.py:76]
- `test_apps_installations_query_logo_thumbnail_original_image_url_returned` (function) — [saleor/graphql/app/tests/queries/test_apps_installations.py:124]

**`saleor/graphql/app/tests/queries/test_apps_pagination.py`**

- `apps_for_pagination` (function) — [saleor/graphql/app/tests/queries/test_apps_pagination.py:8]
- `test_apps_pagination_with_sorting` (function) — [saleor/graphql/app/tests/queries/test_apps_pagination.py:56]
- `test_apps_pagination_with_filtering` (function) — [saleor/graphql/app/tests/queries/test_apps_pagination.py:87]

**`saleor/graphql/app/tests/queries/test_apps.py`**

- `test_apps_query` (function) — [saleor/graphql/app/tests/queries/test_apps.py:71]
- `test_apps_with_extensions_query` (function) — [saleor/graphql/app/tests/queries/test_apps.py:110]
- `test_apps_query_no_permission` (function) — [saleor/graphql/app/tests/queries/test_apps.py:150]
- `test_apps_query_marked_as_removed` (function) — [saleor/graphql/app/tests/queries/test_apps.py:167]
- `test_query_apps_with_sort` (function) — [saleor/graphql/app/tests/queries/test_apps.py:209]
- `test_apps_query_pending_installation` (function) — [saleor/graphql/app/tests/queries/test_apps.py:242]
- `test_query_app_for_federation` (function) — [saleor/graphql/app/tests/queries/test_apps.py:268]
- `test_query_app_for_federation_without_permission` (function) — [saleor/graphql/app/tests/queries/test_apps.py:295]
- `test_apps_query_staff_without_permissions` (function) — [saleor/graphql/app/tests/queries/test_apps.py:350]
- `test_apps_query_for_normal_user` (function) — [saleor/graphql/app/tests/queries/test_apps.py:377]
- `test_apps_query_access_token_errors_when_app_has_manage_apps` (function) — [saleor/graphql/app/tests/queries/test_apps.py:390]
- `test_apps_query_with_metadata_staff_user_without_permissions` (function) — [saleor/graphql/app/tests/queries/test_apps.py:444]
- `test_apps_query_with_metafield_staff_user_without_permissions` (function) — [saleor/graphql/app/tests/queries/test_apps.py:477]
- `test_apps_query_with_metafields_staff_user_without_permissions` (function) — [saleor/graphql/app/tests/queries/test_apps.py:510]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/app/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/app/tests/queries/test_app_extension.py` (724 lines)
- `saleor/graphql/app/tests/queries/test_app_extensions.py` (414 lines)
- `saleor/graphql/app/tests/queries/test_app_problems.py` (639 lines)
- `saleor/graphql/app/tests/queries/test_app.py` (811 lines)
- `saleor/graphql/app/tests/queries/test_apps_installations.py` (150 lines)
- `saleor/graphql/app/tests/queries/test_apps_pagination.py` (106 lines)
- `saleor/graphql/app/tests/queries/test_apps.py` (526 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....app.models.App`
- `.....app.models.AppExtension`
- `.....app.models.AppProblem`
- `.....app.types.AppType`
- `.....core.jwt.create_access_token_for_app`
- `.....core.jwt.jwt_decode`
- `.....thumbnail.IconThumbnailFormat`
- `.....thumbnail.models.Thumbnail`
- `.....webhook.models.Webhook`
- `....app.enums.CircuitBreakerState`
- `....app.enums.CircuitBreakerStateEnum`
- `....tests.fixtures.ApiClient`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `....tests.utils.get_graphql_content_from_response`
- `...enums.AppTypeEnum`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `6b8ef04f4a5d` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
