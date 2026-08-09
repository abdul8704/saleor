## Purpose

`saleor/checkout/tests` (`saleor/checkout/tests`) groups 21 source file(s) exposing 395 top-level declaration(s).

## Public surface

**`saleor/checkout/tests/test_actions.py`**

- `test_transaction_amounts_for_checkout_updated_fully_paid` (function) — [saleor/checkout/tests/test_actions.py:28]
- `test_transaction_amounts_for_checkout_updated_not_fully_paid_no_automatic_complete` (function) — [saleor/checkout/tests/test_actions.py:67]
- `test_transaction_amounts_for_checkout_updated_with_already_fully_paid` (function) — [saleor/checkout/tests/test_actions.py:109]
- `test_transaction_amounts_for_checkout_updated_with_already_fully_authorized` (function) — [saleor/checkout/tests/test_actions.py:155]
- `test_transaction_amounts_for_checkout_updated_fully_authorized` (function) — [saleor/checkout/tests/test_actions.py:211]
- `test_transaction_amounts_for_checkout_updated_updates_last_transaction_modified_at` (function) — [saleor/checkout/tests/test_actions.py:253]
- `test_get_checkout_refundable_with_transaction_and_last_refund_success` (function) — [saleor/checkout/tests/test_actions.py:285]
- `test_get_checkout_refundable_with_transaction_and_last_refund_failure` (function) — [saleor/checkout/tests/test_actions.py:312]
- `test_get_checkout_refundable_with_transaction_without_funds` (function) — [saleor/checkout/tests/test_actions.py:341]
- `test_get_checkout_refundable_with_multiple_transactions_without_funds` (function) — [saleor/checkout/tests/test_actions.py:370]
- `test_get_checkout_refundable_with_multiple_transactions_with_failure_refund` (function) — [saleor/checkout/tests/test_actions.py:400]
- `test_get_checkout_refundable_with_multiple_active_transactions` (function) — [saleor/checkout/tests/test_actions.py:432]
- `test_call_checkout_event_incorrect_webhook_event` (function) — [saleor/checkout/tests/test_actions.py:473]
- `test_call_checkout_event_triggers_sync_webhook_when_needed` (function) — [saleor/checkout/tests/test_actions.py:513]
- `test_call_checkout_event_skips_tax_webhook_when_not_expired` (function) — [saleor/checkout/tests/test_actions.py:610]
- `test_call_checkout_event_skip_sync_webhooks_when_async_missing` (function) — [saleor/checkout/tests/test_actions.py:699]
- `test_call_checkout_event_only_async_when_sync_missing` (function) — [saleor/checkout/tests/test_actions.py:736]
- `test_call_checkout_info_event_incorrect_webhook_event` (function) — [saleor/checkout/tests/test_actions.py:783]
- `test_call_checkout_info_event_triggers_sync_webhook_when_needed` (function) — [saleor/checkout/tests/test_actions.py:832]
- `test_call_checkout_info_event_skips_tax_webhook_when_not_expired` (function) — [saleor/checkout/tests/test_actions.py:941]
- `test_call_checkout_info_event_only_async_when_sync_missing` (function) — [saleor/checkout/tests/test_actions.py:1041]
- `test_call_checkout_info_event_skip_sync_webhooks_when_async_missing` (function) — [saleor/checkout/tests/test_actions.py:1099]
- `test_transaction_amounts_for_checkout_fully_paid_triggers_sync_webhook` (function) — [saleor/checkout/tests/test_actions.py:1151]
- `test_transaction_amounts_for_checkout_fully_authorized_triggers_sync_webhook` (function) — [saleor/checkout/tests/test_actions.py:1263]
- `test_call_checkout_events_incorrect_webhook_event` (function) — [saleor/checkout/tests/test_actions.py:1374]
- `test_call_checkout_events_triggers_sync_webhook_when_needed` (function) — [saleor/checkout/tests/test_actions.py:1414]
- `test_call_checkout_events_skips_tax_webhook_when_not_expired` (function) — [saleor/checkout/tests/test_actions.py:1515]
- `test_call_checkout_events_skip_sync_webhooks_when_async_missing` (function) — [saleor/checkout/tests/test_actions.py:1606]
- `test_call_checkout_events_only_async_when_sync_missing` (function) — [saleor/checkout/tests/test_actions.py:1647]
- `test_transaction_amounts_for_checkout_updated_without_price_recalculation_considers_gift_cards_balance_when_updating_checkout_payment_status` (function) — [saleor/checkout/tests/test_actions.py:1701]

**`saleor/checkout/tests/test_associate_checkout_with_account.py`**

- `test_associate_guest_checkout_with_account_if_exists` (function) — [saleor/checkout/tests/test_associate_checkout_with_account.py:18]
- `test_associate_guest_checkout_with_account_if_exists_with_guest_user` (function) — [saleor/checkout/tests/test_associate_checkout_with_account.py:53]
- `test_associate_guest_checkout_with_account_if_exists_with_inactive_user` (function) — [saleor/checkout/tests/test_associate_checkout_with_account.py:91]

**`saleor/checkout/tests/test_autodocs_probe.py`**

- `test_autodocs_probe` (function) — [saleor/checkout/tests/test_autodocs_probe.py:5]

**`saleor/checkout/tests/test_base_calculations.py`**

- `test_calculate_base_line_unit_price` (function) — [saleor/checkout/tests/test_base_calculations.py:18]
- `test_calculate_base_line_unit_price_with_custom_price` (function) — [saleor/checkout/tests/test_base_calculations.py:35]
- `test_calculate_base_line_unit_price_with_variant_on_promotion` (function) — [saleor/checkout/tests/test_base_calculations.py:55]
- `test_calculate_base_line_unit_price_with_variant_on_promotion_custom_price` (function) — [saleor/checkout/tests/test_base_calculations.py:70]
- `test_calculate_base_line_unit_price_with_fixed_voucher` (function) — [saleor/checkout/tests/test_base_calculations.py:92]
- `test_calculate_base_line_unit_price_with_fixed_voucher_custom_prices` (function) — [saleor/checkout/tests/test_base_calculations.py:123]
- `test_calculate_base_line_unit_price_with_percentage_voucher` (function) — [saleor/checkout/tests/test_base_calculations.py:155]
- `test_calculate_base_line_unit_price_with_percentage_voucher_custom_prices` (function) — [saleor/checkout/tests/test_base_calculations.py:188]
- `test_calculate_base_line_unit_price_with_discounts_apply_once_per_order` (function) — [saleor/checkout/tests/test_base_calculations.py:224]
- `test_calculate_base_line_unit_price_with_discounts_once_per_order_custom_prices` (function) — [saleor/checkout/tests/test_base_calculations.py:258]
- `test_calculate_base_line_unit_price_with_variant_on_sale_and_voucher` (function) — [saleor/checkout/tests/test_base_calculations.py:293]
- `test_calculate_base_line_unit_price_with_variant_on_promotion_and_voucher` (function) — [saleor/checkout/tests/test_base_calculations.py:320]
- `test_calculate_base_line_total_price` (function) — [saleor/checkout/tests/test_base_calculations.py:352]
- `test_calculate_base_line_total_price_with_variant_on_promotion` (function) — [saleor/checkout/tests/test_base_calculations.py:374]
- `test_calculate_base_line_total_price_with_1_cent_variant_on_10_percentage_discount` (function) — [saleor/checkout/tests/test_base_calculations.py:395]
- `test_calculate_base_line_total_price_with_fixed_voucher` (function) — [saleor/checkout/tests/test_base_calculations.py:438]
- `test_calculate_base_line_total_price_with_percentage_voucher` (function) — [saleor/checkout/tests/test_base_calculations.py:474]
- `test_calculate_base_line_total_price_with_discounts_apply_once_per_order` (function) — [saleor/checkout/tests/test_base_calculations.py:512]
- `test_calculate_base_line_total_price_with_variant_on_promotion_and_voucher` (function) — [saleor/checkout/tests/test_base_calculations.py:552]
- `test_calculate_base_line_total_price_variant_on_promotion_and_voucher_applied_once` (function) — [saleor/checkout/tests/test_base_calculations.py:587]
- `test_base_tax_rate_net_price_zero` (function) — [saleor/checkout/tests/test_base_calculations.py:629]
- `test_base_tax_rate_gross_price_zero` (function) — [saleor/checkout/tests/test_base_calculations.py:634]
- `test_base_checkout_total` (function) — [saleor/checkout/tests/test_base_calculations.py:639]
- `test_base_checkout_total_high_discount_on_entire_order_apply_once_per_order` (function) — [saleor/checkout/tests/test_base_calculations.py:675]
- `test_base_checkout_total_high_discount_on_shipping` (function) — [saleor/checkout/tests/test_base_calculations.py:712]
- `test_base_checkout_total_order_discount` (function) — [saleor/checkout/tests/test_base_calculations.py:743]
- `test_checkout_total_order_discount` (function) — [saleor/checkout/tests/test_base_calculations.py:770]
- `test_base_checkout_total_gift_promotion` (function) — [saleor/checkout/tests/test_base_calculations.py:799]
- `test_checkout_total_gift_promotion` (function) — [saleor/checkout/tests/test_base_calculations.py:827]

**`saleor/checkout/tests/test_calculations.py`**

- `tax_data` (function) — [saleor/checkout/tests/test_calculations.py:56]
- `test_apply_tax_data` (function) — [saleor/checkout/tests/test_calculations.py:77]
- `test_apply_tax_data_tax_rate_matches` (function) — [saleor/checkout/tests/test_calculations.py:109]
- `fetch_kwargs` (function) — [saleor/checkout/tests/test_calculations.py:150]
- `get_checkout_taxed_prices_data` (function) — [saleor/checkout/tests/test_calculations.py:166]
- `get_taxed_money` (function) — [saleor/checkout/tests/test_calculations.py:178]
- `test_fetch_checkout_data_plugins` (function) — [saleor/checkout/tests/test_calculations.py:191]
- `test_fetch_checkout_data_plugins_allow_sync_webhooks_set_to_false` (function) — [saleor/checkout/tests/test_calculations.py:254]
- `test_fetch_checkout_data_flat_rates` (function) — [saleor/checkout/tests/test_calculations.py:318]
- `test_fetch_checkout_data_flat_rates_with_weighted_shipping_tax` (function) — [saleor/checkout/tests/test_calculations.py:362]
- `test_fetch_checkout_data_flat_rates_and_no_tax_calc_strategy` (function) — [saleor/checkout/tests/test_calculations.py:429]
- `test_set_checkout_base_prices_no_charge_taxes_with_voucher` (function) — [saleor/checkout/tests/test_calculations.py:464]
- `test_set_checkout_base_prices_no_charge_taxes_with_order_promotion` (function) — [saleor/checkout/tests/test_calculations.py:534]
- `test_fetch_checkout_data_webhooks_success` (function) — [saleor/checkout/tests/test_calculations.py:576]
- `test_fetch_checkout_prices_when_tax_exemption_and_include_taxes_in_prices` (function) — [saleor/checkout/tests/test_calculations.py:607]
- `test_fetch_checkout_prices_when_tax_exemption_and_not_include_taxes_in_prices` (function) — [saleor/checkout/tests/test_calculations.py:683]
- `test_fetch_checkout_data_calls_plugin` (function) — [saleor/checkout/tests/test_calculations.py:742]
- `test_fetch_checkout_data_calls_tax_app` (function) — [saleor/checkout/tests/test_calculations.py:780]
- `test_fetch_checkout_data_dont_call_tax_app_when_allow_sync_webhooks_set_to_false` (function) — [saleor/checkout/tests/test_calculations.py:820]
- `test_fetch_checkout_data_calls_inactive_plugin` (function) — [saleor/checkout/tests/test_calculations.py:870]
- `test_fetch_checkout_data_flat_rates_shipping_tax_differs_from_default` (function) — [saleor/checkout/tests/test_calculations.py:898]
- `test_external_shipping_webhook_it_not_called_during_tax_calculations` (function) — [saleor/checkout/tests/test_calculations.py:953]
- `test_calculate_and_add_tax_empty_tax_data_logging_address` (function) — [saleor/checkout/tests/test_calculations.py:1021]
- `test_fetch_checkout_data_tax_data_with_tax_data_error` (function) — [saleor/checkout/tests/test_calculations.py:1077]
- `test_fetch_checkout_data_tax_data_missing_tax_id_empty_tax_data` (function) — [saleor/checkout/tests/test_calculations.py:1132]
- `test_fetch_order_data_plugin_tax_data_with_negative_values` (function) — [saleor/checkout/tests/test_calculations.py:1174]
- `test_fetch_order_data_plugin_tax_data_price_overflow` (function) — [saleor/checkout/tests/test_calculations.py:1221]
- `test_fetch_checkout_with_prior_price_change` (function) — [saleor/checkout/tests/test_calculations.py:1266]
- `test_fetch_checkout_with_prior_price_none` (function) — [saleor/checkout/tests/test_calculations.py:1298]
- `test_fetch_checkout_data_updates_status_for_zero_amount_checkout_with_lines` (function) — [saleor/checkout/tests/test_calculations.py:1329]
- `test_fetch_checkout_data_considers_gift_cards_balance_when_updating_checkout_payment_status` (function) — [saleor/checkout/tests/test_calculations.py:1364]
- `test_fetch_checkout_data_checkout_removed_before_save` (function) — [saleor/checkout/tests/test_calculations.py:1408]
- `delete_checkout` (function) — [saleor/checkout/tests/test_calculations.py:1423]
- `test_fetch_checkout_data_checkout_updated_during_price_recalculation` (function) — [saleor/checkout/tests/test_calculations.py:1454]
- `modify_checkout` (function) — [saleor/checkout/tests/test_calculations.py:1473]
- `test_fetch_checkout_data_checkout_deleted_during_discount_recalculation` (function) — [saleor/checkout/tests/test_calculations.py:1511]
- `delete_checkout` (function) — [saleor/checkout/tests/test_calculations.py:1523]

**`saleor/checkout/tests/test_cart.py`**

- `anonymous_checkout` (function) — [saleor/checkout/tests/test_cart.py:21]
- `test_get_user_checkout` (function) — [saleor/checkout/tests/test_cart.py:25]
- `test_adding_zero_quantity` (function) — [saleor/checkout/tests/test_cart.py:33]
- `test_adding_same_variant` (function) — [saleor/checkout/tests/test_cart.py:42]
- `test_replacing_same_variant` (function) — [saleor/checkout/tests/test_cart.py:67]
- `test_adding_invalid_quantity` (function) — [saleor/checkout/tests/test_cart.py:79]
- `test_getting_line` (function) — [saleor/checkout/tests/test_cart.py:88]
- `test_shipping_detection` (function) — [saleor/checkout/tests/test_cart.py:98]
- `test_get_prices_of_discounted_specific_product` (function) — [saleor/checkout/tests/test_cart.py:108]
- `test_get_prices_of_discounted_specific_product_only_product` (function) — [saleor/checkout/tests/test_cart.py:136]
- `test_get_prices_of_discounted_specific_product_only_collection` (function) — [saleor/checkout/tests/test_cart.py:168]
- `test_get_prices_of_discounted_specific_product_only_category` (function) — [saleor/checkout/tests/test_cart.py:202]
- `test_get_prices_of_discounted_specific_product_all_products` (function) — [saleor/checkout/tests/test_cart.py:242]
- `test_checkout_line_repr` (function) — [saleor/checkout/tests/test_cart.py:262]
- `test_checkout_line_state` (function) — [saleor/checkout/tests/test_cart.py:271]
- `test_get_total_weight` (function) — [saleor/checkout/tests/test_cart.py:282]

**`saleor/checkout/tests/test_checkout_cleaner.py`**

- `test_validate_gift_cards_rejects_mismatched_assignment` (function) — [saleor/checkout/tests/test_checkout_cleaner.py:7]
- `test_validate_gift_cards_allows_matching_assignment` (function) — [saleor/checkout/tests/test_checkout_cleaner.py:24]

**`saleor/checkout/tests/test_checkout_complete.py`**

- `test_create_order_captured_payment_creates_expected_events` (function) — [saleor/checkout/tests/test_checkout_complete.py:50]
- `test_create_order_captured_payment_creates_expected_events_anonymous_user` (function) — [saleor/checkout/tests/test_checkout_complete.py:213]
- `test_create_order_preauth_payment_creates_expected_events` (function) — [saleor/checkout/tests/test_checkout_complete.py:373]
- `test_create_order_preauth_payment_creates_expected_events_anonymous_user` (function) — [saleor/checkout/tests/test_checkout_complete.py:488]
- `test_create_order_insufficient_stock` (function) — [saleor/checkout/tests/test_checkout_complete.py:597]
- `test_create_order_doesnt_duplicate_order` (function) — [saleor/checkout/tests/test_checkout_complete.py:622]
- `test_create_order_with_gift_card` (function) — [saleor/checkout/tests/test_checkout_complete.py:668]
- `test_create_order_with_gift_card_partial_use` (function) — [saleor/checkout/tests/test_checkout_complete.py:723]
- `test_create_order_with_many_gift_cards` (function) — [saleor/checkout/tests/test_checkout_complete.py:780]
- `test_create_order_gift_card_bought` (function) — [saleor/checkout/tests/test_checkout_complete.py:847]
- `test_create_order_gift_card_bought_order_not_captured_gift_cards_not_sent` (function) — [saleor/checkout/tests/test_checkout_complete.py:942]
- `test_create_order_gift_card_bought_only_shippable_gift_card` (function) — [saleor/checkout/tests/test_checkout_complete.py:1002]
- `test_create_order_gift_card_bought_do_not_fulfill_gift_cards_automatically` (function) — [saleor/checkout/tests/test_checkout_complete.py:1061]
- `test_note_in_created_order` (function) — [saleor/checkout/tests/test_checkout_complete.py:1116]
- `test_create_order_with_variant_tracking_false` (function) — [saleor/checkout/tests/test_checkout_complete.py:1144]
- `test_create_order_use_translations` (function) — [saleor/checkout/tests/test_checkout_complete.py:1179]
- `test_complete_checkout_0_total_with_transaction_for_mark_as_paid` (function) — [saleor/checkout/tests/test_checkout_complete.py:1227]
- `test_complete_checkout_0_total_captured_payment_creates_expected_events` (function) — [saleor/checkout/tests/test_checkout_complete.py:1272]
- `test_complete_checkout_action_required_voucher_once_per_customer` (function) — [saleor/checkout/tests/test_checkout_complete.py:1403]
- `test_complete_checkout_action_required_voucher_single_use` (function) — [saleor/checkout/tests/test_checkout_complete.py:1464]
- `test_complete_checkout_order_not_created_when_the_refund_is_ongoing` (function) — [saleor/checkout/tests/test_checkout_complete.py:1534]
- `test_complete_checkout_when_checkout_doesnt_exists` (function) — [saleor/checkout/tests/test_checkout_complete.py:1586]
- `test_complete_checkout_checkout_was_deleted_before_completing` (function) — [saleor/checkout/tests/test_checkout_complete.py:1643]
- `convert_checkout_to_order` (function) — [saleor/checkout/tests/test_checkout_complete.py:1674]
- `test_complete_checkout_checkout_limited_use_voucher_multiple_thread` (function) — [saleor/checkout/tests/test_checkout_complete.py:1699]
- `call_checkout_complete` (function) — [saleor/checkout/tests/test_checkout_complete.py:1738]
- `test_complete_checkout_checkout_completed_in_the_meantime` (function) — [saleor/checkout/tests/test_checkout_complete.py:1772]
- `call_checkout_complete` (function) — [saleor/checkout/tests/test_checkout_complete.py:1806]
- `test_process_shipping_data_for_order_store_customer_shipping_address` (function) — [saleor/checkout/tests/test_checkout_complete.py:1837]
- `test_process_shipping_data_for_order_not_store_customer_shipping_address_saving_addresses_off` (function) — [saleor/checkout/tests/test_checkout_complete.py:1875]
- `test_process_shipping_data_for_order_dont_store_customer_click_and_collect_address` (function) — [saleor/checkout/tests/test_checkout_complete.py:1915]
- `test_process_user_data_for_order_store_customer_address` (function) — [saleor/checkout/tests/test_checkout_complete.py:1960]
- `test_process_user_data_for_order_do_not_store_customer_address_saving_addresses_off` (function) — [saleor/checkout/tests/test_checkout_complete.py:1985]
- `test_create_order_update_display_gross_prices` (function) — [saleor/checkout/tests/test_checkout_complete.py:2011]
- `test_create_order_store_shipping_prices` (function) — [saleor/checkout/tests/test_checkout_complete.py:2048]
- `test_create_order_store_shipping_prices_with_free_shipping_voucher` (function) — [saleor/checkout/tests/test_checkout_complete.py:2105]
- `test_complete_checkout_invalid_shipping_method` (function) — [saleor/checkout/tests/test_checkout_complete.py:2177]
- `test_checkout_complete_pick_transaction_flow` (function) — [saleor/checkout/tests/test_checkout_complete.py:2242]
- `test_checkout_complete_pick_transaction_flow_when_checkout_total_zero` (function) — [saleor/checkout/tests/test_checkout_complete.py:2289]
- `test_checkout_complete_pick_transaction_flow_not_authorized_no_active_payment` (function) — [saleor/checkout/tests/test_checkout_complete.py:2341]
- _…and 14 more in this file_

**`saleor/checkout/tests/test_checkout.py`**

- `test_last_change_update` (function) — [saleor/checkout/tests/test_checkout.py:57]
- `test_last_change_update_foreign_key` (function) — [saleor/checkout/tests/test_checkout.py:67]
- `test_get_discount_for_checkout_value_entire_order_voucher` (function) — [saleor/checkout/tests/test_checkout.py:98]
- `test_get_discount_for_checkout_value_specific_product_voucher` (function) — [saleor/checkout/tests/test_checkout.py:257]
- `test_get_voucher_discount_for_checkout_voucher_validation` (function) — [saleor/checkout/tests/test_checkout.py:339]
- `test_get_discount_for_checkout_entire_order_voucher_not_applicable` (function) — [saleor/checkout/tests/test_checkout.py:385]
- `test_get_discount_for_checkout_specific_products_voucher` (function) — [saleor/checkout/tests/test_checkout.py:436]
- `test_get_discount_for_checkout_specific_products_voucher_apply_only_once` (function) — [saleor/checkout/tests/test_checkout.py:491]
- `test_get_discount_for_checkout_specific_products_voucher_not_applicable` (function) — [saleor/checkout/tests/test_checkout.py:555]
- `test_get_discount_for_checkout_shipping_voucher` (function) — [saleor/checkout/tests/test_checkout.py:651]
- `test_get_discount_for_checkout_shipping_voucher_all_countries` (function) — [saleor/checkout/tests/test_checkout.py:700]
- `test_get_discount_for_checkout_shipping_voucher_limited_countries` (function) — [saleor/checkout/tests/test_checkout.py:734]
- `test_get_discount_for_checkout_shipping_voucher_not_applicable_missing_delivery` (function) — [saleor/checkout/tests/test_checkout.py:784]
- `test_get_discount_for_checkout_shipping_voucher_not_applicable_delivery_not_required` (function) — [saleor/checkout/tests/test_checkout.py:818]
- `test_get_discount_for_checkout_shipping_voucher_not_applicable_in_country` (function) — [saleor/checkout/tests/test_checkout.py:853]
- `test_get_discount_for_checkout_shipping_voucher_not_applicable_spent_not_enough` (function) — [saleor/checkout/tests/test_checkout.py:892]
- `test_get_discount_for_checkout_shipping_voucher_not_applicable_minimum_quantity_not_reached` (function) — [saleor/checkout/tests/test_checkout.py:933]
- `test_get_voucher_for_checkout_info` (function) — [saleor/checkout/tests/test_checkout.py:974]
- `test_get_voucher_for_checkout_info_expired_voucher` (function) — [saleor/checkout/tests/test_checkout.py:981]
- `test_get_voucher_for_checkout_info_no_voucher_code` (function) — [saleor/checkout/tests/test_checkout.py:991]
- `test_get_voucher_for_checkout` (function) — [saleor/checkout/tests/test_checkout.py:998]
- `test_get_voucher_for_checkout_voucher_used` (function) — [saleor/checkout/tests/test_checkout.py:1011]
- `test_get_voucher_for_checkout_voucher_used_voucher_usage_already_increased` (function) — [saleor/checkout/tests/test_checkout.py:1028]
- `test_remove_voucher_from_checkout` (function) — [saleor/checkout/tests/test_checkout.py:1050]
- `test_checkout_discount_amount_should_be_decimal` (function) — [saleor/checkout/tests/test_checkout.py:1061]
- `test_recalculate_checkout_discount` (function) — [saleor/checkout/tests/test_checkout.py:1066]
- `test_recalculate_checkout_discount_percentage` (function) — [saleor/checkout/tests/test_checkout.py:1081]
- `test_recalculate_checkout_discount_with_promotion` (function) — [saleor/checkout/tests/test_checkout.py:1096]
- `test_recalculate_checkout_discount_with_checkout_discount_voucher_not_applicable` (function) — [saleor/checkout/tests/test_checkout.py:1180]
- `test_recalculate_checkout_discount_with_order_discount_voucher_added` (function) — [saleor/checkout/tests/test_checkout.py:1224]
- `test_recalculate_checkout_discount_with_gift_reward_voucher_added` (function) — [saleor/checkout/tests/test_checkout.py:1260]
- `test_recalculate_checkout_discount_voucher_not_applicable` (function) — [saleor/checkout/tests/test_checkout.py:1303]
- `test_recalculate_checkout_discount_expired_voucher` (function) — [saleor/checkout/tests/test_checkout.py:1319]
- `test_recalculate_checkout_discount_free_shipping_subtotal_less_than_shipping` (function) — [saleor/checkout/tests/test_checkout.py:1335]
- `test_recalculate_checkout_discount_free_shipping_subtotal_bigger_than_shipping` (function) — [saleor/checkout/tests/test_checkout.py:1372]
- `test_recalculate_checkout_discount_free_shipping_for_checkout_without_shipping` (function) — [saleor/checkout/tests/test_checkout.py:1411]
- `test_recalculate_checkout_discount_translate_discount_in_checkout_language` (function) — [saleor/checkout/tests/test_checkout.py:1425]
- `test_change_address_in_checkout` (function) — [saleor/checkout/tests/test_checkout.py:1452]
- `test_change_address_in_checkout_to_none` (function) — [saleor/checkout/tests/test_checkout.py:1477]
- `test_change_address_in_checkout_to_same` (function) — [saleor/checkout/tests/test_checkout.py:1505]
- _…and 24 more in this file_

**`saleor/checkout/tests/test_delivery_assignent_to_checkout.py`**

- `test_remove_delivery_method_from_checkout_with_cc` (function) — [saleor/checkout/tests/test_delivery_assignent_to_checkout.py:10]
- `test_remove_delivery_method_from_checkout_with_shipping` (function) — [saleor/checkout/tests/test_delivery_assignent_to_checkout.py:30]
- `test_remove_delivery_method_from_checkout_without_method` (function) — [saleor/checkout/tests/test_delivery_assignent_to_checkout.py:48]
- `test_assign_shipping_to_checkout_without_delivery_method` (function) — [saleor/checkout/tests/test_delivery_assignent_to_checkout.py:59]
- `test_assign_shipping_to_checkout_with_cc` (function) — [saleor/checkout/tests/test_delivery_assignent_to_checkout.py:79]
- `test_assign_shipping_to_checkout_with_different_shipping_method` (function) — [saleor/checkout/tests/test_delivery_assignent_to_checkout.py:104]
- `test_assign_shipping_to_checkout_with_the_same_shipping_method` (function) — [saleor/checkout/tests/test_delivery_assignent_to_checkout.py:130]
- `test_assign_collection_point_to_checkout_without_delivery_method` (function) — [saleor/checkout/tests/test_delivery_assignent_to_checkout.py:149]
- `test_assign_collection_point_to_checkout_with_shipping_method` (function) — [saleor/checkout/tests/test_delivery_assignent_to_checkout.py:171]
- `test_assign_collection_point_to_checkout_with_different_cc` (function) — [saleor/checkout/tests/test_delivery_assignent_to_checkout.py:200]
- `test_assign_collection_point_to_checkout_with_the_same_cc` (function) — [saleor/checkout/tests/test_delivery_assignent_to_checkout.py:230]

**`saleor/checkout/tests/test_delivery_context.py`**

- `test_fetch_shipping_methods_for_checkout_with_built_in_shipping_method` (function) — [saleor/checkout/tests/test_delivery_context.py:77]
- `test_fetch_shipping_methods_for_checkout_updates_existing_built_in_shipping_method` (function) — [saleor/checkout/tests/test_delivery_context.py:134]
- `test_fetch_shipping_methods_for_checkout_removes_non_applicable_built_in_shipping_method` (function) — [saleor/checkout/tests/test_delivery_context.py:217]
- `test_fetch_shipping_methods_for_checkout_non_applicable_assigned_built_in_shipping_method` (function) — [saleor/checkout/tests/test_delivery_context.py:262]
- `test_fetch_shipping_methods_for_checkout_with_excluded_built_in_shipping_method` (function) — [saleor/checkout/tests/test_delivery_context.py:320]
- `test_fetch_shipping_methods_for_checkout_with_changed_price_of_built_in_shipping_method` (function) — [saleor/checkout/tests/test_delivery_context.py:363]
- `test_fetch_shipping_methods_for_checkout_with_changed_tax_class_of_built_in_shipping_method` (function) — [saleor/checkout/tests/test_delivery_context.py:416]
- `test_fetch_shipping_methods_for_checkout_with_external_shipping_method` (function) — [saleor/checkout/tests/test_delivery_context.py:498]
- `test_fetch_shipping_methods_for_checkout_updates_existing_external_shipping_method` (function) — [saleor/checkout/tests/test_delivery_context.py:554]
- `test_fetch_shipping_methods_for_checkout_removes_non_applicable_external_shipping_method` (function) — [saleor/checkout/tests/test_delivery_context.py:619]
- `test_fetch_shipping_methods_for_checkout_non_applicable_assigned_external_shipping_method` (function) — [saleor/checkout/tests/test_delivery_context.py:685]
- `test_fetch_shipping_methods_for_checkout_with_excluded_external_shipping_method` (function) — [saleor/checkout/tests/test_delivery_context.py:762]
- `test_fetch_shipping_methods_for_checkout_with_changed_price_of_external_shipping_method` (function) — [saleor/checkout/tests/test_delivery_context.py:827]
- `test_fetch_shipping_methods_for_checkout_with_preserve_when_assigned_is_none` (function) — [saleor/checkout/tests/test_delivery_context.py:896]
- `test_fetch_shipping_methods_for_checkout_with_preserve_when_assigned_is_invalid_and_refreshed_is_none` (function) — [saleor/checkout/tests/test_delivery_context.py:935]
- `test_fetch_shipping_methods_for_checkout_with_preserve_when_assigned_is_valid_and_refreshed_is_none` (function) — [saleor/checkout/tests/test_delivery_context.py:992]
- `test_fetch_shipping_methods_for_checkout_with_preserve_when_assigned_is_valid_and_refreshed_unchanged` (function) — [saleor/checkout/tests/test_delivery_context.py:1047]
- `test_fetch_shipping_methods_for_checkout_with_preserve_when_assigned_is_invalid_and_refreshed_unchanged` (function) — [saleor/checkout/tests/test_delivery_context.py:1115]
- `test_fetch_shipping_methods_for_checkout_with_preserve_when_assigned_is_valid_and_refreshed_changed` (function) — [saleor/checkout/tests/test_delivery_context.py:1184]
- `test_fetch_shipping_methods_for_checkout_with_preserve_when_assigned_is_invalid_and_refreshed_changed` (function) — [saleor/checkout/tests/test_delivery_context.py:1270]
- `test_fetch_shipping_methods_for_checkout_with_preserve_when_refreshed_is_changed_to_match_assigned` (function) — [saleor/checkout/tests/test_delivery_context.py:1352]
- `test_assign_delivery_method_to_checkout_delivery_method_to_none` (function) — [saleor/checkout/tests/test_delivery_context.py:1429]
- `test_assign_delivery_method_to_checkout_delivery_method_to_external` (function) — [saleor/checkout/tests/test_delivery_context.py:1449]
- `test_assign_delivery_method_to_checkout_delivery_method_to_cc` (function) — [saleor/checkout/tests/test_delivery_context.py:1488]
- `test_clear_cc_delivery_method` (function) — [saleor/checkout/tests/test_delivery_context.py:1521]
- `test_is_valid_delivery_method` (function) — [saleor/checkout/tests/test_delivery_context.py:1540]
- `test_fetch_shipping_methods_for_checkout_invalidates_assigned_when_stale_invalid_sibling_exists` (function) — [saleor/checkout/tests/test_delivery_context.py:1569]
- `test_fetch_shipping_methods_for_checkout_preserve_invalidates_when_stale_invalid_sibling_exists` (function) — [saleor/checkout/tests/test_delivery_context.py:1638]

**`saleor/checkout/tests/test_fetch.py`**

- `test_checkout_line_info_undiscounted_unit_price` (function) — [saleor/checkout/tests/test_fetch.py:13]
- `test_checkout_line_info_undiscounted_unit_price_without_listing` (function) — [saleor/checkout/tests/test_fetch.py:44]
- `test_checkout_line_info_undiscounted_unit_price_when_listing_without_price` (function) — [saleor/checkout/tests/test_fetch.py:79]
- `test_checkout_line_info_variant_discounted_price` (function) — [saleor/checkout/tests/test_fetch.py:115]
- `test_checkout_line_info_variant_discounted_price_without_listing` (function) — [saleor/checkout/tests/test_fetch.py:149]
- `test_checkout_line_info_variant_discounted_price_when_listing_without_price` (function) — [saleor/checkout/tests/test_fetch.py:187]
- `test_checkout_line_info_variant_discounted_price_with_price_override` (function) — [saleor/checkout/tests/test_fetch.py:226]
- `test_fetch_checkout_lines_info` (function) — [saleor/checkout/tests/test_fetch.py:265]
- `test_fetch_checkout_lines_info_when_product_not_available` (function) — [saleor/checkout/tests/test_fetch.py:282]
- `test_fetch_checkout_lines_info_when_line_without_channel_listing` (function) — [saleor/checkout/tests/test_fetch.py:308]
- `test_fetch_checkout_lines_info_when_variant_channel_listing_without_price` (function) — [saleor/checkout/tests/test_fetch.py:335]

**`saleor/checkout/tests/test_migrations_tasks.py`**

- `test_fix_shared_billing_addresses` (function) — [saleor/checkout/tests/test_migrations_tasks.py:13]
- `test_fix_shared_shipping_addresses` (function) — [saleor/checkout/tests/test_migrations_tasks.py:50]
- `test_no_checkouts_with_shared_addresses` (function) — [saleor/checkout/tests/test_migrations_tasks.py:87]
- `test_task_switches_fields` (function) — [saleor/checkout/tests/test_migrations_tasks.py:110]
- `test_task_recursion` (function) — [saleor/checkout/tests/test_migrations_tasks.py:131]
- `test_propagate_checkout_built_in_delivery` (function) — [saleor/checkout/tests/test_migrations_tasks.py:165]
- `test_propagate_checkout_external_delivery` (function) — [saleor/checkout/tests/test_migrations_tasks.py:197]
- `test_propagate_checkout_delivery_handles_duplicated_deliveries` (function) — [saleor/checkout/tests/test_migrations_tasks.py:230]
- `test_propagate_checkout_delivery_built_in_when_no_valid_checkouts` (function) — [saleor/checkout/tests/test_migrations_tasks.py:266]
- `test_propagate_checkout_delivery_external_when_no_valid_checkouts` (function) — [saleor/checkout/tests/test_migrations_tasks.py:294]

**`saleor/checkout/tests/test_order_from_checkout.py`**

- `test_create_order_insufficient_stock` (function) — [saleor/checkout/tests/test_order_from_checkout.py:36]
- `test_create_order_with_gift_card` (function) — [saleor/checkout/tests/test_order_from_checkout.py:63]
- `test_create_order_with_gift_card_partial_use` (function) — [saleor/checkout/tests/test_order_from_checkout.py:110]
- `test_create_order_with_many_gift_cards_worth_more_than_total` (function) — [saleor/checkout/tests/test_order_from_checkout.py:159]
- `test_create_order_with_many_gift_cards` (function) — [saleor/checkout/tests/test_order_from_checkout.py:225]
- `test_create_order_gift_card_bought` (function) — [saleor/checkout/tests/test_order_from_checkout.py:287]
- `test_create_order_gift_card_bought_only_shippable_gift_card` (function) — [saleor/checkout/tests/test_order_from_checkout.py:362]
- `test_create_order_gift_card_bought_do_not_fulfill_gift_cards_automatically` (function) — [saleor/checkout/tests/test_order_from_checkout.py:413]
- `test_note_in_created_order` (function) — [saleor/checkout/tests/test_order_from_checkout.py:461]
- `test_create_order_use_translations` (function) — [saleor/checkout/tests/test_order_from_checkout.py:483]
- `test_create_order_from_checkout_updates_total_authorized_amount` (function) — [saleor/checkout/tests/test_order_from_checkout.py:525]
- `test_create_order_from_checkout_updates_total_charged_amount` (function) — [saleor/checkout/tests/test_order_from_checkout.py:556]
- `test_create_order_from_checkout_update_display_gross_prices` (function) — [saleor/checkout/tests/test_order_from_checkout.py:591]
- `test_create_order_from_checkout_store_shipping_prices` (function) — [saleor/checkout/tests/test_order_from_checkout.py:619]
- `test_create_order_from_checkout_valid_undiscounted_prices` (function) — [saleor/checkout/tests/test_order_from_checkout.py:670]
- `test_create_order_from_store_shipping_prices_with_free_shipping_voucher` (function) — [saleor/checkout/tests/test_order_from_checkout.py:724]
- `test_note_in_created_order_checkout_line_deleted_in_the_meantime` (function) — [saleor/checkout/tests/test_order_from_checkout.py:776]
- `delete_checkout_line` (function) — [saleor/checkout/tests/test_order_from_checkout.py:792]
- `test_note_in_created_order_checkout_deleted_in_the_meantime` (function) — [saleor/checkout/tests/test_order_from_checkout.py:811]
- `delete_checkout` (function) — [saleor/checkout/tests/test_order_from_checkout.py:826]
- `test_create_order_from_checkout_update_undiscounted_prices_match` (function) — [saleor/checkout/tests/test_order_from_checkout.py:847]
- `test_create_order_product_on_promotion` (function) — [saleor/checkout/tests/test_order_from_checkout.py:898]
- `test_create_order_with_voucher_0_total` (function) — [saleor/checkout/tests/test_order_from_checkout.py:940]
- `test_create_order_from_checkout_update_tax_error` (function) — [saleor/checkout/tests/test_order_from_checkout.py:1009]
- `test_created_order_from_checkout_missing_lines` (function) — [saleor/checkout/tests/test_order_from_checkout.py:1041]
- `delete_lines` (function) — [saleor/checkout/tests/test_order_from_checkout.py:1058]

**`saleor/checkout/tests/test_payment_utils.py`**

- `test_checkout_charge_status` (function) — [saleor/checkout/tests/test_payment_utils.py:28]

**`saleor/checkout/tests/test_search_indexing.py`**

- `checkout_list_with_relations` (function) — [saleor/checkout/tests/test_search_indexing.py:28]
- `test_update_checkouts_search_vector` (function) — [saleor/checkout/tests/test_search_indexing.py:97]
- `test_update_checkouts_search_vector_multiple_checkouts` (function) — [saleor/checkout/tests/test_search_indexing.py:111]
- `test_update_checkouts_search_vector_empty_list` (function) — [saleor/checkout/tests/test_search_indexing.py:130]
- `test_update_checkouts_search_vector_constant_queries` (function) — [saleor/checkout/tests/test_search_indexing.py:138]
- `test_prepare_checkout_search_vector_value_basic` (function) — [saleor/checkout/tests/test_search_indexing.py:172]
- `test_prepare_checkout_search_vector_value_with_user` (function) — [saleor/checkout/tests/test_search_indexing.py:194]
- `test_prepare_checkout_search_vector_value_with_addresses` (function) — [saleor/checkout/tests/test_search_indexing.py:221]
- `test_prepare_checkout_search_vector_value_with_no_email` (function) — [saleor/checkout/tests/test_search_indexing.py:250]
- `test_generate_checkout_payments_search_vector_value_empty` (function) — [saleor/checkout/tests/test_search_indexing.py:273]
- `test_generate_checkout_payments_search_vector_value` (function) — [saleor/checkout/tests/test_search_indexing.py:284]
- `test_generate_checkout_payments_search_vector_value_respects_max_limit` (function) — [saleor/checkout/tests/test_search_indexing.py:323]
- `test_generate_checkout_lines_search_vector_value_empty` (function) — [saleor/checkout/tests/test_search_indexing.py:350]
- `test_generate_checkout_lines_search_vector_value` (function) — [saleor/checkout/tests/test_search_indexing.py:361]
- `test_generate_checkout_lines_search_vector_value_without_variant` (function) — [saleor/checkout/tests/test_search_indexing.py:385]
- `test_generate_checkout_lines_search_vector_value_without_sku` (function) — [saleor/checkout/tests/test_search_indexing.py:403]
- `test_generate_checkout_lines_search_vector_value_respects_max_limit` (function) — [saleor/checkout/tests/test_search_indexing.py:430]
- `test_generate_checkout_transactions_search_vector_value_empty` (function) — [saleor/checkout/tests/test_search_indexing.py:463]
- `test_generate_checkout_transactions_search_vector_value` (function) — [saleor/checkout/tests/test_search_indexing.py:474]
- `test_generate_checkout_transactions_search_vector_value_without_psp_reference` (function) — [saleor/checkout/tests/test_search_indexing.py:509]
- `test_generate_checkout_transactions_search_vector_value_with_multiple_events` (function) — [saleor/checkout/tests/test_search_indexing.py:535]
- `test_generate_checkout_transactions_search_vector_value_respects_max_limit` (function) — [saleor/checkout/tests/test_search_indexing.py:586]
- `test_update_checkouts_search_vector_handles_deleted_checkout` (function) — [saleor/checkout/tests/test_search_indexing.py:617]
- `delete_checkout` (function) — [saleor/checkout/tests/test_search_indexing.py:626]
- `test_update_checkouts_search_vector_handles_deleted_checkout_before_lock` (function) — [saleor/checkout/tests/test_search_indexing.py:642]
- `delete_checkout` (function) — [saleor/checkout/tests/test_search_indexing.py:651]
- `test_update_checkouts_search_vector_resets_flag_on_prepare_exception` (function) — [saleor/checkout/tests/test_search_indexing.py:667]
- `test_update_checkouts_search_vector_resets_flag_on_load_data_exception` (function) — [saleor/checkout/tests/test_search_indexing.py:690]

**`saleor/checkout/tests/test_search_loaders.py`**

- `test_load_checkout_data` (function) — [saleor/checkout/tests/test_search_loaders.py:7]
- `test_load_checkout_data_empty_list` (function) — [saleor/checkout/tests/test_search_loaders.py:45]
- `test_load_checkout_data_with_no_relations` (function) — [saleor/checkout/tests/test_search_loaders.py:56]
- `test_load_checkout_data_multiple_checkouts` (function) — [saleor/checkout/tests/test_search_loaders.py:77]

**`saleor/checkout/tests/test_tasks.py`**

- `test_delete_expired_anonymous_checkouts` (function) — [saleor/checkout/tests/test_tasks.py:28]
- `test_delete_expired_user_checkouts` (function) — [saleor/checkout/tests/test_tasks.py:128]
- `test_delete_empty_checkouts` (function) — [saleor/checkout/tests/test_tasks.py:240]
- `test_delete_expired_checkouts` (function) — [saleor/checkout/tests/test_tasks.py:285]
- `test_delete_expired_checkouts_doesnt_delete_when_transaction_amount_exists` (function) — [saleor/checkout/tests/test_tasks.py:373]
- `test_delete_expired_checkouts_no_checkouts_to_delete` (function) — [saleor/checkout/tests/test_tasks.py:474]
- `test_delete_checkouts_until_done` (function) — [saleor/checkout/tests/test_tasks.py:486]
- `test_aborts_deleting_checkouts_when_invocation_count_exhausted` (function) — [saleor/checkout/tests/test_tasks.py:552]
- `test_automatic_checkout_completion_transaction_flow` (function) — [saleor/checkout/tests/test_tasks.py:600]
- `test_automatic_checkout_completion_payment_flow` (function) — [saleor/checkout/tests/test_tasks.py:649]
- `test_automatic_checkout_completion_missing_checkout` (function) — [saleor/checkout/tests/test_tasks.py:697]
- `test_automatic_checkout_completion_unavailable_variant` (function) — [saleor/checkout/tests/test_tasks.py:712]
- `test_automatic_checkout_completion_line_without_listing` (function) — [saleor/checkout/tests/test_tasks.py:761]
- `test_automatic_checkout_completion_error_raised` (function) — [saleor/checkout/tests/test_tasks.py:808]
- `test_automatic_checkout_completion_missing_lines` (function) — [saleor/checkout/tests/test_tasks.py:844]
- `test_automatic_checkout_completion_missing_delivery_method` (function) — [saleor/checkout/tests/test_tasks.py:882]
- `test_trigger_automatic_checkout_completion_task_no_channels` (function) — [saleor/checkout/tests/test_tasks.py:924]
- `test_trigger_automatic_checkout_completion_task_no_eligible_checkouts` (function) — [saleor/checkout/tests/test_tasks.py:952]
- `test_trigger_automatic_checkout_completion_task_with_eligible_checkouts` (function) — [saleor/checkout/tests/test_tasks.py:981]
- `test_trigger_automatic_checkout_completion_task_checkout_not_eligible_due_to_delay` (function) — [saleor/checkout/tests/test_tasks.py:1015]
- `test_trigger_automatic_checkout_completion_task_checkout_too_old` (function) — [saleor/checkout/tests/test_tasks.py:1045]
- `test_trigger_automatic_checkout_completion_task_checkout_not_eligible_due_missing_billing_address` (function) — [saleor/checkout/tests/test_tasks.py:1082]
- `test_trigger_automatic_checkout_completion_task_checkout_not_eligible_due_missing_email_or_user` (function) — [saleor/checkout/tests/test_tasks.py:1115]
- `test_trigger_automatic_checkout_completion_task_checkout_not_eligible_due_total_0` (function) — [saleor/checkout/tests/test_tasks.py:1148]
- `test_trigger_automatic_checkout_completion_task_respects_batch_size` (function) — [saleor/checkout/tests/test_tasks.py:1181]
- `test_trigger_automatic_checkout_completion_task_prioritizes_never_attempted` (function) — [saleor/checkout/tests/test_tasks.py:1225]
- `test_trigger_automatic_checkout_completion_task_multiple_channels` (function) — [saleor/checkout/tests/test_tasks.py:1297]
- `test_trigger_automatic_checkout_completion_task_with_cut_off_date` (function) — [saleor/checkout/tests/test_tasks.py:1381]
- `test_update_checkouts_search_vector_task_updates_dirty_checkouts` (function) — [saleor/checkout/tests/test_tasks.py:1461]
- `test_update_checkouts_search_vector_task_respects_batch_size` (function) — [saleor/checkout/tests/test_tasks.py:1489]
- `test_update_checkouts_search_vector_task_no_dirty_checkouts` (function) — [saleor/checkout/tests/test_tasks.py:1525]
- `test_update_checkouts_search_vector_task_skips_clean_checkouts` (function) — [saleor/checkout/tests/test_tasks.py:1542]
- `test_update_checkouts_search_vector_task_batch_process_updates_checkouts` (function) — [saleor/checkout/tests/test_tasks.py:1568]
- `test_update_checkouts_search_vector_task_batch_process_skips_clean_checkouts` (function) — [saleor/checkout/tests/test_tasks.py:1591]
- `test_update_checkouts_search_vector_task_batch_process_no_dirty_checkouts` (function) — [saleor/checkout/tests/test_tasks.py:1617]
- `test_update_checkouts_search_vector_task_batch_process_empty_pks` (function) — [saleor/checkout/tests/test_tasks.py:1637]

**`saleor/checkout/tests/test_utils.py`**

- `test_get_taxed_undiscounted_price` (function) — [saleor/checkout/tests/test_utils.py:47]
- `test_checkout_info_for_logs` (function) — [saleor/checkout/tests/test_utils.py:58]

**`saleor/checkout/tests/utils.py`**

- `add_variant_to_checkout` (function) — [saleor/checkout/tests/utils.py:13]
- `check_variant_in_stock` (function) — [saleor/checkout/tests/utils.py:94]

## How it works

The module's files, as provided to this run:

- `saleor/checkout/tests/__init__.py` (1 lines)
- `saleor/checkout/tests/test_actions.py` (1740 lines)
- `saleor/checkout/tests/test_associate_checkout_with_account.py` (118 lines)
- `saleor/checkout/tests/test_autodocs_probe.py` (6 lines)
- `saleor/checkout/tests/test_base_calculations.py` (852 lines)
- `saleor/checkout/tests/test_calculations.py` (1543 lines)
- `saleor/checkout/tests/test_cart.py` (290 lines)
- `saleor/checkout/tests/test_checkout_cleaner.py` (37 lines)
- `saleor/checkout/tests/test_checkout_complete.py` (2862 lines)
- `saleor/checkout/tests/test_checkout.py` (1963 lines)
- `saleor/checkout/tests/test_delivery_assignent_to_checkout.py` (246 lines)
- `saleor/checkout/tests/test_delivery_context.py` (1731 lines)
- `saleor/checkout/tests/test_fetch.py` (359 lines)
- `saleor/checkout/tests/test_migrations_tasks.py` (325 lines)
- `saleor/checkout/tests/test_order_from_checkout.py` (1072 lines)
- `saleor/checkout/tests/test_payment_utils.py` (54 lines)
- `saleor/checkout/tests/test_search_indexing.py` (710 lines)
- `saleor/checkout/tests/test_search_loaders.py` (87 lines)
- `saleor/checkout/tests/test_tasks.py` (1647 lines)
- `saleor/checkout/tests/test_utils.py` (91 lines)
- `saleor/checkout/tests/utils.py` (128 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/checkout`, `saleor/graphql`, `saleor/checkout/webhooks`, `saleor/channel/tests`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...CheckoutAuthorizeStatus`
- `...CheckoutChargeStatus`
- `...account.CustomerEvents`
- `...account.models.Address`
- `...account.models.CustomerEvent`
- `...base_calculations`
- `...calculations`
- `...channel.MarkAsPaidStrategy`
- `...channel.models.Channel`
- `...checkout.CheckoutAuthorizeStatus`
- `...checkout.fetch.fetch_checkout_info`
- `...checkout.fetch.fetch_checkout_lines`
- `...checkout.models.Checkout`
- `...checkout.models.CheckoutDelivery`
- `...checkout.models.CheckoutLine`
- `...core.exceptions.GiftCardNotApplicable`
- `...core.exceptions.InsufficientStock`
- `...core.exceptions.ProductNotPublished`
- `...core.models.EventDelivery`
- `...core.notify.NotifyEventType`
- `...core.prices.quantize_price`
- `...core.taxes.zero_money`
- `...core.taxes.zero_taxed_money`
- `...core.tests.utils.get_site_context_payload`
- `...discount.DiscountType`
- `...discount.DiscountValueType`
- `...discount.RewardValueType`
- `...discount.VoucherType`
- `...discount.interface.VariantPromotionRuleInfo`
- `...discount.models.PromotionRule`
- `...discount.models.VoucherCustomer`
- `...giftcard.GiftCardEvents`
- `...giftcard.models.GiftCard`
- `...giftcard.models.GiftCardEvent`
- `...graphql.core.utils.to_global_id_or_none`
- `...order.OrderAuthorizeStatus`
- `...order.OrderChargeStatus`
- `...order.OrderEvents`
- `...order.OrderStatus`
- `...order.models.Order`
- `...order.models.OrderEvent`
- `...order.notifications.get_default_order_payload`
- `...payment.TransactionKind`
- `...payment.interface.GatewayResponse`
- `...payment.models.Payment`
- `...payment.models.TransactionEvent`
- `...payment.models.TransactionItem`
- `...plugins.PLUGIN_IDENTIFIER_PREFIX`
- `...plugins.avatax.plugin.DeprecatedAvataxPlugin`
- `...plugins.avatax.tests.conftest.plugin_configuration  # noqa: F401`
- `...plugins.manager.get_plugins_manager`
- `...plugins.tests.sample_plugins.PluginSample`
- `...product.models`
- `...product.models.Category`
- `...product.models.ProductChannelListing`
- `...product.models.ProductTranslation`
- `...product.models.ProductVariantChannelListing`
- `...product.models.ProductVariantTranslation`
- `...product.models.VariantChannelListingPromotionRule`
- `...shipping.interface.ExcludedShippingMethod`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `59766b9ee306` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
