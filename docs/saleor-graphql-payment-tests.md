## Purpose

`saleor/graphql/payment/tests` (`saleor/graphql/payment/tests`) groups 7 source file(s) exposing 19 top-level declaration(s).

## Public surface

**`saleor/graphql/payment/tests/benchmark/test_payment_transactions.py`**

- `test_payment_transactions` (function) — [saleor/graphql/payment/tests/benchmark/test_payment_transactions.py:54]

**`saleor/graphql/payment/tests/deprecated/test_checkout_payment_create.py`**

- `test_checkout_add_payment_by_checkout_id` (function) — [saleor/graphql/payment/tests/deprecated/test_checkout_payment_create.py:29]
- `test_checkout_add_payment_neither_token_and_id_given` (function) — [saleor/graphql/payment/tests/deprecated/test_checkout_payment_create.py:72]
- `test_checkout_add_payment_both_token_and_id_given` (function) — [saleor/graphql/payment/tests/deprecated/test_checkout_payment_create.py:105]

**`saleor/graphql/payment/tests/test_legacy_api_deprecation.py`**

- `test_legacy_payment_fields_are_deprecated` (function) — [saleor/graphql/payment/tests/test_legacy_api_deprecation.py:109]
- `test_legacy_payment_enum_values_are_deprecated` (function) — [saleor/graphql/payment/tests/test_legacy_api_deprecation.py:119]
- `test_legacy_payment_types_have_deprecation_description` (function) — [saleor/graphql/payment/tests/test_legacy_api_deprecation.py:130]
- `test_order_payment_status_filter_is_deprecated_in_printed_schema` (function) — [saleor/graphql/payment/tests/test_legacy_api_deprecation.py:137]
- `test_shared_payment_gateway_type_is_not_deprecated` (function) — [saleor/graphql/payment/tests/test_legacy_api_deprecation.py:154]
- `test_transactions_api_fields_are_not_deprecated` (function) — [saleor/graphql/payment/tests/test_legacy_api_deprecation.py:160]

**`saleor/graphql/payment/tests/test_utils.py`**

- `test_no_reference_type_configured_no_reference_id_provided` (function) — [saleor/graphql/payment/tests/test_utils.py:12]
- `test_no_reference_type_configured_reference_id_provided_raises_invalid` (function) — [saleor/graphql/payment/tests/test_utils.py:26]
- `test_reference_type_configured_no_reference_id_user_requestor_raises_required` (function) — [saleor/graphql/payment/tests/test_utils.py:48]
- `test_reference_type_configured_no_reference_id_app_requestor_success` (function) — [saleor/graphql/payment/tests/test_utils.py:72]
- `test_reference_type_configured_reference_id_provided_success` (function) — [saleor/graphql/payment/tests/test_utils.py:91]
- `test_reference_type_configured_reference_id_provided_app_requestor_success` (function) — [saleor/graphql/payment/tests/test_utils.py:110]
- `test_custom_field_name_in_error_message` (function) — [saleor/graphql/payment/tests/test_utils.py:129]
- `test_custom_field_name_in_required_error_message` (function) — [saleor/graphql/payment/tests/test_utils.py:151]
- `test_different_error_code_enum` (function) — [saleor/graphql/payment/tests/test_utils.py:175]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/payment/tests/__init__.py` (1 lines)
- `saleor/graphql/payment/tests/benchmark/__init__.py` (1 lines)
- `saleor/graphql/payment/tests/benchmark/test_payment_transactions.py` (78 lines)
- `saleor/graphql/payment/tests/deprecated/__init__.py` (1 lines)
- `saleor/graphql/payment/tests/deprecated/test_checkout_payment_create.py` (138 lines)
- `saleor/graphql/payment/tests/test_legacy_api_deprecation.py` (167 lines)
- `saleor/graphql/payment/tests/test_utils.py` (192 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....checkout.calculations`
- `.....checkout.fetch.fetch_checkout_info`
- `.....checkout.fetch.fetch_checkout_lines`
- `.....payment.error_codes.PaymentErrorCode`
- `.....payment.models.ChargeStatus`
- `.....payment.models.Payment`
- `.....payment.models.Transaction`
- `.....plugins.manager.get_plugins_manager`
- `....page.models.PageType`
- `....tests.utils.get_graphql_content`
- `...api.schema`
- `...schema_printer.print_type`
- `..utils.validate_reason_reference_context`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `b89220ca325f` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
