## Purpose

`saleor/graphql/product/tests/mutations` (`saleor/graphql/product/tests/mutations`) groups 39 source file(s) exposing 326 top-level declaration(s).

## Public surface

**`saleor/graphql/product/tests/mutations/test_assign_variant_media.py`**

- `test_assign_variant_media` (function) — [saleor/graphql/product/tests/mutations/test_assign_variant_media.py:27]
- `test_assign_variant_media_second_time` (function) — [saleor/graphql/product/tests/mutations/test_assign_variant_media.py:46]
- `test_assign_variant_media_from_different_product` (function) — [saleor/graphql/product/tests/mutations/test_assign_variant_media.py:73]

**`saleor/graphql/product/tests/mutations/test_category_create.py`**

- `test_category_create_mutation` (function) — [saleor/graphql/product/tests/mutations/test_category_create.py:72]
- `test_category_create_trigger_webhook` (function) — [saleor/graphql/product/tests/mutations/test_category_create.py:140]
- `test_create_category_with_given_slug` (function) — [saleor/graphql/product/tests/mutations/test_category_create.py:209]
- `test_create_category_name_with_unicode` (function) — [saleor/graphql/product/tests/mutations/test_category_create.py:224]
- `test_category_create_mutation_without_background_image` (function) — [saleor/graphql/product/tests/mutations/test_category_create.py:240]
- `test_category_create_mutation_file_size_exceeds_limit` (function) — [saleor/graphql/product/tests/mutations/test_category_create.py:261]

**`saleor/graphql/product/tests/mutations/test_category_delete.py`**

- `test_category_delete_mutation` (function) — [saleor/graphql/product/tests/mutations/test_category_delete.py:38]
- `test_category_delete_trigger_webhook` (function) — [saleor/graphql/product/tests/mutations/test_category_delete.py:80]
- `test_delete_category_with_background_image` (function) — [saleor/graphql/product/tests/mutations/test_category_delete.py:122]
- `test_category_delete_mutation_for_categories_tree` (function) — [saleor/graphql/product/tests/mutations/test_category_delete.py:141]
- `test_category_delete_mutation_for_children_from_categories_tree` (function) — [saleor/graphql/product/tests/mutations/test_category_delete.py:173]
- `test_category_delete_removes_reference_to_product` (function) — [saleor/graphql/product/tests/mutations/test_category_delete.py:215]
- `test_category_delete_removes_reference_to_product_variant` (function) — [saleor/graphql/product/tests/mutations/test_category_delete.py:257]
- `test_category_delete_removes_reference_to_page` (function) — [saleor/graphql/product/tests/mutations/test_category_delete.py:300]

**`saleor/graphql/product/tests/mutations/test_category_update.py`**

- `test_category_update_mutation` (function) — [saleor/graphql/product/tests/mutations/test_category_update.py:65]
- `test_category_update_mutation_marks_prices_to_recalculate` (function) — [saleor/graphql/product/tests/mutations/test_category_update.py:127]
- `test_category_update_mutation_with_update_at_field` (function) — [saleor/graphql/product/tests/mutations/test_category_update.py:158]
- `test_category_update_trigger_webhook` (function) — [saleor/graphql/product/tests/mutations/test_category_update.py:199]
- `test_category_update_background_image_mutation` (function) — [saleor/graphql/product/tests/mutations/test_category_update.py:260]
- `test_category_update_mutation_invalid_background_image_content_type` (function) — [saleor/graphql/product/tests/mutations/test_category_update.py:326]
- `test_category_update_mutation_invalid_background_image` (function) — [saleor/graphql/product/tests/mutations/test_category_update.py:370]
- `test_category_update_mutation_without_background_image` (function) — [saleor/graphql/product/tests/mutations/test_category_update.py:421]
- `test_update_category_slug` (function) — [saleor/graphql/product/tests/mutations/test_category_update.py:489]
- `test_update_category_slug_exists` (function) — [saleor/graphql/product/tests/mutations/test_category_update.py:519]
- `test_update_category_slug_and_name` (function) — [saleor/graphql/product/tests/mutations/test_category_update.py:556]
- `test_update_category_mutation_remove_background_image` (function) — [saleor/graphql/product/tests/mutations/test_category_update.py:612]

**`saleor/graphql/product/tests/mutations/test_collection_add_products.py`**

- `test_add_products_to_collection` (function) — [saleor/graphql/product/tests/mutations/test_collection_add_products.py:29]
- `test_add_products_to_collection_trigger_product_updated_webhook` (function) — [saleor/graphql/product/tests/mutations/test_collection_add_products.py:59]
- `test_add_products_to_collection_on_sale_trigger_discounted_price_recalculation` (function) — [saleor/graphql/product/tests/mutations/test_collection_add_products.py:82]
- `test_add_products_to_collection_with_product_without_variants` (function) — [saleor/graphql/product/tests/mutations/test_collection_add_products.py:100]

**`saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py`**

- `test_collection_channel_listing_update_duplicated_ids_in_add_and_remove` (function) — [saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py:36]
- `test_collection_channel_listing_update_duplicated_channel_in_add` (function) — [saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py:66]
- `test_collection_channel_listing_update_duplicated_channel_in_remove` (function) — [saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py:98]
- `test_collection_channel_listing_update_with_empty_input` (function) — [saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py:125]
- `test_collection_channel_listing_update_with_empty_lists_in_input` (function) — [saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py:148]
- `test_collection_channel_listing_update_as_staff_user` (function) — [saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py:171]
- `test_collection_channel_listing_update_as_app` (function) — [saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py:227]
- `test_collection_channel_listing_update_as_customer` (function) — [saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py:282]
- `test_collection_channel_listing_update_as_anonymous` (function) — [saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py:302]
- `test_collection_channel_listing_update_add_channel` (function) — [saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py:322]
- `test_collection_channel_listing_update_unpublished` (function) — [saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py:377]
- `test_collection_channel_listing_update_update_publication_date` (function) — [saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py:411]
- `test_collection_channel_listing_update_remove_not_assigned_channel` (function) — [saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py:445]
- `test_collection_channel_listing_update_add_channel_without_publication_date` (function) — [saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py:486]
- `test_collection_channel_listing_update_publish_without_publication_date` (function) — [saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py:525]

**`saleor/graphql/product/tests/mutations/test_collection_create.py`**

- `test_create_collection` (function) — [saleor/graphql/product/tests/mutations/test_collection_create.py:64]
- `test_create_collection_trigger_product_update_webhook` (function) — [saleor/graphql/product/tests/mutations/test_collection_create.py:127]
- `test_create_collection_without_background_image` (function) — [saleor/graphql/product/tests/mutations/test_collection_create.py:162]
- `test_create_collection_with_given_slug` (function) — [saleor/graphql/product/tests/mutations/test_collection_create.py:187]
- `test_create_collection_name_with_unicode` (function) — [saleor/graphql/product/tests/mutations/test_collection_create.py:202]
- `test_create_collection_file_size_exceeds_limit` (function) — [saleor/graphql/product/tests/mutations/test_collection_create.py:218]

**`saleor/graphql/product/tests/mutations/test_collection_delete.py`**

- `test_delete_collection` (function) — [saleor/graphql/product/tests/mutations/test_collection_delete.py:32]
- `test_delete_collection_with_background_image` (function) — [saleor/graphql/product/tests/mutations/test_collection_delete.py:63]
- `test_delete_collection_trigger_product_updated_webhook` (function) — [saleor/graphql/product/tests/mutations/test_collection_delete.py:98]
- `test_collection_delete_removes_reference_to_product` (function) — [saleor/graphql/product/tests/mutations/test_collection_delete.py:120]
- `test_collection_delete_removes_reference_to_product_variant` (function) — [saleor/graphql/product/tests/mutations/test_collection_delete.py:162]
- `test_collection_delete_removes_reference_to_page` (function) — [saleor/graphql/product/tests/mutations/test_collection_delete.py:205]

**`saleor/graphql/product/tests/mutations/test_collection_remove_products.py`**

- `test_remove_products_from_collection` (function) — [saleor/graphql/product/tests/mutations/test_collection_remove_products.py:24]
- `test_remove_products_from_collection_trigger_product_updated_webhook` (function) — [saleor/graphql/product/tests/mutations/test_collection_remove_products.py:54]

**`saleor/graphql/product/tests/mutations/test_collection_update.py`**

- `test_update_collection` (function) — [saleor/graphql/product/tests/mutations/test_collection_update.py:20]
- `test_update_collection_metadata_marks_prices_to_recalculate` (function) — [saleor/graphql/product/tests/mutations/test_collection_update.py:95]
- `test_update_collection_with_background_image` (function) — [saleor/graphql/product/tests/mutations/test_collection_update.py:179]
- `test_update_collection_invalid_background_image_content_type` (function) — [saleor/graphql/product/tests/mutations/test_collection_update.py:236]
- `test_update_collection_invalid_background_image` (function) — [saleor/graphql/product/tests/mutations/test_collection_update.py:282]
- `test_update_collection_slug` (function) — [saleor/graphql/product/tests/mutations/test_collection_update.py:365]
- `test_update_collection_slug_exists` (function) — [saleor/graphql/product/tests/mutations/test_collection_update.py:395]
- `test_update_collection_slug_and_name` (function) — [saleor/graphql/product/tests/mutations/test_collection_update.py:433]
- `test_update_collection_mutation_remove_background_image` (function) — [saleor/graphql/product/tests/mutations/test_collection_update.py:489]

**`saleor/graphql/product/tests/mutations/test_product_bulk_create.py`**

- `test_product_bulk_create_with_base_data` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:199]
- `test_product_bulk_create_with_description_as_json_object_does_not_crash` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:273]
- `test_product_bulk_create_with_base_data_and_collections` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:336]
- `test_product_bulk_create_with_no_slug_and_name_with_unslugify_characters` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:402]
- `test_product_bulk_create_send_product_created_webhook` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:449]
- `test_product_bulk_create_with_same_name_and_no_slug` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:508]
- `test_product_bulk_create_with_invalid_attributes` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:563]
- `test_product_bulk_create_without_value_required_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:623]
- `test_product_bulk_create_with_media` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:679]
- `test_product_bulk_create_with_media_invalid_extension` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:790]
- `test_product_bulk_create_with_media_file_size_exceeds_limit` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:886]
- `test_product_bulk_create_with_media_invalid_media_type` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:946]
- `test_product_bulk_create_with_media_image_with_invalid_exif` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:1041]
- `open_image_side_effect` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:1062]
- `test_product_bulk_create_with_media_with_media_url` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:1118]
- `test_product_bulk_create_with_media_with_media_url_invalid_provider` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:1219]
- `test_product_bulk_create_with_media_url_character_limit` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:1278]
- `test_product_bulk_create_with_media_with_media_url_invalid_image_type` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:1333]
- `test_product_bulk_create_with_media_invalid_image_file_fetch_only_header` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:1396]
- `test_product_bulk_create_with_media_image_file_is_fetched_only_once` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:1454]
- `test_product_bulk_create_with_no_extension_media_url` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:1513]
- `test_product_bulk_create_with_attributes` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:1562]
- `test_product_bulk_create_with_single_reference_attributes` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:1664]
- `test_product_bulk_create_with_reference_attributes_and_reference_types_defined` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:1752]
- `test_product_bulk_create_with_reference_attributes_refs_not_in_available_choices` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:1876]
- `test_product_bulk_create_with_attributes_using_external_refs` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:1970]
- `test_product_bulk_create_with_attributes_and_create_new_value_with_external_ref` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:2051]
- `test_product_bulk_create_return_error_when_attribute_id_and_external_ref_provided` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:2130]
- `test_product_bulk_create_with_meta_data` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:2191]
- `test_product_bulk_create_with_channel_listings` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:2260]
- `test_product_bulk_create_with_variants` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:2341]
- `test_product_bulk_create_with_variants_and_attributes_by_external_reference` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:2515]
- `test_product_bulk_create_with_variants_with_duplicated_sku` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:2668]
- `test_product_bulk_create_with_variants_send_product_variant_created_event` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:2763]
- `test_product_bulk_create_with_variants_and_stocks` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:2871]
- `test_product_bulk_create_with_variants_and_invalid_stock` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:2983]
- `test_product_bulk_create_with_variants_and_channel_listings` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:3080]
- `test_product_bulk_create_with_variants_and_channel_listings_with_wrong_price` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:3216]
- `test_product_bulk_create_with_collections_and_invalid_product_data` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:3313]
- `test_product_bulk_create_with_media_incorrect_alt` (function) — [saleor/graphql/product/tests/mutations/test_product_bulk_create.py:3360]
- _…and 3 more in this file_

**`saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py`**

- `test_product_channel_listing_update_duplicated_ids_in_add_and_remove` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:66]
- `test_product_channel_listing_update_duplicated_channel_in_add` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:96]
- `test_product_channel_listing_update_duplicated_channel_in_remove` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:128]
- `test_product_channel_listing_update_with_empty_input` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:155]
- `test_product_channel_listing_update_with_empty_lists_in_input` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:178]
- `test_product_channel_listing_update_as_staff_user` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:201]
- `test_product_channel_listing_update_trigger_webhook_product_updated` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:275]
- `test_product_channel_listing_update_as_app` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:319]
- `test_product_channel_listing_update_as_customer` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:379]
- `test_product_channel_listing_update_as_anonymous` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:399]
- `test_product_channel_listing_update_add_channel` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:417]
- `test_product_channel_listing_update_add_channel_without_publication_date` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:472]
- `test_product_channel_listing_update_unpublished` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:508]
- `test_product_channel_listing_update_publish_without_publication_date` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:548]
- `test_product_channel_listing_update_remove_publication_date` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:581]
- `test_product_channel_listing_update_visible_in_listings` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:617]
- `test_product_channel_listing_update_update_publication_data` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:654]
- `test_product_channel_listing_update_update_is_available_for_purchase_false` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:701]
- `test_product_channel_listing_update_update_is_available_for_purchase_without_date` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:738]
- `test_product_channel_listing_update_update_is_available_for_purchase_past_date` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:778]
- `test_product_channel_listing_update_update_is_available_for_purchase_future_date` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:823]
- `test_product_channel_listing_update_update_is_available_for_purchase_false_and_date` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:870]
- `test_product_channel_listing_update_remove_channel` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:909]
- `test_product_channel_listing_update_remove_channel_dont_remove_checkout_lines` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:946]
- `test_product_channel_listing_update_remove_not_assigned_channel` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:984]
- `test_product_channel_listing_update_publish_product_without_category` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:1013]
- `test_product_channel_listing_update_available_for_purchase_product_without_category` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:1050]
- `test_product_channel_listing_add_variant_as_staff_user` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:1087]
- `test_product_channel_listing_add_variant_as_app` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:1132]
- `test_product_channel_listing_remove_variant_as_staff_user` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:1178]
- `test_product_channel_listing_remove_variant_is_None_as_staff_user` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:1213]
- `test_product_channel_listing_remove_variant_as_app` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:1245]
- `test_product_channel_listing_remove_variant_is_None_as_app` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:1280]
- `test_product_channel_listing_remove_variant_do_not_removes_checkout_lines` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:1312]
- `test_product_channel_listing_add_variant_duplicated_ids_in_add_and_remove` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:1361]
- `test_product_channel_listing_add_variant_with_existing_channel_listing` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:1400]
- `test_product_channel_listing_remove_last_variant_channel_listing` (function) — [saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py:1437]

**`saleor/graphql/product/tests/mutations/test_product_create.py`**

- `test_create_product` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:190]
- `test_create_product_without_slug_and_not_allowed_characters_for_slug_in_name` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:297]
- `test_create_second_product_without_slug_and_not_allowed_characters_for_slug_in_name` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:323]
- `test_create_product_use_tax_class_from_product_type` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:350]
- `test_create_product_description_plaintext` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:380]
- `test_create_product_with_using_attribute_external_ref` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:429]
- `test_create_product_with_using_attribute_id_and_external_ref` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:504]
- `test_create_product_with_using_attribute_and_value_external_ref` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:550]
- `test_create_product_with_rich_text_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:625]
- `test_create_product_no_value_for_rich_text_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:709]
- `test_create_product_with_plain_text_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:762]
- `test_create_product_no_value_for_plain_text_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:847]
- `test_create_product_with_date_time_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:905]
- `test_create_product_with_date_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:976]
- `test_create_product_no_value_for_date_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1044]
- `test_create_product_with_boolean_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1094]
- `test_create_product_no_value_for_boolean_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1161]
- `test_create_product_no_slug_in_input` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1212]
- `test_create_product_no_category_id` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1247]
- `test_create_product_with_negative_weight` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1278]
- `test_create_product_with_unicode_in_slug_and_name` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1309]
- `test_create_product_invalid_product_attributes` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1342]
- `test_create_product_without_variants` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1467]
- `test_product_create_without_product_type` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1496]
- `test_product_create_with_collections_webhook` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1526]
- `assert_product_has_collections` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1560]
- `test_product_create_with_invalid_json_description` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1586]
- `test_create_product_with_rating` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1615]
- `test_create_product_with_file_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1650]
- `test_create_product_with_page_reference_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1736]
- `test_create_product_with_page_reference_attribute_and_reference_types` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1816]
- `test_create_product_with_product_reference_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1897]
- `test_create_product_with_product_reference_attribute_and_reference_types` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:1977]
- `test_create_product_with_variant_reference_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:2060]
- `test_create_product_with_variant_reference_attribute_and_reference_types` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:2144]
- `test_create_product_with_category_reference_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:2231]
- `test_create_product_with_collection_reference_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:2312]
- `test_create_product_with_single_reference_attributes` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:2396]
- `test_create_product_with_product_reference_attribute_values_saved_in_order` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:2537]
- `test_create_product_with_page_reference_attribute_and_invalid_product_one` (function) — [saleor/graphql/product/tests/mutations/test_product_create.py:2629]
- _…and 19 more in this file_

**`saleor/graphql/product/tests/mutations/test_product_delete.py`**

- `test_delete_product` (function) — [saleor/graphql/product/tests/mutations/test_product_delete.py:39]
- `test_delete_product_with_image` (function) — [saleor/graphql/product/tests/mutations/test_product_delete.py:62]
- `test_delete_product_trigger_webhook` (function) — [saleor/graphql/product/tests/mutations/test_product_delete.py:110]
- `test_delete_product_with_file_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_delete.py:151]
- `test_delete_product_removes_checkout_lines` (function) — [saleor/graphql/product/tests/mutations/test_product_delete.py:182]
- `test_delete_product_variant_in_draft_order` (function) — [saleor/graphql/product/tests/mutations/test_product_delete.py:214]
- `test_product_delete_removes_reference_to_product` (function) — [saleor/graphql/product/tests/mutations/test_product_delete.py:305]
- `test_product_delete_removes_reference_to_product_variant` (function) — [saleor/graphql/product/tests/mutations/test_product_delete.py:347]
- `test_product_delete_removes_reference_to_page` (function) — [saleor/graphql/product/tests/mutations/test_product_delete.py:386]
- `test_delete_product_by_external_reference` (function) — [saleor/graphql/product/tests/mutations/test_product_delete.py:443]
- `test_delete_product_by_both_id_and_external_reference` (function) — [saleor/graphql/product/tests/mutations/test_product_delete.py:473]
- `test_delete_product_by_external_reference_not_existing` (function) — [saleor/graphql/product/tests/mutations/test_product_delete.py:494]

**`saleor/graphql/product/tests/mutations/test_product_media_create.py`**

- `test_product_media_create_mutation` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:50]
- `test_product_media_create_mutation_file_size_exceeds_limit` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:89]
- `test_product_media_create_mutation_without_file` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:118]
- `test_product_media_create_mutation_with_media_url` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:144]
- `test_product_media_create_mutation_without_url_or_image` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:184]
- `test_product_media_create_mutation_with_both_url_and_image` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:209]
- `test_product_media_create_mutation_with_unknown_url` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:238]
- `test_invalid_product_media_create_mutation` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:267]
- `test_product_media_create_mutation_invalid_image_file_fetch_only_header` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:308]
- `test_product_media_create_mutation_valid_image_file_is_fetched_once` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:359]
- `test_product_media_create_mutation_with_no_extension_media_url` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:404]
- `test_product_media_create_mutation_alt_character_limit` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:440]
- `test_product_media_create_mutation_media_url_character_limit` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:472]
- `test_product_media_create_when_alt_is_null` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:500]
- `test_product_media_create_with_media_url_when_alt_is_null` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:528]
- `test_product_media_create_mutation_request_exception` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:574]
- `test_product_media_create_mutation_with_empty_product_id` (function) — [saleor/graphql/product/tests/mutations/test_product_media_create.py:605]

**`saleor/graphql/product/tests/mutations/test_product_media_delete.py`**

- `test_product_media_delete` (function) — [saleor/graphql/product/tests/mutations/test_product_media_delete.py:12]

**`saleor/graphql/product/tests/mutations/test_product_media_reorder.py`**

- `test_reorder_media` (function) — [saleor/graphql/product/tests/mutations/test_product_media_reorder.py:28]
- `test_reorder_media_not_enough_ids` (function) — [saleor/graphql/product/tests/mutations/test_product_media_reorder.py:60]
- `test_reorder_not_existing_media` (function) — [saleor/graphql/product/tests/mutations/test_product_media_reorder.py:94]
- `delete_media` (function) — [saleor/graphql/product/tests/mutations/test_product_media_reorder.py:108]

**`saleor/graphql/product/tests/mutations/test_product_media_update.py`**

- `test_product_image_update_mutation` (function) — [saleor/graphql/product/tests/mutations/test_product_media_update.py:25]
- `test_product_image_update_mutation_alt_over_char_limit` (function) — [saleor/graphql/product/tests/mutations/test_product_media_update.py:58]

**`saleor/graphql/product/tests/mutations/test_product_type_create.py`**

- `test_product_type_create_mutation` (function) — [saleor/graphql/product/tests/mutations/test_product_type_create.py:91]
- `test_product_type_create_trigger_webhook` (function) — [saleor/graphql/product/tests/mutations/test_product_type_create.py:155]
- `test_product_type_create_mutation_optional_kind` (function) — [saleor/graphql/product/tests/mutations/test_product_type_create.py:211]
- `test_create_gift_card_product_type` (function) — [saleor/graphql/product/tests/mutations/test_product_type_create.py:227]
- `test_create_product_type_with_rich_text_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_type_create.py:285]
- `test_create_product_type_with_plain_text_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_type_create.py:345]
- `test_create_product_type_with_date_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_type_create.py:385]
- `test_create_product_type_with_boolean_attribute` (function) — [saleor/graphql/product/tests/mutations/test_product_type_create.py:432]
- `test_create_product_type_with_given_slug` (function) — [saleor/graphql/product/tests/mutations/test_product_type_create.py:479]
- `test_create_product_type_with_unicode_in_name` (function) — [saleor/graphql/product/tests/mutations/test_product_type_create.py:501]
- `test_create_product_type_create_with_negative_weight` (function) — [saleor/graphql/product/tests/mutations/test_product_type_create.py:522]
- `test_product_type_create_mutation_not_valid_attributes` (function) — [saleor/graphql/product/tests/mutations/test_product_type_create.py:542]

**`saleor/graphql/product/tests/mutations/test_product_type_delete.py`**

- `test_product_type_delete_mutation` (function) — [saleor/graphql/product/tests/mutations/test_product_type_delete.py:30]
- `test_product_type_delete_trigger_webhook` (function) — [saleor/graphql/product/tests/mutations/test_product_type_delete.py:48]
- `test_product_type_delete_mutation_deletes_also_images` (function) — [saleor/graphql/product/tests/mutations/test_product_type_delete.py:99]
- `test_product_type_delete_with_file_attributes` (function) — [saleor/graphql/product/tests/mutations/test_product_type_delete.py:124]
- `test_product_type_delete_mutation_variants_in_draft_order` (function) — [saleor/graphql/product/tests/mutations/test_product_type_delete.py:158]

**`saleor/graphql/product/tests/mutations/test_product_type_update.py`**

- `test_product_type_update_trigger_webhook` (function) — [saleor/graphql/product/tests/mutations/test_product_type_update.py:64]
- `test_product_type_update_mutation` (function) — [saleor/graphql/product/tests/mutations/test_product_type_update.py:119]
- `test_product_type_update_mutation_not_valid_attributes` (function) — [saleor/graphql/product/tests/mutations/test_product_type_update.py:164]
- `test_update_product_type_slug` (function) — [saleor/graphql/product/tests/mutations/test_product_type_update.py:242]
- `test_update_product_type_slug_exists` (function) — [saleor/graphql/product/tests/mutations/test_product_type_update.py:274]
- `test_update_product_type_slug_and_name` (function) — [saleor/graphql/product/tests/mutations/test_product_type_update.py:311]
- `test_update_product_type_with_negative_weight` (function) — [saleor/graphql/product/tests/mutations/test_product_type_update.py:367]
- `test_update_product_type_kind` (function) — [saleor/graphql/product/tests/mutations/test_product_type_update.py:405]
- `test_update_product_type_kind_omitted` (function) — [saleor/graphql/product/tests/mutations/test_product_type_update.py:443]
- `test_product_type_update_changes_variant_name` (function) — [saleor/graphql/product/tests/mutations/test_product_type_update.py:482]

**`saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py`**

- `test_product_variant_bulk_update` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:209]
- `test_product_variant_bulk_create_stock_thread_race` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:284]
- `add_stock_before_save` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:302]
- `test_product_variant_bulk_update_stocks` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:362]
- `test_product_variant_bulk_update_create_already_existing_stock` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:430]
- `test_product_variant_bulk_update_create_already_existing_channel_listing` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:477]
- `test_product_variant_bulk_update_create_already_existing_channel_listing_error_policy` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:543]
- `test_product_variant_bulk_update_create_duplicate_and_invalid_channel_listing_error_paths` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:615]
- `test_product_variant_bulk_update_and_remove_stock` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:686]
- `test_product_variant_bulk_update_and_remove_stock_when_stock_not_exists` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:726]
- `test_product_variant_bulk_update_stocks_with_invalid_warehouse` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:767]
- `test_product_variant_bulk_update_channel_listings_input` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:814]
- `test_product_variant_bulk_update_and_remove_channel_listings` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:901]
- `test_product_variant_bulk_update_channel_listings_with_invalid_price` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:948]
- `test_product_variant_bulk_update_with_already_existing_sku` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:1003]
- `test_product_variant_bulk_update_when_variant_not_exists` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:1035]
- `test_product_variant_bulk_update_attributes` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:1068]
- `test_product_variant_bulk_update_with_ref_attributes_and_reference_types_defined` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:1129]
- `test_product_variant_bulk_update_with_ref_attributes_refs_not_in_available_choices` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:1241]
- `test_product_variant_bulk_update_attributes_by_external_reference` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:1328]
- `test_generate_pre_save_payloads` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:1391]
- `test_product_variant_bulk_update_channel_listings_input_with_prior_price` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py:1437]

**`saleor/graphql/product/tests/mutations/test_product_variant_delete.py`**

- `test_delete_variant_by_sku` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_delete.py:27]
- `test_delete_variant` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_delete.py:72]
- `test_delete_variant_remove_checkout_lines` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_delete.py:99]
- `test_delete_variant_with_image` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_delete.py:125]
- `test_delete_variant_in_draft_order` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_delete.py:156]
- `test_delete_default_variant` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_delete.py:254]
- `test_delete_not_default_variant_left_default_variant_unchanged` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_delete.py:293]
- `test_delete_default_all_product_variant_left_product_default_variant_unset` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_delete.py:332]
- `test_delete_variant_delete_product_channel_listing_without_available_channel` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_delete.py:370]
- `test_delete_variant_delete_product_channel_listing_not_deleted` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_delete.py:410]
- `test_delete_variant_by_external_reference` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_delete.py:464]
- `test_delete_product_by_both_id_and_external_reference` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_delete.py:499]
- `test_delete_product_by_external_reference_not_existing` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_delete.py:520]

**`saleor/graphql/product/tests/mutations/test_product_variant_preorder_deactivate.py`**

- `test_product_variant_deactivate_preorder` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_preorder_deactivate.py:36]
- `test_product_variant_deactivate_preorder_non_preorder_variant` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_preorder_deactivate.py:65]
- `test_product_variant_deactivate_preorder_cannot_deactivate` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_preorder_deactivate.py:89]
- `test_product_variant_deactivate_preorder_as_customer` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_preorder_deactivate.py:115]
- `test_product_variant_deactivate_preorder_as_anonymous` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_preorder_deactivate.py:130]
- `test_product_variant_deactivate_preorder_as_app_with_permission` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_preorder_deactivate.py:145]
- `test_product_variant_deactivate_preorder_as_app` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_preorder_deactivate.py:164]

**`saleor/graphql/product/tests/mutations/test_product_variant_set_default.py`**

- `test_product_variant_set_default` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_set_default.py:23]
- `test_product_variant_set_default_invalid_id` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_set_default.py:51]
- `test_product_variant_set_default_not_products_variant` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_set_default.py:78]

**`saleor/graphql/product/tests/mutations/test_product_variant_stocks_create.py`**

- `test_variant_stocks_create` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_stocks_create.py:35]

**`saleor/graphql/product/tests/mutations/test_product_variant_stocks_delete.py`**

- `test_product_variant_stocks_delete_mutation` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_stocks_delete.py:34]

**`saleor/graphql/product/tests/mutations/test_product_variant_stocks_update.py`**

- `test_product_variant_stocks_update` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_stocks_update.py:39]

**`saleor/graphql/product/tests/mutations/test_product_variant_update.py`**

- `test_product_variant_update_with_new_attributes` (function) — [saleor/graphql/product/tests/mutations/test_product_variant_update.py:22]

**`saleor/graphql/product/tests/mutations/test_product_variants_reorder.py`**

- `test_reorder_variants` (function) — [saleor/graphql/product/tests/mutations/test_product_variants_reorder.py:21]
- `test_reorder_variants_invalid_variants` (function) — [saleor/graphql/product/tests/mutations/test_product_variants_reorder.py:52]

**`saleor/graphql/product/tests/mutations/test_unassign_variant_media.py`**

- `test_unassign_variant_media_image` (function) — [saleor/graphql/product/tests/mutations/test_unassign_variant_media.py:21]
- `test_unassign_not_assigned_variant_media_image` (function) — [saleor/graphql/product/tests/mutations/test_unassign_variant_media.py:42]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/product/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/product/tests/mutations/cassettes/test_product_bulk_create/test_product_bulk_create_with_media_image_file_is_fetched_only_once.yaml` (134 lines)
- `saleor/graphql/product/tests/mutations/cassettes/test_product_bulk_create/test_product_bulk_create_with_media_with_media_url.yaml` (102 lines)
- `saleor/graphql/product/tests/mutations/cassettes/test_product_media_create/test_product_media_create_mutation_valid_image_file_is_fetched_once.yaml` (134 lines)
- `saleor/graphql/product/tests/mutations/cassettes/test_product_media_create/test_product_media_create_mutation_with_media_url.yaml` (52 lines)
- `saleor/graphql/product/tests/mutations/test_assign_variant_media.py` (95 lines)
- `saleor/graphql/product/tests/mutations/test_category_create.py` (288 lines)
- `saleor/graphql/product/tests/mutations/test_category_delete.py` (339 lines)
- `saleor/graphql/product/tests/mutations/test_category_update.py` (646 lines)
- `saleor/graphql/product/tests/mutations/test_collection_add_products.py` (121 lines)
- `saleor/graphql/product/tests/mutations/test_collection_channel_listing_update.py` (555 lines)
- `saleor/graphql/product/tests/mutations/test_collection_create.py` (245 lines)
- `saleor/graphql/product/tests/mutations/test_collection_delete.py` (244 lines)
- `saleor/graphql/product/tests/mutations/test_collection_remove_products.py` (75 lines)
- `saleor/graphql/product/tests/mutations/test_collection_update.py` (523 lines)
- `saleor/graphql/product/tests/mutations/test_product_bulk_create.py` (3580 lines)
- `saleor/graphql/product/tests/mutations/test_product_channel_listing_update.py` (1471 lines)
- `saleor/graphql/product/tests/mutations/test_product_create.py` (3829 lines)
- `saleor/graphql/product/tests/mutations/test_product_delete.py` (510 lines)
- `saleor/graphql/product/tests/mutations/test_product_media_create.py` (626 lines)
- `saleor/graphql/product/tests/mutations/test_product_media_delete.py` (52 lines)
- `saleor/graphql/product/tests/mutations/test_product_media_reorder.py` (125 lines)
- `saleor/graphql/product/tests/mutations/test_product_media_update.py` (87 lines)
- `saleor/graphql/product/tests/mutations/test_product_type_create.py` (615 lines)
- `saleor/graphql/product/tests/mutations/test_product_type_delete.py` (223 lines)
- `saleor/graphql/product/tests/mutations/test_product_type_update.py` (533 lines)
- `saleor/graphql/product/tests/mutations/test_product_update.py` (86 lines)
- `saleor/graphql/product/tests/mutations/test_product_variant_bulk_create.py` (75 lines)
- `saleor/graphql/product/tests/mutations/test_product_variant_bulk_update.py` (1503 lines)
- `saleor/graphql/product/tests/mutations/test_product_variant_create.py` (82 lines)
- `saleor/graphql/product/tests/mutations/test_product_variant_delete.py` (536 lines)
- `saleor/graphql/product/tests/mutations/test_product_variant_preorder_deactivate.py` (176 lines)
- `saleor/graphql/product/tests/mutations/test_product_variant_set_default.py` (105 lines)
- `saleor/graphql/product/tests/mutations/test_product_variant_stocks_create.py` (69 lines)
- `saleor/graphql/product/tests/mutations/test_product_variant_stocks_delete.py` (67 lines)
- `saleor/graphql/product/tests/mutations/test_product_variant_stocks_update.py` (68 lines)
- `saleor/graphql/product/tests/mutations/test_product_variant_update.py` (68 lines)
- `saleor/graphql/product/tests/mutations/test_product_variants_reorder.py` (80 lines)
- `saleor/graphql/product/tests/mutations/test_unassign_variant_media.py` (58 lines)

## Interactions

- Imports from: `saleor/graphql/product/bulk_mutations`, `saleor/core/utils`, `saleor/core`, `saleor/warehouse`, `saleor/graphql/product/mutations/product`, `saleor/core/cleaners`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....attribute.AttributeInputType`
- `.....attribute.AttributeType`
- `.....attribute.models.AttributeValue`
- `.....attribute.utils.associate_attribute_values_to_instance`
- `.....checkout.fetch.fetch_checkout_info`
- `.....checkout.tests.utils.add_variant_to_checkout`
- `.....core.exceptions.PreorderAllocationError`
- `.....core.exceptions.UnsupportedMediaProviderException`
- `.....core.taxes.TaxType`
- `.....core.utils.json_serializer.CustomJsonEncoder`
- `.....discount.models.PromotionRule`
- `.....discount.utils.promotion.get_active_catalogue_promotion_rules`
- `.....graphql.core.enums.AttributeErrorCode`
- `.....graphql.core.enums.ErrorPolicyEnum`
- `.....graphql.tests.utils.get_graphql_content`
- `.....graphql.tests.utils.get_multipart_request_body`
- `.....graphql.webhook.subscription_payload.get_pre_save_payload_key`
- `.....order.OrderEvents`
- `.....order.OrderStatus`
- `.....order.models.OrderEvent`
- `.....order.models.OrderLine`
- `.....plugins.manager.PluginsManager`
- `.....plugins.manager.get_plugins_manager`
- `.....product.MEDIA_URL_CHAR_LIMIT`
- `.....product.ProductMediaTypes`
- `.....product.error_codes.CollectionErrorCode`
- `.....product.error_codes.ProductBulkCreateErrorCode`
- `.....product.error_codes.ProductErrorCode`
- `.....product.error_codes.ProductVariantBulkErrorCode`
- `.....product.models.Category`
- `.....product.models.Collection`
- `.....product.models.Product`
- `.....product.models.ProductChannelListing`
- `.....product.models.ProductMedia`
- `.....product.models.ProductType`
- `.....product.models.ProductVariant`
- `.....product.models.ProductVariantChannelListing`
- `.....product.tests.utils.create_image`
- `.....product.tests.utils.create_zip_file_with_image_ext`
- `.....product.utils.costs.get_product_costs_data`
- `.....tests.race_condition`
- `.....tests.utils.dummy_editorjs`
- `.....thumbnail.models.Thumbnail`
- `.....warehouse.WarehouseClickAndCollectOption`
- `.....warehouse.error_codes.StockErrorCode`
- `.....warehouse.models.Allocation`
- `.....warehouse.models.Stock`
- `.....warehouse.models.Warehouse`
- `.....webhook.event_types.WebhookEventAsyncType`
- `.....webhook.models.Webhook`
- `.....webhook.payloads.generate_meta`
- `.....webhook.payloads.generate_requestor`
- `....attribute.utils.type_handlers.AttributeInputErrors`
- `....core.enums.ErrorPolicyEnum`
- `....core.enums.WeightUnitsEnum`
- `....core.utils.snake_to_camel_case`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `...bulk_mutations.ProductVariantStocksUpdate`
- `...enums.ProductTypeKindEnum`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `be09215caf72` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
