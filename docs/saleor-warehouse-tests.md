## Purpose

`saleor/warehouse/tests` (`saleor/warehouse/tests`) groups 12 source file(s) exposing 195 top-level declaration(s).

## Public surface

**`saleor/warehouse/tests/test_channel_stock_availability.py`**

- `test_out_of_stock_fires_when_only_warehouse_in_bucket` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:27]
- `test_out_of_stock_does_not_fire_when_another_warehouse_has_stock` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:48]
- `test_out_of_stock_fires_even_when_cc_warehouse_in_channel_has_stock` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:72]
- `test_out_of_stock_in_cc_warehouse_fires_click_and_collect_event` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:98]
- `test_back_in_stock_fires_when_all_other_warehouses_in_bucket_are_empty` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:125]
- `test_back_in_stock_does_not_fire_when_another_warehouse_already_has_stock` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:149]
- `test_does_not_fire_when_warehouse_belongs_to_no_channels` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:173]
- `test_fires_only_for_channels_whose_bucket_is_empty` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:193]
- `test_out_of_stock_fires_when_other_warehouse_has_only_fully_allocated_stock` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:222]
- `test_out_of_stock_ignores_stocks_of_other_variants_in_same_bucket` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:251]
- `test_out_of_stock_ignores_warehouse_stock_attached_to_different_channel` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:284]
- `test_trigger_forwards_site_settings_requestor_and_webhooks` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:311]
- `test_bulk_out_of_stock_fires_for_multiple_stocks_in_same_warehouse` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:330]
- `test_bulk_out_of_stock_does_not_fire_when_other_warehouse_covers_all_variants` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:353]
- `test_bulk_out_of_stock_fires_selectively_when_other_warehouse_covers_only_one_variant` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:391]
- `test_bulk_out_of_stock_deduplicates_same_variant_across_warehouses_in_channel` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:429]
- `test_bulk_out_of_stock_warehouse_a_is_other_for_warehouse_b_stock` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:459]
- `test_bulk_out_of_stock_mixed_cc_and_non_cc_stocks` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:504]
- `test_bulk_out_of_stock_multi_channel_fires_per_channel_independently` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:540]
- `test_bulk_out_of_stock_empty_list_does_not_fire` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:568]
- `test_bulk_out_of_stock_two_different_variants_fires_for_each` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:579]
- `test_bulk_out_of_stock_deduplicates_same_variant_multiple_warehouses_and_channels` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:606]
- `test_bulk_out_of_stock_different_variants_partial_coverage_by_other_warehouse` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:637]
- `test_bulk_back_in_stock_fires_for_multiple_stocks_in_same_warehouse` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:689]
- `test_bulk_back_in_stock_does_not_fire_when_other_warehouse_covers_all_variants` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:713]
- `test_bulk_back_in_stock_fires_selectively_when_other_warehouse_covers_only_one_variant` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:751]
- `test_bulk_back_in_stock_deduplicates_same_variant_across_warehouses_in_channel` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:789]
- `test_bulk_back_in_stock_warehouse_a_is_other_for_warehouse_b_stock` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:821]
- `test_bulk_back_in_stock_mixed_cc_and_non_cc_stocks` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:866]
- `test_bulk_back_in_stock_multi_channel_fires_per_channel_independently` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:902]
- `test_bulk_back_in_stock_empty_list_does_not_fire` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:930]
- `test_bulk_back_in_stock_two_different_variants_fires_for_each` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:941]
- `test_bulk_back_in_stock_deduplicates_same_variant_multiple_warehouses_and_channels` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:968]
- `test_bulk_back_in_stock_different_variants_partial_coverage_by_other_warehouse` (function) — [saleor/warehouse/tests/test_channel_stock_availability.py:1001]

**`saleor/warehouse/tests/test_preorder_availability.py`**

- `test_check_stock_and_preorder_quantity` (function) — [saleor/warehouse/tests/test_preorder_availability.py:22]
- `test_check_stock_and_preorder_quantity_bulk` (function) — [saleor/warehouse/tests/test_preorder_availability.py:52]
- `test_check_preorder_threshold_bulk_channel_threshold` (function) — [saleor/warehouse/tests/test_preorder_availability.py:97]
- `test_check_preorder_reserved_threshold_bulk_channel_threshold` (function) — [saleor/warehouse/tests/test_preorder_availability.py:128]
- `test_check_preorder_reserved_threshold_bulk_global_threshold` (function) — [saleor/warehouse/tests/test_preorder_availability.py:197]
- `test_check_preorder_threshold_bulk_global_threshold` (function) — [saleor/warehouse/tests/test_preorder_availability.py:269]
- `test_check_preorder_threshold_bulk_global_and_channel_threshold` (function) — [saleor/warehouse/tests/test_preorder_availability.py:305]

**`saleor/warehouse/tests/test_preorder_complete.py`**

- `test_deactivate_preorder_for_variant` (function) — [saleor/warehouse/tests/test_preorder_complete.py:8]
- `test_deactivate_preorder_for_variant_order_without_shipping_method` (function) — [saleor/warehouse/tests/test_preorder_complete.py:65]
- `test_deactivate_preorder_for_variant_existing_stock` (function) — [saleor/warehouse/tests/test_preorder_complete.py:100]

**`saleor/warehouse/tests/test_preorder_reservations_management.py`**

- `test_reserve_preorders` (function) — [saleor/warehouse/tests/test_preorder_reservations_management.py:17]
- `test_preorder_reservation_skips_prev_reservation_delete_if_replace_is_disabled` (function) — [saleor/warehouse/tests/test_preorder_reservations_management.py:35]
- `test_preorder_reservation_removes_previous_reservations_for_checkout` (function) — [saleor/warehouse/tests/test_preorder_reservations_management.py:60]
- `test_preorder_reservation_fails_if_there_is_not_enough_channel_threshold_available` (function) — [saleor/warehouse/tests/test_preorder_reservations_management.py:86]
- `test_preorder_reservation_fails_if_channel_threshold_was_allocated` (function) — [saleor/warehouse/tests/test_preorder_reservations_management.py:107]
- `test_preorder_reservation_fails_if_channel_threshold_was_reserved` (function) — [saleor/warehouse/tests/test_preorder_reservations_management.py:139]
- `test_preorder_reservation_fails_if_global_threshold_was_allocated` (function) — [saleor/warehouse/tests/test_preorder_reservations_management.py:179]
- `test_preorder_reservation_fails_if_global_threshold_was_reserved` (function) — [saleor/warehouse/tests/test_preorder_reservations_management.py:219]
- `test_preorder_reservation_fails_if_there_is_not_enough_global_threshold_available` (function) — [saleor/warehouse/tests/test_preorder_reservations_management.py:268]

**`saleor/warehouse/tests/test_stock_availability.py`**

- `test_check_stock_quantity` (function) — [saleor/warehouse/tests/test_stock_availability.py:18]
- `test_check_stock_quantity_out_of_stock` (function) — [saleor/warehouse/tests/test_stock_availability.py:31]
- `test_check_stock_quantity_with_allocations` (function) — [saleor/warehouse/tests/test_stock_availability.py:42]
- `test_check_stock_quantity_with_allocations_out_of_stock` (function) — [saleor/warehouse/tests/test_stock_availability.py:60]
- `test_check_stock_quantity_with_reservations` (function) — [saleor/warehouse/tests/test_stock_availability.py:73]
- `test_check_stock_quantity_with_reservations_excluding_given_checkout_lines` (function) — [saleor/warehouse/tests/test_stock_availability.py:92]
- `test_check_stock_quantity_without_stocks` (function) — [saleor/warehouse/tests/test_stock_availability.py:115]
- `test_check_stock_quantity_without_one_stock` (function) — [saleor/warehouse/tests/test_stock_availability.py:127]
- `test_get_available_quantity` (function) — [saleor/warehouse/tests/test_stock_availability.py:141]
- `test_get_available_quantity_without_allocation` (function) — [saleor/warehouse/tests/test_stock_availability.py:151]
- `test_get_available_quantity_with_allocations` (function) — [saleor/warehouse/tests/test_stock_availability.py:162]
- `test_get_available_quantity_with_reservations` (function) — [saleor/warehouse/tests/test_stock_availability.py:177]
- `test_get_available_quantity_with_allocations_and_reservations` (function) — [saleor/warehouse/tests/test_stock_availability.py:193]
- `test_get_available_quantity_with_reservations_excluding_given_checkout_lines` (function) — [saleor/warehouse/tests/test_stock_availability.py:209]
- `test_get_available_quantity_without_stocks` (function) — [saleor/warehouse/tests/test_stock_availability.py:229]
- `test_check_stock_quantity_bulk` (function) — [saleor/warehouse/tests/test_stock_availability.py:240]
- `test_check_stock_quantity_bulk_no_channel_shipping_zones` (function) — [saleor/warehouse/tests/test_stock_availability.py:295]
- `test_check_stock_quantity_bulk_no_channel_shipping_zones_excluded_from_stock_calculations` (function) — [saleor/warehouse/tests/test_stock_availability.py:318]
- `test_check_stock_quantity_bulk_with_reservations` (function) — [saleor/warehouse/tests/test_stock_availability.py:343]
- `test_check_stock_quantity_no_shipping_zones_included` (function) — [saleor/warehouse/tests/test_stock_availability.py:405]
- `test_check_stock_quantity_no_shipping_zones_excluded_from_stock_calculations` (function) — [saleor/warehouse/tests/test_stock_availability.py:423]
- `test_get_available_quantity_no_shipping_zones_included` (function) — [saleor/warehouse/tests/test_stock_availability.py:443]
- `test_get_available_quantity_no_shipping_zones_excluded_from_stock_calculations` (function) — [saleor/warehouse/tests/test_stock_availability.py:462]
- `test_check_stock_quantity_country_not_in_zone_include_shipping_zones` (function) — [saleor/warehouse/tests/test_stock_availability.py:481]
- `test_check_stock_quantity_country_not_in_zone_shipping_zones_excluded_from_stock_calculations` (function) — [saleor/warehouse/tests/test_stock_availability.py:501]
- `test_check_stock_and_preorder_quantity_no_shipping_zones_included` (function) — [saleor/warehouse/tests/test_stock_availability.py:523]
- `test_check_stock_and_preorder_quantity_no_shipping_zones_excluded_from_stock_calculations` (function) — [saleor/warehouse/tests/test_stock_availability.py:541]
- `test_is_product_in_stock_no_shipping_zones_included` (function) — [saleor/warehouse/tests/test_stock_availability.py:561]
- `test_is_product_in_stock_no_shipping_zones_excluded_from_stock_calculations` (function) — [saleor/warehouse/tests/test_stock_availability.py:581]

**`saleor/warehouse/tests/test_stock_management.py`**

- `test_allocate_stocks` (function) — [saleor/warehouse/tests/test_stock_management.py:27]
- `test_allocate_stocks_multiple_lines_the_highest_stock_strategy` (function) — [saleor/warehouse/tests/test_stock_management.py:49]
- `test_allocate_stock_many_stocks_the_highest_stock_strategy` (function) — [saleor/warehouse/tests/test_stock_management.py:94]
- `test_allocate_stocks_the_highest_stock_strategy_with_collection_point` (function) — [saleor/warehouse/tests/test_stock_management.py:115]
- `test_allocate_stock_many_stocks_prioritize_sorting_order_strategy` (function) — [saleor/warehouse/tests/test_stock_management.py:151]
- `test_allocate_stock_prioritize_sorting_order_strategy_with_collection_point` (function) — [saleor/warehouse/tests/test_stock_management.py:204]
- `test_allocate_stock_with_reservations_the_highest_stock_strategy` (function) — [saleor/warehouse/tests/test_stock_management.py:257]
- `test_allocate_stock_with_reservations_prioritize_sorting_order_strategy` (function) — [saleor/warehouse/tests/test_stock_management.py:283]
- `test_allocate_stock_insufficient_stock_due_to_reservations` (function) — [saleor/warehouse/tests/test_stock_management.py:337]
- `test_allocate_stock_many_stocks_partially_allocated` (function) — [saleor/warehouse/tests/test_stock_management.py:363]
- `test_allocate_stock_partially_allocated_insufficient_stocks` (function) — [saleor/warehouse/tests/test_stock_management.py:404]
- `test_allocate_stocks_no_channel_shipping_zones` (function) — [saleor/warehouse/tests/test_stock_management.py:427]
- `test_allocate_stocks_no_channel_shipping_zones_excluded_from_stock_calculations` (function) — [saleor/warehouse/tests/test_stock_management.py:450]
- `test_allocate_stock_insufficient_stocks` (function) — [saleor/warehouse/tests/test_stock_management.py:472]
- `test_allocate_stock_insufficient_stocks_for_multiple_lines` (function) — [saleor/warehouse/tests/test_stock_management.py:494]
- `test_deallocate_stock` (function) — [saleor/warehouse/tests/test_stock_management.py:536]
- `test_deallocate_stock_when_quantity_less_than_zero` (function) — [saleor/warehouse/tests/test_stock_management.py:561]
- `test_deallocate_stock_partially` (function) — [saleor/warehouse/tests/test_stock_management.py:584]
- `test_deallocate_stock_many_allocations` (function) — [saleor/warehouse/tests/test_stock_management.py:609]
- `test_deallocate_stock_many_allocations_partially` (function) — [saleor/warehouse/tests/test_stock_management.py:626]
- `test_increase_stock_without_allocate` (function) — [saleor/warehouse/tests/test_stock_management.py:643]
- `test_increase_stock_with_allocate` (function) — [saleor/warehouse/tests/test_stock_management.py:660]
- `test_increase_stock_with_new_allocation` (function) — [saleor/warehouse/tests/test_stock_management.py:677]
- `test_increase_allocations` (function) — [saleor/warehouse/tests/test_stock_management.py:692]
- `test_increase_allocations_with_multiple_allocations_for_the_same_stock` (function) — [saleor/warehouse/tests/test_stock_management.py:731]
- `test_increase_allocation_insufficient_stock` (function) — [saleor/warehouse/tests/test_stock_management.py:800]
- `test_increase_stock_with_back_in_stock_webhook_triggered_without_allocation` (function) — [saleor/warehouse/tests/test_stock_management.py:839]
- `test_decrease_stock` (function) — [saleor/warehouse/tests/test_stock_management.py:856]
- `test_decrease_allocations` (function) — [saleor/warehouse/tests/test_stock_management.py:886]
- `test_decrease_stock_multiple_lines` (function) — [saleor/warehouse/tests/test_stock_management.py:915]
- `test_decrease_stock_multiple_lines_deallocate_stock_raises_error` (function) — [saleor/warehouse/tests/test_stock_management.py:955]
- `test_decrease_stock_partially` (function) — [saleor/warehouse/tests/test_stock_management.py:1030]
- `test_decrease_stock_many_allocations` (function) — [saleor/warehouse/tests/test_stock_management.py:1057]
- `test_decrease_stock_many_allocations_partially` (function) — [saleor/warehouse/tests/test_stock_management.py:1084]
- `test_decrease_stock_more_then_allocated` (function) — [saleor/warehouse/tests/test_stock_management.py:1111]
- `test_decrease_stock_insufficient_stock` (function) — [saleor/warehouse/tests/test_stock_management.py:1145]
- `test_deallocate_stock_for_orders` (function) — [saleor/warehouse/tests/test_stock_management.py:1175]
- `test_deallocate_stock_for_orders_with_multiple_allocations_from_the_same_stock` (function) — [saleor/warehouse/tests/test_stock_management.py:1200]
- `test_increase_stock_with_back_in_stock_webhook_not_triggered` (function) — [saleor/warehouse/tests/test_stock_management.py:1251]
- `test_increase_stock_with_back_in_stock_webhook_not_triggered_with_allocation` (function) — [saleor/warehouse/tests/test_stock_management.py:1272]
- _…and 14 more in this file_

**`saleor/warehouse/tests/test_stock_reservations_management.py`**

- `test_reserve_stocks` (function) — [saleor/warehouse/tests/test_stock_reservations_management.py:16]
- `test_stocks_reservation_skips_prev_reservation_delete_if_replace_is_disabled` (function) — [saleor/warehouse/tests/test_stock_reservations_management.py:40]
- `test_multiple_stocks_reserved_if_single_stock_is_not_enough_highest_stock_strategy` (function) — [saleor/warehouse/tests/test_stock_reservations_management.py:65]
- `test_multiple_stocks_reserved_if_single_stock_is_not_enough_sorting_order_strategy` (function) — [saleor/warehouse/tests/test_stock_reservations_management.py:114]
- `test_stocks_reservation_removes_previous_reservations_for_checkout` (function) — [saleor/warehouse/tests/test_stock_reservations_management.py:185]
- `test_stock_reservation_fails_if_there_is_not_enough_stock_available` (function) — [saleor/warehouse/tests/test_stock_reservations_management.py:215]
- `test_stock_reservation_fails_if_there_is_no_stock` (function) — [saleor/warehouse/tests/test_stock_reservations_management.py:236]
- `test_stock_reservation_accounts_for_order_allocations` (function) — [saleor/warehouse/tests/test_stock_reservations_management.py:253]
- `test_stock_reservation_accounts_for_order_allocations_and_reservations` (function) — [saleor/warehouse/tests/test_stock_reservations_management.py:278]
- `test_reserve_stocks_no_shipping_zones_included` (function) — [saleor/warehouse/tests/test_stock_reservations_management.py:321]
- `test_reserve_stocks_no_shipping_zones_excluded_from_stock_calculations` (function) — [saleor/warehouse/tests/test_stock_reservations_management.py:344]

**`saleor/warehouse/tests/test_stock.py`**

- `variant_with_stocks_in_two_channels` (function) — [saleor/warehouse/tests/test_stock.py:9]
- `test_stocks_for_country` (function) — [saleor/warehouse/tests/test_stock.py:45]
- `test_stock_for_country_does_not_exists` (function) — [saleor/warehouse/tests/test_stock.py:63]
- `test_stocks_for_country_warehouse_with_given_channel_do_not_exist` (function) — [saleor/warehouse/tests/test_stock.py:82]
- `test_for_channel_returns_stocks_from_channel_warehouses` (function) — [saleor/warehouse/tests/test_stock.py:97]
- `test_for_channel_excludes_stocks_from_other_channel` (function) — [saleor/warehouse/tests/test_stock.py:115]
- `test_for_channel_not_available` (function) — [saleor/warehouse/tests/test_stock.py:133]
- `test_get_variant_stocks_with_shipping_zones` (function) — [saleor/warehouse/tests/test_stock.py:151]
- `test_get_variant_stocks_with_shipping_zones_no_zone_match` (function) — [saleor/warehouse/tests/test_stock.py:173]
- `test_get_variant_stocks_without_shipping_zones` (function) — [saleor/warehouse/tests/test_stock.py:196]
- `test_get_variants_stocks_with_shipping_zones` (function) — [saleor/warehouse/tests/test_stock.py:221]
- `test_get_variants_stocks_without_shipping_zones` (function) — [saleor/warehouse/tests/test_stock.py:243]
- `test_get_product_stocks_with_shipping_zones` (function) — [saleor/warehouse/tests/test_stock.py:267]
- `test_get_product_stocks_without_shipping_zones` (function) — [saleor/warehouse/tests/test_stock.py:295]

**`saleor/warehouse/tests/test_tasks.py`**

- `test_delete_empty_allocations_task` (function) — [saleor/warehouse/tests/test_tasks.py:14]
- `test_delete_expired_reservations_task_deletes_expired_stock_reservations` (function) — [saleor/warehouse/tests/test_tasks.py:28]
- `test_delete_expired_reservations_task_skips_active_stock_reservations` (function) — [saleor/warehouse/tests/test_tasks.py:38]
- `test_delete_expired_reservations_task_deletes_expired_preorder_reservations` (function) — [saleor/warehouse/tests/test_tasks.py:49]
- `test_delete_expired_reservations_task_skips_active_preorder_reservations` (function) — [saleor/warehouse/tests/test_tasks.py:59]
- `test_update_stocks_quantity_allocated_task` (function) — [saleor/warehouse/tests/test_tasks.py:79]
- `test_update_stocks_quantity_allocated_task_stock_without_allocations` (function) — [saleor/warehouse/tests/test_tasks.py:96]

**`saleor/warehouse/tests/test_warehouse.py`**

- `test_applicable_for_click_and_collect_finds_warehouse_with_all_and_local` (function) — [saleor/warehouse/tests/test_warehouse.py:9]
- `test_applicable_for_click_and_collect_warehouse_with_all_not_available_in_channel` (function) — [saleor/warehouse/tests/test_warehouse.py:35]
- `test_applicable_for_click_and_collect_quantity_exceeded` (function) — [saleor/warehouse/tests/test_warehouse.py:56]
- `test_applicable_for_click_and_collect_quantity_exceeded_for_local` (function) — [saleor/warehouse/tests/test_warehouse.py:81]
- `test_applicable_for_click_and_collect_for_one_line_two_local_warehouses` (function) — [saleor/warehouse/tests/test_warehouse.py:121]
- `test_applicable_for_click_and_collect_does_not_show_warehouses_with_empty_stocks` (function) — [saleor/warehouse/tests/test_warehouse.py:151]
- `test_applicable_for_click_and_collect_additional_stock_does_not_change_availbility` (function) — [saleor/warehouse/tests/test_warehouse.py:178]
- `test_applicable_for_click_and_collect_returns_empty_collection_if_no_channels` (function) — [saleor/warehouse/tests/test_warehouse.py:210]
- `test_applicable_for_click_and_collect_returns_empty_collection_if_different_channel` (function) — [saleor/warehouse/tests/test_warehouse.py:223]
- `test_applicable_for_click_and_collect_stock_only_in_local_all_and_local_returned` (function) — [saleor/warehouse/tests/test_warehouse.py:237]
- `test_applicable_for_click_and_collect_stock_only_in_warehouse_with_all_option` (function) — [saleor/warehouse/tests/test_warehouse.py:272]
- `test_applicable_for_click_and_collect_all_returned_stock_collected_from_local` (function) — [saleor/warehouse/tests/test_warehouse.py:303]
- `test_applicable_for_click_and_collect_stock_from_local_but_not_all_in_channel` (function) — [saleor/warehouse/tests/test_warehouse.py:343]
- `test_applicable_for_click_and_collect_all_returned_stock_from_disabled_warehouse` (function) — [saleor/warehouse/tests/test_warehouse.py:384]
- `test_applicable_for_click_and_collect_stock_collected_from_different_warehouses` (function) — [saleor/warehouse/tests/test_warehouse.py:419]
- `test_applicable_for_click_and_collect_empty_result_when_not_all_products_available` (function) — [saleor/warehouse/tests/test_warehouse.py:471]
- `test_applicable_for_click_and_collect_additional_stocks` (function) — [saleor/warehouse/tests/test_warehouse.py:520]
- `test_applicable_for_click_and_collect_no_quantity_check_stock_available` (function) — [saleor/warehouse/tests/test_warehouse.py:575]
- `test_applicable_for_click_and_collect_no_quantity_check_stock_available_in_local` (function) — [saleor/warehouse/tests/test_warehouse.py:609]
- `test_applicable_for_click_and_collect_no_quantity_check_stock_available_in_disabled` (function) — [saleor/warehouse/tests/test_warehouse.py:646]
- `test_applicable_for_click_and_collect_no_quantity_check_no_stocks` (function) — [saleor/warehouse/tests/test_warehouse.py:683]
- `test_applicable_for_click_and_collect_no_quantity_check_one_line_without_stock` (function) — [saleor/warehouse/tests/test_warehouse.py:703]
- `test_applicable_for_click_and_collect_no_quantity_check_no_channels` (function) — [saleor/warehouse/tests/test_warehouse.py:734]
- `test_applicable_for_click_and_collect_no_quantity_check_additional_stock` (function) — [saleor/warehouse/tests/test_warehouse.py:765]
- `test_for_channel_with_active_shipping_zone_or_cc` (function) — [saleor/warehouse/tests/test_warehouse.py:812]

**`saleor/warehouse/tests/utils.py`**

- `get_quantity_allocated_for_stock` (function) — [saleor/warehouse/tests/utils.py:5]
- `get_available_quantity_for_stock` (function) — [saleor/warehouse/tests/utils.py:12]

## How it works

The module's files, as provided to this run:

- `saleor/warehouse/tests/__init__.py` (1 lines)
- `saleor/warehouse/tests/test_channel_stock_availability.py` (1050 lines)
- `saleor/warehouse/tests/test_preorder_availability.py` (351 lines)
- `saleor/warehouse/tests/test_preorder_complete.py` (148 lines)
- `saleor/warehouse/tests/test_preorder_reservations_management.py` (285 lines)
- `saleor/warehouse/tests/test_stock_availability.py` (598 lines)
- `saleor/warehouse/tests/test_stock_management.py` (1712 lines)
- `saleor/warehouse/tests/test_stock_reservations_management.py` (369 lines)
- `saleor/warehouse/tests/test_stock.py` (319 lines)
- `saleor/warehouse/tests/test_tasks.py` (106 lines)
- `saleor/warehouse/tests/test_warehouse.py` (825 lines)
- `saleor/warehouse/tests/utils.py` (15 lines)

## Interactions

- Imports from: `saleor/warehouse`, `saleor/warehouse/webhooks`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...WarehouseClickAndCollectOption`
- `...channel.AllocationStrategy`
- `...checkout.fetch.CheckoutLineInfo`
- `...checkout.fetch.fetch_checkout_lines`
- `...checkout.models.Checkout`
- `...core.exceptions.InsufficientStock`
- `...order.fetch.OrderLineInfo`
- `...order.models.OrderLine`
- `...product.models.ProductVariantChannelListing`
- `...warehouse.models.Stock`
- `..interface.VariantChannelStockInfo`
- `..management.deactivate_preorder_for_variant`
- `..models.Allocation`
- `..models.ChannelWarehouse`
- `..models.PreorderAllocation`
- `..models.PreorderReservation`
- `..models.Reservation`
- `..models.Stock`
- `..models.Warehouse`
- `..reservations.reserve_preorders`
- `..reservations.reserve_stocks`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `ab8108383eb5` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
