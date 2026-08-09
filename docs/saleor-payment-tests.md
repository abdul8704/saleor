## Purpose

`saleor/payment/tests` (`saleor/payment/tests`) groups 6 source file(s) exposing 141 top-level declaration(s).

## Public surface

**`saleor/payment/tests/test_gateway.py`**

- `test_process_payment` (function) — [saleor/payment/tests/test_gateway.py:104]
- `test_store_source_when_processing_payment` (function) — [saleor/payment/tests/test_gateway.py:131]
- `test_authorize_payment` (function) — [saleor/payment/tests/test_gateway.py:154]
- `test_capture_payment` (function) — [saleor/payment/tests/test_gateway.py:178]
- `test_refund_for_manual_payment` (function) — [saleor/payment/tests/test_gateway.py:205]
- `test_partial_refund_payment` (function) — [saleor/payment/tests/test_gateway.py:220]
- `test_full_refund_payment` (function) — [saleor/payment/tests/test_gateway.py:246]
- `test_void_payment` (function) — [saleor/payment/tests/test_gateway.py:271]
- `test_confirm_payment` (function) — [saleor/payment/tests/test_gateway.py:298]
- `test_list_gateways` (function) — [saleor/payment/tests/test_gateway.py:329]
- `test_request_charge_action_missing_active_event` (function) — [saleor/payment/tests/test_gateway.py:338]
- `test_request_charge_action_on_order` (function) — [saleor/payment/tests/test_gateway.py:373]
- `test_request_charge_action_by_app` (function) — [saleor/payment/tests/test_gateway.py:438]
- `test_request_action_by_removed_app` (function) — [saleor/payment/tests/test_gateway.py:501]
- `test_request_action_by_disabled_app` (function) — [saleor/payment/tests/test_gateway.py:537]
- `test_request_action_by_removed_app_and_second_active` (function) — [saleor/payment/tests/test_gateway.py:574]
- `test_request_action_by_disabled_app_and_second_active` (function) — [saleor/payment/tests/test_gateway.py:639]
- `test_request_charge_action_on_checkout` (function) — [saleor/payment/tests/test_gateway.py:702]
- `test_request_refund_action_missing_active_event` (function) — [saleor/payment/tests/test_gateway.py:760]
- `test_request_refund_action_updates_refundable_for_checkout` (function) — [saleor/payment/tests/test_gateway.py:794]
- `test_request_refund_action_on_order` (function) — [saleor/payment/tests/test_gateway.py:832]
- `test_request_refund_action_with_granted_refund` (function) — [saleor/payment/tests/test_gateway.py:897]
- `test_request_refund_action_by_app` (function) — [saleor/payment/tests/test_gateway.py:973]
- `test_request_refund_action_on_checkout` (function) — [saleor/payment/tests/test_gateway.py:1039]
- `test_request_cancelation_action_missing_active_event` (function) — [saleor/payment/tests/test_gateway.py:1097]
- `test_request_cancel_action_updates_refundable_for_checkout` (function) — [saleor/payment/tests/test_gateway.py:1131]
- `test_request_cancelation_action_on_order` (function) — [saleor/payment/tests/test_gateway.py:1170]
- `test_request_cancelation_action_by_app` (function) — [saleor/payment/tests/test_gateway.py:1235]
- `test_request_cancelation_action_on_checkout` (function) — [saleor/payment/tests/test_gateway.py:1302]
- `test_payment_refund_or_void_no_payment` (function) — [saleor/payment/tests/test_gateway.py:1363]
- `test_payment_refund_or_void_refund_called` (function) — [saleor/payment/tests/test_gateway.py:1374]
- `test_payment_refund_or_void_refund_not_called_refund_already_started` (function) — [saleor/payment/tests/test_gateway.py:1391]
- `test_payment_refund_or_void_refund_called_txn_exist` (function) — [saleor/payment/tests/test_gateway.py:1421]
- `test_payment_refund_or_void_refund_called_no_txn_with_given_transaction_id` (function) — [saleor/payment/tests/test_gateway.py:1452]
- `test_payment_refund_or_void_void_called` (function) — [saleor/payment/tests/test_gateway.py:1485]
- `test_payment_refund_or_void_void_not_called_txn_exist` (function) — [saleor/payment/tests/test_gateway.py:1502]

**`saleor/payment/tests/test_gateways_utils.py`**

- `gateway_config` (function) — [saleor/payment/tests/test_gateways_utils.py:10]
- `test_get_supported_currencies` (function) — [saleor/payment/tests/test_gateways_utils.py:28]
- `test_get_supported_currencies_not_configured` (function) — [saleor/payment/tests/test_gateways_utils.py:41]

**`saleor/payment/tests/test_payment.py`**

- `payment_method_details` (function) — [saleor/payment/tests/test_payment.py:40]
- `gateway_response` (function) — [saleor/payment/tests/test_payment.py:52]
- `transaction_data` (function) — [saleor/payment/tests/test_payment.py:71]
- `transaction_data_long_error_message` (function) — [saleor/payment/tests/test_payment.py:83]
- `transaction_token` (function) — [saleor/payment/tests/test_payment.py:96]
- `dummy_response` (function) — [saleor/payment/tests/test_payment.py:101]
- `test_create_payment` (function) — [saleor/payment/tests/test_payment.py:115]
- `test_create_payment_requires_order_or_checkout` (function) — [saleor/payment/tests/test_payment.py:143]
- `test_create_payment_from_checkout_requires_billing_address` (function) — [saleor/payment/tests/test_payment.py:156]
- `test_create_payment_from_order_requires_billing_address` (function) — [saleor/payment/tests/test_payment.py:180]
- `test_create_payment_information_for_checkout_payment` (function) — [saleor/payment/tests/test_payment.py:197]
- `test_create_payment_information_for_checkout_token` (function) — [saleor/payment/tests/test_payment.py:232]
- `test_create_payment_information_for_checkout_token_from_order` (function) — [saleor/payment/tests/test_payment.py:241]
- `test_create_payment_information_for_empty_payment` (function) — [saleor/payment/tests/test_payment.py:253]
- `test_create_payment_information_for_checkout_metadata` (function) — [saleor/payment/tests/test_payment.py:263]
- `test_create_payment_information_for_payment_with_transactions` (function) — [saleor/payment/tests/test_payment.py:275]
- `test_create_payment_information_for_draft_order` (function) — [saleor/payment/tests/test_payment.py:307]
- `test_create_payment_information_store` (function) — [saleor/payment/tests/test_payment.py:332]
- `test_create_payment_information_metadata` (function) — [saleor/payment/tests/test_payment.py:367]
- `test_create_transaction` (function) — [saleor/payment/tests/test_payment.py:399]
- `test_create_transaction_long_error_message` (function) — [saleor/payment/tests/test_payment.py:412]
- `test_create_transaction_no_gateway_response` (function) — [saleor/payment/tests/test_payment.py:420]
- `test_gateway_charge_failed` (function) — [saleor/payment/tests/test_payment.py:428]
- `test_gateway_charge_errors` (function) — [saleor/payment/tests/test_payment.py:452]
- `test_gateway_refund_errors` (function) — [saleor/payment/tests/test_payment.py:492]
- `test_clean_authorize` (function) — [saleor/payment/tests/test_payment.py:524]
- `test_clean_capture` (function) — [saleor/payment/tests/test_payment.py:533]
- `test_can_authorize` (function) — [saleor/payment/tests/test_payment.py:565]
- `test_can_capture` (function) — [saleor/payment/tests/test_payment.py:581]
- `test_can_void` (function) — [saleor/payment/tests/test_payment.py:601]
- `test_can_refund` (function) — [saleor/payment/tests/test_payment.py:621]
- `test_payment_get_authorized_amount` (function) — [saleor/payment/tests/test_payment.py:637]
- `test_validate_gateway_response` (function) — [saleor/payment/tests/test_payment.py:655]
- `test_validate_gateway_response_incorrect_transaction_kind` (function) — [saleor/payment/tests/test_payment.py:659]
- `test_validate_gateway_response_not_json_serializable` (function) — [saleor/payment/tests/test_payment.py:670]
- `CustomClass` (class) — [saleor/payment/tests/test_payment.py:671]
- `test_is_currency_supported` (function) — [saleor/payment/tests/test_payment.py:686]
- `test_update_payment` (function) — [saleor/payment/tests/test_payment.py:704]
- `test_payment_owned_by_user_from_order` (function) — [saleor/payment/tests/test_payment.py:718]
- `test_payment_owned_by_user_from_checkout` (function) — [saleor/payment/tests/test_payment.py:731]
- _…and 3 more in this file_

**`saleor/payment/tests/test_tasks.py`**

- `test_transaction_release_funds_for_checkout_task_checkout_with_new_last_change` (function) — [saleor/payment/tests/test_tasks.py:19]
- `test_transaction_release_funds_for_checkout_task_checkout_not_refundable` (function) — [saleor/payment/tests/test_tasks.py:57]
- `test_transaction_release_funds_for_checkout_task_checkout_with_new_tr_modified` (function) — [saleor/payment/tests/test_tasks.py:92]
- `test_transaction_release_funds_for_checkout_task_checkout_with_none_status` (function) — [saleor/payment/tests/test_tasks.py:130]
- `test_transaction_release_funds_for_checkout_task_not_valid_checkout` (function) — [saleor/payment/tests/test_tasks.py:167]
- `test_transaction_release_funds_for_checkout_task_transaction_for_order` (function) — [saleor/payment/tests/test_tasks.py:193]
- `test_transaction_release_funds_for_checkout_task_without_transaction` (function) — [saleor/payment/tests/test_tasks.py:221]
- `test_transaction_release_funds_for_checkout_task_refund_already_requested` (function) — [saleor/payment/tests/test_tasks.py:256]
- `test_transaction_release_funds_for_checkout_task_cancel_already_requested` (function) — [saleor/payment/tests/test_tasks.py:293]
- `test_transaction_release_funds_for_checkout_task_transaction_with_authorization` (function) — [saleor/payment/tests/test_tasks.py:330]
- `test_transaction_release_funds_for_checkout_task_transaction_with_charge` (function) — [saleor/payment/tests/test_tasks.py:378]
- `test_transactions_to_release_funds_setting_toogle` (function) — [saleor/payment/tests/test_tasks.py:423]
- `test_transactions_to_release_funds_after_year` (function) — [saleor/payment/tests/test_tasks.py:466]

**`saleor/payment/tests/test_transaction_item_calculations.py`**

- `test_with_only_authorize_success_event` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:56]
- `test_with_only_authorize_request_event` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:83]
- `test_with_only_authorize_failure_event` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:110]
- `test_with_authorize_request_and_success_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:139]
- `test_with_authorize_request_and_failure_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:167]
- `test_with_authorize_success_and_failure_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:193]
- `test_with_authorize_success_and_older_failure_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:219]
- `test_with_authorize_adjustment` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:251]
- `test_with_authorize_request_and_success_events_different_psp_references` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:293]
- `test_with_only_charge_success_event` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:323]
- `test_with_only_charge_request_event` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:350]
- `test_with_only_charge_failure_event` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:377]
- `test_with_charge_request_and_success_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:406]
- `test_with_charge_request_and_failure_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:434]
- `test_with_charge_success_and_failure_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:460]
- `test_with_charge_success_and_older_failure_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:486]
- `test_with_charge_request_and_success_events_different_psp_references` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:518]
- `test_with_charge_back` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:548]
- `test_with_only_refund_success_event` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:577]
- `test_with_only_refund_request_event` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:606]
- `test_with_only_refund_failure_event` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:637]
- `test_with_refund_request_and_success_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:666]
- `test_with_refund_request_and_failure_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:695]
- `test_with_refund_success_and_failure_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:721]
- `test_with_refund_success_and_older_failure_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:747]
- `test_with_refund_request_and_success_events_different_psp_references` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:780]
- `test_with_refund_reverse` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:811]
- `test_with_only_cancel_success_event` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:851]
- `test_with_only_cancel_request_event` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:878]
- `test_with_only_cancel_failure_event` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:905]
- `test_with_cancel_request_and_success_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:934]
- `test_with_cancel_request_and_failure_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:962]
- `test_with_cancel_success_and_failure_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:988]
- `test_with_cancel_success_and_older_failure_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:1014]
- `test_with_cancel_request_and_success_events_different_psp_references` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:1046]
- `test_with_authorization_success_and_refund_success_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:1076]
- `test_event_without_psp_reference` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:1106]
- `test_event_multiple_events` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:1147]
- `test_event_multiple_events_with_auth_charge_and_refund` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:1256]
- `test_event_multiple_events_with_auth_charge_and_refund_without_psp_references` (function) — [saleor/payment/tests/test_transaction_item_calculations.py:1322]
- _…and 6 more in this file_

## How it works

The module's files, as provided to this run:

- `saleor/payment/tests/__init__.py` (1 lines)
- `saleor/payment/tests/test_gateway.py` (1528 lines)
- `saleor/payment/tests/test_gateways_utils.py` (53 lines)
- `saleor/payment/tests/test_payment.py` (780 lines)
- `saleor/payment/tests/test_tasks.py` (493 lines)
- `saleor/payment/tests/test_transaction_item_calculations.py` (1666 lines)

## Interactions

- Imports from: `saleor/payment`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...TransactionAction`
- `...TransactionEventType`
- `...checkout.CheckoutAuthorizeStatus`
- `...checkout.CheckoutChargeStatus`
- `...checkout.actions.transaction_amounts_for_checkout_updated`
- `...checkout.calculations.calculate_checkout_total`
- `...checkout.fetch.fetch_checkout_info`
- `...checkout.fetch.fetch_checkout_lines`
- `...core.prices.quantize_price`
- `...order.OrderEvents`
- `...plugins.manager.PluginsManager`
- `...plugins.manager.get_plugins_manager`
- `...webhook.event_types.WebhookEventSyncType`
- `...webhook.models.Webhook`
- `..error_codes.PaymentErrorCode`
- `..gateway.is_currency_supported`
- `..gateways.utils.get_supported_currencies`
- `..interface.GatewayConfig`
- `..interface.GatewayResponse`
- `..interface.PaymentMethodInfo`
- `..interface.TransactionActionData`
- `..interface.TransactionData`
- `..models.Payment`
- `..models.TransactionItem`
- `..transaction_item_calculations.recalculate_transaction_amounts`
- `..utils.create_payment_information`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `389f1c946f5d` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
