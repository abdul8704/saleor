## Purpose

`saleor/graphql/product/filters` (`saleor/graphql/product/filters`) groups 9 source file(s) exposing 150 top-level declaration(s).

## Public surface

**`saleor/graphql/product/filters/category.py`**

- `CategoryFilter` (class) — [saleor/graphql/product/filters/category.py:29]
- `Meta` (class) — [saleor/graphql/product/filters/category.py:39]
- `category_filter_search` (function) — [saleor/graphql/product/filters/category.py:44]
- `CategoryWhere` (class) — [saleor/graphql/product/filters/category.py:56]
- `Meta` (class) — [saleor/graphql/product/filters/category.py:62]
- `CategoryFilterInput` (class) — [saleor/graphql/product/filters/category.py:67]
- `Meta` (class) — [saleor/graphql/product/filters/category.py:68]
- `CategoryWhereInput` (class) — [saleor/graphql/product/filters/category.py:73]
- `Meta` (class) — [saleor/graphql/product/filters/category.py:74]

**`saleor/graphql/product/filters/collection.py`**

- `CollectionFilter` (class) — [saleor/graphql/product/filters/collection.py:38]
- `Meta` (class) — [saleor/graphql/product/filters/collection.py:46]
- `collection_filter_search` (function) — [saleor/graphql/product/filters/collection.py:50]
- `filter_is_published` (function) — [saleor/graphql/product/filters/collection.py:56]
- `CollectionWhere` (class) — [saleor/graphql/product/filters/collection.py:65]
- `Meta` (class) — [saleor/graphql/product/filters/collection.py:71]
- `CollectionFilterInput` (class) — [saleor/graphql/product/filters/collection.py:76]
- `Meta` (class) — [saleor/graphql/product/filters/collection.py:77]
- `CollectionWhereInput` (class) — [saleor/graphql/product/filters/collection.py:82]
- `Meta` (class) — [saleor/graphql/product/filters/collection.py:83]

**`saleor/graphql/product/filters/product_attributes.py`**

- `KeyValueDict` (class) — [saleor/graphql/product/filters/product_attributes.py:168]
- `filter_products_by_attributes_values` (function) — [saleor/graphql/product/filters/product_attributes.py:201]
- `filter_products_by_attributes_values_qs` (function) — [saleor/graphql/product/filters/product_attributes.py:240]
- `deprecated_filter_attributes` (function) — [saleor/graphql/product/filters/product_attributes.py:306]
- `filter_by_slug_or_name` (function) — [saleor/graphql/product/filters/product_attributes.py:366]
- `filter_by_numeric_attribute` (function) — [saleor/graphql/product/filters/product_attributes.py:382]
- `filter_by_boolean_attribute` (function) — [saleor/graphql/product/filters/product_attributes.py:398]
- `filter_by_date_attribute` (function) — [saleor/graphql/product/filters/product_attributes.py:414]
- `filter_by_date_time_attribute` (function) — [saleor/graphql/product/filters/product_attributes.py:430]
- `filter_by_contains_referenced_page_slugs` (function) — [saleor/graphql/product/filters/product_attributes.py:461]
- `filter_by_contains_referenced_product_slugs` (function) — [saleor/graphql/product/filters/product_attributes.py:501]
- `filter_by_contains_referenced_variant_skus` (function) — [saleor/graphql/product/filters/product_attributes.py:541]
- `filter_by_contains_referenced_category_slugs` (function) — [saleor/graphql/product/filters/product_attributes.py:581]
- `filter_by_contains_referenced_collection_slugs` (function) — [saleor/graphql/product/filters/product_attributes.py:621]
- `filter_by_contains_referenced_object_ids` (function) — [saleor/graphql/product/filters/product_attributes.py:784]
- `filter_objects_by_reference_attributes` (function) — [saleor/graphql/product/filters/product_attributes.py:822]
- `validate_attribute_input` (function) — [saleor/graphql/product/filters/product_attributes.py:961]
- `filter_products_by_attributes` (function) — [saleor/graphql/product/filters/product_attributes.py:1003]

**`saleor/graphql/product/filters/product_helpers.py`**

- `filter_products_by_variant_price` (function) — [saleor/graphql/product/filters/product_helpers.py:34]
- `filter_products_by_minimal_price` (function) — [saleor/graphql/product/filters/product_helpers.py:60]
- `filter_products_by_categories` (function) — [saleor/graphql/product/filters/product_helpers.py:81]
- `filter_products_by_collections` (function) — [saleor/graphql/product/filters/product_helpers.py:91]
- `filter_products_by_stock_availability` (function) — [saleor/graphql/product/filters/product_helpers.py:140]
- `filter_variants_by_stock_availability` (function) — [saleor/graphql/product/filters/product_helpers.py:154]
- `get_available_warehouse_pks_for_product` (function) — [saleor/graphql/product/filters/product_helpers.py:165]
- `filter_categories` (function) — [saleor/graphql/product/filters/product_helpers.py:192]
- `filter_product_types` (function) — [saleor/graphql/product/filters/product_helpers.py:201]
- `filter_has_category` (function) — [saleor/graphql/product/filters/product_helpers.py:210]
- `filter_has_preordered_variants` (function) — [saleor/graphql/product/filters/product_helpers.py:214]
- `filter_collections` (function) — [saleor/graphql/product/filters/product_helpers.py:228]
- `filter_products_is_published` (function) — [saleor/graphql/product/filters/product_helpers.py:237]
- `filter_products_is_available` (function) — [saleor/graphql/product/filters/product_helpers.py:266]
- `filter_products_channel_field_from_date` (function) — [saleor/graphql/product/filters/product_helpers.py:292]
- `filter_products_visible_in_listing` (function) — [saleor/graphql/product/filters/product_helpers.py:309]
- `filter_variant_price` (function) — [saleor/graphql/product/filters/product_helpers.py:322]
- `filter_minimal_price` (function) — [saleor/graphql/product/filters/product_helpers.py:329]
- `filter_stock_availability` (function) — [saleor/graphql/product/filters/product_helpers.py:339]
- `filter_search` (function) — [saleor/graphql/product/filters/product_helpers.py:345]
- `filter_gift_card` (function) — [saleor/graphql/product/filters/product_helpers.py:349]
- `filter_stocks` (function) — [saleor/graphql/product/filters/product_helpers.py:357]
- `filter_warehouses` (function) — [saleor/graphql/product/filters/product_helpers.py:369]
- `filter_quantity` (function) — [saleor/graphql/product/filters/product_helpers.py:389]
- `where_filter_products_is_available` (function) — [saleor/graphql/product/filters/product_helpers.py:418]
- `where_filter_products_channel_field_from_date` (function) — [saleor/graphql/product/filters/product_helpers.py:446]
- `where_filter_has_category` (function) — [saleor/graphql/product/filters/product_helpers.py:465]
- `where_filter_stocks` (function) — [saleor/graphql/product/filters/product_helpers.py:471]
- `where_filter_warehouses` (function) — [saleor/graphql/product/filters/product_helpers.py:485]
- `where_filter_quantity` (function) — [saleor/graphql/product/filters/product_helpers.py:505]
- `where_filter_stock_availability` (function) — [saleor/graphql/product/filters/product_helpers.py:541]
- `where_filter_variant_stock_availability` (function) — [saleor/graphql/product/filters/product_helpers.py:547]
- `where_filter_variant_warehouses` (function) — [saleor/graphql/product/filters/product_helpers.py:553]
- `where_filter_variant_quantity` (function) — [saleor/graphql/product/filters/product_helpers.py:570]
- `where_filter_variant_stocks` (function) — [saleor/graphql/product/filters/product_helpers.py:592]
- `where_filter_gift_card` (function) — [saleor/graphql/product/filters/product_helpers.py:606]
- `where_filter_has_preordered_variants` (function) — [saleor/graphql/product/filters/product_helpers.py:617]
- `where_filter_updated_at_range` (function) — [saleor/graphql/product/filters/product_helpers.py:634]
- `where_filter_by_categories` (function) — [saleor/graphql/product/filters/product_helpers.py:640]

**`saleor/graphql/product/filters/product_type.py`**

- `filter_product_type_configurable` (function) — [saleor/graphql/product/filters/product_type.py:24]
- `filter_product_type` (function) — [saleor/graphql/product/filters/product_type.py:32]
- `filter_product_type_kind` (function) — [saleor/graphql/product/filters/product_type.py:38]
- `ProductTypeFilter` (class) — [saleor/graphql/product/filters/product_type.py:44]
- `Meta` (class) — [saleor/graphql/product/filters/product_type.py:62]
- `filter_product_type_searchable` (function) — [saleor/graphql/product/filters/product_type.py:67]
- `ProductTypeFilterInput` (class) — [saleor/graphql/product/filters/product_type.py:74]
- `Meta` (class) — [saleor/graphql/product/filters/product_type.py:75]

**`saleor/graphql/product/filters/product_variant.py`**

- `filter_sku_list` (function) — [saleor/graphql/product/filters/product_variant.py:67]
- `filter_is_preorder` (function) — [saleor/graphql/product/filters/product_variant.py:71]
- `filter_by_slug_or_name` (function) — [saleor/graphql/product/filters/product_variant.py:82]
- `filter_by_numeric_attribute` (function) — [saleor/graphql/product/filters/product_variant.py:98]
- `filter_by_boolean_attribute` (function) — [saleor/graphql/product/filters/product_variant.py:114]
- `filter_by_date_attribute` (function) — [saleor/graphql/product/filters/product_variant.py:130]
- `filter_by_date_time_attribute` (function) — [saleor/graphql/product/filters/product_variant.py:146]
- `filter_by_contains_referenced_page_slugs` (function) — [saleor/graphql/product/filters/product_variant.py:205]
- `filter_by_contains_referenced_category_slugs` (function) — [saleor/graphql/product/filters/product_variant.py:245]
- `filter_by_contains_referenced_collection_slugs` (function) — [saleor/graphql/product/filters/product_variant.py:285]
- `filter_by_contains_referenced_product_slugs` (function) — [saleor/graphql/product/filters/product_variant.py:327]
- `filter_by_contains_referenced_variant_skus` (function) — [saleor/graphql/product/filters/product_variant.py:367]
- `filter_by_contains_referenced_object_ids` (function) — [saleor/graphql/product/filters/product_variant.py:528]
- `filter_objects_by_reference_attributes` (function) — [saleor/graphql/product/filters/product_variant.py:566]
- `filter_variants_by_attributes` (function) — [saleor/graphql/product/filters/product_variant.py:622]
- `ProductVariantFilter` (class) — [saleor/graphql/product/filters/product_variant.py:704]
- `Meta` (class) — [saleor/graphql/product/filters/product_variant.py:712]
- `product_variant_filter_search` (function) — [saleor/graphql/product/filters/product_variant.py:716]
- `ProductVariantWhere` (class) — [saleor/graphql/product/filters/product_variant.py:727]
- `Meta` (class) — [saleor/graphql/product/filters/product_variant.py:758]
- `filter_product_sku` (function) — [saleor/graphql/product/filters/product_variant.py:763]
- `filter_updated_at` (function) — [saleor/graphql/product/filters/product_variant.py:767]
- `filter_attributes` (function) — [saleor/graphql/product/filters/product_variant.py:771]
- `filter_stock_availability` (function) — [saleor/graphql/product/filters/product_variant.py:776]
- `filter_stocks` (function) — [saleor/graphql/product/filters/product_variant.py:781]
- `is_valid` (function) — [saleor/graphql/product/filters/product_variant.py:784]
- `ProductVariantFilterInput` (class) — [saleor/graphql/product/filters/product_variant.py:790]
- `Meta` (class) — [saleor/graphql/product/filters/product_variant.py:791]
- `ProductVariantWhereInput` (class) — [saleor/graphql/product/filters/product_variant.py:796]
- `Meta` (class) — [saleor/graphql/product/filters/product_variant.py:797]

**`saleor/graphql/product/filters/product.py`**

- `ProductFilter` (class) — [saleor/graphql/product/filters/product.py:85]
- `Meta` (class) — [saleor/graphql/product/filters/product.py:142]
- `filter_attributes` (function) — [saleor/graphql/product/filters/product.py:155]
- `filter_variant_price` (function) — [saleor/graphql/product/filters/product.py:160]
- `filter_minimal_price` (function) — [saleor/graphql/product/filters/product.py:164]
- `filter_is_published` (function) — [saleor/graphql/product/filters/product.py:168]
- `filter_published_from` (function) — [saleor/graphql/product/filters/product.py:177]
- `filter_is_available` (function) — [saleor/graphql/product/filters/product.py:187]
- `filter_available_from` (function) — [saleor/graphql/product/filters/product.py:196]
- `filter_listed` (function) — [saleor/graphql/product/filters/product.py:206]
- `filter_stock_availability` (function) — [saleor/graphql/product/filters/product.py:215]
- `is_valid` (function) — [saleor/graphql/product/filters/product.py:219]
- `ProductWhere` (class) — [saleor/graphql/product/filters/product.py:225]
- `Meta` (class) — [saleor/graphql/product/filters/product.py:315]
- `filter_product_name` (function) — [saleor/graphql/product/filters/product.py:320]
- `filter_product_slug` (function) — [saleor/graphql/product/filters/product.py:324]
- `filter_product_type` (function) — [saleor/graphql/product/filters/product.py:328]
- `filter_category` (function) — [saleor/graphql/product/filters/product.py:332]
- `filter_collection` (function) — [saleor/graphql/product/filters/product.py:336]
- `filter_is_available` (function) — [saleor/graphql/product/filters/product.py:344]
- `filter_is_published` (function) — [saleor/graphql/product/filters/product.py:353]
- `filter_is_listed` (function) — [saleor/graphql/product/filters/product.py:362]
- `filter_published_from` (function) — [saleor/graphql/product/filters/product.py:371]
- `filter_available_from` (function) — [saleor/graphql/product/filters/product.py:381]
- `filter_variant_price` (function) — [saleor/graphql/product/filters/product.py:391]
- `filter_minimal_price` (function) — [saleor/graphql/product/filters/product.py:408]
- `filter_attributes` (function) — [saleor/graphql/product/filters/product.py:423]
- `filter_stock_availability` (function) — [saleor/graphql/product/filters/product.py:426]
- `is_valid` (function) — [saleor/graphql/product/filters/product.py:430]
- `ProductFilterInput` (class) — [saleor/graphql/product/filters/product.py:436]
- `Meta` (class) — [saleor/graphql/product/filters/product.py:437]
- `ProductWhereInput` (class) — [saleor/graphql/product/filters/product.py:442]
- `Meta` (class) — [saleor/graphql/product/filters/product.py:443]

**`saleor/graphql/product/filters/shared.py`**

- `filter_updated_at_range` (function) — [saleor/graphql/product/filters/shared.py:8]
- `ProductStockFilterInput` (class) — [saleor/graphql/product/filters/shared.py:12]
- `Meta` (class) — [saleor/graphql/product/filters/shared.py:16]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/product/filters/__init__.py` (1 lines)
- `saleor/graphql/product/filters/category.py` (76 lines)
- `saleor/graphql/product/filters/collection.py` (85 lines)
- `saleor/graphql/product/filters/product_attributes.py` (1011 lines)
- `saleor/graphql/product/filters/product_helpers.py` (653 lines)
- `saleor/graphql/product/filters/product_type.py` (77 lines)
- `saleor/graphql/product/filters/product_variant.py` (799 lines)
- `saleor/graphql/product/filters/product.py` (445 lines)
- `saleor/graphql/product/filters/shared.py` (17 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core/db`, `saleor/graphql/product`, `saleor/graphql/warehouse`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....attribute.AttributeInputType`
- `....channel.models.Channel`
- `....core.search.prefix_search`
- `....product.ProductTypeKind`
- `....product.models.Category`
- `....product.models.Product`
- `....product.models.ProductType`
- `....product.models.ProductVariant`
- `....warehouse.models.Allocation`
- `....warehouse.models.Reservation`
- `....warehouse.models.Stock`
- `....warehouse.models.Warehouse`
- `...channel.filters.get_channel_slug_from_filter_data`
- `...core.descriptions.ADDED_IN_322`
- `...core.descriptions.ADDED_IN_324`
- `...core.doc_category.DOC_CATEGORY_PRODUCTS`
- `...core.filters.where_input.StringFilterInput`
- `...core.filters.where_input.WhereInputObjectType`
- `...core.scalars.DateTime`
- `...core.types.BaseInputObjectType`
- `...core.types.DateTimeRangeInput`
- `...core.types.IntRangeInput`
- `...core.types.NonNullList`
- `...types`
- `...utils.filters.Number`
- `...utils.filters.filter_range_field`
- `...utils.filters.filter_slug_list`
- `...utils.resolve_global_ids_to_primary_keys`
- `...warehouse.types`
- `..enums.StockAvailability`
- `.product_attributes.filter_products_by_attributes`
- `.product_attributes.validate_attribute_input`
- `.shared.ProductStockFilterInput`
- `.shared.filter_updated_at_range`
- `saleor.graphql.warehouse.types.DEPRECATED_IN_3X_INPUT`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `1273c5e50364` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
