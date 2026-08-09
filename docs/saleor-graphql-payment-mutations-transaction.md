## Purpose

`saleor/graphql/payment/mutations/transaction` (`saleor/graphql/payment/mutations/transaction`) groups 11 source file(s) exposing 85 top-level declaration(s).

## Public surface

**`saleor/graphql/payment/mutations/transaction/payment_gateway_initialize.py`**

- `PaymentGatewayConfig` (class) — [saleor/graphql/payment/mutations/transaction/payment_gateway_initialize.py:14]
- `Meta` (class) — [saleor/graphql/payment/mutations/transaction/payment_gateway_initialize.py:21]
- `PaymentGatewayToInitialize` (class) — [saleor/graphql/payment/mutations/transaction/payment_gateway_initialize.py:25]
- `Meta` (class) — [saleor/graphql/payment/mutations/transaction/payment_gateway_initialize.py:34]
- `PaymentGatewayInitialize` (class) — [saleor/graphql/payment/mutations/transaction/payment_gateway_initialize.py:38]
- `Arguments` (class) — [saleor/graphql/payment/mutations/transaction/payment_gateway_initialize.py:43]
- `Meta` (class) — [saleor/graphql/payment/mutations/transaction/payment_gateway_initialize.py:62]
- `prepare_response` (function) — [saleor/graphql/payment/mutations/transaction/payment_gateway_initialize.py:74]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/transaction/payment_gateway_initialize.py:127]

**`saleor/graphql/payment/mutations/transaction/shared.py`**

- `CardPaymentMethodDetailsInput` (class) — [saleor/graphql/payment/mutations/transaction/shared.py:21]
- `OtherPaymentMethodDetailsInput` (class) — [saleor/graphql/payment/mutations/transaction/shared.py:48]
- `GiftCardPaymentMethodDetailsInput` (class) — [saleor/graphql/payment/mutations/transaction/shared.py:55]
- `PaymentMethodDetailsInput` (class) — [saleor/graphql/payment/mutations/transaction/shared.py:79]
- `Meta` (class) — [saleor/graphql/payment/mutations/transaction/shared.py:99]
- `validate_card_payment_method_details_input` (function) — [saleor/graphql/payment/mutations/transaction/shared.py:106]
- `GiftCardPaymentMethodDetailsValidatedInput` (class) — [saleor/graphql/payment/mutations/transaction/shared.py:183]
- `validate_gift_card_payment_method_details_input` (function) — [saleor/graphql/payment/mutations/transaction/shared.py:193]
- `validate_payment_method_details_input` (function) — [saleor/graphql/payment/mutations/transaction/shared.py:211]
- `get_payment_method_details` (function) — [saleor/graphql/payment/mutations/transaction/shared.py:275]

**`saleor/graphql/payment/mutations/transaction/transaction_create.py`**

- `TransactionCreateInput` (class) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:49]
- `Meta` (class) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:88]
- `TransactionEventInput` (class) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:92]
- `Meta` (class) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:97]
- `TransactionCreate` (class) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:101]
- `Arguments` (class) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:104]
- `Meta` (class) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:117]
- `validate_external_url` (function) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:124]
- `validate_metadata_keys` (function) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:142]
- `get_money_data_from_input` (function) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:158]
- `cleanup_and_update_metadata_data` (function) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:182]
- `validate_instance` (function) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:198]
- `validate_money_input` (function) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:214]
- `validate_input` (function) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:239]
- `create_transaction` (function) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:273]
- `create_transaction_event` (function) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:307]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/transaction/transaction_create.py:330]

**`saleor/graphql/payment/mutations/transaction/transaction_event_report.py`**

- `TransactionEventReport` (class) — [saleor/graphql/payment/mutations/transaction/transaction_event_report.py:65]
- `Arguments` (class) — [saleor/graphql/payment/mutations/transaction/transaction_event_report.py:80]
- `Meta` (class) — [saleor/graphql/payment/mutations/transaction/transaction_event_report.py:151]
- `update_transaction` (function) — [saleor/graphql/payment/mutations/transaction/transaction_event_report.py:196]
- `get_related_granted_refund` (function) — [saleor/graphql/payment/mutations/transaction/transaction_event_report.py:257]
- `clean_amount_value` (function) — [saleor/graphql/payment/mutations/transaction/transaction_event_report.py:272]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/transaction/transaction_event_report.py:299]

**`saleor/graphql/payment/mutations/transaction/transaction_initialize.py`**

- `TransactionInitialize` (class) — [saleor/graphql/payment/mutations/transaction/transaction_initialize.py:30]
- `Arguments` (class) — [saleor/graphql/payment/mutations/transaction/transaction_initialize.py:42]
- `Meta` (class) — [saleor/graphql/payment/mutations/transaction/transaction_initialize.py:88]
- `clean_action` (function) — [saleor/graphql/payment/mutations/transaction/transaction_initialize.py:99]
- `clean_app_from_payment_gateway` (function) — [saleor/graphql/payment/mutations/transaction/transaction_initialize.py:117]
- `clean_idempotency_key` (function) — [saleor/graphql/payment/mutations/transaction/transaction_initialize.py:140]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/transaction/transaction_initialize.py:155]
- `validate_checkout` (function) — [saleor/graphql/payment/mutations/transaction/transaction_initialize.py:229]

**`saleor/graphql/payment/mutations/transaction/transaction_process.py`**

- `TransactionProcess` (class) — [saleor/graphql/payment/mutations/transaction/transaction_process.py:35]
- `Arguments` (class) — [saleor/graphql/payment/mutations/transaction/transaction_process.py:47]
- `Meta` (class) — [saleor/graphql/payment/mutations/transaction/transaction_process.py:76]
- `get_action` (function) — [saleor/graphql/payment/mutations/transaction/transaction_process.py:85]
- `get_source_object` (function) — [saleor/graphql/payment/mutations/transaction/transaction_process.py:93]
- `get_request_event` (function) — [saleor/graphql/payment/mutations/transaction/transaction_process.py:112]
- `get_already_processed_event` (function) — [saleor/graphql/payment/mutations/transaction/transaction_process.py:139]
- `clean_payment_app` (function) — [saleor/graphql/payment/mutations/transaction/transaction_process.py:149]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/transaction/transaction_process.py:177]
- `validate_checkout` (function) — [saleor/graphql/payment/mutations/transaction/transaction_process.py:231]

**`saleor/graphql/payment/mutations/transaction/transaction_request_action.py`**

- `TransactionRequestAction` (class) — [saleor/graphql/payment/mutations/transaction/transaction_request_action.py:44]
- `Arguments` (class) — [saleor/graphql/payment/mutations/transaction/transaction_request_action.py:47]
- `Meta` (class) — [saleor/graphql/payment/mutations/transaction/transaction_request_action.py:81]
- `handle_transaction_action` (function) — [saleor/graphql/payment/mutations/transaction/transaction_request_action.py:88]
- `create_transaction_event_requested` (function) — [saleor/graphql/payment/mutations/transaction/transaction_request_action.py:159]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/transaction/transaction_request_action.py:252]

**`saleor/graphql/payment/mutations/transaction/transaction_request_refund_for_granted_refund.py`**

- `TransactionRequestRefundForGrantedRefund` (class) — [saleor/graphql/payment/mutations/transaction/transaction_request_refund_for_granted_refund.py:32]
- `Arguments` (class) — [saleor/graphql/payment/mutations/transaction/transaction_request_refund_for_granted_refund.py:35]
- `Meta` (class) — [saleor/graphql/payment/mutations/transaction/transaction_request_refund_for_granted_refund.py:59]
- `clean_input` (function) — [saleor/graphql/payment/mutations/transaction/transaction_request_refund_for_granted_refund.py:68]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/transaction/transaction_request_refund_for_granted_refund.py:149]

**`saleor/graphql/payment/mutations/transaction/transaction_update.py`**

- `TransactionUpdateInput` (class) — [saleor/graphql/payment/mutations/transaction/transaction_update.py:47]
- `Meta` (class) — [saleor/graphql/payment/mutations/transaction/transaction_update.py:48]
- `TransactionUpdate` (class) — [saleor/graphql/payment/mutations/transaction/transaction_update.py:52]
- `Arguments` (class) — [saleor/graphql/payment/mutations/transaction/transaction_update.py:55]
- `Meta` (class) — [saleor/graphql/payment/mutations/transaction/transaction_update.py:75]
- `check_can_update` (function) — [saleor/graphql/payment/mutations/transaction/transaction_update.py:91]
- `validate_transaction_input` (function) — [saleor/graphql/payment/mutations/transaction/transaction_update.py:108]
- `update_transaction` (function) — [saleor/graphql/payment/mutations/transaction/transaction_update.py:142]
- `assign_app_to_transaction_data_if_missing` (function) — [saleor/graphql/payment/mutations/transaction/transaction_update.py:178]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/transaction/transaction_update.py:195]

**`saleor/graphql/payment/mutations/transaction/utils.py`**

- `get_transaction_item` (function) — [saleor/graphql/payment/mutations/transaction/utils.py:21]
- `clean_customer_ip_address` (function) — [saleor/graphql/payment/mutations/transaction/utils.py:56]
- `create_transaction_event_requested` (function) — [saleor/graphql/payment/mutations/transaction/utils.py:85]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/payment/mutations/transaction/transaction_event_report.py` (496 lines)
- `saleor/graphql/payment/mutations/transaction/__init__.py` (21 lines)
- `saleor/graphql/payment/mutations/transaction/payment_gateway_initialize.py` (151 lines)
- `saleor/graphql/payment/mutations/transaction/shared.py` (315 lines)
- `saleor/graphql/payment/mutations/transaction/transaction_create.py` (391 lines)
- `saleor/graphql/payment/mutations/transaction/transaction_initialize.py` (244 lines)
- `saleor/graphql/payment/mutations/transaction/transaction_process.py` (246 lines)
- `saleor/graphql/payment/mutations/transaction/transaction_request_action.py` (308 lines)
- `saleor/graphql/payment/mutations/transaction/transaction_request_refund_for_granted_refund.py` (212 lines)
- `saleor/graphql/payment/mutations/transaction/transaction_update.py` (268 lines)
- `saleor/graphql/payment/mutations/transaction/utils.py` (129 lines)

## Interactions

- Imports from: `saleor/permission`
- Imported by: `saleor/graphql/payment/tests/mutations`

Internal dependencies named in the source:

- `.....account.models.User`
- `.....app.models.App`
- `.....channel.TransactionFlowStrategy`
- `.....channel.models.Channel`
- `.....checkout.models`
- `.....checkout.models.Checkout`
- `.....checkout.utils.activate_payments`
- `.....checkout.utils.cancel_active_payments`
- `.....core.exceptions.PermissionDenied`
- `.....core.prices.quantize_price`
- `.....core.tracing.traced_atomic_transaction`
- `.....core.utils.events.call_event`
- `.....core.utils.get_client_ip`
- `.....giftcard.const.GIFT_CARD_PAYMENT_GATEWAY_ID`
- `.....giftcard.gateway.refund_gift_card_transaction`
- `.....order.OrderGrantedRefundStatus`
- `.....order.events.transaction_event`
- `.....order.models`
- `.....order.models.Order`
- `.....order.utils.calculate_order_granted_refund_status`
- `.....page.models.Page`
- `.....payment.FAILED_TRANSACTION_EVENTS`
- `.....payment.OPTIONAL_AMOUNT_EVENTS`
- `.....payment.PaymentError`
- `.....payment.PaymentMethodType`
- `.....payment.TransactionAction`
- `.....payment.TransactionEventType`
- `.....payment.TransactionItemIdempotencyUniqueError`
- `.....payment.error_codes.TransactionCreateErrorCode`
- `.....payment.error_codes.TransactionProcessErrorCode`
- `.....payment.error_codes.TransactionRequestActionErrorCode`
- `.....payment.gateway.request_refund_action`
- `.....payment.interface.PaymentGatewayData`
- `.....payment.interface.PaymentMethodDetails`
- `.....payment.models`
- `.....payment.transaction_item_calculations.recalculate_transaction_amounts`
- `.....payment.utils.handle_transaction_initialize_session`
- `.....permission.auth_filters.AuthorizationFilters`
- `.....permission.enums.PaymentPermissions`
- `.....plugins.manager.PluginsManager`
- `.....webhook.event_types.WebhookEventAsyncType`
- `....app.dataloaders.get_app_promise`
- `....channel.enums.TransactionFlowStrategyEnum`
- `....checkout.types.Checkout`
- `....core.ResolveInfo`
- `....core.descriptions.ADDED_IN_322`
- `....core.descriptions.ADDED_IN_323`
- `....core.doc_category.DOC_CATEGORY_PAYMENTS`
- `....core.enums.PaymentGatewayInitializeErrorCode`
- `....core.enums.TransactionEventReportErrorCode`
- `....core.enums.TransactionInitializeErrorCode`
- `....core.enums.TransactionRequestRefundForGrantedRefundErrorCode`
- `....core.mutations.BaseMutation`
- `....core.mutations.DeprecatedModelMutation`
- `....core.scalars.DateTime`
- `....core.scalars.JSON`
- `....core.scalars.PositiveDecimal`
- `....core.scalars.UUID`
- `....core.types.BaseInputObjectType`
- `....core.types.BaseObjectType`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `7f395d14c1ce` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
