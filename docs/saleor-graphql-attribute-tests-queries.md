## Purpose

`saleor/graphql/attribute/tests/queries` (`saleor/graphql/attribute/tests/queries`) groups 8 source file(s) exposing 175 top-level declaration(s).

## Public surface

**`saleor/graphql/attribute/tests/queries/test_attribute_filter.py`**

- `test_search_attributes` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:48]
- `test_search_attributes_value` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:63]
- `test_atribute_values_with_filtering_slugs` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:80]
- `test_filter_attributes_if_filterable_in_dashboard` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:93]
- `test_filter_attributes_if_available_in_grid` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:109]
- `test_filter_attributes_by_global_id_list` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:125]
- `test_filter_attribute_values_by_global_id_list` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:148]
- `test_filter_attributes_in_category_invalid_category_id` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:171]
- `test_filter_attributes_in_category_object_with_given_id_does_not_exist` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:211]
- `test_filter_attributes_in_category_not_visible_in_listings_by_customer` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:248]
- `test_filter_attributes_in_category_not_visible_in_listings_by_staff_with_perm` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:292]
- `test_filter_attributes_in_category_not_in_listings_by_staff_without_manage_products` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:339]
- `test_filter_attributes_in_category_not_visible_in_listings_by_app_with_perm` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:383]
- `test_filter_attributes_in_category_not_in_listings_by_app_without_manage_products` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:430]
- `test_filter_attributes_in_category_not_published_by_customer` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:474]
- `test_filter_attributes_in_category_not_published_by_staff_with_perm` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:518]
- `test_filter_attributes_in_category_not_published_by_staff_without_manage_products` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:565]
- `test_filter_attributes_in_category_not_published_by_app_with_perm` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:609]
- `test_filter_attributes_in_category_not_published_by_app_without_manage_products` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:656]
- `test_filter_attributes_in_collection_invalid_category_id` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:700]
- `test_filter_attributes_in_collection_object_with_given_id_does_not_exist` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:743]
- `test_filter_attributes_in_collection_not_visible_in_listings_by_customer` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:783]
- `test_filter_in_collection_not_published_by_customer` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:826]
- `test_filter_in_collection_not_published_by_staff_with_perm` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:872]
- `test_filter_in_collection_not_published_by_staff_without_manage_products` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:922]
- `test_filter_in_collection_not_published_by_app_with_perm` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:969]
- `test_filter_in_collection_not_published_by_app_without_manage_products` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:1019]
- `test_filter_attributes_in_category_no_duplicates_when_shared_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:1066]
- `test_filter_attributes_in_collection_no_duplicates_when_shared_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:1139]
- `test_filter_attributes_by_page_type` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:1214]
- `test_filter_attributes_by_product_type` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:1235]
- `test_attributes_filter_by_product_type_with_empty_value` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:1258]
- `test_attributes_filter_by_product_type_with_unsupported_field` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:1265]
- `test_attributes_filter_by_non_existing_category_id` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filter.py:1278]

**`saleor/graphql/attribute/tests/queries/test_attribute_filtering_with_channels.py`**

- `attributes_for_filtering_with_channels` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filtering_with_channels.py:19]
- `test_attributes_with_filtering_without_channel` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filtering_with_channels.py:166]
- `test_products_with_filtering_with_channel_as_staff_user` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filtering_with_channels.py:199]
- `test_products_with_alternative_filtering_with_channel_as_staff_user` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filtering_with_channels.py:234]
- `test_products_with_filtering_as_anonymous_client` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filtering_with_channels.py:266]
- `test_products_with_filtering_with_not_visible_in_listings_as_staff_user` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filtering_with_channels.py:299]
- `test_products_with_filtering_with_not_visible_in_listings_as_anonymous_client` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filtering_with_channels.py:342]
- `test_products_with_filtering_with_not_published_as_staff_user` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filtering_with_channels.py:375]
- `test_products_with_filtering_with_not_published_as_anonymous_client` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filtering_with_channels.py:414]
- `test_products_with_filtering_not_existing_channel` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_filtering_with_channels.py:447]

**`saleor/graphql/attribute/tests/queries/test_attribute_pagination.py`**

- `attributes_for_pagination` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_pagination.py:20]
- `test_attributes_pagination_with_sorting` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_pagination.py:173]
- `test_attributes_pagination_with_filtering` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_pagination.py:203]
- `test_attributes_pagination_with_filtering_in_collection` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_pagination.py:220]
- `test_attributes_pagination_with_filtering_in_category` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_pagination.py:242]

**`saleor/graphql/attribute/tests/queries/test_attribute_query.py`**

- `test_get_single_attribute_by_id_as_customer` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:18]
- `test_get_single_attribute_by_slug_as_customer` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:42]
- `test_get_single_product_attribute_by_staff` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:131]
- `test_get_single_product_attribute_by_app` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:172]
- `test_query_attribute_by_invalid_id` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:213]
- `test_query_attribute_with_invalid_object_type` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:225]
- `test_get_single_product_attribute_by_staff_no_perm` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:236]
- `test_get_single_page_attribute_by_staff` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:249]
- `test_get_single_page_attribute_by_staff_no_perm` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:264]
- `test_get_single_product_attribute_with_file_value` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:275]
- `test_get_single_reference_attribute_by_staff` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:307]
- `test_get_single_numeric_attribute_by_staff` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:356]
- `test_get_single_swatch_attribute_by_staff` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:400]
- `test_get_single_reference_product_attribute_with_reference_types` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:464]
- `test_get_single_reference_variant_attribute_with_reference_types` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:499]
- `test_get_single_reference_page_attribute_with_reference_types` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:534]
- `test_get_reference_product_attribute_with_reference_types` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:567]
- `test_get_reference_variant_attribute_with_reference_types` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:602]
- `test_get_reference_page_attribute_with_reference_types` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:637]
- `test_get_reference_collection_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:670]
- `test_get_reference_category_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:699]
- `test_get_attribute_reference_product_types_with_limit` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:751]
- `test_get_attribute_reference_product_types_limit_exceeded` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:788]
- `test_get_attribute_reference_page_types_with_limit` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:825]
- `test_get_attribute_reference_page_types_invalid_limit` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:855]
- `test_attributes_query` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:929]
- `test_attributes_query_hidden_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:939]
- `test_attributes_query_hidden_attribute_as_staff_user_without_permissions` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:957]
- `test_attributes_query_hidden_attribute_as_staff_user_with_permissions` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:974]
- `test_attributes_query_ids_not_exists` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:1012]
- `test_retrieving_the_restricted_attributes_restricted` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:1035]
- `test_attributes_in_collection_query` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:1064]
- `test_attributes_with_choice_flag` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:1149]
- `test_get_attribute_by_external_reference` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:1195]
- `test_get_reference_product_attribute_with_reference_types_and_different_limits` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_query.py:1256]

**`saleor/graphql/attribute/tests/queries/test_attribute_where.py`**

- `test_attributes_filter_by_ids` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:30]
- `test_attributes_filter_by_none_as_ids` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:52]
- `test_attributes_filter_by_ids_empty_list` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:65]
- `test_attributes_filter_by_name` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:92]
- `test_attributes_filter_by_slug` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:124]
- `test_attributes_filter_by_with_choices` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:145]
- `test_attributes_filter_by_input_type` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:192]
- `test_attributes_filter_by_entity_type` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:238]
- `test_attributes_filter_by_type` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:295]
- `test_attributes_filter_by_unit` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:347]
- `test_attributes_filter_by_value_required` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:386]
- `test_attributes_filter_by_visible_in_storefront` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:414]
- `test_attributes_filter_by_filterable_in_dashboard` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:451]
- `test_attributes_filter_attributes_in_collection_not_visible_in_listings_by_customer` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:476]
- `test_attributes_filter_in_collection_not_published_by_customer` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:520]
- `test_attributes_filter_in_collection_not_published_by_staff_with_perm` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:567]
- `test_attributes_filter_in_collection_not_published_by_staff_without_manage_products` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:618]
- `test_attributes_filter_in_collection_not_published_by_app_with_perm` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:666]
- `test_attributes_filter_in_collection_not_published_by_app_without_manage_products` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:717]
- `test_attributes_filter_attributes_in_collection_invalid_collection_id` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:765]
- `test_attributes_filter_attributes_in_collection_object_with_given_id_does_not_exist` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:809]
- `test_attributes_filter_in_collection_empty_value` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:850]
- `test_attributes_filter_in_category_not_visible_in_listings_by_customer` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:899]
- `test_attributes_filter_in_category_not_visible_in_listings_by_staff_with_perm` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:944]
- `test_attributes_filter_in_category_not_in_listings_by_staff_without_manage_products` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:992]
- `test_attributes_filter_in_category_not_visible_in_listings_by_app_with_perm` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:1037]
- `test_attributes_filter_in_category_not_in_listings_by_app_without_manage_products` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:1085]
- `test_attributes_filter_in_category_not_published_by_customer` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:1130]
- `test_attributes_filter_in_category_not_published_by_staff_with_perm` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:1175]
- `test_attributes_filter_in_category_not_published_by_staff_without_manage_products` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:1223]
- `test_attributes_filter_in_category_not_published_by_app_with_perm` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:1268]
- `test_attributes_filter_in_category_not_published_by_app_without_manage_products` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:1316]
- `test_attributes_filter_in_category_invalid_category_id` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:1361]
- `test_attributes_filter_in_category_object_with_given_id_does_not_exist` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:1402]
- `test_attributes_filter_in_category_empty_value` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:1440]
- `test_attributes_filter_in_category_no_duplicates_when_shared_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:1485]
- `test_attributes_filter_in_collection_no_duplicates_when_shared_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:1558]
- `test_attributes_filter_and_where_both_used` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:1633]
- `test_attributes_filter_invalid_input` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:1722]
- `test_attributes_where_operator_invalid_input_data` (function) — [saleor/graphql/attribute/tests/queries/test_attribute_where.py:1759]
- _…and 8 more in this file_

**`saleor/graphql/attribute/tests/queries/test_attributes_sort.py`**

- `test_sort_attributes_by_slug` (function) — [saleor/graphql/attribute/tests/queries/test_attributes_sort.py:21]
- `test_sort_attributes_by_default_sorting` (function) — [saleor/graphql/attribute/tests/queries/test_attributes_sort.py:40]
- `test_attributes_of_products_are_sorted_on_variant` (function) — [saleor/graphql/attribute/tests/queries/test_attributes_sort.py:58]
- `test_attributes_of_products_are_sorted_on_product` (function) — [saleor/graphql/attribute/tests/queries/test_attributes_sort.py:119]
- `test_sort_attribute_choices_by_slug` (function) — [saleor/graphql/attribute/tests/queries/test_attributes_sort.py:200]
- `test_sort_attribute_choices_by_name` (function) — [saleor/graphql/attribute/tests/queries/test_attributes_sort.py:213]

**`saleor/graphql/attribute/tests/queries/test_selected_attribute.py`**

- `test_attribute_value_name_when_referenced_product_was_changed` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:29]
- `test_attribute_value_name_when_referenced_variant_was_changed` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:68]
- `test_attribute_value_name_when_referenced_page_was_changed` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:110]
- `test_assigned_numeric_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:167]
- `test_assigned_text_attribute_translation` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:205]
- `test_assigned_text_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:240]
- `test_assigned_plain_text_attribute_translation` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:281]
- `test_assigned_plain_text_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:322]
- `test_assigned_file_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:367]
- `test_assigned_single_page_reference_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:417]
- `test_assigned_single_product_reference_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:477]
- `test_assigned_single_product_variant_reference_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:538]
- `test_assigned_single_category_reference_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:599]
- `test_assigned_single_collection_reference_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:660]
- `test_assigned_multi_page_reference_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:721]
- `test_assigned_multi_product_reference_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:782]
- `test_applies_limit_to_multi_product_references` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:826]
- `test_assigned_multi_product_variant_reference_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:900]
- `test_applies_limit_to_multi_variant_references` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:944]
- `test_assigned_multi_category_reference_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1018]
- `test_applies_limit_to_multi_category_references` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1062]
- `test_assigned_multi_collection_reference_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1141]
- `test_applies_limit_to_multi_collection_references` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1185]
- `test_assigned_single_choice_attribute_translation` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1264]
- `test_assigned_single_choice_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1298]
- `test_assigned_multi_choice_attribute_translation` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1348]
- `test_applies_limit_to_multi_choices` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1384]
- `test_assigned_multi_choice_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1429]
- `test_assigned_swatch_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1487]
- `test_assigned_swatch_file_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1526]
- `test_assigned_swatch_attribute_translation` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1578]
- `test_assigned_boolean_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1626]
- `test_assigned_date_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1672]
- `test_assigned_datetime_attribute` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1718]
- `test_all_non_reference_attribute_type_has_own_assigned_types` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1751]
- `test_all_single_reference_attribute_type_has_own_assigned_types` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1764]
- `test_all_multi_reference_attribute_type_has_own_assigned_types` (function) — [saleor/graphql/attribute/tests/queries/test_selected_attribute.py:1773]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/attribute/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/attribute/tests/queries/test_attribute_filter.py` (1286 lines)
- `saleor/graphql/attribute/tests/queries/test_attribute_filtering_with_channels.py` (471 lines)
- `saleor/graphql/attribute/tests/queries/test_attribute_pagination.py` (261 lines)
- `saleor/graphql/attribute/tests/queries/test_attribute_query.py` (1295 lines)
- `saleor/graphql/attribute/tests/queries/test_attribute_where.py` (2142 lines)
- `saleor/graphql/attribute/tests/queries/test_attributes_sort.py` (223 lines)
- `saleor/graphql/attribute/tests/queries/test_selected_attribute.py` (1779 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....attribute.AttributeEntityType`
- `.....attribute.AttributeInputType`
- `.....attribute.AttributeType`
- `.....attribute.models.AssignedProductAttributeValue`
- `.....attribute.models.Attribute`
- `.....attribute.models.AttributeProduct`
- `.....attribute.models.AttributeValue`
- `.....attribute.models.AttributeVariant`
- `.....attribute.models.base.AttributeValue`
- `.....attribute.models.base.AttributeValueTranslation`
- `.....attribute.utils.associate_attribute_values_to_instance`
- `.....core.units.MeasurementUnits`
- `.....product.ProductTypeKind`
- `.....product.models.Category`
- `.....product.models.Collection`
- `.....product.models.Product`
- `.....product.models.ProductChannelListing`
- `.....product.models.ProductType`
- `.....tests.utils.dummy_editorjs`
- `....core.enums.MeasurementUnitsEnum`
- `....tests.utils.assert_graphql_error_with_message`
- `....tests.utils.get_graphql_content`
- `....tests.utils.get_graphql_content_from_response`
- `...enums.AttributeEntityTypeEnum`
- `...enums.AttributeInputTypeEnum`
- `...enums.AttributeTypeEnum`
- `...filters.filter_attributes_by_product_types`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `5fecb21e0f48` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
