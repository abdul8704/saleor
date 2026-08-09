## Purpose

`saleor/webhook/response_schemas` (`saleor/webhook/response_schemas`) groups 9 source file(s) exposing 63 top-level declaration(s).

## Public surface

**`saleor/webhook/response_schemas/payment.py`**

- `CreditCardInfoSchema` (class) — [saleor/webhook/response_schemas/payment.py:36]
- `clean_digits` (function) — [saleor/webhook/response_schemas/payment.py:69]
- `StoredPaymentMethodSchema` (class) — [saleor/webhook/response_schemas/payment.py:73]
- `ListStoredPaymentMethodsSchema` (class) — [saleor/webhook/response_schemas/payment.py:112]
- `StoredPaymentMethodDeleteRequestedSchema` (class) — [saleor/webhook/response_schemas/payment.py:123]
- `PaymentGatewayInitializeTokenizationSessionSchema` (class) — [saleor/webhook/response_schemas/payment.py:139]
- `clean_id` (function) — [saleor/webhook/response_schemas/payment.py:162]
- `clean_result` (function) — [saleor/webhook/response_schemas/payment.py:171]
- `PaymentMethodTokenizationSuccessSchema` (class) — [saleor/webhook/response_schemas/payment.py:175]
- `clean_id` (function) — [saleor/webhook/response_schemas/payment.py:196]
- `PaymentMethodTokenizationPendingSchema` (class) — [saleor/webhook/response_schemas/payment.py:202]
- `clean_id` (function) — [saleor/webhook/response_schemas/payment.py:222]
- `PaymentMethodTokenizationFailedSchema` (class) — [saleor/webhook/response_schemas/payment.py:230]

**`saleor/webhook/response_schemas/shipping.py`**

- `ShippingMethodSchema` (class) — [saleor/webhook/response_schemas/shipping.py:29]
- `price` (function) — [saleor/webhook/response_schemas/shipping.py:82]
- `clean_id` (function) — [saleor/webhook/response_schemas/shipping.py:87]
- `clean_currency` (function) — [saleor/webhook/response_schemas/shipping.py:95]
- `ListShippingMethodsSchema` (class) — [saleor/webhook/response_schemas/shipping.py:108]
- `ExcludedShippingMethodSchema` (class) — [saleor/webhook/response_schemas/shipping.py:112]
- `clean_id` (function) — [saleor/webhook/response_schemas/shipping.py:118]
- `FilterShippingMethodsSchema` (class) — [saleor/webhook/response_schemas/shipping.py:133]

**`saleor/webhook/response_schemas/taxes.py`**

- `LineCalculateTaxesSchema` (class) — [saleor/webhook/response_schemas/taxes.py:9]
- `CalculateTaxesSchema` (class) — [saleor/webhook/response_schemas/taxes.py:15]
- `clean_lines_length` (function) — [saleor/webhook/response_schemas/taxes.py:23]

**`saleor/webhook/response_schemas/transaction.py`**

- `PaymentMethodDetailsBase` (class) — [saleor/webhook/response_schemas/transaction.py:33]
- `clean_type` (function) — [saleor/webhook/response_schemas/transaction.py:51]
- `OtherPaymentMethodDetails` (class) — [saleor/webhook/response_schemas/transaction.py:55]
- `CardPaymentMethodDetails` (class) — [saleor/webhook/response_schemas/transaction.py:65]
- `GiftCardPaymentMethodDetails` (class) — [saleor/webhook/response_schemas/transaction.py:115]
- `TransactionBaseSchema` (class) — [saleor/webhook/response_schemas/transaction.py:140]
- `clean_amount` (function) — [saleor/webhook/response_schemas/transaction.py:203]
- `clean_time` (function) — [saleor/webhook/response_schemas/transaction.py:211]
- `clean_message` (function) — [saleor/webhook/response_schemas/transaction.py:226]
- `clean_actions` (function) — [saleor/webhook/response_schemas/transaction.py:252]
- `clean_result` (function) — [saleor/webhook/response_schemas/transaction.py:257]
- `TransactionAsyncSchema` (class) — [saleor/webhook/response_schemas/transaction.py:263]
- `TransactionSyncFailureSchema` (class) — [saleor/webhook/response_schemas/transaction.py:288]
- `TransactionSyncSuccessSchema` (class) — [saleor/webhook/response_schemas/transaction.py:299]
- `TransactionChargeRequestedAsyncSchema` (class) — [saleor/webhook/response_schemas/transaction.py:315]
- `TransactionChargeRequestedSyncSuccessSchema` (class) — [saleor/webhook/response_schemas/transaction.py:319]
- `TransactionChargeRequestedSyncFailureSchema` (class) — [saleor/webhook/response_schemas/transaction.py:326]
- `TransactionCancelationRequestedAsyncSchema` (class) — [saleor/webhook/response_schemas/transaction.py:333]
- `TransactionCancelationRequestedSyncSuccessSchema` (class) — [saleor/webhook/response_schemas/transaction.py:337]
- `TransactionCancelationRequestedSyncFailureSchema` (class) — [saleor/webhook/response_schemas/transaction.py:344]
- `TransactionRefundRequestedAsyncSchema` (class) — [saleor/webhook/response_schemas/transaction.py:351]
- `TransactionRefundRequestedSyncSuccessSchema` (class) — [saleor/webhook/response_schemas/transaction.py:355]
- `TransactionRefundRequestedSyncFailureSchema` (class) — [saleor/webhook/response_schemas/transaction.py:362]
- `TransactionSessionBaseSchema` (class) — [saleor/webhook/response_schemas/transaction.py:369]
- `TransactionSessionFailureSchema` (class) — [saleor/webhook/response_schemas/transaction.py:392]
- `TransactionSessionCancelSuccessSchema` (class) — [saleor/webhook/response_schemas/transaction.py:410]
- `TransactionSessionActionRequiredSchema` (class) — [saleor/webhook/response_schemas/transaction.py:425]
- `TransactionSessionSuccessSchema` (class) — [saleor/webhook/response_schemas/transaction.py:443]
- `PaymentGatewayInitializeSessionSchema` (class) — [saleor/webhook/response_schemas/transaction.py:462]

**`saleor/webhook/response_schemas/utils/annotations.py`**

- `skip_invalid_metadata` (function) — [saleor/webhook/response_schemas/utils/annotations.py:29]
- `default_if_none` (function) — [saleor/webhook/response_schemas/utils/annotations.py:38]
- `skip_invalid` (function) — [saleor/webhook/response_schemas/utils/annotations.py:48]
- `default_if_invalid` (function) — [saleor/webhook/response_schemas/utils/annotations.py:72]
- `skip_invalid_literal` (function) — [saleor/webhook/response_schemas/utils/annotations.py:97]
- `EnumName` (class) — [saleor/webhook/response_schemas/utils/annotations.py:108]
- `enum_or_name` (function) — [saleor/webhook/response_schemas/utils/annotations.py:121]
- `JSONValue` (class) — [saleor/webhook/response_schemas/utils/annotations.py:155]

**`saleor/webhook/response_schemas/utils/helpers.py`**

- `parse_validation_error` (function) — [saleor/webhook/response_schemas/utils/helpers.py:4]

**`saleor/webhook/response_schemas/utils/validators.py`**

- `lower_values` (function) — [saleor/webhook/response_schemas/utils/validators.py:1]

## How it works

The module's files, as provided to this run:

- `saleor/webhook/response_schemas/transaction.py` (463 lines)
- `saleor/webhook/response_schemas/utils/helpers.py` (21 lines)
- `saleor/webhook/response_schemas/utils/validators.py` (11 lines)
- `saleor/webhook/response_schemas/__init__.py` (126 lines)
- `saleor/webhook/response_schemas/payment.py` (247 lines)
- `saleor/webhook/response_schemas/shipping.py` (136 lines)
- `saleor/webhook/response_schemas/taxes.py` (36 lines)
- `saleor/webhook/response_schemas/utils/__init__.py` (1 lines)
- `saleor/webhook/response_schemas/utils/annotations.py` (173 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/graphql`
- Imported by: `saleor/app/tests`, `saleor/plugins/sendgrid`, `saleor/webhook/tests/response_schemas`, `saleor/webhook/tests`

Internal dependencies named in the source:

- `....core.utils.metadata_manager.metadata_is_valid`
- `....payment.interface`
- `...app.models.App`
- `...core.prices.MAXIMUM_PRICE`
- `...graphql.core.utils.from_global_id_or_error`
- `...graphql.core.utils.str_to_enum`
- `...payment.TokenizedPaymentFlow`
- `...shipping.models.ShippingMethod`
- `..const.APP_ID_PREFIX`
- `..transport.shipping_helpers.to_shipping_app_id`
- `..transport.utils.to_payment_app_id`
- `.shipping.FilterShippingMethodsSchema`
- `.shipping.ListShippingMethodsSchema`
- `.taxes.CalculateTaxesSchema`
- `.utils.annotations.DatetimeUTC`
- `.utils.annotations.DefaultIfNone`
- `.utils.annotations.JSONValue`
- `.utils.annotations.Metadata`
- `.utils.annotations.OnErrorSkip`
- `.utils.annotations.OnErrorSkipLiteral`
- `.utils.validators.lower_values`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `fd7afcb8a1ea` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
