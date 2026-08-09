## Purpose

`saleor/webhook/transport/asynchronous` (`saleor/webhook/transport/asynchronous`) groups 7 source file(s) exposing 52 top-level declaration(s).

## Public surface

**`saleor/webhook/transport/asynchronous/tests/test_create_deliveries_for_subscriptions.py`**

- `test_create_deliveries_different_pre_save_payloads` (function) — [saleor/webhook/transport/asynchronous/tests/test_create_deliveries_for_subscriptions.py:32]
- `test_skip_delivery_creation_no_payload_changes` (function) — [saleor/webhook/transport/asynchronous/tests/test_create_deliveries_for_subscriptions.py:62]
- `test_create_deliveries_no_payload_changes_limiting_disabled` (function) — [saleor/webhook/transport/asynchronous/tests/test_create_deliveries_for_subscriptions.py:88]
- `test_create_deliveries_reuse_request_for_webhooks` (function) — [saleor/webhook/transport/asynchronous/tests/test_create_deliveries_for_subscriptions.py:123]
- `test_create_deliveries_for_multiple_subscription_objects` (function) — [saleor/webhook/transport/asynchronous/tests/test_create_deliveries_for_subscriptions.py:166]
- `test_create_deliveries_for_multiple_subscription_objects_when_more_objs_than_bulk` (function) — [saleor/webhook/transport/asynchronous/tests/test_create_deliveries_for_subscriptions.py:193]

**`saleor/webhook/transport/asynchronous/tests/test_deferred_payload.py`**

- `fetch_kwargs` (function) — [saleor/webhook/transport/asynchronous/tests/test_deferred_payload.py:37]
- `test_call_trigger_webhook_async_deferred_payload` (function) — [saleor/webhook/transport/asynchronous/tests/test_deferred_payload.py:52]
- `test_generate_deferred_payload` (function) — [saleor/webhook/transport/asynchronous/tests/test_deferred_payload.py:93]
- `test_generate_deferred_payload_waits_for_replica_to_sync` (function) — [saleor/webhook/transport/asynchronous/tests/test_deferred_payload.py:158]
- `test_generate_deferred_payload_triggers_for_existing_deliveries` (function) — [saleor/webhook/transport/asynchronous/tests/test_deferred_payload.py:202]
- `test_generate_deferred_payload_model_pk_does_not_exist` (function) — [saleor/webhook/transport/asynchronous/tests/test_deferred_payload.py:266]
- `test_pass_queue_to_send_webhook_request_async` (function) — [saleor/webhook/transport/asynchronous/tests/test_deferred_payload.py:306]
- `test_call_trigger_webhook_async_deferred_payload_with_dataclass` (function) — [saleor/webhook/transport/asynchronous/tests/test_deferred_payload.py:349]
- `test_generate_deferred_payload_with_dataclass` (function) — [saleor/webhook/transport/asynchronous/tests/test_deferred_payload.py:411]
- `test_call_trigger_webhook_async_deferred_payload_with_variant_channel_stock_info` (function) — [saleor/webhook/transport/asynchronous/tests/test_deferred_payload.py:483]
- `test_generate_deferred_payload_with_variant_channel_stock_info` (function) — [saleor/webhook/transport/asynchronous/tests/test_deferred_payload.py:532]
- `test_reconstruct_subscribable_object_with_invalid_data` (function) — [saleor/webhook/transport/asynchronous/tests/test_deferred_payload.py:582]
- `test_reconstruct_subscribable_object_with_unregistered_event_type` (function) — [saleor/webhook/transport/asynchronous/tests/test_deferred_payload.py:597]

**`saleor/webhook/transport/asynchronous/tests/test_send_webhooks_async_for_app.py`**

- `test_send_webhooks_async_for_app` (function) — [saleor/webhook/transport/asynchronous/tests/test_send_webhooks_async_for_app.py:16]
- `test_send_webhooks_async_for_app_no_deliveries` (function) — [saleor/webhook/transport/asynchronous/tests/test_send_webhooks_async_for_app.py:44]
- `test_send_webhooks_async_for_app_doesnt_pick_failed` (function) — [saleor/webhook/transport/asynchronous/tests/test_send_webhooks_async_for_app.py:60]
- `test_send_webhooks_async_for_app_no_payload` (function) — [saleor/webhook/transport/asynchronous/tests/test_send_webhooks_async_for_app.py:81]
- `test_send_webhooks_async_for_app_failed_status` (function) — [saleor/webhook/transport/asynchronous/tests/test_send_webhooks_async_for_app.py:116]
- `test_send_multiple_webhooks_async_for_app` (function) — [saleor/webhook/transport/asynchronous/tests/test_send_webhooks_async_for_app.py:151]
- `test_send_webhooks_async_for_app_last_retry_failed` (function) — [saleor/webhook/transport/asynchronous/tests/test_send_webhooks_async_for_app.py:182]

**`saleor/webhook/transport/asynchronous/tests/test_transport.py`**

- `test_send_webhook_request_async_set_span_status_failed` (function) — [saleor/webhook/transport/asynchronous/tests/test_transport.py:24]
- `test_send_webhook_request_async_record_external_request` (function) — [saleor/webhook/transport/asynchronous/tests/test_transport.py:48]
- `test_send_webhook_request_async_record_external_request_when_delivery_attempt_failed` (function) — [saleor/webhook/transport/asynchronous/tests/test_transport.py:98]
- `test_send_webhook_request_async_record_external_request_with_unknown_webhook_scheme` (function) — [saleor/webhook/transport/asynchronous/tests/test_transport.py:149]
- `test_send_webhook_request_async_fails_when_exception_raised_by_webhooks_otel_trace` (function) — [saleor/webhook/transport/asynchronous/tests/test_transport.py:198]
- `test_send_webhook_request_async_when_google_cloud_pubsub_publish_fails` (function) — [saleor/webhook/transport/asynchronous/tests/test_transport.py:225]
- `test_send_webhook_request_async_when_aws_sqs_send_message_fails` (function) — [saleor/webhook/transport/asynchronous/tests/test_transport.py:275]

**`saleor/webhook/transport/asynchronous/transport.py`**

- `WebhookPayloadData` (class) — [saleor/webhook/transport/asynchronous/transport.py:79]
- `create_deliveries_for_multiple_subscription_objects` (function) — [saleor/webhook/transport/asynchronous/transport.py:85]
- `process_webhook_payloads` (function) — [saleor/webhook/transport/asynchronous/transport.py:150]
- `create_deliveries_for_subscriptions` (function) — [saleor/webhook/transport/asynchronous/transport.py:223]
- `create_deliveries_for_deferred_payload_subscriptions` (function) — [saleor/webhook/transport/asynchronous/transport.py:255]
- `group_webhooks_by_subscription` (function) — [saleor/webhook/transport/asynchronous/transport.py:290]
- `create_event_delivery_list_for_webhooks` (function) — [saleor/webhook/transport/asynchronous/transport.py:303]
- `get_queue_name_for_webhook` (function) — [saleor/webhook/transport/asynchronous/transport.py:322]
- `trigger_webhooks_async_for_multiple_objects` (function) — [saleor/webhook/transport/asynchronous/transport.py:332]
- `process_deliveries` (function) — [saleor/webhook/transport/asynchronous/transport.py:454]
- `trigger_webhooks_async` (function) — [saleor/webhook/transport/asynchronous/transport.py:477]
- `confirm_event_delivery_availability` (function) — [saleor/webhook/transport/asynchronous/transport.py:520]
- `generate_deferred_payloads` (function) — [saleor/webhook/transport/asynchronous/transport.py:541]
- `with_subscription_payload` (function) — [saleor/webhook/transport/asynchronous/transport.py:688]
- `send_webhook_request_async` (function) — [saleor/webhook/transport/asynchronous/transport.py:769]
- `send_webhooks_async_for_app` (function) — [saleor/webhook/transport/asynchronous/transport.py:852]
- `send_observability_events` (function) — [saleor/webhook/transport/asynchronous/transport.py:947]
- `observability_send_events` (function) — [saleor/webhook/transport/asynchronous/transport.py:1008]
- `observability_reporter_task` (function) — [saleor/webhook/transport/asynchronous/transport.py:1020]

## How it works

The module's files, as provided to this run:

- `saleor/webhook/transport/asynchronous/transport.py` (1031 lines)
- `saleor/webhook/transport/asynchronous/__init__.py` (11 lines)
- `saleor/webhook/transport/asynchronous/tests/__init__.py` (1 lines)
- `saleor/webhook/transport/asynchronous/tests/test_create_deliveries_for_subscriptions.py` (214 lines)
- `saleor/webhook/transport/asynchronous/tests/test_deferred_payload.py` (608 lines)
- `saleor/webhook/transport/asynchronous/tests/test_send_webhooks_async_for_app.py` (216 lines)
- `saleor/webhook/transport/asynchronous/tests/test_transport.py` (311 lines)

## Interactions

- Imports from: `saleor/plugins/openid_connect`, `saleor/core/telemetry`, `saleor/graphql/product/types`, `saleor/graphql`, `saleor/core`
- Imported by: `saleor/plugins/webhook/tests/subscription_webhooks/filterable_webhooks`, `saleor/plugins/webhook/tests`, `saleor/graphql/webhook/tests/mutations`, `saleor/warehouse/tests/webhooks`, `saleor/webhook/observability/tests`, `saleor/webhook/tests/subscription_webhooks`

Internal dependencies named in the source:

- `.....checkout.calculations.fetch_checkout_data`
- `.....checkout.fetch.fetch_checkout_info`
- `.....checkout.fetch.fetch_checkout_lines`
- `.....core.EventDeliveryStatus`
- `.....core.models.EventDelivery`
- `.....core.models.EventDeliveryAttempt`
- `.....core.models.EventDeliveryStatus`
- `.....core.telemetry.get_task_context`
- `.....product.interface.VariantDiscountedPriceChange`
- `.....tests.utils.get_metric_data_point`
- `.....tests.utils.get_span_by_name`
- `.....warehouse.interface.VariantChannelStockInfo`
- `.....webhook.event_types.WebhookEventAsyncType`
- `.....webhook.models.Webhook`
- `....celeryconf.app`
- `....core.EventDeliveryStatus`
- `....core.db.connection.allow_writer`
- `....core.models.EventDelivery`
- `....core.models.EventPayload`
- `....core.tracing.webhooks_otel_trace`
- `....core.utils.get_domain`
- `....core.utils.url.sanitize_url_for_logging`
- `....event_types.WebhookEventAsyncType`
- `....graphql.core.context.SaleorContext`
- `....graphql.core.dataloaders.DataLoader`
- `....graphql.webhook.subscription_types.WEBHOOK_TYPES_MAP`
- `....observability`
- `....utils.get_webhooks_for_event`
- `....webhook.models.Webhook`
- `...event_types.WebhookEventAsyncType`
- `...event_types.WebhookEventSyncType`
- `...observability.WebhookData`
- `..metrics.record_external_request`
- `..metrics.record_first_delivery_attempt_delay`
- `..transport.send_webhook_request_async`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `16d00e0d7f65` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
