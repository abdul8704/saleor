## Purpose

`saleor/graphql/order/tests/mutations` (`saleor/graphql/order/tests/mutations`) groups 39 source file(s) exposing 334 top-level declaration(s).

## Public surface

**`saleor/graphql/order/tests/mutations/test_draft_order_bulk_delete.py`**

- `test_delete_draft_orders` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_bulk_delete.py:24]
- `test_delete_draft_orders_exceeding_max_input_size` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_bulk_delete.py:51]
- `test_delete_draft_orders_by_user_no_channel_access` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_bulk_delete.py:81]
- `test_delete_draft_orders_by_app` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_bulk_delete.py:112]
- `test_delete_draft_orders_orders_with_transaction_item` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_bulk_delete.py:145]
- `test_draft_order_bulk_delete_with_voucher_and_include_draft_order_in_voucher_usage_false` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_bulk_delete.py:184]
- `test_draft_order_bulk_delete_with_voucher_and_include_draft_order_in_voucher_usage_true` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_bulk_delete.py:226]
- `test_fail_to_delete_non_draft_order_lines` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_bulk_delete.py:287]
- `test_delete_draft_order_lines` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_bulk_delete.py:310]
- `test_delete_draft_order_lines_by_user_no_channel_access` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_bulk_delete.py:336]
- `test_delete_draft_order_lines_by_app` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_bulk_delete.py:365]

**`saleor/graphql/order/tests/mutations/test_draft_order_complete.py`**

- `test_draft_order_complete` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:108]
- `test_draft_order_complete_no_automatically_confirm_all_new_orders` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:175]
- `test_draft_order_complete_by_user_no_channel_access` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:219]
- `test_draft_order_complete_by_app` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:242]
- `test_draft_order_complete_with_voucher` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:272]
- `test_draft_order_complete_with_invalid_voucher` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:356]
- `test_draft_order_complete_with_voucher_once_per_customer` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:380]
- `test_draft_order_complete_0_total` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:413]
- `test_draft_order_complete_without_sku` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:481]
- `test_draft_order_complete_with_out_of_stock_webhook` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:537]
- `test_draft_order_from_reissue_complete` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:570]
- `test_draft_order_complete_with_inactive_channel` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:620]
- `test_draft_order_complete_with_unavailable_variant` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:646]
- `test_draft_order_complete_channel_without_shipping_zones_assigned` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:674]
- `test_draft_order_complete_channel_with_shipping_zones_excluded_from_stock_calculation` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:709]
- `test_draft_order_complete_product_without_inventory_tracking` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:743]
- `test_draft_order_complete_not_available_shipping_method` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:790]
- `test_draft_order_complete_with_excluded_shipping_method` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:828]
- `test_draft_order_complete_with_not_excluded_shipping_method` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:859]
- `test_draft_order_complete_builtin_shipping_method_metadata_denormalization` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:888]
- `clear_shipping_metadata` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:913]
- `test_draft_order_complete_out_of_stock_variant` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:951]
- `test_draft_order_complete_existing_user_email_updates_user_field` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:983]
- `test_draft_order_complete_anonymous_user_email_sets_user_field_null` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1000]
- `test_draft_order_complete_anonymous_user_no_email` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1017]
- `test_draft_order_complete_drops_shipping_address` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1033]
- `test_draft_order_complete_unavailable_for_purchase` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1059]
- `test_draft_order_complete_preorders` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1092]
- `test_draft_order_complete_insufficient_stock_preorders` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1135]
- `test_draft_order_complete_not_draft_order` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1166]
- `test_draft_order_complete_display_gross_prices` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1181]
- `test_draft_order_complete_fails_with_invalid_tax_app` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1212]
- `test_draft_order_complete_force_tax_calculation_when_tax_error_was_saved` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1258]
- `test_draft_order_complete_calls_correct_tax_app` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1305]
- `test_draft_order_complete_calls_failing_plugin` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1351]
- `side_effect` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1361]
- `test_draft_order_complete_with_catalogue_and_order_discount` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1461]
- `test_draft_order_complete_with_catalogue_and_gift_discount` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1561]
- `test_draft_order_complete_with_invalid_address` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1665]
- `test_draft_order_complete_with_invalid_address_save_addresses_on` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_complete.py:1709]
- _…and 5 more in this file_

**`saleor/graphql/order/tests/mutations/test_draft_order_create.py`**

- `test_draft_order_create_with_voucher_entire_order` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:163]
- `test_draft_order_create_with_voucher_and_voucher_code` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:322]
- `test_draft_order_create_with_voucher_code_in_voucher_input` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:393]
- `test_draft_order_create_with_voucher_code` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:464]
- `test_draft_order_create_percentage_voucher` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:611]
- `test_draft_order_create_with_voucher_specific_product` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:727]
- `test_draft_order_create_with_voucher_apply_once_per_order` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:882]
- `test_draft_order_create_by_user_no_channel_access` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:1039]
- `test_draft_order_create_by_app` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:1087]
- `test_draft_order_create_with_voucher_including_drafts_in_voucher_usage` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:1140]
- `test_draft_order_create_with_voucher_including_drafts_in_voucher_usage_invalid_code` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:1229]
- `test_draft_order_create_with_voucher_code_including_drafts_in_voucher_usage` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:1291]
- `test_draft_order_create_voucher_code_including_drafts_in_voucher_usage_invalid_code` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:1381]
- `test_draft_order_create_voucher_including_drafts_in_voucher_usage_invalid_code` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:1442]
- `test_draft_order_create_with_same_variant_and_force_new_line` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:1504]
- `test_draft_order_create_with_inactive_channel` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:1604]
- `test_draft_order_create_without_sku` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:1677]
- `test_draft_order_create_variant_with_0_price` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:1770]
- `test_draft_order_create_tax_error` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:1839]
- `test_draft_order_create_with_voucher_not_assigned_to_order_channel` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:1899]
- `test_draft_order_create_with_product_and_variant_not_assigned_to_order_channel` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:1943]
- `test_draft_order_create_with_variant_not_assigned_to_order_channel` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:1983]
- `test_draft_order_create_without_channel` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:2023]
- `test_draft_order_create_with_negative_quantity_line` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:2061]
- `test_draft_order_create_with_channel_with_unpublished_product` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:2103]
- `test_draft_order_create_with_channel_with_unpublished_product_by_date` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:2162]
- `test_draft_order_create_with_channel` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:2221]
- `test_draft_order_create_product_without_shipping` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:2296]
- `test_draft_order_create_invalid_billing_address` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:2369]
- `test_draft_order_create_invalid_shipping_address` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:2428]
- `test_draft_order_create_invalid_address_skip_validation` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:2487]
- `test_draft_order_create_price_recalculation` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:2543]
- `test_draft_order_create_update_display_gross_prices` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:2601]
- `test_draft_order_create_with_non_unique_external_reference` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:2647]
- `test_draft_order_create_with_custom_price_in_order_line` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:2676]
- `test_draft_order_create_with_custom_price_and_catalogue_promotion` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:2749]
- `test_draft_order_create_product_catalogue_promotion` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:2884]
- `test_draft_order_create_product_catalogue_promotion_flat_taxes` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:3026]
- `test_draft_order_create_order_promotion_flat_rates` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:3174]
- `test_draft_order_create_gift_promotion_flat_rates` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_create.py:3295]
- _…and 17 more in this file_

**`saleor/graphql/order/tests/mutations/test_draft_order_delete.py`**

- `test_draft_order_delete` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_delete.py:30]
- `test_draft_order_delete_non_draft_order` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_delete.py:56]
- `test_draft_order_delete_draft_with_transactions` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_delete.py:74]
- `test_draft_order_delete_by_user_no_channel_access` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_delete.py:101]
- `test_draft_order_delete_by_app` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_delete.py:124]
- `test_draft_order_delete_product` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_delete.py:146]
- `test_draft_order_delete_by_external_reference` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_delete.py:186]
- `test_draft_order_delete_by_both_id_and_external_reference` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_delete.py:210]
- `test_draft_order_delete_by_external_reference_not_existing` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_delete.py:230]
- `test_draft_order_delete_release_voucher_codes_multiple_use` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_delete.py:248]
- `test_draft_order_delete_release_voucher_codes_single_use` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_delete.py:276]
- `test_draft_order_delete_do_not_trigger_sync_webhooks` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_delete.py:309]
- `test_draft_order_delete_with_voucher_and_include_draft_order_in_voucher_usage_false` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_delete.py:355]
- `test_draft_order_delete_with_voucher_and_include_draft_order_in_voucher_usage_true` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_delete.py:392]

**`saleor/graphql/order/tests/mutations/test_draft_order_update.py`**

- `test_draft_order_update_existing_channel_id` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:181]
- `test_draft_order_update_voucher_not_available` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:206]
- `test_draft_order_update_with_voucher_entire_order` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:233]
- `test_draft_order_update_with_voucher_specific_product` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:323]
- `test_draft_order_update_with_voucher_apply_once_per_order` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:429]
- `test_draft_order_update_clear_voucher` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:546]
- `test_draft_order_update_clear_voucher_code` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:612]
- `test_draft_order_update_clear_voucher_and_reduce_voucher_usage` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:678]
- `test_draft_order_update_clear_voucher_code_and_reduce_voucher_usage` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:748]
- `test_draft_order_update_with_voucher_and_voucher_code` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:818]
- `test_draft_order_update_with_voucher_including_drafts_in_voucher_usage` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:859]
- `test_draft_order_update_with_voucher_code_including_drafts_in_voucher_usage` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:924]
- `test_draft_order_update_voucher_including_drafts_in_voucher_usage_invalid_code` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:991]
- `test_draft_order_update_add_voucher_code_remove_order_promotion` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1035]
- `test_draft_order_update_add_voucher_code_remove_gift_promotion` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1083]
- `test_draft_order_update_remove_voucher_code_add_order_promotion` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1137]
- `test_draft_order_update_remove_voucher_code_add_gift_promotion` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1199]
- `test_draft_order_update_with_non_draft_order` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1263]
- `test_draft_order_update_invalid_address` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1283]
- `test_draft_order_update_invalid_address_skip_validation` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1319]
- `test_draft_order_update_by_user_no_channel_access` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1358]
- `test_draft_order_update_by_app` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1389]
- `test_draft_order_update_doing_nothing_generates_no_events` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1423]
- `test_draft_order_update_free_shipping_voucher` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1447]
- `test_draft_order_update_when_not_existing_customer_email_provided` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1515]
- `test_draft_order_update_assign_user_when_existing_customer_email_provided` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1540]
- `test_draft_order_update_by_external_reference` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1596]
- `test_draft_order_update_by_both_id_and_external_reference` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1630]
- `test_draft_order_update_by_external_reference_not_existing` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1656]
- `test_draft_order_update_with_non_unique_external_reference` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1678]
- `test_draft_order_update_shipping_method_from_different_channel` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1746]
- `test_draft_order_update_shipping_method_prices_updates` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1783]
- `test_draft_order_update_shipping_method_clear_with_none` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1826]
- `test_draft_order_update_shipping_method` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1870]
- `test_draft_order_update_sets_shipping_tax_details_to_none_when_default_tax_used` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1930]
- `test_draft_order_update_shipping_method_order_with_shipping_voucher` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:1982]
- `test_draft_order_update_no_shipping_method_channel_listings` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:2051]
- `test_draft_order_update_order_promotion` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:2083]
- `test_draft_order_update_gift_promotion` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:2137]
- `test_draft_order_update_with_cc_warehouse_as_shipping_method` (function) — [saleor/graphql/order/tests/mutations/test_draft_order_update.py:2208]
- _…and 29 more in this file_

**`saleor/graphql/order/tests/mutations/test_fulfillment_approve.py`**

- `test_fulfillment_approve` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_approve.py:42]
- `test_fulfillment_approve_by_user_no_channel_access` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_approve.py:78]
- `test_fulfillment_approve_by_app` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_approve.py:104]
- `test_fulfillment_approve_delete_products_before_approval_allow_stock_exceeded_true` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_approve.py:142]
- `test_fulfillment_approve_delete_products_before_approval_allow_stock_exceeded_false` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_approve.py:179]
- `test_fulfillment_approve_gift_cards_created` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_approve.py:237]
- `test_fulfillment_approve_when_stock_is_exceeded_and_flag_enabled` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_approve.py:307]
- `test_fulfillment_approve_when_stock_is_exceeded_and_flag_disabled` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_approve.py:349]
- `test_fulfillment_approve_partial_order_fulfill` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_approve.py:398]
- `test_fulfillment_approve_invalid_status` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_approve.py:450]
- `test_fulfillment_approve_order_unpaid` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_approve.py:465]
- `test_fulfillment_approve_preorder` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_approve.py:485]
- `test_fulfillment_approve_trigger_webhook_event` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_approve.py:513]

**`saleor/graphql/order/tests/mutations/test_fulfillment_cancel.py`**

- `test_cancel_fulfillment` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_cancel.py:29]
- `test_cancel_fulfillment_by_user_no_channel_access` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_cancel.py:63]
- `test_cancel_fulfillment_by_app` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_cancel.py:90]
- `test_cancel_fulfillment_for_order_with_gift_card_lines` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_cancel.py:131]
- `test_cancel_fulfillment_no_warehouse_id` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_cancel.py:155]
- `test_cancel_fulfillment_awaiting_approval` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_cancel.py:187]
- `test_cancel_fulfillment_awaiting_approval_warehouse_specified` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_cancel.py:216]
- `test_cancel_fulfillment_canceled_state` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_cancel.py:248]
- `test_cancel_fulfillment_warehouse_without_stock` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_cancel.py:267]

**`saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py`**

- `test_fulfillment_refund_products_by_user_no_channel_access` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:50]
- `test_fulfillment_refund_products_with_action_requested_by_app` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:83]
- `test_fulfillment_refund_products_with_back_in_stock_webhook` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:131]
- `test_fulfillment_refund_gift_card_products` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:165]
- `test_fulfillment_refund_products_order_without_payment` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:205]
- `test_fulfillment_refund_products_amount_and_shipping_costs` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:223]
- `test_fulfillment_refund_products_amount_costs_for_order_with_gift_card_lines` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:255]
- `test_fulfillment_refund_products_refund_raising_payment_error` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:292]
- `test_fulfillment_refund_products_order_lines` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:326]
- `test_fulfillment_refund_products_order_lines_quantity_bigger_than_total` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:373]
- `test_fulfillment_refund_products_order_lines_quantity_bigger_than_unfulfilled` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:401]
- `test_fulfillment_refund_products_fulfillment_lines` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:433]
- `test_fulfillment_refund_products_waiting_fulfillment_lines` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:490]
- `test_fulfillment_refund_products_gift_card_fulfillment_line` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:551]
- `test_fulfillment_refund_products_fulfillment_lines_quantity_bigger_than_total` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:593]
- `test_fulfillment_refund_products_amount_bigger_than_captured_amount` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:627]
- `test_fulfillment_refund_products_fulfillment_lines_include_shipping_costs` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:663]
- `test_fulfillment_refund_products_order_lines_include_shipping_costs` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:721]
- `test_fulfillment_refund_products_fulfillment_lines_custom_amount` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:773]
- `test_fulfillment_refund_products_order_lines_custom_amount` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:833]
- `test_fulfillment_refund_products_fulfillment_lines_and_order_lines` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:884]
- `test_fulfillment_refund_products_calls_order_refunded` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py:990]

**`saleor/graphql/order/tests/mutations/test_fulfillment_return_products_by_app.py`**

- `test_fulfillment_return_products_app_omits_reason_reference_when_configured` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products_by_app.py:9]

**`saleor/graphql/order/tests/mutations/test_fulfillment_return_products_reason.py`**

- `test_fulfillment_return_products_with_global_reason_and_reason_reference` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products_reason.py:30]
- `test_fulfillment_return_products_staff_omits_reason_reference_when_configured` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products_reason.py:88]
- `test_fulfillment_return_products_with_per_line_reason` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products_reason.py:135]
- `test_fulfillment_return_products_per_line_reason_reference_when_not_configured` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products_reason.py:191]
- `test_fulfillment_return_products_per_line_reason_reference_wrong_page_type` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products_reason.py:240]
- `test_fulfillment_return_products_reason_fields_resolve` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products_reason.py:301]
- `test_fulfillment_return_products_fulfillment_lines_with_global_and_per_line_reasons` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products_reason.py:368]
- `test_fulfillment_return_products_fulfillment_lines_mixed_per_line_reason` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products_reason.py:451]
- `test_fulfillment_return_products_refund_requires_reason_reference_for_staff` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products_reason.py:526]
- `test_fulfillment_return_products_refund_stores_reason_reference` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products_reason.py:583]
- `test_fulfillment_return_products_replace_with_per_line_reasons` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products_reason.py:648]

**`saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py`**

- `test_fulfillment_return_products_by_user_no_channel_access` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:71]
- `test_fulfillment_return_products_by_app` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:107]
- `test_fulfillment_return_products_order_without_payment` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:156]
- `test_fulfillment_return_products_amount_and_shipping_costs` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:177]
- `test_fulfillment_return_products_amount_order_with_gift_card` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:213]
- `test_fulfillment_return_products_refund_raising_payment_error` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:256]
- `test_fulfillment_return_products_order_lines` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:290]
- `test_fulfillment_return_products_gift_card_order_line` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:412]
- `test_fulfillment_return_products_order_lines_quantity_bigger_than_total` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:462]
- `test_fulfillment_return_products_order_lines_quantity_bigger_than_unfulfilled` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:492]
- `test_fulfillment_return_products_order_lines_custom_amount` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:524]
- `test_fulfillment_return_products_fulfillment_lines` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:580]
- `test_fulfillment_return_products_gift_card_fulfillment_line` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:714]
- `test_fulfillment_return_products_fulfillment_lines_quantity_bigger_than_total` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:770]
- `test_fulfillment_return_products_amount_bigger_than_captured_amount` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:805]
- `test_fulfillment_return_products_lines_with_incorrect_status` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:841]
- `test_fulfillment_return_products_fulfillment_lines_include_shipping_costs` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:881]
- `test_fulfillment_return_products_fulfillment_lines_and_order_lines` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:942]
- `test_fulfillment_return_and_replace_products_calls_order_refunded_and_webhooks` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:1065]
- `test_fulfillment_return_products_calls_order_refunded_and_webhooks` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py:1155]

**`saleor/graphql/order/tests/mutations/test_fulfillment_update_tracking.py`**

- `test_fulfillment_update_tracking` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_update_tracking.py:28]
- `test_fulfillment_update_tracking_by_user_no_channel_access` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_update_tracking.py:47]
- `test_fulfillment_update_tracking_by_app` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_update_tracking.py:74]
- `test_fulfillment_update_tracking_send_notification_true` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_update_tracking.py:99]
- `test_fulfillment_update_tracking_send_notification_false` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_update_tracking.py:125]
- `test_fulfillment_tracking_number_updated_event_triggered` (function) — [saleor/graphql/order/tests/mutations/test_fulfillment_update_tracking.py:149]

**`saleor/graphql/order/tests/mutations/test_order_bulk_cancel.py`**

- `test_order_bulk_cancel` (function) — [saleor/graphql/order/tests/mutations/test_order_bulk_cancel.py:28]
- `test_order_bulk_cancel_by_user_no_channel_access` (function) — [saleor/graphql/order/tests/mutations/test_order_bulk_cancel.py:72]
- `test_order_bulk_cancel_with_back_in_stock_webhook` (function) — [saleor/graphql/order/tests/mutations/test_order_bulk_cancel.py:99]
- `test_order_bulk_cancel_as_app` (function) — [saleor/graphql/order/tests/mutations/test_order_bulk_cancel.py:122]
- `test_order_bulk_cancel_without_sku` (function) — [saleor/graphql/order/tests/mutations/test_order_bulk_cancel.py:172]

**`saleor/graphql/order/tests/mutations/test_order_cancel.py`**

- `test_order_cancel` (function) — [saleor/graphql/order/tests/mutations/test_order_cancel.py:33]
- `test_order_cancel_as_app` (function) — [saleor/graphql/order/tests/mutations/test_order_cancel.py:62]
- `test_order_cancel_with_bought_gift_cards` (function) — [saleor/graphql/order/tests/mutations/test_order_cancel.py:92]
- `test_order_cancel_no_channel_access` (function) — [saleor/graphql/order/tests/mutations/test_order_cancel.py:126]
- `test_order_cancel_skip_trigger_webhooks` (function) — [saleor/graphql/order/tests/mutations/test_order_cancel.py:159]

**`saleor/graphql/order/tests/mutations/test_order_capture.py`**

- `test_order_capture` (function) — [saleor/graphql/order/tests/mutations/test_order_capture.py:50]
- `test_order_capture_by_user_no_channel_access` (function) — [saleor/graphql/order/tests/mutations/test_order_capture.py:125]
- `test_order_capture_by_app` (function) — [saleor/graphql/order/tests/mutations/test_order_capture.py:148]
- `test_order_capture_triggers_webhooks` (function) — [saleor/graphql/order/tests/mutations/test_order_capture.py:192]
- `test_draft_order_capture_dont_triggers_fully_paid_webhook` (function) — [saleor/graphql/order/tests/mutations/test_order_capture.py:336]

**`saleor/graphql/order/tests/mutations/test_order_confirm.py`**

- `test_order_confirm` (function) — [saleor/graphql/order/tests/mutations/test_order_confirm.py:57]
- `test_order_confirm_without_sku` (function) — [saleor/graphql/order/tests/mutations/test_order_confirm.py:202]
- `test_order_confirm_unfulfilled` (function) — [saleor/graphql/order/tests/mutations/test_order_confirm.py:267]
- `test_order_confirm_no_products_in_order` (function) — [saleor/graphql/order/tests/mutations/test_order_confirm.py:285]
- `test_order_confirm_wont_call_capture_for_non_active_payment` (function) — [saleor/graphql/order/tests/mutations/test_order_confirm.py:306]
- `test_order_confirm_update_display_gross_prices` (function) — [saleor/graphql/order/tests/mutations/test_order_confirm.py:336]
- `test_order_confirm_by_user_no_channel_access` (function) — [saleor/graphql/order/tests/mutations/test_order_confirm.py:371]
- `test_order_confirm_by_app` (function) — [saleor/graphql/order/tests/mutations/test_order_confirm.py:411]
- `test_order_confirm_skip_address_validation` (function) — [saleor/graphql/order/tests/mutations/test_order_confirm.py:557]
- `test_order_confirm_triggers_webhooks` (function) — [saleor/graphql/order/tests/mutations/test_order_confirm.py:618]

**`saleor/graphql/order/tests/mutations/test_order_discount.py`**

- `test_add_order_discount_incorrect_values` (function) — [saleor/graphql/order/tests/mutations/test_order_discount.py:49]

**`saleor/graphql/order/tests/mutations/test_order_fulfill.py`**

- `test_order_fulfill_with_out_of_stock_webhook` (function) — [saleor/graphql/order/tests/mutations/test_order_fulfill.py:47]

**`saleor/graphql/order/tests/mutations/test_order_grant_refund_create_line_reason.py`**

- `test_with_per_line_reason_reference` (function) — [saleor/graphql/order/tests/mutations/test_order_grant_refund_create_line_reason.py:51]

**`saleor/graphql/order/tests/mutations/test_order_grant_refund_create_reason.py`**

- `test_grant_refund_with_reference_required_created_by_user` (function) — [saleor/graphql/order/tests/mutations/test_order_grant_refund_create_reason.py:102]

**`saleor/graphql/order/tests/mutations/test_order_grant_refund_create.py`**

- `test_grant_refund_by_user` (function) — [saleor/graphql/order/tests/mutations/test_order_grant_refund_create.py:109]

**`saleor/graphql/order/tests/mutations/test_order_grant_refund_update_line_reason.py`**

- `test_add_line_with_reason_reference` (function) — [saleor/graphql/order/tests/mutations/test_order_grant_refund_update_line_reason.py:51]

**`saleor/graphql/order/tests/mutations/test_order_grant_refund_update_reason.py`**

- `test_granted_refund_updated_when_status_blocks_action_and_only_reason_provided` (function) — [saleor/graphql/order/tests/mutations/test_order_grant_refund_update_reason.py:115]

**`saleor/graphql/order/tests/mutations/test_order_grant_refund_update.py`**

- `test_grant_refund_update_by_user` (function) — [saleor/graphql/order/tests/mutations/test_order_grant_refund_update.py:117]

**`saleor/graphql/order/tests/mutations/test_order_grant_refund_utils.py`**

- `refund_page_type` (function) — [saleor/graphql/order/tests/mutations/test_order_grant_refund_utils.py:16]
- `refund_page` (function) — [saleor/graphql/order/tests/mutations/test_order_grant_refund_utils.py:21]
- `test_resolves_valid_page` (function) — [saleor/graphql/order/tests/mutations/test_order_grant_refund_utils.py:30]
- `test_raises_graphql_error_for_wrong_type_id` (function) — [saleor/graphql/order/tests/mutations/test_order_grant_refund_utils.py:43]
- `test_raises_invalid_for_wrong_page_type` (function) — [saleor/graphql/order/tests/mutations/test_order_grant_refund_utils.py:56]

**`saleor/graphql/order/tests/mutations/test_order_line_delete.py`**

- `test_order_line_remove_with_back_in_stock_webhook` (function) — [saleor/graphql/order/tests/mutations/test_order_line_delete.py:49]

**`saleor/graphql/order/tests/mutations/test_order_mark_as_paid.py`**

- `test_paid_order_mark_as_paid_with_payment` (function) — [saleor/graphql/order/tests/mutations/test_order_mark_as_paid.py:40]
- `test_order_mark_as_paid_with_external_reference_with_payment` (function) — [saleor/graphql/order/tests/mutations/test_order_mark_as_paid.py:59]

**`saleor/graphql/order/tests/mutations/test_order_note_add.py`**

- `test_order_note_add_as_staff_user` (function) — [saleor/graphql/order/tests/mutations/test_order_note_add.py:42]

**`saleor/graphql/order/tests/mutations/test_order_note_update.py`**

- `test_order_note_update_as_staff_user` (function) — [saleor/graphql/order/tests/mutations/test_order_note_update.py:44]

**`saleor/graphql/order/tests/mutations/test_order_price_expiration.py`**

- `order_with_lines` (function) — [saleor/graphql/order/tests/mutations/test_order_price_expiration.py:34]
- `test_draft_order_update_shipping_address_invalidate_prices` (function) — [saleor/graphql/order/tests/mutations/test_order_price_expiration.py:40]
- `test_draft_order_update_billing_address_invalidate_prices` (function) — [saleor/graphql/order/tests/mutations/test_order_price_expiration.py:65]

**`saleor/graphql/order/tests/mutations/test_order_refund.py`**

- `test_order_refund` (function) — [saleor/graphql/order/tests/mutations/test_order_refund.py:34]

**`saleor/graphql/order/tests/mutations/test_order_update_shipping.py`**

- `test_order_update_shipping` (function) — [saleor/graphql/order/tests/mutations/test_order_update_shipping.py:44]

**`saleor/graphql/order/tests/mutations/test_order_update.py`**

- `test_order_update` (function) — [saleor/graphql/order/tests/mutations/test_order_update.py:43]

**`saleor/graphql/order/tests/mutations/test_order_void.py`**

- `test_order_void` (function) — [saleor/graphql/order/tests/mutations/test_order_void.py:33]
- `test_order_void_by_user_no_channel_access` (function) — [saleor/graphql/order/tests/mutations/test_order_void.py:52]

**`saleor/graphql/order/tests/mutations/test_utils.py`**

- `test_get_instance` (function) — [saleor/graphql/order/tests/mutations/test_utils.py:15]
- `test_get_instance_fail_multiple_identifiers` (function) — [saleor/graphql/order/tests/mutations/test_utils.py:29]
- `test_get_instance_fail_no_identifier` (function) — [saleor/graphql/order/tests/mutations/test_utils.py:43]
- `test_get_instance_fail_invalid_global_id_syntax` (function) — [saleor/graphql/order/tests/mutations/test_utils.py:54]
- `test_get_instance_fail_invalid_global_id_model` (function) — [saleor/graphql/order/tests/mutations/test_utils.py:62]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/order/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/order/tests/mutations/test_draft_order_bulk_delete.py` (393 lines)
- `saleor/graphql/order/tests/mutations/test_draft_order_complete.py` (2091 lines)
- `saleor/graphql/order/tests/mutations/test_draft_order_create.py` (4421 lines)
- `saleor/graphql/order/tests/mutations/test_draft_order_delete.py` (428 lines)
- `saleor/graphql/order/tests/mutations/test_draft_order_update.py` (4004 lines)
- `saleor/graphql/order/tests/mutations/test_fulfillment_approve.py` (541 lines)
- `saleor/graphql/order/tests/mutations/test_fulfillment_cancel.py` (308 lines)
- `saleor/graphql/order/tests/mutations/test_fulfillment_refund_products.py` (1067 lines)
- `saleor/graphql/order/tests/mutations/test_fulfillment_return_products_by_app.py` (52 lines)
- `saleor/graphql/order/tests/mutations/test_fulfillment_return_products_reason.py` (727 lines)
- `saleor/graphql/order/tests/mutations/test_fulfillment_return_products.py` (1244 lines)
- `saleor/graphql/order/tests/mutations/test_fulfillment_update_tracking.py` (175 lines)
- `saleor/graphql/order/tests/mutations/test_order_bulk_cancel.py` (217 lines)
- `saleor/graphql/order/tests/mutations/test_order_bulk_create.py` (68 lines)
- `saleor/graphql/order/tests/mutations/test_order_cancel.py` (254 lines)
- `saleor/graphql/order/tests/mutations/test_order_capture.py` (388 lines)
- `saleor/graphql/order/tests/mutations/test_order_confirm.py` (725 lines)
- `saleor/graphql/order/tests/mutations/test_order_discount.py` (68 lines)
- `saleor/graphql/order/tests/mutations/test_order_fulfill.py` (62 lines)
- `saleor/graphql/order/tests/mutations/test_order_grant_refund_create_line_reason.py` (89 lines)
- `saleor/graphql/order/tests/mutations/test_order_grant_refund_create_reason.py` (119 lines)
- `saleor/graphql/order/tests/mutations/test_order_grant_refund_create.py` (119 lines)
- `saleor/graphql/order/tests/mutations/test_order_grant_refund_update_line_reason.py` (89 lines)
- `saleor/graphql/order/tests/mutations/test_order_grant_refund_update_reason.py` (121 lines)
- `saleor/graphql/order/tests/mutations/test_order_grant_refund_update.py` (119 lines)
- `saleor/graphql/order/tests/mutations/test_order_grant_refund_utils.py` (71 lines)
- `saleor/graphql/order/tests/mutations/test_order_line_delete.py` (71 lines)
- `saleor/graphql/order/tests/mutations/test_order_line_update.py` (54 lines)
- `saleor/graphql/order/tests/mutations/test_order_lines_create.py` (51 lines)
- `saleor/graphql/order/tests/mutations/test_order_mark_as_paid.py` (61 lines)
- `saleor/graphql/order/tests/mutations/test_order_note_add.py` (68 lines)
- `saleor/graphql/order/tests/mutations/test_order_note_update.py` (73 lines)
- `saleor/graphql/order/tests/mutations/test_order_price_expiration.py` (83 lines)
- `saleor/graphql/order/tests/mutations/test_order_refund.py` (66 lines)
- `saleor/graphql/order/tests/mutations/test_order_update_shipping.py` (63 lines)
- `saleor/graphql/order/tests/mutations/test_order_update.py` (66 lines)
- `saleor/graphql/order/tests/mutations/test_order_void.py` (64 lines)
- `saleor/graphql/order/tests/mutations/test_utils.py` (65 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/graphql`, `saleor/graphql/order/mutations`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....account.models.Address`
- `.....account.models.CustomerEvent`
- `.....account.models.User`
- `.....channel.MarkAsPaidStrategy`
- `.....checkout.AddressType`
- `.....core.EventDeliveryStatus`
- `.....core.JobStatus`
- `.....core.exceptions.InsufficientStock`
- `.....core.exceptions.InsufficientStockData`
- `.....core.models.EventDelivery`
- `.....core.notification.utils.get_site_context`
- `.....core.notify.NotifyEventType`
- `.....core.prices.quantize_price`
- `.....core.taxes.TaxError`
- `.....core.taxes.zero_money`
- `.....core.taxes.zero_taxed_money`
- `.....core.tests.utils.get_site_context_payload`
- `.....discount.DiscountType`
- `.....discount.DiscountValueType`
- `.....discount.RewardType`
- `.....discount.RewardValueType`
- `.....discount.VoucherType`
- `.....discount.models.OrderDiscount`
- `.....discount.models.OrderLineDiscount`
- `.....discount.models.PromotionRule`
- `.....discount.models.Voucher`
- `.....discount.models.VoucherChannelListing`
- `.....discount.models.VoucherCode`
- `.....discount.models.VoucherCustomer`
- `.....discount.utils.manual_discount.DiscountValueType`
- `.....giftcard.GiftCardEvents`
- `.....giftcard.events.gift_cards_bought_event`
- `.....giftcard.models.GiftCard`
- `.....giftcard.models.GiftCardEvent`
- `.....invoice.models.Invoice`
- `.....order.FulfillmentLineData`
- `.....order.FulfillmentStatus`
- `.....order.OrderEvents`
- `.....order.OrderGrantedRefundStatus`
- `.....order.OrderOrigin`
- `.....order.OrderStatus`
- `.....order.actions.MARK_AS_PAID_TRANSACTION_NAME`
- `.....order.actions.WEBHOOK_EVENTS_FOR_ORDER_CANCELED`
- `.....order.actions.call_order_event`
- `.....order.actions.cancel_order`
- `.....order.actions.fulfill_order_lines`
- `.....order.actions.order_charged`
- `.....order.actions.order_created`
- `.....order.actions.order_fulfilled`
- `.....order.calculations.fetch_order_prices_if_expired`
- `.....order.calculations.process_order_prices`
- `.....order.error_codes.OrderBulkCreateErrorCode`
- `.....order.error_codes.OrderErrorCode`
- `.....order.error_codes.OrderGrantRefundCreateLineErrorCode`
- `.....order.error_codes.OrderNoteAddErrorCode`
- `.....order.error_codes.OrderNoteUpdateErrorCode`
- `.....order.events`
- `.....order.fetch.OrderLineInfo`
- `.....order.fetch.fetch_order_info`
- `.....order.interface.OrderTaxedPricesData`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `59d35dc33585` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
