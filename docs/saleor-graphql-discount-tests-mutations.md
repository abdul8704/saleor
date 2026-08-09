## Purpose

`saleor/graphql/discount/tests/mutations` (`saleor/graphql/discount/tests/mutations`) groups 23 source file(s) exposing 221 top-level declaration(s).

## Public surface

**`saleor/graphql/discount/tests/mutations/test_promotion_bulk_delete.py`**

- `test_delete_promotions_by_staff` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_bulk_delete.py:22]
- `test_delete_promotions_by_app` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_bulk_delete.py:51]
- `test_delete_promotions_trigger_webhooks` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_bulk_delete.py:81]
- `test_delete_promotions_marks_product_to_recalculate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_bulk_delete.py:106]

**`saleor/graphql/discount/tests/mutations/test_promotion_create.py`**

- `test_promotion_create_by_staff_user` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:64]
- `test_promotion_create_by_app` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:185]
- `test_promotion_create_by_customer` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:264]
- `test_promotion_create_with_order_rule` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:319]
- `test_promotion_create_fixed_reward_value_multiple_currencies` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:381]
- `test_promotion_create_invalid_price_precision` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:453]
- `test_promotion_create_invalid_percentage_value` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:519]
- `test_promotion_create_only_name_and_end_date` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:591]
- `test_promotion_create_start_date_and_end_date_after_current_date` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:639]
- `test_promotion_create_missing_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:758]
- `test_promotion_create_missing_reward_value` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:834]
- `test_promotion_create_missing_reward_value_type` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:903]
- `test_promotion_create_invalid_channel_id` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:971]
- `test_promotion_create_mixed_catalogue_and_order_rules` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:1040]
- `test_promotion_create_mixed_currencies_for_price_based_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:1132]
- `test_promotion_create_multiple_errors` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:1198]
- `test_promotion_create_end_date_before_start_date` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:1280]
- `test_promotion_create_invalid_catalogue_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:1350]
- `test_promotion_create_exceeds_rules_number_limit` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:1442]
- `test_promotion_create_exceeds_gifts_number_limit` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:1502]
- `test_promotion_create_rules_without_channels_and_percentage_reward` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:1564]
- `test_promotion_create_events_by_staff_user` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:1646]
- `test_promotion_create_events_by_app` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:1719]
- `test_promotion_create_gift_promotion` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:1793]
- `test_promotion_create_gift_promotion_wrong_gift_instance` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:1854]
- `test_promotion_create_gift_promotion_with_reward_value` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:1905]
- `test_promotion_create_gift_promotion_with_reward_value_type` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:1959]
- `test_promotion_create_gift_promotion_missing_gifts` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:2013]
- `test_promotion_create_without_catalogue_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_create.py:2059]

**`saleor/graphql/discount/tests/mutations/test_promotion_delete.py`**

- `test_promotion_delete_by_staff_user` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_delete.py:29]
- `test_promotion_delete_by_staff_app` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_delete.py:69]
- `test_promotion_delete_by_customer` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_delete.py:110]

**`saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py`**

- `test_promotion_rule_create_by_staff_user` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:58]
- `test_promotion_rule_create_by_app` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:150]
- `test_promotion_rule_create_by_customer` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:218]
- `test_promotion_rule_create_missing_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:270]
- `test_promotion_rule_create_missing_reward_value` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:326]
- `test_promotion_rule_create_missing_reward_value_type` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:377]
- `test_promotion_rule_create_multiple_errors` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:428]
- `test_promotion_rule_invalid_catalogue_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:497]
- `test_promotion_rule_invalid_order_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:565]
- `test_promotion_rule_create_invalid_price_precision` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:627]
- `test_promotion_rule_create_fixed_reward_value_multiple_currencies` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:688]
- `test_promotion_rule_create_fixed_reward_no_channels` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:756]
- `test_promotion_rule_create_percentage_value_above_100` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:815]
- `test_promotion_rule_create_clears_old_sale_id` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:880]
- `test_promotion_rule_create_events` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:955]
- `test_promotion_rule_create_serializable_decimal_in_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1008]
- `test_promotion_rule_create_multiple_predicates` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1043]
- `test_promotion_rule_create_mixed_predicates_order` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1102]
- `test_promotion_rule_create_mixed_predicates_catalogue` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1156]
- `test_promotion_rule_create_missing_reward_type` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1208]
- `test_promotion_rule_create_reward_type_with_catalogue_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1256]
- `test_promotion_rule_create_order_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1307]
- `test_promotion_rule_create_mixed_currencies_for_price_based_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1367]
- `test_promotion_rule_create_with_metadata` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1424]
- `test_promotion_rule_create_exceeds_rules_number_limit` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1475]
- `test_promotion_rule_create_exceeds_gifts_number_limit` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1535]
- `test_promotion_rule_create_gift_promotion` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1590]
- `test_promotion_rule_create_gift_promotion_wrong_gift_instance` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1648]
- `test_promotion_rule_create_gift_promotion_no_gifts` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1696]
- `test_promotion_rule_create_gift_promotion_with_reward_value` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1741]
- `test_promotion_rule_create_gift_promotion_with_reward_value_type` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1792]
- `test_promotion_rule_create_gift_promotion_missing_gifts` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1843]
- `test_promotion_rule_create_invalid_promotion_id` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py:1887]

**`saleor/graphql/discount/tests/mutations/test_promotion_rule_delete.py`**

- `test_promotion_rule_delete_by_staff_user` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_delete.py:37]
- `test_promotion_rule_delete_by_staff_app` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_delete.py:66]
- `test_promotion_rule_delete_by_customer` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_delete.py:99]
- `test_promotion_delete_clears_old_sale_id` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_delete.py:119]
- `test_promotion_rule_delete_events` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_delete.py:155]

**`saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py`**

- `test_promotion_rule_update_by_staff_user` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:56]
- `test_promotion_rule_update_by_app` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:147]
- `test_promotion_rule_update_by_customer` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:207]
- `test_promotion_rule_update_duplicates_channels_in_add_and_remove_field` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:242]
- `test_promotion_rule_update_invalid_catalogue_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:322]
- `test_promotion_rule_update_add_channel_with_different_currency_to_fixed_discount` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:377]
- `test_promotion_rule_update_remove_last_channel_from_fixed_discount` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:420]
- `test_promotion_rule_update_remove_and_add_channel_with_the_same_currency` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:460]
- `test_promotion_rule_update_change_reward_value_type_to_fixed_multiple_channels` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:500]
- `test_promotion_rule_update_change_reward_value_type_to_fixed_no_channels` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:543]
- `test_promotion_rule_update_reward_value_invalid_precision` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:582]
- `test_promotion_rule_update_reward_value_invalid_percentage_value` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:625]
- `test_promotion_rule_update_clears_old_sale_id` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:668]
- `test_promotion_rule_update_events` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:762]
- `test_promotion_rule_update_mix_predicates_invalid_order_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:815]
- `test_promotion_rule_update_mix_predicates_invalid_catalogue_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:854]
- `test_promotion_rule_update_mix_predicates_both_predicate_types_given` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:894]
- `test_promotion_rule_update_reward_type_with_catalogue_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:946]
- `test_promotion_rule_update_clear_reward_type_for_order_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:980]
- `test_promotion_rule_update_add_invalid_channels_for_order_rule` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:1012]
- `test_promotion_rule_update_gift_promotion` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:1049]
- `test_promotion_rule_update_gift_promotion_wrong_gift_instance` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:1097]
- `test_promotion_rule_update_gift_promotion_with_reward_value` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:1134]
- `test_promotion_rule_update_gift_promotion_with_reward_value_type` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:1165]
- `test_promotion_rule_update_gift_promotion_remove_gifts` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:1196]
- `test_promotion_rule_update_exceeds_gifts_number_limit` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py:1235]

**`saleor/graphql/discount/tests/mutations/test_promotion_update.py`**

- `test_promotion_update_by_staff_user` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_update.py:43]
- `test_promotion_update_by_app` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_update.py:97]
- `test_promotion_update_dates_dont_change` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_update.py:151]
- `test_promotion_update_by_customer` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_update.py:212]
- `test_promotion_update_end_date_before_start_date` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_update.py:248]
- `test_promotion_update_clears_old_sale_id` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_update.py:286]
- `test_promotion_update_events` (function) — [saleor/graphql/discount/tests/mutations/test_promotion_update.py:336]

**`saleor/graphql/discount/tests/mutations/test_sale_bulk_delete.py`**

- `test_delete_sales_exceeding_max_input_size` (function) — [saleor/graphql/discount/tests/mutations/test_sale_bulk_delete.py:24]
- `test_delete_sales` (function) — [saleor/graphql/discount/tests/mutations/test_sale_bulk_delete.py:54]
- `test_delete_sales_triggers_webhook` (function) — [saleor/graphql/discount/tests/mutations/test_sale_bulk_delete.py:108]
- `test_delete_sales_with_variants_triggers_webhook` (function) — [saleor/graphql/discount/tests/mutations/test_sale_bulk_delete.py:143]
- `test_delete_sales_with_promotion_ids` (function) — [saleor/graphql/discount/tests/mutations/test_sale_bulk_delete.py:202]

**`saleor/graphql/discount/tests/mutations/test_sale_catalogues_add.py`**

- `test_sale_add_catalogues` (function) — [saleor/graphql/discount/tests/mutations/test_sale_catalogues_add.py:27]
- `test_sale_add_catalogues_no_changes_in_catalogue` (function) — [saleor/graphql/discount/tests/mutations/test_sale_catalogues_add.py:88]
- `test_sale_add_empty_catalogues` (function) — [saleor/graphql/discount/tests/mutations/test_sale_catalogues_add.py:147]
- `test_sale_add_empty_catalogues_to_sale_with_empty_catalogues` (function) — [saleor/graphql/discount/tests/mutations/test_sale_catalogues_add.py:197]
- `test_sale_add_catalogues_no_product_ids_change` (function) — [saleor/graphql/discount/tests/mutations/test_sale_catalogues_add.py:233]
- `test_sale_add_catalogues_with_product_without_variants` (function) — [saleor/graphql/discount/tests/mutations/test_sale_catalogues_add.py:285]
- `test_sale_add_catalogues_with_promotion_id` (function) — [saleor/graphql/discount/tests/mutations/test_sale_catalogues_add.py:329]
- `test_sale_add_catalogues_not_found_error` (function) — [saleor/graphql/discount/tests/mutations/test_sale_catalogues_add.py:363]

**`saleor/graphql/discount/tests/mutations/test_sale_catalogues_remove.py`**

- `test_sale_remove_catalogues` (function) — [saleor/graphql/discount/tests/mutations/test_sale_catalogues_remove.py:27]
- `test_sale_remove_empty_catalogues` (function) — [saleor/graphql/discount/tests/mutations/test_sale_catalogues_remove.py:103]
- `test_sale_remove_empty_catalogues_from_sale_with_empty_catalogues` (function) — [saleor/graphql/discount/tests/mutations/test_sale_catalogues_remove.py:168]
- `test_sale_remove_catalogues_no_product_changes` (function) — [saleor/graphql/discount/tests/mutations/test_sale_catalogues_remove.py:210]
- `test_sale_remove_catalogues_with_promotion_id` (function) — [saleor/graphql/discount/tests/mutations/test_sale_catalogues_remove.py:259]
- `test_sale_remove_catalogues_not_found_error` (function) — [saleor/graphql/discount/tests/mutations/test_sale_catalogues_remove.py:293]

**`saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py`**

- `test_sale_channel_listing_add_channels` (function) — [saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py:35]
- `test_sale_channel_listing_add_multiple_channels` (function) — [saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py:86]
- `test_sale_channel_listing_update_channels` (function) — [saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py:141]
- `test_sale_channel_listing_remove_channels` (function) — [saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py:186]
- `test_sale_channel_listing_remove_all_channels` (function) — [saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py:232]
- `test_sale_channel_listing_add_update_remove_channels` (function) — [saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py:288]
- `test_sale_channel_listing_update_with_negative_discounted_value` (function) — [saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py:345]
- `test_sale_channel_listing_update_duplicated_ids_in_add_and_remove` (function) — [saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py:377]
- `test_sale_channel_listing_update_duplicated_channel_in_add` (function) — [saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py:416]
- `test_sale_channel_listing_update_duplicated_channel_in_remove` (function) — [saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py:456]
- `test_sale_channel_listing_update_with_invalid_decimal_places` (function) — [saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py:490]
- `test_sale_channel_listing_update_with_invalid_percentage_value` (function) — [saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py:527]
- `test_invalidate_data_sale_channel_listings_update` (function) — [saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py:600]
- `test_sale_channel_listing_remove_all_channels_multiple_times` (function) — [saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py:661]
- `test_sale_channel_listing_update_not_found_error` (function) — [saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py:712]

**`saleor/graphql/discount/tests/mutations/test_sale_create.py`**

- `test_create_sale` (function) — [saleor/graphql/discount/tests/mutations/test_sale_create.py:45]
- `test_create_sale_only_start_date` (function) — [saleor/graphql/discount/tests/mutations/test_sale_create.py:109]
- `test_create_sale_with_end_date_before_startdate` (function) — [saleor/graphql/discount/tests/mutations/test_sale_create.py:157]
- `test_create_sale_start_date_and_end_date_before_current_date` (function) — [saleor/graphql/discount/tests/mutations/test_sale_create.py:190]
- `test_create_sale_start_date_and_end_date_after_current_date` (function) — [saleor/graphql/discount/tests/mutations/test_sale_create.py:242]
- `test_create_sale_empty_predicate` (function) — [saleor/graphql/discount/tests/mutations/test_sale_create.py:295]

**`saleor/graphql/discount/tests/mutations/test_sale_delete.py`**

- `test_sale_delete_mutation` (function) — [saleor/graphql/discount/tests/mutations/test_sale_delete.py:33]
- `test_sale_delete_mutation_with_promotion_id` (function) — [saleor/graphql/discount/tests/mutations/test_sale_delete.py:80]
- `test_sale_delete_not_found_error` (function) — [saleor/graphql/discount/tests/mutations/test_sale_delete.py:113]

**`saleor/graphql/discount/tests/mutations/test_sale_update.py`**

- `test_update_sale` (function) — [saleor/graphql/discount/tests/mutations/test_sale_update.py:39]
- `test_update_sale_name` (function) — [saleor/graphql/discount/tests/mutations/test_sale_update.py:109]
- `test_update_sale_start_date_after_current_date_notification_not_sent` (function) — [saleor/graphql/discount/tests/mutations/test_sale_update.py:169]
- `test_update_sale_start_date_before_current_date_notification_already_sent` (function) — [saleor/graphql/discount/tests/mutations/test_sale_update.py:232]
- `test_update_sale_start_date_before_current_date_notification_sent` (function) — [saleor/graphql/discount/tests/mutations/test_sale_update.py:299]
- `test_update_sale_end_date_after_current_date_notification_not_sent` (function) — [saleor/graphql/discount/tests/mutations/test_sale_update.py:363]
- `test_update_sale_end_date_before_current_date_notification_already_sent` (function) — [saleor/graphql/discount/tests/mutations/test_sale_update.py:427]
- `test_update_sale_end_date_before_current_date_notification_sent` (function) — [saleor/graphql/discount/tests/mutations/test_sale_update.py:493]
- `test_update_sale_categories` (function) — [saleor/graphql/discount/tests/mutations/test_sale_update.py:555]
- `test_update_sale_collections` (function) — [saleor/graphql/discount/tests/mutations/test_sale_update.py:601]
- `test_update_sale_variants` (function) — [saleor/graphql/discount/tests/mutations/test_sale_update.py:649]
- `test_update_sale_products` (function) — [saleor/graphql/discount/tests/mutations/test_sale_update.py:708]
- `test_update_sale_end_date_before_start_date` (function) — [saleor/graphql/discount/tests/mutations/test_sale_update.py:767]
- `test_update_sale_with_none_values` (function) — [saleor/graphql/discount/tests/mutations/test_sale_update.py:818]
- `test_update_sale_with_promotion_id` (function) — [saleor/graphql/discount/tests/mutations/test_sale_update.py:875]
- `test_update_sale_not_found_error` (function) — [saleor/graphql/discount/tests/mutations/test_sale_update.py:926]

**`saleor/graphql/discount/tests/mutations/test_voucher_bulk_delete.py`**

- `test_delete_vouchers` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_bulk_delete.py:17]
- `test_delete_vouchers_trigger_webhook` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_bulk_delete.py:39]

**`saleor/graphql/discount/tests/mutations/test_voucher_catalogues_add.py`**

- `test_voucher_add_catalogues` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_catalogues_add.py:30]
- `test_voucher_add_catalogues_trigger_webhook` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_catalogues_add.py:74]
- `test_voucher_add_no_catalogues` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_catalogues_add.py:142]
- `test_voucher_add_catalogues_with_product_without_variant` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_catalogues_add.py:163]
- `test_voucher_remove_no_catalogues` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_catalogues_add.py:195]

**`saleor/graphql/discount/tests/mutations/test_voucher_catalogues_remove.py`**

- `test_voucher_remove_catalogues` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_catalogues_remove.py:21]

**`saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py`**

- `test_voucher_channel_listing_create_as_staff` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:43]
- `test_voucher_channel_listing_update_as_app` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:75]
- `test_voucher_channel_listing_update_as_customer` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:107]
- `test_voucher_channel_listing_update_trigger_webhook` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:132]
- `test_voucher_channel_listing_update_as_anonymous` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:186]
- `test_voucher_channel_listing_create_many_channel` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:208]
- `test_voucher_channel_listing_create_and_remove` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:264]
- `test_voucher_channel_listing_update` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:310]
- `test_voucher_channel_listing_update_without_discount_value` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:354]
- `test_voucher_channel_listing_remove_channel` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:392]
- `test_voucher_channel_listing_update_with_null_as_discount_value` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:421]
- `test_voucher_channel_listing_create_with_null_as_discount_value` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:459]
- `test_voucher_channel_listing_create_with_invalid_percentage_value` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:498]
- `test_voucher_channel_listing_create_without_discount_value` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:538]
- `test_voucher_channel_listing_update_duplicates_in_add` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:569]
- `test_voucher_channel_listing_update_duplicates_in_remove` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:604]
- `test_voucher_channel_listing_update_duplicates_in_add_and_remove` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:634]
- `test_voucher_channel_listing_update_invalid_precision_discount_value` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:667]
- `test_voucher_channel_listing_update_invalid_precision_min_amount_spent` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py:705]

**`saleor/graphql/discount/tests/mutations/test_voucher_code_bulk_delete.py`**

- `test_delete_voucher_codes` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_code_bulk_delete.py:20]
- `test_delete_voucher_codes_as_app` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_code_bulk_delete.py:48]
- `test_delete_voucher_codes_trigger_voucher_codes_deleted_webhook` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_code_bulk_delete.py:80]
- `test_delete_voucher_codes_return_error_when_invalid_id` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_code_bulk_delete.py:118]

**`saleor/graphql/discount/tests/mutations/test_voucher_create.py`**

- `test_create_voucher` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_create.py:60]
- `test_create_voucher_no_codes` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_create.py:121]
- `test_create_voucher_return_error_when_code_and_codes_args_combined` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_create.py:170]
- `test_create_voucher_return_error_when_code_or_codes_arg_not_in_input` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_create.py:207]
- `test_create_voucher_trigger_webhook` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_create.py:245]
- `test_create_voucher_with_empty_code` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_create.py:331]
- `test_create_voucher_with_spaces_in_code` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_create.py:360]
- `test_create_voucher_with_duplicated_codes` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_create.py:391]
- `test_create_voucher_with_existing_gift_card_code` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_create.py:425]
- `test_create_voucher_with_existing_voucher_code` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_create.py:461]
- `test_create_voucher_with_enddate_before_startdate` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_create.py:494]

**`saleor/graphql/discount/tests/mutations/test_voucher_delete.py`**

- `test_voucher_delete_mutation` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_delete.py:31]
- `test_voucher_delete_mutation_trigger_webhook` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_delete.py:49]

**`saleor/graphql/discount/tests/mutations/test_voucher_update.py`**

- `test_update_voucher` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_update.py:83]
- `test_update_voucher_without_codes` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_update.py:141]
- `test_update_voucher_trigger_webhook` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_update.py:183]
- `test_update_voucher_doesnt_trigger_voucher_updated_when_only_codes_added` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_update.py:257]
- `test_update_voucher_single_use_voucher_already_used_in_order` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_update.py:305]
- `test_update_voucher_single_use_voucher_already_used_in_order_line` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_update.py:344]
- `test_update_voucher_single_use_voucher_already_used_in_checkout` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_update.py:382]
- `test_update_voucher_usage_limit_voucher_already_used` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_update.py:420]
- `test_update_voucher_usage_limit_the_same_value` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_update.py:454]
- `test_update_voucher_with_deprecated_code_field` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_update.py:485]
- `test_update_voucher_usage_limit_order_with_given_voucher_code_exists` (function) — [saleor/graphql/discount/tests/mutations/test_voucher_update.py:517]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/discount/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/discount/tests/mutations/test_promotion_bulk_delete.py` (139 lines)
- `saleor/graphql/discount/tests/mutations/test_promotion_create.py` (2113 lines)
- `saleor/graphql/discount/tests/mutations/test_promotion_delete.py` (138 lines)
- `saleor/graphql/discount/tests/mutations/test_promotion_rule_create.py` (1933 lines)
- `saleor/graphql/discount/tests/mutations/test_promotion_rule_delete.py` (178 lines)
- `saleor/graphql/discount/tests/mutations/test_promotion_rule_update.py` (1278 lines)
- `saleor/graphql/discount/tests/mutations/test_promotion_update.py` (365 lines)
- `saleor/graphql/discount/tests/mutations/test_sale_bulk_delete.py` (250 lines)
- `saleor/graphql/discount/tests/mutations/test_sale_catalogues_add.py` (385 lines)
- `saleor/graphql/discount/tests/mutations/test_sale_catalogues_remove.py` (315 lines)
- `saleor/graphql/discount/tests/mutations/test_sale_channel_listing_update.py` (734 lines)
- `saleor/graphql/discount/tests/mutations/test_sale_create.py` (343 lines)
- `saleor/graphql/discount/tests/mutations/test_sale_delete.py` (129 lines)
- `saleor/graphql/discount/tests/mutations/test_sale_update.py` (945 lines)
- `saleor/graphql/discount/tests/mutations/test_voucher_bulk_delete.py` (66 lines)
- `saleor/graphql/discount/tests/mutations/test_voucher_catalogues_add.py` (229 lines)
- `saleor/graphql/discount/tests/mutations/test_voucher_catalogues_remove.py` (63 lines)
- `saleor/graphql/discount/tests/mutations/test_voucher_channel_listing_update.py` (740 lines)
- `saleor/graphql/discount/tests/mutations/test_voucher_code_bulk_delete.py` (137 lines)
- `saleor/graphql/discount/tests/mutations/test_voucher_create.py` (525 lines)
- `saleor/graphql/discount/tests/mutations/test_voucher_delete.py` (91 lines)
- `saleor/graphql/discount/tests/mutations/test_voucher_update.py` (555 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....core.utils.json_serializer.CustomJsonEncoder`
- `.....discount.DiscountValueType`
- `.....discount.PromotionEvents`
- `.....discount.RewardValueType`
- `.....discount.VoucherType`
- `.....discount.error_codes.DiscountErrorCode`
- `.....discount.error_codes.PromotionCreateErrorCode`
- `.....discount.error_codes.PromotionRuleCreateErrorCode`
- `.....discount.error_codes.PromotionRuleUpdateErrorCode`
- `.....discount.models.Promotion`
- `.....discount.models.PromotionEvent`
- `.....discount.models.PromotionRule`
- `.....discount.models.RewardValueType`
- `.....discount.models.Voucher`
- `.....product.models.ProductChannelListing`
- `.....product.models.ProductVariant`
- `.....webhook.event_types.WebhookEventAsyncType`
- `.....webhook.payloads.generate_meta`
- `.....webhook.payloads.generate_requestor`
- `....tests.utils.assert_negative_positive_decimal_value`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `...enums.DiscountValueTypeEnum`
- `...enums.PromotionTypeEnum`
- `...enums.RewardTypeEnum`
- `...enums.RewardValueTypeEnum`
- `...enums.VoucherTypeEnum`
- `...utils.convert_migrated_sale_predicate_to_catalogue_info`
- `...utils.get_products_for_promotion`
- `...utils.get_products_for_rule`
- `...utils.get_variants_for_catalogue_predicate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `e307ba91d1d7` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
