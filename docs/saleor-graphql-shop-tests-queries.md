## Purpose

`saleor/graphql/shop/tests/queries` (`saleor/graphql/shop/tests/queries`) groups 5 source file(s) exposing 55 top-level declaration(s).

## Public surface

**`saleor/graphql/shop/tests/queries/test_gift_card_settings.py`**

- `test_gift_card_settings_query_as_staff` (function) — [saleor/graphql/shop/tests/queries/test_gift_card_settings.py:18]
- `test_query_gift_card_settings_expiry_period` (function) — [saleor/graphql/shop/tests/queries/test_gift_card_settings.py:39]
- `test_gift_card_settings_query_as_app` (function) — [saleor/graphql/shop/tests/queries/test_gift_card_settings.py:75]
- `test_gift_card_settings_query_as_user` (function) — [saleor/graphql/shop/tests/queries/test_gift_card_settings.py:96]

**`saleor/graphql/shop/tests/queries/test_shop_allow_storefront_traffic.py`**

- `test_shop_allow_storefront_traffic_defaults_to_true` (function) — [saleor/graphql/shop/tests/queries/test_shop_allow_storefront_traffic.py:10]
- `test_shop_allow_storefront_traffic_reflects_stored_value` (function) — [saleor/graphql/shop/tests/queries/test_shop_allow_storefront_traffic.py:23]

**`saleor/graphql/shop/tests/queries/test_shop_announcements.py`**

- `resolve_dummy_announcements` (function) — [saleor/graphql/shop/tests/queries/test_shop_announcements.py:63]
- `resolve_dummy_announcements_with_empty_extra_dict` (function) — [saleor/graphql/shop/tests/queries/test_shop_announcements.py:67]
- `resolve_dummy_announcements_with_null_extra` (function) — [saleor/graphql/shop/tests/queries/test_shop_announcements.py:76]
- `use_dummy_announcements` (function) — [saleor/graphql/shop/tests/queries/test_shop_announcements.py:86]
- `default_settings` (function) — [saleor/graphql/shop/tests/queries/test_shop_announcements.py:118]
- `test_cannot_get_announcements_when_not_staff` (function) — [saleor/graphql/shop/tests/queries/test_shop_announcements.py:133]
- `test_cannot_get_announcements_when_anonymous` (function) — [saleor/graphql/shop/tests/queries/test_shop_announcements.py:141]
- `test_can_get_announcements_when_staff` (function) — [saleor/graphql/shop/tests/queries/test_shop_announcements.py:149]
- `test_get_announcements_empty_when_unconfigured` (function) — [saleor/graphql/shop/tests/queries/test_shop_announcements.py:165]
- `test_get_announcements_uses_custom_resolver` (function) — [saleor/graphql/shop/tests/queries/test_shop_announcements.py:177]
- `test_get_announcements_allows_empty_extra_dict` (function) — [saleor/graphql/shop/tests/queries/test_shop_announcements.py:208]
- `test_get_announcements_does_not_allow_null_extra` (function) — [saleor/graphql/shop/tests/queries/test_shop_announcements.py:237]

**`saleor/graphql/shop/tests/queries/test_shop.py`**

- `test_shop_id_query` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:30]
- `test_query_countries` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:52]
- `test_query_countries_with_translation` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:71]
- `test_cannot_get_shop_limit_info_when_not_staff` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:103]
- `test_get_shop_limit_info_returns_null_by_default` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:114]
- `test_version_query_as_anonymous_user` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:142]
- `test_version_query_as_customer` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:150]
- `test_version_query_as_app` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:158]
- `test_version_query_as_staff_user` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:167]
- `test_schema_version_query` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:176]
- `test_fetch_channel_currencies` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:206]
- `test_fetch_channel_currencies_by_app` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:223]
- `test_fetch_channel_currencies_by_customer` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:240]
- `test_query_name` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:251]
- `test_query_company_address` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:272]
- `test_query_domain` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:300]
- `test_query_languages` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:325]
- `test_query_permissions` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:347]
- `test_query_charge_taxes_on_shipping` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:374]
- `test_query_default_mail_sender_settings` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:403]
- `test_query_default_mail_sender_settings_not_set` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:428]
- `test_query_default_country` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:455]
- `test_query_available_external_authentications` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:499]
- `test_query_available_payment_gateways` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:530]
- `test_query_available_payment_gateways_specified_currency_USD` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:550]
- `test_query_available_payment_gateways_specified_currency_EUR` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:574]
- `test_query_available_shipping_methods_no_address` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:602]
- `test_query_available_shipping_methods_no_channel_shipping_zones` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:624]
- `test_query_available_shipping_methods_for_given_address` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:640]
- `test_query_available_shipping_methods_for_excluded_postal_code` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:668]
- `test_query_available_shipping_methods_for_included_postal_code` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:692]
- `test_staff_notification_query` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:716]
- `test_query_countries_filter_shiping_zones_attached_true` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:772]
- `test_query_countries_filter_shiping_zones_attached_false` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:791]
- `test_query_countries_filter_shiping_zones_attached_none` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:812]
- `test_query_allow_login_without_confirmation` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:828]
- `test_query_available_tax_apps` (function) — [saleor/graphql/shop/tests/queries/test_shop.py:852]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/shop/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/shop/tests/queries/test_gift_card_settings.py` (101 lines)
- `saleor/graphql/shop/tests/queries/test_shop_allow_storefront_traffic.py` (35 lines)
- `saleor/graphql/shop/tests/queries/test_shop_announcements.py` (258 lines)
- `saleor/graphql/shop/tests/queries/test_shop.py` (879 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `......__version__`
- `.....core.TimePeriodType`
- `.....core.tests.test_taxes.app_factory`
- `.....core.tests.test_taxes.tax_app_factory  # noqa: F401`
- `.....permission.enums.get_permissions_codename`
- `.....shipping.PostalCodeRuleInclusionType`
- `.....shipping.models.ShippingMethod`
- `.....site.GiftCardSettingsExpiryType`
- `.....site.apps.SiteAppConfig`
- `....account.enums.CountryCodeEnum`
- `....core.utils.str_to_enum`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `...enums.AnnouncementImportanceEnum`
- `...types.Announcement`
- `...types.SHOP_ID`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `d987d34bccf7` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
