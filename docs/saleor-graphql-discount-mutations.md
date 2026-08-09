## Purpose

`saleor/graphql/discount/mutations` (`saleor/graphql/discount/mutations`) groups 3 source file(s) exposing 18 top-level declaration(s).

## Public surface

**`saleor/graphql/discount/mutations/bulk_mutations.py`**

- `SaleBulkDelete` (class) — [saleor/graphql/discount/mutations/bulk_mutations.py:31]
- `Arguments` (class) — [saleor/graphql/discount/mutations/bulk_mutations.py:32]
- `Meta` (class) — [saleor/graphql/discount/mutations/bulk_mutations.py:42]
- `perform_mutation` (function) — [saleor/graphql/discount/mutations/bulk_mutations.py:60]
- `get_promotion_instances` (function) — [saleor/graphql/discount/mutations/bulk_mutations.py:78]
- `bulk_action` (function) — [saleor/graphql/discount/mutations/bulk_mutations.py:96]
- `get_sale_and_rules` (function) — [saleor/graphql/discount/mutations/bulk_mutations.py:128]
- `get_catalogue_info` (function) — [saleor/graphql/discount/mutations/bulk_mutations.py:132]
- `get_channel_to_products_map` (function) — [saleor/graphql/discount/mutations/bulk_mutations.py:138]
- `get_sales` (function) — [saleor/graphql/discount/mutations/bulk_mutations.py:145]
- `VoucherBulkDelete` (class) — [saleor/graphql/discount/mutations/bulk_mutations.py:153]
- `Arguments` (class) — [saleor/graphql/discount/mutations/bulk_mutations.py:154]
- `Meta` (class) — [saleor/graphql/discount/mutations/bulk_mutations.py:164]
- `bulk_action` (function) — [saleor/graphql/discount/mutations/bulk_mutations.py:180]

**`saleor/graphql/discount/mutations/utils.py`**

- `convert_catalogue_info_to_global_ids` (function) — [saleor/graphql/discount/mutations/utils.py:19]
- `clear_promotion_old_sale_id` (function) — [saleor/graphql/discount/mutations/utils.py:32]
- `update_variants_for_promotion` (function) — [saleor/graphql/discount/mutations/utils.py:40]
- `promotion_rule_should_be_marked_with_dirty_variants` (function) — [saleor/graphql/discount/mutations/utils.py:58]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/discount/mutations/__init__.py` (43 lines)
- `saleor/graphql/discount/mutations/bulk_mutations.py` (192 lines)
- `saleor/graphql/discount/mutations/utils.py` (80 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....discount.PromotionType`
- `....discount.error_codes.DiscountErrorCode`
- `....discount.models`
- `....discount.models.Promotion`
- `....discount.models.PromotionRule`
- `....discount.models.VoucherCode`
- `....discount.utils.promotion.CatalogueInfo`
- `....discount.utils.promotion.update_rule_variant_relation`
- `....permission.enums.DiscountPermissions`
- `....product.models.ProductVariant`
- `....webhook.event_types.WebhookEventAsyncType`
- `....webhook.utils.get_webhooks_for_event`
- `...core.ResolveInfo`
- `...core.doc_category.DOC_CATEGORY_DISCOUNTS`
- `...core.mutations.ModelBulkDeleteMutation`
- `...core.types.DiscountError`
- `...core.types.NonNullList`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `..types.Sale`
- `..types.Voucher`
- `..utils.convert_migrated_sale_predicate_to_catalogue_info`
- `.promotion.promotion_bulk_delete.PromotionBulkDelete`
- `.promotion.promotion_create.PromotionCreate`
- `.promotion.promotion_delete.PromotionDelete`
- `.promotion.promotion_rule_create.PromotionRuleCreate`
- `.promotion.promotion_rule_delete.PromotionRuleDelete`
- `.promotion.promotion_rule_update.PromotionRuleUpdate`
- `.promotion.promotion_update.PromotionUpdate`
- `.sale.sale_add_catalogues.SaleAddCatalogues`
- `.sale.sale_channel_listing_update.SaleChannelListingUpdate`
- `.sale.sale_create.SaleCreate`
- `.sale.sale_delete.SaleDelete`
- `.sale.sale_remove_catalogues.SaleRemoveCatalogues`
- `.sale.sale_update.SaleUpdate`
- `.voucher.voucher_add_catalogues.VoucherAddCatalogues`
- `.voucher.voucher_channel_listing_update.VoucherChannelListingUpdate`
- `.voucher.voucher_code_bulk_delete.VoucherCodeBulkDelete`
- `.voucher.voucher_create.VoucherCreate`
- `.voucher.voucher_delete.VoucherDelete`
- `.voucher.voucher_remove_catalogues.VoucherRemoveCatalogues`
- `.voucher.voucher_update.VoucherUpdate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `3a89d9424396` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
