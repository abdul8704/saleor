## Purpose

`saleor/graphql/product/bulk_mutations` (`saleor/graphql/product/bulk_mutations`) groups 13 source file(s) exposing 127 top-level declaration(s).

## Public surface

**`saleor/graphql/product/bulk_mutations/category_bulk_delete.py`**

- `CategoryBulkDelete` (class) — [saleor/graphql/product/bulk_mutations/category_bulk_delete.py:13]
- `Arguments` (class) — [saleor/graphql/product/bulk_mutations/category_bulk_delete.py:14]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/category_bulk_delete.py:24]
- `bulk_action` (function) — [saleor/graphql/product/bulk_mutations/category_bulk_delete.py:34]

**`saleor/graphql/product/bulk_mutations/collection_bulk_delete.py`**

- `CollectionBulkDelete` (class) — [saleor/graphql/product/bulk_mutations/collection_bulk_delete.py:17]
- `Arguments` (class) — [saleor/graphql/product/bulk_mutations/collection_bulk_delete.py:18]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/collection_bulk_delete.py:28]
- `bulk_action` (function) — [saleor/graphql/product/bulk_mutations/collection_bulk_delete.py:38]

**`saleor/graphql/product/bulk_mutations/product_bulk_create.py`**

- `get_results` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:55]
- `ProductChannelListingCreateInput` (class) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:74]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:101]
- `ProductBulkResult` (class) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:105]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:113]
- `ProductBulkCreateInput` (class) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:117]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:174]
- `ProductBulkCreate` (class) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:178]
- `Arguments` (class) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:190]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:202]
- `generate_unique_slug` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:211]
- `clean_base_fields` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:234]
- `add_indexes_to_errors` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:265]
- `clean_attributes` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:286]
- `set_available_for_purchase_at` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:349]
- `set_published_at` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:362]
- `clean_product_channel_listings` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:367]
- `clean_media` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:429]
- `clean_variants` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:489]
- `clean_product_input` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:554]
- `clean_products` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:619]
- `create_products` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:657]
- `create_variants` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:729]
- `save` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:778]
- `schedule_fetch_product_media_image_tasks` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:830]
- `prepare_products_channel_listings` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:861]
- `save_variants` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:881]
- `prepare_media` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:885]
- `post_save_actions` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:921]
- `perform_mutation` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_create.py:939]

**`saleor/graphql/product/bulk_mutations/product_bulk_delete.py`**

- `ProductBulkDelete` (class) — [saleor/graphql/product/bulk_mutations/product_bulk_delete.py:28]
- `Arguments` (class) — [saleor/graphql/product/bulk_mutations/product_bulk_delete.py:29]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_bulk_delete.py:39]
- `perform_mutation` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_delete.py:50]
- `delete_assigned_attribute_values` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_delete.py:93]
- `bulk_action` (function) — [saleor/graphql/product/bulk_mutations/product_bulk_delete.py:107]

**`saleor/graphql/product/bulk_mutations/product_media_bulk_delete.py`**

- `ProductMediaBulkDelete` (class) — [saleor/graphql/product/bulk_mutations/product_media_bulk_delete.py:11]
- `Arguments` (class) — [saleor/graphql/product/bulk_mutations/product_media_bulk_delete.py:12]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_media_bulk_delete.py:22]

**`saleor/graphql/product/bulk_mutations/product_type_bulk_delete.py`**

- `ProductTypeBulkDelete` (class) — [saleor/graphql/product/bulk_mutations/product_type_bulk_delete.py:21]
- `Arguments` (class) — [saleor/graphql/product/bulk_mutations/product_type_bulk_delete.py:22]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_type_bulk_delete.py:32]
- `perform_mutation` (function) — [saleor/graphql/product/bulk_mutations/product_type_bulk_delete.py:43]
- `bulk_action` (function) — [saleor/graphql/product/bulk_mutations/product_type_bulk_delete.py:56]
- `delete_assigned_attribute_values` (function) — [saleor/graphql/product/bulk_mutations/product_type_bulk_delete.py:67]

**`saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py`**

- `clean_price` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:56]
- `get_results` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:88]
- `ProductVariantBulkResult` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:107]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:117]
- `BulkAttributeValueInput` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:121]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:191]
- `ProductVariantBulkCreateInput` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:195]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:213]
- `ProductVariantBulkCreate` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:217]
- `Arguments` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:237]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:256]
- `clean_attributes` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:266]
- `clean_prices` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:341]
- `clean_channel_listings` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:389]
- `clean_stocks` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:516]
- `add_indexes_to_errors` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:584]
- `create_variants` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:603]
- `validate_base_fields` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:650]
- `clean_variant` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:710]
- `clean_variants` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:781]
- `prepare_channel_listings` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:836]
- `set_variant_name` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:854]
- `save_variants` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:874]
- `prepare_stocks` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:924]
- `post_save_actions` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:935]
- `perform_mutation` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py:957]

**`saleor/graphql/product/bulk_mutations/product_variant_bulk_delete.py`**

- `ProductVariantBulkDelete` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_delete.py:34]
- `Arguments` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_delete.py:35]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_delete.py:53]
- `post_save_actions` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_delete.py:63]
- `perform_mutation` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_delete.py:82]
- `delete_assigned_attribute_values` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_delete.py:174]
- `delete_product_channel_listings_without_available_variants` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_delete.py:181]

**`saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py`**

- `ProductVariantStocksUpdateInput` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:43]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:60]
- `ChannelListingUpdateInput` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:64]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:73]
- `ProductVariantChannelListingUpdateInput` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:77]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:94]
- `ProductVariantBulkUpdateInput` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:98]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:117]
- `ProductVariantBulkUpdate` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:122]
- `Arguments` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:135]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:154]
- `save` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:163]
- `validate_base_fields` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:167]
- `clean_prices` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:175]
- `clean_channel_listings` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:222]
- `clean_stocks` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:308]
- `clean_variant` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:387]
- `clean_variants` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:476]
- `update_variants` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:568]
- `prepare_stocks` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:620]
- `prepare_channel_listings` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:634]
- `save_variants` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:674]
- `post_save_actions` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:763]
- `perform_mutation` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:828]
- `generate_pre_save_payloads` (function) — [saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py:893]

**`saleor/graphql/product/bulk_mutations/product_variant_stocks_create.py`**

- `ProductVariantStocksCreate` (class) — [saleor/graphql/product/bulk_mutations/product_variant_stocks_create.py:33]
- `Arguments` (class) — [saleor/graphql/product/bulk_mutations/product_variant_stocks_create.py:38]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_variant_stocks_create.py:49]
- `perform_mutation` (function) — [saleor/graphql/product/bulk_mutations/product_variant_stocks_create.py:86]
- `clean_stocks_input` (function) — [saleor/graphql/product/bulk_mutations/product_variant_stocks_create.py:124]
- `check_for_duplicates` (function) — [saleor/graphql/product/bulk_mutations/product_variant_stocks_create.py:147]
- `update_errors` (function) — [saleor/graphql/product/bulk_mutations/product_variant_stocks_create.py:162]

**`saleor/graphql/product/bulk_mutations/product_variant_stocks_delete.py`**

- `ProductVariantStocksDelete` (class) — [saleor/graphql/product/bulk_mutations/product_variant_stocks_delete.py:32]
- `Arguments` (class) — [saleor/graphql/product/bulk_mutations/product_variant_stocks_delete.py:37]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_variant_stocks_delete.py:50]
- `perform_mutation` (function) — [saleor/graphql/product/bulk_mutations/product_variant_stocks_delete.py:87]

**`saleor/graphql/product/bulk_mutations/product_variant_stocks_update.py`**

- `ProductVariantStocksUpdate` (class) — [saleor/graphql/product/bulk_mutations/product_variant_stocks_update.py:38]
- `Meta` (class) — [saleor/graphql/product/bulk_mutations/product_variant_stocks_update.py:39]
- `Arguments` (class) — [saleor/graphql/product/bulk_mutations/product_variant_stocks_update.py:110]
- `perform_mutation` (function) — [saleor/graphql/product/bulk_mutations/product_variant_stocks_update.py:126]
- `update_or_create_variant_stocks` (function) — [saleor/graphql/product/bulk_mutations/product_variant_stocks_update.py:169]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/product/bulk_mutations/product_variant_stocks_update.py` (237 lines)
- `saleor/graphql/product/bulk_mutations/product_variant_bulk_delete.py` (219 lines)
- `saleor/graphql/product/bulk_mutations/product_variant_stocks_create.py` (167 lines)
- `saleor/graphql/product/bulk_mutations/product_variant_stocks_delete.py` (139 lines)
- `saleor/graphql/product/bulk_mutations/collection_bulk_delete.py` (63 lines)
- `saleor/graphql/product/bulk_mutations/product_bulk_create.py` (972 lines)
- `saleor/graphql/product/bulk_mutations/product_bulk_delete.py` (137 lines)
- `saleor/graphql/product/bulk_mutations/product_type_bulk_delete.py` (80 lines)
- `saleor/graphql/product/bulk_mutations/product_variant_bulk_create.py` (1007 lines)
- `saleor/graphql/product/bulk_mutations/product_variant_bulk_update.py` (913 lines)
- `saleor/graphql/product/bulk_mutations/__init__.py` (27 lines)
- `saleor/graphql/product/bulk_mutations/category_bulk_delete.py` (36 lines)
- `saleor/graphql/product/bulk_mutations/product_media_bulk_delete.py` (29 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core/db`, `saleor/channel/tests`, `saleor/core/utils`
- Imported by: `saleor/graphql/product/tests/mutations`, `saleor/graphql/product/tests`, `saleor/graphql/product/tests/benchmark`, `saleor/graphql/product/tests/deprecated`

Internal dependencies named in the source:

- `....attribute.AttributeInputType`
- `....attribute.AttributeType`
- `....attribute.models`
- `....core.editorjs.editorjs_to_text`
- `....core.postgres.FlatConcatSearchVector`
- `....core.tracing.traced_atomic_transaction`
- `....core.utils.events.call_event`
- `....core.utils.prepare_unique_slug`
- `....discount.utils.promotion.mark_active_catalogue_promotion_rules_as_dirty`
- `....order.events`
- `....order.lock_objects.order_lines_qs_select_for_update`
- `....order.models`
- `....order.tasks.recalculate_orders_task`
- `....permission.enums.ProductPermissions`
- `....permission.enums.ProductTypePermissions`
- `....product.ProductMediaTypes`
- `....product.error_codes.ProductBulkCreateErrorCode`
- `....product.error_codes.ProductErrorCode`
- `....product.error_codes.ProductVariantBulkErrorCode`
- `....product.models`
- `....product.models.CollectionProduct`
- `....product.models.ProductChannelListing`
- `....product.search.prepare_product_search_vector_value`
- `....product.tasks.fetch_product_media_image_task`
- `....product.utils.delete_categories`
- `....warehouse.error_codes.StockErrorCode`
- `....warehouse.management.delete_stocks`
- `....warehouse.management.stock_bulk_update`
- `....warehouse.models`
- `....warehouse.models.Warehouse`
- `....webhook.event_types.WebhookEventAsyncType`
- `....webhook.utils.get_webhooks_for_event`
- `...app.dataloaders.get_app_promise`
- `...attribute.types.AttributeValueInput`
- `...attribute.utils.attribute_assignment.AttributeAssignmentMixin`
- `...core.ResolveInfo`
- `...core.context.ChannelContext`
- `...core.descriptions.ADDED_IN_322`
- `...core.descriptions.DEPRECATED_IN_3X_INPUT`
- `...core.descriptions.RICH_CONTENT`
- `...core.doc_category.DOC_CATEGORY_PRODUCTS`
- `...core.enums.ErrorPolicyEnum`
- `...core.fields.JSONString`
- `...core.mutations.BaseMutation`
- `...core.mutations.DeprecatedModelMutation`
- `...core.mutations.ModelBulkDeleteMutation`
- `...core.scalars.Date`
- `...core.scalars.DateTime`
- `...core.scalars.PositiveDecimal`
- `...core.scalars.WeightScalar`
- `...core.types.BaseInputObjectType`
- `...core.types.BulkStockError`
- `...core.types.CollectionError`
- `...core.types.NonNullList`
- `...core.types.ProductError`
- `...core.types.ProductVariantBulkError`
- `...core.types.StockError`
- `...core.utils.WebhookEventInfo`
- `...core.utils.get_duplicated_values`
- `...core.validators.clean_seo_fields`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c4523784e443` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
