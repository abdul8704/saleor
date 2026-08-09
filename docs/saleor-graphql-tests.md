## Purpose

`saleor/graphql/tests` (`saleor/graphql/tests`) groups 13 source file(s) exposing 99 top-level declaration(s).

## Public surface

**`saleor/graphql/tests/fixtures.py`**

- `BaseApiClient` (class) — [saleor/graphql/tests/fixtures.py:24]
- `regenerate_access_token` (function) — [saleor/graphql/tests/fixtures.py:53]
- `ensure_access_token` (function) — [saleor/graphql/tests/fixtures.py:59]
- `user` (function) — [saleor/graphql/tests/fixtures.py:64]
- `user` (function) — [saleor/graphql/tests/fixtures.py:68]
- `post` (function) — [saleor/graphql/tests/fixtures.py:72]
- `ApiClient` (class) — [saleor/graphql/tests/fixtures.py:85]
- `post_graphql` (function) — [saleor/graphql/tests/fixtures.py:86]
- `post_multipart` (function) — [saleor/graphql/tests/fixtures.py:121]
- `app_api_client` (function) — [saleor/graphql/tests/fixtures.py:139]
- `staff_api_client` (function) — [saleor/graphql/tests/fixtures.py:144]
- `superuser_api_client` (function) — [saleor/graphql/tests/fixtures.py:149]
- `user_api_client` (function) — [saleor/graphql/tests/fixtures.py:154]
- `user2_api_client` (function) — [saleor/graphql/tests/fixtures.py:159]
- `api_client` (function) — [saleor/graphql/tests/fixtures.py:164]
- `schema_context` (function) — [saleor/graphql/tests/fixtures.py:169]
- `info` (function) — [saleor/graphql/tests/fixtures.py:180]
- `anonymous_plugins` (function) — [saleor/graphql/tests/fixtures.py:185]
- `LoggingHandler` (class) — [saleor/graphql/tests/fixtures.py:189]
- `emit` (function) — [saleor/graphql/tests/fixtures.py:194]
- `graphql_log_handler` (function) — [saleor/graphql/tests/fixtures.py:202]
- `superuser` (function) — [saleor/graphql/tests/fixtures.py:212]
- `user_list` (function) — [saleor/graphql/tests/fixtures.py:224]
- `user_list_not_active` (function) — [saleor/graphql/tests/fixtures.py:237]

**`saleor/graphql/tests/test_context.py`**

- `test_user_is_cached_on_request` (function) — [saleor/graphql/tests/test_context.py:26]
- `test_get_context_value_not_override_dataloaders_if_passed_already` (function) — [saleor/graphql/tests/test_context.py:49]
- `test_get_context_value_uses_request_time_if_passed_already` (function) — [saleor/graphql/tests/test_context.py:64]
- `test_clear_context` (function) — [saleor/graphql/tests/test_context.py:77]

**`saleor/graphql/tests/test_decorators.py`**

- `test_permission_required_with_limited_permissions` (function) — [saleor/graphql/tests/test_decorators.py:40]
- `test_permission_required` (function) — [saleor/graphql/tests/test_decorators.py:78]

**`saleor/graphql/tests/test_error.py`**

- `SampleModel` (class) — [saleor/graphql/tests/test_error.py:11]
- `ModelWithCustomErrorCode` (class) — [saleor/graphql/tests/test_error.py:16]
- `validate_url` (function) — [saleor/graphql/tests/test_error.py:21]
- `test_pydantic_to_validation_error_single_field` (function) — [saleor/graphql/tests/test_error.py:31]
- `test_pydantic_to_validation_error_multiple_fields` (function) — [saleor/graphql/tests/test_error.py:46]
- `test_pydantic_to_validation_error_uses_default_error_code` (function) — [saleor/graphql/tests/test_error.py:63]
- `test_pydantic_to_validation_error_uses_custom_error_code` (function) — [saleor/graphql/tests/test_error.py:78]
- `test_pydantic_to_validation_error_per_error_code_overrides_global` (function) — [saleor/graphql/tests/test_error.py:95]
- `test_pydantic_to_validation_error_falls_back_to_global_when_no_ctx_code` (function) — [saleor/graphql/tests/test_error.py:109]

**`saleor/graphql/tests/test_metrics.py`**

- `test_record_field_usage_with_deprecated_field` (function) — [saleor/graphql/tests/test_metrics.py:28]
- `test_record_field_usage_explicit` (function) — [saleor/graphql/tests/test_metrics.py:45]
- `test_record_graphql_query_count` (function) — [saleor/graphql/tests/test_metrics.py:64]
- `test_record_graphql_query_duration` (function) — [saleor/graphql/tests/test_metrics.py:76]
- `test_record_graphql_query_duration_with_slow_query` (function) — [saleor/graphql/tests/test_metrics.py:104]
- `test_graphql_query_record_metrics` (function) — [saleor/graphql/tests/test_metrics.py:141]
- `test_graphql_query_record_metrics_invalid_query` (function) — [saleor/graphql/tests/test_metrics.py:221]
- `test_graphql_query_record_metrics_cost_exceeded` (function) — [saleor/graphql/tests/test_metrics.py:283]
- `test_graphql_view_record_http_metrics` (function) — [saleor/graphql/tests/test_metrics.py:355]
- `test_graphql_view_record_http_metrics_error_type` (function) — [saleor/graphql/tests/test_metrics.py:394]

**`saleor/graphql/tests/test_middleware.py`**

- `test_middleware_invalid_name` (function) — [saleor/graphql/tests/test_middleware.py:6]

**`saleor/graphql/tests/test_storefront_traffic.py`**

- `test_blocks_anonymous_request_when_disabled` (function) — [saleor/graphql/tests/test_storefront_traffic.py:36]
- `test_allows_anonymous_request_when_enabled` (function) — [saleor/graphql/tests/test_storefront_traffic.py:45]
- `test_allows_app_request_when_disabled` (function) — [saleor/graphql/tests/test_storefront_traffic.py:54]
- `test_user_traffic` (function) — [saleor/graphql/tests/test_storefront_traffic.py:72]
- `test_invalid_token_user_resolution` (function) — [saleor/graphql/tests/test_storefront_traffic.py:97]
- `Request` (class) — [saleor/graphql/tests/test_storefront_traffic.py:108]
- `user` (function) — [saleor/graphql/tests/test_storefront_traffic.py:113]
- `test_unexpected_user_object_is_not_privileged` (function) — [saleor/graphql/tests/test_storefront_traffic.py:127]

**`saleor/graphql/tests/test_tracing.py`**

- `test_tracing_query_hashing` (function) — [saleor/graphql/tests/test_tracing.py:19]
- `test_tracing_query_hashing_with_fragment` (function) — [saleor/graphql/tests/test_tracing.py:53]
- `test_tracing_query_hashing_different_vars_same_checksum` (function) — [saleor/graphql/tests/test_tracing.py:93]
- `test_tracing_query_hashing_unnamed_query` (function) — [saleor/graphql/tests/test_tracing.py:127]
- `test_tracing_query_hashing_unnamed_query_no_query_spec` (function) — [saleor/graphql/tests/test_tracing.py:161]
- `test_tracing_mutation_hashing` (function) — [saleor/graphql/tests/test_tracing.py:195]
- `test_tracing_query_identifier_for_query` (function) — [saleor/graphql/tests/test_tracing.py:238]
- `test_tracing_query_identifier_with_fragment` (function) — [saleor/graphql/tests/test_tracing.py:278]
- `test_tracing_query_identifier_for_unnamed_mutation` (function) — [saleor/graphql/tests/test_tracing.py:312]
- `test_tracing_query_identifier_for_named_mutation` (function) — [saleor/graphql/tests/test_tracing.py:337]
- `test_tracing_query_identifier_for_many_mutations` (function) — [saleor/graphql/tests/test_tracing.py:361]
- `test_tracing_query_identifier_undefined` (function) — [saleor/graphql/tests/test_tracing.py:396]
- `test_tracing_dont_have_app_data_staff_as_requestor` (function) — [saleor/graphql/tests/test_tracing.py:419]
- `test_tracing_have_app_data_app_as_requestor` (function) — [saleor/graphql/tests/test_tracing.py:448]
- `test_tracing_have_source_service_name_set` (function) — [saleor/graphql/tests/test_tracing.py:492]
- `test_graphql_query_span_set_status_error_invalid_query` (function) — [saleor/graphql/tests/test_tracing.py:546]
- `test_graphql_query_span_set_status_error_cost_exceeded` (function) — [saleor/graphql/tests/test_tracing.py:574]
- `test_trace_context_propagation` (function) — [saleor/graphql/tests/test_tracing.py:615]
- `test_trace_context_propagation_in_sync_webhook` (function) — [saleor/graphql/tests/test_tracing.py:657]

**`saleor/graphql/tests/test_utils.py`**

- `test_multiple_interface_separator_in_schema` (function) — [saleor/graphql/tests/test_utils.py:19]
- `test_graphql_core_contains_patched_function` (function) — [saleor/graphql/tests/test_utils.py:37]
- `test_format_error_hides_internal_error_msg_in_production_mode` (function) — [saleor/graphql/tests/test_utils.py:42]
- `test_format_error_prints_allowed_errors` (function) — [saleor/graphql/tests/test_utils.py:49]
- `test_format_error_prints_internal_error_msg_in_debug_mode` (function) — [saleor/graphql/tests/test_utils.py:57]
- `test_check_if_query_contains_only_schema_with_schema_query` (function) — [saleor/graphql/tests/test_utils.py:63]
- `test_check_if_query_contains_only_schema_with_mixed_query` (function) — [saleor/graphql/tests/test_utils.py:81]
- `test_check_if_query_contains_only_schema_with_mixed_query_and_fragments` (function) — [saleor/graphql/tests/test_utils.py:100]
- `test_check_if_query_contains_only_schema_with_fragments` (function) — [saleor/graphql/tests/test_utils.py:123]
- `test_check_if_query_contains_only_schema_with_schema_query_and_inline_fragment` (function) — [saleor/graphql/tests/test_utils.py:147]
- `test_check_if_query_contains_only_schema_with_schema_query_and_unconditional_inline_fragment` (function) — [saleor/graphql/tests/test_utils.py:167]
- `test_check_if_query_contains_only_schema_with_schema_query_and_named_fragment` (function) — [saleor/graphql/tests/test_utils.py:187]
- `test_check_if_query_contains_only_schema_with_schema_query_and_fragments` (function) — [saleor/graphql/tests/test_utils.py:209]
- `test_check_if_query_contains_only_schema_with_introspection` (function) — [saleor/graphql/tests/test_utils.py:233]
- `test_get_source_service_name_value` (function) — [saleor/graphql/tests/test_utils.py:353]

**`saleor/graphql/tests/utils.py`**

- `get_graphql_content_from_response` (function) — [saleor/graphql/tests/utils.py:6]
- `get_graphql_content` (function) — [saleor/graphql/tests/utils.py:10]
- `assert_no_permission` (function) — [saleor/graphql/tests/utils.py:22]
- `assert_negative_positive_decimal_value` (function) — [saleor/graphql/tests/utils.py:30]
- `assert_graphql_error_with_message` (function) — [saleor/graphql/tests/utils.py:38]
- `get_multipart_request_body` (function) — [saleor/graphql/tests/utils.py:44]
- `get_multipart_request_body_with_multiple_files` (function) — [saleor/graphql/tests/utils.py:59]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/tests/utils.py` (72 lines)
- `saleor/graphql/tests/__init__.py` (1 lines)
- `saleor/graphql/tests/fixtures.py` (240 lines)
- `saleor/graphql/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/tests/queries/fragments.py` (577 lines)
- `saleor/graphql/tests/test_context.py` (86 lines)
- `saleor/graphql/tests/test_decorators.py` (93 lines)
- `saleor/graphql/tests/test_error.py` (121 lines)
- `saleor/graphql/tests/test_metrics.py` (427 lines)
- `saleor/graphql/tests/test_middleware.py` (8 lines)
- `saleor/graphql/tests/test_storefront_traffic.py` (134 lines)
- `saleor/graphql/tests/test_tracing.py` (724 lines)
- `saleor/graphql/tests/test_utils.py` (358 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/webhook`, `saleor/plugins/openid_connect`, `saleor/graphql`, `saleor/core/telemetry`
- Imported by: `saleor/tests/e2e/orders/utils`, `saleor/graphql/checkout/tests/deprecated`, `saleor/tests/e2e/checkout/utils`

Internal dependencies named in the source:

- `...account.models.User`
- `...account.tests.fixtures.user.dangerously_create_test_user`
- `...core.jwt.create_access_token`
- `...core.telemetry.DEFAULT_DURATION_BUCKETS`
- `...core.telemetry.Scope`
- `...core.telemetry.Unit`
- `...core.telemetry.saleor_attributes`
- `...graphql.api.backend`
- `...graphql.api.schema`
- `...permission.models.Permission`
- `...permission.utils.permission_required`
- `...plugins.manager.get_plugins_manager`
- `...tests.utils.filter_spans_by_name`
- `...tests.utils.get_metric_and_data_point`
- `...tests.utils.get_metric_data`
- `...tests.utils.get_span_by_name`
- `..api.backend`
- `..api.schema`
- `..context.clear_context`
- `..context.get_context_value`
- `..core.dataloaders.DataLoader`
- `..error.pydantic_to_validation_error`
- `..utils.get_user_or_app_from_context`
- `..utils.handled_errors_logger`
- `..utils.unhandled_errors_logger`
- `..utils.validators.check_if_query_contains_only_schema`
- `..views.GraphQLView`
- `.utils.assert_no_permission`
- `.utils.get_graphql_content`
- `saleor.core.auth.SALEOR_AUTH_HEADER`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `96e323315fd6` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
