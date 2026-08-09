## Purpose

`saleor/graphql/shipping/mutations` (`saleor/graphql/shipping/mutations`) groups 12 source file(s) exposing 80 top-level declaration(s).

## Public surface

**`saleor/graphql/shipping/mutations/base.py`**

- `ShippingZoneMixin` (class) — [saleor/graphql/shipping/mutations/base.py:26]
- `clean_input` (function) — [saleor/graphql/shipping/mutations/base.py:28]
- `check_duplicates` (function) — [saleor/graphql/shipping/mutations/base.py:49]
- `clean_add_warehouses` (function) — [saleor/graphql/shipping/mutations/base.py:69]
- `clean_default` (function) — [saleor/graphql/shipping/mutations/base.py:164]
- `delete_invalid_shipping_zone_to_warehouse_relation` (function) — [saleor/graphql/shipping/mutations/base.py:220]
- `ShippingPriceMixin` (class) — [saleor/graphql/shipping/mutations/base.py:277]
- `get_type_for_model` (function) — [saleor/graphql/shipping/mutations/base.py:279]
- `clean_input` (function) — [saleor/graphql/shipping/mutations/base.py:283]
- `clean_weight` (function) — [saleor/graphql/shipping/mutations/base.py:316]
- `clean_delivery_time` (function) — [saleor/graphql/shipping/mutations/base.py:352]
- `save` (function) — [saleor/graphql/shipping/mutations/base.py:405]
- `ShippingMethodTypeMixin` (class) — [saleor/graphql/shipping/mutations/base.py:435]
- `get_type_for_model` (function) — [saleor/graphql/shipping/mutations/base.py:437]
- `get_instance` (function) — [saleor/graphql/shipping/mutations/base.py:441]

**`saleor/graphql/shipping/mutations/delivery_options_calculate.py`**

- `DeliveryOptionsCalculate` (class) — [saleor/graphql/shipping/mutations/delivery_options_calculate.py:16]
- `Arguments` (class) — [saleor/graphql/shipping/mutations/delivery_options_calculate.py:24]
- `Meta` (class) — [saleor/graphql/shipping/mutations/delivery_options_calculate.py:30]
- `perform_mutation` (function) — [saleor/graphql/shipping/mutations/delivery_options_calculate.py:48]

**`saleor/graphql/shipping/mutations/shipping_method_channel_listing_update.py`**

- `ShippingMethodChannelListingAddInput` (class) — [saleor/graphql/shipping/mutations/shipping_method_channel_listing_update.py:31]
- `Meta` (class) — [saleor/graphql/shipping/mutations/shipping_method_channel_listing_update.py:43]
- `ShippingMethodChannelListingInput` (class) — [saleor/graphql/shipping/mutations/shipping_method_channel_listing_update.py:47]
- `Meta` (class) — [saleor/graphql/shipping/mutations/shipping_method_channel_listing_update.py:61]
- `ShippingMethodChannelListingUpdate` (class) — [saleor/graphql/shipping/mutations/shipping_method_channel_listing_update.py:65]
- `Arguments` (class) — [saleor/graphql/shipping/mutations/shipping_method_channel_listing_update.py:70]
- `Meta` (class) — [saleor/graphql/shipping/mutations/shipping_method_channel_listing_update.py:79]
- `add_channels` (function) — [saleor/graphql/shipping/mutations/shipping_method_channel_listing_update.py:87]
- `remove_channels` (function) — [saleor/graphql/shipping/mutations/shipping_method_channel_listing_update.py:110]
- `save` (function) — [saleor/graphql/shipping/mutations/shipping_method_channel_listing_update.py:121]
- `get_shipping_method_channel_listing_to_update` (function) — [saleor/graphql/shipping/mutations/shipping_method_channel_listing_update.py:135]
- `clean_input` (function) — [saleor/graphql/shipping/mutations/shipping_method_channel_listing_update.py:151]
- `clean_add_channels` (function) — [saleor/graphql/shipping/mutations/shipping_method_channel_listing_update.py:236]
- `perform_mutation` (function) — [saleor/graphql/shipping/mutations/shipping_method_channel_listing_update.py:259]

**`saleor/graphql/shipping/mutations/shipping_price_create.py`**

- `ShippingPostalCodeRulesCreateInputRange` (class) — [saleor/graphql/shipping/mutations/shipping_price_create.py:18]
- `Meta` (class) — [saleor/graphql/shipping/mutations/shipping_price_create.py:24]
- `ShippingPriceInput` (class) — [saleor/graphql/shipping/mutations/shipping_price_create.py:28]
- `Meta` (class) — [saleor/graphql/shipping/mutations/shipping_price_create.py:66]
- `ShippingPriceCreate` (class) — [saleor/graphql/shipping/mutations/shipping_price_create.py:70]
- `Arguments` (class) — [saleor/graphql/shipping/mutations/shipping_price_create.py:81]
- `Meta` (class) — [saleor/graphql/shipping/mutations/shipping_price_create.py:86]
- `post_save_action` (function) — [saleor/graphql/shipping/mutations/shipping_price_create.py:96]
- `success_response` (function) — [saleor/graphql/shipping/mutations/shipping_price_create.py:101]

**`saleor/graphql/shipping/mutations/shipping_price_delete.py`**

- `ShippingPriceDelete` (class) — [saleor/graphql/shipping/mutations/shipping_price_delete.py:16]
- `Arguments` (class) — [saleor/graphql/shipping/mutations/shipping_price_delete.py:25]
- `Meta` (class) — [saleor/graphql/shipping/mutations/shipping_price_delete.py:28]
- `perform_mutation` (function) — [saleor/graphql/shipping/mutations/shipping_price_delete.py:36]

**`saleor/graphql/shipping/mutations/shipping_price_exclude_products.py`**

- `ShippingPriceExcludeProductsInput` (class) — [saleor/graphql/shipping/mutations/shipping_price_exclude_products.py:16]
- `Meta` (class) — [saleor/graphql/shipping/mutations/shipping_price_exclude_products.py:23]
- `ShippingPriceExcludeProducts` (class) — [saleor/graphql/shipping/mutations/shipping_price_exclude_products.py:27]
- `Arguments` (class) — [saleor/graphql/shipping/mutations/shipping_price_exclude_products.py:33]
- `Meta` (class) — [saleor/graphql/shipping/mutations/shipping_price_exclude_products.py:39]
- `perform_mutation` (function) — [saleor/graphql/shipping/mutations/shipping_price_exclude_products.py:47]

**`saleor/graphql/shipping/mutations/shipping_price_remove_product_from_exclude.py`**

- `ShippingPriceRemoveProductFromExclude` (class) — [saleor/graphql/shipping/mutations/shipping_price_remove_product_from_exclude.py:17]
- `Arguments` (class) — [saleor/graphql/shipping/mutations/shipping_price_remove_product_from_exclude.py:23]
- `Meta` (class) — [saleor/graphql/shipping/mutations/shipping_price_remove_product_from_exclude.py:31]
- `perform_mutation` (function) — [saleor/graphql/shipping/mutations/shipping_price_remove_product_from_exclude.py:39]

**`saleor/graphql/shipping/mutations/shipping_price_update.py`**

- `ShippingPriceUpdate` (class) — [saleor/graphql/shipping/mutations/shipping_price_update.py:15]
- `Arguments` (class) — [saleor/graphql/shipping/mutations/shipping_price_update.py:26]
- `Meta` (class) — [saleor/graphql/shipping/mutations/shipping_price_update.py:32]
- `post_save_action` (function) — [saleor/graphql/shipping/mutations/shipping_price_update.py:42]
- `success_response` (function) — [saleor/graphql/shipping/mutations/shipping_price_update.py:47]

**`saleor/graphql/shipping/mutations/shipping_zone_create.py`**

- `ShippingZoneCreateInput` (class) — [saleor/graphql/shipping/mutations/shipping_zone_create.py:15]
- `Meta` (class) — [saleor/graphql/shipping/mutations/shipping_zone_create.py:38]
- `ShippingZoneCreate` (class) — [saleor/graphql/shipping/mutations/shipping_zone_create.py:42]
- `Arguments` (class) — [saleor/graphql/shipping/mutations/shipping_zone_create.py:43]
- `Meta` (class) — [saleor/graphql/shipping/mutations/shipping_zone_create.py:48]
- `post_save_action` (function) — [saleor/graphql/shipping/mutations/shipping_zone_create.py:57]
- `success_response` (function) — [saleor/graphql/shipping/mutations/shipping_zone_create.py:62]

**`saleor/graphql/shipping/mutations/shipping_zone_delete.py`**

- `ShippingZoneDelete` (class) — [saleor/graphql/shipping/mutations/shipping_zone_delete.py:13]
- `Arguments` (class) — [saleor/graphql/shipping/mutations/shipping_zone_delete.py:14]
- `Meta` (class) — [saleor/graphql/shipping/mutations/shipping_zone_delete.py:17]
- `post_save_action` (function) — [saleor/graphql/shipping/mutations/shipping_zone_delete.py:26]
- `success_response` (function) — [saleor/graphql/shipping/mutations/shipping_zone_delete.py:31]

**`saleor/graphql/shipping/mutations/shipping_zone_update.py`**

- `ShippingZoneUpdateInput` (class) — [saleor/graphql/shipping/mutations/shipping_zone_update.py:16]
- `Meta` (class) — [saleor/graphql/shipping/mutations/shipping_zone_update.py:26]
- `ShippingZoneUpdate` (class) — [saleor/graphql/shipping/mutations/shipping_zone_update.py:30]
- `Arguments` (class) — [saleor/graphql/shipping/mutations/shipping_zone_update.py:31]
- `Meta` (class) — [saleor/graphql/shipping/mutations/shipping_zone_update.py:37]
- `post_save_action` (function) — [saleor/graphql/shipping/mutations/shipping_zone_update.py:46]
- `success_response` (function) — [saleor/graphql/shipping/mutations/shipping_zone_update.py:51]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/shipping/mutations/base.py` (449 lines)
- `saleor/graphql/shipping/mutations/shipping_method_channel_listing_update.py` (279 lines)
- `saleor/graphql/shipping/mutations/__init__.py` (23 lines)
- `saleor/graphql/shipping/mutations/delivery_options_calculate.py` (69 lines)
- `saleor/graphql/shipping/mutations/shipping_price_create.py` (107 lines)
- `saleor/graphql/shipping/mutations/shipping_price_delete.py` (53 lines)
- `saleor/graphql/shipping/mutations/shipping_price_exclude_products.py` (72 lines)
- `saleor/graphql/shipping/mutations/shipping_price_remove_product_from_exclude.py` (59 lines)
- `saleor/graphql/shipping/mutations/shipping_price_update.py` (54 lines)
- `saleor/graphql/shipping/mutations/shipping_zone_create.py` (66 lines)
- `saleor/graphql/shipping/mutations/shipping_zone_delete.py` (35 lines)
- `saleor/graphql/shipping/mutations/shipping_zone_update.py` (55 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: `saleor/graphql/shipping/tests/mutations`

Internal dependencies named in the source:

- `....channel.models`
- `....checkout.delivery_context.fetch_shipping_methods_for_checkout`
- `....checkout.fetch.fetch_checkout_info`
- `....checkout.fetch.fetch_checkout_lines`
- `....core.tracing.traced_atomic_transaction`
- `....permission.enums.ShippingPermissions`
- `....product.models`
- `....shipping.error_codes.ShippingErrorCode`
- `....shipping.models`
- `....shipping.models.ShippingMethod`
- `....shipping.models.ShippingMethodChannelListing`
- `....webhook.event_types.WebhookEventSyncType`
- `...channel.mutations.BaseChannelListingMutation`
- `...checkout.types`
- `...core.ResolveInfo`
- `...core.context.ChannelContext`
- `...core.descriptions.ADDED_IN_323`
- `...core.doc_category.DOC_CATEGORY_SHIPPING`
- `...core.fields.JSONString`
- `...core.mutations.BaseMutation`
- `...core.mutations.DeprecatedModelMutation`
- `...core.mutations.ModelDeleteMutation`
- `...core.scalars.PositiveDecimal`
- `...core.scalars.WeightScalar`
- `...core.types.BaseInputObjectType`
- `...core.types.NonNullList`
- `...core.types.ShippingError`
- `...core.types.common.DeliveryOptionsCalculateError`
- `...core.types.common.NonNullList`
- `...core.utils.WebhookEventInfo`
- `...core.validators.validate_decimal_max_value`
- `...core.validators.validate_price_precision`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `...product.types`
- `...shipping.types`
- `...utils.get_user_or_app_from_context`
- `...utils.resolve_global_ids_to_primary_keys`
- `...utils.validators.check_for_duplicates`
- `..enums.PostalCodeRuleInclusionTypeEnum`
- `..enums.ShippingMethodTypeEnum`
- `..types.ShippingMethodPostalCodeRule`
- `..types.ShippingMethodType`
- `..types.ShippingZone`
- `..utils.get_shipping_model_by_object_id`
- `.base.ShippingMethodTypeMixin`
- `.base.ShippingPriceMixin`
- `.base.ShippingZoneMixin`
- `.shipping_method_channel_listing_update.ShippingMethodChannelListing`
- `.shipping_price_create.ShippingPriceCreate`
- `.shipping_price_create.ShippingPriceInput`
- `.shipping_price_delete.ShippingPriceDelete`
- `.shipping_price_exclude_products.ShippingPriceExcludeProducts`
- `.shipping_price_update.ShippingPriceUpdate`
- `.shipping_zone_create.ShippingZoneCreate`
- `.shipping_zone_create.ShippingZoneCreateInput`
- `.shipping_zone_delete.ShippingZoneDelete`
- `.shipping_zone_update.ShippingZoneUpdate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `42abebf58302` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
