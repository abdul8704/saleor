## Purpose

`saleor/webhook/transport/tests` (`saleor/webhook/transport/tests`) groups 3 source file(s) exposing 33 top-level declaration(s).

## Public surface

**`saleor/webhook/transport/tests/test_list_stored_payment_methods.py`**

- `test_get_list_stored_payment_methods_from_response` (function) — [saleor/webhook/transport/tests/test_list_stored_payment_methods.py:26]
- `test_get_list_stored_payment_methods_from_response_only_required_fields` (function) — [saleor/webhook/transport/tests/test_list_stored_payment_methods.py:90]
- `test_get_list_stored_payment_methods_from_response_invalid_input_data` (function) — [saleor/webhook/transport/tests/test_list_stored_payment_methods.py:123]
- `test_get_response_for_stored_payment_method_request_delete_valid_response` (function) — [saleor/webhook/transport/tests/test_list_stored_payment_methods.py:170]
- `test_get_response_for_stored_payment_method_request_delete_invalid_response` (function) — [saleor/webhook/transport/tests/test_list_stored_payment_methods.py:197]
- `test_get_response_for_stored_payment_method_request_delete_response_is_none` (function) — [saleor/webhook/transport/tests/test_list_stored_payment_methods.py:211]
- `test_get_response_for_payment_gateway_initialize_tokenization_valid_response` (function) — [saleor/webhook/transport/tests/test_list_stored_payment_methods.py:245]
- `test_get_response_for_payment_gateway_initialize_tokenization_invalid_response` (function) — [saleor/webhook/transport/tests/test_list_stored_payment_methods.py:273]
- `test_get_response_for_payment_gateway_initialize_tokenization_response_is_none` (function) — [saleor/webhook/transport/tests/test_list_stored_payment_methods.py:287]
- `test_get_response_for_payment_method_tokenization` (function) — [saleor/webhook/transport/tests/test_list_stored_payment_methods.py:374]
- `test_get_response_for_payment_method_tokenization_validation_error` (function) — [saleor/webhook/transport/tests/test_list_stored_payment_methods.py:416]
- `test_get_response_for_payment_method_tokenization_value_error` (function) — [saleor/webhook/transport/tests/test_list_stored_payment_methods.py:427]

**`saleor/webhook/transport/tests/test_utils.py`**

- `mocked_boto3_client_constructor` (function) — [saleor/webhook/transport/tests/test_utils.py:26]
- `sqs_response` (function) — [saleor/webhook/transport/tests/test_utils.py:32]
- `mocked_boto3_client` (function) — [saleor/webhook/transport/tests/test_utils.py:43]
- `DummyTask` (class) — [saleor/webhook/transport/tests/test_utils.py:50]
- `test_webhook_retry` (function) — [saleor/webhook/transport/tests/test_utils.py:56]
- `test_webhook_retry_404` (function) — [saleor/webhook/transport/tests/test_utils.py:76]
- `test_webhook_retry_redirect` (function) — [saleor/webhook/transport/tests/test_utils.py:96]
- `test_send_webhook_using_aws_sqs` (function) — [saleor/webhook/transport/tests/test_utils.py:141]
- `test_send_webhook_using_aws_sqs_with_fifo_queue` (function) — [saleor/webhook/transport/tests/test_utils.py:186]
- `test_get_delivery_for_webhook` (function) — [saleor/webhook/transport/tests/test_utils.py:202]
- `test_get_delivery_for_webhook_invalid_id` (function) — [saleor/webhook/transport/tests/test_utils.py:211]
- `test_get_delivery_for_webhook_inactive_webhook` (function) — [saleor/webhook/transport/tests/test_utils.py:222]
- `test_get_delivery_for_webhook_inactive_app` (function) — [saleor/webhook/transport/tests/test_utils.py:240]
- `test_get_delivery_for_webhook_inactive_app_self_lifecycle_event` (function) — [saleor/webhook/transport/tests/test_utils.py:265]
- `test_get_delivery_for_webhook_inactive_webhook_self_lifecycle_event` (function) — [saleor/webhook/transport/tests/test_utils.py:284]
- `test_get_multiple_deliveries_for_webhooks` (function) — [saleor/webhook/transport/tests/test_utils.py:303]
- `test_get_multiple_deliveries_for_webhooks_with_inactive_webhook` (function) — [saleor/webhook/transport/tests/test_utils.py:316]
- `test_get_multiple_deliveries_for_webhooks_with_inactive_app` (function) — [saleor/webhook/transport/tests/test_utils.py:340]
- `test_truncate_attempt_response` (function) — [saleor/webhook/transport/tests/test_utils.py:386]
- `test_get_sqs_message_group_id` (function) — [saleor/webhook/transport/tests/test_utils.py:416]
- `test_get_sqs_message_group_id_no_app` (function) — [saleor/webhook/transport/tests/test_utils.py:425]

## How it works

The module's files, as provided to this run:

- `saleor/webhook/transport/tests/__init__.py` (1 lines)
- `saleor/webhook/transport/tests/test_list_stored_payment_methods.py` (440 lines)
- `saleor/webhook/transport/tests/test_utils.py` (428 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....core.EventDeliveryStatus`
- `....core.models.EventDelivery`
- `....core.models.EventDeliveryAttempt`
- `...event_types.WebhookEventAsyncType`
- `...response_schemas.utils.annotations.logger`
- `..utils.to_payment_app_id`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `73431da013f5` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
