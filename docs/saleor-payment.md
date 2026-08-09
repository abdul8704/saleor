## Purpose

`saleor/payment` (`saleor/payment`) groups 11 source file(s) exposing 186 top-level declaration(s).

## Public surface

**`saleor/payment/__init__.py`**

- `PaymentError` (class) — [saleor/payment/__init__.py:4]
- `GatewayError` (class) — [saleor/payment/__init__.py:14]
- `TransactionItemIdempotencyUniqueError` (class) — [saleor/payment/__init__.py:18]
- `CustomPaymentChoices` (class) — [saleor/payment/__init__.py:22]
- `OperationType` (class) — [saleor/payment/__init__.py:28]
- `TransactionError` (class) — [saleor/payment/__init__.py:37]
- `TransactionKind` (class) — [saleor/payment/__init__.py:52]
- `ChargeStatus` (class) — [saleor/payment/__init__.py:94]
- `StorePaymentMethod` (class) — [saleor/payment/__init__.py:128]
- `TransactionAction` (class) — [saleor/payment/__init__.py:150]
- `TransactionEventType` (class) — [saleor/payment/__init__.py:170]
- `TokenizedPaymentFlow` (class) — [saleor/payment/__init__.py:272]
- `PaymentMethodType` (class) — [saleor/payment/__init__.py:287]

**`saleor/payment/dataloaders.py`**

- `PaymentsByOrderIdLoader` (class) — [saleor/payment/dataloaders.py:7]
- `batch_load` (function) — [saleor/payment/dataloaders.py:10]

**`saleor/payment/error_codes.py`**

- `PaymentErrorCode` (class) — [saleor/payment/error_codes.py:4]
- `TransactionCreateErrorCode` (class) — [saleor/payment/error_codes.py:26]
- `TransactionUpdateErrorCode` (class) — [saleor/payment/error_codes.py:35]
- `TransactionRequestActionErrorCode` (class) — [saleor/payment/error_codes.py:44]
- `TransactionRequestRefundForGrantedRefundErrorCode` (class) — [saleor/payment/error_codes.py:54]
- `TransactionEventReportErrorCode` (class) — [saleor/payment/error_codes.py:66]
- `PaymentGatewayConfigErrorCode` (class) — [saleor/payment/error_codes.py:75]
- `PaymentGatewayInitializeErrorCode` (class) — [saleor/payment/error_codes.py:81]
- `TransactionInitializeErrorCode` (class) — [saleor/payment/error_codes.py:87]
- `TransactionProcessErrorCode` (class) — [saleor/payment/error_codes.py:95]
- `StoredPaymentMethodRequestDeleteErrorCode` (class) — [saleor/payment/error_codes.py:105]
- `PaymentGatewayInitializeTokenizationErrorCode` (class) — [saleor/payment/error_codes.py:113]
- `PaymentMethodInitializeTokenizationErrorCode` (class) — [saleor/payment/error_codes.py:121]
- `PaymentMethodProcessTokenizationErrorCode` (class) — [saleor/payment/error_codes.py:129]

**`saleor/payment/gateway.py`**

- `raise_payment_error` (function) — [saleor/payment/gateway.py:55]
- `wrapped` (function) — [saleor/payment/gateway.py:56]
- `payment_postprocess` (function) — [saleor/payment/gateway.py:65]
- `wrapped` (function) — [saleor/payment/gateway.py:66]
- `require_active_payment` (function) — [saleor/payment/gateway.py:74]
- `wrapped` (function) — [saleor/payment/gateway.py:75]
- `with_locked_payment` (function) — [saleor/payment/gateway.py:83]
- `wrapped` (function) — [saleor/payment/gateway.py:86]
- `request_charge_action` (function) — [saleor/payment/gateway.py:94]
- `request_refund_action` (function) — [saleor/payment/gateway.py:130]
- `request_cancelation_action` (function) — [saleor/payment/gateway.py:169]
- `process_payment` (function) — [saleor/payment/gateway.py:272]
- `authorize` (function) — [saleor/payment/gateway.py:313]
- `capture` (function) — [saleor/payment/gateway.py:351]
- `refund` (function) — [saleor/payment/gateway.py:391]
- `void` (function) — [saleor/payment/gateway.py:438]
- `confirm` (function) — [saleor/payment/gateway.py:463]
- `list_payment_sources` (function) — [saleor/payment/gateway.py:498]
- `list_gateways` (function) — [saleor/payment/gateway.py:507]
- `payment_refund_or_void` (function) — [saleor/payment/gateway.py:546]
- `get_payment_gateways` (function) — [saleor/payment/gateway.py:593]
- `is_currency_supported` (function) — [saleor/payment/gateway.py:629]

**`saleor/payment/interface.py`**

- `StoredPaymentMethodRequestDeleteResult` (class) — [saleor/payment/interface.py:25]
- `StoredPaymentMethodRequestDeleteResponseData` (class) — [saleor/payment/interface.py:41]
- `StoredPaymentMethodRequestDeleteData` (class) — [saleor/payment/interface.py:49]
- `PaymentGateway` (class) — [saleor/payment/interface.py:58]
- `ListStoredPaymentMethodsRequestData` (class) — [saleor/payment/interface.py:68]
- `PaymentMethodCreditCardInfo` (class) — [saleor/payment/interface.py:74]
- `PaymentMethodData` (class) — [saleor/payment/interface.py:83]
- `TransactionActionData` (class) — [saleor/payment/interface.py:112]
- `TransactionRequestEventResponse` (class) — [saleor/payment/interface.py:122]
- `PaymentMethodDetails` (class) — [saleor/payment/interface.py:132]
- `TransactionResponseBase` (class) — [saleor/payment/interface.py:143]
- `TransactionSessionResponse` (class) — [saleor/payment/interface.py:149]
- `TransactionRequestResponse` (class) — [saleor/payment/interface.py:155]
- `TransactionData` (class) — [saleor/payment/interface.py:160]
- `PaymentGatewayData` (class) — [saleor/payment/interface.py:169]
- `TransactionProcessActionData` (class) — [saleor/payment/interface.py:176]
- `TransactionSessionData` (class) — [saleor/payment/interface.py:183]
- `TransactionSessionResult` (class) — [saleor/payment/interface.py:193]
- `PaymentMethodTokenizationBaseRequestData` (class) — [saleor/payment/interface.py:200]
- `PaymentMethodTokenizationBaseResponseData` (class) — [saleor/payment/interface.py:207]
- `PaymentGatewayInitializeTokenizationRequestData` (class) — [saleor/payment/interface.py:213]
- `PaymentGatewayInitializeTokenizationResult` (class) — [saleor/payment/interface.py:221]
- `PaymentGatewayInitializeTokenizationResponseData` (class) — [saleor/payment/interface.py:236]
- `PaymentMethodInitializeTokenizationRequestData` (class) — [saleor/payment/interface.py:245]
- `PaymentMethodProcessTokenizationRequestData` (class) — [saleor/payment/interface.py:255]
- `PaymentMethodTokenizationResult` (class) — [saleor/payment/interface.py:263]
- `PaymentMethodTokenizationResponseData` (class) — [saleor/payment/interface.py:282]
- `PaymentMethodInfo` (class) — [saleor/payment/interface.py:290]
- `GatewayResponse` (class) — [saleor/payment/interface.py:303]
- `AddressData` (class) — [saleor/payment/interface.py:329]
- `StorePaymentMethodEnum` (class) — [saleor/payment/interface.py:346]
- `PaymentLineData` (class) — [saleor/payment/interface.py:353]
- `PaymentLinesData` (class) — [saleor/payment/interface.py:362]
- `RefundData` (class) — [saleor/payment/interface.py:369]
- `PaymentData` (class) — [saleor/payment/interface.py:377]
- `lines_data` (function) — [saleor/payment/interface.py:416]
- `TokenConfig` (class) — [saleor/payment/interface.py:421]
- `GatewayConfig` (class) — [saleor/payment/interface.py:428]
- `CustomerSource` (class) — [saleor/payment/interface.py:446]
- `InitializedPaymentResponse` (class) — [saleor/payment/interface.py:456]

**`saleor/payment/lock_objects.py`**

- `transaction_item_qs_select_for_update` (function) — [saleor/payment/lock_objects.py:15]
- `get_order_and_transaction_item_locked_for_update` (function) — [saleor/payment/lock_objects.py:19]
- `get_checkout_and_transaction_item_locked_for_update` (function) — [saleor/payment/lock_objects.py:29]

**`saleor/payment/model_helpers.py`**

- `get_last_payment` (function) — [saleor/payment/model_helpers.py:12]
- `get_total_authorized` (function) — [saleor/payment/model_helpers.py:16]
- `get_subtotal` (function) — [saleor/payment/model_helpers.py:24]

**`saleor/payment/models.py`**

- `TransactionItem` (class) — [saleor/payment/models.py:31]
- `Meta` (class) — [saleor/payment/models.py:187]
- `TransactionEvent` (class) — [saleor/payment/models.py:206]
- `Meta` (class) — [saleor/payment/models.py:259]
- `Payment` (class) — [saleor/payment/models.py:273]
- `Meta` (class) — [saleor/payment/models.py:357]
- `get_last_transaction` (function) — [saleor/payment/models.py:377]
- `get_total` (function) — [saleor/payment/models.py:380]
- `get_authorized_amount` (function) — [saleor/payment/models.py:383]
- `get_captured_amount` (function) — [saleor/payment/models.py:415]
- `get_charge_amount` (function) — [saleor/payment/models.py:418]
- `is_authorized` (function) — [saleor/payment/models.py:423]
- `not_charged` (function) — [saleor/payment/models.py:432]
- `can_authorize` (function) — [saleor/payment/models.py:435]
- `can_capture` (function) — [saleor/payment/models.py:438]
- `can_void` (function) — [saleor/payment/models.py:443]
- `can_refund` (function) — [saleor/payment/models.py:446]
- `can_confirm` (function) — [saleor/payment/models.py:454]
- `is_manual` (function) — [saleor/payment/models.py:457]
- `Transaction` (class) — [saleor/payment/models.py:461]
- `Meta` (class) — [saleor/payment/models.py:493]
- `get_amount` (function) — [saleor/payment/models.py:508]

**`saleor/payment/tasks.py`**

- `transactions_to_release_funds` (function) — [saleor/payment/tasks.py:23]
- `transaction_release_funds_for_checkout_task` (function) — [saleor/payment/tasks.py:89]

**`saleor/payment/transaction_item_calculations.py`**

- `BaseEvent` (class) — [saleor/payment/transaction_item_calculations.py:12]
- `AuthorizationEvents` (class) — [saleor/payment/transaction_item_calculations.py:19]
- `ChargeEvents` (class) — [saleor/payment/transaction_item_calculations.py:24]
- `RefundEvents` (class) — [saleor/payment/transaction_item_calculations.py:29]
- `CancelEvents` (class) — [saleor/payment/transaction_item_calculations.py:34]
- `ActionEventMap` (class) — [saleor/payment/transaction_item_calculations.py:48]
- `calculate_transaction_amount_based_on_events` (function) — [saleor/payment/transaction_item_calculations.py:329]
- `recalculate_transaction_amounts` (function) — [saleor/payment/transaction_item_calculations.py:352]

**`saleor/payment/utils.py`**

- `recalculate_refundable_for_checkout` (function) — [saleor/payment/utils.py:146]
- `create_payment_lines_information` (function) — [saleor/payment/utils.py:163]
- `create_checkout_payment_lines_information` (function) — [saleor/payment/utils.py:182]
- `create_order_payment_lines_information` (function) — [saleor/payment/utils.py:222]
- `generate_transactions_data` (function) — [saleor/payment/utils.py:251]
- `create_payment_information` (function) — [saleor/payment/utils.py:267]
- `create_payment` (function) — [saleor/payment/utils.py:353]
- `get_already_processed_transaction` (function) — [saleor/payment/utils.py:424]
- `create_transaction` (function) — [saleor/payment/utils.py:439]
- `create_transaction` (function) — [saleor/payment/utils.py:452]
- `create_transaction` (function) — [saleor/payment/utils.py:464]
- `get_already_processed_transaction_or_create_new_transaction` (function) — [saleor/payment/utils.py:507]
- `clean_capture` (function) — [saleor/payment/utils.py:529]
- `clean_authorize` (function) — [saleor/payment/utils.py:539]
- `validate_gateway_response` (function) — [saleor/payment/utils.py:545]
- `gateway_postprocess` (function) — [saleor/payment/utils.py:562]
- `update_payment_charge_status` (function) — [saleor/payment/utils.py:587]
- `fetch_customer_id` (function) — [saleor/payment/utils.py:644]
- `store_customer_id` (function) — [saleor/payment/utils.py:650]
- `prepare_key_for_gateway_customer_id` (function) — [saleor/payment/utils.py:657]
- `update_payment` (function) — [saleor/payment/utils.py:661]
- `update_payment_method_details` (function) — [saleor/payment/utils.py:676]
- `get_payment_token` (function) — [saleor/payment/utils.py:700]
- `price_from_minor_unit` (function) — [saleor/payment/utils.py:709]
- `price_to_minor_unit` (function) — [saleor/payment/utils.py:721]
- `get_channel_slug_from_payment` (function) — [saleor/payment/utils.py:735]
- `try_void_or_refund_inactive_payment` (function) — [saleor/payment/utils.py:746]
- `payment_owned_by_user` (function) — [saleor/payment/utils.py:773]
- `get_final_session_statuses` (function) — [saleor/payment/utils.py:788]
- `get_correct_event_types_based_on_request_type` (function) — [saleor/payment/utils.py:799]
- `parse_transaction_action_data_for_action_webhook` (function) — [saleor/payment/utils.py:830]
- `parse_transaction_action_data_for_session_webhook` (function) — [saleor/payment/utils.py:891]
- `parse_available_actions` (function) — [saleor/payment/utils.py:1051]
- `truncate_transaction_event_message` (function) — [saleor/payment/utils.py:1065]
- `get_failed_transaction_event_type_for_request_event` (function) — [saleor/payment/utils.py:1069]
- `get_failed_type_based_on_event` (function) — [saleor/payment/utils.py:1083]
- `create_failed_transaction_event` (function) — [saleor/payment/utils.py:1108]
- `authorization_success_already_exists` (function) — [saleor/payment/utils.py:1124]
- `get_already_existing_event` (function) — [saleor/payment/utils.py:1131]
- `deduplicate_event` (function) — [saleor/payment/utils.py:1154]
- _…and 17 more in this file_

## How it works

The module's files, as provided to this run:

- `saleor/payment/__init__.py` (305 lines)
- `saleor/payment/interface.py` (459 lines)
- `saleor/payment/models.py` (509 lines)
- `saleor/payment/utils.py` (2080 lines)
- `saleor/payment/dataloaders.py` (19 lines)
- `saleor/payment/error_codes.py` (134 lines)
- `saleor/payment/gateway.py` (632 lines)
- `saleor/payment/lock_objects.py` (36 lines)
- `saleor/payment/model_helpers.py` (26 lines)
- `saleor/payment/tasks.py` (219 lines)
- `saleor/payment/transaction_item_calculations.py` (399 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core`, `saleor/plugins/openid_connect`, `saleor/webhook`
- Imported by: `saleor/payment/tests`, `saleor/payment/gateways`, `saleor/graphql/order/tests/integration`, `saleor/payment/migrations`, `saleor/plugins/tests`

Internal dependencies named in the source:

- `..GatewayError`
- `..PaymentError`
- `..TransactionAction`
- `..TransactionEventType`
- `..TransactionKind`
- `..account.models.User`
- `..app.models.App`
- `..celeryconf.app`
- `..channel.TransactionFlowStrategy`
- `..channel.models.Channel`
- `..checkout.CheckoutAuthorizeStatus`
- `..checkout.calculations`
- `..checkout.lock_objects.checkout_qs_select_for_update`
- `..checkout.models.Checkout`
- `..checkout.payment_utils.update_refundable_for_checkout`
- `..checkout.utils.get_checkout_metadata`
- `..core.db.connection.allow_writer`
- `..core.db.fields.MoneyField`
- `..core.models.ModelWithMetadata`
- `..core.prices.quantize_price`
- `..core.taxes.zero_money`
- `..core.taxes.zero_taxed_money`
- `..core.tracing.traced_atomic_transaction`
- `..core.utils.text.safe_truncate`
- `..giftcard.const.GIFT_CARD_PAYMENT_GATEWAY_ID`
- `..graphql.core.dataloaders.DataLoader`
- `..graphql.core.utils.str_to_enum`
- `..order.FulfillmentLineData`
- `..order.OrderStatus`
- `..order.actions.order_transaction_updated`
- `..order.fetch.OrderLineInfo`
- `..order.fetch.fetch_order_info`
- `..order.lock_objects.order_qs_select_for_update`
- `..order.models.Order`
- `..order.models.OrderGrantedRefund`
- `..order.models.OrderLine`
- `..order.search.update_order_search_vector`
- `..payment.models.TransactionEvent`
- `..payment.models.TransactionItem`
- `..permission.enums.PaymentPermissions`
- `..plugins.manager.PluginsManager`
- `..plugins.manager.get_plugins_manager`
- `..webhook.event_types.WebhookEventSyncType`
- `..webhook.response_schemas.transaction`
- `..webhook.response_schemas.utils.helpers.parse_validation_error`
- `..webhook.utils.get_webhooks_for_event`
- `.error_codes.PaymentErrorCode`
- `.gateway.payment_refund_or_void`
- `.gateway.request_cancelation_action`
- `.gateway.request_refund_action`
- `.models.Payment`
- `.models.Transaction`
- `.models.TransactionEvent`
- `.models.TransactionItem`
- `.transaction_item_calculations.recalculate_transaction_amounts`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `7bad4e34d3ca` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
