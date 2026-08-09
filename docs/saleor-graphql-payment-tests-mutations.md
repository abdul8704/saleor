## Purpose

`saleor/graphql/payment/tests/mutations` (`saleor/graphql/payment/tests/mutations`) groups 21 source file(s) exposing 325 top-level declaration(s).

## Public surface

**`saleor/graphql/payment/tests/mutations/conftest.py`**

- `transaction_request_webhook` (function) — [saleor/graphql/payment/tests/mutations/conftest.py:7]

**`saleor/graphql/payment/tests/mutations/test_check_payment_balance.py`**

- `test_payment_check_balance_mutation_validate_gateway_does_not_exist` (function) — [saleor/graphql/payment/tests/mutations/test_check_payment_balance.py:24]
- `test_payment_check_balance_validate_not_supported_currency` (function) — [saleor/graphql/payment/tests/mutations/test_check_payment_balance.py:52]
- `test_payment_check_balance_validate_channel_does_not_exist` (function) — [saleor/graphql/payment/tests/mutations/test_check_payment_balance.py:80]
- `test_payment_check_balance_validate_channel_inactive` (function) — [saleor/graphql/payment/tests/mutations/test_check_payment_balance.py:108]
- `test_payment_check_balance_payment` (function) — [saleor/graphql/payment/tests/mutations/test_check_payment_balance.py:143]
- `test_payment_check_balance_balance_raises_error` (function) — [saleor/graphql/payment/tests/mutations/test_check_payment_balance.py:177]

**`saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py`**

- `test_checkout_add_payment_without_shipping_method_and_not_shipping_required` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:45]
- `test_checkout_add_payment_without_shipping_method_with_shipping_required` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:87]
- `test_checkout_add_payment_with_shipping_method_and_shipping_required` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:122]
- `test_checkout_add_payment` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:171]
- `test_checkout_add_payment_default_amount` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:220]
- `test_checkout_add_payment_bad_amount` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:256]
- `test_checkout_add_payment_no_checkout_email` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:291]
- `test_checkout_add_payment_not_supported_currency` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:331]
- `test_checkout_add_payment_not_existing_gateway` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:355]
- `test_checkout_add_payment_gateway_inactive` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:382]
- `test_use_checkout_billing_address_as_payment_billing` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:405]
- `test_create_payment_for_checkout_with_active_payments` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:450]
- `test_create_payment_with_store` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:508]
- `test_create_payment_with_store_as_none` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:541]
- `test_create_payment_with_metadata` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:578]
- `test_checkout_add_payment_no_variant_channel_listings` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:611]
- `test_checkout_add_payment_no_product_channel_listings` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:657]
- `test_checkout_add_payment_checkout_without_lines` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:703]
- `test_checkout_add_payment_run_multiple_times` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:745]
- `call_payment_create_mutation` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:769]
- `test_with_active_problems_flow` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:789]
- `test_checkout_payment_create_checkout_locked` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:820]
- `test_checkout_payment_create_checkout_locked_time_pass` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:860]
- `test_checkout_payment_create_is_not_allowed_when_checkout_has_transaction` (function) — [saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py:898]

**`saleor/graphql/payment/tests/mutations/test_payment_capture.py`**

- `test_payment_capture_success` (function) — [saleor/graphql/payment/tests/mutations/test_payment_capture.py:29]
- `test_payment_capture_success_by_user_no_channel_access` (function) — [saleor/graphql/payment/tests/mutations/test_payment_capture.py:54]
- `test_payment_capture_success_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_payment_capture.py:80]
- `test_payment_capture_with_invalid_argument` (function) — [saleor/graphql/payment/tests/mutations/test_payment_capture.py:106]
- `test_payment_capture_with_unauthorized_payment` (function) — [saleor/graphql/payment/tests/mutations/test_payment_capture.py:127]
- `test_payment_capture_gateway_error` (function) — [saleor/graphql/payment/tests/mutations/test_payment_capture.py:153]
- `test_payment_capture_gateway_declined_card_error` (function) — [saleor/graphql/payment/tests/mutations/test_payment_capture.py:185]
- `test_payment_capture_marks_checkout_search_index_dirty` (function) — [saleor/graphql/payment/tests/mutations/test_payment_capture.py:223]

**`saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize_tokenization.py`**

- `test_payment_gateway_initialize_tokenization` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize_tokenization.py:42]
- `test_payment_gateway_initialize_tokenization_called_by_anonymous_user` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize_tokenization.py:94]
- `test_payment_gateway_initialize_tokenization_called_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize_tokenization.py:118]
- `test_payment_gateway_initialize_tokenization_not_app_or_plugin_subscribed_to_event` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize_tokenization.py:142]
- `test_payment_gateway_initialize_tokenization_incorrect_channel` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize_tokenization.py:178]
- `test_payment_gateway_initialize_tokenization_failure_from_app` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize_tokenization.py:209]

**`saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py`**

- `test_for_checkout_without_payment_gateways` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:52]
- `test_for_checkout_transactions_limit_on_gateway_initialize` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:90]
- `test_for_order_without_payment_gateways` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:124]
- `test_for_checkout_with_payment_gateways` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:159]
- `test_for_order_with_payment_gateways` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:213]
- `test_for_checkout_with_payment_gateways_and_amount` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:262]
- `test_for_order_with_payment_gateways_and_amount` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:313]
- `test_for_checkout_with_payment_gateways_returns_error` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:362]
- `test_for_order_with_payment_gateways_returns_error` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:421]
- `test_for_checkout_with_missing_payment_gateway` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:479]
- `test_for_order_with_missing_payment_gateway` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:536]
- `test_for_checkout_with_multiple_payment_gateways` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:592]
- `test_for_order_with_multiple_payment_gateways` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:698]
- `test_with_payment_gateways_and_amount_with_lot_of_decimal_places` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:804]
- `test_for_checkout_with_shipping_app` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:854]
- `test_for_checkout_with_tax_app` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:959]
- `test_for_order_with_tax_app` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:1042]
- `test_with_mutiple_payment_gateways_have_different_recipments` (function) — [saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py:1126]

**`saleor/graphql/payment/tests/mutations/test_payment_initialize.py`**

- `test_payment_initialize` (function) — [saleor/graphql/payment/tests/mutations/test_payment_initialize.py:29]
- `test_payment_initialize_gateway_doesnt_exist` (function) — [saleor/graphql/payment/tests/mutations/test_payment_initialize.py:65]
- `test_payment_initialize_plugin_raises_error` (function) — [saleor/graphql/payment/tests/mutations/test_payment_initialize.py:85]

**`saleor/graphql/payment/tests/mutations/test_payment_method_initialize_tokenization.py`**

- `test_payment_method_initialize_tokenization` (function) — [saleor/graphql/payment/tests/mutations/test_payment_method_initialize_tokenization.py:48]
- `test_payment_method_initialize_tokenization_called_by_anonymous_user` (function) — [saleor/graphql/payment/tests/mutations/test_payment_method_initialize_tokenization.py:105]
- `test_payment_method_initialize_tokenization_called_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_payment_method_initialize_tokenization.py:133]
- `test_payment_method_initialize_tokenization_not_app_or_plugin_subscribed_to_event` (function) — [saleor/graphql/payment/tests/mutations/test_payment_method_initialize_tokenization.py:161]
- `test_payment_method_initialize_tokenization_incorrect_channel` (function) — [saleor/graphql/payment/tests/mutations/test_payment_method_initialize_tokenization.py:201]
- `test_payment_method_initialize_tokenization_failure_from_app` (function) — [saleor/graphql/payment/tests/mutations/test_payment_method_initialize_tokenization.py:236]

**`saleor/graphql/payment/tests/mutations/test_payment_method_process_tokenization.py`**

- `test_payment_method_process_tokenization` (function) — [saleor/graphql/payment/tests/mutations/test_payment_method_process_tokenization.py:43]
- `test_payment_method_process_tokenization_called_by_anonymous_user` (function) — [saleor/graphql/payment/tests/mutations/test_payment_method_process_tokenization.py:100]
- `test_payment_method_process_tokenization_called_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_payment_method_process_tokenization.py:125]
- `test_payment_method_process_tokenization_not_app_or_plugin_subscribed_to_event` (function) — [saleor/graphql/payment/tests/mutations/test_payment_method_process_tokenization.py:150]
- `test_payment_method_process_tokenization_incorrect_channel` (function) — [saleor/graphql/payment/tests/mutations/test_payment_method_process_tokenization.py:187]
- `test_payment_method_process_tokenization_failure_from_app` (function) — [saleor/graphql/payment/tests/mutations/test_payment_method_process_tokenization.py:219]

**`saleor/graphql/payment/tests/mutations/test_payment_refund.py`**

- `test_payment_refund_success` (function) — [saleor/graphql/payment/tests/mutations/test_payment_refund.py:30]
- `test_payment_refund_success_by_user_no_channel_access` (function) — [saleor/graphql/payment/tests/mutations/test_payment_refund.py:68]
- `test_payment_refund_success_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_payment_refund.py:99]
- `test_payment_refund_with_invalid_argument` (function) — [saleor/graphql/payment/tests/mutations/test_payment_refund.py:139]
- `test_payment_refund_error` (function) — [saleor/graphql/payment/tests/mutations/test_payment_refund.py:174]

**`saleor/graphql/payment/tests/mutations/test_payment_void.py`**

- `test_payment_void_success` (function) — [saleor/graphql/payment/tests/mutations/test_payment_void.py:23]
- `test_payment_void_success_by_user_no_channel_access` (function) — [saleor/graphql/payment/tests/mutations/test_payment_void.py:46]
- `test_payment_void_success_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_payment_void.py:70]
- `test_payment_void_gateway_error` (function) — [saleor/graphql/payment/tests/mutations/test_payment_void.py:94]
- `test_payment_void_marks_checkout_search_index_dirty` (function) — [saleor/graphql/payment/tests/mutations/test_payment_void.py:124]

**`saleor/graphql/payment/tests/mutations/test_stored_payment_method_request_delete.py`**

- `test_stored_payment_method_request_delete` (function) — [saleor/graphql/payment/tests/mutations/test_stored_payment_method_request_delete.py:29]
- `test_stored_payment_method_request_delete_app_returned_failure_event` (function) — [saleor/graphql/payment/tests/mutations/test_stored_payment_method_request_delete.py:72]
- `test_stored_payment_method_request_delete_called_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_stored_payment_method_request_delete.py:120]
- `test_stored_payment_method_request_delete_called_by_anonymous_user` (function) — [saleor/graphql/payment/tests/mutations/test_stored_payment_method_request_delete.py:150]
- `test_stored_payment_method_request_delete_not_app_or_plugin_subscribed_to_event` (function) — [saleor/graphql/payment/tests/mutations/test_stored_payment_method_request_delete.py:180]
- `test_stored_payment_method_request_delete_incorrect_channel` (function) — [saleor/graphql/payment/tests/mutations/test_stored_payment_method_request_delete.py:222]

**`saleor/graphql/payment/tests/mutations/test_transaction_create.py`**

- `test_transaction_create_updates_order_authorize_amounts` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:116]
- `test_transaction_create_for_order_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:159]
- `test_transaction_create_for_order_by_app_metadata_null_value` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:220]
- `test_transaction_create_for_order_updates_order_total_authorized_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:277]
- `test_transaction_create_for_order_updates_order_total_charged_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:323]
- `test_transaction_create_for_draft_order` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:369]
- `test_transaction_create_for_checkout_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:425]
- `test_transaction_create_for_checkout_by_app_metadata_null_value` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:490]
- `test_transaction_create_calculate_amount_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:560]
- `test_transaction_create_multiple_amounts_provided_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:597]
- `test_transaction_create_create_event_for_order_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:659]
- `test_transaction_create_missing_permission_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:705]
- `test_transaction_create_incorrect_currency_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:747]
- `test_transaction_create_empty_metadata_key_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:786]
- `test_transaction_create_empty_private_metadata_key_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:827]
- `test_creates_transaction_event_for_order_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:868]
- `test_creates_transaction_event_for_checkout_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:928]
- `test_transaction_create_for_order_by_staff` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:989]
- `test_transaction_create_for_order_updates_order_total_authorized_by_staff` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1047]
- `test_transaction_create_for_order_updates_order_total_charged_by_staff` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1093]
- `test_transaction_create_for_checkout_by_staff` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1138]
- `test_transaction_create_for_checkout_fully_paid` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1202]
- `test_transaction_create_for_checkout_fully_authorized` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1262]
- `test_transaction_create_calculate_amount_by_staff` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1328]
- `test_transaction_create_multiple_amounts_provided_by_staff` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1365]
- `test_transaction_create_create_event_for_order_by_staff` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1427]
- `test_transaction_create_missing_permission_by_staff` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1472]
- `test_transaction_create_incorrect_currency_by_staff` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1516]
- `test_transaction_create_empty_metadata_key_by_staff` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1555]
- `test_transaction_create_empty_private_metadata_key_by_staff` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1596]
- `test_creates_transaction_event_for_order_by_staff` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1637]
- `test_creates_transaction_event_for_checkout_by_staff` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1697]
- `test_creates_transaction_automatically_confirm` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1764]
- `test_transaction_create_external_url_incorrect_url_format_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1813]
- `test_transaction_create_creates_calculation_events` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1856]
- `test_transaction_create_for_order_triggers_webhooks_when_fully_paid` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1943]
- `test_transaction_create_for_order_triggers_webhook_when_partially_paid` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:1991]
- `test_transaction_create_for_order_triggers_webhook_when_authorized` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:2032]
- `test_transaction_create_for_order_triggers_webhooks_when_fully_refunded` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:2072]
- `test_transaction_create_for_order_triggers_webhook_when_partially_refunded` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_create.py:2113]
- _…and 15 more in this file_

**`saleor/graphql/payment/tests/mutations/test_transaction_event_report.py`**

- `test_transaction_event_report_by_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:111]
- `test_transaction_event_report_by_app_via_token` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:190]
- `test_transaction_event_report_by_user` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:268]
- `test_transaction_event_report_by_another_user` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:344]
- `test_transaction_event_report_amount_with_lot_of_decimal_places` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:417]
- `test_transaction_event_report_no_permission` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:496]
- `test_transaction_event_report_called_by_non_app_owner` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:540]
- `test_transaction_event_report_called_by_non_user_owner` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:591]
- `test_transaction_event_report_event_already_exists` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:633]
- `test_transaction_event_report_event_already_exists_updates_available_actions` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:711]
- `test_event_already_exists_do_not_overwrite_actions_when_not_provided_in_input` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:788]
- `test_transaction_event_report_incorrect_amount_for_already_existing` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:866]
- `test_transaction_event_report_calls_amount_recalculations` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:952]
- `test_transaction_event_updates_order_total_charged` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:1015]
- `test_transaction_event_updates_order_total_authorized` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:1072]
- `test_transaction_event_updates_search_vector` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:1128]
- `test_transaction_event_report_authorize_event_already_exists` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:1183]
- `test_transaction_event_updates_checkout_payment_statuses` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:1263]
- `test_transaction_event_updates_checkout_last_transaction_modified_at` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:1336]
- `test_transaction_event_updates_checkout_search_index_dirty_flag` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:1399]
- `test_transaction_event_updates_checkout_full_paid_with_charged_amount` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:1457]
- `test_transaction_event_updates_checkout_full_paid_with_pending_charge_amount` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:1527]
- `test_transaction_event_updates_checkout_fully_authorized` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:1596]
- `test_transaction_event_report_with_info_event` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:1665]
- `test_transaction_event_report_accepts_old_id_for_old_transaction` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:1738]
- `test_transaction_event_report_doesnt_accept_old_id_for_new_transaction` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:1817]
- `test_transaction_event_report_for_order_triggers_webhooks_when_fully_paid` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:1898]
- `test_transaction_event_report_for_draft_order_does_not_trigger_webhooks_when_fully_paid` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:1965]
- `test_transaction_event_report_for_order_triggers_webhooks_when_partially_paid` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:2026]
- `test_transaction_event_report_for_order_triggers_webhooks_when_partially_authorized` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:2081]
- `test_transaction_event_report_for_order_triggers_webhooks_when_fully_authorized` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:2136]
- `test_transaction_event_report_for_order_triggers_webhooks_when_fully_refunded` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:2192]
- `test_transaction_event_report_for_order_triggers_webhooks_when_partially_refunded` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:2249]
- `test_transaction_event_report_by_app_assign_app_owner` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:2303]
- `test_transaction_event_report_assign_transaction_psp_reference_if_missing` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:2380]
- `test_transaction_event_report_updates_granted_refund_status_when_needed` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:2444]
- `test_transaction_event_report_missing_amount` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:2513]
- `test_transaction_event_report_missing_amount_not_deduced_error_raised` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:2603]
- `test_transaction_event_report_missing_amount_error_raised` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:2661]
- `test_transaction_event_report_update_transaction_metadata` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_event_report.py:2732]
- _…and 19 more in this file_

**`saleor/graphql/payment/tests/mutations/test_transaction_initialize.py`**

- `test_for_checkout_without_payment_gateway_data` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:227]
- `test_for_checkout_transactions_limit_on_transaction_initialize` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:278]
- `test_for_checkout_with_idempotency_key` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:314]
- `test_for_checkout_amount_with_lot_of_decimal_places` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:368]
- `test_for_checkout_with_multiple_calls_and_idempotency_key` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:433]
- `test_for_order_with_multiple_calls_and_idempotency_key` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:490]
- `test_for_order_with_idempotency_key` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:547]
- `test_for_order_without_payment_gateway_data` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:601]
- `test_checkout_with_pending_amount` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:652]
- `test_order_with_pending_amount` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:704]
- `test_checkout_with_action_required_response` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:757]
- `test_order_with_action_required_response` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:807]
- `test_checkout_with_action_required_response_and_missing_psp_reference` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:858]
- `test_order_with_action_required_response_and_missing_psp_reference` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:907]
- `test_checkout_when_amount_is_not_provided` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:957]
- `test_order_when_amount_is_not_provided` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1014]
- `test_order_status_with_order_confirmation` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1073]
- `test_draft_order_status_with_order_confirmation` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1137]
- `test_order_with_transaction_when_amount_is_not_provided` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1195]
- `test_checkout_with_transaction_when_amount_is_not_provided` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1257]
- `test_app_with_action_field_and_handle_payments` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1326]
- `test_uses_default_channel_action` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1389]
- `test_transaction_initialize_for_already_used_idempotency_key` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1443]
- `test_transaction_initialize_for_already_used_idempotency_key_and_different_input` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1493]
- `test_transaction_initialize_for_empty_string_as_idempotency_key` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1559]
- `test_transaction_initialize_for_removed_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1605]
- `test_transaction_initialize_for_disabled_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1637]
- `test_app_with_action_field` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1670]
- `test_customer_with_action_field` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1716]
- `test_incorrect_source_object_id` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1749]
- `test_checkout_doesnt_exist` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1788]
- `test_order_doesnt_exists` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1822]
- `test_checkout_fully_paid` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1862]
- `test_checkout_fully_paid_pending_charge` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1916]
- `test_checkout_fully_authorized` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:1976]
- `test_checkout_fully_authorized_pending_authorization` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:2030]
- `test_user_missing_permission_for_customer_ip_address` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:2084]
- `test_app_missing_permission_for_customer_ip_address` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:2112]
- `test_with_customer_ip_address` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:2141]
- `test_sets_customer_ip_address_when_not_provided` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_initialize.py:2199]
- _…and 30 more in this file_

**`saleor/graphql/payment/tests/mutations/test_transaction_process.py`**

- `test_for_checkout_without_data` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:257]
- `test_for_order_without_data` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:320]
- `test_order_status_with_order_confirmation` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:385]
- `test_draft_order_status_with_order_confirmation` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:453]
- `test_for_checkout_with_data` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:516]
- `test_for_checkout_with_data_via_token` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:579]
- `test_for_order_with_data` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:645]
- `test_checkout_with_pending_amount` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:704]
- `test_order_with_pending_amount` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:766]
- `test_checkout_with_action_required_response` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:823]
- `test_order_with_action_required_response` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:883]
- `test_transaction_already_processed` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:937]
- `test_request_event_is_missing` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:976]
- `test_transaction_doesnt_have_source_object` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1011]
- `test_transaction_doesnt_have_app_identifier` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1049]
- `test_app_attached_to_transaction_doesnt_exist` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1082]
- `test_checkout_fully_paid` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1130]
- `test_checkout_fully_paid_pending` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1198]
- `test_checkout_fully_authorized` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1273]
- `test_checkout_fully_authorized_pending` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1341]
- `test_transaction_process_doesnt_accept_old_id` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1406]
- `test_transaction_process_for_removed_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1440]
- `test_user_missing_permission_for_customer_ip_address` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1479]
- `test_app_missing_permission_for_customer_ip_address` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1518]
- `test_with_customer_ip_address` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1558]
- `test_sets_customer_ip_address_when_not_provided` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1621]
- `test_customer_ip_address_wrong_format` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1684]
- `test_customer_ip_address_ipv6` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1729]
- `test_transaction_process_for_disabled_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1791]
- `test_updates_checkout_last_transaction_modified_at` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1838]
- `test_for_locked_checkout` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1904]
- `test_for_checkout_with_payments` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:1963]
- `test_for_checkout_with_payments_transaction_process_failure` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:2041]
- `test_for_order_too_long_message_in_response` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:2115]
- `test_for_order_empty_message` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:2180]
- `test_for_checkout_with_shipping_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:2242]
- `test_for_checkout_with_tax_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:2320]
- `test_for_order_with_tax_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:2380]
- `test_lock_order_during_updating_order_amounts` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:2449]
- `test_lock_checkout_during_updating_checkout_amounts` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_process.py:2524]
- _…and 6 more in this file_

**`saleor/graphql/payment/tests/mutations/test_transaction_request_refund_for_granted_refund.py`**

- `test_missing_permission_for_app` (function) — [saleor/graphql/payment/tests/mutations/test_transaction_request_refund_for_granted_refund.py:63]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/payment/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/payment/tests/mutations/conftest.py` (18 lines)
- `saleor/graphql/payment/tests/mutations/test_check_payment_balance.py` (214 lines)
- `saleor/graphql/payment/tests/mutations/test_checkout_payment_create.py` (937 lines)
- `saleor/graphql/payment/tests/mutations/test_payment_capture.py` (253 lines)
- `saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize_tokenization.py` (260 lines)
- `saleor/graphql/payment/tests/mutations/test_payment_gateway_initialize.py` (1235 lines)
- `saleor/graphql/payment/tests/mutations/test_payment_initialize.py` (111 lines)
- `saleor/graphql/payment/tests/mutations/test_payment_method_initialize_tokenization.py` (288 lines)
- `saleor/graphql/payment/tests/mutations/test_payment_method_process_tokenization.py` (268 lines)
- `saleor/graphql/payment/tests/mutations/test_payment_refund.py` (218 lines)
- `saleor/graphql/payment/tests/mutations/test_payment_void.py` (154 lines)
- `saleor/graphql/payment/tests/mutations/test_stored_payment_method_request_delete.py` (256 lines)
- `saleor/graphql/payment/tests/mutations/test_transaction_create.py` (2893 lines)
- `saleor/graphql/payment/tests/mutations/test_transaction_event_report.py` (4159 lines)
- `saleor/graphql/payment/tests/mutations/test_transaction_initialize.py` (3999 lines)
- `saleor/graphql/payment/tests/mutations/test_transaction_process.py` (2993 lines)
- `saleor/graphql/payment/tests/mutations/test_transaction_request_action_reason.py` (78 lines)
- `saleor/graphql/payment/tests/mutations/test_transaction_request_action.py` (71 lines)
- `saleor/graphql/payment/tests/mutations/test_transaction_request_refund_for_granted_refund.py` (79 lines)
- `saleor/graphql/payment/tests/mutations/test_transaction_update.py` (59 lines)

## Interactions

- Imports from: `saleor/graphql/payment/mutations/payment`, `saleor/plugins/tests`, `saleor/graphql/payment/mutations/transaction`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....app.models.App`
- `.....channel.TransactionFlowStrategy`
- `.....checkout.CheckoutAuthorizeStatus`
- `.....checkout.CheckoutChargeStatus`
- `.....checkout.calculations`
- `.....checkout.calculations.fetch_checkout_data`
- `.....checkout.complete_checkout.create_order_from_checkout`
- `.....checkout.error_codes.CheckoutErrorCode`
- `.....checkout.fetch.fetch_checkout_info`
- `.....checkout.fetch.fetch_checkout_lines`
- `.....checkout.models.Checkout`
- `.....checkout.payment_utils.update_checkout_payment_statuses`
- `.....checkout.tests.utils.add_variant_to_checkout`
- `.....core.EventDeliveryStatus`
- `.....core.prices.Money`
- `.....core.prices.quantize_price`
- `.....giftcard.GiftCardEvents`
- `.....giftcard.const.GIFT_CARD_PAYMENT_GATEWAY_ID`
- `.....giftcard.models.GiftCardEvent`
- `.....order.OrderAuthorizeStatus`
- `.....order.OrderChargeStatus`
- `.....order.OrderEvents`
- `.....order.OrderGrantedRefundStatus`
- `.....order.OrderStatus`
- `.....order.models.Order`
- `.....order.utils.update_order_authorize_data`
- `.....order.utils.update_order_charge_data`
- `.....page.models.Page`
- `.....page.models.PageType`
- `.....payment.ChargeStatus`
- `.....payment.FAILED_TRANSACTION_EVENTS`
- `.....payment.OPTIONAL_AMOUNT_EVENTS`
- `.....payment.PaymentError`
- `.....payment.PaymentMethodType`
- `.....payment.StorePaymentMethod`
- `.....payment.TokenizedPaymentFlow`
- `.....payment.TransactionAction`
- `.....payment.TransactionEventType`
- `.....payment.TransactionKind`
- `.....payment.error_codes.PaymentErrorCode`
- `.....payment.error_codes.TransactionCreateErrorCode`
- `.....payment.error_codes.TransactionUpdateErrorCode`
- `.....payment.interface.InitializedPaymentResponse`
- `.....payment.interface.PaymentGatewayData`
- `.....payment.interface.StorePaymentMethodEnum`
- `.....payment.interface.TransactionActionData`
- `.....payment.models.ChargeStatus`
- `.....payment.models.Payment`
- `.....payment.models.TransactionEvent`
- `.....payment.models.TransactionItem`
- `.....payment.transaction_item_calculations.recalculate_transaction_amounts`
- `.....plugins.manager.PluginsManager`
- `.....plugins.manager.get_plugins_manager`
- `.....tests.e2e.utils.assign_permissions`
- `.....tests.race_condition`
- `.....webhook.event_types.WebhookEventSyncType`
- `.....webhook.models.Webhook`
- `.....webhook.transport.utils.WebhookResponse`
- `.....webhook.transport.utils.generate_cache_key_for_webhook`
- `.....webhook.transport.utils.to_payment_app_id`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `f5b0746f7031` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
