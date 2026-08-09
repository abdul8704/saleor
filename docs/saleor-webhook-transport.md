## Purpose

`saleor/webhook/transport` (`saleor/webhook/transport`) groups 6 source file(s) exposing 45 top-level declaration(s).

## Public surface

**`saleor/webhook/transport/__init__.py`**

- `signature_for_payload` (function) — [saleor/webhook/transport/__init__.py:7]

**`saleor/webhook/transport/list_stored_payment_methods.py`**

- `get_list_stored_payment_methods_from_response` (function) — [saleor/webhook/transport/list_stored_payment_methods.py:37]
- `get_response_for_stored_payment_method_request_delete` (function) — [saleor/webhook/transport/list_stored_payment_methods.py:79]
- `get_list_stored_payment_methods_data_dict` (function) — [saleor/webhook/transport/list_stored_payment_methods.py:103]
- `invalidate_cache_for_stored_payment_methods` (function) — [saleor/webhook/transport/list_stored_payment_methods.py:110]
- `get_response_for_payment_gateway_initialize_tokenization` (function) — [saleor/webhook/transport/list_stored_payment_methods.py:123]
- `get_response_for_payment_method_tokenization` (function) — [saleor/webhook/transport/list_stored_payment_methods.py:151]

**`saleor/webhook/transport/metrics.py`**

- `record_external_request` (function) — [saleor/webhook/transport/metrics.py:71]
- `record_first_delivery_attempt_delay` (function) — [saleor/webhook/transport/metrics.py:102]

**`saleor/webhook/transport/payment.py`**

- `parse_list_payment_gateways_response` (function) — [saleor/webhook/transport/payment.py:14]
- `parse_payment_action_response` (function) — [saleor/webhook/transport/payment.py:39]

**`saleor/webhook/transport/shipping_helpers.py`**

- `to_shipping_app_id` (function) — [saleor/webhook/transport/shipping_helpers.py:7]

**`saleor/webhook/transport/utils.py`**

- `WebhookSchemes` (class) — [saleor/webhook/transport/utils.py:59]
- `EventDeliveryWithAttemptCount` (class) — [saleor/webhook/transport/utils.py:67]
- `PaymentAppData` (class) — [saleor/webhook/transport/utils.py:73]
- `WebhookResponse` (class) — [saleor/webhook/transport/utils.py:80]
- `RequestorModelName` (class) — [saleor/webhook/transport/utils.py:89]
- `DeferredPayloadData` (class) — [saleor/webhook/transport/utils.py:96]
- `prepare_deferred_payload_data` (function) — [saleor/webhook/transport/utils.py:166]
- `generate_cache_key_for_webhook` (function) — [saleor/webhook/transport/utils.py:191]
- `send_webhook_using_http` (function) — [saleor/webhook/transport/utils.py:209]
- `send_webhook_using_aws_sqs` (function) — [saleor/webhook/transport/utils.py:290]
- `send_webhook_using_google_cloud_pubsub` (function) — [saleor/webhook/transport/utils.py:312]
- `send_webhook_using_scheme_method` (function) — [saleor/webhook/transport/utils.py:346]
- `handle_webhook_retry` (function) — [saleor/webhook/transport/utils.py:377]
- `get_delivery_for_webhook` (function) — [saleor/webhook/transport/utils.py:440]
- `get_deliveries_for_app` (function) — [saleor/webhook/transport/utils.py:453]
- `get_multiple_deliveries_for_webhooks` (function) — [saleor/webhook/transport/utils.py:474]
- `catch_duration_time` (function) — [saleor/webhook/transport/utils.py:519]
- `create_attempt` (function) — [saleor/webhook/transport/utils.py:525]
- `attempt_update` (function) — [saleor/webhook/transport/utils.py:545]
- `clear_successful_delivery` (function) — [saleor/webhook/transport/utils.py:578]
- `clear_successful_deliveries` (function) — [saleor/webhook/transport/utils.py:583]
- `process_failed_deliveries` (function) — [saleor/webhook/transport/utils.py:618]
- `create_attempts_for_deliveries` (function) — [saleor/webhook/transport/utils.py:648]
- `delivery_update` (function) — [saleor/webhook/transport/utils.py:670]
- `save_unsuccessful_delivery_attempt` (function) — [saleor/webhook/transport/utils.py:677]
- `from_payment_app_id` (function) — [saleor/webhook/transport/utils.py:691]
- `get_meta_code_key` (function) — [saleor/webhook/transport/utils.py:707]
- `get_meta_description_key` (function) — [saleor/webhook/transport/utils.py:711]
- `to_payment_app_id` (function) — [saleor/webhook/transport/utils.py:715]
- `get_sqs_message_group_id` (function) — [saleor/webhook/transport/utils.py:720]
- `get_boto3_sqs_client` (function) — [saleor/webhook/transport/utils.py:729]
- `get_boto3_sqs_message_kwargs` (function) — [saleor/webhook/transport/utils.py:755]
- `get_google_pubsub_client_and_retry_config` (function) — [saleor/webhook/transport/utils.py:793]

## How it works

The module's files, as provided to this run:

- `saleor/webhook/transport/__init__.py` (11 lines)
- `saleor/webhook/transport/list_stored_payment_methods.py` (214 lines)
- `saleor/webhook/transport/metrics.py` (115 lines)
- `saleor/webhook/transport/payment.py` (82 lines)
- `saleor/webhook/transport/shipping_helpers.py` (11 lines)
- `saleor/webhook/transport/utils.py` (811 lines)

## Interactions

- Imports from: `saleor/core/utils`, `saleor/core`, `saleor/graphql/product/types`, `saleor/plugins/openid_connect`, `saleor/webhook`
- Imported by: `saleor/webhook/transport/synchronous`

Internal dependencies named in the source:

- `...app.headers.AppHeaders`
- `...app.headers.DeprecatedAppHeaders`
- `...app.models.App`
- `...core.db.connection.allow_writer`
- `...core.http_client.HTTPClient`
- `...core.jwt_manager.get_jwt_manager`
- `...core.models.EventDeliveryStatus`
- `...core.tasks.delete_files_from_private_storage_task`
- `...core.telemetry.tracer`
- `...core.utils.build_absolute_uri`
- `...core.utils.json_serializer.CustomJsonEncoder`
- `...core.utils.url.sanitize_url_for_logging`
- `...observability`
- `...product.interface.VariantDiscountedPriceChange`
- `...warehouse.interface.VariantChannelStockInfo`
- `...webhook.event_types.WebhookEventSyncType`
- `...webhook.utils.get_webhooks_for_event`
- `..const.APP_ID_PREFIX`
- `..event_types.WebhookEventAsyncType`
- `..models.Webhook`
- `..response_schemas.utils.helpers.parse_validation_error`
- `..signature_for_payload`
- `.utils.WebhookResponse`
- `.utils.generate_cache_key_for_webhook`
- `.utils.to_payment_app_id`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `7abbb9617271` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
