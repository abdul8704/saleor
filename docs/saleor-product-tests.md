## Purpose

`saleor/product/tests` (`saleor/product/tests`) groups 17 source file(s) exposing 142 top-level declaration(s).

## Public surface

**`saleor/product/tests/test_category.py`**

- `test_collect_categories_tree_products` (function) — [saleor/product/tests/test_category.py:9]
- `test_delete_categories` (function) — [saleor/product/tests/test_category.py:22]
- `test_delete_categories_trigger_product_updated_webhook` (function) — [saleor/product/tests/test_category.py:49]

**`saleor/product/tests/test_collections_availability.py`**

- `test_visible_to_customer_user` (function) — [saleor/product/tests/test_collections_availability.py:4]
- `test_visible_to_customer_user_without_channel_slug` (function) — [saleor/product/tests/test_collections_availability.py:18]
- `test_visible_to_staff_user` (function) — [saleor/product/tests/test_collections_availability.py:38]
- `test_visible_to_staff_user_with_channel` (function) — [saleor/product/tests/test_collections_availability.py:57]

**`saleor/product/tests/test_fetch_variants_for_promotion_rules.py`**

- `test_fetch_variants_for_promotion_rules_discount` (function) — [saleor/product/tests/test_fetch_variants_for_promotion_rules.py:12]
- `test_fetch_variants_for_promotion_rules_empty_catalogue_predicate` (function) — [saleor/product/tests/test_fetch_variants_for_promotion_rules.py:76]
- `test_fetch_variants_for_promotion_rules_no_applicable_variants` (function) — [saleor/product/tests/test_fetch_variants_for_promotion_rules.py:99]
- `test_fetch_variants_for_promotion_rules_relation_already_exist` (function) — [saleor/product/tests/test_fetch_variants_for_promotion_rules.py:126]
- `test_fetch_variants_for_promotion_rules_discount_race_condition` (function) — [saleor/product/tests/test_fetch_variants_for_promotion_rules.py:142]

**`saleor/product/tests/test_generate_and_set_variant_name.py`**

- `test_generate_and_set_variant_name_different_attributes` (function) — [saleor/product/tests/test_generate_and_set_variant_name.py:11]
- `test_generate_and_set_variant_name_only_variant_selection_attributes` (function) — [saleor/product/tests/test_generate_and_set_variant_name.py:56]
- `test_generate_and_set_variant_name_only_not_variant_selection_attributes` (function) — [saleor/product/tests/test_generate_and_set_variant_name.py:104]
- `test_generate_name_from_values_empty` (function) — [saleor/product/tests/test_generate_and_set_variant_name.py:151]
- `test_product_type_update_changes_variant_name` (function) — [saleor/product/tests/test_generate_and_set_variant_name.py:159]
- `test_only_not_variant_selection_attr_left_variant_name_change_to_sku` (function) — [saleor/product/tests/test_generate_and_set_variant_name.py:172]
- `test_update_variants_changed_does_nothing_with_no_attributes` (function) — [saleor/product/tests/test_generate_and_set_variant_name.py:188]
- `test_only_not_variant_selection_attr_left_variant_name_change_to_global_id` (function) — [saleor/product/tests/test_generate_and_set_variant_name.py:196]

**`saleor/product/tests/test_get_variant_selection_attributes.py`**

- `test_get_variant_selection_attributes` (function) — [saleor/product/tests/test_get_variant_selection_attributes.py:5]

**`saleor/product/tests/test_managers.py`**

- `test_available_quantity_with_no_allocations` (function) — [saleor/product/tests/test_managers.py:4]
- `test_available_quantity_with_allocations` (function) — [saleor/product/tests/test_managers.py:15]
- `test_available_quantity_with_allocations_quantity_zero` (function) — [saleor/product/tests/test_managers.py:30]
- `test_available_quantity_with_insufficient_stock` (function) — [saleor/product/tests/test_managers.py:42]
- `test_available_quantity_with_no_stock` (function) — [saleor/product/tests/test_managers.py:55]

**`saleor/product/tests/test_product_availability.py`**

- `test_availability` (function) — [saleor/product/tests/test_product_availability.py:14]
- `test_availability_with_all_variant_channel_listings` (function) — [saleor/product/tests/test_product_availability.py:57]
- `test_availability_no_prices` (function) — [saleor/product/tests/test_product_availability.py:87]
- `test_availability_with_missing_variant_channel_listings` (function) — [saleor/product/tests/test_product_availability.py:123]
- `test_availability_without_variant_channel_listings` (function) — [saleor/product/tests/test_product_availability.py:150]
- `test_available_products_only_published` (function) — [saleor/product/tests/test_product_availability.py:173]
- `test_available_products_only_available` (function) — [saleor/product/tests/test_product_availability.py:186]
- `test_available_products_available_from_yesterday` (function) — [saleor/product/tests/test_product_availability.py:200]
- `test_available_products_available_without_channel_listings` (function) — [saleor/product/tests/test_product_availability.py:214]
- `test_available_products_available_with_many_channels` (function) — [saleor/product/tests/test_product_availability.py:221]
- `test_product_is_visible_from_today` (function) — [saleor/product/tests/test_product_availability.py:235]
- `test_available_products_with_variants` (function) — [saleor/product/tests/test_product_availability.py:242]
- `test_available_products_with_variants_in_many_channels_usd` (function) — [saleor/product/tests/test_product_availability.py:250]
- `test_available_products_with_variants_in_many_channels_pln` (function) — [saleor/product/tests/test_product_availability.py:257]
- `test_visible_to_customer_user` (function) — [saleor/product/tests/test_product_availability.py:264]
- `test_visible_to_customer_user_without_channel` (function) — [saleor/product/tests/test_product_availability.py:278]
- `test_visible_to_customer_user_with_not_existing_channel_slug_passed` (function) — [saleor/product/tests/test_product_availability.py:298]
- `test_visible_to_staff_user` (function) — [saleor/product/tests/test_product_availability.py:318]
- `test_visible_to_staff_user_with_channel` (function) — [saleor/product/tests/test_product_availability.py:337]
- `test_visible_to_staff_user_with_not_existing_channel_slug_passed` (function) — [saleor/product/tests/test_product_availability.py:358]
- `test_filter_not_published_product_is_unpublished` (function) — [saleor/product/tests/test_product_availability.py:377]
- `test_filter_not_published_product_published_tomorrow` (function) — [saleor/product/tests/test_product_availability.py:386]
- `test_filter_not_published_product_not_published_tomorrow` (function) — [saleor/product/tests/test_product_availability.py:397]
- `test_filter_not_published_product_is_published` (function) — [saleor/product/tests/test_product_availability.py:408]
- `test_filter_not_published_product_is_unpublished_other_channel` (function) — [saleor/product/tests/test_product_availability.py:413]
- `test_filter_not_published_product_without_assigned_channel` (function) — [saleor/product/tests/test_product_availability.py:427]
- `test_availability_with_prior_price` (function) — [saleor/product/tests/test_product_availability.py:437]
- `test_availability_with_negative_prior_discount` (function) — [saleor/product/tests/test_product_availability.py:474]

**`saleor/product/tests/test_product_minimal_variant_price.py`**

- `test_update_discounted_price_for_promotion_no_discount` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:23]
- `test_update_discounted_price_for_promotion_discount_on_variant` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:45]
- `test_update_discounted_price_for_promotion_discount_on_product` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:93]
- `test_update_discounted_price_for_promotion_discount_multiple_applicable_rules` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:142]
- `test_update_discounted_price_for_promotion_1_cent_variant_on_10_percentage_discount` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:205]
- `test_update_discounted_price_for_promotion_promotion_not_applicable_for_channel` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:256]
- `test_update_discounted_price_for_promotion_discount_updated` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:298]
- `test_update_discounted_price_for_promotion_discount_not_valid_anymore` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:349]
- `test_update_discounted_price_for_promotion_discount_one_rule_not_valid_anymore` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:398]
- `test_management_commmand_update_all_products_discounted_price` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:480]
- `test_update_discounted_price_for_promotion_promotion_rule_deleted_in_meantime` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:495]
- `delete_promotion_rule` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:526]
- `test_update_discounted_price_rule_deleted_in_meantime_promotion_listing_exist` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:549]
- `delete_promotion_rule` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:587]
- `test_update_discounted_prices_for_promotion_only_dirty_products` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:610]
- `test_update_discounted_prices_returns_changed_prices_when_discount_applied` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:674]
- `test_update_discounted_prices_returns_empty_when_prices_unchanged` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:717]
- `test_update_discounted_prices_returns_changed_prices_for_multiple_channels` (function) — [saleor/product/tests/test_product_minimal_variant_price.py:739]

**`saleor/product/tests/test_product_search.py`**

- `test_update_products_search_vector` (function) — [saleor/product/tests/test_product_search.py:5]

**`saleor/product/tests/test_product_tags.py`**

- `test_get_product_image_thumbnail_no_instance` (function) — [saleor/product/tests/test_product_tags.py:14]
- `test_get_product_image_thumbnail_no_media_image` (function) — [saleor/product/tests/test_product_tags.py:22]
- `test_get_product_image_thumbnail_proxy_url_returned` (function) — [saleor/product/tests/test_product_tags.py:35]
- `test_get_product_image_thumbnail_url_returned` (function) — [saleor/product/tests/test_product_tags.py:49]
- `test_choose_placeholder` (function) — [saleor/product/tests/test_product_tags.py:67]

**`saleor/product/tests/test_product_without_variants.py`**

- `test_get_products_ids_without_variants` (function) — [saleor/product/tests/test_product_without_variants.py:4]

**`saleor/product/tests/test_product.py`**

- `test_filtering_by_attribute` (function) — [saleor/product/tests/test_product.py:23]
- `test_clean_product_attributes_date_time_range_filter_input` (function) — [saleor/product/tests/test_product.py:157]
- `test_clean_product_attributes_boolean_filter_input` (function) — [saleor/product/tests/test_product.py:218]
- `test_get_price` (function) — [saleor/product/tests/test_product.py:258]
- `test_get_price_overridden_price_no_discount` (function) — [saleor/product/tests/test_product.py:286]
- `test_get_price_overridden_price_with_discount` (function) — [saleor/product/tests/test_product.py:313]
- `test_costs_get_margin_for_variant_channel_listing` (function) — [saleor/product/tests/test_product.py:399]
- `test_product_media_delete` (function) — [saleor/product/tests/test_product.py:411]
- `test_product_update_variants_names` (function) — [saleor/product/tests/test_product.py:423]

**`saleor/product/tests/test_tasks.py`**

- `mock_http_response_for_product_task` (function) — [saleor/product/tests/test_tasks.py:36]
- `test_update_variant_relations_for_active_promotion_rules_task` (function) — [saleor/product/tests/test_tasks.py:56]
- `test_update_variant_relations_for_active_promotion_rules_task_when_not_valid` (function) — [saleor/product/tests/test_tasks.py:92]
- `test_update_variant_relations_for_active_promotion_rules_task_with_order_predicate` (function) — [saleor/product/tests/test_tasks.py:135]
- `test_update_variant_relations_for_active_promotion_rules_with_empty_reward_value` (function) — [saleor/product/tests/test_tasks.py:153]
- `test_recalculate_discounted_price_for_products_task` (function) — [saleor/product/tests/test_tasks.py:182]
- `test_recalculate_discounted_price_for_products_task_with_correct_prices` (function) — [saleor/product/tests/test_tasks.py:205]
- `test_recalculate_discounted_price_for_products_task_updates_only_dirty_listings` (function) — [saleor/product/tests/test_tasks.py:223]
- `test_recalculate_discounted_price_for_products_task_re_trigger_task` (function) — [saleor/product/tests/test_tasks.py:247]
- `test_update_variants_names` (function) — [saleor/product/tests/test_tasks.py:261]
- `test_update_variants_names_product_type_does_not_exist` (function) — [saleor/product/tests/test_tasks.py:280]
- `test_get_preorder_variants_to_clean` (function) — [saleor/product/tests/test_tasks.py:292]
- `test_update_products_search_vector_task` (function) — [saleor/product/tests/test_tasks.py:315]
- `test_update_products_search_vector_task_with_static_number_of_queries` (function) — [saleor/product/tests/test_tasks.py:329]
- `test_mem_usage_recalculate_discounted_price_for_products_task` (function) — [saleor/product/tests/test_tasks.py:346]
- `test_mark_products_search_vector_as_dirty` (function) — [saleor/product/tests/test_tasks.py:352]
- `test_fetch_product_media_image_already_has_image` (function) — [saleor/product/tests/test_tasks.py:368]
- `test_fetch_product_media_image_not_found` (function) — [saleor/product/tests/test_tasks.py:381]
- `test_fetch_product_media_image_missing_external_url_and_image` (function) — [saleor/product/tests/test_tasks.py:393]
- `test_fetch_product_media_image_wrong_type` (function) — [saleor/product/tests/test_tasks.py:409]
- `test_fetch_product_media_image_non_image_content_type` (function) — [saleor/product/tests/test_tasks.py:422]
- `test_fetch_product_media_image_success` (function) — [saleor/product/tests/test_tasks.py:441]
- `test_fetch_product_media_image_unsupported_image_content_type` (function) — [saleor/product/tests/test_tasks.py:465]
- `test_fetch_product_media_image_request_exception` (function) — [saleor/product/tests/test_tasks.py:483]
- `test_fetch_product_media_image_non_retryable_exception` (function) — [saleor/product/tests/test_tasks.py:507]
- `test_fetch_product_media_image_non_retryable_exception_on_failure_handler` (function) — [saleor/product/tests/test_tasks.py:528]
- `test_fetch_product_media_image_deleted_after_final_retry` (function) — [saleor/product/tests/test_tasks.py:546]
- `test_fetch_product_media_image_invalid_exif` (function) — [saleor/product/tests/test_tasks.py:564]
- `test_fetch_product_media_image_invalid_metadata` (function) — [saleor/product/tests/test_tasks.py:593]
- `test_fetch_product_media_image_server_error_triggers_retry` (function) — [saleor/product/tests/test_tasks.py:612]
- `test_fetch_product_media_image_client_error_does_not_retry` (function) — [saleor/product/tests/test_tasks.py:634]
- `test_recalculate_discounted_price_triggers_variant_price_updated_webhook` (function) — [saleor/product/tests/test_tasks.py:654]
- `test_recalculate_discounted_price_no_webhook_when_prices_unchanged` (function) — [saleor/product/tests/test_tasks.py:698]

**`saleor/product/tests/test_translation.py`**

- `product_translation_pl` (function) — [saleor/product/tests/test_translation.py:10]
- `attribute_value_translation_fr` (function) — [saleor/product/tests/test_translation.py:20]
- `test_translation` (function) — [saleor/product/tests/test_translation.py:27]
- `test_translation_str_returns_str_of_instance` (function) — [saleor/product/tests/test_translation.py:36]
- `test_wrapper_gets_proper_wrapper` (function) — [saleor/product/tests/test_translation.py:44]
- `test_getattr` (function) — [saleor/product/tests/test_translation.py:56]
- `test_translation_not_override_id` (function) — [saleor/product/tests/test_translation.py:61]
- `test_product_variant_translation` (function) — [saleor/product/tests/test_translation.py:68]
- `test_attribute_value_translation` (function) — [saleor/product/tests/test_translation.py:77]
- `test_voucher_translation` (function) — [saleor/product/tests/test_translation.py:84]

**`saleor/product/tests/test_utils_product.py`**

- `test_mark_products_in_channels_as_dirty_skips_when_input_as_empty_dict` (function) — [saleor/product/tests/test_utils_product.py:13]
- `test_mark_products_in_channels_as_dirty` (function) — [saleor/product/tests/test_utils_product.py:23]
- `test_mark_products_in_channels_as_dirty_product_process_only_for_provided_channels` (function) — [saleor/product/tests/test_utils_product.py:44]
- `test_mark_products_in_channels_as_dirty_with_multiple_products_and_channels` (function) — [saleor/product/tests/test_utils_product.py:78]
- `test_get_channel_to_products_map_from_rules_empty_rules_qs` (function) — [saleor/product/tests/test_utils_product.py:131]
- `test_get_channel_to_products_when_single_rule_related` (function) — [saleor/product/tests/test_utils_product.py:139]
- `test_get_channel_to_products_when_multiple_rules_related` (function) — [saleor/product/tests/test_utils_product.py:157]
- `test_get_channel_to_products_when_multiple_channels_and_rules_related` (function) — [saleor/product/tests/test_utils_product.py:183]

**`saleor/product/tests/utils.py`**

- `create_image` (function) — [saleor/product/tests/utils.py:7]
- `create_image_without_extension` (function) — [saleor/product/tests/utils.py:15]
- `create_zip_file_with_image_ext` (function) — [saleor/product/tests/utils.py:25]

## How it works

The module's files, as provided to this run:

- `saleor/product/tests/__init__.py` (1 lines)
- `saleor/product/tests/test_category.py` (74 lines)
- `saleor/product/tests/test_collections_availability.py` (75 lines)
- `saleor/product/tests/test_fetch_variants_for_promotion_rules.py` (179 lines)
- `saleor/product/tests/test_generate_and_set_variant_name.py` (211 lines)
- `saleor/product/tests/test_get_variant_selection_attributes.py` (39 lines)
- `saleor/product/tests/test_managers.py` (60 lines)
- `saleor/product/tests/test_product_availability.py` (503 lines)
- `saleor/product/tests/test_product_minimal_variant_price.py` (806 lines)
- `saleor/product/tests/test_product_search.py` (17 lines)
- `saleor/product/tests/test_product_tags.py` (83 lines)
- `saleor/product/tests/test_product_without_variants.py` (16 lines)
- `saleor/product/tests/test_product.py` (427 lines)
- `saleor/product/tests/test_tasks.py` (712 lines)
- `saleor/product/tests/test_translation.py` (87 lines)
- `saleor/product/tests/test_utils_product.py` (210 lines)
- `saleor/product/tests/utils.py` (28 lines)

## Interactions

- Imports from: `saleor/product`, `saleor/core`, `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...ProductTypeKind`
- `...attribute.AttributeInputType`
- `...attribute.models.AttributeValue`
- `...attribute.models.AttributeValueTranslation`
- `...attribute.utils.associate_attribute_values_to_instance`
- `...core.utils.translations.get_translation`
- `...discount.PromotionType`
- `...discount.RewardValueType`
- `...discount.models.Promotion`
- `...discount.models.PromotionRule`
- `...discount.utils.promotion.get_active_catalogue_promotion_rules`
- `...discount.utils.promotion.update_rule_variant_relation`
- `...models`
- `...plugins.manager.get_plugins_manager`
- `...product.interface.VariantDiscountedPriceChange`
- `...product.models.ProductVariant`
- `...tax.TaxCalculationStrategy`
- `...tests.race_condition`
- `...tests.utils.dummy_editorjs`
- `...thumbnail.models.Thumbnail`
- `..interface.VariantDiscountedPriceChange`
- `..models.Category`
- `..models.Product`
- `..models.ProductChannelListing`
- `..models.ProductTranslation`
- `..models.ProductType`
- `..models.ProductVariantTranslation`
- `..search.update_products_search_vector`
- `..tasks._update_variants_names`
- `..tasks.update_variants_names`
- `..utils.availability.get_product_availability`
- `..utils.collect_categories_tree_products`
- `..utils.costs.get_margin_for_variant_channel_listing`
- `..utils.delete_categories`
- `..utils.get_products_ids_without_variants`
- `..utils.variant_prices.update_discounted_prices_for_promotion`
- `..utils.variants.fetch_variants_for_promotion_rules`
- `..utils.variants.generate_and_set_variant_name`
- `..utils.variants.get_variant_selection_attributes`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `6aa188077b14` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
