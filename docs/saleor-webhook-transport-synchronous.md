## Purpose

`saleor/webhook/transport/synchronous` (`saleor/webhook/transport/synchronous`) groups 4 source file(s) exposing 16 top-level declaration(s).

## Public surface

**`saleor/webhook/transport/synchronous/tests/test_transport.py`**

- `test_send_webhook_request_sync_set_span_status_failed_invalid_json` (function) — [saleor/webhook/transport/synchronous/tests/test_transport.py:21]
- `test_send_webhook_request_sync_set_span_status_failed_error_response` (function) — [saleor/webhook/transport/synchronous/tests/test_transport.py:50]
- `test_send_webhook_request_sync_record_external_request` (function) — [saleor/webhook/transport/synchronous/tests/test_transport.py:77]
- `test_send_webhook_request_sync_record_external_request_when_delivery_attempt_failed` (function) — [saleor/webhook/transport/synchronous/tests/test_transport.py:126]
- `test_send_webhook_request_sync_record_external_request_with_invalid_json_response` (function) — [saleor/webhook/transport/synchronous/tests/test_transport.py:176]
- `test_send_webhook_request_sync_record_external_request_with_unknown_webhook_scheme` (function) — [saleor/webhook/transport/synchronous/tests/test_transport.py:225]

**`saleor/webhook/transport/synchronous/transport.py`**

- `handle_transaction_request_task` (function) — [saleor/webhook/transport/synchronous/transport.py:75]
- `send_webhook_request_sync` (function) — [saleor/webhook/transport/synchronous/transport.py:195]
- `trigger_webhook_sync_promise_if_not_cached` (function) — [saleor/webhook/transport/synchronous/transport.py:202]
- `process_response_data` (function) — [saleor/webhook/transport/synchronous/transport.py:236]
- `create_delivery_for_subscription_sync_event` (function) — [saleor/webhook/transport/synchronous/transport.py:263]
- `create_promise_delivery_for_subscription_sync_event` (function) — [saleor/webhook/transport/synchronous/transport.py:329]
- `create_delivery` (function) — [saleor/webhook/transport/synchronous/transport.py:366]
- `trigger_webhook_sync_promise` (function) — [saleor/webhook/transport/synchronous/transport.py:398]
- `trigger_sync_for_delivery` (function) — [saleor/webhook/transport/synchronous/transport.py:411]
- `trigger_transaction_request` (function) — [saleor/webhook/transport/synchronous/transport.py:451]

## How it works

The module's files, as provided to this run:

- `saleor/webhook/transport/synchronous/transport.py` (516 lines)
- `saleor/webhook/transport/synchronous/__init__.py` (1 lines)
- `saleor/webhook/transport/synchronous/tests/__init__.py` (1 lines)
- `saleor/webhook/transport/synchronous/tests/test_transport.py` (271 lines)

## Interactions

- Imports from: `saleor/core/telemetry`, `saleor/core/utils`, `saleor/graphql`, `saleor/webhook/transport`, `saleor/core`
- Imported by: `saleor/checkout/tests/webhooks`, `saleor/order/tests/webhooks`, `saleor/plugins/webhook/tests`, `saleor/shipping/tests`

Internal dependencies named in the source:

- `.....core.models.EventDeliveryStatus`
- `.....core.telemetry.set_global_attributes`
- `.....tests.utils.get_metric_data_point`
- `....account.models.User`
- `....app.models.App`
- `....celeryconf.app`
- `....const`
- `....core.EventDeliveryStatus`
- `....core.db.connection.allow_writer`
- `....core.models.EventDelivery`
- `....core.models.EventPayload`
- `....core.tracing.webhooks_otel_trace`
- `....core.utils.events.call_event`
- `....core.utils.get_domain`
- `....core.utils.url.sanitize_url_for_logging`
- `....graphql.webhook.subscription_types.WEBHOOK_TYPES_MAP`
- `....observability`
- `....payment.PaymentError`
- `....payment.interface.TransactionActionData`
- `....payment.models.TransactionEvent`
- `....webhook.models.Webhook`
- `...event_types.WebhookEventSyncType`
- `...payloads.generate_transaction_action_request_payload`
- `...signature_for_payload`
- `...utils.WebhookResponse`
- `...utils.get_webhooks_for_event`
- `..metrics.record_external_request`
- `..transport._send_webhook_request_sync`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `5f80808fedfc` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
