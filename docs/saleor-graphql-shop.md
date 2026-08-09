## Purpose

`saleor/graphql/shop` (`saleor/graphql/shop`) groups 7 source file(s) exposing 86 top-level declaration(s).

## Public surface

**`saleor/graphql/shop/filters.py`**

- `CountryFilterInput` (class) — [saleor/graphql/shop/filters.py:4]

**`saleor/graphql/shop/resolvers.py`**

- `resolve_available_shipping_methods` (function) — [saleor/graphql/shop/resolvers.py:15]
- `resolve_countries` (function) — [saleor/graphql/shop/resolvers.py:39]
- `get_shipping_method_to_listing_mapping` (function) — [saleor/graphql/shop/resolvers.py:56]

**`saleor/graphql/shop/schema.py`**

- `ShopQueries` (class) — [saleor/graphql/shop/schema.py:26]
- `resolve_shop` (function) — [saleor/graphql/shop/schema.py:54]
- `resolve_gift_card_settings` (function) — [saleor/graphql/shop/schema.py:58]
- `resolve_refund_settings` (function) — [saleor/graphql/shop/schema.py:62]
- `resolve_return_settings` (function) — [saleor/graphql/shop/schema.py:66]
- `ShopMutations` (class) — [saleor/graphql/shop/schema.py:70]

**`saleor/graphql/shop/types.py`**

- `Domain` (class) — [saleor/graphql/shop/types.py:72]
- `Meta` (class) — [saleor/graphql/shop/types.py:79]
- `OrderSettings` (class) — [saleor/graphql/shop/types.py:83]
- `Meta` (class) — [saleor/graphql/shop/types.py:87]
- `RefundSettings` (class) — [saleor/graphql/shop/types.py:93]
- `Meta` (class) — [saleor/graphql/shop/types.py:98]
- `resolve_reason_reference_type` (function) — [saleor/graphql/shop/types.py:104]
- `ReturnSettings` (class) — [saleor/graphql/shop/types.py:108]
- `Meta` (class) — [saleor/graphql/shop/types.py:114]
- `resolve_reason_reference_type` (function) — [saleor/graphql/shop/types.py:120]
- `GiftCardSettings` (class) — [saleor/graphql/shop/types.py:124]
- `Meta` (class) — [saleor/graphql/shop/types.py:132]
- `resolve_expiry_type` (function) — [saleor/graphql/shop/types.py:138]
- `resolve_expiry_period` (function) — [saleor/graphql/shop/types.py:142]
- `ExternalAuthentication` (class) — [saleor/graphql/shop/types.py:150]
- `Meta` (class) — [saleor/graphql/shop/types.py:156]
- `Limits` (class) — [saleor/graphql/shop/types.py:161]
- `LimitInfo` (class) — [saleor/graphql/shop/types.py:171]
- `Meta` (class) — [saleor/graphql/shop/types.py:183]
- `Announcement` (class) — [saleor/graphql/shop/types.py:187]
- `Meta` (class) — [saleor/graphql/shop/types.py:223]
- `Shop` (class) — [saleor/graphql/shop/types.py:227]
- `Meta` (class) — [saleor/graphql/shop/types.py:516]
- `get_model` (function) — [saleor/graphql/shop/types.py:523]
- `get_node` (function) — [saleor/graphql/shop/types.py:527]
- `resolve_id` (function) — [saleor/graphql/shop/types.py:535]
- `resolve_available_payment_gateways` (function) — [saleor/graphql/shop/types.py:541]
- `resolve_available_external_authentications` (function) — [saleor/graphql/shop/types.py:553]
- `resolve_available_shipping_methods` (function) — [saleor/graphql/shop/types.py:557]
- `resolve_channel_currencies` (function) — [saleor/graphql/shop/types.py:563]
- `resolve_countries` (function) — [saleor/graphql/shop/types.py:571]
- `resolve_domain` (function) — [saleor/graphql/shop/types.py:576]
- `resolve_description` (function) — [saleor/graphql/shop/types.py:585]
- `resolve_languages` (function) — [saleor/graphql/shop/types.py:589]
- `resolve_name` (function) — [saleor/graphql/shop/types.py:599]
- `resolve_permissions` (function) — [saleor/graphql/shop/types.py:604]
- `resolve_phone_prefixes` (function) — [saleor/graphql/shop/types.py:610]
- `resolve_header_text` (function) — [saleor/graphql/shop/types.py:615]
- `resolve_fulfillment_auto_approve` (function) — [saleor/graphql/shop/types.py:620]
- `resolve_fulfillment_allow_unpaid` (function) — [saleor/graphql/shop/types.py:625]
- _…and 34 more in this file_

**`saleor/graphql/shop/utils.py`**

- `get_countries_codes_list` (function) — [saleor/graphql/shop/utils.py:8]
- `get_track_inventory_by_default` (function) — [saleor/graphql/shop/utils.py:36]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/shop/__init__.py` (1 lines)
- `saleor/graphql/shop/enums.py` (40 lines)
- `saleor/graphql/shop/filters.py` (10 lines)
- `saleor/graphql/shop/resolvers.py` (65 lines)
- `saleor/graphql/shop/schema.py` (83 lines)
- `saleor/graphql/shop/types.py` (813 lines)
- `saleor/graphql/shop/utils.py` (40 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....__version__`
- `....schema_version`
- `...account.models`
- `...account.models.Address`
- `...app.utils.get_active_tax_apps`
- `...channel.models`
- `...core.models.ModelWithMetadata`
- `...core.utils.build_absolute_uri`
- `...core.utils.get_domain`
- `...core.utils.is_ssl_enabled`
- `...payment.gateway.get_payment_gateways`
- `...permission.auth_filters.AuthorizationFilters`
- `...permission.enums.AppPermission`
- `...permission.enums.GiftcardPermissions`
- `...permission.enums.SitePermissions`
- `...permission.enums.get_permissions`
- `...shipping.models.ShippingMethod`
- `...shipping.models.ShippingMethodChannelListing`
- `...shipping.models.ShippingZone`
- `...shipping.postal_codes.filter_shipping_methods_by_postal_code_rules`
- `...shipping.utils.convert_to_shipping_method_data`
- `...site.apps.SiteAppConfig`
- `...site.models`
- `..account.types.Address`
- `..account.types.AddressInput`
- `..account.types.StaffNotificationRecipient`
- `..app.types.App`
- `..core.ResolveInfo`
- `..core.context.get_database_connection_name`
- `..core.enums.LanguageCodeEnum`
- `..core.enums.WeightUnitsEnum`
- `..core.enums.to_enum`
- `..core.fields.PermissionsField`
- `..core.scalars.DateTime`
- `..core.tracing.traced_resolver`
- `..core.types.CountryDisplay`
- `..core.utils.str_to_enum`
- `..meta.types.Metadata`
- `..meta.types.ObjectWithMetadata`
- `..page.types.PageType`
- `..payment.types.PaymentGateway`
- `..plugins.dataloaders.plugin_manager_promise_callback`
- `..shipping.types.ShippingMethod`
- `..site.dataloaders.get_site_promise`
- `..site.dataloaders.load_site_callback`
- `..translations.fields.TranslationField`
- `..translations.mutations.ShopSettingsTranslate`
- `..translations.resolvers.resolve_translation`
- `..translations.types.ShopTranslation`
- `..utils.format_permissions_for_display`
- `.filters.CountryFilterInput`
- `.resolvers.resolve_available_shipping_methods`
- `.resolvers.resolve_countries`
- `.types.GiftCardSettings`
- `.types.RefundSettings`
- `.types.ReturnSettings`
- `.types.Shop`
- `.utils.get_countries_codes_list`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `a323e0c9b1cc` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
