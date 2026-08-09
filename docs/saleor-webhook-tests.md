## Purpose

`saleor/webhook/tests` (`saleor/webhook/tests`) groups 14 source file(s) exposing 156 top-level declaration(s).

## Public surface

**`saleor/webhook/tests/conftest.py`**

- `mocked_fetch_checkout` (function) — [saleor/webhook/tests/conftest.py:7]
- `mocked_fetch_side_effect` (function) — [saleor/webhook/tests/conftest.py:8]
- `mocked_fetch_order` (function) — [saleor/webhook/tests/conftest.py:21]
- `mocked_fetch_side_effect` (function) — [saleor/webhook/tests/conftest.py:22]
- `payment_method_response` (function) — [saleor/webhook/tests/conftest.py:33]

**`saleor/webhook/tests/test_models.py`**

- `test_webhook_identifier_must_be_unique_per_app` (function) — [saleor/webhook/tests/test_models.py:11]
- `test_webhook_identifier_can_be_reused_across_apps` (function) — [saleor/webhook/tests/test_models.py:21]
- `test_webhook_allows_multiple_null_identifiers_per_app` (function) — [saleor/webhook/tests/test_models.py:36]
- `test_webhook_identifier_cannot_be_blank` (function) — [saleor/webhook/tests/test_models.py:46]

**`saleor/webhook/tests/test_payment_webhook_utils.py`**

- `test_to_payment_app_id_app_identifier_used` (function) — [saleor/webhook/tests/test_payment_webhook_utils.py:18]
- `test_to_payment_app_id_app_id_used` (function) — [saleor/webhook/tests/test_payment_webhook_utils.py:29]
- `test_from_payment_app_id_from_pk` (function) — [saleor/webhook/tests/test_payment_webhook_utils.py:43]
- `test_from_payment_app_id_from_identifier` (function) — [saleor/webhook/tests/test_payment_webhook_utils.py:50]
- `test_from_payment_app_id_invalid` (function) — [saleor/webhook/tests/test_payment_webhook_utils.py:69]
- `test_parse_list_payment_gateways_response_app_identifier` (function) — [saleor/webhook/tests/test_payment_webhook_utils.py:74]
- `test_parse_list_payment_gateways_response_app_id` (function) — [saleor/webhook/tests/test_payment_webhook_utils.py:95]
- `test_parse_list_payment_gateways_response_no_id` (function) — [saleor/webhook/tests/test_payment_webhook_utils.py:119]
- `test_parse_list_payment_gateways_response_dict_response` (function) — [saleor/webhook/tests/test_payment_webhook_utils.py:130]
- `payment_action_response` (function) — [saleor/webhook/tests/test_payment_webhook_utils.py:144]
- `test_parse_payment_action_response` (function) — [saleor/webhook/tests/test_payment_webhook_utils.py:166]
- `test_parse_payment_action_response_parse_amount` (function) — [saleor/webhook/tests/test_payment_webhook_utils.py:219]
- `test_clear_successful_delivery` (function) — [saleor/webhook/tests/test_payment_webhook_utils.py:237]
- `test_clear_successful_delivery_with_payload_in_database` (function) — [saleor/webhook/tests/test_payment_webhook_utils.py:252]
- `test_clear_successful_delivery_when_payload_in_multiple_deliveries` (function) — [saleor/webhook/tests/test_payment_webhook_utils.py:272]
- `test_clear_successful_delivery_on_failed_delivery` (function) — [saleor/webhook/tests/test_payment_webhook_utils.py:288]

**`saleor/webhook/tests/test_tasks.py`**

- `mocked_webhook_response` (function) — [saleor/webhook/tests/test_tasks.py:26]
- `test_trigger_transaction_request` (function) — [saleor/webhook/tests/test_tasks.py:42]
- `test_trigger_transaction_request_with_webhook_subscription` (function) — [saleor/webhook/tests/test_tasks.py:101]
- `test_trigger_transaction_request_missing_app_owner_updates_refundable_checkout` (function) — [saleor/webhook/tests/test_tasks.py:184]
- `test_trigger_transaction_request_missing_webhook_updates_refundable_checkout` (function) — [saleor/webhook/tests/test_tasks.py:253]
- `test_trigger_transaction_request_incorrect_subscription_updates_refundable_checkout` (function) — [saleor/webhook/tests/test_tasks.py:299]
- `test_handle_transaction_request_task_missing_delivery_updates_refundable_checkout` (function) — [saleor/webhook/tests/test_tasks.py:367]
- `test_handle_transaction_request_task_with_only_psp_reference` (function) — [saleor/webhook/tests/test_tasks.py:434]
- `test_handle_transaction_request_task_with_server_error` (function) — [saleor/webhook/tests/test_tasks.py:501]
- `test_handle_transaction_request_task_with_missing_psp_reference` (function) — [saleor/webhook/tests/test_tasks.py:557]
- `test_handle_transaction_request_task_with_missing_required_event_field` (function) — [saleor/webhook/tests/test_tasks.py:636]
- `test_handle_transaction_request_task_with_result_event` (function) — [saleor/webhook/tests/test_tasks.py:723]
- `test_handle_transaction_request_task_with_only_required_fields_for_result_event` (function) — [saleor/webhook/tests/test_tasks.py:822]
- `test_handle_transaction_request_task_calls_recalculation_of_amounts` (function) — [saleor/webhook/tests/test_tasks.py:919]
- `test_handle_transaction_request_task_with_available_actions` (function) — [saleor/webhook/tests/test_tasks.py:989]
- `test_handle_transaction_request_task_request_event_included_in_calculations` (function) — [saleor/webhook/tests/test_tasks.py:1087]

**`saleor/webhook/tests/test_utils.py`**

- `sync_type` (function) — [saleor/webhook/tests/test_utils.py:24]
- `async_type` (function) — [saleor/webhook/tests/test_utils.py:29]
- `sync_webhook` (function) — [saleor/webhook/tests/test_utils.py:34]
- `async_app_factory` (function) — [saleor/webhook/tests/test_utils.py:44]
- `create_app` (function) — [saleor/webhook/tests/test_utils.py:45]
- `test_get_webhooks_for_event` (function) — [saleor/webhook/tests/test_utils.py:59]
- `test_get_webhooks_for_event_when_app_webhook_inactive` (function) — [saleor/webhook/tests/test_utils.py:68]
- `test_get_webhooks_for_event_when_webhooks_provided` (function) — [saleor/webhook/tests/test_utils.py:80]
- `test_get_webhooks_for_event_when_app_has_no_permissions` (function) — [saleor/webhook/tests/test_utils.py:93]
- `test_get_webhook_for_event_no_duplicates` (function) — [saleor/webhook/tests/test_utils.py:105]
- `test_get_webhook_for_event_not_returning_any_webhook_for_sync_event_types` (function) — [saleor/webhook/tests/test_utils.py:114]
- `app_lifecycle_app_factory` (function) — [saleor/webhook/tests/test_utils.py:126]
- `create_app` (function) — [saleor/webhook/tests/test_utils.py:133]
- `test_app_lifecycle_returns_self_webhook_without_manage_apps` (function) — [saleor/webhook/tests/test_utils.py:153]
- `test_app_lifecycle_does_not_leak_to_other_apps` (function) — [saleor/webhook/tests/test_utils.py:168]
- `test_app_lifecycle_ignores_manage_apps_holders` (function) — [saleor/webhook/tests/test_utils.py:182]
- `test_app_lifecycle_includes_soft_deleted_app` (function) — [saleor/webhook/tests/test_utils.py:202]
- `test_app_lifecycle_includes_inactive_app` (function) — [saleor/webhook/tests/test_utils.py:215]
- `test_app_lifecycle_excludes_inactive_webhook` (function) — [saleor/webhook/tests/test_utils.py:230]
- `test_app_lifecycle_matches_any_subscription` (function) — [saleor/webhook/tests/test_utils.py:243]
- `test_app_lifecycle_rejects_non_lifecycle_event` (function) — [saleor/webhook/tests/test_utils.py:260]
- `test_truncation_error_extra_fields` (function) — [saleor/webhook/tests/test_utils.py:284]
- `test_get_webhooks_for_multiple_events` (function) — [saleor/webhook/tests/test_utils.py:300]
- `test_different_target_urls_produce_different_cache_key` (function) — [saleor/webhook/tests/test_utils.py:370]
- `test_different_payload_produce_different_cache_key` (function) — [saleor/webhook/tests/test_utils.py:395]
- `test_different_event_produce_different_cache_key` (function) — [saleor/webhook/tests/test_utils.py:420]
- `test_different_app_produce_different_cache_key` (function) — [saleor/webhook/tests/test_utils.py:438]

**`saleor/webhook/tests/test_webhook_ip_filtering.py`**

- `test_rejects_private_ips` (function) — [saleor/webhook/tests/test_webhook_ip_filtering.py:6]

**`saleor/webhook/tests/test_webhook_payload_serializers.py`**

- `test_python_serializer_extra_model_fields` (function) — [saleor/webhook/tests/test_webhook_payload_serializers.py:4]
- `test_python_serializer_extra_model_fields_incorrect_fields` (function) — [saleor/webhook/tests/test_webhook_payload_serializers.py:19]

**`saleor/webhook/tests/test_webhook_payloads.py`**

- `parse_django_datetime` (function) — [saleor/webhook/tests/test_webhook_payloads.py:57]
- `order_for_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:62]
- `payment_for_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:103]
- `test_generate_order_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:112]
- `test_generate_order_payload_no_user_email_but_user_set` (function) — [saleor/webhook/tests/test_webhook_payloads.py:295]
- `test_generate_fulfillment_lines_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:330]
- `test_generate_fulfillment_lines_payload_deleted_variant` (function) — [saleor/webhook/tests/test_webhook_payloads.py:383]
- `test_generate_fulfillment_metadata_updated_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:408]
- `test_generate_gift_card_metadata_updated_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:427]
- `test_generate_voucher_metadata_updated_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:442]
- `test_order_lines_have_all_required_fields` (function) — [saleor/webhook/tests/test_webhook_payloads.py:456]
- `test_order_line_without_sku_still_has_id` (function) — [saleor/webhook/tests/test_webhook_payloads.py:536]
- `test_generate_order_metadata_updated_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:557]
- `test_generate_collection_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:573]
- `test_generate_product_payload_charge_taxes` (function) — [saleor/webhook/tests/test_webhook_payloads.py:597]
- `test_generate_shipping_zone_metadata_updated_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:616]
- `test_generate_collection_metadata_updated_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:633]
- `test_generate_product_metadata_updated_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:650]
- `test_generate_product_variant_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:666]
- `test_generate_product_variant_with_external_media_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:707]
- `test_generate_product_variant_without_sku_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:742]
- `test_generate_product_variant_deleted_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:773]
- `test_generate_product_variant_metadata_updated_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:803]
- `test_generate_invoice_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:819]
- `test_generate_list_gateways_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:867]
- `test_generate_payment_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:880]
- `test_generate_payment_payload_with_refund_data` (function) — [saleor/webhook/tests/test_webhook_payloads.py:900]
- `test_generate_payment_payload_fulfillment_return` (function) — [saleor/webhook/tests/test_webhook_payloads.py:931]
- `test_generate_payment_with_transactions_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:960]
- `test_generate_transaction_item_metadata_updated_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:998]
- `test_generate_checkout_lines_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:1019]
- `test_generate_checkout_lines_payload_when_variant_without_listing` (function) — [saleor/webhook/tests/test_webhook_payloads.py:1029]
- `test_generate_checkout_lines_payload_custom_price` (function) — [saleor/webhook/tests/test_webhook_payloads.py:1047]
- `test_generate_checkout_metadata_updated_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:1065]
- `test_generate_product_translation_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:1081]
- `test_generate_product_variant_translation_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:1098]
- `test_generate_choices_attribute_value_translation_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:1114]
- `test_generate_unique_product_attribute_value_translation_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:1134]
- `test_generate_unique_variant_attribute_value_translation_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:1155]
- `test_generate_unique_page_attribute_value_translation_payload` (function) — [saleor/webhook/tests/test_webhook_payloads.py:1180]
- _…and 19 more in this file_

**`saleor/webhook/tests/test_webhook_protocols.py`**

- `test_trigger_webhooks_with_aws_sqs` (function) — [saleor/webhook/tests/test_webhook_protocols.py:23]
- `test_trigger_webhooks_with_aws_sqs_and_secret_key` (function) — [saleor/webhook/tests/test_webhook_protocols.py:93]
- `test_trigger_webhooks_with_google_pub_sub` (function) — [saleor/webhook/tests/test_webhook_protocols.py:157]
- `test_trigger_webhooks_with_google_pub_sub_when_timout_error_raised` (function) — [saleor/webhook/tests/test_webhook_protocols.py:206]
- `test_trigger_webhooks_with_google_pub_sub_and_secret_key` (function) — [saleor/webhook/tests/test_webhook_protocols.py:260]
- `test_trigger_webhooks_with_http` (function) — [saleor/webhook/tests/test_webhook_protocols.py:304]
- `test_trigger_webhooks_with_http_and_secret_key` (function) — [saleor/webhook/tests/test_webhook_protocols.py:359]
- `test_trigger_webhooks_with_http_and_secret_key_as_empty_string` (function) — [saleor/webhook/tests/test_webhook_protocols.py:408]
- `test_trigger_webhooks_with_http_and_custom_headers` (function) — [saleor/webhook/tests/test_webhook_protocols.py:461]
- `test_trigger_webhooks_async_pick_up_queue_based_on_protocol` (function) — [saleor/webhook/tests/test_webhook_protocols.py:512]

**`saleor/webhook/tests/test_webhook_sample_payloads.py`**

- `test_generate_sample_payload_order` (function) — [saleor/webhook/tests/test_webhook_sample_payloads.py:41]
- `test_generate_sample_payload_fulfillment_created` (function) — [saleor/webhook/tests/test_webhook_sample_payloads.py:71]
- `test_generate_sample_payload_order_removed_channel_listing_from_shipping` (function) — [saleor/webhook/tests/test_webhook_sample_payloads.py:110]
- `test_generate_sample_payload_empty_response_` (function) — [saleor/webhook/tests/test_webhook_sample_payloads.py:149]
- `test_generate_sample_customer_payload` (function) — [saleor/webhook/tests/test_webhook_sample_payloads.py:153]
- `test_generate_sample_product_payload` (function) — [saleor/webhook/tests/test_webhook_sample_payloads.py:160]
- `test_generate_sample_checkout_payload` (function) — [saleor/webhook/tests/test_webhook_sample_payloads.py:184]

**`saleor/webhook/tests/test_webhook_serializers.py`**

- `test_serialize_variant_attributes` (function) — [saleor/webhook/tests/test_webhook_serializers.py:23]
- `test_serialize_product_attributes` (function) — [saleor/webhook/tests/test_webhook_serializers.py:51]
- `test_serialize_checkout_lines` (function) — [saleor/webhook/tests/test_webhook_serializers.py:195]
- `test_serialize_checkout_lines_with_promotion` (function) — [saleor/webhook/tests/test_webhook_serializers.py:229]

**`saleor/webhook/tests/test_webhook_tasks.py`**

- `webhooks_factory` (function) — [saleor/webhook/tests/test_webhook_tasks.py:10]
- `factory` (function) — [saleor/webhook/tests/test_webhook_tasks.py:11]
- `test_get_webhooks_for_event_webhook_ordering` (function) — [saleor/webhook/tests/test_webhook_tasks.py:21]

**`saleor/webhook/tests/test_webhook_validators.py`**

- `test_webhook_validator` (function) — [saleor/webhook/tests/test_webhook_validators.py:61]
- `test_webhook_header_name_case_insensitive` (function) — [saleor/webhook/tests/test_webhook_validators.py:70]

## How it works

The module's files, as provided to this run:

- `saleor/webhook/tests/__init__.py` (1 lines)
- `saleor/webhook/tests/conftest.py` (47 lines)
- `saleor/webhook/tests/test_models.py` (49 lines)
- `saleor/webhook/tests/test_payment_webhook_utils.py` (295 lines)
- `saleor/webhook/tests/test_tasks.py` (1154 lines)
- `saleor/webhook/tests/test_utils.py` (460 lines)
- `saleor/webhook/tests/test_webhook_ip_filtering.py` (28 lines)
- `saleor/webhook/tests/test_webhook_payload_serializers.py` (34 lines)
- `saleor/webhook/tests/test_webhook_payloads.py` (1812 lines)
- `saleor/webhook/tests/test_webhook_protocols.py` (549 lines)
- `saleor/webhook/tests/test_webhook_sample_payloads.py` (213 lines)
- `saleor/webhook/tests/test_webhook_serializers.py` (268 lines)
- `saleor/webhook/tests/test_webhook_tasks.py` (35 lines)
- `saleor/webhook/tests/test_webhook_validators.py` (71 lines)

## Interactions

- Imports from: `saleor/webhook`, `saleor/webhook/response_schemas`, `saleor/plugins/openid_connect`, `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....__version__`
- `...app.models.App`
- `...attribute.AttributeEntityType`
- `...attribute.AttributeInputType`
- `...attribute.AttributeType`
- `...attribute.models.Attribute`
- `...attribute.models.AttributeValue`
- `...attribute.utils.associate_attribute_values_to_instance`
- `...checkout.fetch.fetch_checkout_info`
- `...checkout.fetch.fetch_checkout_lines`
- `...core.EventDeliveryStatus`
- `...core.http_client.HTTPClient`
- `...core.models.EventDelivery`
- `...core.models.EventDeliveryAttempt`
- `...core.models.EventPayload`
- `...core.prices.quantize_price`
- `...core.private_storage`
- `...core.utils.json_serializer.CustomJsonEncoder`
- `...discount.DiscountType`
- `...discount.DiscountValueType`
- `...graphql.utils.get_user_or_app_from_context`
- `...order.FulfillmentLineData`
- `...order.OrderOrigin`
- `...order.OrderStatus`
- `...order.actions.fulfill_order_lines`
- `...order.fetch.OrderLineInfo`
- `...order.models.Order`
- `...payment.TransactionAction`
- `...payment.TransactionEventType`
- `...payment.TransactionKind`
- `...payment.interface.RefundData`
- `...payment.interface.TransactionActionData`
- `...payment.interface.TransactionData`
- `...payment.models.TransactionEvent`
- `...payment.models.TransactionItem`
- `...payment.transaction_item_calculations.recalculate_transaction_amounts`
- `...plugins.manager.get_plugins_manager`
- `...product.models.ProductVariant`
- `...warehouse.WarehouseClickAndCollectOption`
- `..const.APP_ID_PREFIX`
- `..event_types.WebhookEventAsyncType`
- `..event_types.WebhookEventSyncType`
- `..models.Webhook`
- `..models.WebhookEvent`
- `..observability.payload_schema.ObservabilityEventTypes`
- `..payload_serializers.PythonSerializer`
- `..payloads.generate_transaction_action_request_payload`
- `..serializers.serialize_checkout_lines`
- `..transport.asynchronous.trigger_webhooks_async`
- `..transport.signature_for_payload`
- `..transport.utils.from_payment_app_id`
- `..utils.get_webhooks_for_event`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `0f32719e113b` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
