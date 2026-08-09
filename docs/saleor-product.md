## Purpose

`saleor/product` (`saleor/product`) groups 11 source file(s) exposing 108 top-level declaration(s).

## Public surface

**`saleor/product/__init__.py`**

- `ProductMediaTypes` (class) — [saleor/product/__init__.py:4]
- `ProductTypeKind` (class) — [saleor/product/__init__.py:14]

**`saleor/product/apps.py`**

- `ProductAppConfig` (class) — [saleor/product/apps.py:5]
- `ready` (function) — [saleor/product/apps.py:8]

**`saleor/product/error_codes.py`**

- `ProductErrorCode` (class) — [saleor/product/error_codes.py:4]
- `CollectionErrorCode` (class) — [saleor/product/error_codes.py:29]
- `ProductVariantBulkErrorCode` (class) — [saleor/product/error_codes.py:40]
- `ProductBulkCreateErrorCode` (class) — [saleor/product/error_codes.py:56]

**`saleor/product/interface.py`**

- `VariantDiscountedPriceChange` (class) — [saleor/product/interface.py:6]
- `pk` (function) — [saleor/product/interface.py:14]

**`saleor/product/lock_objects.py`**

- `product_qs_select_for_update` (function) — [saleor/product/lock_objects.py:6]

**`saleor/product/managers.py`**

- `ProductsQueryset` (class) — [saleor/product/managers.py:29]
- `published` (function) — [saleor/product/managers.py:30]
- `not_published` (function) — [saleor/product/managers.py:47]
- `published_with_variants` (function) — [saleor/product/managers.py:55]
- `visible_to_user` (function) — [saleor/product/managers.py:75]
- `annotate_publication_info` (function) — [saleor/product/managers.py:115]
- `annotate_is_published` (function) — [saleor/product/managers.py:118]
- `annotate_published_at` (function) — [saleor/product/managers.py:130]
- `annotate_visible_in_listings` (function) — [saleor/product/managers.py:142]
- `sort_by_attribute` (function) — [saleor/product/managers.py:158]
- `prefetched_for_webhook` (function) — [saleor/product/managers.py:239]
- `ProductVariantQueryset` (class) — [saleor/product/managers.py:258]
- `annotate_quantities` (function) — [saleor/product/managers.py:259]
- `available_in_channel` (function) — [saleor/product/managers.py:297]
- `prefetched_for_webhook` (function) — [saleor/product/managers.py:309]
- `visible_to_user` (function) — [saleor/product/managers.py:316]
- `ProductVariantChannelListingQuerySet` (class) — [saleor/product/managers.py:362]
- `annotate_preorder_quantity_allocated` (function) — [saleor/product/managers.py:363]
- `CollectionsQueryset` (class) — [saleor/product/managers.py:376]
- `published` (function) — [saleor/product/managers.py:377]
- `visible_to_user` (function) — [saleor/product/managers.py:387]

**`saleor/product/models.py`**

- `Category` (class) — [saleor/product/models.py:57]
- `Meta` (class) — [saleor/product/models.py:74]
- `CategoryTranslation` (class) — [saleor/product/models.py:90]
- `Meta` (class) — [saleor/product/models.py:97]
- `get_translated_object_id` (function) — [saleor/product/models.py:113]
- `get_translated_keys` (function) — [saleor/product/models.py:116]
- `ProductType` (class) — [saleor/product/models.py:127]
- `Meta` (class) — [saleor/product/models.py:150]
- `Product` (class) — [saleor/product/models.py:176]
- `Meta` (class) — [saleor/product/models.py:221]
- `get_first_image` (function) — [saleor/product/models.py:259]
- `sort_by_attribute_fields` (function) — [saleor/product/models.py:265]
- `ProductTranslation` (class) — [saleor/product/models.py:269]
- `Meta` (class) — [saleor/product/models.py:276]
- `get_translated_object_id` (function) — [saleor/product/models.py:292]
- `get_translated_keys` (function) — [saleor/product/models.py:295]
- `ProductChannelListing` (class) — [saleor/product/models.py:306]
- `Meta` (class) — [saleor/product/models.py:335]
- `is_available_for_purchase` (function) — [saleor/product/models.py:343]
- `ProductVariant` (class) — [saleor/product/models.py:350]
- `Meta` (class) — [saleor/product/models.py:378]
- `get_global_id` (function) — [saleor/product/models.py:393]
- `get_base_price` (function) — [saleor/product/models.py:396]
- `get_price` (function) — [saleor/product/models.py:408]
- `get_prior_price_amount` (function) — [saleor/product/models.py:429]
- `get_weight` (function) — [saleor/product/models.py:438]
- `is_shipping_required` (function) — [saleor/product/models.py:441]
- `is_gift_card` (function) — [saleor/product/models.py:444]
- `get_ordering_queryset` (function) — [saleor/product/models.py:447]
- `is_preorder_active` (function) — [saleor/product/models.py:450]
- `ProductVariantTranslation` (class) — [saleor/product/models.py:456]
- `Meta` (class) — [saleor/product/models.py:462]
- `get_translated_object_id` (function) — [saleor/product/models.py:472]
- `get_translated_keys` (function) — [saleor/product/models.py:475]
- `ProductVariantChannelListing` (class) — [saleor/product/models.py:479]
- `Meta` (class) — [saleor/product/models.py:541]
- `VariantChannelListingPromotionRule` (class) — [saleor/product/models.py:549]
- `Meta` (class) — [saleor/product/models.py:570]
- `ProductMedia` (class) — [saleor/product/models.py:574]
- `Meta` (class) — [saleor/product/models.py:597]
- _…and 15 more in this file_

**`saleor/product/product_images.py`**

- `get_product_image_thumbnail_url` (function) — [saleor/product/product_images.py:17]
- `get_product_image_placeholder` (function) — [saleor/product/product_images.py:30]

**`saleor/product/search.py`**

- `update_products_search_vector` (function) — [saleor/product/search.py:52]
- `prepare_product_search_vector_value` (function) — [saleor/product/search.py:77]
- `generate_variants_search_vector_value` (function) — [saleor/product/search.py:99]
- `generate_attributes_search_vector_value` (function) — [saleor/product/search.py:121]
- `generate_attributes_search_vector_value_with_assignment` (function) — [saleor/product/search.py:155]

**`saleor/product/signals.py`**

- `delete_background_image` (function) — [saleor/product/signals.py:4]
- `delete_product_media_image` (function) — [saleor/product/signals.py:9]

**`saleor/product/tasks.py`**

- `update_variants_names` (function) — [saleor/product/tasks.py:106]
- `update_products_discounted_prices_of_promotion_task` (function) — [saleor/product/tasks.py:123]
- `update_variant_relations_for_active_promotion_rules_task` (function) — [saleor/product/tasks.py:191]
- `update_products_discounted_prices_for_promotion_task` (function) — [saleor/product/tasks.py:239]
- `recalculate_discounted_price_for_products_task` (function) — [saleor/product/tasks.py:273]
- `update_discounted_prices_task` (function) — [saleor/product/tasks.py:309]
- `deactivate_preorder_for_variants_task` (function) — [saleor/product/tasks.py:321]
- `mark_products_search_vector_as_dirty` (function) — [saleor/product/tasks.py:339]
- `update_products_search_vector_task` (function) — [saleor/product/tasks.py:352]
- `collection_product_updated_task` (function) — [saleor/product/tasks.py:365]
- `on_failure_fetch_product_media_image_task` (function) — [saleor/product/tasks.py:387]
- `fetch_product_media_image_task` (function) — [saleor/product/tasks.py:411]

## How it works

The module's files, as provided to this run:

- `saleor/product/__init__.py` (21 lines)
- `saleor/product/managers.py` (401 lines)
- `saleor/product/tasks.py` (454 lines)
- `saleor/product/models.py` (728 lines)
- `saleor/product/apps.py` (30 lines)
- `saleor/product/error_codes.py` (72 lines)
- `saleor/product/interface.py` (20 lines)
- `saleor/product/lock_objects.py` (7 lines)
- `saleor/product/product_images.py` (33 lines)
- `saleor/product/search.py` (172 lines)
- `saleor/product/signals.py` (11 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/graphql/product/types`, `saleor/plugins/openid_connect`, `saleor/warehouse`
- Imported by: `saleor/product/tests`, `saleor/menu/migrations`, `saleor/menu`, `saleor/product/migrations`, `saleor`

Internal dependencies named in the source:

- `..account.models.User`
- `..app.models.App`
- `..attribute.models.AssignedProductAttributeValue`
- `..attribute.models.Attribute`
- `..attribute.models.AttributeValue`
- `..attribute.search.get_search_vectors_for_attribute_values`
- `..celeryconf.app`
- `..channel.models.Channel`
- `..core.db.connection.allow_writer`
- `..core.db.fields.MoneyField`
- `..core.db.fields.SanitizedJSONField`
- `..core.editorjs.clean_editorjs`
- `..core.exceptions.PreorderAllocationError`
- `..core.http_client.HTTPClient`
- `..core.postgres.FlatConcatSearchVector`
- `..core.postgres.NoValidationSearchVector`
- `..core.tasks.delete_from_storage_task`
- `..core.units.WeightUnits`
- `..core.utils.batches.queryset_in_batches`
- `..core.utils.events.call_event`
- `..core.utils.translations.Translation`
- `..core.utils.validators.get_mime_type`
- `..core.weight.zero_weight`
- `..discount.PromotionType`
- `..discount.models.Promotion`
- `..discount.models.PromotionRule`
- `..discount.utils.promotion.calculate_discounted_price_for_rules`
- `..page.models.Page`
- `..permission.utils.has_one_of_permissions`
- `..plugins.manager.get_plugins_manager`
- `..product.ProductMediaTypes`
- `..product.models.Product`
- `..seo.models.SeoModel`
- `..seo.models.SeoModelTranslationWithSlug`
- `..tax.models.TaxClass`
- `..thumbnail.models.Thumbnail`
- `..thumbnail.utils.get_image_or_proxy_url`
- `..thumbnail.utils.get_thumbnail_size`
- `..warehouse.management.deactivate_preorder_for_variant`
- `..webhook.event_types.WebhookEventAsyncType`
- `..webhook.utils.get_webhooks_for_event`
- `.interface.VariantDiscountedPriceChange`
- `.lock_objects.product_qs_select_for_update`
- `.models.ALL_PRODUCTS_PERMISSIONS`
- `.models.Category`
- `.models.Collection`
- `.models.Product`
- `.models.ProductChannelListing`
- `.models.ProductMedia`
- `.models.ProductVariant`
- `.models.ProductVariantChannelListing`
- `.search.update_products_search_vector`
- `.utils.product.mark_products_in_channels_as_dirty`
- `.utils.variant_prices.update_discounted_prices_for_promotion`
- `saleor.warehouse.models.Allocation`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `55f2ddbb4c9c` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
