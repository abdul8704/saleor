## Purpose

`saleor/graphql/discount/types` (`saleor/graphql/discount/types`) groups 6 source file(s) exposing 89 top-level declaration(s).

## Public surface

**`saleor/graphql/discount/types/discounts.py`**

- `BaseOrderDiscount` (class) — [saleor/graphql/discount/types/discounts.py:21]
- `Meta` (class) — [saleor/graphql/discount/types/discounts.py:49]
- `OrderDiscount` (class) — [saleor/graphql/discount/types/discounts.py:53]
- `Meta` (class) — [saleor/graphql/discount/types/discounts.py:67]
- `resolve_reason` (function) — [saleor/graphql/discount/types/discounts.py:75]
- `resolve_total` (function) — [saleor/graphql/discount/types/discounts.py:79]
- `OrderLineDiscount` (class) — [saleor/graphql/discount/types/discounts.py:83]
- `Meta` (class) — [saleor/graphql/discount/types/discounts.py:95]
- `resolve_total` (function) — [saleor/graphql/discount/types/discounts.py:101]
- `resolve_unit` (function) — [saleor/graphql/discount/types/discounts.py:105]
- `with_order_line` (function) — [saleor/graphql/discount/types/discounts.py:106]

**`saleor/graphql/discount/types/promotion_events.py`**

- `resolve_event_type` (function) — [saleor/graphql/discount/types/promotion_events.py:20]
- `PromotionEventInterface` (class) — [saleor/graphql/discount/types/promotion_events.py:24]
- `Meta` (class) — [saleor/graphql/discount/types/promotion_events.py:40]
- `resolve_type` (function) — [saleor/graphql/discount/types/promotion_events.py:44]
- `resolve_created_by` (function) — [saleor/graphql/discount/types/promotion_events.py:48]
- `PromotionCreatedEvent` (class) — [saleor/graphql/discount/types/promotion_events.py:81]
- `Meta` (class) — [saleor/graphql/discount/types/promotion_events.py:82]
- `PromotionUpdatedEvent` (class) — [saleor/graphql/discount/types/promotion_events.py:89]
- `Meta` (class) — [saleor/graphql/discount/types/promotion_events.py:90]
- `PromotionStartedEvent` (class) — [saleor/graphql/discount/types/promotion_events.py:97]
- `Meta` (class) — [saleor/graphql/discount/types/promotion_events.py:98]
- `PromotionEndedEvent` (class) — [saleor/graphql/discount/types/promotion_events.py:105]
- `Meta` (class) — [saleor/graphql/discount/types/promotion_events.py:106]
- `PromotionRuleEventInterface` (class) — [saleor/graphql/discount/types/promotion_events.py:113]
- `Meta` (class) — [saleor/graphql/discount/types/promotion_events.py:114]
- `resolve_rule_id` (function) — [saleor/graphql/discount/types/promotion_events.py:125]
- `PromotionRuleCreatedEvent` (class) — [saleor/graphql/discount/types/promotion_events.py:129]
- `Meta` (class) — [saleor/graphql/discount/types/promotion_events.py:130]
- `PromotionRuleUpdatedEvent` (class) — [saleor/graphql/discount/types/promotion_events.py:137]
- `Meta` (class) — [saleor/graphql/discount/types/promotion_events.py:138]
- `PromotionRuleDeletedEvent` (class) — [saleor/graphql/discount/types/promotion_events.py:145]
- `Meta` (class) — [saleor/graphql/discount/types/promotion_events.py:146]
- `PromotionEvent` (class) — [saleor/graphql/discount/types/promotion_events.py:164]
- `Meta` (class) — [saleor/graphql/discount/types/promotion_events.py:165]
- `resolve_type` (function) — [saleor/graphql/discount/types/promotion_events.py:169]

**`saleor/graphql/discount/types/promotions.py`**

- `Promotion` (class) — [saleor/graphql/discount/types/promotions.py:28]
- `Meta` (class) — [saleor/graphql/discount/types/promotions.py:53]
- `resolve_rules` (function) — [saleor/graphql/discount/types/promotions.py:63]
- `resolve_events` (function) — [saleor/graphql/discount/types/promotions.py:67]
- `PromotionRule` (class) — [saleor/graphql/discount/types/promotions.py:71]
- `Meta` (class) — [saleor/graphql/discount/types/promotions.py:127]
- `resolve_promotion` (function) — [saleor/graphql/discount/types/promotions.py:137]
- `resolve_predicate_type` (function) — [saleor/graphql/discount/types/promotions.py:141]
- `with_promotion` (function) — [saleor/graphql/discount/types/promotions.py:142]
- `resolve_channels` (function) — [saleor/graphql/discount/types/promotions.py:152]
- `resolve_gift_ids` (function) — [saleor/graphql/discount/types/promotions.py:156]
- `with_gifts` (function) — [saleor/graphql/discount/types/promotions.py:157]
- `PromotionCountableConnection` (class) — [saleor/graphql/discount/types/promotions.py:167]
- `Meta` (class) — [saleor/graphql/discount/types/promotions.py:168]

**`saleor/graphql/discount/types/sales.py`**

- `SaleChannelListing` (class) — [saleor/graphql/discount/types/sales.py:40]
- `Meta` (class) — [saleor/graphql/discount/types/sales.py:56]
- `Sale` (class) — [saleor/graphql/discount/types/sales.py:66]
- `Meta` (class) — [saleor/graphql/discount/types/sales.py:120]
- `resolve_id` (function) — [saleor/graphql/discount/types/sales.py:133]
- `resolve_created` (function) — [saleor/graphql/discount/types/sales.py:137]
- `resolve_type` (function) — [saleor/graphql/discount/types/sales.py:141]
- `resolve_categories` (function) — [saleor/graphql/discount/types/sales.py:153]
- `resolve_channel_listings` (function) — [saleor/graphql/discount/types/sales.py:173]
- `resolve_collections` (function) — [saleor/graphql/discount/types/sales.py:179]
- `resolve_products` (function) — [saleor/graphql/discount/types/sales.py:200]
- `resolve_variants` (function) — [saleor/graphql/discount/types/sales.py:221]
- `resolve_discount_value` (function) — [saleor/graphql/discount/types/sales.py:242]
- `resolve_currency` (function) — [saleor/graphql/discount/types/sales.py:260]
- `SaleCountableConnection` (class) — [saleor/graphql/discount/types/sales.py:276]
- `Meta` (class) — [saleor/graphql/discount/types/sales.py:277]

**`saleor/graphql/discount/types/vouchers.py`**

- `VoucherChannelListing` (class) — [saleor/graphql/discount/types/vouchers.py:39]
- `Meta` (class) — [saleor/graphql/discount/types/vouchers.py:56]
- `resolve_channel` (function) — [saleor/graphql/discount/types/vouchers.py:62]
- `VoucherCode` (class) — [saleor/graphql/discount/types/vouchers.py:66]
- `Meta` (class) — [saleor/graphql/discount/types/vouchers.py:73]
- `VoucherCodeCountableConnection` (class) — [saleor/graphql/discount/types/vouchers.py:78]
- `Meta` (class) — [saleor/graphql/discount/types/vouchers.py:79]
- `Voucher` (class) — [saleor/graphql/discount/types/vouchers.py:84]
- `Meta` (class) — [saleor/graphql/discount/types/vouchers.py:180]
- `resolve_code` (function) — [saleor/graphql/discount/types/vouchers.py:191]
- `resolve_used` (function) — [saleor/graphql/discount/types/vouchers.py:195]
- `resolve_codes` (function) — [saleor/graphql/discount/types/vouchers.py:199]
- `resolve_categories` (function) — [saleor/graphql/discount/types/vouchers.py:211]
- `resolve_collections` (function) — [saleor/graphql/discount/types/vouchers.py:218]
- `resolve_products` (function) — [saleor/graphql/discount/types/vouchers.py:228]
- `resolve_variants` (function) — [saleor/graphql/discount/types/vouchers.py:236]
- `resolve_countries` (function) — [saleor/graphql/discount/types/vouchers.py:246]
- `resolve_discount_value` (function) — [saleor/graphql/discount/types/vouchers.py:253]
- `resolve_currency` (function) — [saleor/graphql/discount/types/vouchers.py:268]
- `resolve_min_spent` (function) — [saleor/graphql/discount/types/vouchers.py:283]
- `resolve_channel_listings` (function) — [saleor/graphql/discount/types/vouchers.py:298]
- `VoucherCountableConnection` (class) — [saleor/graphql/discount/types/vouchers.py:304]
- `Meta` (class) — [saleor/graphql/discount/types/vouchers.py:305]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/discount/types/__init__.py` (22 lines)
- `saleor/graphql/discount/types/discounts.py` (113 lines)
- `saleor/graphql/discount/types/promotion_events.py` (170 lines)
- `saleor/graphql/discount/types/promotions.py` (170 lines)
- `saleor/graphql/discount/types/sales.py` (279 lines)
- `saleor/graphql/discount/types/vouchers.py` (307 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....core.prices.quantize_price`
- `....discount.DiscountValueType`
- `....discount.PromotionEvents`
- `....discount.models`
- `....permission.auth_filters.AuthorizationFilters`
- `....permission.enums.AccountPermissions`
- `....permission.enums.AppPermission`
- `....permission.enums.DiscountPermissions`
- `....permission.enums.OrderPermissions`
- `....product.models.Category`
- `....product.models.Collection`
- `....product.models.Product`
- `....product.models.ProductVariant`
- `...account.dataloaders.UserByUserIdLoader`
- `...account.utils.is_owner_or_has_one_of_perms`
- `...app.dataloaders.AppByIdLoader`
- `...channel.dataloaders.by_self.ChannelByIdLoader`
- `...channel.dataloaders.by_self.ChannelBySlugLoader`
- `...channel.types.Channel`
- `...core.ResolveInfo`
- `...core.connection.CountableConnection`
- `...core.connection.create_connection_slice`
- `...core.descriptions.DEPRECATED_IN_3X_INPUT`
- `...core.descriptions.DEPRECATED_IN_3X_TYPE`
- `...core.descriptions.PREVIEW_FEATURE`
- `...core.doc_category.DOC_CATEGORY_DISCOUNTS`
- `...core.doc_category.DOC_CATEGORY_ORDERS`
- `...core.fields.ConnectionField`
- `...core.fields.PermissionsField`
- `...core.scalars.DateTime`
- `...core.scalars.JSON`
- `...core.scalars.PositiveDecimal`
- `...core.types`
- `...core.types.BaseObjectType`
- `...core.types.ModelObjectType`
- `...core.types.Money`
- `...core.types.NonNullList`
- `...core.types.context.ChannelContextType`
- `...core.types.user_or_app.UserOrApp`
- `...meta.types.ObjectWithMetadata`
- `...order.dataloaders.OrderLineByIdLoader`
- `...translations.fields.TranslationField`
- `...translations.types.PromotionRuleTranslation`
- `...translations.types.PromotionTranslation`
- `...translations.types.SaleTranslation`
- `...translations.types.VoucherTranslation`
- `...utils.get_user_or_app_from_context`
- `..enums.DiscountValueTypeEnum`
- `..enums.OrderDiscountTypeEnum`
- `..enums.PromotionEventsEnum`
- `..enums.PromotionTypeEnum`
- `..enums.RewardTypeEnum`
- `..enums.RewardValueTypeEnum`
- `..enums.SaleType`
- `..enums.VoucherTypeEnum`
- `.discounts.OrderDiscount`
- `.promotion_events.PromotionEvent`
- `.promotions.Promotion`
- `.promotions.PromotionRule`
- `.sales.Sale`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `187e9843d6a9` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
