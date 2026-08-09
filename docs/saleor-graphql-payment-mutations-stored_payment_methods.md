## Purpose

`saleor/graphql/payment/mutations/stored_payment_methods` (`saleor/graphql/payment/mutations/stored_payment_methods`) groups 6 source file(s) exposing 17 top-level declaration(s).

## Public surface

**`saleor/graphql/payment/mutations/stored_payment_methods/payment_gateway_initialize_tokenization.py`**

- `PaymentGatewayInitializeTokenization` (class) — [saleor/graphql/payment/mutations/stored_payment_methods/payment_gateway_initialize_tokenization.py:18]
- `Arguments` (class) — [saleor/graphql/payment/mutations/stored_payment_methods/payment_gateway_initialize_tokenization.py:26]
- `Meta` (class) — [saleor/graphql/payment/mutations/stored_payment_methods/payment_gateway_initialize_tokenization.py:42]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/stored_payment_methods/payment_gateway_initialize_tokenization.py:103]

**`saleor/graphql/payment/mutations/stored_payment_methods/payment_method_intialize_tokenization.py`**

- `PaymentMethodInitializeTokenization` (class) — [saleor/graphql/payment/mutations/stored_payment_methods/payment_method_intialize_tokenization.py:18]
- `Arguments` (class) — [saleor/graphql/payment/mutations/stored_payment_methods/payment_method_intialize_tokenization.py:27]
- `Meta` (class) — [saleor/graphql/payment/mutations/stored_payment_methods/payment_method_intialize_tokenization.py:50]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/stored_payment_methods/payment_method_intialize_tokenization.py:92]

**`saleor/graphql/payment/mutations/stored_payment_methods/payment_method_process_tokenization.py`**

- `PaymentMethodProcessTokenization` (class) — [saleor/graphql/payment/mutations/stored_payment_methods/payment_method_process_tokenization.py:18]
- `Arguments` (class) — [saleor/graphql/payment/mutations/stored_payment_methods/payment_method_process_tokenization.py:27]
- `Meta` (class) — [saleor/graphql/payment/mutations/stored_payment_methods/payment_method_process_tokenization.py:44]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/stored_payment_methods/payment_method_process_tokenization.py:75]

**`saleor/graphql/payment/mutations/stored_payment_methods/payment_method_request_delete.py`**

- `StoredPaymentMethodRequestDelete` (class) — [saleor/graphql/payment/mutations/stored_payment_methods/payment_method_request_delete.py:20]
- `Arguments` (class) — [saleor/graphql/payment/mutations/stored_payment_methods/payment_method_request_delete.py:25]
- `Meta` (class) — [saleor/graphql/payment/mutations/stored_payment_methods/payment_method_request_delete.py:34]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/stored_payment_methods/payment_method_request_delete.py:50]

**`saleor/graphql/payment/mutations/stored_payment_methods/utils.py`**

- `handle_payment_method_action` (function) — [saleor/graphql/payment/mutations/stored_payment_methods/utils.py:13]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/payment/mutations/stored_payment_methods/payment_gateway_initialize_tokenization.py` (111 lines)
- `saleor/graphql/payment/mutations/stored_payment_methods/payment_method_process_tokenization.py` (83 lines)
- `saleor/graphql/payment/mutations/stored_payment_methods/__init__.py` (13 lines)
- `saleor/graphql/payment/mutations/stored_payment_methods/payment_method_intialize_tokenization.py` (104 lines)
- `saleor/graphql/payment/mutations/stored_payment_methods/payment_method_request_delete.py` (99 lines)
- `saleor/graphql/payment/mutations/stored_payment_methods/utils.py` (48 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: `saleor/plugins/tests`

Internal dependencies named in the source:

- `.....channel.models.Channel`
- `.....payment.interface.PaymentGatewayInitializeTokenizationRequestData`
- `.....payment.interface.PaymentMethodInitializeTokenizationRequestData`
- `.....payment.interface.PaymentMethodProcessTokenizationRequestData`
- `.....permission.auth_filters.AuthorizationFilters`
- `.....webhook.event_types.WebhookEventSyncType`
- `....channel.utils.validate_channel`
- `....core.ResolveInfo`
- `....core.doc_category.DOC_CATEGORY_PAYMENTS`
- `....core.enums.PaymentGatewayInitializeTokenizationErrorCode`
- `....core.enums.PaymentMethodInitializeTokenizationErrorCode`
- `....core.enums.PaymentMethodProcessTokenizationErrorCode`
- `....core.enums.StoredPaymentMethodRequestDeleteErrorCode`
- `....core.mutations.BaseMutation`
- `....core.scalars.JSON`
- `....core.types.common.PaymentGatewayInitializeTokenizationError`
- `....core.types.common.PaymentMethodInitializeTokenizationError`
- `....core.types.common.PaymentMethodProcessTokenizationError`
- `....core.types.common.PaymentMethodRequestDeleteError`
- `....core.utils.WebhookEventInfo`
- `....plugins.dataloaders.get_plugin_manager_promise`
- `...enums.PaymentGatewayInitializeTokenizationResultEnum`
- `...enums.PaymentMethodTokenizationResultEnum`
- `...enums.StoredPaymentMethodRequestDeleteResultEnum`
- `...enums.TokenizedPaymentFlowEnum`
- `.payment_method_intialize_tokenization.PaymentMethodInitializeTokenization`
- `.payment_method_process_tokenization.PaymentMethodProcessTokenization`
- `.payment_method_request_delete.StoredPaymentMethodRequestDelete`
- `.utils.handle_payment_method_action`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `ff45252dc4d7` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
