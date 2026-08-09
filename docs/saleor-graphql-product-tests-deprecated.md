## Purpose

`saleor/graphql/product/tests/deprecated` (`saleor/graphql/product/tests/deprecated`) groups 9 source file(s) exposing 60 top-level declaration(s).

## Public surface

**`saleor/graphql/product/tests/deprecated/test_collection_channel_listing_update.py`**

- `test_collection_channel_listing_update_as_staff_user` (function) — [saleor/graphql/product/tests/deprecated/test_collection_channel_listing_update.py:35]
- `test_collection_channel_listing_update_as_app` (function) — [saleor/graphql/product/tests/deprecated/test_collection_channel_listing_update.py:91]
- `test_collection_channel_listing_update_add_channel` (function) — [saleor/graphql/product/tests/deprecated/test_collection_channel_listing_update.py:146]
- `test_collection_channel_listing_update_update_publication_date` (function) — [saleor/graphql/product/tests/deprecated/test_collection_channel_listing_update.py:201]
- `test_collection_channel_listing_update_update_publication_date_and_published_at` (function) — [saleor/graphql/product/tests/deprecated/test_collection_channel_listing_update.py:237]

**`saleor/graphql/product/tests/deprecated/test_collection_sorting.py`**

- `collections_for_sorting_with_channels` (function) — [saleor/graphql/product/tests/deprecated/test_collection_sorting.py:10]
- `test_collections_with_sorting_and_without_channel` (function) — [saleor/graphql/product/tests/deprecated/test_collection_sorting.py:102]
- `test_collections_with_sorting_and_channel_USD` (function) — [saleor/graphql/product/tests/deprecated/test_collection_sorting.py:135]
- `test_collections_with_sorting_and_channel_PLN` (function) — [saleor/graphql/product/tests/deprecated/test_collection_sorting.py:174]
- `test_collections_with_sorting_and_not_existing_channel_asc` (function) — [saleor/graphql/product/tests/deprecated/test_collection_sorting.py:208]
- `test_collections_with_sorting_and_not_existing_channel_desc` (function) — [saleor/graphql/product/tests/deprecated/test_collection_sorting.py:238]

**`saleor/graphql/product/tests/deprecated/test_collection.py`**

- `test_collections_query_with_default_channel_slug` (function) — [saleor/graphql/product/tests/deprecated/test_collection.py:8]

**`saleor/graphql/product/tests/deprecated/test_product_channel_listing_update.py`**

- `test_product_channel_listing_update_as_staff_user` (function) — [saleor/graphql/product/tests/deprecated/test_product_channel_listing_update.py:63]
- `test_product_channel_listing_update_trigger_webhook_product_updated` (function) — [saleor/graphql/product/tests/deprecated/test_product_channel_listing_update.py:145]
- `test_product_channel_listing_update_add_channel` (function) — [saleor/graphql/product/tests/deprecated/test_product_channel_listing_update.py:187]
- `test_product_channel_listing_update_update_publication_data` (function) — [saleor/graphql/product/tests/deprecated/test_product_channel_listing_update.py:242]
- `test_product_channel_listing_update_update_publication_date_and_published_at` (function) — [saleor/graphql/product/tests/deprecated/test_product_channel_listing_update.py:290]
- `test_product_channel_listing_update_update_is_available_for_purchase_past_date` (function) — [saleor/graphql/product/tests/deprecated/test_product_channel_listing_update.py:330]
- `test_product_channel_listing_update_update_is_available_for_purchase_future_date` (function) — [saleor/graphql/product/tests/deprecated/test_product_channel_listing_update.py:375]
- `test_product_channel_listing_update_update_is_available_for_purchase_false_and_date` (function) — [saleor/graphql/product/tests/deprecated/test_product_channel_listing_update.py:422]
- `test_product_channel_listing_update_available_for_purchase_both_date_value_given` (function) — [saleor/graphql/product/tests/deprecated/test_product_channel_listing_update.py:462]

**`saleor/graphql/product/tests/deprecated/test_product_sorting.py`**

- `test_sort_products_by_publication_date` (function) — [saleor/graphql/product/tests/deprecated/test_product_sorting.py:33]
- `test_products_with_sorting_and_without_channel` (function) — [saleor/graphql/product/tests/deprecated/test_product_sorting.py:86]
- `test_pagination_for_sorting_products_by_publication_date` (function) — [saleor/graphql/product/tests/deprecated/test_product_sorting.py:127]
- `test_pagination_for_sorting_collections_by_publication_date` (function) — [saleor/graphql/product/tests/deprecated/test_product_sorting.py:194]

**`saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py`**

- `test_product_variant_bulk_create_by_name` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:67]
- `test_product_variant_bulk_create_by_attribute_id` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:125]
- `test_product_variant_bulk_create_with_swatch_attribute` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:172]
- `test_product_variant_bulk_create_only_not_variant_selection_attributes` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:220]
- `test_product_variant_bulk_create_empty_attribute` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:265]
- `test_product_variant_bulk_create_with_new_attribute_value` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:289]
- `test_product_variant_bulk_create_variant_selection_and_other_attributes` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:336]
- `test_product_variant_bulk_create_stocks_input` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:380]
- `test_product_variant_bulk_create_duplicated_warehouses` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:465]
- `test_product_variant_bulk_create_channel_listings_input` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:513]
- `test_product_variant_bulk_create_preorder_channel_listings_input` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:632]
- `test_product_variant_bulk_create_duplicated_channels` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:750]
- `test_product_variant_bulk_create_too_many_decimal_places_in_price` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:791]
- `test_product_variant_bulk_create_product_not_assigned_to_channel` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:845]
- `test_product_variant_bulk_create_duplicated_sku` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:886]
- `test_product_variant_bulk_create_duplicated_sku_in_input` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:926]
- `test_product_variant_bulk_create_without_sku` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:959]
- `test_product_variant_bulk_create_many_errors` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:992]
- `test_product_variant_bulk_create_two_variants_duplicated_one_attribute_value` (function) — [saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py:1054]

**`saleor/graphql/product/tests/deprecated/test_product.py`**

- `test_product_query_by_id_with_default_channel` (function) — [saleor/graphql/product/tests/deprecated/test_product.py:75]
- `test_product_query_by_slug_with_default_channel` (function) — [saleor/graphql/product/tests/deprecated/test_product.py:87]
- `test_fetch_all_products` (function) — [saleor/graphql/product/tests/deprecated/test_product.py:98]
- `test_products_query_with_price_filter` (function) — [saleor/graphql/product/tests/deprecated/test_product.py:116]
- `test_sort_products_product_type_name` (function) — [saleor/graphql/product/tests/deprecated/test_product.py:141]
- `test_get_collections_from_product_as_customer` (function) — [saleor/graphql/product/tests/deprecated/test_product.py:211]
- `test_get_collections_from_product_as_anonymous` (function) — [saleor/graphql/product/tests/deprecated/test_product.py:235]
- `test_collections_query_with_filter` (function) — [saleor/graphql/product/tests/deprecated/test_product.py:259]
- `test_collections_query_with_sort` (function) — [saleor/graphql/product/tests/deprecated/test_product.py:313]
- `test_fetch_all_variants` (function) — [saleor/graphql/product/tests/deprecated/test_product.py:378]

**`saleor/graphql/product/tests/deprecated/test_utils.py`**

- `test_clean_tax_code_does_nothing_when_empty_data` (function) — [saleor/graphql/product/tests/deprecated/test_utils.py:5]
- `test_clean_tax_code_does_nothing_when_tax_class_provided` (function) — [saleor/graphql/product/tests/deprecated/test_utils.py:16]
- `test_clean_tax_code_when_tax_class_exists_by_name` (function) — [saleor/graphql/product/tests/deprecated/test_utils.py:27]
- `test_clean_tax_code_when_tax_class_exists_by_avatax` (function) — [saleor/graphql/product/tests/deprecated/test_utils.py:40]
- `test_clean_tax_code_when_tax_class_exists_by_vatlayer` (function) — [saleor/graphql/product/tests/deprecated/test_utils.py:53]
- `test_clean_tax_code_when_tax_class_does_not_exists` (function) — [saleor/graphql/product/tests/deprecated/test_utils.py:68]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/product/tests/deprecated/__init__.py` (1 lines)
- `saleor/graphql/product/tests/deprecated/test_collection_channel_listing_update.py` (273 lines)
- `saleor/graphql/product/tests/deprecated/test_collection_sorting.py` (258 lines)
- `saleor/graphql/product/tests/deprecated/test_collection.py` (49 lines)
- `saleor/graphql/product/tests/deprecated/test_product_channel_listing_update.py` (499 lines)
- `saleor/graphql/product/tests/deprecated/test_product_sorting.py` (249 lines)
- `saleor/graphql/product/tests/deprecated/test_product_variant_bulk_create.py` (1084 lines)
- `saleor/graphql/product/tests/deprecated/test_product.py` (386 lines)
- `saleor/graphql/product/tests/deprecated/test_utils.py` (78 lines)

## Interactions

- Imports from: `saleor/graphql/product/bulk_mutations`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....attribute.AttributeInputType`
- `.....channel.models.Channel`
- `.....channel.utils.DEPRECATION_WARNING_MESSAGE`
- `.....product.error_codes.CollectionErrorCode`
- `.....product.error_codes.ProductErrorCode`
- `.....product.error_codes.ProductVariantBulkErrorCode`
- `.....product.models.Collection`
- `.....product.models.CollectionChannelListing`
- `.....product.models.Product`
- `.....product.models.ProductChannelListing`
- `.....product.models.ProductVariant`
- `.....product.utils.costs.get_product_costs_data`
- `.....tax.models.TaxClass`
- `.....tests.utils.dummy_editorjs`
- `....tests.utils.assert_graphql_error_with_message`
- `....tests.utils.get_graphql_content`
- `...mutations.utils.clean_tax_code`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `37ce2c73db17` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
