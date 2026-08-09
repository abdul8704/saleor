## Purpose

`saleor/graphql/core/types` (`saleor/graphql/core/types`) groups 16 source file(s) exposing 272 top-level declaration(s).

## Public surface

**`saleor/graphql/core/types/base.py`**

- `BaseObjectType` (class) — [saleor/graphql/core/types/base.py:8]
- `BaseInputObjectType` (class) — [saleor/graphql/core/types/base.py:31]
- `BaseEnum` (class) — [saleor/graphql/core/types/base.py:40]
- `BaseConnection` (class) — [saleor/graphql/core/types/base.py:49]
- `Meta` (class) — [saleor/graphql/core/types/base.py:50]
- `BaseInterface` (class) — [saleor/graphql/core/types/base.py:61]
- `Meta` (class) — [saleor/graphql/core/types/base.py:62]

**`saleor/graphql/core/types/common.py`**

- `NonNullList` (class) — [saleor/graphql/core/types/common.py:110]
- `SecureGlobalID` (class) — [saleor/graphql/core/types/common.py:118]
- `id_resolver` (function) — [saleor/graphql/core/types/common.py:120]
- `CountryDisplay` (class) — [saleor/graphql/core/types/common.py:128]
- `LanguageDisplay` (class) — [saleor/graphql/core/types/common.py:138]
- `Permission` (class) — [saleor/graphql/core/types/common.py:145]
- `Meta` (class) — [saleor/graphql/core/types/common.py:151]
- `Error` (class) — [saleor/graphql/core/types/common.py:156]
- `Meta` (class) — [saleor/graphql/core/types/common.py:166]
- `BulkError` (class) — [saleor/graphql/core/types/common.py:170]
- `Meta` (class) — [saleor/graphql/core/types/common.py:180]
- `AccountError` (class) — [saleor/graphql/core/types/common.py:184]
- `Meta` (class) — [saleor/graphql/core/types/common.py:190]
- `SendConfirmationEmailError` (class) — [saleor/graphql/core/types/common.py:195]
- `Meta` (class) — [saleor/graphql/core/types/common.py:198]
- `AppError` (class) — [saleor/graphql/core/types/common.py:202]
- `Meta` (class) — [saleor/graphql/core/types/common.py:210]
- `AttributeError` (class) — [saleor/graphql/core/types/common.py:214]
- `Meta` (class) — [saleor/graphql/core/types/common.py:217]
- `StaffError` (class) — [saleor/graphql/core/types/common.py:221]
- `Meta` (class) — [saleor/graphql/core/types/common.py:238]
- `ChannelError` (class) — [saleor/graphql/core/types/common.py:242]
- `Meta` (class) — [saleor/graphql/core/types/common.py:255]
- `CheckoutError` (class) — [saleor/graphql/core/types/common.py:259]
- `Meta` (class) — [saleor/graphql/core/types/common.py:275]
- `CustomerBulkUpdateError` (class) — [saleor/graphql/core/types/common.py:279]
- `Meta` (class) — [saleor/graphql/core/types/common.py:282]
- `ProductWithoutVariantError` (class) — [saleor/graphql/core/types/common.py:286]
- `Meta` (class) — [saleor/graphql/core/types/common.py:292]
- `DiscountError` (class) — [saleor/graphql/core/types/common.py:296]
- `Meta` (class) — [saleor/graphql/core/types/common.py:309]
- `VoucherCodeBulkDeleteError` (class) — [saleor/graphql/core/types/common.py:313]
- `Meta` (class) — [saleor/graphql/core/types/common.py:321]
- `ExportError` (class) — [saleor/graphql/core/types/common.py:325]
- `ExternalNotificationError` (class) — [saleor/graphql/core/types/common.py:329]
- `MenuError` (class) — [saleor/graphql/core/types/common.py:335]
- `Meta` (class) — [saleor/graphql/core/types/common.py:338]
- `GiftCardSettingsError` (class) — [saleor/graphql/core/types/common.py:342]
- `Meta` (class) — [saleor/graphql/core/types/common.py:345]
- `RefundSettingsUpdateError` (class) — [saleor/graphql/core/types/common.py:349]
- _…and 118 more in this file_

**`saleor/graphql/core/types/context.py`**

- `ChannelContextTypeForObjectType` (class) — [saleor/graphql/core/types/context.py:15]
- `Meta` (class) — [saleor/graphql/core/types/context.py:18]
- `resolver_with_context` (function) — [saleor/graphql/core/types/context.py:22]
- `resolve_translation` (function) — [saleor/graphql/core/types/context.py:29]
- `ChannelContextType` (class) — [saleor/graphql/core/types/context.py:39]
- `Meta` (class) — [saleor/graphql/core/types/context.py:42]
- `resolve_id` (function) — [saleor/graphql/core/types/context.py:46]
- `is_type_of` (function) — [saleor/graphql/core/types/context.py:50]

**`saleor/graphql/core/types/converter.py`**

- `get_form_field_description` (function) — [saleor/graphql/core/types/converter.py:24]
- `convert_form_field` (function) — [saleor/graphql/core/types/converter.py:33]
- `convert_form_field_to_string` (function) — [saleor/graphql/core/types/converter.py:41]
- `convert_form_field_to_nullboolean` (function) — [saleor/graphql/core/types/converter.py:48]
- `convert_form_field_to_float` (function) — [saleor/graphql/core/types/converter.py:54]
- `convert_convert_enum` (function) — [saleor/graphql/core/types/converter.py:66]
- `convert_form_field_to_id` (function) — [saleor/graphql/core/types/converter.py:71]
- `convert_list_object_type` (function) — [saleor/graphql/core/types/converter.py:77]
- `convert_form_field_to_list` (function) — [saleor/graphql/core/types/converter.py:82]

**`saleor/graphql/core/types/event.py`**

- `SubscriptionObjectType` (class) — [saleor/graphql/core/types/event.py:13]
- `Meta` (class) — [saleor/graphql/core/types/event.py:14]

**`saleor/graphql/core/types/model.py`**

- `ModelObjectOptions` (class) — [saleor/graphql/core/types/model.py:12]
- `ModelObjectType` (class) — [saleor/graphql/core/types/model.py:19]
- `get_node` (function) — [saleor/graphql/core/types/model.py:63]
- `get_model` (function) — [saleor/graphql/core/types/model.py:84]

**`saleor/graphql/core/types/money.py`**

- `Money` (class) — [saleor/graphql/core/types/money.py:9]
- `Meta` (class) — [saleor/graphql/core/types/money.py:21]
- `resolve_amount` (function) — [saleor/graphql/core/types/money.py:25]
- `resolve_fractional_amount` (function) — [saleor/graphql/core/types/money.py:29]
- `resolve_fraction_digits` (function) — [saleor/graphql/core/types/money.py:34]
- `MoneyRange` (class) — [saleor/graphql/core/types/money.py:38]
- `Meta` (class) — [saleor/graphql/core/types/money.py:42]
- `TaxedMoney` (class) — [saleor/graphql/core/types/money.py:46]
- `Meta` (class) — [saleor/graphql/core/types/money.py:56]
- `TaxedMoneyRange` (class) — [saleor/graphql/core/types/money.py:63]
- `Meta` (class) — [saleor/graphql/core/types/money.py:67]
- `VAT` (class) — [saleor/graphql/core/types/money.py:71]
- `Meta` (class) — [saleor/graphql/core/types/money.py:80]
- `resolve_standard_rate` (function) — [saleor/graphql/core/types/money.py:85]
- `resolve_reduced_rates` (function) — [saleor/graphql/core/types/money.py:89]
- `ReducedRate` (class) — [saleor/graphql/core/types/money.py:97]
- `Meta` (class) — [saleor/graphql/core/types/money.py:101]

**`saleor/graphql/core/types/order_or_checkout.py`**

- `OrderOrCheckoutBase` (class) — [saleor/graphql/core/types/order_or_checkout.py:14]
- `Meta` (class) — [saleor/graphql/core/types/order_or_checkout.py:15]
- `get_types` (function) — [saleor/graphql/core/types/order_or_checkout.py:19]
- `resolve_type` (function) — [saleor/graphql/core/types/order_or_checkout.py:23]
- `OrderOrCheckout` (class) — [saleor/graphql/core/types/order_or_checkout.py:34]
- `Meta` (class) — [saleor/graphql/core/types/order_or_checkout.py:35]

**`saleor/graphql/core/types/sort_input.py`**

- `SortInputMeta` (class) — [saleor/graphql/core/types/sort_input.py:11]
- `SortInputObjectType` (class) — [saleor/graphql/core/types/sort_input.py:15]
- `Meta` (class) — [saleor/graphql/core/types/sort_input.py:22]
- `ChannelSortInputObjectType` (class) — [saleor/graphql/core/types/sort_input.py:48]
- `Meta` (class) — [saleor/graphql/core/types/sort_input.py:57]

**`saleor/graphql/core/types/sync_webhook_control.py`**

- `SyncWebhookControlContextObjectType` (class) — [saleor/graphql/core/types/sync_webhook_control.py:14]
- `Meta` (class) — [saleor/graphql/core/types/sync_webhook_control.py:15]
- `resolver_with_context` (function) — [saleor/graphql/core/types/sync_webhook_control.py:19]
- `SyncWebhookControlContextModelObjectType` (class) — [saleor/graphql/core/types/sync_webhook_control.py:33]
- `Meta` (class) — [saleor/graphql/core/types/sync_webhook_control.py:36]

**`saleor/graphql/core/types/taxes.py`**

- `TaxSourceObject` (class) — [saleor/graphql/core/types/taxes.py:50]
- `Meta` (class) — [saleor/graphql/core/types/taxes.py:51]
- `TaxSourceLine` (class) — [saleor/graphql/core/types/taxes.py:55]
- `Meta` (class) — [saleor/graphql/core/types/taxes.py:56]
- `resolve_type` (function) — [saleor/graphql/core/types/taxes.py:60]
- `TaxableObjectLine` (class) — [saleor/graphql/core/types/taxes.py:70]
- `Meta` (class) — [saleor/graphql/core/types/taxes.py:106]
- `resolve_variant_name` (function) — [saleor/graphql/core/types/taxes.py:110]
- `get_name` (function) — [saleor/graphql/core/types/taxes.py:113]
- `resolve_product_name` (function) — [saleor/graphql/core/types/taxes.py:126]
- `get_name` (function) — [saleor/graphql/core/types/taxes.py:129]
- `resolve_product_sku` (function) — [saleor/graphql/core/types/taxes.py:142]
- `get_sku` (function) — [saleor/graphql/core/types/taxes.py:147]
- `resolve_source_line` (function) — [saleor/graphql/core/types/taxes.py:158]
- `resolve_charge_taxes` (function) — [saleor/graphql/core/types/taxes.py:162]
- `load_tax_configuration` (function) — [saleor/graphql/core/types/taxes.py:163]
- `load_tax_country_exceptions` (function) — [saleor/graphql/core/types/taxes.py:166]
- `calculate_charge_taxes` (function) — [saleor/graphql/core/types/taxes.py:173]
- `load_channel_for_checkout` (function) — [saleor/graphql/core/types/taxes.py:192]
- `load_channel_for_order` (function) — [saleor/graphql/core/types/taxes.py:206]
- `resolve_unit_price` (function) — [saleor/graphql/core/types/taxes.py:220]
- `with_checkout` (function) — [saleor/graphql/core/types/taxes.py:223]
- `calculate_line_unit_price` (function) — [saleor/graphql/core/types/taxes.py:228]
- `resolve_total_price` (function) — [saleor/graphql/core/types/taxes.py:246]
- `with_checkout` (function) — [saleor/graphql/core/types/taxes.py:249]
- `calculate_line_total_price` (function) — [saleor/graphql/core/types/taxes.py:254]
- `TaxableObjectDiscount` (class) — [saleor/graphql/core/types/taxes.py:272]
- `Meta` (class) — [saleor/graphql/core/types/taxes.py:283]
- `TaxableObject` (class) — [saleor/graphql/core/types/taxes.py:288]
- `Meta` (class) — [saleor/graphql/core/types/taxes.py:320]
- `resolve_channel` (function) — [saleor/graphql/core/types/taxes.py:325]
- `resolve_address` (function) — [saleor/graphql/core/types/taxes.py:329]
- `resolve_source_object` (function) — [saleor/graphql/core/types/taxes.py:336]
- `resolve_prices_entered_with_tax` (function) — [saleor/graphql/core/types/taxes.py:340]
- `resolve_currency` (function) — [saleor/graphql/core/types/taxes.py:345]
- `resolve_shipping_price` (function) — [saleor/graphql/core/types/taxes.py:349]
- `calculate_shipping_price` (function) — [saleor/graphql/core/types/taxes.py:352]
- `resolve_discounts` (function) — [saleor/graphql/core/types/taxes.py:374]
- `calculate_checkout_discounts` (function) — [saleor/graphql/core/types/taxes.py:377]
- `calculate_order_discounts` (function) — [saleor/graphql/core/types/taxes.py:406]
- _…and 1 more in this file_

**`saleor/graphql/core/types/tests/test_money.py`**

- `test_money_object_usd` (function) — [saleor/graphql/core/types/tests/test_money.py:8]
- `test_money_object_jpy` (function) — [saleor/graphql/core/types/tests/test_money.py:17]

**`saleor/graphql/core/types/upload.py`**

- `Upload` (class) — [saleor/graphql/core/types/upload.py:4]
- `Meta` (class) — [saleor/graphql/core/types/upload.py:5]
- `serialize` (function) — [saleor/graphql/core/types/upload.py:14]
- `parse_literal` (function) — [saleor/graphql/core/types/upload.py:18]
- `parse_value` (function) — [saleor/graphql/core/types/upload.py:22]

**`saleor/graphql/core/types/user_or_app.py`**

- `UserOrApp` (class) — [saleor/graphql/core/types/user_or_app.py:12]
- `Meta` (class) — [saleor/graphql/core/types/user_or_app.py:13]
- `resolve_type` (function) — [saleor/graphql/core/types/user_or_app.py:17]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/core/types/common.py` (1036 lines)
- `saleor/graphql/core/types/__init__.py` (178 lines)
- `saleor/graphql/core/types/base.py` (71 lines)
- `saleor/graphql/core/types/context.py` (62 lines)
- `saleor/graphql/core/types/converter.py` (87 lines)
- `saleor/graphql/core/types/event.py` (43 lines)
- `saleor/graphql/core/types/model.py` (85 lines)
- `saleor/graphql/core/types/money.py` (103 lines)
- `saleor/graphql/core/types/order_or_checkout.py` (36 lines)
- `saleor/graphql/core/types/sort_input.py` (58 lines)
- `saleor/graphql/core/types/sync_webhook_control.py` (37 lines)
- `saleor/graphql/core/types/taxes.py` (453 lines)
- `saleor/graphql/core/types/tests/__init__.py` (1 lines)
- `saleor/graphql/core/types/tests/test_money.py` (23 lines)
- `saleor/graphql/core/types/upload.py` (23 lines)
- `saleor/graphql/core/types/user_or_app.py` (22 lines)

## Interactions

- Imports from: `saleor/graphql/core`, `saleor/core`, `saleor/webhook`, `saleor/graphql`
- Imported by: `saleor/account/migrations`, `saleor/app/migrations`, `saleor/app`, `saleor/graphql/app/mutations`, `saleor/plugins/openid_connect`

Internal dependencies named in the source:

- `....account.models`
- `....app.models`
- `....checkout.base_calculations`
- `....checkout.models.Checkout`
- `....checkout.models.CheckoutLine`
- `....core.db.connection.allow_writer_in_context`
- `....core.prices.quantize_price`
- `....core.utils.build_absolute_uri`
- `....discount.DiscountType`
- `....discount.utils.checkout.has_checkout_order_promotion`
- `....discount.utils.manual_discount.split_manual_discount`
- `....discount.utils.voucher.is_order_level_voucher`
- `....order.base_calculations.base_order_subtotal`
- `....order.models.Order`
- `....order.models.OrderLine`
- `....order.utils.get_order_country`
- `....tax.utils.get_charge_taxes`
- `...ResolveInfo`
- `...account.dataloaders.AddressByIdLoader`
- `...account.enums.AddressTypeEnum`
- `...account.types`
- `...app.types`
- `...channel.dataloaders.by_self.ChannelByIdLoader`
- `...channel.types.Channel`
- `...checkout.types`
- `...core.doc_category.DOC_CATEGORY_TAXES`
- `...core.scalars.DateTime`
- `...core.scalars.Decimal`
- `...core.types.BaseObjectType`
- `...discount.dataloaders.OrderDiscountsByOrderIDLoader`
- `...order.dataloaders.OrderByIdLoader`
- `...order.dataloaders.OrderLinesByOrderIdLoader`
- `...order.types`
- `...tax.enums.TaxableObjectDiscountTypeEnum`
- `...translations.resolvers.resolve_translation`
- `..BaseObjectType`
- `..TYPES_WITH_DOUBLE_ID_AVAILABLE`
- `..context.ChannelContext`
- `..context.SyncWebhookControlContext`
- `..descriptions.DEPRECATED_IN_3X_INPUT`
- `..doc_category.DOC_CATEGORY_MAP`
- `..enums.OrderDirection`
- `..money.Money`
- `..scalars.Date`
- `..scalars.PositiveDecimal`
- `..tracing.traced_resolver`
- `..types.BaseObjectType`
- `.base.BaseInputObjectType`
- `.base.BaseObjectType`
- `.common.NonNullList`
- `.event.SubscriptionObjectType`
- `.model.ModelObjectType`
- `.money.Money`
- `.money.MoneyRange`
- `.money.ReducedRate`
- `.money.TaxedMoney`
- `.money.TaxedMoneyRange`
- `.money.VAT`
- `.order_or_checkout.OrderOrCheckoutBase`
- `.sort_input.ChannelSortInputObjectType`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `24c01274df42` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
