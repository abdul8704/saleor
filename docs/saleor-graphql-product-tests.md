## Purpose

`saleor/graphql/product/tests` (`saleor/graphql/product/tests`) groups 17 source file(s) exposing 222 top-level declaration(s).

## Public surface

**`saleor/graphql/product/tests/test_attributes.py`**

- `test_resolve_attributes_with_hidden` (function) — [saleor/graphql/product/tests/test_attributes.py:308]
- `test_resolve_attribute_values` (function) — [saleor/graphql/product/tests/test_attributes.py:350]
- `test_resolve_attribute_values_non_assigned_to_node` (function) — [saleor/graphql/product/tests/test_attributes.py:396]
- `test_resolve_assigned_attribute_without_values` (function) — [saleor/graphql/product/tests/test_attributes.py:459]
- `test_assign_attributes_to_product_type` (function) — [saleor/graphql/product/tests/test_attributes.py:555]
- `test_assign_non_existing_attributes_to_product_type` (function) — [saleor/graphql/product/tests/test_attributes.py:614]
- `test_assign_non_existing_and_existing_attributes_to_product_type` (function) — [saleor/graphql/product/tests/test_attributes.py:640]
- `test_assign_variant_attribute_to_product_type_with_disabled_variants` (function) — [saleor/graphql/product/tests/test_attributes.py:680]
- `test_assign_variant_attribute_having_multiselect_input_type` (function) — [saleor/graphql/product/tests/test_attributes.py:707]
- `test_assign_variant_attribute_having_multiselect_input_type_with_variant_selection` (function) — [saleor/graphql/product/tests/test_attributes.py:738]
- `test_assign_product_attribute_having_variant_selection` (function) — [saleor/graphql/product/tests/test_attributes.py:776]
- `test_assign_attribute_to_product_type_having_already_that_attribute` (function) — [saleor/graphql/product/tests/test_attributes.py:822]
- `test_assignment_attribute_update_not_assigned_attribute_should_raise_an_error` (function) — [saleor/graphql/product/tests/test_attributes.py:893]
- `test_assignment_attribute_update_assigned_to_product_should_raise_an_error` (function) — [saleor/graphql/product/tests/test_attributes.py:939]
- `test_assignment_attrib_update_assigned_with_duplicates_type_should_raise_an_error` (function) — [saleor/graphql/product/tests/test_attributes.py:980]
- `test_assignment_attribute_update_assigned_unsupported_type_should_raise_an_error` (function) — [saleor/graphql/product/tests/test_attributes.py:1029]
- `test_assignment_attribute_update_assigned_should_modify_variant_selection` (function) — [saleor/graphql/product/tests/test_attributes.py:1079]
- `test_assignment_attrib_update_assigned_should_modify_variant_selection_from_ext_app` (function) — [saleor/graphql/product/tests/test_attributes.py:1125]
- `test_assign_page_attribute_to_product_type` (function) — [saleor/graphql/product/tests/test_attributes.py:1169]
- `test_assign_attribute_to_product_type_multiple_errors_returned` (function) — [saleor/graphql/product/tests/test_attributes.py:1204]
- `test_unassign_attributes_from_product_type` (function) — [saleor/graphql/product/tests/test_attributes.py:1294]
- `test_unassign_attributes_not_in_product_type` (function) — [saleor/graphql/product/tests/test_attributes.py:1353]
- `test_retrieve_product_attributes_input_type` (function) — [saleor/graphql/product/tests/test_attributes.py:1383]
- `test_sort_attributes_within_product_type_invalid_product_type` (function) — [saleor/graphql/product/tests/test_attributes.py:1444]
- `test_sort_attributes_within_product_type_invalid_id` (function) — [saleor/graphql/product/tests/test_attributes.py:1476]
- `test_sort_attributes_within_product_type` (function) — [saleor/graphql/product/tests/test_attributes.py:1519]
- `test_sort_product_attribute_values` (function) — [saleor/graphql/product/tests/test_attributes.py:1617]
- `test_sort_product_attribute_values_invalid_attribute_id` (function) — [saleor/graphql/product/tests/test_attributes.py:1692]
- `test_sort_product_attribute_values_invalid_value_id` (function) — [saleor/graphql/product/tests/test_attributes.py:1747]
- `test_sort_product_variant_attribute_values` (function) — [saleor/graphql/product/tests/test_attributes.py:1852]
- `test_sort_product_variant_attribute_values_invalid_attribute_id` (function) — [saleor/graphql/product/tests/test_attributes.py:1929]
- `test_sort_product_variant_attribute_values_invalid_value_id` (function) — [saleor/graphql/product/tests/test_attributes.py:1985]

**`saleor/graphql/product/tests/test_bulk_delete.py`**

- `test_delete_categories` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:44]
- `test_delete_categories_invalidate_active_promotion_rules` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:79]
- `test_delete_categories_trigger_webhook` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:113]
- `test_delete_categories_with_images` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:146]
- `test_delete_categories_trigger_product_updated_webhook` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:191]
- `test_delete_categories_with_subcategories_and_products` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:235]
- `test_delete_collections` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:311]
- `test_delete_collections_with_images` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:347]
- `test_delete_collections_trigger_collection_deleted_webhook` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:395]
- `test_delete_collections_trigger_product_updated_webhook` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:432]
- `test_delete_products` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:481]
- `test_delete_products_invalid_object_typed_of_given_ids` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:562]
- `test_delete_products_exceeding_max_input_size` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:583]
- `test_delete_products_with_images` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:610]
- `test_delete_products_trigger_webhook` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:649]
- `test_delete_products_without_variants` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:685]
- `test_delete_products_removes_checkout_lines` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:718]
- `test_delete_products_with_file_attributes` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:753]
- `test_delete_products_variants_in_draft_order` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:793]
- `test_delete_product_media` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:838]
- `test_delete_product_types` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:881]
- `test_delete_product_types_trigger_webhooks` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:908]
- `test_delete_product_types_invalid_object_typed_of_given_ids` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:947]
- `test_delete_product_types_with_file_attributes` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:972]
- `test_delete_product_variants_by_sku` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:1030]
- `test_delete_product_variants_by_sku_task_for_recalculate_product_prices_called` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:1081]
- `test_delete_product_variants_by_sku_exceeding_max_input_size` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:1123]
- `test_delete_product_variants` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:1166]
- `test_delete_product_variants_task_for_recalculate_product_prices_called` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:1219]
- `test_delete_product_variants_invalid_object_typed_of_given_ids` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:1263]
- `test_delete_product_variants_removes_checkout_lines` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:1290]
- `test_delete_product_variants_with_images` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:1342]
- `test_product_delete_removes_reference_to_product` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:1397]
- `test_product_delete_removes_variant_reference_to_product` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:1439]
- `test_product_delete_removes_reference_to_variant` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:1478]
- `test_product_delete_removes_reference_to_page` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:1523]
- `test_delete_product_variants_with_file_attribute` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:1569]
- `test_delete_product_variants_in_draft_orders` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:1624]
- `test_delete_product_variants_delete_default_variant` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:1739]
- `test_delete_product_variants_delete_all_product_variants` (function) — [saleor/graphql/product/tests/test_bulk_delete.py:1790]
- _…and 2 more in this file_

**`saleor/graphql/product/tests/test_product_channel_listings_queries.py`**

- `test_product_channel_listing_pricing_field` (function) — [saleor/graphql/product/tests/test_product_channel_listings_queries.py:47]
- `test_product_channel_listing_pricing_no_prices` (function) — [saleor/graphql/product/tests/test_product_channel_listings_queries.py:91]
- `test_product_channel_listing_pricing_field_no_address` (function) — [saleor/graphql/product/tests/test_product_channel_listings_queries.py:159]
- `test_product_pricing` (function) — [saleor/graphql/product/tests/test_product_channel_listings_queries.py:284]
- `test_product_pricing_default_country_default_rate` (function) — [saleor/graphql/product/tests/test_product_channel_listings_queries.py:342]
- `test_product_pricing_use_tax_class_from_product_type` (function) — [saleor/graphql/product/tests/test_product_channel_listings_queries.py:395]
- `test_product_pricing_no_flat_rates_in_one_country` (function) — [saleor/graphql/product/tests/test_product_channel_listings_queries.py:449]

**`saleor/graphql/product/tests/test_product_discounted_price.py`**

- `test_product_variant_delete_updates_discounted_price` (function) — [saleor/graphql/product/tests/test_product_discounted_price.py:17]
- `test_category_delete_updates_discounted_price` (function) — [saleor/graphql/product/tests/test_product_discounted_price.py:55]
- `test_collection_add_products_updates_rule_variants_dirty` (function) — [saleor/graphql/product/tests/test_product_discounted_price.py:99]
- `test_collection_remove_products_updates_rule_variants_dirty` (function) — [saleor/graphql/product/tests/test_product_discounted_price.py:139]
- `test_sale_create_updates_products_discounted_prices` (function) — [saleor/graphql/product/tests/test_product_discounted_price.py:180]
- `test_sale_update_updates_products_discounted_prices` (function) — [saleor/graphql/product/tests/test_product_discounted_price.py:227]
- `test_sale_delete_updates_products_discounted_prices` (function) — [saleor/graphql/product/tests/test_product_discounted_price.py:277]
- `test_sale_add_catalogues_updates_products_discounted_prices` (function) — [saleor/graphql/product/tests/test_product_discounted_price.py:324]
- `test_sale_remove_catalogues_updates_products_discounted_prices` (function) — [saleor/graphql/product/tests/test_product_discounted_price.py:371]

**`saleor/graphql/product/tests/test_product_filtering_and_sorting_with_channels.py`**

- `products_for_sorting_with_channels` (function) — [saleor/graphql/product/tests/test_product_filtering_and_sorting_with_channels.py:21]
- `test_products_with_sorting_and_without_channel` (function) — [saleor/graphql/product/tests/test_product_filtering_and_sorting_with_channels.py:271]
- `test_products_with_sorting_and_channel_USD` (function) — [saleor/graphql/product/tests/test_product_filtering_and_sorting_with_channels.py:344]
- `test_products_with_sorting_and_channel_PLN` (function) — [saleor/graphql/product/tests/test_product_filtering_and_sorting_with_channels.py:423]
- `test_products_with_sorting_and_not_existing_channel_asc` (function) — [saleor/graphql/product/tests/test_product_filtering_and_sorting_with_channels.py:457]
- `test_products_with_sorting_and_not_existing_channel_desc` (function) — [saleor/graphql/product/tests/test_product_filtering_and_sorting_with_channels.py:488]
- `test_products_with_filtering_without_channel` (function) — [saleor/graphql/product/tests/test_product_filtering_and_sorting_with_channels.py:515]
- `test_products_with_filtering_with_channel_USD` (function) — [saleor/graphql/product/tests/test_product_filtering_and_sorting_with_channels.py:553]
- `test_products_with_filtering_with_channel_PLN` (function) — [saleor/graphql/product/tests/test_product_filtering_and_sorting_with_channels.py:595]
- `test_products_with_filtering_and_not_existing_channel` (function) — [saleor/graphql/product/tests/test_product_filtering_and_sorting_with_channels.py:638]
- `test_published_products_without_sku_as_staff` (function) — [saleor/graphql/product/tests/test_product_filtering_and_sorting_with_channels.py:662]
- `test_product_query_with_filter_updated_at` (function) — [saleor/graphql/product/tests/test_product_filtering_and_sorting_with_channels.py:706]
- `test_products_variants_with_sorting_and_channel_USD` (function) — [saleor/graphql/product/tests/test_product_filtering_and_sorting_with_channels.py:768]
- `test_products_variants_with_sorting_and_channel_PLN` (function) — [saleor/graphql/product/tests/test_product_filtering_and_sorting_with_channels.py:807]

**`saleor/graphql/product/tests/test_product_pagination.py`**

- `categories_for_pagination` (function) — [saleor/graphql/product/tests/test_product_pagination.py:25]
- `test_categories_pagination_with_sorting` (function) — [saleor/graphql/product/tests/test_product_pagination.py:113]
- `test_categories_pagination_with_filtering` (function) — [saleor/graphql/product/tests/test_product_pagination.py:142]
- `collections_for_pagination` (function) — [saleor/graphql/product/tests/test_product_pagination.py:163]
- `test_collections_pagination_with_sorting` (function) — [saleor/graphql/product/tests/test_product_pagination.py:236]
- `test_collections_pagination_with_filtering` (function) — [saleor/graphql/product/tests/test_product_pagination.py:277]
- `products_for_pagination` (function) — [saleor/graphql/product/tests/test_product_pagination.py:306]
- `test_products_pagination_with_sorting` (function) — [saleor/graphql/product/tests/test_product_pagination.py:494]
- `test_products_pagination_with_sorting_and_channel` (function) — [saleor/graphql/product/tests/test_product_pagination.py:535]
- `test_products_pagination_with_sorting_by_attribute` (function) — [saleor/graphql/product/tests/test_product_pagination.py:565]
- `test_products_pagination_for_products_with_the_same_names_two_pages` (function) — [saleor/graphql/product/tests/test_product_pagination.py:592]
- `test_products_pagination_for_products_with_the_same_names_one_page` (function) — [saleor/graphql/product/tests/test_product_pagination.py:654]
- `test_products_pagination_with_filtering` (function) — [saleor/graphql/product/tests/test_product_pagination.py:710]
- `test_products_pagination_with_filtering_and_channel` (function) — [saleor/graphql/product/tests/test_product_pagination.py:746]
- `test_products_pagination_with_filtering_by_attribute` (function) — [saleor/graphql/product/tests/test_product_pagination.py:775]
- `test_products_pagination_with_filtering_by_product_types` (function) — [saleor/graphql/product/tests/test_product_pagination.py:803]
- `test_products_pagination_with_filtering_by_stocks` (function) — [saleor/graphql/product/tests/test_product_pagination.py:829]
- `product_types_for_pagination` (function) — [saleor/graphql/product/tests/test_product_pagination.py:856]
- `test_product_types_pagination_with_sorting` (function) — [saleor/graphql/product/tests/test_product_pagination.py:932]
- `test_product_types_pagination_with_filtering` (function) — [saleor/graphql/product/tests/test_product_pagination.py:964]

**`saleor/graphql/product/tests/test_product_pricing.py`**

- `test_product_pricing` (function) — [saleor/graphql/product/tests/test_product_pricing.py:113]
- `test_product_pricing_default_country_default_rate` (function) — [saleor/graphql/product/tests/test_product_pricing.py:161]
- `test_product_pricing_use_tax_class_from_product_type` (function) — [saleor/graphql/product/tests/test_product_pricing.py:203]
- `test_product_pricing_no_flat_rates_in_one_country` (function) — [saleor/graphql/product/tests/test_product_pricing.py:247]

**`saleor/graphql/product/tests/test_product_prior_price.py`**

- `test_product_prior_price` (function) — [saleor/graphql/product/tests/test_product_prior_price.py:6]

**`saleor/graphql/product/tests/test_product_sorting_attributes.py`**

- `products_structures` (function) — [saleor/graphql/product/tests/test_product_sorting_attributes.py:51]
- `attr_value` (function) — [saleor/graphql/product/tests/test_product_sorting_attributes.py:52]
- `test_sort_products_cannot_sort_both_by_field_and_by_attribute` (function) — [saleor/graphql/product/tests/test_product_sorting_attributes.py:234]
- `test_sort_product_by_attribute_single_value` (function) — [saleor/graphql/product/tests/test_product_sorting_attributes.py:505]
- `test_sort_product_by_attribute_multiple_values` (function) — [saleor/graphql/product/tests/test_product_sorting_attributes.py:531]
- `test_sort_product_not_having_attribute_data` (function) — [saleor/graphql/product/tests/test_product_sorting_attributes.py:556]
- `test_sort_product_by_attribute_using_invalid_attribute_id` (function) — [saleor/graphql/product/tests/test_product_sorting_attributes.py:618]
- `test_sort_product_by_attribute_using_string_as_attribute_id` (function) — [saleor/graphql/product/tests/test_product_sorting_attributes.py:646]
- `test_sort_product_by_attribute_using_attribute_having_no_products` (function) — [saleor/graphql/product/tests/test_product_sorting_attributes.py:666]

**`saleor/graphql/product/tests/test_product_sorting.py`**

- `test_sort_products_within_collection_invalid_collection_id` (function) — [saleor/graphql/product/tests/test_product_sorting.py:36]
- `test_sort_products_within_collection_invalid_product_id` (function) — [saleor/graphql/product/tests/test_product_sorting.py:60]
- `test_sort_products_within_collection` (function) — [saleor/graphql/product/tests/test_product_sorting.py:84]
- `test_sort_products_within_collection_when_null_as_sort_order` (function) — [saleor/graphql/product/tests/test_product_sorting.py:147]
- `test_sort_products_by_published_at` (function) — [saleor/graphql/product/tests/test_product_sorting.py:219]
- `test_sort_products_by_created_at` (function) — [saleor/graphql/product/tests/test_product_sorting.py:257]
- `test_sort_products_by_rating` (function) — [saleor/graphql/product/tests/test_product_sorting.py:281]
- `test_pagination_for_sorting_products_by_published_at_date` (function) — [saleor/graphql/product/tests/test_product_sorting.py:329]
- `test_query_products_sorted_by_collection_with_asc_direction` (function) — [saleor/graphql/product/tests/test_product_sorting.py:402]
- `test_query_products_sorted_by_collection_with_desc_direction` (function) — [saleor/graphql/product/tests/test_product_sorting.py:462]
- `test_query_products_sorted_by_collection_when_items_with_sort_null_and_asc_sorting` (function) — [saleor/graphql/product/tests/test_product_sorting.py:522]
- `test_query_products_sorted_by_collection_when_items_with_sort_null_and_desc_sorting` (function) — [saleor/graphql/product/tests/test_product_sorting.py:582]
- `test_query_products_sorted_by_collection_returns_useable_cursor` (function) — [saleor/graphql/product/tests/test_product_sorting.py:642]
- `test_query_products_sorted_by_collection_when_items_with_null_and_negative_sorting` (function) — [saleor/graphql/product/tests/test_product_sorting.py:717]
- `test_query_products_sorted_by_collection_when_items_when_null_as_sorting` (function) — [saleor/graphql/product/tests/test_product_sorting.py:777]

**`saleor/graphql/product/tests/test_variant_availability.py`**

- `test_variant_quantity_available_without_country_code` (function) — [saleor/graphql/product/tests/test_variant_availability.py:26]
- `test_variant_quantity_available_without_country_code_or_channel` (function) — [saleor/graphql/product/tests/test_variant_availability.py:39]
- `test_variant_quantity_available_without_country_code_stock_only_in_cc_warehouse` (function) — [saleor/graphql/product/tests/test_variant_availability.py:53]
- `test_variant_quantity_available_without_country_code_local_cc_warehouse` (function) — [saleor/graphql/product/tests/test_variant_availability.py:76]
- `test_variant_quantity_available_without_country_code_global_cc_warehouse` (function) — [saleor/graphql/product/tests/test_variant_availability.py:106]
- `test_variant_quantity_available_when_one_stock_is_exceeded` (function) — [saleor/graphql/product/tests/test_variant_availability.py:142]
- `test_variant_quantity_available_without_country_code_and_no_channel_shipping_zones` (function) — [saleor/graphql/product/tests/test_variant_availability.py:164]
- `test_variant_quantity_available_no_country_warehouse_without_zone` (function) — [saleor/graphql/product/tests/test_variant_availability.py:178]
- `test_variant_quantity_available_no_channel_and_no_country_warehouse_without_zone` (function) — [saleor/graphql/product/tests/test_variant_availability.py:206]
- `test_variant_quantity_available_only_warehouse_without_zone_no_channel_no_country` (function) — [saleor/graphql/product/tests/test_variant_availability.py:245]
- `test_variant_quantity_available_with_country_code` (function) — [saleor/graphql/product/tests/test_variant_availability.py:290]
- `test_variant_quantity_available_with_country_code_warehouse_in_many_shipping_zones` (function) — [saleor/graphql/product/tests/test_variant_availability.py:305]
- `test_variant_quantity_available_with_country_code_no_channel_shipping_zones` (function) — [saleor/graphql/product/tests/test_variant_availability.py:327]
- `test_variant_quantity_available_with_country_code_only_one_available_warehouse` (function) — [saleor/graphql/product/tests/test_variant_availability.py:343]
- `test_variant_quantity_available_with_null_as_country_code` (function) — [saleor/graphql/product/tests/test_variant_availability.py:362]
- `test_variant_quantity_available_with_country_code_only_negative_quantity` (function) — [saleor/graphql/product/tests/test_variant_availability.py:377]
- `test_variant_quantity_available_with_country_code_and_cc_warehouse_without_zone` (function) — [saleor/graphql/product/tests/test_variant_availability.py:418]
- `test_variant_quantity_available_with_country_code_and_local_cc_warehouse_with_zone` (function) — [saleor/graphql/product/tests/test_variant_availability.py:459]
- `test_variant_qty_available_with_country_code_and_local_cc_warehouse_negative_qty` (function) — [saleor/graphql/product/tests/test_variant_availability.py:497]
- `test_variant_quantity_available_with_country_code_and_global_cc_warehouse` (function) — [saleor/graphql/product/tests/test_variant_availability.py:535]
- `test_variant_quantity_available_with_max` (function) — [saleor/graphql/product/tests/test_variant_availability.py:569]
- `test_variant_quantity_available_without_stocks` (function) — [saleor/graphql/product/tests/test_variant_availability.py:591]
- `test_variant_quantity_available_with_allocations` (function) — [saleor/graphql/product/tests/test_variant_availability.py:607]
- `test_variant_quantity_available_with_enabled_reservations` (function) — [saleor/graphql/product/tests/test_variant_availability.py:626]
- `test_variant_quantity_available_with_enabled_expired_reservations` (function) — [saleor/graphql/product/tests/test_variant_availability.py:645]
- `test_variant_quantity_available_with_disabled_reservations` (function) — [saleor/graphql/product/tests/test_variant_availability.py:667]
- `test_variant_quantity_available_without_inventory_tracking` (function) — [saleor/graphql/product/tests/test_variant_availability.py:685]
- `test_variant_quantity_available_without_inventory_tracking_no_global_limit` (function) — [saleor/graphql/product/tests/test_variant_availability.py:706]
- `test_variant_quantity_available_without_inventory_tracking_and_stocks` (function) — [saleor/graphql/product/tests/test_variant_availability.py:725]
- `test_variant_qty_available_without_inventory_tracking_and_stocks_no_global_limit` (function) — [saleor/graphql/product/tests/test_variant_availability.py:746]
- `test_variant_quantity_available_preorder_with_channel_threshold` (function) — [saleor/graphql/product/tests/test_variant_availability.py:766]
- `test_variant_quantity_available_preorder_without_reservations` (function) — [saleor/graphql/product/tests/test_variant_availability.py:793]
- `test_variant_quantity_available_preorder_with_channel_threshold_and_reservation` (function) — [saleor/graphql/product/tests/test_variant_availability.py:819]
- `test_variant_quantity_available_preorder_with_global_threshold` (function) — [saleor/graphql/product/tests/test_variant_availability.py:849]
- `test_variant_quantity_available_preorder_with_global_threshold_and_reservations` (function) — [saleor/graphql/product/tests/test_variant_availability.py:871]
- `test_variant_quantity_available_preorder_without_threshold` (function) — [saleor/graphql/product/tests/test_variant_availability.py:903]
- `test_variant_quantity_available_preorder_without_channel` (function) — [saleor/graphql/product/tests/test_variant_availability.py:931]

**`saleor/graphql/product/tests/test_variant_channel_listing_update.py`**

- `test_variant_channel_listing_update_duplicated_channel` (function) — [saleor/graphql/product/tests/test_variant_channel_listing_update.py:58]
- `test_variant_channel_listing_update_with_empty_input` (function) — [saleor/graphql/product/tests/test_variant_channel_listing_update.py:89]
- `test_variant_channel_listing_update_not_assigned_channel` (function) — [saleor/graphql/product/tests/test_variant_channel_listing_update.py:113]
- `test_variant_channel_listing_update_negative_price` (function) — [saleor/graphql/product/tests/test_variant_channel_listing_update.py:141]
- `test_variant_channel_listing_update_with_too_many_decimal_places_in_price` (function) — [saleor/graphql/product/tests/test_variant_channel_listing_update.py:163]
- `test_variant_channel_listing_update_as_staff_user` (function) — [saleor/graphql/product/tests/test_variant_channel_listing_update.py:189]
- `test_variant_channel_listing_update_by_sku` (function) — [saleor/graphql/product/tests/test_variant_channel_listing_update.py:259]
- `test_variant_channel_listing_update_trigger_webhook_product_variant_updated` (function) — [saleor/graphql/product/tests/test_variant_channel_listing_update.py:320]
- `test_variant_channel_listing_update_as_app` (function) — [saleor/graphql/product/tests/test_variant_channel_listing_update.py:364]
- `test_variant_channel_listing_update_as_customer` (function) — [saleor/graphql/product/tests/test_variant_channel_listing_update.py:416]
- `test_variant_channel_listing_update_as_anonymous` (function) — [saleor/graphql/product/tests/test_variant_channel_listing_update.py:447]
- `test_product_variant_channel_listing_update_remove_cost_price` (function) — [saleor/graphql/product/tests/test_variant_channel_listing_update.py:478]
- `test_product_channel_listing_update_too_many_decimal_places_in_cost_price` (function) — [saleor/graphql/product/tests/test_variant_channel_listing_update.py:511]
- `test_product_channel_listing_update_invalid_cost_price` (function) — [saleor/graphql/product/tests/test_variant_channel_listing_update.py:537]
- `test_variant_channel_listing_update_preorder` (function) — [saleor/graphql/product/tests/test_variant_channel_listing_update.py:559]
- `test_variant_channel_listing_update_with_prior_price` (function) — [saleor/graphql/product/tests/test_variant_channel_listing_update.py:628]

**`saleor/graphql/product/tests/test_variant_pricing.py`**

- `test_get_variant_pricing_on_promotion` (function) — [saleor/graphql/product/tests/test_variant_pricing.py:58]
- `test_get_variant_pricing_not_on_promotion` (function) — [saleor/graphql/product/tests/test_variant_pricing.py:100]
- `test_variant_pricing` (function) — [saleor/graphql/product/tests/test_variant_pricing.py:127]
- `test_variant_pricing_no_prices` (function) — [saleor/graphql/product/tests/test_variant_pricing.py:168]
- `test_product_variant_price` (function) — [saleor/graphql/product/tests/test_variant_pricing.py:234]
- `test_product_variant_without_price_as_user` (function) — [saleor/graphql/product/tests/test_variant_pricing.py:262]
- `test_product_variant_without_price_as_staff_without_permission` (function) — [saleor/graphql/product/tests/test_variant_pricing.py:291]
- `test_product_variant_without_price_as_staff_with_permission` (function) — [saleor/graphql/product/tests/test_variant_pricing.py:320]
- `test_product_variant_price_no_address` (function) — [saleor/graphql/product/tests/test_variant_pricing.py:389]
- `test_product_variant_pricing` (function) — [saleor/graphql/product/tests/test_variant_pricing.py:483]
- `test_product_variant_pricing_default_country_default_rate` (function) — [saleor/graphql/product/tests/test_variant_pricing.py:524]
- `test_product_variant_pricing_use_tax_class_from_product_type` (function) — [saleor/graphql/product/tests/test_variant_pricing.py:562]
- `test_product_variant_pricing_no_flat_rates_in_one_country` (function) — [saleor/graphql/product/tests/test_variant_pricing.py:602]

**`saleor/graphql/product/tests/test_variant_with_filtering.py`**

- `products_for_variant_filtering` (function) — [saleor/graphql/product/tests/test_variant_with_filtering.py:26]
- `test_products_pagination_with_filtering` (function) — [saleor/graphql/product/tests/test_variant_with_filtering.py:155]
- `test_product_variant_query_with_filter_updated_at` (function) — [saleor/graphql/product/tests/test_variant_with_filtering.py:213]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/product/tests/__init__.py` (1 lines)
- `saleor/graphql/product/tests/app/__init__.py` (1 lines)
- `saleor/graphql/product/tests/test_attributes.py` (2052 lines)
- `saleor/graphql/product/tests/test_bulk_delete.py` (1946 lines)
- `saleor/graphql/product/tests/test_collection_filtering_and_sorting_with_channels.py` (1 lines)
- `saleor/graphql/product/tests/test_product_channel_listings_queries.py` (510 lines)
- `saleor/graphql/product/tests/test_product_discounted_price.py` (423 lines)
- `saleor/graphql/product/tests/test_product_filtering_and_sorting_with_channels.py` (830 lines)
- `saleor/graphql/product/tests/test_product_pagination.py` (981 lines)
- `saleor/graphql/product/tests/test_product_pricing.py` (298 lines)
- `saleor/graphql/product/tests/test_product_prior_price.py` (41 lines)
- `saleor/graphql/product/tests/test_product_sorting_attributes.py` (694 lines)
- `saleor/graphql/product/tests/test_product_sorting.py` (849 lines)
- `saleor/graphql/product/tests/test_variant_availability.py` (948 lines)
- `saleor/graphql/product/tests/test_variant_channel_listing_update.py` (657 lines)
- `saleor/graphql/product/tests/test_variant_pricing.py` (645 lines)
- `saleor/graphql/product/tests/test_variant_with_filtering.py` (241 lines)

## Interactions

- Imports from: `saleor/graphql/product/bulk_mutations`, `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....attribute.AttributeInputType`
- `....attribute.AttributeType`
- `....attribute.models`
- `....attribute.models.AttributeValue`
- `....attribute.utils.associate_attribute_values_to_instance`
- `....channel.utils.DEPRECATION_WARNING_MESSAGE`
- `....checkout.fetch.fetch_checkout_info`
- `....checkout.fetch.fetch_checkout_lines`
- `....checkout.tests.utils.add_variant_to_checkout`
- `....checkout.utils.calculate_checkout_quantity`
- `....discount.models.Promotion`
- `....discount.models.PromotionRule`
- `....discount.utils.promotion.get_active_catalogue_promotion_rules`
- `....order.OrderEvents`
- `....order.OrderStatus`
- `....order.models.OrderEvent`
- `....order.models.OrderLine`
- `....plugins.manager.get_plugins_manager`
- `....product.ProductTypeKind`
- `....product.error_codes.ProductErrorCode`
- `....product.models`
- `....product.models.CollectionProduct`
- `....product.models.Product`
- `....product.models.ProductChannelListing`
- `....product.models.ProductType`
- `....product.models.ProductVariant`
- `....product.models.ProductVariantChannelListing`
- `....product.search.update_products_search_vector`
- `....product.utils.availability.get_variant_availability`
- `....shipping.models.ShippingZone`
- `....tax.TaxCalculationStrategy`
- `....tax.models.TaxClassCountryRate`
- `....tax.models.TaxConfigurationPerCountry`
- `....tax.utils.get_display_gross_prices`
- `....tests.utils.dummy_editorjs`
- `....thumbnail.models.Thumbnail`
- `....warehouse.WarehouseClickAndCollectOption`
- `....warehouse.models.PreorderReservation`
- `....warehouse.models.Reservation`
- `....warehouse.models.Stock`
- `....warehouse.models.Warehouse`
- `...attribute.enums.AttributeTypeEnum`
- `...core.connection.from_global_cursor`
- `...core.connection.to_global_cursor`
- `...core.utils.snake_to_camel_case`
- `...discount.enums.DiscountValueTypeEnum`
- `...tests.utils.assert_graphql_error_with_message`
- `...tests.utils.get_graphql_content`
- `..bulk_mutations.product_bulk_delete.ProductBulkDelete`
- `..bulk_mutations.product_variant_bulk_delete.ProductVariantBulkDelete`
- `..enums.ProductAttributeType`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `a24d34e4a3e7` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
