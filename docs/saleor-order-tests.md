## Purpose

`saleor/order/tests` (`saleor/order/tests`) groups 24 source file(s) exposing 282 top-level declaration(s).

## Public surface

**`saleor/order/tests/benchmark/test_fetch_order_prices.py`**

- `test_fetch_order_prices` (function) — [saleor/order/tests/benchmark/test_fetch_order_prices.py:9]

**`saleor/order/tests/test_actions.py`**

- `test_order_created_order_confirmed_with_turned_flag_on` (function) — [saleor/order/tests/test_actions.py:22]
- `test_order_created_order_confirmed_with_turned_flag_off` (function) — [saleor/order/tests/test_actions.py:53]
- `test_order_created_with_tax_error` (function) — [saleor/order/tests/test_actions.py:76]
- `test_order_created_negative_order_price` (function) — [saleor/order/tests/test_actions.py:109]
- `test_order_created_negative_order_line_price` (function) — [saleor/order/tests/test_actions.py:148]

**`saleor/order/tests/test_base_order_line_total.py`**

- `test_base_order_line_total` (function) — [saleor/order/tests/test_base_order_line_total.py:7]

**`saleor/order/tests/test_base_order_total.py`**

- `test_base_order_total` (function) — [saleor/order/tests/test_base_order_total.py:10]
- `test_base_order_total_with_fixed_voucher` (function) — [saleor/order/tests/test_base_order_total.py:27]
- `test_base_order_total_with_fixed_voucher_more_then_total` (function) — [saleor/order/tests/test_base_order_total.py:58]
- `test_base_order_total_with_percentage_voucher` (function) — [saleor/order/tests/test_base_order_total.py:88]
- `test_base_order_total_with_fixed_manual_discount` (function) — [saleor/order/tests/test_base_order_total.py:119]
- `test_base_order_total_with_fixed_manual_discount_and_zero_order_total` (function) — [saleor/order/tests/test_base_order_total.py:149]
- `test_base_order_total_with_fixed_manual_discount_more_then_total` (function) — [saleor/order/tests/test_base_order_total.py:170]
- `test_base_order_total_with_percentage_manual_discount` (function) — [saleor/order/tests/test_base_order_total.py:199]
- `test_base_order_total_with_fixed_voucher_and_fixed_manual_discount` (function) — [saleor/order/tests/test_base_order_total.py:229]
- `test_base_order_total_with_percentage_voucher_and_fixed_manual_discount` (function) — [saleor/order/tests/test_base_order_total.py:276]
- `test_base_order_total_with_fixed_voucher_and_percentage_manual_discount` (function) — [saleor/order/tests/test_base_order_total.py:323]
- `test_base_order_total_with_percentage_voucher_and_percentage_manual_discount` (function) — [saleor/order/tests/test_base_order_total.py:373]
- `test_base_order_total_with_fixed_manual_discount_and_fixed_voucher` (function) — [saleor/order/tests/test_base_order_total.py:424]
- `test_base_order_total_with_fixed_manual_discount_and_percentage_voucher` (function) — [saleor/order/tests/test_base_order_total.py:472]
- `test_base_order_total_with_percentage_manual_discount_and_fixed_voucher` (function) — [saleor/order/tests/test_base_order_total.py:530]
- `test_base_order_total_with_percentage_manual_discount_and_percentage_voucher` (function) — [saleor/order/tests/test_base_order_total.py:578]

**`saleor/order/tests/test_calculate_prices.py`**

- `test_calculate_prices_voucher_entire_order` (function) — [saleor/order/tests/test_calculate_prices.py:16]
- `test_calculate_prices_voucher_entire_order_exceed_subtotal` (function) — [saleor/order/tests/test_calculate_prices.py:56]
- `test_calculate_prices_voucher_entire_order_percentage` (function) — [saleor/order/tests/test_calculate_prices.py:98]
- `test_calculate_prices_manual_discount` (function) — [saleor/order/tests/test_calculate_prices.py:138]
- `test_calculate_prices_shipping_voucher` (function) — [saleor/order/tests/test_calculate_prices.py:182]
- `test_calculate_prices_zero_discount` (function) — [saleor/order/tests/test_calculate_prices.py:212]
- `test_calculate_prices_subtotal_zero` (function) — [saleor/order/tests/test_calculate_prices.py:239]
- `test_calculate_prices_manual_discount_no_lines` (function) — [saleor/order/tests/test_calculate_prices.py:264]
- `test_calculate_prices_manual_discount_exceed_total` (function) — [saleor/order/tests/test_calculate_prices.py:286]
- `test_calculate_prices_manual_discount_percentage` (function) — [saleor/order/tests/test_calculate_prices.py:325]
- `test_calculate_prices_voucher_entire_order_and_manual_discount_fixed` (function) — [saleor/order/tests/test_calculate_prices.py:364]
- `test_calculate_prices_manual_discount_fixed_and_voucher_entire_order` (function) — [saleor/order/tests/test_calculate_prices.py:433]
- `test_calculate_prices_voucher_entire_order_and_manual_discount_percentage` (function) — [saleor/order/tests/test_calculate_prices.py:497]
- `test_calculate_prices_manual_discount_percentage_and_voucher_entire_order` (function) — [saleor/order/tests/test_calculate_prices.py:563]
- `test_apply_subtotal_discount_to_order_lines` (function) — [saleor/order/tests/test_calculate_prices.py:630]
- `test_apply_subtotal_discount_to_order_lines_order_with_single_line` (function) — [saleor/order/tests/test_calculate_prices.py:717]

**`saleor/order/tests/test_calculations.py`**

- `order_with_lines` (function) — [saleor/order/tests/test_calculations.py:39]
- `order_lines` (function) — [saleor/order/tests/test_calculations.py:45]
- `tax_data` (function) — [saleor/order/tests/test_calculations.py:50]
- `tax_data_prices_entered_with_tax` (function) — [saleor/order/tests/test_calculations.py:81]
- `create_taxed_money` (function) — [saleor/order/tests/test_calculations.py:113]
- `create_order_taxed_prices_data` (function) — [saleor/order/tests/test_calculations.py:117]
- `test_recalculate_with_plugins` (function) — [saleor/order/tests/test_calculations.py:126]
- `test_recalculate_with_plugins_tax_error` (function) — [saleor/order/tests/test_calculations.py:199]
- `test_recalculate_with_plugins_tax_error_line_prices` (function) — [saleor/order/tests/test_calculations.py:227]
- `test_recalculate_with_plugins_tax_error_shipping_price` (function) — [saleor/order/tests/test_calculations.py:305]
- `test_recalculate_with_plugins_order_discounts_and_total_undiscounted_price_changed` (function) — [saleor/order/tests/test_calculations.py:372]
- `test_recalculate_with_plugin_prices_entered_without_taxes` (function) — [saleor/order/tests/test_calculations.py:439]
- `test_recalculate_with_plugin_prices_entered_with_taxes` (function) — [saleor/order/tests/test_calculations.py:535]
- `test_calculate_prices_total_shipping_price_changed` (function) — [saleor/order/tests/test_calculations.py:638]
- `test_calculate_prices_line_quantity_changed` (function) — [saleor/order/tests/test_calculations.py:688]
- `test_apply_tax_data` (function) — [saleor/order/tests/test_calculations.py:722]
- `manager_with_mocked_plugins_calculations` (function) — [saleor/order/tests/test_calculations.py:776]
- `fetch_kwargs` (function) — [saleor/order/tests/test_calculations.py:814]
- `fetch_kwargs_with_lines` (function) — [saleor/order/tests/test_calculations.py:824]
- `get_taxed_money` (function) — [saleor/order/tests/test_calculations.py:833]
- `get_order_priced_taxes_data` (function) — [saleor/order/tests/test_calculations.py:856]
- `test_fetch_order_prices_if_expired_plugins` (function) — [saleor/order/tests/test_calculations.py:867]
- `test_fetch_order_prices_if_expired_flat_rates` (function) — [saleor/order/tests/test_calculations.py:927]
- `test_fetch_order_prices_if_expired_webhooks_success` (function) — [saleor/order/tests/test_calculations.py:958]
- `test_fetch_order_prices_if_expired_plugins_with_allow_sync_webhooks_to_false` (function) — [saleor/order/tests/test_calculations.py:990]
- `test_fetch_order_prices_if_expired_flat_rates_with_allow_sync_webhook_set_to_false` (function) — [saleor/order/tests/test_calculations.py:1032]
- `test_fetch_order_prices_tax_app_with_allow_sync_webhook_set_to_false` (function) — [saleor/order/tests/test_calculations.py:1064]
- `test_fetch_order_prices_if_expired_recalculate_all_prices` (function) — [saleor/order/tests/test_calculations.py:1089]
- `test_fetch_order_prices_when_tax_exemption` (function) — [saleor/order/tests/test_calculations.py:1144]
- `test_fetch_order_prices_if_expired_prefetch` (function) — [saleor/order/tests/test_calculations.py:1212]
- `test_fetch_order_prices_if_expired_prefetch_with_lines` (function) — [saleor/order/tests/test_calculations.py:1220]
- `test_fetch_order_prices_if_expired_use_base_shipping_price` (function) — [saleor/order/tests/test_calculations.py:1230]
- `test_fetch_order_prices_if_expired_flat_rates_and_no_tax_calc_strategy` (function) — [saleor/order/tests/test_calculations.py:1257]
- `test_fetch_order_prices_on_promotion_if_expired_recalculate_all_prices` (function) — [saleor/order/tests/test_calculations.py:1290]
- `test_order_line_unit` (function) — [saleor/order/tests/test_calculations.py:1340]
- `test_order_line_total` (function) — [saleor/order/tests/test_calculations.py:1372]
- `test_order_line_tax_rate` (function) — [saleor/order/tests/test_calculations.py:1404]
- `test_order_shipping` (function) — [saleor/order/tests/test_calculations.py:1423]
- `test_order_shipping_tax_rate` (function) — [saleor/order/tests/test_calculations.py:1440]
- `test_order_total` (function) — [saleor/order/tests/test_calculations.py:1457]
- _…and 15 more in this file_

**`saleor/order/tests/test_fetch_order_prices_line_price_expiration.py`**

- `test_fetch_order_prices_lines_expired_base_prices` (function) — [saleor/order/tests/test_fetch_order_prices_line_price_expiration.py:23]
- `test_fetch_order_prices_single_line_expired_base_prices` (function) — [saleor/order/tests/test_fetch_order_prices_line_price_expiration.py:113]
- `test_fetch_order_prices_lines_expired_catalogue_discount` (function) — [saleor/order/tests/test_fetch_order_prices_line_price_expiration.py:202]
- `test_fetch_order_prices_single_line_expired_catalogue_discount` (function) — [saleor/order/tests/test_fetch_order_prices_line_price_expiration.py:374]
- `test_fetch_order_prices_lines_expired_new_catalogue_discount` (function) — [saleor/order/tests/test_fetch_order_prices_line_price_expiration.py:545]
- `test_fetch_order_prices_lines_expired_manual_line_discount` (function) — [saleor/order/tests/test_fetch_order_prices_line_price_expiration.py:672]
- `test_fetch_order_prices_single_line_expired_manual_line_discount` (function) — [saleor/order/tests/test_fetch_order_prices_line_price_expiration.py:828]
- `test_fetch_order_prices_lines_expired_specific_product_voucher` (function) — [saleor/order/tests/test_fetch_order_prices_line_price_expiration.py:989]
- `test_fetch_order_prices_single_line_expired_specific_product_voucher` (function) — [saleor/order/tests/test_fetch_order_prices_line_price_expiration.py:1149]
- `test_fetch_order_prices_lines_expired_apply_once_per_order_voucher` (function) — [saleor/order/tests/test_fetch_order_prices_line_price_expiration.py:1308]
- `test_fetch_order_prices_single_line_expired_apply_once_per_order_voucher_new_cheapest` (function) — [saleor/order/tests/test_fetch_order_prices_line_price_expiration.py:1460]
- `test_fetch_order_prices_single_line_expired_apply_once_per_order_voucher_old_cheapest` (function) — [saleor/order/tests/test_fetch_order_prices_line_price_expiration.py:1608]

**`saleor/order/tests/test_fetch_order_prices_tax_app.py`**

- `order_with_lines` (function) — [saleor/order/tests/test_fetch_order_prices_tax_app.py:23]
- `test_fetch_order_prices_tax_app` (function) — [saleor/order/tests/test_fetch_order_prices_tax_app.py:29]
- `test_fetch_order_prices_catalogue_discount_tax_app` (function) — [saleor/order/tests/test_fetch_order_prices_tax_app.py:138]
- `test_fetch_order_prices_order_discount_tax_app` (function) — [saleor/order/tests/test_fetch_order_prices_tax_app.py:273]
- `test_fetch_order_prices_order_discount_tax_app_prices_entered_with_taxes` (function) — [saleor/order/tests/test_fetch_order_prices_tax_app.py:448]
- `test_fetch_order_prices_gift_discount_tax_app` (function) — [saleor/order/tests/test_fetch_order_prices_tax_app.py:634]
- `test_fetch_order_prices_catalogue_and_order_discounts_tax_app` (function) — [saleor/order/tests/test_fetch_order_prices_tax_app.py:770]
- `test_fetch_order_prices_manual_order_discount_and_line_level_voucher_tax_app` (function) — [saleor/order/tests/test_fetch_order_prices_tax_app.py:975]
- `test_fetch_order_prices_manual_line_discount_and_entire_order_voucher_tax_app` (function) — [saleor/order/tests/test_fetch_order_prices_tax_app.py:1188]
- `test_fetch_order_prices_shipping_voucher_and_manual_discount_tax_app` (function) — [saleor/order/tests/test_fetch_order_prices_tax_app.py:1396]
- `test_fetch_order_prices_entire_order_voucher_no_tax_data_tax_app` (function) — [saleor/order/tests/test_fetch_order_prices_tax_app.py:1605]

**`saleor/order/tests/test_fetch_order_prices.py`**

- `test_fetch_order_prices_catalogue_discount_flat_rates` (function) — [saleor/order/tests/test_fetch_order_prices.py:21]
- `test_fetch_order_prices_order_discount_flat_rates` (function) — [saleor/order/tests/test_fetch_order_prices.py:135]
- `test_fetch_order_prices_gift_discount_flat_rates` (function) — [saleor/order/tests/test_fetch_order_prices.py:269]
- `test_fetch_order_prices_catalogue_and_order_discounts_flat_rates` (function) — [saleor/order/tests/test_fetch_order_prices.py:398]
- `test_fetch_order_prices_catalogue_and_gift_discounts_flat_rates` (function) — [saleor/order/tests/test_fetch_order_prices.py:551]
- `test_fetch_order_prices_catalogue_and_order_discounts_exceed_total_flat_rates` (function) — [saleor/order/tests/test_fetch_order_prices.py:710]
- `test_fetch_order_prices_manual_discount_and_order_discount_flat_rates` (function) — [saleor/order/tests/test_fetch_order_prices.py:830]
- `test_fetch_order_prices_manual_discount_and_gift_discount_flat_rates` (function) — [saleor/order/tests/test_fetch_order_prices.py:967]
- `test_fetch_order_prices_manual_discount_and_catalogue_discount_flat_rates` (function) — [saleor/order/tests/test_fetch_order_prices.py:1113]
- `test_fetch_order_prices_manual_order_discount_voucher_specific_product` (function) — [saleor/order/tests/test_fetch_order_prices.py:1276]
- `test_fetch_order_prices_manual_order_discount_and_voucher_apply_once_per_order` (function) — [saleor/order/tests/test_fetch_order_prices.py:1395]
- `test_fetch_order_prices_order_promotion_discount_race_condition` (function) — [saleor/order/tests/test_fetch_order_prices.py:1516]
- `call_before_creating_order_promotion_line_discount` (function) — [saleor/order/tests/test_fetch_order_prices.py:1527]
- `test_fetch_order_prices_voucher_shipping_and_manual_discount_fixed` (function) — [saleor/order/tests/test_fetch_order_prices.py:1544]
- `test_fetch_order_prices_voucher_shipping_and_manual_discount_percentage` (function) — [saleor/order/tests/test_fetch_order_prices.py:1636]
- `test_fetch_order_prices_voucher_shipping_and_manual_discount_fixed_exceed_total` (function) — [saleor/order/tests/test_fetch_order_prices.py:1731]
- `test_fetch_order_prices_catalogue_discount_prices_entered_with_tax_tax_exemption` (function) — [saleor/order/tests/test_fetch_order_prices.py:1827]
- `test_fetch_order_prices_removing_catalogue_promotion_doesnt_remove_discount` (function) — [saleor/order/tests/test_fetch_order_prices.py:1945]

**`saleor/order/tests/test_fetch.py`**

- `test_fetch_draft_order_lines_info` (function) — [saleor/order/tests/test_fetch.py:11]
- `test_fetch_draft_order_lines_info_extended` (function) — [saleor/order/tests/test_fetch.py:60]
- `test_editable_order_line_info_variant_discounted_price` (function) — [saleor/order/tests/test_fetch.py:125]

**`saleor/order/tests/test_fulfillments_actions.py`**

- `test_create_fulfillments` (function) — [saleor/order/tests/test_fulfillments_actions.py:16]
- `test_create_fulfillments_require_approval` (function) — [saleor/order/tests/test_fulfillments_actions.py:92]
- `test_create_fulfillments_require_approval_as_app` (function) — [saleor/order/tests/test_fulfillments_actions.py:163]
- `test_create_fulfillments_without_notification` (function) — [saleor/order/tests/test_fulfillments_actions.py:233]
- `test_create_fulfillments_many_warehouses` (function) — [saleor/order/tests/test_fulfillments_actions.py:287]
- `test_create_fulfillments_with_one_line_empty_quantity` (function) — [saleor/order/tests/test_fulfillments_actions.py:355]
- `test_create_fulfillments_with_variant_without_inventory_tracking` (function) — [saleor/order/tests/test_fulfillments_actions.py:411]
- `test_create_fulfillments_without_allocations` (function) — [saleor/order/tests/test_fulfillments_actions.py:461]
- `test_create_fulfillments_warehouse_without_stock` (function) — [saleor/order/tests/test_fulfillments_actions.py:520]
- `test_create_fulfillments_with_variant_without_inventory_tracking_and_without_stock` (function) — [saleor/order/tests/test_fulfillments_actions.py:578]
- `test_create_fullfilment_with_out_of_stock_webhook` (function) — [saleor/order/tests/test_fulfillments_actions.py:627]
- `test_create_fullfilment_with_out_of_stock_webhook_not_triggered` (function) — [saleor/order/tests/test_fulfillments_actions.py:658]
- `test_create_fulfillments_quantity_allocated_lower_than_line_quantity` (function) — [saleor/order/tests/test_fulfillments_actions.py:690]
- `test_create_fulfillments_validate_lines_raise_error` (function) — [saleor/order/tests/test_fulfillments_actions.py:771]

**`saleor/order/tests/test_notifications.py`**

- `test_get_custom_order_payload` (function) — [saleor/order/tests/test_notifications.py:39]
- `test_get_order_line_payload` (function) — [saleor/order/tests/test_notifications.py:103]
- `test_get_order_line_payload_deleted_variant` (function) — [saleor/order/tests/test_notifications.py:192]
- `test_get_address_payload` (function) — [saleor/order/tests/test_notifications.py:205]
- `test_get_default_order_payload` (function) — [saleor/order/tests/test_notifications.py:222]
- `test_get_default_fulfillment_payload` (function) — [saleor/order/tests/test_notifications.py:294]
- `test_send_email_payment_confirmation` (function) — [saleor/order/tests/test_notifications.py:337]
- `test_send_email_order_confirmation` (function) — [saleor/order/tests/test_notifications.py:371]
- `test_send_email_order_confirmation_for_cc` (function) — [saleor/order/tests/test_notifications.py:397]
- `test_send_email_order_confirmation_with_staff_recipients` (function) — [saleor/order/tests/test_notifications.py:427]
- `test_send_confirmation_emails_without_addresses_for_payment` (function) — [saleor/order/tests/test_notifications.py:454]
- `test_send_confirmation_emails_without_addresses_for_order` (function) — [saleor/order/tests/test_notifications.py:513]
- `test_send_fulfillment_confirmation_by_user` (function) — [saleor/order/tests/test_notifications.py:566]
- `test_send_fulfillment_confirmation_by_app` (function) — [saleor/order/tests/test_notifications.py:599]
- `test_send_fulfillment_update` (function) — [saleor/order/tests/test_notifications.py:633]
- `test_send_email_order_canceled_by_user` (function) — [saleor/order/tests/test_notifications.py:659]
- `test_send_email_order_canceled_by_app` (function) — [saleor/order/tests/test_notifications.py:688]
- `test_send_email_order_refunded_by_user` (function) — [saleor/order/tests/test_notifications.py:714]
- `test_send_email_order_refunded_by_app` (function) — [saleor/order/tests/test_notifications.py:748]
- `test_get_default_images_payload` (function) — [saleor/order/tests/test_notifications.py:779]

**`saleor/order/tests/test_order_actions_create_fulfillments_for_returned_products.py`**

- `test_create_return_fulfillment_only_order_lines` (function) — [saleor/order/tests/test_order_actions_create_fulfillments_for_returned_products.py:19]
- `test_create_return_fulfillment_only_order_lines_with_refund` (function) — [saleor/order/tests/test_order_actions_create_fulfillments_for_returned_products.py:99]
- `test_create_return_fulfillment_only_order_lines_included_shipping_costs` (function) — [saleor/order/tests/test_order_actions_create_fulfillments_for_returned_products.py:181]
- `test_create_return_fulfillment_only_order_lines_with_replace_request` (function) — [saleor/order/tests/test_order_actions_create_fulfillments_for_returned_products.py:269]
- `test_create_return_fulfillment_only_fulfillment_lines` (function) — [saleor/order/tests/test_order_actions_create_fulfillments_for_returned_products.py:406]
- `test_create_return_fulfillment_only_fulfillment_lines_replace_order` (function) — [saleor/order/tests/test_order_actions_create_fulfillments_for_returned_products.py:459]
- `test_create_return_fulfillment_with_lines_already_refunded` (function) — [saleor/order/tests/test_order_actions_create_fulfillments_for_returned_products.py:572]
- `test_create_return_fulfillment_with_already_refunded_lines_persists_reason` (function) — [saleor/order/tests/test_order_actions_create_fulfillments_for_returned_products.py:686]
- `test_create_return_fulfillment_only_order_lines_with_old_ids` (function) — [saleor/order/tests/test_order_actions_create_fulfillments_for_returned_products.py:785]

**`saleor/order/tests/test_order_actions_refund_products.py`**

- `test_create_refund_fulfillment_only_order_lines` (function) — [saleor/order/tests/test_order_actions_refund_products.py:16]
- `test_create_refund_fulfillment_included_shipping_costs` (function) — [saleor/order/tests/test_order_actions_refund_products.py:92]
- `test_create_refund_fulfillment_only_fulfillment_lines` (function) — [saleor/order/tests/test_order_actions_refund_products.py:160]
- `test_create_refund_fulfillment_custom_amount` (function) — [saleor/order/tests/test_order_actions_refund_products.py:223]

**`saleor/order/tests/test_order_actions.py`**

- `test_handle_fully_paid_order` (function) — [saleor/order/tests/test_order_actions.py:61]
- `test_handle_fully_paid_order_no_email` (function) — [saleor/order/tests/test_order_actions.py:81]
- `test_handle_fully_paid_order_with_gateway` (function) — [saleor/order/tests/test_order_actions.py:99]
- `test_handle_fully_paid_order_gift_cards_created` (function) — [saleor/order/tests/test_order_actions.py:126]
- `test_handle_fully_paid_order_gift_cards_not_created` (function) — [saleor/order/tests/test_order_actions.py:207]
- `test_handle_fully_paid_order_for_draft_order` (function) — [saleor/order/tests/test_order_actions.py:276]
- `test_handle_fully_paid_order_triggers_webhooks` (function) — [saleor/order/tests/test_order_actions.py:312]
- `test_mark_as_paid_with_payment` (function) — [saleor/order/tests/test_order_actions.py:419]
- `test_mark_as_paid_with_external_reference_with_payment` (function) — [saleor/order/tests/test_order_actions.py:431]
- `test_mark_as_paid_no_billing_address` (function) — [saleor/order/tests/test_order_actions.py:448]
- `test_clean_mark_order_as_paid` (function) — [saleor/order/tests/test_order_actions.py:457]
- `test_mark_as_paid_with_transaction` (function) — [saleor/order/tests/test_order_actions.py:465]
- `test_mark_as_paid_with_external_reference_with_transaction` (function) — [saleor/order/tests/test_order_actions.py:492]
- `test_cancel_fulfillment` (function) — [saleor/order/tests/test_order_actions.py:511]
- `test_cancel_fulfillment_waiting_for_approval` (function) — [saleor/order/tests/test_order_actions.py:532]
- `test_cancel_fulfillment_variant_without_inventory_tracking` (function) — [saleor/order/tests/test_order_actions.py:562]
- `test_cancel_order` (function) — [saleor/order/tests/test_order_actions.py:589]
- `test_cancel_order_dont_trigger_webhooks` (function) — [saleor/order/tests/test_order_actions.py:630]
- `test_order_refunded_by_user` (function) — [saleor/order/tests/test_order_actions.py:705]
- `test_order_refunded_by_app` (function) — [saleor/order/tests/test_order_actions.py:739]
- `test_order_refunded_triggers_webhooks` (function) — [saleor/order/tests/test_order_actions.py:780]
- `test_order_voided_triggers_webhooks` (function) — [saleor/order/tests/test_order_actions.py:905]
- `test_order_fulfilled_does_not_trigger_webhooks` (function) — [saleor/order/tests/test_order_actions.py:1001]
- `test_order_awaits_fulfillment_approval_triggers_webhooks` (function) — [saleor/order/tests/test_order_actions.py:1085]
- `test_order_authorized_triggers_webhooks` (function) — [saleor/order/tests/test_order_actions.py:1189]
- `test_order_charged_triggers_webhooks` (function) — [saleor/order/tests/test_order_actions.py:1289]
- `test_fulfill_order_lines` (function) — [saleor/order/tests/test_order_actions.py:1401]
- `test_fulfill_order_lines_multiple_lines` (function) — [saleor/order/tests/test_order_actions.py:1427]
- `test_fulfill_order_lines_with_variant_deleted` (function) — [saleor/order/tests/test_order_actions.py:1475]
- `test_fulfill_order_lines_without_inventory_tracking` (function) — [saleor/order/tests/test_order_actions.py:1488]
- `test_order_transaction_updated_order_fully_paid` (function) — [saleor/order/tests/test_order_actions.py:1522]
- `test_order_transaction_updated_for_charged_triggers_webhooks` (function) — [saleor/order/tests/test_order_actions.py:1567]
- `test_order_transaction_updated_for_authorized_triggers_webhooks` (function) — [saleor/order/tests/test_order_actions.py:1702]
- `test_order_transaction_updated_for_refunded_triggers_webhooks` (function) — [saleor/order/tests/test_order_actions.py:1810]
- `test_order_transaction_updated_order_partially_paid` (function) — [saleor/order/tests/test_order_actions.py:1934]
- `test_order_transaction_updated_order_partially_paid_and_multiple_transactions` (function) — [saleor/order/tests/test_order_actions.py:1971]
- `test_order_transaction_updated_with_the_same_transaction_charged_amount` (function) — [saleor/order/tests/test_order_actions.py:2009]
- `test_order_transaction_updated_order_authorized` (function) — [saleor/order/tests/test_order_actions.py:2048]
- `test_order_transaction_updated_order_partially_authorized_and_multiple_transactions` (function) — [saleor/order/tests/test_order_actions.py:2086]
- `test_order_transaction_updated_with_the_same_transaction_authorized_amount` (function) — [saleor/order/tests/test_order_actions.py:2126]
- _…and 16 more in this file_

**`saleor/order/tests/test_order_search.py`**

- `test_update_order_search_vector_auto_save` (function) — [saleor/order/tests/test_order_search.py:8]
- `test_update_order_search_vector_without_save` (function) — [saleor/order/tests/test_order_search.py:22]
- `test_prepare_order_search_vector_value` (function) — [saleor/order/tests/test_order_search.py:37]
- `test_prepare_order_search_vector_value_empty_relation_fields` (function) — [saleor/order/tests/test_order_search.py:67]
- `test_prepare_order_search_vector_value_no_relations_data` (function) — [saleor/order/tests/test_order_search.py:98]

**`saleor/order/tests/test_order_utils.py`**

- `test_change_quantity_generates_proper_event` (function) — [saleor/order/tests/test_order_utils.py:44]
- `test_change_quantity_update_line_fields` (function) — [saleor/order/tests/test_order_utils.py:110]
- `test_match_orders_with_new_user` (function) — [saleor/order/tests/test_order_utils.py:143]
- `test_match_draft_order_with_new_user` (function) — [saleor/order/tests/test_order_utils.py:167]
- `test_add_variant_to_order` (function) — [saleor/order/tests/test_order_utils.py:183]
- `test_add_gift_cards_to_order` (function) — [saleor/order/tests/test_order_utils.py:234]
- `test_add_gift_cards_to_order_with_more_than_total` (function) — [saleor/order/tests/test_order_utils.py:289]
- `test_add_gift_cards_to_order_no_checkout_user` (function) — [saleor/order/tests/test_order_utils.py:317]
- `test_add_gift_cards_to_order_invalidates_prices_for_other_checkout_attached_to_the_same_gift_card` (function) — [saleor/order/tests/test_order_utils.py:374]
- `test_get_total_order_discount_excluding_shipping` (function) — [saleor/order/tests/test_order_utils.py:406]
- `test_get_total_order_discount_excluding_shipping_no_shipping_discounts` (function) — [saleor/order/tests/test_order_utils.py:438]
- `test_update_order_display_gross_prices_use_default_tax_settings` (function) — [saleor/order/tests/test_order_utils.py:474]
- `test_update_order_display_gross_prices_use_country_specific_tax_settings` (function) — [saleor/order/tests/test_order_utils.py:491]
- `test_get_total_order_discount_excluding_shipping_no_discounts` (function) — [saleor/order/tests/test_order_utils.py:513]
- `test_get_order_country_use_channel_country` (function) — [saleor/order/tests/test_order_utils.py:521]
- `test_calculate_order_granted_refund_status` (function) — [saleor/order/tests/test_order_utils.py:543]
- `test_order_info_for_logs` (function) — [saleor/order/tests/test_order_utils.py:574]
- `test_store_user_addresses_from_draft_order` (function) — [saleor/order/tests/test_order_utils.py:611]
- `test_store_user_addresses_from_draft_order_no_user` (function) — [saleor/order/tests/test_order_utils.py:646]
- `test_store_user_addresses_from_draft_order_save_address_options_set_to_false` (function) — [saleor/order/tests/test_order_utils.py:670]
- `test_store_user_addresses_from_draft_order_save_address_options_empty` (function) — [saleor/order/tests/test_order_utils.py:703]
- `test_store_user_addresses_from_draft_order_only_draft_save_shipping_address_true` (function) — [saleor/order/tests/test_order_utils.py:736]
- `test_store_user_addresses_from_draft_order_only_draft_save_billing_address_true` (function) — [saleor/order/tests/test_order_utils.py:771]

**`saleor/order/tests/test_order.py`**

- `test_total_setter` (function) — [saleor/order/tests/test_order.py:47]
- `test_order_get_subtotal` (function) — [saleor/order/tests/test_order.py:58]

**`saleor/order/tests/test_refresh_all_order_base_prices_and_discounts.py`**

- `test_refresh_all_order_base_prices` (function) — [saleor/order/tests/test_refresh_all_order_base_prices_and_discounts.py:24]

**`saleor/order/tests/test_refresh_order_base_prices_and_discounts.py`**

- `test_refresh_order_base_prices` (function) — [saleor/order/tests/test_refresh_order_base_prices_and_discounts.py:24]

**`saleor/order/tests/test_shipping_context.py`**

- `test_get_valid_shipping_methods_for_order` (function) — [saleor/order/tests/test_shipping_context.py:8]
- `test_get_valid_shipping_methods_for_order_no_channel_shipping_zones` (function) — [saleor/order/tests/test_shipping_context.py:27]
- `test_get_valid_shipping_methods_for_order_no_shipping_address` (function) — [saleor/order/tests/test_shipping_context.py:48]
- `test_get_valid_shipping_methods_for_order_shipping_not_required` (function) — [saleor/order/tests/test_shipping_context.py:67]
- `test_get_all_shipping_methods_returns_empty_when_shipping_not_required` (function) — [saleor/order/tests/test_shipping_context.py:88]
- `test_get_all_shipping_methods_returns_empty_when_no_shipping_address` (function) — [saleor/order/tests/test_shipping_context.py:107]
- `test_get_all_shipping_methods_returns_applicable_methods_with_listings` (function) — [saleor/order/tests/test_shipping_context.py:124]
- `test_get_all_shipping_methods_excludes_methods_without_channel_listing` (function) — [saleor/order/tests/test_shipping_context.py:145]

**`saleor/order/tests/test_tasks.py`**

- `test_expire_orders_task_check_voucher` (function) — [saleor/order/tests/test_tasks.py:26]

## How it works

The module's files, as provided to this run:

- `saleor/order/tests/__init__.py` (1 lines)
- `saleor/order/tests/benchmark/__init__.py` (1 lines)
- `saleor/order/tests/benchmark/test_fetch_order_prices.py` (22 lines)
- `saleor/order/tests/test_actions.py` (180 lines)
- `saleor/order/tests/test_base_order_line_total.py` (28 lines)
- `saleor/order/tests/test_base_order_total.py` (624 lines)
- `saleor/order/tests/test_calculate_prices.py` (756 lines)
- `saleor/order/tests/test_calculations.py` (1997 lines)
- `saleor/order/tests/test_fetch_order_prices_line_price_expiration.py` (1754 lines)
- `saleor/order/tests/test_fetch_order_prices_tax_app.py` (1749 lines)
- `saleor/order/tests/test_fetch_order_prices.py` (2041 lines)
- `saleor/order/tests/test_fetch.py` (155 lines)
- `saleor/order/tests/test_fulfillments_actions.py` (801 lines)
- `saleor/order/tests/test_notifications.py` (800 lines)
- `saleor/order/tests/test_order_actions_create_fulfillments_for_returned_products.py` (861 lines)
- `saleor/order/tests/test_order_actions_refund_products.py` (281 lines)
- `saleor/order/tests/test_order_actions.py` (3197 lines)
- `saleor/order/tests/test_order_search.py` (114 lines)
- `saleor/order/tests/test_order_utils.py` (803 lines)
- `saleor/order/tests/test_order.py` (60 lines)
- `saleor/order/tests/test_refresh_all_order_base_prices_and_discounts.py` (48 lines)
- `saleor/order/tests/test_refresh_order_base_prices_and_discounts.py` (48 lines)
- `saleor/order/tests/test_shipping_context.py` (169 lines)
- `saleor/order/tests/test_tasks.py` (68 lines)

## Interactions

- Imports from: `saleor/order`, `saleor/core`, `saleor/graphql`, `saleor/plugins/openid_connect`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....OrderStatus`
- `...FulfillmentLineData`
- `...FulfillmentStatus`
- `...OrderChargeStatus`
- `...OrderEvents`
- `...OrderGrantedRefundStatus`
- `...OrderOrigin`
- `...OrderStatus`
- `...account.models.User`
- `...base_calculations`
- `...calculations`
- `...calculations.fetch_order_prices_if_expired`
- `...channel.MarkAsPaidStrategy`
- `...checkout.fetch.fetch_checkout_info`
- `...checkout.fetch.fetch_checkout_lines`
- `...checkout.models.Checkout`
- `...core.exceptions.InsufficientStock`
- `...core.models.EventDelivery`
- `...core.notify.NotifyEventType`
- `...core.prices.quantize_price`
- `...core.taxes.TaxData`
- `...core.taxes.TaxLineData`
- `...core.taxes.zero_money`
- `...core.tests.utils.get_site_context_payload`
- `...core.utils.events.call_event`
- `...core.utils.translations.get_translation`
- `...core.weight.zero_weight`
- `...discount.DiscountType`
- `...discount.DiscountValueType`
- `...discount.RewardValueType`
- `...discount.VoucherType`
- `...discount.interface.VariantPromotionRuleInfo`
- `...discount.models.OrderDiscount`
- `...discount.models.OrderLineDiscount`
- `...discount.models.Promotion`
- `...discount.models.PromotionRule`
- `...discount.models.VoucherCustomer`
- `...discount.utils.voucher.validate_voucher_in_order`
- `...giftcard.GiftCardEvents`
- `...giftcard.const.GIFT_CARD_PAYMENT_GATEWAY_ID`
- `...giftcard.models.GiftCard`
- `...giftcard.models.GiftCardEvent`
- `...graphql.core.utils.to_global_id_or_none`
- `...graphql.order.utils.OrderLineData`
- `...graphql.tests.utils.get_graphql_content`
- `...order.OrderEvents`
- `...order.fetch.OrderLineInfo`
- `...order.fetch.fetch_order_info`
- `...order.notifications`
- `...order.utils.get_order_country`
- `...page.models.Page`
- `...page.models.PageType`
- `...payment.ChargeStatus`
- `...payment.TransactionEventType`
- `...payment.interface.RefundData`
- `...payment.model_helpers.get_subtotal`
- `...payment.models.Payment`
- `...plugins.PLUGIN_IDENTIFIER_PREFIX`
- `...plugins.avatax.plugin.DeprecatedAvataxPlugin`
- `...plugins.avatax.tests.conftest.plugin_configuration  # noqa: F401`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `537e8fdfc251` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
