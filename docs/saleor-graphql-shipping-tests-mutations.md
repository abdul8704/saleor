## Purpose

`saleor/graphql/shipping/tests/mutations` (`saleor/graphql/shipping/tests/mutations`) groups 12 source file(s) exposing 87 top-level declaration(s).

## Public surface

**`saleor/graphql/shipping/tests/mutations/test_bulk_delete.py`**

- `shipping_method_list` (function) — [saleor/graphql/shipping/tests/mutations/test_bulk_delete.py:11]
- `shipping_zone_list` (function) — [saleor/graphql/shipping/tests/mutations/test_bulk_delete.py:34]
- `test_delete_shipping_methods` (function) — [saleor/graphql/shipping/tests/mutations/test_bulk_delete.py:41]
- `test_delete_shipping_methods_trigger_multiple_webhook_events` (function) — [saleor/graphql/shipping/tests/mutations/test_bulk_delete.py:73]
- `test_delete_shipping_zones` (function) — [saleor/graphql/shipping/tests/mutations/test_bulk_delete.py:115]
- `test_delete_shipping_zones_trigger_multiple_webhook_events` (function) — [saleor/graphql/shipping/tests/mutations/test_bulk_delete.py:147]

**`saleor/graphql/shipping/tests/mutations/test_delivery_options_calculate.py`**

- `test_used_with_different_type_than_checkout` (function) — [saleor/graphql/shipping/tests/mutations/test_delivery_options_calculate.py:44]
- `test_checkout_not_found` (function) — [saleor/graphql/shipping/tests/mutations/test_delivery_options_calculate.py:60]
- `test_fetches_external_shipping_methods` (function) — [saleor/graphql/shipping/tests/mutations/test_delivery_options_calculate.py:87]
- `test_excluded_shipping_methods_called_for_checkout` (function) — [saleor/graphql/shipping/tests/mutations/test_delivery_options_calculate.py:140]
- `test_when_checkout_has_stale_deliveries` (function) — [saleor/graphql/shipping/tests/mutations/test_delivery_options_calculate.py:187]
- `test_refresh_deliveries_when_delivery_methods_stale_at_has_future_date` (function) — [saleor/graphql/shipping/tests/mutations/test_delivery_options_calculate.py:234]
- `test_when_refreshed_delivery_has_different_details` (function) — [saleor/graphql/shipping/tests/mutations/test_delivery_options_calculate.py:280]
- `test_when_assigned_delivery_has_stale_invalid_sibling` (function) — [saleor/graphql/shipping/tests/mutations/test_delivery_options_calculate.py:337]
- `test_refresh_deliveries_when_assigned_delivery_is_none` (function) — [saleor/graphql/shipping/tests/mutations/test_delivery_options_calculate.py:424]

**`saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py`**

- `test_shipping_method_channel_listing_create_as_staff_user` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py:50]
- `test_shipping_method_channel_listing_update_allow_to_set_null_for_limit_fields` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py:110]
- `test_shipping_method_channel_listing_create_trigger_webhook` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py:168]
- `test_shipping_method_channel_listing_update_as_staff_user` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py:238]
- `test_shipping_method_channel_listing_update_with_negative_price` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py:306]
- `test_shipping_method_channel_listing_update_with_negative_min_value` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py:347]
- `test_shipping_method_channel_listing_update_with_negative_max_value` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py:388]
- `test_shipping_method_channel_listing_update_with_max_less_than_min` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py:427]
- `test_shipping_method_channel_listing_create_without_price` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py:472]
- `test_shipping_method_channel_listing_update_with_to_many_decimal_places_in_price` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py:515]
- `test_shipping_method_channel_listing_update_with_to_many_decimal_places_in_min_val` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py:560]
- `test_shipping_method_channel_listing_update_with_to_many_decimal_places_in_max_val` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py:605]
- `test_shipping_method_channel_listing_create_channel_not_valid` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py:650]
- `test_shipping_method_channel_listing_update_remove_channels` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py:701]
- `test_shipping_method_channel_listing_create_channel_max_value_validation` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py:753]

**`saleor/graphql/shipping/tests/mutations/test_shipping_price_create.py`**

- `test_create_shipping_method` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_create.py:88]
- `test_create_shipping_method_trigger_webhook` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_create.py:140]
- `test_create_shipping_method_minimum_delivery_days_higher_than_maximum` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_create.py:207]
- `test_create_shipping_method_minimum_delivery_days_below_0` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_create.py:242]
- `test_create_shipping_method_maximum_delivery_days_below_0` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_create.py:277]
- `test_create_shipping_method_postal_code_duplicate_entry` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_create.py:312]
- `test_create_shipping_method_postal_code_missing_inclusion_type` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_create.py:353]
- `test_create_weight_based_shipping_method` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_create.py:441]
- `test_create_weight_shipping_method_errors` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_create.py:475]
- `test_create_shipping_method_with_negative_min_weight` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_create.py:501]
- `test_create_shipping_method_with_negative_max_weight` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_create.py:528]

**`saleor/graphql/shipping/tests/mutations/test_shipping_price_delete.py`**

- `test_delete_shipping_method` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_delete.py:30]
- `test_delete_shipping_method_trigger_webhook` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_delete.py:59]

**`saleor/graphql/shipping/tests/mutations/test_shipping_price_exclude_products.py`**

- `test_exclude_products_for_shipping_method_only_products` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_exclude_products.py:42]
- `test_exclude_products_for_shipping_method_already_has_excluded_products` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_exclude_products.py:74]
- `test_exclude_products_for_shipping_method_trigger_webhook` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_exclude_products.py:113]

**`saleor/graphql/shipping/tests/mutations/test_shipping_price_remove_product_from_exclude.py`**

- `test_remove_products_from_excluded_products_for_shipping_method_delete_all_products` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_remove_product_from_exclude.py:42]
- `test_remove_products_from_excluded_products_for_shipping_method` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_remove_product_from_exclude.py:80]
- `test_remove_products_from_excluded_products_for_shipping_method_trigger_webhook` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_remove_product_from_exclude.py:128]

**`saleor/graphql/shipping/tests/mutations/test_shipping_price_update.py`**

- `test_update_shipping_method` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_update.py:72]
- `test_update_shipping_method_trigger_webhook` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_update.py:114]
- `test_update_shipping_method_postal_codes` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_update.py:176]
- `test_update_shipping_method_minimum_delivery_days_higher_than_maximum` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_update.py:221]
- `test_update_shipping_method_minimum_delivery_days_below_0` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_update.py:259]
- `test_update_shipping_method_maximum_delivery_days_below_0` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_update.py:297]
- `test_update_shipping_method_minimum_delivery_days_higher_than_max_from_instance` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_update.py:335]
- `test_update_shipping_method_maximum_delivery_days_lower_than_min_from_instance` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_update.py:373]
- `test_update_shipping_method_multiple_errors` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_update.py:411]
- `test_update_shipping_method_delivery_days_without_value` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_price_update.py:464]

**`saleor/graphql/shipping/tests/mutations/test_shipping_zone_create.py`**

- `test_create_shipping_zone` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_create.py:61]
- `test_create_shipping_zone_trigger_webhook` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_create.py:101]
- `test_create_shipping_zone_with_empty_warehouses` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_create.py:160]
- `test_create_shipping_zone_without_warehouses_and_channels` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_create.py:188]
- `test_create_default_shipping_zone` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_create.py:222]
- `test_create_duplicated_default_shipping_zone` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_create.py:258]
- `test_create_shipping_zone_invalid_warehouses_no_channels_assigned` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_create.py:287]
- `test_create_shipping_zone_invalid_warehouses` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_create.py:318]

**`saleor/graphql/shipping/tests/mutations/test_shipping_zone_delete.py`**

- `test_delete_shipping_zone` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_delete.py:31]
- `test_delete_shipping_zone_trigger_webhook` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_delete.py:56]

**`saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py`**

- `test_update_shipping_zone` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:83]
- `test_update_shipping_zone_trigger_webhook` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:116]
- `test_update_shipping_zone_default_exists` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:168]
- `test_update_shipping_zone_add_warehouses` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:195]
- `test_update_shipping_zone_add_second_warehouses` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:232]
- `test_update_shipping_zone_remove_warehouses` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:269]
- `test_update_shipping_zone_remove_one_warehouses` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:299]
- `test_update_shipping_zone_replace_warehouse` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:332]
- `test_update_shipping_zone_same_warehouse_id_in_add_and_remove` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:370]
- `test_update_shipping_zone_add_channels` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:402]
- `test_update_shipping_zone_remove_channels` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:442]
- `test_update_shipping_zone_add_and_remove_channels` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:493]
- `test_update_shipping_zone_same_channel_id_in_add_and_remove_list` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:529]
- `test_update_shipping_zone_add_invalid_warehouses` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:565]
- `test_update_shipping_zone_add_warehouse_without_any_channel` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:617]
- `test_update_shipping_zone_add_warehouses_and_remove_common_channel` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:655]
- `test_update_shipping_zone_remove_channels_remove_common_warehouse_channel` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:690]
- `test_shipping_method_update_countries` (function) — [saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py:745]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/shipping/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/shipping/tests/mutations/test_bulk_delete.py` (177 lines)
- `saleor/graphql/shipping/tests/mutations/test_delivery_options_calculate.py` (463 lines)
- `saleor/graphql/shipping/tests/mutations/test_shipping_method_channel_listing_update.py` (795 lines)
- `saleor/graphql/shipping/tests/mutations/test_shipping_price_create.py` (552 lines)
- `saleor/graphql/shipping/tests/mutations/test_shipping_price_delete.py` (105 lines)
- `saleor/graphql/shipping/tests/mutations/test_shipping_price_exclude_products.py` (158 lines)
- `saleor/graphql/shipping/tests/mutations/test_shipping_price_remove_product_from_exclude.py` (181 lines)
- `saleor/graphql/shipping/tests/mutations/test_shipping_price_update.py` (501 lines)
- `saleor/graphql/shipping/tests/mutations/test_shipping_zone_create.py` (353 lines)
- `saleor/graphql/shipping/tests/mutations/test_shipping_zone_delete.py` (102 lines)
- `saleor/graphql/shipping/tests/mutations/test_shipping_zone_update.py` (769 lines)

## Interactions

- Imports from: `saleor/graphql/shipping/bulk_mutations`, `saleor/graphql/shipping/mutations`, `saleor/core`, `saleor/graphql`, `saleor/checkout/webhooks`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....checkout.delivery_context.fetch_shipping_methods_for_checkout`
- `.....checkout.models.Checkout`
- `.....checkout.models.CheckoutDelivery`
- `.....core.utils.json_serializer.CustomJsonEncoder`
- `.....shipping.error_codes.DeliveryOptionsCalculateErrorCode`
- `.....shipping.error_codes.ShippingErrorCode`
- `.....shipping.interface.ShippingMethodData`
- `.....shipping.models.ShippingMethod`
- `.....shipping.models.ShippingMethodChannelListing`
- `.....shipping.models.ShippingZone`
- `.....tests.utils.dummy_editorjs`
- `.....webhook.event_types.WebhookEventAsyncType`
- `.....webhook.payloads.generate_meta`
- `.....webhook.payloads.generate_requestor`
- `.....webhook.transport.shipping_helpers.to_shipping_app_id`
- `....core.enums.WeightUnitsEnum`
- `....core.utils.to_global_id_or_none`
- `....tests.utils.assert_negative_positive_decimal_value`
- `....tests.utils.get_graphql_content`
- `...types.PostalCodeRuleInclusionTypeEnum`
- `...types.ShippingMethodTypeEnum`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `35ca09f88cbc` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
