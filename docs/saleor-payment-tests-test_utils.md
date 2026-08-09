## Purpose

`saleor/payment/tests/test_utils` (`saleor/payment/tests/test_utils`) groups 5 source file(s) exposing 117 top-level declaration(s).

## Public surface

**`saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py`**

- `test_create_transaction_event_from_request_triggers_webhooks_when_authorized` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:21]
- `test_create_transaction_event_from_request_updates_order_authorize` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:65]
- `test_create_transaction_event_for_transaction_session_success_response` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:109]
- `test_create_transaction_event_for_transaction_session_success_response_with_no_amount` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:150]
- `test_create_transaction_event_for_transaction_session_success_response_with_0` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:196]
- `test_create_transaction_event_for_transaction_session_not_success_events` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:239]
- `test_create_transaction_event_for_transaction_session_not_success_events_with_no_amount` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:287]
- `test_create_transaction_event_for_transaction_session_missing_psp_reference` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:350]
- `test_create_transaction_event_for_transaction_session_missing_reference_with_action` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:397]
- `test_create_transaction_event_for_transaction_session_call_webhook_order_updated` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:444]
- `test_create_transaction_event_for_transaction_session_call_webhook_for_fully_paid` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:481]
- `test_create_transaction_event_for_transaction_session_success_sets_actions` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:524]
- `test_create_transaction_event_for_transaction_session_failure_doesnt_set_actions` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:568]
- `test_create_transaction_event_for_transaction_session_request_events_as_response` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:609]
- `test_create_transaction_event_updates_transaction_modified_at` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:649]
- `test_create_transaction_event_for_transaction_session_failure_set_psp_reference` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:683]
- `test_create_transaction_event_for_transaction_session_when_psp_ref_missing` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:722]
- `test_create_transaction_event_updates_transaction_modified_at_for_failure` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:759]
- `test_create_transaction_event_message_limit_exceeded` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:794]
- `test_create_transaction_event_with_message` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:839]
- `test_create_transaction_event_with_invalid_message` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:874]
- `NonParsableObject` (class) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:883]
- `test_create_transaction_event_from_request_and_webhook_response_incorrect_data` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:915]
- `test_create_transaction_event_for_transaction_session_twice_auth` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:946]
- `test_create_transaction_event_for_transaction_session_sets_payment_method_details` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:1034]
- `test_create_transaction_event_for_transaction_session_invalid_payment_method_details` (function) — [saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py:1104]

**`saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_action_webhook.py`**

- `test_parse_transaction_action_data_for_action_webhook_with_only_psp_reference` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_action_webhook.py:17]
- `test_parse_transaction_action_data_for_action_webhook_with_provided_time` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_action_webhook.py:72]
- `test_parse_transaction_action_data_for_action_webhook_with_event_all_fields_provided` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_action_webhook.py:102]
- `test_parse_transaction_action_data_for_action_webhook_with_incorrect_result` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_action_webhook.py:140]
- `test_parse_transaction_action_data_for_action_webhook_with_event_only_mandatory_fields` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_action_webhook.py:173]
- `test_parse_transaction_action_data_for_action_webhook_use_provided_amount_when_event_amount_is_missing` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_action_webhook.py:200]
- `test_parse_transaction_action_data_for_action_webhook_skips_input_amount_when_event_has_amount` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_action_webhook.py:219]
- `test_parse_transaction_action_data_for_action_webhook_with_missing_psp_reference` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_action_webhook.py:243]
- `test_parse_transaction_action_data_for_action_webhook_with_missing_optional_psp_reference` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_action_webhook.py:256]

**`saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_session_webhook.py`**

- `test_parse_transaction_action_data_for_session_webhook_with_provided_time` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_session_webhook.py:52]
- `test_parse_transaction_action_data_for_session_webhook_with_event_all_fields_provided` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_session_webhook.py:81]
- `test_parse_transaction_action_data_for_session_webhook_with_incorrect_result` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_session_webhook.py:119]
- `test_parse_transaction_action_data_for_session_webhook_with_event_only_mandatory_fields` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_session_webhook.py:151]
- `test_parse_transaction_action_data_for_session_webhook_use_provided_amount_when_event_amount_is_missing` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_session_webhook.py:178]
- `test_parse_transaction_action_data_for_session_webhook_skips_input_amount_when_event_has_amount` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_session_webhook.py:196]
- `test_parse_transaction_action_data_for_session_webhook_with_empty_response` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_session_webhook.py:219]
- `test_parse_transaction_action_data_for_session_webhook_with_missing_optional_psp_reference` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_session_webhook.py:232]
- `test_parse_transaction_action_data_with_missing_mandatory_event_fields` (function) — [saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_session_webhook.py:247]

**`saleor/payment/tests/test_utils/test_utils.py`**

- `test_create_payment_lines_information_order` (function) — [saleor/payment/tests/test_utils/test_utils.py:38]
- `test_create_payment_lines_information_order_with_voucher` (function) — [saleor/payment/tests/test_utils/test_utils.py:61]
- `get_expected_checkout_payment_lines` (function) — [saleor/payment/tests/test_utils/test_utils.py:85]
- `test_create_payment_lines_information_checkout_with_flat_rates` (function) — [saleor/payment/tests/test_utils/test_utils.py:122]
- `test_create_payment_lines_information_checkout` (function) — [saleor/payment/tests/test_utils/test_utils.py:156]
- `test_create_payment_lines_information_checkout_with_voucher` (function) — [saleor/payment/tests/test_utils/test_utils.py:176]
- `test_create_payment_lines_information_invalid_payment` (function) — [saleor/payment/tests/test_utils/test_utils.py:203]
- `test_get_channel_slug_from_payment_with_order` (function) — [saleor/payment/tests/test_utils/test_utils.py:217]
- `test_get_channel_slug_from_payment_with_checkout` (function) — [saleor/payment/tests/test_utils/test_utils.py:222]
- `test_get_channel_slug_from_payment_without_order` (function) — [saleor/payment/tests/test_utils/test_utils.py:228]
- `test_try_void_or_refund_inactive_payment_failed_transaction` (function) — [saleor/payment/tests/test_utils/test_utils.py:240]
- `test_try_void_or_refund_inactive_payment_transaction_success` (function) — [saleor/payment/tests/test_utils/test_utils.py:258]
- `test_create_failed_transaction_event` (function) — [saleor/payment/tests/test_utils/test_utils.py:272]
- `test_create_transaction_event_from_request_and_webhook_response_with_psp_reference` (function) — [saleor/payment/tests/test_utils/test_utils.py:293]
- `test_create_transaction_event_with_psp_reference_checkout_search_index_dirty_updated` (function) — [saleor/payment/tests/test_utils/test_utils.py:320]
- `test_create_transaction_event_with_missing_psp_reference_checkout_search_index_dirty_not_updated` (function) — [saleor/payment/tests/test_utils/test_utils.py:354]
- `test_create_transaction_event_from_request_and_webhook_response_with_no_psp_reference_valid_event` (function) — [saleor/payment/tests/test_utils/test_utils.py:408]
- `test_create_transaction_event_from_request_and_webhook_response_with_no_psp_reference_invalid_event` (function) — [saleor/payment/tests/test_utils/test_utils.py:459]
- `test_create_transaction_event_from_request_and_webhook_response_with_no_amount_in_response` (function) — [saleor/payment/tests/test_utils/test_utils.py:529]
- `test_create_transaction_event_from_request_and_webhook_response_part_event` (function) — [saleor/payment/tests/test_utils/test_utils.py:571]
- `test_create_transaction_event_from_request_updates_order_charge` (function) — [saleor/payment/tests/test_utils/test_utils.py:611]
- `test_create_transaction_event_from_request_triggers_webhooks_when_fully_paid` (function) — [saleor/payment/tests/test_utils/test_utils.py:651]
- `test_create_transaction_event_from_request_triggers_webhooks_when_partially_paid` (function) — [saleor/payment/tests/test_utils/test_utils.py:699]
- `test_create_transaction_event_from_request_triggers_webhooks_when_fully_refunded` (function) — [saleor/payment/tests/test_utils/test_utils.py:747]
- `test_create_transaction_event_from_request_triggers_webhooks_partially_refunded` (function) — [saleor/payment/tests/test_utils/test_utils.py:795]
- `test_create_transaction_event_from_request_and_webhook_response_full_event` (function) — [saleor/payment/tests/test_utils/test_utils.py:840]
- `test_create_transaction_event_from_request_when_paid` (function) — [saleor/payment/tests/test_utils/test_utils.py:896]
- `test_create_transaction_event_from_request_when_authorized_logs_warnning` (function) — [saleor/payment/tests/test_utils/test_utils.py:945]
- `test_create_transaction_event_from_request_and_webhook_response_same_event` (function) — [saleor/payment/tests/test_utils/test_utils.py:1004]
- `test_create_transaction_event_from_request_handle_incorrect_values` (function) — [saleor/payment/tests/test_utils/test_utils.py:1059]
- `test_create_transaction_event_from_request_and_webhook_response_different_amount` (function) — [saleor/payment/tests/test_utils/test_utils.py:1103]
- `test_create_event_from_request_and_webhook_missing_response_calculate_refundable` (function) — [saleor/payment/tests/test_utils/test_utils.py:1154]
- `test_create_event_from_request_and_webhook_error_response_calculate_refundable` (function) — [saleor/payment/tests/test_utils/test_utils.py:1187]
- `test_create_event_from_request_and_webhook_failure_event_calculate_refundable` (function) — [saleor/payment/tests/test_utils/test_utils.py:1234]
- `test_create_event_from_request_and_webhook_success_event_calculate_refundable` (function) — [saleor/payment/tests/test_utils/test_utils.py:1281]
- `test_create_event_from_request_and_webhook_success_updated_granted_refund_status` (function) — [saleor/payment/tests/test_utils/test_utils.py:1335]
- `test_create_event_from_request_and_webhook_success_granted_refund_status_only_psp` (function) — [saleor/payment/tests/test_utils/test_utils.py:1388]
- `test_create_event_from_request_and_webhook_pending_event_calculate_refundable` (function) — [saleor/payment/tests/test_utils/test_utils.py:1427]
- `test_create_transaction_event_from_request_and_webhook_response_message_loo_long` (function) — [saleor/payment/tests/test_utils/test_utils.py:1462]
- `test_create_transaction_event_from_request_and_webhook_with_message` (function) — [saleor/payment/tests/test_utils/test_utils.py:1524]
- _…and 33 more in this file_

## How it works

The module's files, as provided to this run:

- `saleor/payment/tests/test_utils/__init__.py` (1 lines)
- `saleor/payment/tests/test_utils/test_create_transaction_event_for_transaction_session.py` (1145 lines)
- `saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_action_webhook.py` (270 lines)
- `saleor/payment/tests/test_utils/test_parse_transaction_action_data_for_session_webhook.py` (261 lines)
- `saleor/payment/tests/test_utils/test_utils.py` (2713 lines)

## Interactions

- Imports from: `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....TransactionEventType`
- `....checkout.CheckoutAuthorizeStatus`
- `....checkout.calculations`
- `....checkout.fetch.fetch_checkout_info`
- `....checkout.fetch.fetch_checkout_lines`
- `....order.OrderAuthorizeStatus`
- `....order.OrderChargeStatus`
- `....order.OrderGrantedRefundStatus`
- `....plugins.manager.get_plugins_manager`
- `....webhook.event_types.WebhookEventSyncType`
- `....webhook.models.Webhook`
- `....webhook.transport.utils.generate_cache_key_for_webhook`
- `...interface.TransactionRequestEventResponse`
- `...interface.TransactionSessionResponse`
- `...models.TransactionEvent`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `3f1f8eb2d807` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
