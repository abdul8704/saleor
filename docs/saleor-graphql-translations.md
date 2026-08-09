## Purpose

`saleor/graphql/translations` (`saleor/graphql/translations`) groups 7 source file(s) exposing 149 top-level declaration(s).

## Public surface

**`saleor/graphql/translations/dataloaders.py`**

- `BaseTranslationByIdAndLanguageCodeLoader` (class) — [saleor/graphql/translations/dataloaders.py:16]
- `batch_load` (function) — [saleor/graphql/translations/dataloaders.py:20]
- `AttributeTranslationByIdAndLanguageCodeLoader` (class) — [saleor/graphql/translations/dataloaders.py:47]
- `AttributeValueTranslationByIdAndLanguageCodeLoader` (class) — [saleor/graphql/translations/dataloaders.py:55]
- `CategoryTranslationByIdAndLanguageCodeLoader` (class) — [saleor/graphql/translations/dataloaders.py:63]
- `CollectionTranslationByIdAndLanguageCodeLoader` (class) — [saleor/graphql/translations/dataloaders.py:71]
- `MenuItemTranslationByIdAndLanguageCodeLoader` (class) — [saleor/graphql/translations/dataloaders.py:79]
- `PageTranslationByIdAndLanguageCodeLoader` (class) — [saleor/graphql/translations/dataloaders.py:87]
- `ProductTranslationByIdAndLanguageCodeLoader` (class) — [saleor/graphql/translations/dataloaders.py:95]
- `ProductVariantTranslationByIdAndLanguageCodeLoader` (class) — [saleor/graphql/translations/dataloaders.py:103]
- `ShippingMethodTranslationByIdAndLanguageCodeLoader` (class) — [saleor/graphql/translations/dataloaders.py:111]
- `SiteSettingsTranslationByIdAndLanguageCodeLoader` (class) — [saleor/graphql/translations/dataloaders.py:119]
- `VoucherTranslationByIdAndLanguageCodeLoader` (class) — [saleor/graphql/translations/dataloaders.py:127]
- `PromotionTranslationByIdAndLanguageCodeLoader` (class) — [saleor/graphql/translations/dataloaders.py:135]
- `PromotionRuleTranslationByIdAndLanguageCodeLoader` (class) — [saleor/graphql/translations/dataloaders.py:143]

**`saleor/graphql/translations/descriptions.py`**

- `TranslationDescriptions` (class) — [saleor/graphql/translations/descriptions.py:1]

**`saleor/graphql/translations/fields.py`**

- `TranslationField` (class) — [saleor/graphql/translations/fields.py:8]

**`saleor/graphql/translations/resolvers.py`**

- `resolve_translation` (function) — [saleor/graphql/translations/resolvers.py:50]
- `resolve_shipping_methods` (function) — [saleor/graphql/translations/resolvers.py:59]
- `resolve_attribute_values` (function) — [saleor/graphql/translations/resolvers.py:65]
- `resolve_products` (function) — [saleor/graphql/translations/resolvers.py:71]
- `resolve_product_variants` (function) — [saleor/graphql/translations/resolvers.py:77]
- `resolve_sales` (function) — [saleor/graphql/translations/resolvers.py:83]
- `resolve_vouchers` (function) — [saleor/graphql/translations/resolvers.py:89]
- `resolve_collections` (function) — [saleor/graphql/translations/resolvers.py:95]
- `resolve_promotions` (function) — [saleor/graphql/translations/resolvers.py:101]
- `resolve_promotion_rules` (function) — [saleor/graphql/translations/resolvers.py:107]

**`saleor/graphql/translations/schema.py`**

- `TranslatableItem` (class) — [saleor/graphql/translations/schema.py:48]
- `Meta` (class) — [saleor/graphql/translations/schema.py:49]
- `resolve_type` (function) — [saleor/graphql/translations/schema.py:55]
- `TranslatableItemConnection` (class) — [saleor/graphql/translations/schema.py:68]
- `Meta` (class) — [saleor/graphql/translations/schema.py:69]
- `TranslatableKinds` (class) — [saleor/graphql/translations/schema.py:73]
- `TranslationQueries` (class) — [saleor/graphql/translations/schema.py:89]
- `resolve_translations` (function) — [saleor/graphql/translations/schema.py:115]
- `resolve_translation` (function) — [saleor/graphql/translations/schema.py:146]

**`saleor/graphql/translations/types.py`**

- `get_translatable_attribute_values` (function) — [saleor/graphql/translations/types.py:65]
- `BaseTranslationType` (class) — [saleor/graphql/translations/types.py:79]
- `Meta` (class) — [saleor/graphql/translations/types.py:84]
- `resolve_language` (function) — [saleor/graphql/translations/types.py:89]
- `AttributeValueTranslation` (class) — [saleor/graphql/translations/types.py:103]
- `Meta` (class) — [saleor/graphql/translations/types.py:121]
- `resolve_translatable_content` (function) — [saleor/graphql/translations/types.py:127]
- `AttributeTranslation` (class) — [saleor/graphql/translations/types.py:133]
- `Meta` (class) — [saleor/graphql/translations/types.py:143]
- `resolve_translatable_content` (function) — [saleor/graphql/translations/types.py:149]
- `AttributeTranslatableContent` (class) — [saleor/graphql/translations/types.py:153]
- `Meta` (class) — [saleor/graphql/translations/types.py:170]
- `resolve_attribute` (function) — [saleor/graphql/translations/types.py:179]
- `resolve_attribute_id` (function) — [saleor/graphql/translations/types.py:183]
- `AttributeValueTranslatableContent` (class) — [saleor/graphql/translations/types.py:187]
- `Meta` (class) — [saleor/graphql/translations/types.py:216]
- `resolve_attribute_value` (function) — [saleor/graphql/translations/types.py:225]
- `resolve_attribute` (function) — [saleor/graphql/translations/types.py:229]
- `resolve_attribute_value_id` (function) — [saleor/graphql/translations/types.py:233]
- `ProductVariantTranslation` (class) — [saleor/graphql/translations/types.py:237]
- `Meta` (class) — [saleor/graphql/translations/types.py:251]
- `resolve_translatable_content` (function) — [saleor/graphql/translations/types.py:257]
- `ProductVariantTranslatableContent` (class) — [saleor/graphql/translations/types.py:263]
- `Meta` (class) — [saleor/graphql/translations/types.py:290]
- `resolve_product_variant` (function) — [saleor/graphql/translations/types.py:299]
- `resolve_attribute_values` (function) — [saleor/graphql/translations/types.py:303]
- `with_attribute_values` (function) — [saleor/graphql/translations/types.py:304]
- `with_attributes` (function) — [saleor/graphql/translations/types.py:307]
- `resolve_product_variant_id` (function) — [saleor/graphql/translations/types.py:335]
- `ProductTranslation` (class) — [saleor/graphql/translations/types.py:339]
- `Meta` (class) — [saleor/graphql/translations/types.py:359]
- `resolve_description_json` (function) — [saleor/graphql/translations/types.py:365]
- `resolve_translatable_content` (function) — [saleor/graphql/translations/types.py:370]
- `ProductTranslatableContent` (class) — [saleor/graphql/translations/types.py:374]
- `Meta` (class) — [saleor/graphql/translations/types.py:405]
- `resolve_product` (function) — [saleor/graphql/translations/types.py:414]
- `resolve_description_json` (function) — [saleor/graphql/translations/types.py:418]
- `resolve_attribute_values` (function) — [saleor/graphql/translations/types.py:423]
- `with_attribute_values` (function) — [saleor/graphql/translations/types.py:424]
- `with_attributes` (function) — [saleor/graphql/translations/types.py:427]
- _…and 73 more in this file_

## How it works

The module's files, as provided to this run:

- `saleor/graphql/translations/__init__.py` (1 lines)
- `saleor/graphql/translations/dataloaders.py` (148 lines)
- `saleor/graphql/translations/descriptions.py` (3 lines)
- `saleor/graphql/translations/fields.py` (21 lines)
- `saleor/graphql/translations/resolvers.py` (110 lines)
- `saleor/graphql/translations/schema.py` (175 lines)
- `saleor/graphql/translations/types.py` (1100 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: `saleor/graphql/translations/mutations`

Internal dependencies named in the source:

- `...attribute.AttributeInputType`
- `...attribute.models`
- `...attribute.models.Attribute`
- `...attribute.models.AttributeValue`
- `...discount.models`
- `...discount.models.Promotion`
- `...discount.models.PromotionRule`
- `...discount.models.Voucher`
- `...menu.models`
- `...menu.models.MenuItem`
- `...page.models`
- `...page.models.Page`
- `...permission.enums.SitePermissions`
- `...permission.utils.all_permissions_required`
- `...product.models`
- `...product.models.Category`
- `...product.models.Collection`
- `...product.models.Product`
- `...product.models.ProductVariant`
- `...shipping.interface`
- `...shipping.models`
- `...shipping.models.ShippingMethod`
- `...site.models`
- `..attribute.resolvers.resolve_attributes`
- `..core.ResolveInfo`
- `..core.connection.CountableConnection`
- `..core.connection.create_connection_slice`
- `..core.context.ChannelContext`
- `..core.context.get_database_connection_name`
- `..core.dataloaders.DataLoader`
- `..core.descriptions.DEPRECATED_IN_3X_TYPE`
- `..core.descriptions.RICH_CONTENT`
- `..core.enums.LanguageCodeEnum`
- `..core.fields.ConnectionField`
- `..core.fields.JSONString`
- `..core.fields.PermissionsField`
- `..core.tracing.traced_resolver`
- `..core.types.LanguageDisplay`
- `..core.types.ModelObjectType`
- `..core.types.NonNullList`
- `..core.utils.from_global_id_or_error`
- `..core.utils.str_to_enum`
- `..dataloaders`
- `..menu.dataloaders.MenuItemByIdLoader`
- `..menu.resolvers.resolve_menu_items`
- `..page.resolvers.resolve_pages`
- `..product.resolvers.resolve_categories`
- `..shipping.dataloaders.ShippingMethodByIdLoader`
- `..translations.types`
- `.descriptions.TranslationDescriptions`
- `.fields.TranslationField`
- `.resolvers.resolve_translation`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `1cf0e9fa2ceb` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
