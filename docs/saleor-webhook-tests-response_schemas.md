## Purpose

`saleor/webhook/tests/response_schemas` (`saleor/webhook/tests/response_schemas`) groups 7 source file(s) exposing 83 top-level declaration(s).

## Public surface

**`saleor/webhook/tests/response_schemas/test_helpers.py`**

- `ExampleSchema` (class) — [saleor/webhook/tests/response_schemas/test_helpers.py:6]
- `test_parse_validation_error_single_error` (function) — [saleor/webhook/tests/response_schemas/test_helpers.py:11]
- `test_parse_validation_error_multiple_errors` (function) — [saleor/webhook/tests/response_schemas/test_helpers.py:27]
- `test_parse_validation_error_missing_field_value` (function) — [saleor/webhook/tests/response_schemas/test_helpers.py:44]

**`saleor/webhook/tests/response_schemas/test_payment.py`**

- `test_credit_card_info_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:61]
- `NonParsableObject` (class) — [saleor/webhook/tests/response_schemas/test_payment.py:74]
- `test_credit_card_info_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:199]
- `test_credit_card_info_schema_required_field_is_none` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:218]
- `test_stored_payment_method_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:278]
- `test_stored_payment_method_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:345]
- `test_stored_payment_method_schema_invalid_credit_card_info_skipped` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:356]
- `test_list_stored_payment_methods_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:434]
- `test_list_stored_payment_methods_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:448]
- `test_list_stored_payment_methods_schema_invalid_element_skipped` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:457]
- `test_stored_payment_method_delete_requested_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:514]
- `test_stored_payment_method_delete_requested_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:559]
- `test_payment_gateway_initialize_tokenization_session_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:606]
- `test_payment_gateway_initialize_tokenization_session_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:661]
- `test_payment_method_tokenization_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:689]
- `test_payment_method_tokenization_schema_valid_extra_data_in_input` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:701]
- `test_payment_method_tokenization_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:761]
- `test_payment_method_tokenization_pending_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:795]
- `test_payment_method_tokenization_pending_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:838]
- `test_payment_method_tokenization_failed_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:872]
- `test_payment_method_tokenization_failed_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_payment.py:909]

**`saleor/webhook/tests/response_schemas/test_shipping.py`**

- `decode_id` (function) — [saleor/webhook/tests/response_schemas/test_shipping.py:20]
- `test_shipping_method_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_shipping.py:100]
- `test_shipping_method_schema_invalid_metadata_skipped` (function) — [saleor/webhook/tests/response_schemas/test_shipping.py:127]
- `test_shipping_method_schema_invalid_private_metadata_skipped` (function) — [saleor/webhook/tests/response_schemas/test_shipping.py:156]
- `test_shipping_method_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_shipping.py:318]
- `test_list_shipping_methods_schema_skipped_values` (function) — [saleor/webhook/tests/response_schemas/test_shipping.py:329]
- `test_list_shipping_methods_schema_invalid_element_skipped` (function) — [saleor/webhook/tests/response_schemas/test_shipping.py:340]
- `test_excluded_shipping_method_schema_valid_external_method` (function) — [saleor/webhook/tests/response_schemas/test_shipping.py:388]
- `test_excluded_shipping_method_schema_valid_shipping_method` (function) — [saleor/webhook/tests/response_schemas/test_shipping.py:408]
- `test_excluded_shipping_method_schema_invalid_id` (function) — [saleor/webhook/tests/response_schemas/test_shipping.py:426]
- `test_filter_shipping_methods_schema_skipped_values` (function) — [saleor/webhook/tests/response_schemas/test_shipping.py:439]
- `test_filter_shipping_methods_schema_invalid_element_skipped` (function) — [saleor/webhook/tests/response_schemas/test_shipping.py:451]

**`saleor/webhook/tests/response_schemas/test_taxes.py`**

- `test_line_calculate_taxes_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_taxes.py:45]
- `test_line_calculate_taxes_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_taxes.py:96]
- `test_calculate_taxes_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_taxes.py:144]
- `test_calculate_taxes_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_taxes.py:253]
- `test_calculate_taxes_schema_missing_context` (function) — [saleor/webhook/tests/response_schemas/test_taxes.py:263]

**`saleor/webhook/tests/response_schemas/test_transaction.py`**

- `test_transaction_schema_valid_full_data` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:30]
- `test_transaction_schema_valid_only_required_fields` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:76]
- `test_transaction_schema_with_various_amount_types` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:94]
- `test_transaction_schema_time_valid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:130]
- `test_transaction_schema_actions_validation` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:184]
- `test_transaction_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:233]
- `test_transaction_charge_requested_sync_success_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:243]
- `test_transaction_charge_requested_sync_success_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:272]
- `test_transaction_charge_requested_sync_failure_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:289]
- `test_transaction_charge_requested_sync_failure_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:318]
- `test_transaction_charge_requested_async_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:335]
- `test_transaction_charge_requested_async_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:349]
- `test_transaction_cancel_requested_sync_success_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:365]
- `test_transaction_cancel_requested_sync_success_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:394]
- `test_transaction_cancel_requested_sync_failure_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:411]
- `test_transaction_cancel_requested_sync_failure_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:440]
- `test_transaction_cancel_requested_async_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:457]
- `test_transaction_cancel_requested_async_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:471]
- `test_transaction_refund_requested_sync_success_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:487]
- `test_transaction_refund_requested_sync_success_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:516]
- `test_transaction_refund_requested_sync_failure_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:533]
- `test_transaction_refund_requested_sync_failure_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:562]
- `test_transaction_refund_requested_async_schema_valid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:579]
- `test_transaction_refund_requested_async_schema_invalid` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:593]
- `test_transaction_session_action_required_schema_valid_result` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:616]
- `test_transaction_session_action_required_schema_valid_payment_method_details` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:676]
- `test_transaction_session_action_required_schema_invalid_payment_method_details` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:740]
- `test_transaction_session_action_required_schema_invalid_result` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:770]
- `test_transaction_session_success_schema_valid_result` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:797]
- `test_transaction_session_success_schema_valid_payment_method_details` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:859]
- `test_transaction_session_success_schema_invalid_payment_method_details` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:923]
- `test_transaction_session_success_schema_invalid_result` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:951]
- `test_transaction_session_failure_schema_valid_result` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:976]
- `test_transaction_session_failure_schema_valid_payment_method_details` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:1036]
- `test_transaction_session_failure_schema_invalid_payment_method_details` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:1101]
- `test_transaction_session_failure_schema_invalid_result` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:1131]
- `test_transaction_session_base_schema_valid_data` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:1170]
- `test_transaction_session_base_schema_invalid_data` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:1199]
- `test_payment_gateway_initialize_schema_valid_data` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:1238]
- `test_payment_gateway_initialize_schema_invalid_data` (function) — [saleor/webhook/tests/response_schemas/test_transaction.py:1264]

**`saleor/webhook/tests/response_schemas/test_validators.py`**

- `test_lower_values` (function) — [saleor/webhook/tests/response_schemas/test_validators.py:18]

## How it works

The module's files, as provided to this run:

- `saleor/webhook/tests/response_schemas/__init__.py` (1 lines)
- `saleor/webhook/tests/response_schemas/test_helpers.py` (55 lines)
- `saleor/webhook/tests/response_schemas/test_payment.py` (916 lines)
- `saleor/webhook/tests/response_schemas/test_shipping.py` (487 lines)
- `saleor/webhook/tests/response_schemas/test_taxes.py` (270 lines)
- `saleor/webhook/tests/response_schemas/test_transaction.py` (1276 lines)
- `saleor/webhook/tests/response_schemas/test_validators.py` (19 lines)

## Interactions

- Imports from: `saleor/webhook/response_schemas`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....core.prices.MAXIMUM_PRICE`
- `....payment.TransactionAction`
- `....payment.TransactionEventType`
- `...response_schemas.taxes.CalculateTaxesSchema`
- `...response_schemas.taxes.LineCalculateTaxesSchema`
- `...response_schemas.utils.annotations.logger`
- `...response_schemas.utils.helpers.parse_validation_error`
- `...transport.shipping_helpers.to_shipping_app_id`
- `...transport.utils.to_payment_app_id`
- `saleor.webhook.response_schemas.utils.validators.lower_values`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `9f4b2c5ac25b` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
