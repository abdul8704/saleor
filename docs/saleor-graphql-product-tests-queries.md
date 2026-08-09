## Purpose

`saleor/graphql/product/tests/queries` (`saleor/graphql/product/tests/queries`) groups 20 source file(s) exposing 487 top-level declaration(s).

## Public surface

**`saleor/graphql/product/tests/queries/test_categories_query_with_filter.py`**

- `categories_for_filtering` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:17]
- `test_categories_with_filtering` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:59]
- `test_order_query_with_filter_updated_at` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:110]
- `test_category_filter_products_by_channel` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:222]
- `test_category_filter_products_by_is_published` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:275]
- `test_category_filter_products_by_multiple_attributes` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:316]
- `test_category_filter_products_by_stock_availability` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:379]
- `test_category_filter_products_by_stocks` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:436]
- `test_category_filter_products_search_by_sku` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:529]
- `test_category_filter_products_by_price` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:570]
- `test_category_filter_products_by_ids` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:601]
- `test_category_where_products_by_is_published` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:639]
- `test_category_search_products_by_sku` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:687]
- `test_category_sort_products_by_name` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:753]
- `test_category_products_where_filter` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:783]
- `test_categories_where_by_ids` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:828]
- `test_categories_where_by_none_as_ids` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:850]
- `test_categories_where_by_ids_empty_list` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:863]
- `test_categories_query_with_filter` (function) — [saleor/graphql/product/tests/queries/test_categories_query_with_filter.py:895]

**`saleor/graphql/product/tests/queries/test_categories_query.py`**

- `test_category_level` (function) — [saleor/graphql/product/tests/queries/test_categories_query.py:25]
- `test_categories_query_ids_not_exists` (function) — [saleor/graphql/product/tests/queries/test_categories_query.py:57]
- `test_categories_query_with_sort` (function) — [saleor/graphql/product/tests/queries/test_categories_query.py:110]

**`saleor/graphql/product/tests/queries/test_category_query.py`**

- `test_category_query_by_id` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:52]
- `test_category_query_with_ancestors` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:68]
- `test_category_query_invalid_id` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:90]
- `test_category_query_object_with_given_id_does_not_exist` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:106]
- `test_category_query_object_with_invalid_object_type` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:119]
- `test_category_query_doesnt_show_not_available_products` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:133]
- `test_category_query_description` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:154]
- `test_category_query_without_description` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:183]
- `test_category_query_by_slug` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:210]
- `test_category_query_by_translated_slug` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:222]
- `test_category_query_error_when_id_and_slug_provided` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:237]
- `test_category_query_error_when_no_param` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:261]
- `test_query_category_product_only_visible_in_listings_as_customer` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:280]
- `test_query_category_product_visible_in_listings_as_staff_without_manage_products` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:303]
- `test_query_category_product_only_visible_in_listings_as_staff_with_perm` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:328]
- `test_query_category_product_only_visible_in_listings_as_app_without_manage_products` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:350]
- `test_query_category_product_only_visible_in_listings_as_app_with_perm` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:375]
- `test_category_image_query_with_size_and_format_proxy_url_returned` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:410]
- `test_category_image_query_with_size_proxy_url_returned` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:445]
- `test_category_image_query_with_size_thumbnail_url_returned` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:478]
- `test_category_image_query_zero_size_custom_format_provided_original_image_returned` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:515]
- `test_category_image_query_zero_size_value_original_image_returned` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:550]
- `test_category_image_query_without_associated_file` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:582]
- `test_query_category_for_federation` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:600]
- `test_query_products_no_channel_shipping_zones` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:633]
- `test_fetch_product_from_category_query` (function) — [saleor/graphql/product/tests/queries/test_category_query.py:670]

**`saleor/graphql/product/tests/queries/test_collection_query.py`**

- `test_collection_query_by_id` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:27]
- `test_collection_query_unpublished_collection_by_id_as_app` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:40]
- `test_collection_query_by_slug` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:64]
- `test_collection_query_by_translated_slug` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:76]
- `test_collection_query_unpublished_collection_by_slug_as_staff` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:91]
- `test_collection_query_unpublished_collection_by_slug_and_anonymous_user` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:110]
- `test_collection_query_error_when_id_and_slug_provided` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:125]
- `test_collection_query_error_when_no_param` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:149]
- `test_filter_collection_products` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:213]
- `test_filter_collection_published_products` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:240]
- `test_filter_collection_products_by_multiple_attributes` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:273]
- `test_filter_where_collection_products` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:337]
- `test_search_collection_products` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:369]
- `test_collection_image_query_with_size_and_format_proxy_url_returned` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:411]
- `test_collection_image_query_with_size_proxy_url_returned` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:448]
- `test_collection_image_query_with_size_thumbnail_url_returned` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:482]
- `test_collection_image_query_zero_size_custom_format_provided` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:520]
- `test_collection_image_query_zero_size_value_original_image_returned` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:556]
- `test_collection_image_query_without_associated_file` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:589]
- `test_collection_query_invalid_id` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:607]
- `test_collection_query_object_with_given_id_does_not_exist` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:625]
- `test_collection_query_object_with_invalid_object_type` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:638]
- `test_fetch_unpublished_collection_staff_user` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:673]
- `test_fetch_unpublished_collection_customer` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:686]
- `test_fetch_unpublished_collection_anonymous_user` (function) — [saleor/graphql/product/tests/queries/test_collection_query.py:695]

**`saleor/graphql/product/tests/queries/test_collections_query_with_filter_and_sort.py`**

- `test_collections_query_with_filter` (function) — [saleor/graphql/product/tests/queries/test_collections_query_with_filter_and_sort.py:32]
- `collections_for_sorting_with_channels` (function) — [saleor/graphql/product/tests/queries/test_collections_query_with_filter_and_sort.py:95]
- `test_collections_with_sorting_and_without_channel` (function) — [saleor/graphql/product/tests/queries/test_collections_query_with_filter_and_sort.py:187]
- `test_collections_with_sorting_and_channel_USD` (function) — [saleor/graphql/product/tests/queries/test_collections_query_with_filter_and_sort.py:228]
- `test_collections_with_sorting_and_channel_PLN` (function) — [saleor/graphql/product/tests/queries/test_collections_query_with_filter_and_sort.py:275]
- `test_collections_with_sorting_and_not_existing_channel_asc` (function) — [saleor/graphql/product/tests/queries/test_collections_query_with_filter_and_sort.py:309]
- `test_collections_with_sorting_and_not_existing_channel_desc` (function) — [saleor/graphql/product/tests/queries/test_collections_query_with_filter_and_sort.py:339]
- `test_collections_with_filtering_without_channel` (function) — [saleor/graphql/product/tests/queries/test_collections_query_with_filter_and_sort.py:362]
- `test_collections_with_filtering_with_channel_USD` (function) — [saleor/graphql/product/tests/queries/test_collections_query_with_filter_and_sort.py:390]
- `test_collections_with_filtering_with_channel_PLN` (function) — [saleor/graphql/product/tests/queries/test_collections_query_with_filter_and_sort.py:419]
- `test_collections_with_filtering_and_not_existing_channel` (function) — [saleor/graphql/product/tests/queries/test_collections_query_with_filter_and_sort.py:452]
- `test_collections_where_by_ids` (function) — [saleor/graphql/product/tests/queries/test_collections_query_with_filter_and_sort.py:490]
- `test_collections_where_by_none_as_ids` (function) — [saleor/graphql/product/tests/queries/test_collections_query_with_filter_and_sort.py:512]
- `test_collections_where_by_ids_empty_list` (function) — [saleor/graphql/product/tests/queries/test_collections_query_with_filter_and_sort.py:525]

**`saleor/graphql/product/tests/queries/test_collections_query.py`**

- `test_collections_query` (function) — [saleor/graphql/product/tests/queries/test_collections_query.py:13]
- `test_collections_query_without_description` (function) — [saleor/graphql/product/tests/queries/test_collections_query.py:56]
- `test_collections_query_as_staff` (function) — [saleor/graphql/product/tests/queries/test_collections_query.py:94]
- `test_collections_query_as_staff_without_channel` (function) — [saleor/graphql/product/tests/queries/test_collections_query.py:126]
- `test_collections_query_ids_not_exists` (function) — [saleor/graphql/product/tests/queries/test_collections_query.py:171]
- `test_sort_collection_products_by_name` (function) — [saleor/graphql/product/tests/queries/test_collections_query.py:203]
- `test_query_collection_for_federation` (function) — [saleor/graphql/product/tests/queries/test_collections_query.py:245]
- `test_collections_query_with_sort` (function) — [saleor/graphql/product/tests/queries/test_collections_query.py:303]
- `test_pagination_for_sorting_collections_by_published_at_date` (function) — [saleor/graphql/product/tests/queries/test_collections_query.py:358]
- `test_collections_query_return_error_with_sort_by_rank_without_search` (function) — [saleor/graphql/product/tests/queries/test_collections_query.py:416]

**`saleor/graphql/product/tests/queries/test_product_query.py`**

- `test_product_query_by_id_available_as_staff_user` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:50]
- `test_product_query_description` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:70]
- `test_product_query_with_no_description` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:108]
- `test_product_query_by_id_not_available_as_staff_user` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:143]
- `test_product_query_by_id_not_existing_in_channel_as_staff_user` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:166]
- `test_product_query_by_id_as_staff_user_without_channel_slug` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:186]
- `test_product_query_by_id_available_as_app` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:206]
- `test_product_query_by_invalid_id` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:227]
- `test_product_query_by_id_as_user` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:262]
- `test_product_query_invalid_id` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:299]
- `test_product_query_object_with_given_id_does_not_exist` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:315]
- `test_product_query_with_invalid_object_type` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:328]
- `test_product_query_by_id_not_available_as_app` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:339]
- `test_product_query_by_id_not_existing_in_channel_as_app` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:362]
- `test_product_query_by_id_as_app_without_channel_slug` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:382]
- `test_product_variants_without_sku_query_by_staff` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:402]
- `test_product_only_with_variants_without_sku_query_by_customer` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:435]
- `test_product_only_with_variants_without_sku_query_by_anonymous` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:467]
- `test_product_variants_query_by_staff_no_channel_provided` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:499]
- `test_product_variants_query_by_app_no_channel_provided` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:531]
- `test_query_product_thumbnail_with_size_and_format_proxy_url_returned` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:578]
- `test_query_product_thumbnail_with_size_and_proxy_url_returned` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:607]
- `test_query_product_thumbnail_with_size_and_thumbnail_url_returned` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:633]
- `test_query_product_thumbnail_only_format_provided_default_size_is_used` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:664]
- `test_query_product_thumbnail_no_product_media` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:692]
- `test_get_collections_from_product_as_staff` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:725]
- `test_get_collections_from_product_as_app` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:751]
- `test_get_collections_from_product_as_customer` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:777]
- `test_get_collections_from_product_as_anonymous` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:802]
- `test_product_query_by_id_available_as_customer` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:827]
- `test_product_query_by_id_not_available_as_customer` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:845]
- `test_product_unpublished_query_by_id_as_app` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:862]
- `test_product_query_by_id_weight_returned_in_default_unit` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:886]
- `test_product_query_by_id_weight_is_rounded` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:914]
- `test_product_query_by_id_unpublished` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:941]
- `test_product_query_by_translated_slug` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:956]
- `test_product_query_by_id_not_existing_in_channel_as_customer` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:975]
- `test_product_query_by_slug_available_as_staff_user` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:990]
- `test_product_query_by_slug_not_available_as_staff_user` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:1010]
- `test_product_query_by_slug_not_existing_in_channel_as_staff_user` (function) — [saleor/graphql/product/tests/queries/test_product_query.py:1033]
- _…and 70 more in this file_

**`saleor/graphql/product/tests/queries/test_product_type_query.py`**

- `test_product_type_query` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:45]
- `test_product_type_query_invalid_id` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:100]
- `test_product_type_query_object_with_given_id_does_not_exist` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:118]
- `test_product_type_query_with_invalid_object_type` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:131]
- `test_product_type_query_only_variant_selections_value_set` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:153]
- `test_product_type_query_only_assigned_variant_selections_value_set` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:268]
- `test_product_type_get_unassigned_product_type_attributes` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:375]
- `test_product_type_filter_unassigned_attributes` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:451]
- `test_product_type_where_filter_unassigned_attributes` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:476]
- `test_product_type_search_unassigned_attributes` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:501]
- `test_product_type_query_by_id_weight_returned_in_default_unit` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:545]
- `test_query_product_type_for_federation` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:570]
- `test_product_type_tax_class_query_by_app` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:616]
- `test_product_type_tax_class_query_by_staff` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:636]
- `test_product_type_attribute_not_visible_in_storefront_for_customer_is_not_returned` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:676]
- `test_product_type_attribute_visible_in_storefront_for_customer_is_returned` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:736]
- `test_product_type_attribute_visible_in_storefront_for_staff_is_always_returned` (function) — [saleor/graphql/product/tests/queries/test_product_type_query.py:797]

**`saleor/graphql/product/tests/queries/test_product_types_query.py`**

- `test_product_types` (function) — [saleor/graphql/product/tests/queries/test_product_types_query.py:8]
- `test_product_type_query_with_filter` (function) — [saleor/graphql/product/tests/queries/test_product_types_query.py:49]
- `test_product_type_query_with_sort` (function) — [saleor/graphql/product/tests/queries/test_product_types_query.py:128]
- `test_product_types_query_ids_not_exists` (function) — [saleor/graphql/product/tests/queries/test_product_types_query.py:178]
- `test_filter_product_types_by_custom_search_value` (function) — [saleor/graphql/product/tests/queries/test_product_types_query.py:212]

**`saleor/graphql/product/tests/queries/test_product_variant_query.py`**

- `test_fetch_variant` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:73]
- `test_fetch_variant_no_stocks` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:121]
- `test_fetch_variant_stocks_from_click_and_collect_warehouse` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:172]
- `test_get_product_variant_channel_listing_as_staff_user` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:233]
- `test_get_product_variant_channel_listing_as_app` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:272]
- `test_get_product_variant_channel_listing_as_customer` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:311]
- `test_get_product_variant_channel_listing_as_anonymous` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:331]
- `test_get_product_variant_stocks` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:377]
- `test_get_product_variant_stocks_no_channel_shipping_zones` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:426]
- `test_get_product_variant_preorder_as_staff` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:471]
- `test_get_product_variant_preorder_as_customer_not_allowed_fields` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:499]
- `test_get_product_variant_preorder_as_customer_allowed_fields` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:519]
- `test_fetch_unpublished_variant_staff_user` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:571]
- `test_fetch_unpublished_variant_customer` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:590]
- `test_fetch_unpublished_variant_anonymous_user` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:598]
- `test_fetch_variant_without_sku_staff_user` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:606]
- `test_fetch_variant_without_sku_customer` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:625]
- `test_fetch_variant_without_sku_anonymous` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:644]
- `test_query_product_variant_for_federation_as_customer` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:674]
- `test_query_product_variant_for_federation_as_customer_not_existing_channel` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:699]
- `test_query_product_variant_for_federation_as_customer_channel_not_active` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:718]
- `test_query_product_variant_for_federation_as_customer_without_channel` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:739]
- `test_query_product_variant_for_federation_as_staff_user` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:757]
- `test_query_product_variant_for_federation_as_staff_user_not_existing_channel` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:785]
- `test_query_product_variant_for_federation_as_staff_user_channel_not_active` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:807]
- `test_query_product_variant_for_federation_as_staff_user_without_chanel` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:837]
- `test_product_variant_with_assigned_attribute` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:882]
- `test_product_variant_with_assigned_attribute_without_value` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:917]
- `test_product_variant_when_assigned_attribute_is_none` (function) — [saleor/graphql/product/tests/queries/test_product_variant_query.py:951]

**`saleor/graphql/product/tests/queries/test_product_variants_query_with_where.py`**

- `test_product_variant_filter_by_ids` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query_with_where.py:26]
- `test_product_variant_filter_by_none_as_ids` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query_with_where.py:48]
- `test_product_variant_filter_by_ids_empty_list` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query_with_where.py:63]
- `test_product_variant_filter_by_updated_at` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query_with_where.py:107]
- `test_product_variant_filter_by_sku` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query_with_where.py:151]

**`saleor/graphql/product/tests/queries/test_product_variants_query.py`**

- `test_fetch_all_variants_staff_user` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:32]
- `test_fetch_all_variants_staff_user_with_channel` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:44]
- `test_fetch_all_variants_staff_user_without_channel` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:57]
- `test_fetch_all_variants_customer` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:68]
- `test_fetch_all_variants_anonymous_user` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:75]
- `test_fetch_all_variants_without_sku_staff_user` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:82]
- `test_fetch_all_variants_without_sku_staff_user_with_channel` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:97]
- `test_fetch_all_variants_without_sku_as_customer_with_channel` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:116]
- `test_fetch_all_variants_without_sku_as_anonymous_user_with_channel` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:130]
- `test_pagination_with_non_unique_default_ordering` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:176]
- `test_product_variants_by_ids` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:242]
- `test_product_variants_by_invalid_ids` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:254]
- `test_product_variants_by_ids_that_do_not_exist` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:269]
- `test_product_variants_visible_in_listings_by_customer` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:281]
- `test_product_variants_visible_in_listings_by_staff_without_manage_products` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:295]
- `test_product_variants_visible_in_listings_by_staff_with_perm` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:311]
- `test_product_variants_visible_in_listings_by_app_without_manage_products` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:329]
- `test_product_variants_visible_in_listings_by_app_with_perm` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:343]
- `test_search_product_variants_by_variant_name_and_sku` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:380]
- `test_search_products_by_product_name` (function) — [saleor/graphql/product/tests/queries/test_product_variants_query.py:408]

**`saleor/graphql/product/tests/queries/test_product_variants_where_unassigned_attribute.py`**

- `test_variant_not_filterable_by_attribute_after_unassign` (function) — [saleor/graphql/product/tests/queries/test_product_variants_where_unassigned_attribute.py:39]

**`saleor/graphql/product/tests/queries/test_products_query_with_filter.py`**

- `test_products_query_with_filter_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:44]
- `test_products_query_with_filter_numeric_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:108]
- `test_products_query_with_filter_boolean_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:208]
- `test_products_query_with_filter_non_existing_boolean_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:282]
- `test_products_query_with_filter_boolean_attributes_not_assigned_to_product` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:313]
- `test_products_query_with_filter_by_attributes_values_and_range` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:341]
- `test_products_query_with_filter_swatch_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:408]
- `test_products_query_with_filter_date_range_date_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:470]
- `test_products_query_with_filter_date_range_date_variant_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:533]
- `test_products_query_with_filter_date_range_date_time_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:596]
- `test_products_query_with_filter_date_range_date_time_variant_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:662]
- `test_products_query_with_filter_date_time_range_date_time_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:728]
- `test_products_query_filter_by_non_existing_attribute` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:801]
- `test_products_query_with_filter_category` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:814]
- `test_products_query_with_filter_has_category_false` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:842]
- `test_products_query_with_filter_has_category_true` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:868]
- `test_products_query_with_filter_collection` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:897]
- `test_products_query_with_filter_category_and_search` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:927]
- `test_products_query_with_filter_gift_card_false` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:965]
- `test_products_query_with_filter_gift_card_true` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:988]
- `test_products_query_with_filter` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1019]
- `test_products_query_with_price_filter_as_staff` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1071]
- `test_products_query_with_price_filter_as_user` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1097]
- `test_products_query_with_filter_search_by_sku` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1126]
- `test_products_query_with_filter_search_by_dropdown_attribute_value` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1155]
- `test_products_query_with_filter_search_by_multiselect_attribute_value` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1207]
- `test_products_query_with_filter_search_by_rich_text_attribute` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1264]
- `test_products_query_with_filter_search_by_plain_text_attribute` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1313]
- `test_products_query_with_filter_search_by_numeric_attribute_value` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1362]
- `test_products_query_with_filter_search_by_numeric_attribute_value_without_unit` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1414]
- `test_products_query_with_filter_search_by_date_attribute_value` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1464]
- `test_products_query_with_filter_search_by_date_time_attribute_value` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1513]
- `test_products_query_with_is_published_filter_variants_without_prices` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1563]
- `test_products_query_with_is_published_filter_one_variant_without_price` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1591]
- `test_products_query_with_filter_stock_availability_as_staff` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1618]
- `test_products_query_with_filter_stock_availability_including_reservations` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1657]
- `test_products_query_with_filter_stock_availability_as_user` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1723]
- `test_products_query_with_filter_stock_availability_channel_without_shipping_zones` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1767]
- `test_products_filter_stock_availability_without_shipping_zones_excluded_from_stock_calculations` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1793]
- `test_products_query_with_filter_stock_availability_only_stock_in_cc_warehouse` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_filter.py:1824]
- _…and 6 more in this file_

**`saleor/graphql/product/tests/queries/test_products_query_with_where.py`**

- `test_product_filter_by_ids` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:33]
- `test_product_filter_by_none_as_ids` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:55]
- `test_product_filter_by_ids_empty_list` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:68]
- `test_product_filter_by_name` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:94]
- `test_product_filter_by_slug` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:122]
- `test_product_filter_by_product_types` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:137]
- `test_product_filter_by_product_type` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:169]
- `test_product_filter_by_none_as_product_type` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:193]
- `test_product_filter_by_categories` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:214]
- `test_product_filter_by_subcategories` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:246]
- `test_product_filter_by_category` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:284]
- `test_product_filter_by_none_as_category` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:308]
- `test_product_filter_by_collections` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:329]
- `test_product_filter_by_collection` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:357]
- `test_product_filter_by_none_as_collection` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:379]
- `test_product_filter_by_is_available` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:409]
- `test_product_filter_by_is_published` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:440]
- `test_product_filter_by_is_visible_in_listing` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:471]
- `test_product_filter_by_has_category` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:502]
- `test_product_filter_by_published_from` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:524]
- `test_product_filter_by_none_as_published_from` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:548]
- `test_product_filter_by_available_from` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:573]
- `test_product_filter_by_none_as_available_from` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:598]
- `test_product_filter_by_variant_price` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:637]
- `test_product_filter_by_minimal_price` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:671]
- `test_products_filter_by_attributes_value_slug` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:691]
- `test_products_filter_by_attributes_empty` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:754]
- `test_products_filter_by_numeric_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:813]
- `test_products_filter_by_boolean_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:876]
- `test_products_filter_by_attributes_values_and_range` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:924]
- `test_products_filter_by_swatch_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:981]
- `test_products_filter_by_date_range_date_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:1028]
- `test_products_filter_by_date_range_date_variant_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:1089]
- `test_products_filter_by_date_range_date_time_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:1150]
- `test_products_filter_by_date_range_date_time_variant_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:1214]
- `test_products_filter_by_date_time_range_date_time_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:1278]
- `test_products_filter_by_non_existing_attribute` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:1349]
- `test_products_filter_by_stock_availability` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:1370]
- `test_products_filter_by_stock_availability_including_reservations` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:1398]
- `test_products_filter_by_stock_availability_as_user` (function) — [saleor/graphql/product/tests/queries/test_products_query_with_where.py:1462]
- _…and 16 more in this file_

**`saleor/graphql/product/tests/queries/test_products_query.py`**

- `test_fetch_all_products_available_as_staff_user` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:38]
- `test_fetch_all_product_variants_available_as_staff_user_with_channel` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:54]
- `test_fetch_all_product_variants_available_as_staff_user_without_channel` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:77]
- `test_fetch_all_products_not_available_as_staff_user` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:99]
- `test_fetch_all_products_not_existing_in_channel_as_staff_user` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:119]
- `test_fetch_all_products_as_staff_user_without_channel_slug` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:142]
- `test_fetch_all_products_available_as_app` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:160]
- `test_fetch_all_products_not_available_as_app` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:176]
- `test_fetch_all_products_not_existing_in_channel_as_app` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:196]
- `test_fetch_all_products_as_app_without_channel_slug` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:218]
- `test_fetch_all_products_available_as_customer` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:236]
- `test_fetch_all_products_not_available_as_customer` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:247]
- `test_fetch_all_products_not_existing_in_channel_as_customer` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:264]
- `test_fetch_all_products_available_as_anonymous` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:276]
- `test_fetch_all_products_not_available_as_anonymous` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:285]
- `test_fetch_all_products_not_existing_in_channel_as_anonymous` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:302]
- `test_fetch_all_products_visible_in_listings` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:314]
- `test_fetch_all_products_visible_in_listings_by_staff_with_perm` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:334]
- `test_fetch_all_products_visible_in_listings_by_staff_without_manage_products` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:357]
- `test_fetch_all_products_visible_in_listings_by_app_with_perm` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:375]
- `test_fetch_all_products_visible_in_listings_by_app_without_manage_products` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:398]
- `test_filter_products_by_wrong_attributes` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:416]
- `test_filter_products_with_unavailable_variants_attributes_as_user` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:448]
- `test_filter_products_with_unavailable_variants_attributes_as_staff` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:490]
- `test_sort_products` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:565]
- `test_sort_products_by_price_as_staff` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:673]
- `test_sort_products_product_type_name` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:750]
- `test_search_product_by_description` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:803]
- `test_search_product_by_description_and_name` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:816]
- `test_sort_product_by_rank_without_search` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:857]
- `test_products_query_by_rank_returns_error_with_filter_nontype_search` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:871]
- `test_products_query_by_rank_returns_error_with_nontype_search` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:898]
- `test_search_product_by_description_and_name_without_sort_by` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:938]
- `test_search_product_by_description_and_name_and_use_cursor` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:977]
- `test_hidden_product_access_with_proper_permissions` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:1022]
- `test_hidden_product_access_with_permission_manage_orders` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:1046]
- `test_hidden_product_access_with_permission_manage_discounts` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:1069]
- `test_hidden_product_access_with_permission_manage_channels` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:1092]
- `test_product_filter_by_attribute_values` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:1115]
- `test_products_with_variants_query_as_app` (function) — [saleor/graphql/product/tests/queries/test_products_query.py:1163]
- _…and 5 more in this file_

**`saleor/graphql/product/tests/queries/test_report_product_sales.py`**

- `test_report_product_sales` (function) — [saleor/graphql/product/tests/queries/test_report_product_sales.py:25]
- `test_report_product_sales_channel_pln` (function) — [saleor/graphql/product/tests/queries/test_report_product_sales.py:55]
- `test_report_product_sales_not_existing_channel` (function) — [saleor/graphql/product/tests/queries/test_report_product_sales.py:85]

**`saleor/graphql/product/tests/queries/test_variant_query.py`**

- `test_get_variant_without_id_sku_and_external_reference` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:67]
- `test_get_variant_with_id_and_sku` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:86]
- `test_get_unpublished_variant_by_id_as_staff` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:104]
- `test_get_unpublished_variant_by_id_as_app` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:126]
- `test_get_unpublished_variant_by_id_as_customer` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:148]
- `test_get_unpublished_variant_by_id_as_anonymous_user` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:168]
- `test_get_variant_by_id_as_staff` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:188]
- `test_get_variant_by_id_as_app` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:209]
- `test_get_variant_by_id_as_customer` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:228]
- `test_get_variant_by_id_as_anonymous_user` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:246]
- `test_get_variant_without_sku_by_id_as_staff` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:264]
- `test_get_variant_without_sku_by_id_as_app` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:288]
- `test_get_variant_without_sku_by_id_as_customer` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:312]
- `test_get_variant_without_sku_by_id_as_anonymous_user` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:335]
- `test_get_unpublished_variant_by_sku_as_staff` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:358]
- `test_get_unpublished_variant_by_sku_as_app` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:379]
- `test_get_unpublished_variant_by_sku_as_customer` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:400]
- `test_get_unpublished_variant_by_sku_as_anonymous_user` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:419]
- `test_get_variant_by_sku_as_staff` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:438]
- `test_get_variant_by_external_reference` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:458]
- `test_get_variant_by_sku_as_app` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:481]
- `test_get_variant_by_sku_as_customer` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:499]
- `test_get_variant_by_sku_as_anonymous_user` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:516]
- `test_get_variant_by_id_with_variant_selection_filter` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:541]
- `test_get_variant_with_sorted_attribute_values` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:592]
- `test_variant_quantity_ordered_field_is_restricted_with_permissions` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:657]
- `test_product_variant_without_price_by_sku_as_user` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:682]
- `test_product_variant_without_price_by_sku_as_app_without_permission` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:704]
- `test_product_variant_without_price_by_sku_as_app_with_permission` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:727]
- `test_product_variant_without_price_by_sku_as_staff_without_permission` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:755]
- `test_product_variant_without_price_by_sku_as_staff_with_permission` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:776]
- `test_product_variant_without_price_by_id_as_staff_with_permission` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:815]
- `test_product_variant_without_price_by_id_as_staff_without_permission` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:835]
- `test_product_variant_without_price_by_id_as_app_without_permission` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:849]
- `test_product_variant_without_price_by_id_as_app_with_permission` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:863]
- `test_product_variant_without_price_by_id_as_user` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:883]
- `test_variant_query_invalid_id` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:898]
- `test_variant_query_object_with_given_id_does_not_exist` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:914]
- `test_variant_query_with_invalid_object_type` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:927]
- `test_stock_quantities_in_different_warehouses` (function) — [saleor/graphql/product/tests/queries/test_variant_query.py:938]
- _…and 5 more in this file_

**`saleor/graphql/product/tests/queries/test_variants_query.py`**

- `test_product_variants_by_ids` (function) — [saleor/graphql/product/tests/queries/test_variants_query.py:7]
- `test_product_variants_without_price_by_ids_as_staff_without_permission` (function) — [saleor/graphql/product/tests/queries/test_variants_query.py:43]
- `test_product_variants_without_price_by_ids_as_staff_with_permission` (function) — [saleor/graphql/product/tests/queries/test_variants_query.py:82]
- `test_product_variants_without_price_by_ids_as_user` (function) — [saleor/graphql/product/tests/queries/test_variants_query.py:127]
- `test_product_variants_without_price_by_ids_as_app_without_permission` (function) — [saleor/graphql/product/tests/queries/test_variants_query.py:154]
- `test_product_variants_without_price_by_ids_as_app_with_permission` (function) — [saleor/graphql/product/tests/queries/test_variants_query.py:192]
- `test_product_variants_by_customer` (function) — [saleor/graphql/product/tests/queries/test_variants_query.py:237]
- `test_product_variants_no_ids_list` (function) — [saleor/graphql/product/tests/queries/test_variants_query.py:270]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/product/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/product/tests/queries/test_categories_query_with_filter.py` (949 lines)
- `saleor/graphql/product/tests/queries/test_categories_query.py` (158 lines)
- `saleor/graphql/product/tests/queries/test_category_query.py` (769 lines)
- `saleor/graphql/product/tests/queries/test_collection_query.py` (701 lines)
- `saleor/graphql/product/tests/queries/test_collections_query_with_filter_and_sort.py` (535 lines)
- `saleor/graphql/product/tests/queries/test_collections_query.py` (439 lines)
- `saleor/graphql/product/tests/queries/test_product_query.py` (3113 lines)
- `saleor/graphql/product/tests/queries/test_product_type_query.py` (858 lines)
- `saleor/graphql/product/tests/queries/test_product_types_query.py` (234 lines)
- `saleor/graphql/product/tests/queries/test_product_variant_query.py` (972 lines)
- `saleor/graphql/product/tests/queries/test_product_variants_query_with_where.py` (174 lines)
- `saleor/graphql/product/tests/queries/test_product_variants_query.py` (430 lines)
- `saleor/graphql/product/tests/queries/test_product_variants_where_unassigned_attribute.py` (95 lines)
- `saleor/graphql/product/tests/queries/test_products_query_with_filter.py` (2075 lines)
- `saleor/graphql/product/tests/queries/test_products_query_with_where.py` (2002 lines)
- `saleor/graphql/product/tests/queries/test_products_query.py` (1492 lines)
- `saleor/graphql/product/tests/queries/test_report_product_sales.py` (98 lines)
- `saleor/graphql/product/tests/queries/test_variant_query.py` (1172 lines)
- `saleor/graphql/product/tests/queries/test_variants_query.py` (286 lines)

## Interactions

- Imports from: `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....attribute.AttributeInputType`
- `.....attribute.AttributeType`
- `.....attribute.models.Attribute`
- `.....attribute.models.AttributeValue`
- `.....attribute.tests.model_helpers.get_product_attributes`
- `.....attribute.utils.associate_attribute_values_to_instance`
- `.....core.postgres.FlatConcatSearchVector`
- `.....core.taxes.TaxType`
- `.....core.units.MeasurementUnits`
- `.....core.units.WeightUnits`
- `.....plugins.manager.PluginsManager`
- `.....product.ProductTypeKind`
- `.....product.models.Category`
- `.....product.models.Collection`
- `.....product.models.CollectionChannelListing`
- `.....product.models.Product`
- `.....product.models.ProductChannelListing`
- `.....product.models.ProductType`
- `.....product.models.ProductVariant`
- `.....product.search.prepare_product_search_vector_value`
- `.....product.search.update_products_search_vector`
- `.....product.tests.utils.create_image`
- `.....product.utils.costs.get_product_costs_data`
- `.....tests.utils.dummy_editorjs`
- `.....thumbnail.models.Thumbnail`
- `.....warehouse.WarehouseClickAndCollectOption`
- `.....warehouse.models.Allocation`
- `.....warehouse.models.Reservation`
- `.....warehouse.models.Stock`
- `.....warehouse.models.Warehouse`
- `....core.connection.from_global_cursor`
- `....core.enums.LanguageCodeEnum`
- `....core.enums.ReportingPeriod`
- `....core.enums.ThumbnailFormatEnum`
- `....core.enums.WeightUnitsEnum`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `....tests.utils.get_graphql_content_from_response`
- `...enums.VariantAttributeScope`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `5a2f3bcc5bd5` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
