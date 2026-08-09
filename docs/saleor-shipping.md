## Purpose

`saleor/shipping` (`saleor/shipping`) groups 9 source file(s) exposing 50 top-level declaration(s).

## Public surface

**`saleor/shipping/__init__.py`**

- `ShippingMethodType` (class) — [saleor/shipping/__init__.py:1]
- `PostalCodeRuleInclusionType` (class) — [saleor/shipping/__init__.py:11]

**`saleor/shipping/error_codes.py`**

- `ShippingErrorCode` (class) — [saleor/shipping/error_codes.py:4]
- `DeliveryOptionsCalculateErrorCode` (class) — [saleor/shipping/error_codes.py:15]

**`saleor/shipping/interface.py`**

- `ShippingMethodData` (class) — [saleor/shipping/interface.py:17]
- `is_external` (function) — [saleor/shipping/interface.py:38]
- `graphql_id` (function) — [saleor/shipping/interface.py:50]
- `ExcludedShippingMethod` (class) — [saleor/shipping/interface.py:57]

**`saleor/shipping/models.py`**

- `ShippingZone` (class) — [saleor/shipping/models.py:87]
- `Meta` (class) — [saleor/shipping/models.py:97]
- `ShippingMethodQueryset` (class) — [saleor/shipping/models.py:111]
- `price_based` (function) — [saleor/shipping/models.py:112]
- `weight_based` (function) — [saleor/shipping/models.py:115]
- `for_channel` (function) — [saleor/shipping/models.py:118]
- `applicable_shipping_methods_by_channel` (function) — [saleor/shipping/models.py:124]
- `exclude_shipping_methods_for_excluded_products` (function) — [saleor/shipping/models.py:134]
- `applicable_shipping_methods` (function) — [saleor/shipping/models.py:140]
- `applicable_shipping_methods_for_instance` (function) — [saleor/shipping/models.py:170]
- `ShippingMethod` (class) — [saleor/shipping/models.py:235]
- `Meta` (class) — [saleor/shipping/models.py:268]
- `ShippingMethodPostalCodeRule` (class) — [saleor/shipping/models.py:283]
- `Meta` (class) — [saleor/shipping/models.py:295]
- `ShippingMethodChannelListing` (class) — [saleor/shipping/models.py:299]
- `get_total` (function) — [saleor/shipping/models.py:343]
- `Meta` (class) — [saleor/shipping/models.py:346]
- `ShippingMethodTranslation` (class) — [saleor/shipping/models.py:351]
- `Meta` (class) — [saleor/shipping/models.py:358]
- `get_translated_object_id` (function) — [saleor/shipping/models.py:361]
- `get_translated_keys` (function) — [saleor/shipping/models.py:364]

**`saleor/shipping/postal_codes.py`**

- `group_values` (function) — [saleor/shipping/postal_codes.py:7]
- `cast_tuple_index_to_type` (function) — [saleor/shipping/postal_codes.py:19]
- `compare_values` (function) — [saleor/shipping/postal_codes.py:37]
- `check_uk_postal_code` (function) — [saleor/shipping/postal_codes.py:45]
- `check_irish_postal_code` (function) — [saleor/shipping/postal_codes.py:57]
- `check_any_postal_code` (function) — [saleor/shipping/postal_codes.py:67]
- `check_postal_code_in_range` (function) — [saleor/shipping/postal_codes.py:75]
- `check_shipping_method_for_postal_code` (function) — [saleor/shipping/postal_codes.py:86]
- `is_shipping_method_applicable_for_postal_code` (function) — [saleor/shipping/postal_codes.py:96]
- `filter_shipping_methods_by_postal_code_rules` (function) — [saleor/shipping/postal_codes.py:117]

**`saleor/shipping/tasks.py`**

- `drop_invalid_shipping_methods_relations_for_given_channels` (function) — [saleor/shipping/tasks.py:14]

**`saleor/shipping/utils.py`**

- `default_shipping_zone_exists` (function) — [saleor/shipping/utils.py:20]
- `get_countries_without_shipping_zone` (function) — [saleor/shipping/utils.py:26]
- `convert_to_shipping_method_data` (function) — [saleor/shipping/utils.py:36]
- `convert_checkout_delivery_to_shipping_method_data` (function) — [saleor/shipping/utils.py:68]
- `convert_shipping_method_data_to_checkout_delivery` (function) — [saleor/shipping/utils.py:91]
- `initialize_shipping_method_active_status` (function) — [saleor/shipping/utils.py:130]

**`saleor/shipping/webhooks/shared.py`**

- `generate_payload_for_shipping_method` (function) — [saleor/shipping/webhooks/shared.py:32]
- `process_responses` (function) — [saleor/shipping/webhooks/shared.py:129]
- `get_excluded_shipping_data` (function) — [saleor/shipping/webhooks/shared.py:143]
- `merge_excluded_methods_map` (function) — [saleor/shipping/webhooks/shared.py:164]

## How it works

The module's files, as provided to this run:

- `saleor/shipping/__init__.py` (18 lines)
- `saleor/shipping/webhooks/shared.py` (183 lines)
- `saleor/shipping/error_codes.py` (18 lines)
- `saleor/shipping/interface.py` (59 lines)
- `saleor/shipping/models.py` (368 lines)
- `saleor/shipping/postal_codes.py` (126 lines)
- `saleor/shipping/tasks.py` (33 lines)
- `saleor/shipping/utils.py` (141 lines)
- `saleor/shipping/webhooks/__init__.py` (1 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/graphql/product/types`, `saleor/plugins/openid_connect`, `saleor/graphql`
- Imported by: `saleor/shipping/tests`, `saleor/shipping/migrations`

Internal dependencies named in the source:

- `...account.models.User`
- `...app.models.App`
- `...checkout.models.Checkout`
- `...order.models.Order`
- `...webhook.models.Webhook`
- `..PostalCodeRuleInclusionType`
- `..ShippingMethodType`
- `..account.models.Address`
- `..celeryconf.app`
- `..channel.models.Channel`
- `..checkout.fetch.CheckoutLineInfo`
- `..checkout.models.Checkout`
- `..checkout.models.CheckoutDelivery`
- `..checkout.models.CheckoutLine`
- `..checkout.utils.calculate_checkout_weight`
- `..core.db.connection.allow_writer`
- `..core.db.fields.MoneyField`
- `..core.db.fields.SanitizedJSONField`
- `..core.editorjs.clean_editorjs`
- `..core.models.ModelWithMetadata`
- `..core.units.WeightUnits`
- `..core.utils.translations.Translation`
- `..core.weight.convert_weight`
- `..core.weight.get_default_weight_unit`
- `..core.weight.zero_weight`
- `..graphql.core.utils.from_global_id_or_error`
- `..interface.ExcludedShippingMethod`
- `..interface.ShippingMethodData`
- `..order.ORDER_EDITABLE_STATUS`
- `..order.fetch.OrderLineInfo`
- `..order.models.Order`
- `..order.models.OrderLine`
- `..permission.enums.ShippingPermissions`
- `..plugins.const.APP_ID_PREFIX`
- `..shipping.interface.ExcludedShippingMethod`
- `..tax.models.TaxClass`
- `.interface.ShippingMethodData`
- `.models.ShippingMethod`
- `.models.ShippingMethodChannelListing`
- `.models.ShippingZone`
- `.postal_codes.filter_shipping_methods_by_postal_code_rules`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `110e26c7a6ee` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
