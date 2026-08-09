## Purpose

`saleor/graphql/discount/mutations/sale` (`saleor/graphql/discount/mutations/sale`) groups 8 source file(s) exposing 61 top-level declaration(s).

## Public surface

**`saleor/graphql/discount/mutations/sale/sale_add_catalogues.py`**

- `SaleAddCatalogues` (class) — [saleor/graphql/discount/mutations/sale/sale_add_catalogues.py:24]
- `Meta` (class) — [saleor/graphql/discount/mutations/sale/sale_add_catalogues.py:25]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/sale/sale_add_catalogues.py:39]
- `get_instance` (function) — [saleor/graphql/discount/mutations/sale/sale_add_catalogues.py:63]
- `add_items_to_catalogue` (function) — [saleor/graphql/discount/mutations/sale/sale_add_catalogues.py:83]

**`saleor/graphql/discount/mutations/sale/sale_base_catalogue.py`**

- `SaleBaseCatalogueMutation` (class) — [saleor/graphql/discount/mutations/sale/sale_base_catalogue.py:26]
- `Arguments` (class) — [saleor/graphql/discount/mutations/sale/sale_base_catalogue.py:31]
- `Meta` (class) — [saleor/graphql/discount/mutations/sale/sale_base_catalogue.py:38]
- `post_save_actions` (function) — [saleor/graphql/discount/mutations/sale/sale_base_catalogue.py:42]
- `get_product_ids_for_predicate` (function) — [saleor/graphql/discount/mutations/sale/sale_base_catalogue.py:83]
- `get_catalogue_info_from_input` (function) — [saleor/graphql/discount/mutations/sale/sale_base_catalogue.py:91]
- `clean_product` (function) — [saleor/graphql/discount/mutations/sale/sale_base_catalogue.py:111]

**`saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py`**

- `SaleChannelListingAddInput` (class) — [saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py:33]
- `Meta` (class) — [saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py:39]
- `SaleChannelListingInput` (class) — [saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py:43]
- `Meta` (class) — [saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py:55]
- `SaleChannelListingUpdate` (class) — [saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py:59]
- `Arguments` (class) — [saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py:62]
- `Meta` (class) — [saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py:69]
- `add_channels` (function) — [saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py:77]
- `save_promotion_rules` (function) — [saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py:117]
- `get_channe_id_to_rule_map` (function) — [saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py:131]
- `remove_channels` (function) — [saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py:148]
- `clean_discount_values` (function) — [saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py:167]
- `save` (function) — [saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py:214]
- `get_instance` (function) — [saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py:241]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py:253]

**`saleor/graphql/discount/mutations/sale/sale_create.py`**

- `SaleInput` (class) — [saleor/graphql/discount/mutations/sale/sale_create.py:30]
- `Meta` (class) — [saleor/graphql/discount/mutations/sale/sale_create.py:55]
- `SaleCreate` (class) — [saleor/graphql/discount/mutations/sale/sale_create.py:59]
- `Arguments` (class) — [saleor/graphql/discount/mutations/sale/sale_create.py:60]
- `Meta` (class) — [saleor/graphql/discount/mutations/sale/sale_create.py:65]
- `create_predicate` (function) — [saleor/graphql/discount/mutations/sale/sale_create.py:82]
- `success_response` (function) — [saleor/graphql/discount/mutations/sale/sale_create.py:91]
- `clean_instance` (function) — [saleor/graphql/discount/mutations/sale/sale_create.py:97]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/sale/sale_create.py:108]
- `send_sale_notifications` (function) — [saleor/graphql/discount/mutations/sale/sale_create.py:129]
- `send_sale_toggle_notification` (function) — [saleor/graphql/discount/mutations/sale/sale_create.py:135]

**`saleor/graphql/discount/mutations/sale/sale_delete.py`**

- `SaleDelete` (class) — [saleor/graphql/discount/mutations/sale/sale_delete.py:28]
- `Arguments` (class) — [saleor/graphql/discount/mutations/sale/sale_delete.py:29]
- `Meta` (class) — [saleor/graphql/discount/mutations/sale/sale_delete.py:32]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/sale/sale_delete.py:49]
- `get_promotion_instance` (function) — [saleor/graphql/discount/mutations/sale/sale_delete.py:83]
- `get_product_ids` (function) — [saleor/graphql/discount/mutations/sale/sale_delete.py:103]
- `get_catalogue_info` (function) — [saleor/graphql/discount/mutations/sale/sale_delete.py:108]

**`saleor/graphql/discount/mutations/sale/sale_remove_catalogues.py`**

- `SaleRemoveCatalogues` (class) — [saleor/graphql/discount/mutations/sale/sale_remove_catalogues.py:24]
- `Meta` (class) — [saleor/graphql/discount/mutations/sale/sale_remove_catalogues.py:25]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/sale/sale_remove_catalogues.py:39]
- `get_instance` (function) — [saleor/graphql/discount/mutations/sale/sale_remove_catalogues.py:65]
- `remove_items_from_catalogue` (function) — [saleor/graphql/discount/mutations/sale/sale_remove_catalogues.py:85]

**`saleor/graphql/discount/mutations/sale/sale_update.py`**

- `SaleUpdate` (class) — [saleor/graphql/discount/mutations/sale/sale_update.py:38]
- `Arguments` (class) — [saleor/graphql/discount/mutations/sale/sale_update.py:39]
- `Meta` (class) — [saleor/graphql/discount/mutations/sale/sale_update.py:45]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/sale/sale_update.py:66]
- `get_instance` (function) — [saleor/graphql/discount/mutations/sale/sale_update.py:98]
- `validate_dates` (function) — [saleor/graphql/discount/mutations/sale/sale_update.py:118]
- `update_fields` (function) — [saleor/graphql/discount/mutations/sale/sale_update.py:128]
- `create_predicate` (function) — [saleor/graphql/discount/mutations/sale/sale_update.py:150]
- `post_save_actions` (function) — [saleor/graphql/discount/mutations/sale/sale_update.py:159]
- `send_sale_notifications` (function) — [saleor/graphql/discount/mutations/sale/sale_update.py:202]
- `send_sale_toggle_notification` (function) — [saleor/graphql/discount/mutations/sale/sale_update.py:223]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/discount/mutations/sale/__init__.py` (1 lines)
- `saleor/graphql/discount/mutations/sale/sale_add_catalogues.py` (97 lines)
- `saleor/graphql/discount/mutations/sale/sale_base_catalogue.py` (123 lines)
- `saleor/graphql/discount/mutations/sale/sale_channel_listing_update.py` (280 lines)
- `saleor/graphql/discount/mutations/sale/sale_create.py` (149 lines)
- `saleor/graphql/discount/mutations/sale/sale_delete.py` (111 lines)
- `saleor/graphql/discount/mutations/sale/sale_remove_catalogues.py` (102 lines)
- `saleor/graphql/discount/mutations/sale/sale_update.py` (258 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....channel.models.Channel`
- `.....core.tracing.traced_atomic_transaction`
- `.....discount.DiscountValueType`
- `.....discount.PromotionType`
- `.....discount.error_codes.DiscountErrorCode`
- `.....discount.models`
- `.....discount.models.Promotion`
- `.....discount.models.PromotionRule`
- `.....discount.utils.promotion.CATALOGUE_FIELDS`
- `.....discount.utils.promotion.mark_catalogue_promotion_rules_as_dirty`
- `.....graphql.core.context.ChannelContext`
- `.....graphql.core.mutations.ModelDeleteMutation`
- `.....permission.enums.DiscountPermissions`
- `.....product.models`
- `.....product.utils.get_products_ids_without_variants`
- `.....product.utils.product.mark_products_in_channels_as_dirty`
- `.....webhook.event_types.WebhookEventAsyncType`
- `....channel.mutations.BaseChannelListingMutation`
- `....core.ResolveInfo`
- `....core.context.ChannelContext`
- `....core.doc_category.DOC_CATEGORY_DISCOUNTS`
- `....core.mutations.BaseMutation`
- `....core.mutations.DeprecatedModelMutation`
- `....core.scalars.DateTime`
- `....core.scalars.PositiveDecimal`
- `....core.types.BaseInputObjectType`
- `....core.types.DiscountError`
- `....core.types.NonNullList`
- `....core.utils.WebhookEventInfo`
- `....core.utils.raise_validation_error`
- `....core.validators.validate_end_is_after_start`
- `....core.validators.validate_price_precision`
- `....discount.types.Sale`
- `....plugins.dataloaders.get_plugin_manager_promise`
- `....product.types.Category`
- `....product.types.Collection`
- `....product.types.Product`
- `....product.types.ProductVariant`
- `...enums.DiscountValueTypeEnum`
- `...types.Sale`
- `...utils.get_products_for_rule`
- `..utils.update_variants_for_promotion`
- `..voucher.voucher_add_catalogues.CatalogueInput`
- `.sale_base_catalogue.SaleBaseCatalogueMutation`
- `.sale_create.SaleInput`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `a1ce778047c2` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
