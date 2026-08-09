## Purpose

`saleor/graphql/discount/mutations/voucher` (`saleor/graphql/discount/mutations/voucher`) groups 8 source file(s) exposing 64 top-level declaration(s).

## Public surface

**`saleor/graphql/discount/mutations/voucher/voucher_add_catalogues.py`**

- `CatalogueInput` (class) — [saleor/graphql/discount/mutations/voucher/voucher_add_catalogues.py:19]
- `Meta` (class) — [saleor/graphql/discount/mutations/voucher/voucher_add_catalogues.py:39]
- `VoucherBaseCatalogueMutation` (class) — [saleor/graphql/discount/mutations/voucher/voucher_add_catalogues.py:43]
- `Arguments` (class) — [saleor/graphql/discount/mutations/voucher/voucher_add_catalogues.py:48]
- `Meta` (class) — [saleor/graphql/discount/mutations/voucher/voucher_add_catalogues.py:55]
- `mutate` (function) — [saleor/graphql/discount/mutations/voucher/voucher_add_catalogues.py:59]
- `clean_product` (function) — [saleor/graphql/discount/mutations/voucher/voucher_add_catalogues.py:66]
- `VoucherAddCatalogues` (class) — [saleor/graphql/discount/mutations/voucher/voucher_add_catalogues.py:81]
- `Meta` (class) — [saleor/graphql/discount/mutations/voucher/voucher_add_catalogues.py:82]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/voucher/voucher_add_catalogues.py:96]
- `add_catalogues_to_node` (function) — [saleor/graphql/discount/mutations/voucher/voucher_add_catalogues.py:111]

**`saleor/graphql/discount/mutations/voucher/voucher_channel_listing_update.py`**

- `VoucherChannelListingAddInput` (class) — [saleor/graphql/discount/mutations/voucher/voucher_channel_listing_update.py:23]
- `Meta` (class) — [saleor/graphql/discount/mutations/voucher/voucher_channel_listing_update.py:30]
- `VoucherChannelListingInput` (class) — [saleor/graphql/discount/mutations/voucher/voucher_channel_listing_update.py:34]
- `Meta` (class) — [saleor/graphql/discount/mutations/voucher/voucher_channel_listing_update.py:46]
- `VoucherChannelListingUpdate` (class) — [saleor/graphql/discount/mutations/voucher/voucher_channel_listing_update.py:50]
- `Arguments` (class) — [saleor/graphql/discount/mutations/voucher/voucher_channel_listing_update.py:53]
- `Meta` (class) — [saleor/graphql/discount/mutations/voucher/voucher_channel_listing_update.py:60]
- `clean_discount_values_per_channel` (function) — [saleor/graphql/discount/mutations/voucher/voucher_channel_listing_update.py:74]
- `clean_discount_values` (function) — [saleor/graphql/discount/mutations/voucher/voucher_channel_listing_update.py:117]
- `add_channels` (function) — [saleor/graphql/discount/mutations/voucher/voucher_channel_listing_update.py:181]
- `remove_channels` (function) — [saleor/graphql/discount/mutations/voucher/voucher_channel_listing_update.py:196]
- `save` (function) — [saleor/graphql/discount/mutations/voucher/voucher_channel_listing_update.py:200]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/voucher/voucher_channel_listing_update.py:206]

**`saleor/graphql/discount/mutations/voucher/voucher_code_bulk_delete.py`**

- `VoucherCodeBulkDelete` (class) — [saleor/graphql/discount/mutations/voucher/voucher_code_bulk_delete.py:16]
- `Arguments` (class) — [saleor/graphql/discount/mutations/voucher/voucher_code_bulk_delete.py:21]
- `Meta` (class) — [saleor/graphql/discount/mutations/voucher/voucher_code_bulk_delete.py:28]
- `clean_codes` (function) — [saleor/graphql/discount/mutations/voucher/voucher_code_bulk_delete.py:43]
- `post_save_actions` (function) — [saleor/graphql/discount/mutations/voucher/voucher_code_bulk_delete.py:67]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/voucher/voucher_code_bulk_delete.py:76]

**`saleor/graphql/discount/mutations/voucher/voucher_create.py`**

- `VoucherInput` (class) — [saleor/graphql/discount/mutations/voucher/voucher_create.py:31]
- `Meta` (class) — [saleor/graphql/discount/mutations/voucher/voucher_create.py:98]
- `VoucherCreate` (class) — [saleor/graphql/discount/mutations/voucher/voucher_create.py:102]
- `Arguments` (class) — [saleor/graphql/discount/mutations/voucher/voucher_create.py:103]
- `Meta` (class) — [saleor/graphql/discount/mutations/voucher/voucher_create.py:108]
- `clean_input` (function) — [saleor/graphql/discount/mutations/voucher/voucher_create.py:127]
- `clean_codes` (function) — [saleor/graphql/discount/mutations/voucher/voucher_create.py:192]
- `construct_codes_instances` (function) — [saleor/graphql/discount/mutations/voucher/voucher_create.py:209]
- `clean_voucher_instance` (function) — [saleor/graphql/discount/mutations/voucher/voucher_create.py:232]
- `clean_codes_instance` (function) — [saleor/graphql/discount/mutations/voucher/voucher_create.py:245]
- `save` (function) — [saleor/graphql/discount/mutations/voucher/voucher_create.py:250]
- `post_save_action` (function) — [saleor/graphql/discount/mutations/voucher/voucher_create.py:258]
- `success_response` (function) — [saleor/graphql/discount/mutations/voucher/voucher_create.py:272]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/voucher/voucher_create.py:277]

**`saleor/graphql/discount/mutations/voucher/voucher_delete.py`**

- `VoucherDelete` (class) — [saleor/graphql/discount/mutations/voucher/voucher_delete.py:16]
- `Arguments` (class) — [saleor/graphql/discount/mutations/voucher/voucher_delete.py:17]
- `Meta` (class) — [saleor/graphql/discount/mutations/voucher/voucher_delete.py:20]
- `success_response` (function) — [saleor/graphql/discount/mutations/voucher/voucher_delete.py:35]
- `post_save_action` (function) — [saleor/graphql/discount/mutations/voucher/voucher_delete.py:41]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/voucher/voucher_delete.py:46]

**`saleor/graphql/discount/mutations/voucher/voucher_remove_catalogues.py`**

- `VoucherRemoveCatalogues` (class) — [saleor/graphql/discount/mutations/voucher/voucher_remove_catalogues.py:13]
- `Meta` (class) — [saleor/graphql/discount/mutations/voucher/voucher_remove_catalogues.py:14]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/voucher/voucher_remove_catalogues.py:28]
- `remove_catalogues_from_node` (function) — [saleor/graphql/discount/mutations/voucher/voucher_remove_catalogues.py:43]

**`saleor/graphql/discount/mutations/voucher/voucher_update.py`**

- `VoucherUpdate` (class) — [saleor/graphql/discount/mutations/voucher/voucher_update.py:20]
- `Arguments` (class) — [saleor/graphql/discount/mutations/voucher/voucher_update.py:21]
- `Meta` (class) — [saleor/graphql/discount/mutations/voucher/voucher_update.py:27]
- `clean_input` (function) — [saleor/graphql/discount/mutations/voucher/voucher_update.py:46]
- `clean_codes` (function) — [saleor/graphql/discount/mutations/voucher/voucher_update.py:54]
- `clean_voucher_usage_setting` (function) — [saleor/graphql/discount/mutations/voucher/voucher_update.py:62]
- `is_voucher_used` (function) — [saleor/graphql/discount/mutations/voucher/voucher_update.py:92]
- `construct_codes_instances` (function) — [saleor/graphql/discount/mutations/voucher/voucher_update.py:112]
- `save` (function) — [saleor/graphql/discount/mutations/voucher/voucher_update.py:141]
- `post_save_action` (function) — [saleor/graphql/discount/mutations/voucher/voucher_update.py:158]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/discount/mutations/voucher/__init__.py` (1 lines)
- `saleor/graphql/discount/mutations/voucher/voucher_add_catalogues.py` (128 lines)
- `saleor/graphql/discount/mutations/voucher/voucher_channel_listing_update.py` (226 lines)
- `saleor/graphql/discount/mutations/voucher/voucher_code_bulk_delete.py` (100 lines)
- `saleor/graphql/discount/mutations/voucher/voucher_create.py` (316 lines)
- `saleor/graphql/discount/mutations/voucher/voucher_delete.py` (62 lines)
- `saleor/graphql/discount/mutations/voucher/voucher_remove_catalogues.py` (60 lines)
- `saleor/graphql/discount/mutations/voucher/voucher_update.py` (166 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....checkout.models`
- `.....core.tracing.traced_atomic_transaction`
- `.....core.utils.promo_code.generate_promo_code`
- `.....core.utils.promo_code.is_available_promo_code`
- `.....discount.DiscountValueType`
- `.....discount.error_codes.DiscountErrorCode`
- `.....discount.models`
- `.....order.models`
- `.....permission.enums.DiscountPermissions`
- `.....product.utils.get_products_ids_without_variants`
- `.....webhook.event_types.WebhookEventAsyncType`
- `....channel.mutations.BaseChannelListingMutation`
- `....core.ResolveInfo`
- `....core.context.ChannelContext`
- `....core.doc_category.DOC_CATEGORY_DISCOUNTS`
- `....core.enums.VoucherCodeBulkDeleteErrorCode`
- `....core.mutations.BaseMutation`
- `....core.mutations.DeprecatedModelMutation`
- `....core.mutations.ModelDeleteMutation`
- `....core.scalars.DateTime`
- `....core.scalars.PositiveDecimal`
- `....core.types.BaseInputObjectType`
- `....core.types.DiscountError`
- `....core.types.NonNullList`
- `....core.types.VoucherCodeBulkDeleteError`
- `....core.utils.WebhookEventInfo`
- `....core.utils.get_duplicated_values`
- `....core.validators.validate_price_precision`
- `....meta.inputs.MetadataInput`
- `....plugins.dataloaders.get_plugin_manager_promise`
- `....product.types.Category`
- `....product.types.Collection`
- `....product.types.Product`
- `....product.types.ProductVariant`
- `...enums.DiscountValueTypeEnum`
- `...enums.VoucherTypeEnum`
- `...types.Voucher`
- `...types.VoucherCode`
- `.voucher_add_catalogues.VoucherBaseCatalogueMutation`
- `.voucher_create.VoucherCreate`
- `.voucher_create.VoucherInput`
- `saleor.discount.models`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `85fd2ee7ade3` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
