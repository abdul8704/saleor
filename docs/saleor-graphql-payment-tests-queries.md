## Purpose

`saleor/graphql/payment/tests/queries` (`saleor/graphql/payment/tests/queries`) groups 10 source file(s) exposing 93 top-level declaration(s).

## Public surface

**`saleor/graphql/payment/tests/queries/test_payment_capture.py`**

- `test_resolve_available_capture_amount_cannot_capture` (function) — [saleor/graphql/payment/tests/queries/test_payment_capture.py:17]
- `test_resolve_available_capture_amount` (function) — [saleor/graphql/payment/tests/queries/test_payment_capture.py:35]

**`saleor/graphql/payment/tests/queries/test_payment_refund.py`**

- `test_resolve_available_refund_amount_cannot_refund` (function) — [saleor/graphql/payment/tests/queries/test_payment_refund.py:20]
- `test_resolve_available_refund_amount` (function) — [saleor/graphql/payment/tests/queries/test_payment_refund.py:38]

**`saleor/graphql/payment/tests/queries/test_payment_sources.py`**

- `braintree_customer_id` (function) — [saleor/graphql/payment/tests/queries/test_payment_sources.py:14]
- `dummy_customer_id` (function) — [saleor/graphql/payment/tests/queries/test_payment_sources.py:19]
- `test_store_payment_gateway_meta` (function) — [saleor/graphql/payment/tests/queries/test_payment_sources.py:23]
- `token_config_with_customer` (function) — [saleor/graphql/payment/tests/queries/test_payment_sources.py:38]
- `set_braintree_customer_id` (function) — [saleor/graphql/payment/tests/queries/test_payment_sources.py:43]
- `set_dummy_customer_id` (function) — [saleor/graphql/payment/tests/queries/test_payment_sources.py:50]
- `test_list_payment_sources` (function) — [saleor/graphql/payment/tests/queries/test_payment_sources.py:56]
- `test_stored_payment_sources_restriction` (function) — [saleor/graphql/payment/tests/queries/test_payment_sources.py:121]

**`saleor/graphql/payment/tests/queries/test_payments_filter.py`**

- `test_query_payments_filter_by_checkout` (function) — [saleor/graphql/payment/tests/queries/test_payments_filter.py:37]
- `test_query_payments_filter_by_one_id` (function) — [saleor/graphql/payment/tests/queries/test_payments_filter.py:78]
- `test_query_payments_filter_by_multiple_ids` (function) — [saleor/graphql/payment/tests/queries/test_payments_filter.py:103]
- `test_query_payments_filter_by_empty_id_list` (function) — [saleor/graphql/payment/tests/queries/test_payments_filter.py:130]
- `test_query_payments_filter_by_not_existing_id` (function) — [saleor/graphql/payment/tests/queries/test_payments_filter.py:152]

**`saleor/graphql/payment/tests/queries/test_payments_query.py`**

- `payments_in_different_channels` (function) — [saleor/graphql/payment/tests/queries/test_payments_query.py:18]
- `test_payments_query` (function) — [saleor/graphql/payment/tests/queries/test_payments_query.py:65]
- `test_query_payments` (function) — [saleor/graphql/payment/tests/queries/test_payments_query.py:97]
- `test_query_payments_failed_payment` (function) — [saleor/graphql/payment/tests/queries/test_payments_query.py:115]
- `test_query_payments_by_user_with_access_to_all_channels` (function) — [saleor/graphql/payment/tests/queries/test_payments_query.py:148]
- `test_query_payments_by_user_with_restricted_access_to_channels` (function) — [saleor/graphql/payment/tests/queries/test_payments_query.py:165]
- `test_query_payments_by_user_with_restricted_access_to_channels_no_acc_channels` (function) — [saleor/graphql/payment/tests/queries/test_payments_query.py:186]
- `test_query_payments_by_app` (function) — [saleor/graphql/payment/tests/queries/test_payments_query.py:203]
- `test_query_payments_by_customer` (function) — [saleor/graphql/payment/tests/queries/test_payments_query.py:217]
- `test_query_payment` (function) — [saleor/graphql/payment/tests/queries/test_payments_query.py:237]
- `test_query_payment_with_checkout` (function) — [saleor/graphql/payment/tests/queries/test_payments_query.py:257]
- `test_staff_query_payment_by_invalid_id` (function) — [saleor/graphql/payment/tests/queries/test_payments_query.py:282]
- `test_staff_query_payment_with_invalid_object_type` (function) — [saleor/graphql/payment/tests/queries/test_payments_query.py:301]

**`saleor/graphql/payment/tests/queries/test_transaction.py`**

- `test_transaction_created_by_app_query_by_app` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:161]
- `test_transaction_created_by_app_query_by_app_with_old_id` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:190]
- `test_transaction_created_with_old_id_for_new_transaction` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:221]
- `test_transaction_creted_by_app_query_no_order` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:241]
- `test_transaction_created_by_app_query_by_staff` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:273]
- `test_transaction_created_by_app_marked_to_remove` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:303]
- `test_transaction_create_by_app_query_no_permission` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:343]
- `test_transaction_created_by_user_query_by_app` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:360]
- `test_transaction_creted_by_user_query_no_order` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:394]
- `test_transaction_created_by_user_query_by_staff` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:431]
- `test_transaction_created_by_user_with_old_id` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:465]
- `test_transaction_create_by_user_query_no_permission` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:502]
- `test_transaction_by_user_with_manage_orders` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:519]
- `test_query_transaction_by_invalid_id` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:547]
- `test_transaction_with_pending_amount` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:578]
- `test_transaction_with_checkout` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:612]
- `test_transaction_event_by_user` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:648]
- `test_transaction_event_by_app` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:698]
- `test_transaction_event_by_reinstalled_app` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:750]
- `test_transaction_event_by_app_marked_to_remove` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:802]
- `test_transaction_query_by_app_with_payment_method_card` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:856]
- `test_transaction_query_by_staff_with_payment_method_card` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:896]
- `test_transaction_query_by_app_with_payment_method_other` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:936]
- `test_transaction_query_by_staff_with_payment_method_other` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:970]
- `test_transaction_query_by_app_with_payment_method_gift_card` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:998]
- `test_transaction_query_by_staff_with_payment_method_gift_card` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:1033]
- `test_transaction_query_with_saleor_gift_card_is_saleor_giftcard_true` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:1068]
- `test_transaction_event_with_reason_reference` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:1111]
- `test_transaction_event_without_reason_reference` (function) — [saleor/graphql/payment/tests/queries/test_transaction.py:1159]

**`saleor/graphql/payment/tests/queries/test_transactions_sorting.py`**

- `transactions_with_different_dates` (function) — [saleor/graphql/payment/tests/queries/test_transactions_sorting.py:25]
- `test_sort_by_created_at_asc` (function) — [saleor/graphql/payment/tests/queries/test_transactions_sorting.py:55]
- `test_sort_by_created_at_desc` (function) — [saleor/graphql/payment/tests/queries/test_transactions_sorting.py:81]
- `test_sort_by_modified_at_asc` (function) — [saleor/graphql/payment/tests/queries/test_transactions_sorting.py:107]
- `test_sort_by_modified_at_desc` (function) — [saleor/graphql/payment/tests/queries/test_transactions_sorting.py:133]

**`saleor/graphql/payment/tests/queries/test_transactions_where.py`**

- `test_transactions_query_filter_by_ids` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:25]
- `test_transactions_query_filter_by_ids_empty_values` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:68]
- `test_transactions_query_filter_by_psp_reference` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:99]
- `test_transactions_query_combined_filters` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:140]
- `test_transactions_query_filter_by_app_identifier` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:197]
- `test_transactions_query_filter_by_app_identifier_combined_with_psp_reference` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:246]
- `test_transactions_query_filter_respects_app_permissions` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:302]
- `test_filter_by_created_at_gte_and_lte` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:368]
- `test_filter_by_created_at_gte` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:422]
- `test_filter_by_created_at_lte` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:467]
- `test_filter_by_modified_at_gte_and_lte` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:512]
- `test_filter_by_modified_at_gte` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:562]
- `test_filter_by_modified_at_lte` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:599]
- `test_filter_by_created_at_combined_with_psp_reference` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:636]
- `test_filter_by_event_type_eq` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:697]
- `test_filter_by_event_type_one_of` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:772]
- `test_filter_by_event_created_at` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:862]
- `test_filter_by_event_type_and_created_at` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:935]
- `test_filter_by_events_empty_returns_none` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:1030]
- `test_filter_by_events_combined_with_psp_reference` (function) — [saleor/graphql/payment/tests/queries/test_transactions_where.py:1058]

**`saleor/graphql/payment/tests/queries/test_transactions.py`**

- `transactions_in_different_channels` (function) — [saleor/graphql/payment/tests/queries/test_transactions.py:8]
- `test_transactions_query_no_permission` (function) — [saleor/graphql/payment/tests/queries/test_transactions.py:62]
- `test_transactions_query_by_app_with_manage_orders_returns_all` (function) — [saleor/graphql/payment/tests/queries/test_transactions.py:75]
- `test_transactions_query_by_app_with_handle_payments_returns_only_own` (function) — [saleor/graphql/payment/tests/queries/test_transactions.py:94]
- `test_transactions_query_by_app_with_handle_payments_no_own_transactions` (function) — [saleor/graphql/payment/tests/queries/test_transactions.py:132]
- `test_transactions_query_by_app_with_both_permissions_returns_all` (function) — [saleor/graphql/payment/tests/queries/test_transactions.py:152]
- `test_transactions_query_with_manage_orders_permission` (function) — [saleor/graphql/payment/tests/queries/test_transactions.py:173]
- `test_transactions_query_filtered_by_accessible_channels_for_user` (function) — [saleor/graphql/payment/tests/queries/test_transactions.py:191]
- `test_transactions_query_by_user_with_no_channel_access` (function) — [saleor/graphql/payment/tests/queries/test_transactions.py:221]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/payment/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/payment/tests/queries/test_payment_capture.py` (50 lines)
- `saleor/graphql/payment/tests/queries/test_payment_refund.py` (53 lines)
- `saleor/graphql/payment/tests/queries/test_payment_sources.py` (154 lines)
- `saleor/graphql/payment/tests/queries/test_payments_filter.py` (168 lines)
- `saleor/graphql/payment/tests/queries/test_payments_query.py` (314 lines)
- `saleor/graphql/payment/tests/queries/test_transaction.py` (1195 lines)
- `saleor/graphql/payment/tests/queries/test_transactions_sorting.py` (156 lines)
- `saleor/graphql/payment/tests/queries/test_transactions_where.py` (1127 lines)
- `saleor/graphql/payment/tests/queries/test_transactions.py` (242 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....order.models.Order`
- `.....page.models.Page`
- `.....payment.PaymentMethodType`
- `.....payment.TransactionEventType`
- `.....payment.interface.CustomerSource`
- `.....payment.interface.PaymentMethodInfo`
- `.....payment.interface.TokenConfig`
- `.....payment.models.Payment`
- `.....payment.models.TransactionEvent`
- `.....payment.models.TransactionItem`
- `.....payment.utils.fetch_customer_id`
- `.....payment.utils.store_customer_id`
- `....core.utils.to_global_id_or_none`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `...enums.PaymentChargeStatusEnum`
- `...enums.TransactionActionEnum`
- `...sorters.TransactionSortField`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `5cf21ad16e2c` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
