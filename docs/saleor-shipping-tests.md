## Purpose

`saleor/shipping/tests` (`saleor/shipping/tests`) groups 11 source file(s) exposing 36 top-level declaration(s).

## Public surface

**`saleor/shipping/tests/fixtures/shipping_method_data.py`**

- `shipping_method_data` (function) — [saleor/shipping/tests/fixtures/shipping_method_data.py:8]

**`saleor/shipping/tests/fixtures/shipping_method_translation.py`**

- `shipping_method_translation_fr` (function) — [saleor/shipping/tests/fixtures/shipping_method_translation.py:7]

**`saleor/shipping/tests/fixtures/shipping_method.py`**

- `shipping_method` (function) — [saleor/shipping/tests/fixtures/shipping_method.py:8]
- `shipping_method_price_0` (function) — [saleor/shipping/tests/fixtures/shipping_method.py:27]
- `other_shipping_method` (function) — [saleor/shipping/tests/fixtures/shipping_method.py:46]
- `shipping_method_weight_based` (function) — [saleor/shipping/tests/fixtures/shipping_method.py:62]
- `shipping_method_excluded_by_postal_code` (function) — [saleor/shipping/tests/fixtures/shipping_method.py:80]
- `shipping_method_channel_PLN` (function) — [saleor/shipping/tests/fixtures/shipping_method.py:86]

**`saleor/shipping/tests/fixtures/shipping_zone.py`**

- `shipping_zone` (function) — [saleor/shipping/tests/fixtures/shipping_zone.py:10]
- `shipping_zone_JPY` (function) — [saleor/shipping/tests/fixtures/shipping_zone.py:32]
- `shipping_zones` (function) — [saleor/shipping/tests/fixtures/shipping_zone.py:46]
- `chunks` (function) — [saleor/shipping/tests/fixtures/shipping_zone.py:100]
- `shipping_zones_with_warehouses` (function) — [saleor/shipping/tests/fixtures/shipping_zone.py:106]
- `shipping_zones_with_different_channels` (function) — [saleor/shipping/tests/fixtures/shipping_zone.py:119]
- `shipping_zone_without_countries` (function) — [saleor/shipping/tests/fixtures/shipping_zone.py:174]

**`saleor/shipping/tests/test_postal_codes.py`**

- `test_check_postal_code_for_uk` (function) — [saleor/shipping/tests/test_postal_codes.py:28]
- `test_check_postal_code_for_uk_fallbacks` (function) — [saleor/shipping/tests/test_postal_codes.py:43]
- `test_check_postal_code_for_ireland` (function) — [saleor/shipping/tests/test_postal_codes.py:55]
- `test_check_postal_code_for_other_countries` (function) — [saleor/shipping/tests/test_postal_codes.py:67]
- `test_check_uk_islands_follow_uk_check` (function) — [saleor/shipping/tests/test_postal_codes.py:80]
- `test_is_shipping_method_applicable_for_postal_code` (function) — [saleor/shipping/tests/test_postal_codes.py:118]

**`saleor/shipping/tests/test_shipping.py`**

- `test_applicable_shipping_methods_price` (function) — [saleor/shipping/tests/test_shipping.py:26]
- `test_applicable_shipping_methods_weight` (function) — [saleor/shipping/tests/test_shipping.py:75]
- `test_applicable_shipping_methods_country_code_outside_shipping_zone` (function) — [saleor/shipping/tests/test_shipping.py:97]
- `test_applicable_shipping_methods_improper_shipping_method_type` (function) — [saleor/shipping/tests/test_shipping.py:121]
- `test_applicable_shipping_methods` (function) — [saleor/shipping/tests/test_shipping.py:160]
- `test_applicable_shipping_methods_with_excluded_products` (function) — [saleor/shipping/tests/test_shipping.py:195]
- `test_applicable_shipping_methods_not_in_channel` (function) — [saleor/shipping/tests/test_shipping.py:234]
- `test_use_default_shipping_zone` (function) — [saleor/shipping/tests/test_shipping.py:258]
- `test_default_shipping_zone_exists` (function) — [saleor/shipping/tests/test_shipping.py:287]
- `test_get_countries_without_shipping_zone` (function) — [saleor/shipping/tests/test_shipping.py:294]
- `test_applicable_shipping_methods_price_rate_use_proper_channel` (function) — [saleor/shipping/tests/test_shipping.py:299]

**`saleor/shipping/tests/test_tasks.py`**

- `test_drop_invalid_shipping_method_relations` (function) — [saleor/shipping/tests/test_tasks.py:13]

**`saleor/shipping/tests/webhooks/test_shared.py`**

- `test_get_excluded_shipping_methods_from_response` (function) — [saleor/shipping/tests/webhooks/test_shared.py:19]
- `test_get_excluded_shipping_methods_from_response_invalid` (function) — [saleor/shipping/tests/webhooks/test_shared.py:62]
- `test_get_excluded_shipping_methods_or_fetch_invalid_response_type` (function) — [saleor/shipping/tests/webhooks/test_shared.py:101]

## How it works

The module's files, as provided to this run:

- `saleor/shipping/tests/__init__.py` (1 lines)
- `saleor/shipping/tests/fixtures/__init__.py` (4 lines)
- `saleor/shipping/tests/fixtures/shipping_method_data.py` (12 lines)
- `saleor/shipping/tests/fixtures/shipping_method_translation.py` (12 lines)
- `saleor/shipping/tests/fixtures/shipping_method.py` (100 lines)
- `saleor/shipping/tests/fixtures/shipping_zone.py` (187 lines)
- `saleor/shipping/tests/test_postal_codes.py` (124 lines)
- `saleor/shipping/tests/test_shipping.py` (383 lines)
- `saleor/shipping/tests/test_tasks.py` (110 lines)
- `saleor/shipping/tests/webhooks/__init__.py` (1 lines)
- `saleor/shipping/tests/webhooks/test_shared.py` (124 lines)

## Interactions

- Imports from: `saleor/shipping`, `saleor/core`, `saleor/graphql`, `saleor/webhook/transport/synchronous`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....core.prices.Money`
- `....warehouse.models.Warehouse`
- `....webhook.event_types.WebhookEventSyncType`
- `....webhook.models.Webhook`
- `....webhook.response_schemas.shipping.logger`
- `....webhook.response_schemas.utils.annotations.logger`
- `....webhook.transport.shipping_helpers.to_shipping_app_id`
- `...PostalCodeRuleInclusionType`
- `...checkout.models.Checkout`
- `...models.ShippingMethod`
- `...models.ShippingMethodChannelListing`
- `...models.ShippingMethodTranslation`
- `...models.ShippingMethodType`
- `...models.ShippingZone`
- `...order.OrderStatus`
- `...order.models.Order`
- `...utils.convert_to_shipping_method_data`
- `..tasks.drop_invalid_shipping_methods_relations_for_given_channels`
- `..utils.default_shipping_zone_exists`
- `..utils.get_countries_without_shipping_zone`
- `.shipping_method.*  # noqa: F401`
- `.shipping_method.F403`
- `.shipping_method_data.*  # noqa: F401`
- `.shipping_method_data.F403`
- `.shipping_method_translation.*  # noqa: F401`
- `.shipping_method_translation.F403`
- `.shipping_zone.*  # noqa: F401`
- `.shipping_zone.F403`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c4f11e47cb7f` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
