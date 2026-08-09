## Purpose

`saleor/graphql/payment/mutations/payment` (`saleor/graphql/payment/mutations/payment`) groups 7 source file(s) exposing 41 top-level declaration(s).

## Public surface

**`saleor/graphql/payment/mutations/payment/checkout_payment_create.py`**

- `PaymentInput` (class) — [saleor/graphql/payment/mutations/payment/checkout_payment_create.py:43]
- `Meta` (class) — [saleor/graphql/payment/mutations/payment/checkout_payment_create.py:84]
- `CheckoutPaymentCreate` (class) — [saleor/graphql/payment/mutations/payment/checkout_payment_create.py:92]
- `Arguments` (class) — [saleor/graphql/payment/mutations/payment/checkout_payment_create.py:96]
- `Meta` (class) — [saleor/graphql/payment/mutations/payment/checkout_payment_create.py:115]
- `clean_payment_amount` (function) — [saleor/graphql/payment/mutations/payment/checkout_payment_create.py:122]
- `validate_gateway` (function) — [saleor/graphql/payment/mutations/payment/checkout_payment_create.py:135]
- `raise_not_supported_gateway_error` (function) — [saleor/graphql/payment/mutations/payment/checkout_payment_create.py:152]
- `validate_token` (function) — [saleor/graphql/payment/mutations/payment/checkout_payment_create.py:163]
- `validate_return_url` (function) — [saleor/graphql/payment/mutations/payment/checkout_payment_create.py:177]
- `validate_metadata_keys` (function) — [saleor/graphql/payment/mutations/payment/checkout_payment_create.py:191]
- `validate_checkout_email` (function) — [saleor/graphql/payment/mutations/payment/checkout_payment_create.py:207]
- `validate_checkout_has_no_transactions` (function) — [saleor/graphql/payment/mutations/payment/checkout_payment_create.py:215]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/payment/checkout_payment_create.py:225]

**`saleor/graphql/payment/mutations/payment/payment_capture.py`**

- `PaymentCapture` (class) — [saleor/graphql/payment/mutations/payment/payment_capture.py:17]
- `Arguments` (class) — [saleor/graphql/payment/mutations/payment/payment_capture.py:20]
- `Meta` (class) — [saleor/graphql/payment/mutations/payment/payment_capture.py:24]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/payment/payment_capture.py:32]

**`saleor/graphql/payment/mutations/payment/payment_check_balance.py`**

- `MoneyInput` (class) — [saleor/graphql/payment/mutations/payment/payment_check_balance.py:19]
- `CardInput` (class) — [saleor/graphql/payment/mutations/payment/payment_check_balance.py:24]
- `Meta` (class) — [saleor/graphql/payment/mutations/payment/payment_check_balance.py:36]
- `PaymentCheckBalanceInput` (class) — [saleor/graphql/payment/mutations/payment/payment_check_balance.py:43]
- `Meta` (class) — [saleor/graphql/payment/mutations/payment/payment_check_balance.py:54]
- `PaymentCheckBalance` (class) — [saleor/graphql/payment/mutations/payment/payment_check_balance.py:62]
- `Arguments` (class) — [saleor/graphql/payment/mutations/payment/payment_check_balance.py:65]
- `Meta` (class) — [saleor/graphql/payment/mutations/payment/payment_check_balance.py:70]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/payment/payment_check_balance.py:77]
- `validate_gateway` (function) — [saleor/graphql/payment/mutations/payment/payment_check_balance.py:98]
- `validate_currency` (function) — [saleor/graphql/payment/mutations/payment/payment_check_balance.py:112]

**`saleor/graphql/payment/mutations/payment/payment_initialize.py`**

- `PaymentInitialize` (class) — [saleor/graphql/payment/mutations/payment/payment_initialize.py:16]
- `Arguments` (class) — [saleor/graphql/payment/mutations/payment/payment_initialize.py:21]
- `Meta` (class) — [saleor/graphql/payment/mutations/payment/payment_initialize.py:36]
- `validate_channel` (function) — [saleor/graphql/payment/mutations/payment/payment_initialize.py:43]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/payment/payment_initialize.py:67]

**`saleor/graphql/payment/mutations/payment/payment_refund.py`**

- `PaymentRefund` (class) — [saleor/graphql/payment/mutations/payment/payment_refund.py:19]
- `Meta` (class) — [saleor/graphql/payment/mutations/payment/payment_refund.py:20]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/payment/payment_refund.py:28]

**`saleor/graphql/payment/mutations/payment/payment_void.py`**

- `PaymentVoid` (class) — [saleor/graphql/payment/mutations/payment/payment_void.py:16]
- `Arguments` (class) — [saleor/graphql/payment/mutations/payment/payment_void.py:19]
- `Meta` (class) — [saleor/graphql/payment/mutations/payment/payment_void.py:22]
- `perform_mutation` (function) — [saleor/graphql/payment/mutations/payment/payment_void.py:30]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/payment/mutations/payment/payment_check_balance.py` (121 lines)
- `saleor/graphql/payment/mutations/payment/__init__.py` (15 lines)
- `saleor/graphql/payment/mutations/payment/checkout_payment_create.py` (352 lines)
- `saleor/graphql/payment/mutations/payment/payment_capture.py` (56 lines)
- `saleor/graphql/payment/mutations/payment/payment_initialize.py` (84 lines)
- `saleor/graphql/payment/mutations/payment/payment_refund.py` (69 lines)
- `saleor/graphql/payment/mutations/payment/payment_void.py` (49 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: `saleor/graphql/payment/tests/mutations`

Internal dependencies named in the source:

- `.....channel.models.Channel`
- `.....checkout.calculations.calculate_checkout_total_with_gift_cards`
- `.....checkout.fetch.fetch_checkout_info`
- `.....checkout.fetch.fetch_checkout_lines`
- `.....checkout.models`
- `.....checkout.utils.cancel_active_payments`
- `.....core.error_codes.MetadataErrorCode`
- `.....core.utils.get_client_ip`
- `.....core.utils.url.validate_storefront_url`
- `.....order.actions.order_refunded`
- `.....order.models`
- `.....payment.PaymentError`
- `.....payment.StorePaymentMethod`
- `.....payment.TransactionKind`
- `.....payment.error_codes.PaymentErrorCode`
- `.....payment.gateway`
- `.....payment.gateway.get_payment_gateways`
- `.....payment.gateway.is_currency_supported`
- `.....payment.models.TransactionItem`
- `.....payment.utils.create_payment`
- `.....payment.utils.mark_checkout_search_index_dirty`
- `.....permission.enums.OrderPermissions`
- `....account.i18n.I18nMixin`
- `....app.dataloaders.get_app_promise`
- `....channel.utils.validate_channel`
- `....checkout.mutations.utils.get_checkout`
- `....checkout.types.Checkout`
- `....core.ResolveInfo`
- `....core.context.SyncWebhookControlContext`
- `....core.descriptions.DEPRECATED_LEGACY_PAYMENTS_TYPE_DESCRIPTION`
- `....core.doc_category.DOC_CATEGORY_CHECKOUT`
- `....core.doc_category.DOC_CATEGORY_PAYMENTS`
- `....core.fields.JSONString`
- `....core.mutations.BaseMutation`
- `....core.scalars.PositiveDecimal`
- `....core.scalars.UUID`
- `....core.types.BaseInputObjectType`
- `....core.types.common`
- `....meta.inputs.MetadataInput`
- `....meta.inputs.MetadataInputDescription`
- `....plugins.dataloaders.get_plugin_manager_promise`
- `...enums.StorePaymentMethodEnum`
- `...types.Payment`
- `...types.PaymentInitialized`
- `...utils.deprecated_metadata_contains_empty_key`
- `.checkout_payment_create.CheckoutPaymentCreate`
- `.payment_capture.PaymentCapture`
- `.payment_check_balance.PaymentCheckBalance`
- `.payment_initialize.PaymentInitialize`
- `.payment_refund.PaymentRefund`
- `.payment_void.PaymentVoid`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `de40e7a8bed2` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
