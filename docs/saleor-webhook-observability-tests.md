## Purpose

`saleor/webhook/observability/tests` (`saleor/webhook/observability/tests`) groups 7 source file(s) exposing 83 top-level declaration(s).

## Public surface

**`saleor/webhook/observability/tests/conftest.py`**

- `gql_operation_factory` (function) — [saleor/webhook/observability/tests/conftest.py:22]
- `factory` (function) — [saleor/webhook/observability/tests/conftest.py:23]
- `redis_server` (function) — [saleor/webhook/observability/tests/conftest.py:49]
- `patch_connection_pool` (function) — [saleor/webhook/observability/tests/conftest.py:59]
- `buffer` (function) — [saleor/webhook/observability/tests/conftest.py:72]
- `event_data` (function) — [saleor/webhook/observability/tests/conftest.py:78]

**`saleor/webhook/observability/tests/test_buffer.py`**

- `test_get_buffer` (function) — [saleor/webhook/observability/tests/test_buffer.py:12]
- `test_get_buffer_with_no_config` (function) — [saleor/webhook/observability/tests/test_buffer.py:19]
- `test_get_connection_pool` (function) — [saleor/webhook/observability/tests/test_buffer.py:25]
- `test_get_or_create_connection_pool` (function) — [saleor/webhook/observability/tests/test_buffer.py:36]
- `test_in_batches` (function) — [saleor/webhook/observability/tests/test_buffer.py:43]
- `test_put_event` (function) — [saleor/webhook/observability/tests/test_buffer.py:47]
- `test_buffer_put_events_max_size` (function) — [saleor/webhook/observability/tests/test_buffer.py:53]
- `test_put_events` (function) — [saleor/webhook/observability/tests/test_buffer.py:59]
- `test_put_events_max_size` (function) — [saleor/webhook/observability/tests/test_buffer.py:66]
- `test_buffer_drops_events_when_put_events` (function) — [saleor/webhook/observability/tests/test_buffer.py:73]
- `test_put_multi_key_events` (function) — [saleor/webhook/observability/tests/test_buffer.py:81]
- `test_put_multi_key_events_when_buffer_full` (function) — [saleor/webhook/observability/tests/test_buffer.py:99]
- `test_pop_event` (function) — [saleor/webhook/observability/tests/test_buffer.py:115]
- `test_pop_events` (function) — [saleor/webhook/observability/tests/test_buffer.py:124]
- `test_pop_events_get_size` (function) — [saleor/webhook/observability/tests/test_buffer.py:133]
- `test_clear` (function) — [saleor/webhook/observability/tests/test_buffer.py:143]
- `test_pop_expired_events` (function) — [saleor/webhook/observability/tests/test_buffer.py:151]

**`saleor/webhook/observability/tests/test_obfuscation.py`**

- `test_filter_and_hide_headers` (function) — [saleor/webhook/observability/tests/test_obfuscation.py:34]
- `test_anonymize_gql_operation_response` (function) — [saleor/webhook/observability/tests/test_obfuscation.py:41]
- `test_anonymize_gql_operation_with_mutation_in_query` (function) — [saleor/webhook/observability/tests/test_obfuscation.py:52]
- `test_anonymize_gql_operation_with_subscription_in_query` (function) — [saleor/webhook/observability/tests/test_obfuscation.py:68]
- `test_anonymize_gql_operation_response_with_empty_sensitive_fields_map` (function) — [saleor/webhook/observability/tests/test_obfuscation.py:90]
- `test_anonymize_gql_operation_response_with_fragment_spread` (function) — [saleor/webhook/observability/tests/test_obfuscation.py:102]
- `test_validate_sensitive_fields_map` (function) — [saleor/webhook/observability/tests/test_obfuscation.py:137]
- `test_anonymize_event_payload` (function) — [saleor/webhook/observability/tests/test_obfuscation.py:142]
- `test_anonymize_event_delivery_payload_when_empty_subscription_query` (function) — [saleor/webhook/observability/tests/test_obfuscation.py:163]

**`saleor/webhook/observability/tests/test_observability.py`**

- `test_observability_reporter_task` (function) — [saleor/webhook/observability/tests/test_observability.py:19]
- `test_observability_send_events` (function) — [saleor/webhook/observability/tests/test_observability.py:47]
- `test_send_observability_events` (function) — [saleor/webhook/observability/tests/test_observability.py:66]
- `test_send_observability_events_when_response_failed` (function) — [saleor/webhook/observability/tests/test_observability.py:85]
- `test_send_observability_events_to_google_pub_sub` (function) — [saleor/webhook/observability/tests/test_observability.py:100]
- `test_send_observability_events_to_google_pub_sub_when_response_failed` (function) — [saleor/webhook/observability/tests/test_observability.py:124]

**`saleor/webhook/observability/tests/test_payloads.py`**

- `test_to_camel_case` (function) — [saleor/webhook/observability/tests/test_payloads.py:77]
- `test_concatenate_json_events_with_one_event` (function) — [saleor/webhook/observability/tests/test_payloads.py:84]
- `test_serialize_gql_operation_result` (function) — [saleor/webhook/observability/tests/test_payloads.py:90]
- `test_serialize_gql_operation_result_when_no_operation_data` (function) — [saleor/webhook/observability/tests/test_payloads.py:106]
- `test_serialize_gql_operation_result_when_too_low_bytes_limit` (function) — [saleor/webhook/observability/tests/test_payloads.py:116]
- `test_serialize_gql_operation_result_when_minimal_bytes_limit` (function) — [saleor/webhook/observability/tests/test_payloads.py:122]
- `test_serialize_gql_operation_result_when_truncated` (function) — [saleor/webhook/observability/tests/test_payloads.py:141]
- `test_serialize_gql_operation_results` (function) — [saleor/webhook/observability/tests/test_payloads.py:159]
- `test_serialize_gql_operation_results_when_minimal_bytes_limit` (function) — [saleor/webhook/observability/tests/test_payloads.py:183]
- `test_serialize_gql_operation_results_when_too_low_bytes_limit` (function) — [saleor/webhook/observability/tests/test_payloads.py:212]
- `test_serialize_headers` (function) — [saleor/webhook/observability/tests/test_payloads.py:244]
- `test_generate_api_call_payload` (function) — [saleor/webhook/observability/tests/test_payloads.py:248]
- `test_generate_api_call_payload_request_not_from_app` (function) — [saleor/webhook/observability/tests/test_payloads.py:313]
- `test_generate_api_call_payload_skip_operations_when_size_limit_too_low` (function) — [saleor/webhook/observability/tests/test_payloads.py:324]
- `test_generate_api_call_payload_when_too_low_bytes_limit` (function) — [saleor/webhook/observability/tests/test_payloads.py:354]
- `test_generate_event_delivery_attempt_payload` (function) — [saleor/webhook/observability/tests/test_payloads.py:367]
- `test_generate_event_delivery_attempt_payload_raises_truncation_error` (function) — [saleor/webhook/observability/tests/test_payloads.py:418]
- `test_generate_event_delivery_attempt_payload_raises_error_when_no_delivery` (function) — [saleor/webhook/observability/tests/test_payloads.py:426]
- `test_generate_event_delivery_attempt_payload_raises_error_when_no_payload` (function) — [saleor/webhook/observability/tests/test_payloads.py:434]
- `test_generate_event_delivery_attempt_payload_with_next_retry_date` (function) — [saleor/webhook/observability/tests/test_payloads.py:442]
- `test_generate_event_delivery_attempt_payload_with_non_empty_headers` (function) — [saleor/webhook/observability/tests/test_payloads.py:453]
- `test_generate_event_delivery_attempt_payload_with_subscription_query` (function) — [saleor/webhook/observability/tests/test_payloads.py:469]
- `test_generate_event_delivery_attempt_payload_target_url_obfuscated` (function) — [saleor/webhook/observability/tests/test_payloads.py:483]

**`saleor/webhook/observability/tests/test_utils.py`**

- `api_call` (function) — [saleor/webhook/observability/tests/test_utils.py:28]
- `patch_get_buffer` (function) — [saleor/webhook/observability/tests/test_utils.py:35]
- `patch_get_webhooks` (function) — [saleor/webhook/observability/tests/test_utils.py:43]
- `test_request` (function) — [saleor/webhook/observability/tests/test_utils.py:52]
- `test_get_webhooks` (function) — [saleor/webhook/observability/tests/test_utils.py:70]
- `test_custom_json_encoder_dumps_json_trunc_text` (function) — [saleor/webhook/observability/tests/test_utils.py:90]
- `test_json_truncate_text_to_byte_limit` (function) — [saleor/webhook/observability/tests/test_utils.py:113]
- `test_json_truncate_text_comparison` (function) — [saleor/webhook/observability/tests/test_utils.py:123]
- `test_task_next_retry_date` (function) — [saleor/webhook/observability/tests/test_utils.py:145]
- `test_report_api_call_scope` (function) — [saleor/webhook/observability/tests/test_utils.py:150]
- `test_report_gql_operation_scope` (function) — [saleor/webhook/observability/tests/test_utils.py:163]
- `test_api_call_report` (function) — [saleor/webhook/observability/tests/test_utils.py:176]
- `test_api_call_response_report_when_observability_not_active` (function) — [saleor/webhook/observability/tests/test_utils.py:192]
- `test_api_call_response_report_when_request_not_from_app` (function) — [saleor/webhook/observability/tests/test_utils.py:205]
- `test_api_call_response_report_when_no_gql_response` (function) — [saleor/webhook/observability/tests/test_utils.py:218]
- `test_report_event_delivery_attempt` (function) — [saleor/webhook/observability/tests/test_utils.py:232]
- `test_report_event_delivery_attempt_not_active` (function) — [saleor/webhook/observability/tests/test_utils.py:243]
- `test_put_event` (function) — [saleor/webhook/observability/tests/test_utils.py:253]
- `test_put_event_catch_exceptions` (function) — [saleor/webhook/observability/tests/test_utils.py:268]
- `error_source` (function) — [saleor/webhook/observability/tests/test_utils.py:269]
- `test_pop_events_with_remaining_size` (function) — [saleor/webhook/observability/tests/test_utils.py:276]
- `test_pop_events_with_remaining_size_catch_exceptions` (function) — [saleor/webhook/observability/tests/test_utils.py:287]

## How it works

The module's files, as provided to this run:

- `saleor/webhook/observability/tests/__init__.py` (1 lines)
- `saleor/webhook/observability/tests/conftest.py` (79 lines)
- `saleor/webhook/observability/tests/test_buffer.py` (158 lines)
- `saleor/webhook/observability/tests/test_obfuscation.py` (169 lines)
- `saleor/webhook/observability/tests/test_observability.py` (136 lines)
- `saleor/webhook/observability/tests/test_payloads.py` (491 lines)
- `saleor/webhook/observability/tests/test_utils.py` (292 lines)

## Interactions

- Imports from: `saleor/core/utils`, `saleor/webhook/observability`, `saleor/webhook/transport/asynchronous`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....core.EventDeliveryStatus`
- `....graphql.api.schema`
- `....webhook.event_types.WebhookEventAsyncType`
- `...concatenate_json_events`
- `...event_types.WebhookEventAsyncType`
- `..buffers.RedisBuffer`
- `..buffers.get_buffer`
- `..exceptions.ApiCallTruncationError`
- `..exceptions.ConnectionNotConfigured`
- `..exceptions.EventDeliveryAttemptTruncationError`
- `..exceptions.TruncationError`
- `..obfuscation.MASK`
- `..payload_schema.JsonTruncText`
- `..payloads.CustomJsonEncoder`
- `..tests.conftest.BATCH_SIZE`
- `..tests.conftest.BROKER_URL_HOST`
- `..tests.conftest.KEY`
- `..tests.conftest.MAX_SIZE`
- `..utils.GraphQLOperationResponse`
- `..utils.get_buffer_name`
- `.conftest.BATCH_SIZE`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `654263020937` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
