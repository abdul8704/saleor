## Purpose

`saleor/graphql/discount` (`saleor/graphql/discount`) groups 9 source file(s) exposing 146 top-level declaration(s).

## Public surface

**`saleor/graphql/discount/dataloaders.py`**

- `VoucherByIdLoader` (class) — [saleor/graphql/discount/dataloaders.py:31]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:34]
- `VoucherCodeByCodeLoader` (class) — [saleor/graphql/discount/dataloaders.py:39]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:42]
- `CodeByVoucherIDLoader` (class) — [saleor/graphql/discount/dataloaders.py:54]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:62]
- `UsedByVoucherIDLoader` (class) — [saleor/graphql/discount/dataloaders.py:72]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:80]
- `VoucherByCodeLoader` (class) — [saleor/graphql/discount/dataloaders.py:92]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:95]
- `with_voucher_codes` (function) — [saleor/graphql/discount/dataloaders.py:96]
- `VoucherChannelListingByVoucherIdAndChannelSlugLoader` (class) — [saleor/graphql/discount/dataloaders.py:117]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:122]
- `VoucherChannelListingsByVoucherIdLoader` (class) — [saleor/graphql/discount/dataloaders.py:145]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:150]
- `VoucherInfoByVoucherCodeLoader` (class) — [saleor/graphql/discount/dataloaders.py:164]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:167]
- `OrderDiscountsByOrderIDLoader` (class) — [saleor/graphql/discount/dataloaders.py:232]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:235]
- `OrderLineDiscountsByOrderLineIDLoader` (class) — [saleor/graphql/discount/dataloaders.py:245]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:248]
- `CheckoutLineDiscountsByCheckoutLineIdLoader` (class) — [saleor/graphql/discount/dataloaders.py:258]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:263]
- `CheckoutDiscountByCheckoutIdLoader` (class) — [saleor/graphql/discount/dataloaders.py:273]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:276]
- `PromotionRulesByPromotionIdLoader` (class) — [saleor/graphql/discount/dataloaders.py:288]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:291]
- `PromotionEventsByPromotionIdLoader` (class) — [saleor/graphql/discount/dataloaders.py:304]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:307]
- `PromotionByIdLoader` (class) — [saleor/graphql/discount/dataloaders.py:320]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:323]
- `ChannelsByPromotionRuleIdLoader` (class) — [saleor/graphql/discount/dataloaders.py:330]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:333]
- `PromotionRuleByIdLoader` (class) — [saleor/graphql/discount/dataloaders.py:351]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:354]
- `PromotionByRuleIdLoader` (class) — [saleor/graphql/discount/dataloaders.py:359]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:362]
- `SaleChannelListingByPromotionIdLoader` (class) — [saleor/graphql/discount/dataloaders.py:375]
- `batch_load` (function) — [saleor/graphql/discount/dataloaders.py:380]
- `with_rules` (function) — [saleor/graphql/discount/dataloaders.py:383]
- _…and 9 more in this file_

**`saleor/graphql/discount/enums.py`**

- `SaleType` (class) — [saleor/graphql/discount/enums.py:58]
- `Meta` (class) — [saleor/graphql/discount/enums.py:62]
- `DiscountValueTypeEnum` (class) — [saleor/graphql/discount/enums.py:66]
- `Meta` (class) — [saleor/graphql/discount/enums.py:70]
- `VoucherTypeEnum` (class) — [saleor/graphql/discount/enums.py:74]
- `Meta` (class) — [saleor/graphql/discount/enums.py:79]
- `DiscountStatusEnum` (class) — [saleor/graphql/discount/enums.py:83]
- `Meta` (class) — [saleor/graphql/discount/enums.py:88]
- `VoucherDiscountType` (class) — [saleor/graphql/discount/enums.py:92]
- `Meta` (class) — [saleor/graphql/discount/enums.py:97]

**`saleor/graphql/discount/filters.py`**

- `filter_status` (function) — [saleor/graphql/discount/filters.py:56]
- `filter_times_used` (function) — [saleor/graphql/discount/filters.py:72]
- `filter_discount_type` (function) — [saleor/graphql/discount/filters.py:77]
- `filter_started` (function) — [saleor/graphql/discount/filters.py:96]
- `filter_sale_type` (function) — [saleor/graphql/discount/filters.py:100]
- `filter_sale_search` (function) — [saleor/graphql/discount/filters.py:107]
- `filter_voucher_search` (function) — [saleor/graphql/discount/filters.py:118]
- `filter_updated_at_range` (function) — [saleor/graphql/discount/filters.py:131]
- `VoucherFilter` (class) — [saleor/graphql/discount/filters.py:135]
- `Meta` (class) — [saleor/graphql/discount/filters.py:146]
- `SaleFilter` (class) — [saleor/graphql/discount/filters.py:151]
- `Meta` (class) — [saleor/graphql/discount/filters.py:162]
- `PromotionTypeEnumFilterInput` (class) — [saleor/graphql/discount/filters.py:167]
- `Meta` (class) — [saleor/graphql/discount/filters.py:175]
- `PromotionWhere` (class) — [saleor/graphql/discount/filters.py:179]
- `filter_promotion_name` (function) — [saleor/graphql/discount/filters.py:202]
- `filter_end_date_range` (function) — [saleor/graphql/discount/filters.py:206]
- `filter_start_date_range` (function) — [saleor/graphql/discount/filters.py:210]
- `filter_is_old_sale` (function) — [saleor/graphql/discount/filters.py:214]
- `filter_type` (function) — [saleor/graphql/discount/filters.py:218]
- `PromotionWhereInput` (class) — [saleor/graphql/discount/filters.py:222]
- `Meta` (class) — [saleor/graphql/discount/filters.py:223]
- `DiscountedObjectWhere` (class) — [saleor/graphql/discount/filters.py:228]
- `Meta` (class) — [saleor/graphql/discount/filters.py:240]
- `DiscountedObjectWhereInput` (class) — [saleor/graphql/discount/filters.py:244]
- `Meta` (class) — [saleor/graphql/discount/filters.py:245]

**`saleor/graphql/discount/inputs.py`**

- `PredicateInputObjectType` (class) — [saleor/graphql/discount/inputs.py:15]
- `Meta` (class) — [saleor/graphql/discount/inputs.py:22]
- `CataloguePredicateInput` (class) — [saleor/graphql/discount/inputs.py:48]
- `Meta` (class) — [saleor/graphql/discount/inputs.py:62]
- `OrderPredicateInput` (class) — [saleor/graphql/discount/inputs.py:66]
- `Meta` (class) — [saleor/graphql/discount/inputs.py:72]
- `PromotionRuleBaseInput` (class) — [saleor/graphql/discount/inputs.py:76]

**`saleor/graphql/discount/resolvers.py`**

- `resolve_voucher` (function) — [saleor/graphql/discount/resolvers.py:13]
- `resolve_vouchers` (function) — [saleor/graphql/discount/resolvers.py:22]
- `resolve_sale` (function) — [saleor/graphql/discount/resolvers.py:34]
- `resolve_sales` (function) — [saleor/graphql/discount/resolvers.py:43]
- `resolve_promotion` (function) — [saleor/graphql/discount/resolvers.py:65]
- `resolve_promotions` (function) — [saleor/graphql/discount/resolvers.py:73]

**`saleor/graphql/discount/schema.py`**

- `VoucherFilterInput` (class) — [saleor/graphql/discount/schema.py:62]
- `Meta` (class) — [saleor/graphql/discount/schema.py:63]
- `SaleFilterInput` (class) — [saleor/graphql/discount/schema.py:68]
- `Meta` (class) — [saleor/graphql/discount/schema.py:69]
- `DiscountQueries` (class) — [saleor/graphql/discount/schema.py:74]
- `resolve_sale` (function) — [saleor/graphql/discount/schema.py:164]
- `resolve_sales` (function) — [saleor/graphql/discount/schema.py:169]
- `resolve_voucher` (function) — [saleor/graphql/discount/schema.py:178]
- `resolve_vouchers` (function) — [saleor/graphql/discount/schema.py:183]
- `resolve_promotion` (function) — [saleor/graphql/discount/schema.py:192]
- `resolve_promotions` (function) — [saleor/graphql/discount/schema.py:197]
- `DiscountMutations` (class) — [saleor/graphql/discount/schema.py:205]

**`saleor/graphql/discount/sorters.py`**

- `SaleSortField` (class) — [saleor/graphql/discount/sorters.py:13]
- `Meta` (class) — [saleor/graphql/discount/sorters.py:22]
- `description` (function) — [saleor/graphql/discount/sorters.py:26]
- `qs_with_value` (function) — [saleor/graphql/discount/sorters.py:41]
- `qs_with_type` (function) — [saleor/graphql/discount/sorters.py:50]
- `SaleSortingInput` (class) — [saleor/graphql/discount/sorters.py:54]
- `Meta` (class) — [saleor/graphql/discount/sorters.py:55]
- `VoucherSortField` (class) — [saleor/graphql/discount/sorters.py:61]
- `Meta` (class) — [saleor/graphql/discount/sorters.py:71]
- `description` (function) — [saleor/graphql/discount/sorters.py:75]
- `deprecation_reason` (function) — [saleor/graphql/discount/sorters.py:89]
- `qs_with_minimum_spent_amount` (function) — [saleor/graphql/discount/sorters.py:98]
- `qs_with_value` (function) — [saleor/graphql/discount/sorters.py:107]
- `qs_with_code` (function) — [saleor/graphql/discount/sorters.py:116]
- `VoucherSortingInput` (class) — [saleor/graphql/discount/sorters.py:127]
- `Meta` (class) — [saleor/graphql/discount/sorters.py:128]
- `PromotionSortField` (class) — [saleor/graphql/discount/sorters.py:134]
- `Meta` (class) — [saleor/graphql/discount/sorters.py:140]
- `description` (function) — [saleor/graphql/discount/sorters.py:144]
- `PromotionSortingInput` (class) — [saleor/graphql/discount/sorters.py:156]
- `Meta` (class) — [saleor/graphql/discount/sorters.py:157]

**`saleor/graphql/discount/utils.py`**

- `PredicateObjectType` (class) — [saleor/graphql/discount/utils.py:34]
- `Operators` (class) — [saleor/graphql/discount/utils.py:40]
- `get_products_for_promotion` (function) — [saleor/graphql/discount/utils.py:45]
- `get_products_for_rule` (function) — [saleor/graphql/discount/utils.py:55]
- `get_variants_for_promotion` (function) — [saleor/graphql/discount/utils.py:65]
- `get_variants_for_catalogue_predicate` (function) — [saleor/graphql/discount/utils.py:168]
- `filter_qs_by_predicate` (function) — [saleor/graphql/discount/utils.py:180]
- `contains_filter_operator` (function) — [saleor/graphql/discount/utils.py:269]
- `convert_migrated_sale_predicate_to_model_ids` (function) — [saleor/graphql/discount/utils.py:374]
- `convert_migrated_sale_predicate_to_catalogue_info` (function) — [saleor/graphql/discount/utils.py:413]
- `convert_catalogue_info_into_predicate` (function) — [saleor/graphql/discount/utils.py:449]
- `get_categories_from_predicate` (function) — [saleor/graphql/discount/utils.py:468]
- `merge_catalogues_info` (function) — [saleor/graphql/discount/utils.py:474]
- `subtract_catalogues_info` (function) — [saleor/graphql/discount/utils.py:485]
- `create_catalogue_predicate` (function) — [saleor/graphql/discount/utils.py:496]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/discount/__init__.py` (1 lines)
- `saleor/graphql/discount/dataloaders.py` (504 lines)
- `saleor/graphql/discount/enums.py` (98 lines)
- `saleor/graphql/discount/filters.py` (247 lines)
- `saleor/graphql/discount/inputs.py` (105 lines)
- `saleor/graphql/discount/resolvers.py` (76 lines)
- `saleor/graphql/discount/schema.py` (247 lines)
- `saleor/graphql/discount/sorters.py` (160 lines)
- `saleor/graphql/discount/utils.py` (509 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/graphql`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...channel.models.Channel`
- `...checkout.models.Checkout`
- `...discount.DiscountValueType`
- `...discount.interface.VoucherInfo`
- `...discount.models`
- `...discount.models.Promotion`
- `...discount.models.PromotionRule`
- `...discount.models.VoucherCode`
- `...discount.utils.promotion.update_rule_variant_relation`
- `...order.models.Order`
- `...permission.enums.DiscountPermissions`
- `...product.managers.ProductVariantQueryset`
- `...product.managers.ProductsQueryset`
- `...product.models.ProductVariant`
- `..channel.dataloaders.by_self.ChannelBySlugLoader`
- `..checkout.filters.CheckoutDiscountedObjectWhere`
- `..core.ResolveInfo`
- `..core.connection.create_connection_slice`
- `..core.connection.filter_connection_queryset`
- `..core.connection.where_filter_qs`
- `..core.dataloaders.DataLoader`
- `..core.descriptions.PREVIEW_FEATURE`
- `..core.doc_category.DOC_CATEGORY_DISCOUNTS`
- `..core.enums.to_enum`
- `..core.fields.FilterConnectionField`
- `..core.fields.PermissionsField`
- `..core.filters.FilterInputObjectType`
- `..core.scalars.JSON`
- `..core.scalars.PositiveDecimal`
- `..core.types.BaseEnum`
- `..core.types.BaseInputObjectType`
- `..core.types.ChannelSortInputObjectType`
- `..core.types.NonNullList`
- `..core.types.SortInputObjectType`
- `..core.utils.from_global_id_or_error`
- `..discount.filters.DiscountedObjectWhereInput`
- `..order.filters.OrderDiscountedObjectWhere`
- `..product.filters.category.CategoryWhere`
- `..product.filters.category.CategoryWhereInput`
- `..product.filters.collection.CollectionWhere`
- `..product.filters.collection.CollectionWhereInput`
- `..product.filters.product.ProductWhere`
- `..product.filters.product.ProductWhereInput`
- `..product.filters.product_variant.ProductVariantWhere`
- `..product.filters.product_variant.ProductVariantWhereInput`
- `.enums.RewardTypeEnum`
- `.enums.RewardValueTypeEnum`
- `.filters.PromotionWhereInput`
- `.filters.SaleFilter`
- `.filters.VoucherFilter`
- `.filters.filter_sale_search`
- `.filters.filter_voucher_search`
- `.mutations.bulk_mutations.SaleBulkDelete`
- `.mutations.bulk_mutations.VoucherBulkDelete`
- `.sorters.PromotionSortingInput`
- `.sorters.SaleSortingInput`
- `.sorters.VoucherSortingInput`
- `.types.promotions.PromotionCountableConnection`
- `.types.sales.SaleChannelListing`
- `.utils.convert_migrated_sale_predicate_to_model_ids`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `f4d5a4d7fe56` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
