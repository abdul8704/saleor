## Purpose

`saleor/graphql/product` (`saleor/graphql/product`) groups 6 source file(s) exposing 102 top-level declaration(s).

## Public surface

**`saleor/graphql/product/enums.py`**

- `ProductAttributeType` (class) — [saleor/graphql/product/enums.py:19]
- `Meta` (class) — [saleor/graphql/product/enums.py:23]
- `StockAvailability` (class) — [saleor/graphql/product/enums.py:27]
- `Meta` (class) — [saleor/graphql/product/enums.py:31]
- `CollectionPublished` (class) — [saleor/graphql/product/enums.py:35]
- `Meta` (class) — [saleor/graphql/product/enums.py:39]
- `ProductTypeConfigurable` (class) — [saleor/graphql/product/enums.py:43]
- `Meta` (class) — [saleor/graphql/product/enums.py:47]
- `ProductTypeEnum` (class) — [saleor/graphql/product/enums.py:51]
- `Meta` (class) — [saleor/graphql/product/enums.py:54]
- `VariantAttributeScope` (class) — [saleor/graphql/product/enums.py:58]
- `Meta` (class) — [saleor/graphql/product/enums.py:63]

**`saleor/graphql/product/resolvers.py`**

- `resolve_categories` (function) — [saleor/graphql/product/resolvers.py:33]
- `resolve_category_by_translated_slug` (function) — [saleor/graphql/product/resolvers.py:42]
- `resolve_collection_by_id` (function) — [saleor/graphql/product/resolvers.py:50]
- `resolve_collection_by_slug` (function) — [saleor/graphql/product/resolvers.py:59]
- `resolve_collection_by_translated_slug` (function) — [saleor/graphql/product/resolvers.py:68]
- `resolve_collections` (function) — [saleor/graphql/product/resolvers.py:79]
- `resolve_product` (function) — [saleor/graphql/product/resolvers.py:88]
- `resolve_products` (function) — [saleor/graphql/product/resolvers.py:116]
- `resolve_product_type_by_id` (function) — [saleor/graphql/product/resolvers.py:142]
- `resolve_product_types` (function) — [saleor/graphql/product/resolvers.py:150]
- `resolve_variant` (function) — [saleor/graphql/product/resolvers.py:157]
- `resolve_product_variants` (function) — [saleor/graphql/product/resolvers.py:188]
- `resolve_report_product_sales` (function) — [saleor/graphql/product/resolvers.py:215]
- `requestor_has_access_to_all_attributes` (function) — [saleor/graphql/product/resolvers.py:246]
- `resolve_product_attribute` (function) — [saleor/graphql/product/resolvers.py:257]
- `with_assigned_attribute_data` (function) — [saleor/graphql/product/resolvers.py:258]
- `resolve_product_attributes` (function) — [saleor/graphql/product/resolvers.py:281]
- `get_assigned_attributes` (function) — [saleor/graphql/product/resolvers.py:284]
- `resolve_variant_attributes` (function) — [saleor/graphql/product/resolvers.py:307]
- `get_assigned_attributes` (function) — [saleor/graphql/product/resolvers.py:314]
- `resolve_variant_attribute` (function) — [saleor/graphql/product/resolvers.py:339]
- `with_assigned_attribute_data` (function) — [saleor/graphql/product/resolvers.py:340]

**`saleor/graphql/product/schema.py`**

- `ProductQueries` (class) — [saleor/graphql/product/schema.py:140]
- `resolve_categories` (function) — [saleor/graphql/product/schema.py:331]
- `resolve_category` (function) — [saleor/graphql/product/schema.py:339]
- `resolve_collection` (function) — [saleor/graphql/product/schema.py:365]
- `resolve_collections` (function) — [saleor/graphql/product/schema.py:408]
- `resolve_product` (function) — [saleor/graphql/product/schema.py:426]
- `resolve_products` (function) — [saleor/graphql/product/schema.py:477]
- `resolve_product_type` (function) — [saleor/graphql/product/schema.py:514]
- `resolve_product_types` (function) — [saleor/graphql/product/schema.py:519]
- `resolve_product_variant` (function) — [saleor/graphql/product/schema.py:528]
- `resolve_product_variants` (function) — [saleor/graphql/product/schema.py:575]
- `resolve_report_product_sales` (function) — [saleor/graphql/product/schema.py:627]
- `ProductMutations` (class) — [saleor/graphql/product/schema.py:637]

**`saleor/graphql/product/sorters.py`**

- `CategorySortField` (class) — [saleor/graphql/product/sorters.py:31]
- `Meta` (class) — [saleor/graphql/product/sorters.py:36]
- `description` (function) — [saleor/graphql/product/sorters.py:40]
- `qs_with_product_count` (function) — [saleor/graphql/product/sorters.py:52]
- `qs_with_subcategory_count` (function) — [saleor/graphql/product/sorters.py:68]
- `CategorySortingInput` (class) — [saleor/graphql/product/sorters.py:72]
- `Meta` (class) — [saleor/graphql/product/sorters.py:73]
- `CollectionSortField` (class) — [saleor/graphql/product/sorters.py:79]
- `Meta` (class) — [saleor/graphql/product/sorters.py:86]
- `description` (function) — [saleor/graphql/product/sorters.py:90]
- `deprecation_reason` (function) — [saleor/graphql/product/sorters.py:104]
- `qs_with_product_count` (function) — [saleor/graphql/product/sorters.py:113]
- `qs_with_availability` (function) — [saleor/graphql/product/sorters.py:117]
- `qs_with_publication_date` (function) — [saleor/graphql/product/sorters.py:128]
- `qs_with_published_at` (function) — [saleor/graphql/product/sorters.py:132]
- `CollectionSortingInput` (class) — [saleor/graphql/product/sorters.py:143]
- `Meta` (class) — [saleor/graphql/product/sorters.py:144]
- `ProductOrderField` (class) — [saleor/graphql/product/sorters.py:150]
- `Meta` (class) — [saleor/graphql/product/sorters.py:166]
- `description` (function) — [saleor/graphql/product/sorters.py:170]
- `deprecation_reason` (function) — [saleor/graphql/product/sorters.py:209]
- `qs_with_price` (function) — [saleor/graphql/product/sorters.py:220]
- `qs_with_minimal_price` (function) — [saleor/graphql/product/sorters.py:230]
- `qs_with_published` (function) — [saleor/graphql/product/sorters.py:239]
- `qs_with_publication_date` (function) — [saleor/graphql/product/sorters.py:250]
- `qs_with_published_at` (function) — [saleor/graphql/product/sorters.py:254]
- `qs_with_collection` (function) — [saleor/graphql/product/sorters.py:265]
- `ProductOrder` (class) — [saleor/graphql/product/sorters.py:287]
- `Meta` (class) — [saleor/graphql/product/sorters.py:299]
- `ProductVariantSortField` (class) — [saleor/graphql/product/sorters.py:305]
- `Meta` (class) — [saleor/graphql/product/sorters.py:308]
- `description` (function) — [saleor/graphql/product/sorters.py:312]
- `ProductVariantSortingInput` (class) — [saleor/graphql/product/sorters.py:322]
- `Meta` (class) — [saleor/graphql/product/sorters.py:323]
- `ProductTypeSortField` (class) — [saleor/graphql/product/sorters.py:329]
- `Meta` (class) — [saleor/graphql/product/sorters.py:333]
- `description` (function) — [saleor/graphql/product/sorters.py:337]
- `ProductTypeSortingInput` (class) — [saleor/graphql/product/sorters.py:348]
- `Meta` (class) — [saleor/graphql/product/sorters.py:349]
- `MediaChoicesSortField` (class) — [saleor/graphql/product/sorters.py:355]
- _…and 4 more in this file_

**`saleor/graphql/product/utils.py`**

- `MediaValidationError` (class) — [saleor/graphql/product/utils.py:41]
- `validate_media_input` (function) — [saleor/graphql/product/utils.py:47]
- `MediaUrlProbeResult` (class) — [saleor/graphql/product/utils.py:82]
- `probe_media_url` (function) — [saleor/graphql/product/utils.py:90]
- `get_used_attribute_values_for_variant` (function) — [saleor/graphql/product/utils.py:145]
- `get_used_variants_attribute_values` (function) — [saleor/graphql/product/utils.py:163]
- `create_stocks` (function) — [saleor/graphql/product/utils.py:193]
- `DraftOrderLinesData` (class) — [saleor/graphql/product/utils.py:215]
- `get_draft_order_lines_data_for_variants` (function) — [saleor/graphql/product/utils.py:221]
- `clean_variant_sku` (function) — [saleor/graphql/product/utils.py:240]
- `update_ordered_media` (function) — [saleor/graphql/product/utils.py:246]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/product/__init__.py` (1 lines)
- `saleor/graphql/product/enums.py` (64 lines)
- `saleor/graphql/product/resolvers.py` (360 lines)
- `saleor/graphql/product/schema.py` (701 lines)
- `saleor/graphql/product/sorters.py` (375 lines)
- `saleor/graphql/product/utils.py` (265 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/graphql`, `saleor/plugins/openid_connect`, `saleor/core`
- Imported by: `saleor/graphql/product/filters`

Internal dependencies named in the source:

- `...attribute.models`
- `...channel.models.Channel`
- `...core.exceptions.UnsupportedMediaProviderException`
- `...core.http_client.HTTPClient`
- `...core.search.prefix_search`
- `...core.tracing.traced_atomic_transaction`
- `...order.OrderStatus`
- `...order.models`
- `...order.models.Order`
- `...permission.enums.ProductPermissions`
- `...permission.utils.has_one_of_permissions`
- `...product.MEDIA_URL_CHAR_LIMIT`
- `...product.ProductMediaTypes`
- `...product.ProductTypeKind`
- `...product.models`
- `...product.models.ALL_PRODUCTS_PERMISSIONS`
- `...product.models.ProductVariant`
- `...warehouse.models.Stock`
- `...warehouse.models.Warehouse`
- `..attribute.utils.shared.AssignedAttributeData`
- `..channel.dataloaders.by_self.ChannelBySlugLoader`
- `..channel.utils.get_default_channel_slug_or_graphql_error`
- `..core.ResolveInfo`
- `..core.connection.create_connection_slice`
- `..core.connection.filter_connection_queryset`
- `..core.context.ChannelContext`
- `..core.context.ChannelQsContext`
- `..core.descriptions.CHANNEL_REQUIRED`
- `..core.doc_category.DOC_CATEGORY_PRODUCTS`
- `..core.enums.LanguageCodeEnum`
- `..core.enums.ProductErrorCode`
- `..core.enums.ReportingPeriod`
- `..core.enums.to_enum`
- `..core.tracing.traced_resolver`
- `..core.types.BaseEnum`
- `..core.types.ChannelSortInputObjectType`
- `..core.types.NonNullList`
- `..core.types.SortInputObjectType`
- `..core.utils.from_global_id_or_error`
- `..core.utils.validate_and_apply_search_rank_sorting`
- `..core.validators.validate_one_of_args_is_in_query`
- `..shop.resolvers.get_database_connection_name`
- `..utils.filters.filter_by_period`
- `..utils.get_user_or_app_from_context`
- `.dataloaders.products.CategoryByIdLoader`
- `.dataloaders.products.CategoryBySlugLoader`
- `.filters.category.CategoryFilterInput`
- `.filters.category.CategoryWhereInput`
- `.filters.collection.CollectionFilterInput`
- `.filters.collection.CollectionWhereInput`
- `.filters.product.ProductFilterInput`
- `.filters.product.ProductWhereInput`
- `.filters.product_type.ProductTypeFilterInput`
- `.filters.product_variant.ProductVariantFilterInput`
- `.filters.product_variant.ProductVariantWhereInput`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `4cd092f0f033` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
