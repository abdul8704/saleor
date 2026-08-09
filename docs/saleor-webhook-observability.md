## Purpose

`saleor/webhook/observability` (`saleor/webhook/observability`) groups 9 source file(s) exposing 85 top-level declaration(s).

## Public surface

**`saleor/webhook/observability/buffers.py`**

- `BaseBuffer` (class) — [saleor/webhook/observability/buffers.py:15]
- `decode` (function) — [saleor/webhook/observability/buffers.py:34]
- `encode` (function) — [saleor/webhook/observability/buffers.py:37]
- `put_event` (function) — [saleor/webhook/observability/buffers.py:40]
- `put_events` (function) — [saleor/webhook/observability/buffers.py:45]
- `put_multi_key_events` (function) — [saleor/webhook/observability/buffers.py:50]
- `pop_event` (function) — [saleor/webhook/observability/buffers.py:57]
- `pop_events` (function) — [saleor/webhook/observability/buffers.py:62]
- `pop_events_get_size` (function) — [saleor/webhook/observability/buffers.py:67]
- `clear` (function) — [saleor/webhook/observability/buffers.py:72]
- `size` (function) — [saleor/webhook/observability/buffers.py:77]
- `in_batches` (function) — [saleor/webhook/observability/buffers.py:82]
- `RedisBuffer` (class) — [saleor/webhook/observability/buffers.py:86]
- `get_connection_pool` (function) — [saleor/webhook/observability/buffers.py:95]
- `get_or_create_connection_pool` (function) — [saleor/webhook/observability/buffers.py:103]
- `connect` (function) — [saleor/webhook/observability/buffers.py:108]
- `client` (function) — [saleor/webhook/observability/buffers.py:113]
- `put_events` (function) — [saleor/webhook/observability/buffers.py:130]
- `put_event` (function) — [saleor/webhook/observability/buffers.py:136]
- `put_multi_key_events` (function) — [saleor/webhook/observability/buffers.py:139]
- `pop_event` (function) — [saleor/webhook/observability/buffers.py:169]
- `pop_events` (function) — [saleor/webhook/observability/buffers.py:173]
- `pop_events_get_size` (function) — [saleor/webhook/observability/buffers.py:177]
- `clear` (function) — [saleor/webhook/observability/buffers.py:180]
- `size` (function) — [saleor/webhook/observability/buffers.py:187]
- `get_buffer` (function) — [saleor/webhook/observability/buffers.py:191]

**`saleor/webhook/observability/exceptions.py`**

- `ObservabilityError` (class) — [saleor/webhook/observability/exceptions.py:4]
- `ConnectionNotConfigured` (class) — [saleor/webhook/observability/exceptions.py:8]
- `TruncationError` (class) — [saleor/webhook/observability/exceptions.py:12]
- `ApiCallTruncationError` (class) — [saleor/webhook/observability/exceptions.py:32]
- `EventDeliveryAttemptTruncationError` (class) — [saleor/webhook/observability/exceptions.py:36]

**`saleor/webhook/observability/obfuscation.py`**

- `filter_and_hide_headers` (function) — [saleor/webhook/observability/obfuscation.py:36]
- `SensitiveFieldError` (class) — [saleor/webhook/observability/obfuscation.py:52]
- `ContainSensitiveField` (class) — [saleor/webhook/observability/obfuscation.py:56]
- `is_sensitive_field` (function) — [saleor/webhook/observability/obfuscation.py:64]
- `contain_sensitive_field` (function) — [saleor/webhook/observability/obfuscation.py:73]
- `enter_operation_definition` (function) — [saleor/webhook/observability/obfuscation.py:104]
- `enter` (function) — [saleor/webhook/observability/obfuscation.py:119]
- `validate_sensitive_fields_map` (function) — [saleor/webhook/observability/obfuscation.py:131]
- `anonymize_gql_operation_response` (function) — [saleor/webhook/observability/obfuscation.py:182]
- `anonymize_event_payload` (function) — [saleor/webhook/observability/obfuscation.py:191]

**`saleor/webhook/observability/payload_schema.py`**

- `JsonTruncText` (class) — [saleor/webhook/observability/payload_schema.py:7]
- `byte_size` (function) — [saleor/webhook/observability/payload_schema.py:22]
- `json_char_len` (function) — [saleor/webhook/observability/payload_schema.py:26]
- `truncate` (function) — [saleor/webhook/observability/payload_schema.py:33]
- `ObservabilityEventTypes` (class) — [saleor/webhook/observability/payload_schema.py:63]
- `App` (class) — [saleor/webhook/observability/payload_schema.py:71]
- `Webhook` (class) — [saleor/webhook/observability/payload_schema.py:76]
- `ObservabilityEventBase` (class) — [saleor/webhook/observability/payload_schema.py:83]
- `GraphQLOperation` (class) — [saleor/webhook/observability/payload_schema.py:87]
- `ApiCallRequest` (class) — [saleor/webhook/observability/payload_schema.py:95]
- `ApiCallResponse` (class) — [saleor/webhook/observability/payload_schema.py:104]
- `ApiCallPayload` (class) — [saleor/webhook/observability/payload_schema.py:110]
- `EventDeliveryPayload` (class) — [saleor/webhook/observability/payload_schema.py:117]
- `EventDelivery` (class) — [saleor/webhook/observability/payload_schema.py:122]
- `EventDeliveryAttemptRequest` (class) — [saleor/webhook/observability/payload_schema.py:130]
- `EventDeliveryAttemptResponse` (class) — [saleor/webhook/observability/payload_schema.py:134]
- `EventDeliveryAttemptPayload` (class) — [saleor/webhook/observability/payload_schema.py:141]

**`saleor/webhook/observability/payloads.py`**

- `CustomJsonEncoder` (class) — [saleor/webhook/observability/payloads.py:47]
- `default` (function) — [saleor/webhook/observability/payloads.py:48]
- `to_camel_case` (function) — [saleor/webhook/observability/payloads.py:54]
- `pretty_json` (function) — [saleor/webhook/observability/payloads.py:65]
- `dump_payload` (function) — [saleor/webhook/observability/payloads.py:69]
- `concatenate_json_events` (function) — [saleor/webhook/observability/payloads.py:75]
- `serialize_headers` (function) — [saleor/webhook/observability/payloads.py:91]
- `serialize_gql_operation_result` (function) — [saleor/webhook/observability/payloads.py:97]
- `serialize_gql_operation_results` (function) — [saleor/webhook/observability/payloads.py:132]
- `generate_api_call_payload` (function) — [saleor/webhook/observability/payloads.py:153]
- `generate_event_delivery_attempt_payload` (function) — [saleor/webhook/observability/payloads.py:194]

**`saleor/webhook/observability/tracing.py`**

- `otel_trace` (function) — [saleor/webhook/observability/tracing.py:7]

**`saleor/webhook/observability/utils.py`**

- `WebhookData` (class) — [saleor/webhook/observability/utils.py:41]
- `get_buffer_name` (function) — [saleor/webhook/observability/utils.py:48]
- `get_webhooks_clear_mem_cache` (function) — [saleor/webhook/observability/utils.py:55]
- `get_webhooks` (function) — [saleor/webhook/observability/utils.py:59]
- `task_next_retry_date` (function) — [saleor/webhook/observability/utils.py:85]
- `put_event` (function) — [saleor/webhook/observability/utils.py:93]
- `pop_events_with_remaining_size` (function) — [saleor/webhook/observability/utils.py:105]
- `GraphQLOperationResponse` (class) — [saleor/webhook/observability/utils.py:118]
- `ApiCall` (class) — [saleor/webhook/observability/utils.py:126]
- `report` (function) — [saleor/webhook/observability/utils.py:133]
- `report_api_call` (function) — [saleor/webhook/observability/utils.py:157]
- `report_gql_operation` (function) — [saleor/webhook/observability/utils.py:168]
- `report_view` (function) — [saleor/webhook/observability/utils.py:179]
- `wrapper` (function) — [saleor/webhook/observability/utils.py:181]
- `report_event_delivery_attempt` (function) — [saleor/webhook/observability/utils.py:190]

## How it works

The module's files, as provided to this run:

- `saleor/webhook/observability/__init__.py` (32 lines)
- `saleor/webhook/observability/buffers.py` (207 lines)
- `saleor/webhook/observability/exceptions.py` (37 lines)
- `saleor/webhook/observability/obfuscation.py` (206 lines)
- `saleor/webhook/observability/payload_schema.py` (151 lines)
- `saleor/webhook/observability/payloads.py` (275 lines)
- `saleor/webhook/observability/sensitive_data.py` (64 lines)
- `saleor/webhook/observability/tracing.py` (10 lines)
- `saleor/webhook/observability/utils.py` (208 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/webhook`, `saleor/plugins/openid_connect`, `saleor/core/utils`, `saleor/core`
- Imported by: `saleor/webhook/observability/tests`

Internal dependencies named in the source:

- `...app.headers.AppHeaders`
- `...app.headers.DeprecatedAppHeaders`
- `...core.models.EventDeliveryAttempt`
- `...core.telemetry.saleor_attributes`
- `...core.telemetry.tracer`
- `...core.utils.build_absolute_uri`
- `...core.utils.get_domain`
- `...core.utils.url.sanitize_url_for_logging`
- `...graphql.api.schema`
- `...traced_payload_generator`
- `..event_types.WebhookEventAsyncType`
- `..event_types.WebhookEventSyncType`
- `..utils.get_webhooks_for_event`
- `.buffers.get_buffer`
- `.exceptions.ApiCallTruncationError`
- `.exceptions.ConnectionNotConfigured`
- `.exceptions.EventDeliveryAttemptTruncationError`
- `.exceptions.ObservabilityError`
- `.exceptions.TruncationError`
- `.payload_schema.ObservabilityEventTypes`
- `.payloads.concatenate_json_events`
- `.payloads.dump_payload`
- `.payloads.generate_api_call_payload`
- `.payloads.generate_event_delivery_attempt_payload`
- `.sensitive_data.ALLOWED_HEADERS`
- `.sensitive_data.SENSITIVE_GQL_FIELDS`
- `.sensitive_data.SENSITIVE_HEADERS`
- `.sensitive_data.SensitiveFieldsMap`
- `.tracing.otel_trace`
- `.utils.GraphQLOperationResponse`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c60a153c1e34` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
