## Purpose

`saleor/webhook` (`saleor/webhook`) groups 14 source file(s) exposing 88 top-level declaration(s).

## Public surface

**`saleor/webhook/__init__.py`**

- `traced_payload_generator` (function) — [saleor/webhook/__init__.py:4]
- `wrapper` (function) — [saleor/webhook/__init__.py:5]

**`saleor/webhook/circuit_breaker/breaker_board.py`**

- `record_circuit_breaker_state_change` (function) — [saleor/webhook/circuit_breaker/breaker_board.py:58]
- `BreakerBoard` (class) — [saleor/webhook/circuit_breaker/breaker_board.py:68]
- `validate_sync_events` (function) — [saleor/webhook/circuit_breaker/breaker_board.py:97]
- `exceeded_error_threshold` (function) — [saleor/webhook/circuit_breaker/breaker_board.py:111]
- `reached_half_open_target_success_count` (function) — [saleor/webhook/circuit_breaker/breaker_board.py:132]
- `set_breaker_state` (function) — [saleor/webhook/circuit_breaker/breaker_board.py:135]
- `update_breaker_state` (function) — [saleor/webhook/circuit_breaker/breaker_board.py:156]
- `register_error` (function) — [saleor/webhook/circuit_breaker/breaker_board.py:185]
- `register_success` (function) — [saleor/webhook/circuit_breaker/breaker_board.py:189]
- `wrap_promise_func` (function) — [saleor/webhook/circuit_breaker/breaker_board.py:192]
- `inner` (function) — [saleor/webhook/circuit_breaker/breaker_board.py:200]
- `process_response` (function) — [saleor/webhook/circuit_breaker/breaker_board.py:219]
- `initialize_breaker_board` (function) — [saleor/webhook/circuit_breaker/breaker_board.py:232]

**`saleor/webhook/circuit_breaker/storage.py`**

- `Storage` (class) — [saleor/webhook/circuit_breaker/storage.py:13]
- `set_app_state` (function) — [saleor/webhook/circuit_breaker/storage.py:14]
- `get_app_state` (function) — [saleor/webhook/circuit_breaker/storage.py:17]
- `get_event_count` (function) — [saleor/webhook/circuit_breaker/storage.py:20]
- `register_event` (function) — [saleor/webhook/circuit_breaker/storage.py:23]
- `clear_state_for_app` (function) — [saleor/webhook/circuit_breaker/storage.py:26]
- `Meta` (class) — [saleor/webhook/circuit_breaker/storage.py:29]
- `serialize_breaker_state` (function) — [saleor/webhook/circuit_breaker/storage.py:33]
- `deserialize_breaker_state` (function) — [saleor/webhook/circuit_breaker/storage.py:37]
- `RedisStorage` (class) — [saleor/webhook/circuit_breaker/storage.py:43]
- `get_base_storage_key` (function) — [saleor/webhook/circuit_breaker/storage.py:56]
- `set_app_state` (function) — [saleor/webhook/circuit_breaker/storage.py:59]
- `get_app_state` (function) — [saleor/webhook/circuit_breaker/storage.py:69]
- `get_event_count` (function) — [saleor/webhook/circuit_breaker/storage.py:80]
- `register_event` (function) — [saleor/webhook/circuit_breaker/storage.py:89]
- `clear_state_for_app` (function) — [saleor/webhook/circuit_breaker/storage.py:113]

**`saleor/webhook/deprecated_event_types.py`**

- `WebhookEventType` (class) — [saleor/webhook/deprecated_event_types.py:1]

**`saleor/webhook/error_codes.py`**

- `WebhookErrorCode` (class) — [saleor/webhook/error_codes.py:4]
- `WebhookDryRunErrorCode` (class) — [saleor/webhook/error_codes.py:19]
- `WebhookTriggerErrorCode` (class) — [saleor/webhook/error_codes.py:31]

**`saleor/webhook/event_types.py`**

- `WebhookEventAsyncType` (class) — [saleor/webhook/event_types.py:23]
- `WebhookEventSyncType` (class) — [saleor/webhook/event_types.py:861]

**`saleor/webhook/models.py`**

- `WebhookURLField` (class) — [saleor/webhook/models.py:12]
- `Webhook` (class) — [saleor/webhook/models.py:18]
- `Meta` (class) — [saleor/webhook/models.py:45]
- `WebhookEvent` (class) — [saleor/webhook/models.py:68]

**`saleor/webhook/payload_helpers.py`**

- `generate_requestor` (function) — [saleor/webhook/payload_helpers.py:14]
- `generate_meta` (function) — [saleor/webhook/payload_helpers.py:22]

**`saleor/webhook/payload_serializers.py`**

- `PythonSerializer` (class) — [saleor/webhook/payload_serializers.py:11]
- `get_dump_object` (function) — [saleor/webhook/payload_serializers.py:23]
- `PayloadSerializer` (class) — [saleor/webhook/payload_serializers.py:38]
- `serialize` (function) — [saleor/webhook/payload_serializers.py:48]
- `get_dump_object` (function) — [saleor/webhook/payload_serializers.py:66]

**`saleor/webhook/payloads.py`**

- `generate_metadata_updated_payload` (function) — [saleor/webhook/payloads.py:108]
- `prepare_order_lines_allocations_payload` (function) — [saleor/webhook/payloads.py:128]
- `generate_order_lines_payload` (function) — [saleor/webhook/payloads.py:143]
- `generate_order_payload` (function) — [saleor/webhook/payloads.py:242]
- `generate_sale_payload` (function) — [saleor/webhook/payloads.py:386]
- `generate_sale_toggle_payload` (function) — [saleor/webhook/payloads.py:435]
- `generate_invoice_payload` (function) — [saleor/webhook/payloads.py:458]
- `generate_checkout_payload` (function) — [saleor/webhook/payloads.py:499]
- `generate_customer_payload` (function) — [saleor/webhook/payloads.py:595]
- `generate_collection_payload` (function) — [saleor/webhook/payloads.py:634]
- `serialize_product_channel_listing_payload` (function) — [saleor/webhook/payloads.py:672]
- `generate_product_payload` (function) — [saleor/webhook/payloads.py:708]
- `generate_product_deleted_payload` (function) — [saleor/webhook/payloads.py:752]
- `generate_product_variant_listings_payload` (function) — [saleor/webhook/payloads.py:783]
- `generate_product_variant_media_payload` (function) — [saleor/webhook/payloads.py:800]
- `generate_product_variant_payload` (function) — [saleor/webhook/payloads.py:816]
- `generate_product_variant_stocks_payload` (function) — [saleor/webhook/payloads.py:855]
- `generate_fulfillment_lines_payload` (function) — [saleor/webhook/payloads.py:861]
- `generate_fulfillment_payload` (function) — [saleor/webhook/payloads.py:936]
- `generate_page_payload` (function) — [saleor/webhook/payloads.py:989]
- `generate_payment_payload` (function) — [saleor/webhook/payloads.py:1040]
- `generate_list_gateways_payload` (function) — [saleor/webhook/payloads.py:1057]
- `generate_sample_payload` (function) — [saleor/webhook/payloads.py:1116]
- `process_translation_context` (function) — [saleor/webhook/payloads.py:1160]
- `generate_translation_payload` (function) — [saleor/webhook/payloads.py:1179]
- `generate_transaction_action_request_payload` (function) — [saleor/webhook/payloads.py:1208]
- `generate_transaction_session_payload` (function) — [saleor/webhook/payloads.py:1267]
- `generate_thumbnail_payload` (function) — [saleor/webhook/payloads.py:1292]
- `generate_product_media_payload` (function) — [saleor/webhook/payloads.py:1299]

**`saleor/webhook/serializers.py`**

- `serialize_variant_full_name` (function) — [saleor/webhook/serializers.py:20]
- `serialize_checkout_lines` (function) — [saleor/webhook/serializers.py:37]
- `serialize_product_attributes` (function) — [saleor/webhook/serializers.py:73]
- `serialize_variant_attributes` (function) — [saleor/webhook/serializers.py:139]

**`saleor/webhook/utils.py`**

- `get_filter_for_single_webhook_event` (function) — [saleor/webhook/utils.py:27]
- `get_webhooks_for_event` (function) — [saleor/webhook/utils.py:69]
- `get_webhooks_for_app_lifecycle_event` (function) — [saleor/webhook/utils.py:94]
- `get_webhooks_for_multiple_events` (function) — [saleor/webhook/utils.py:129]
- `calculate_webhooks_for_multiple_events` (function) — [saleor/webhook/utils.py:162]
- `filter_webhooks_for_channel` (function) — [saleor/webhook/utils.py:202]

**`saleor/webhook/validators.py`**

- `custom_headers_validator` (function) — [saleor/webhook/validators.py:15]

## How it works

The module's files, as provided to this run:

- `saleor/webhook/serializers.py` (194 lines)
- `saleor/webhook/circuit_breaker/storage.py` (122 lines)
- `saleor/webhook/__init__.py` (11 lines)
- `saleor/webhook/event_types.py` (1023 lines)
- `saleor/webhook/circuit_breaker/breaker_board.py` (246 lines)
- `saleor/webhook/error_codes.py` (41 lines)
- `saleor/webhook/models.py` (75 lines)
- `saleor/webhook/validators.py` (51 lines)
- `saleor/webhook/const.py` (8 lines)
- `saleor/webhook/deprecated_event_types.py` (165 lines)
- `saleor/webhook/payload_helpers.py` (38 lines)
- `saleor/webhook/payload_serializers.py` (105 lines)
- `saleor/webhook/payloads.py` (1301 lines)
- `saleor/webhook/utils.py` (222 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core`, `saleor/graphql`, `saleor/core/utils`, `saleor`, `saleor/plugins/openid_connect`, `saleor/core/db`
- Imported by: `saleor/graphql/core/tests/garbage_collection`, `saleor/payment/migrations`, `saleor/core`, `saleor/core/utils`, `saleor/graphql/tests`, `saleor/payment`, `saleor/webhook/migrations`, `saleor/webhook/observability`, `saleor/webhook/tests`, `saleor/app`, `saleor/core/management`, `saleor/core/notification`, `saleor/core/tests`, `saleor/csv`, `saleor/graphql/checkout/mutations`, `saleor/graphql/core`, `saleor/graphql/core/tests`, `saleor/graphql/core/types`, `saleor/graphql/webhook/tests`, `saleor/plugins/webhook/tests`, `saleor/tests/e2e`, `saleor/tests`, `saleor/thumbnail`, `saleor/warehouse/tests/webhooks`, `saleor/webhook/tests/circuit_breaker`, `saleor/webhook/transport`

Internal dependencies named in the source:

- `...__version__`
- `...app.models.App`
- `...graphql.app.enums.CircuitBreakerState`
- `...webhook.event_types.WebhookEventSyncType`
- `...webhook.models.Webhook`
- `..account.models.User`
- `..app.models.App`
- `..app.validators.AppURLValidator`
- `..attribute.AttributeEntityType`
- `..attribute.AttributeInputType`
- `..attribute.models.AttributeValueTranslation`
- `..checkout.fetch.fetch_checkout_lines`
- `..checkout.models.Checkout`
- `..checkout.utils.get_checkout_metadata`
- `..core.db.connection.allow_writer`
- `..core.prices.quantize_price`
- `..core.prices.quantize_price_fields`
- `..core.telemetry.saleor_attributes`
- `..core.telemetry.tracer`
- `..core.utils.build_absolute_uri`
- `..core.utils.json_serializer.CustomJsonEncoder`
- `..discount.models.Promotion`
- `..invoice.models.Invoice`
- `..order.FulfillmentStatus`
- `..order.OrderStatus`
- `..order.models.Fulfillment`
- `..order.models.FulfillmentLine`
- `..order.models.Order`
- `..order.models.OrderLine`
- `..order.utils.get_order_country`
- `..page.models.Page`
- `..payment.ChargeStatus`
- `..payment.models.Payment`
- `..payment.models.TransactionItem`
- `..plugins.base_plugin.RequestorOrLazyObject`
- `..product.ProductMediaTypes`
- `..product.models.Collection`
- `..product.models.Product`
- `..product.models.ProductMedia`
- `..product.models.ProductVariant`
- `..shipping.models.ShippingMethod`
- `..tax.models.TaxClassCountryRate`
- `..thumbnail.models.Thumbnail`
- `..traced_payload_generator`
- `..translation.models.Translation`
- `..warehouse.models.Warehouse`
- `.const.MAX_FILTERABLE_CHANNEL_SLUGS_LIMIT`
- `.event_types.WebhookEventAsyncType`
- `.event_types.WebhookEventSyncType`
- `.models.Webhook`
- `.models.WebhookEvent`
- `.payload_helpers.generate_meta`
- `.payload_helpers.generate_requestor`
- `.payload_serializers.PayloadSerializer`
- `.transport.utils.from_payment_app_id`
- `.validators.custom_headers_validator`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `1e0f2cb0fd44` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
