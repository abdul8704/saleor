## Purpose

`saleor/graphql/product/tests/benchmark` (`saleor/graphql/product/tests/benchmark`) groups 9 source file(s) exposing 50 top-level declaration(s).

## Public surface

**`saleor/graphql/product/tests/benchmark/test_category.py`**

- `test_category_view` (function) — [saleor/graphql/product/tests/benchmark/test_category.py:10]
- `test_categories_children` (function) — [saleor/graphql/product/tests/benchmark/test_category.py:137]
- `test_category_delete` (function) — [saleor/graphql/product/tests/benchmark/test_category.py:178]
- `test_categories_for_federation_query_count` (function) — [saleor/graphql/product/tests/benchmark/test_category.py:211]

**`saleor/graphql/product/tests/benchmark/test_collection.py`**

- `test_collection_view` (function) — [saleor/graphql/product/tests/benchmark/test_collection.py:13]
- `test_retrieve_collection_channel_listings` (function) — [saleor/graphql/product/tests/benchmark/test_collection.py:124]
- `test_create_collection` (function) — [saleor/graphql/product/tests/benchmark/test_collection.py:166]
- `test_delete_collection` (function) — [saleor/graphql/product/tests/benchmark/test_collection.py:228]
- `test_collection_add_products` (function) — [saleor/graphql/product/tests/benchmark/test_collection.py:267]
- `test_remove_products_from_collection` (function) — [saleor/graphql/product/tests/benchmark/test_collection.py:309]
- `test_collection_bulk_delete` (function) — [saleor/graphql/product/tests/benchmark/test_collection.py:351]
- `test_collections_for_federation_query_count` (function) — [saleor/graphql/product/tests/benchmark/test_collection.py:390]
- `test_collection_batching_not_even` (function) — [saleor/graphql/product/tests/benchmark/test_collection.py:462]
- `test_collection_batching_even` (function) — [saleor/graphql/product/tests/benchmark/test_collection.py:483]
- `test_collection_batching_smaller_than_batch_size` (function) — [saleor/graphql/product/tests/benchmark/test_collection.py:504]
- `test_collection_batching_no_ids` (function) — [saleor/graphql/product/tests/benchmark/test_collection.py:525]

**`saleor/graphql/product/tests/benchmark/test_homepage.py`**

- `test_retrieve_product_list` (function) — [saleor/graphql/product/tests/benchmark/test_homepage.py:9]
- `test_report_product_sales` (function) — [saleor/graphql/product/tests/benchmark/test_homepage.py:39]

**`saleor/graphql/product/tests/benchmark/test_product_bulk_create.py`**

- `attributes_without_values` (function) — [saleor/graphql/product/tests/benchmark/test_product_bulk_create.py:69]
- `test_product_bulk_create_with_base_data` (function) — [saleor/graphql/product/tests/benchmark/test_product_bulk_create.py:77]

**`saleor/graphql/product/tests/benchmark/test_product_variant_channel_listing_update.py`**

- `test_variant_channel_listing_update` (function) — [saleor/graphql/product/tests/benchmark/test_product_variant_channel_listing_update.py:10]

**`saleor/graphql/product/tests/benchmark/test_product.py`**

- `test_product_details` (function) — [saleor/graphql/product/tests/benchmark/test_product.py:21]
- `test_retrieve_product_attributes` (function) — [saleor/graphql/product/tests/benchmark/test_product.py:182]
- `test_retrieve_product_images` (function) — [saleor/graphql/product/tests/benchmark/test_product.py:208]
- `test_retrieve_product_media` (function) — [saleor/graphql/product/tests/benchmark/test_product.py:230]
- `test_retrieve_channel_listings` (function) — [saleor/graphql/product/tests/benchmark/test_product.py:252]
- `test_retrive_products_with_product_types_and_attributes` (function) — [saleor/graphql/product/tests/benchmark/test_product.py:368]
- `test_product_create` (function) — [saleor/graphql/product/tests/benchmark/test_product.py:398]
- `test_update_product` (function) — [saleor/graphql/product/tests/benchmark/test_product.py:504]
- `test_filter_products_by_attributes` (function) — [saleor/graphql/product/tests/benchmark/test_product.py:644]
- `test_filter_products_by_numeric_attributes` (function) — [saleor/graphql/product/tests/benchmark/test_product.py:661]
- `test_filter_products_by_boolean_attributes` (function) — [saleor/graphql/product/tests/benchmark/test_product.py:688]
- `test_filter_products_by_gift_card` (function) — [saleor/graphql/product/tests/benchmark/test_product.py:712]
- `test_product_translations` (function) — [saleor/graphql/product/tests/benchmark/test_product.py:729]
- `test_products_for_federation_query_count` (function) — [saleor/graphql/product/tests/benchmark/test_product.py:755]
- `test_products_media_for_federation_query_count` (function) — [saleor/graphql/product/tests/benchmark/test_product.py:815]
- `test_products_types_for_federation_query_count` (function) — [saleor/graphql/product/tests/benchmark/test_product.py:875]

**`saleor/graphql/product/tests/benchmark/test_variant_stocks.py`**

- `test_product_variants_stocks_create` (function) — [saleor/graphql/product/tests/benchmark/test_variant_stocks.py:20]
- `test_product_variants_stocks_create_with_single_webhook_called` (function) — [saleor/graphql/product/tests/benchmark/test_variant_stocks.py:104]
- `test_product_variants_stocks_update_byid` (function) — [saleor/graphql/product/tests/benchmark/test_variant_stocks.py:200]
- `test_product_variants_stocks_update_by_sku` (function) — [saleor/graphql/product/tests/benchmark/test_variant_stocks.py:239]
- `test_product_variants_stocks_delete_by_id` (function) — [saleor/graphql/product/tests/benchmark/test_variant_stocks.py:310]
- `test_product_variants_stocks_delete_by_sku` (function) — [saleor/graphql/product/tests/benchmark/test_variant_stocks.py:372]
- `test_product_variants_stocks_delete_with_out_of_stock_webhook_many_calls` (function) — [saleor/graphql/product/tests/benchmark/test_variant_stocks.py:433]
- `test_query_product_variants_stocks` (function) — [saleor/graphql/product/tests/benchmark/test_variant_stocks.py:503]

**`saleor/graphql/product/tests/benchmark/test_variant.py`**

- `test_retrieve_variant_list` (function) — [saleor/graphql/product/tests/benchmark/test_variant.py:13]
- `test_product_variant_bulk_create` (function) — [saleor/graphql/product/tests/benchmark/test_variant.py:120]
- `test_product_variant_create` (function) — [saleor/graphql/product/tests/benchmark/test_variant.py:173]
- `test_update_product_variant` (function) — [saleor/graphql/product/tests/benchmark/test_variant.py:273]
- `test_products_variants_for_federation_query_count` (function) — [saleor/graphql/product/tests/benchmark/test_variant.py:356]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/product/tests/benchmark/__init__.py` (1 lines)
- `saleor/graphql/product/tests/benchmark/test_category.py` (269 lines)
- `saleor/graphql/product/tests/benchmark/test_collection.py` (528 lines)
- `saleor/graphql/product/tests/benchmark/test_homepage.py` (68 lines)
- `saleor/graphql/product/tests/benchmark/test_product_bulk_create.py` (167 lines)
- `saleor/graphql/product/tests/benchmark/test_product_variant_channel_listing_update.py` (93 lines)
- `saleor/graphql/product/tests/benchmark/test_product.py` (926 lines)
- `saleor/graphql/product/tests/benchmark/test_variant_stocks.py` (539 lines)
- `saleor/graphql/product/tests/benchmark/test_variant.py` (406 lines)

## Interactions

- Imports from: `saleor/graphql/product/bulk_mutations`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....attribute.models.Attribute`
- `.....attribute.utils.associate_attribute_values_to_instance`
- `.....channel.models.Channel`
- `.....core.taxes.TaxType`
- `.....plugins.manager.PluginsManager`
- `.....product.models.Category`
- `.....product.models.Product`
- `.....product.models.ProductChannelListing`
- `.....product.models.ProductMedia`
- `.....product.models.ProductTranslation`
- `.....product.models.ProductVariant`
- `.....product.models.VariantMedia`
- `.....warehouse.models.Stock`
- `.....warehouse.models.Warehouse`
- `....core.enums.ReportingPeriod`
- `....tests.utils.get_graphql_content`
- `...mutations.collection.collection_create.CollectionCreate`
- `...mutations.collection.collection_delete.CollectionDelete`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `151594b0d097` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
