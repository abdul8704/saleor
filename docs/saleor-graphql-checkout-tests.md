## Purpose

`saleor/graphql/checkout/tests` (`saleor/graphql/checkout/tests`) groups 12 source file(s) exposing 222 top-level declaration(s).

## Public surface

**`saleor/graphql/checkout/tests/test_checkout_discount_expiration.py`**

- `test_checkout_basic_fields_no_recalculation` (function) — [saleor/graphql/checkout/tests/test_checkout_discount_expiration.py:74]
- `test_checkout_gift_promotion_changed_only_line_id` (function) — [saleor/graphql/checkout/tests/test_checkout_discount_expiration.py:119]
- `test_checkout_gift_promotion_changed_with_line_prices` (function) — [saleor/graphql/checkout/tests/test_checkout_discount_expiration.py:197]
- `test_checkout_gift_promotion_removed_only_line_id` (function) — [saleor/graphql/checkout/tests/test_checkout_discount_expiration.py:283]
- `test_checkout_gift_promotion_removed_with_line_prices` (function) — [saleor/graphql/checkout/tests/test_checkout_discount_expiration.py:345]
- `test_checkout_gift_promotion_added_only_line_id` (function) — [saleor/graphql/checkout/tests/test_checkout_discount_expiration.py:407]
- `test_checkout_gift_promotion_added_with_line_prices` (function) — [saleor/graphql/checkout/tests/test_checkout_discount_expiration.py:487]
- `test_checkout_lines_with_prices_price_expiration_in_future_no_recalculation` (function) — [saleor/graphql/checkout/tests/test_checkout_discount_expiration.py:583]

**`saleor/graphql/checkout/tests/test_checkout_filters.py`**

- `test_checkout_query_with_filter_channels_with_one_channel` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:35]
- `test_checkout_query_with_filter_channels_without_channel` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:58]
- `test_checkout_query_with_filter_channels_with_many_channel` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:79]
- `test_checkout_query_with_filter_channels_with_empty_channel` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:106]
- `test_checkout_query_with_filter_created` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:180]
- `test_checkouts_query_with_filter_customer_fields` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:212]
- `test_query_checkout_with_sort` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:272]
- `test_checkouts_query_with_filter_search` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:348]
- `test_checkouts_query_with_filter_search_by_global_payment_id` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:410]
- `test_checkouts_search_exact_match_prioritized` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:449]
- `test_filtering_checkout_discounted_object_by_transaction_psp_reference` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:530]
- `test_checkouts_query_with_filter_search_by_token` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:559]
- `test_checkouts_query_with_filter_authorize_status` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:646]
- `test_checkouts_query_with_filter_charge_status` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:748]
- `test_filtering_checkout_discounted_object_where_by_base_total_price_range` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:788]
- `test_filtering_checkout_discounted_object_where_by_base_total_price_one_of` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:833]
- `test_filtering_checkout_discounted_object_where_by_base_total_currency_not_given` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:871]
- `test_filtering_checkout_discounted_object_where_by_base_subtotal_price_range` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:915]
- `test_filtering_checkout_discounted_object_where_by_base_subtotal_price_one_of` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:960]
- `test_filtering_checkout_discounted_object_where_by_base_subtotal_currency_not_given` (function) — [saleor/graphql/checkout/tests/test_checkout_filters.py:998]

**`saleor/graphql/checkout/tests/test_checkout_line_problems.py`**

- `test_line_without_any_problem` (function) — [saleor/graphql/checkout/tests/test_checkout_line_problems.py:59]
- `test_line_variant_without_stock` (function) — [saleor/graphql/checkout/tests/test_checkout_line_problems.py:76]
- `test_line_variant_with_insufficient_stock` (function) — [saleor/graphql/checkout/tests/test_checkout_line_problems.py:123]
- `test_line_variant_without_tracking_inventory` (function) — [saleor/graphql/checkout/tests/test_checkout_line_problems.py:176]
- `test_lines_with_same_variant` (function) — [saleor/graphql/checkout/tests/test_checkout_line_problems.py:206]
- `test_product_is_not_published` (function) — [saleor/graphql/checkout/tests/test_checkout_line_problems.py:276]
- `test_product_doesnt_have_channel_listing` (function) — [saleor/graphql/checkout/tests/test_checkout_line_problems.py:317]
- `test_product_is_not_available_to_purchase` (function) — [saleor/graphql/checkout/tests/test_checkout_line_problems.py:361]
- `test_product_variant_doesnt_have_channel_listing` (function) — [saleor/graphql/checkout/tests/test_checkout_line_problems.py:404]
- `test_product_variant_channel_listing_doesnt_have_price_amount` (function) — [saleor/graphql/checkout/tests/test_checkout_line_problems.py:447]
- `test_query_checkouts_do_not_trigger_sync_tax_webhooks_when_variant_not_available` (function) — [saleor/graphql/checkout/tests/test_checkout_line_problems.py:572]
- `test_query_checkouts_calculate_flat_taxes_when_variant_not_available` (function) — [saleor/graphql/checkout/tests/test_checkout_line_problems.py:627]
- `test_query_checkouts_do_not_trigger_sync_tax_webhooks_when_out_of_stock` (function) — [saleor/graphql/checkout/tests/test_checkout_line_problems.py:676]
- `test_query_checkouts_calculate_flat_taxes_when_variant_out_of_stock` (function) — [saleor/graphql/checkout/tests/test_checkout_line_problems.py:734]

**`saleor/graphql/checkout/tests/test_checkout_no_shipping_needed.py`**

- `test_checkout_has_no_available_shipping_methods` (function) — [saleor/graphql/checkout/tests/test_checkout_no_shipping_needed.py:10]
- `test_do_not_remove_shipping_method_if_only_non_shippable_products_in_checkout` (function) — [saleor/graphql/checkout/tests/test_checkout_no_shipping_needed.py:44]

**`saleor/graphql/checkout/tests/test_checkout_price_expiration.py`**

- `test_checkout_lines_add_invalidate_prices` (function) — [saleor/graphql/checkout/tests/test_checkout_price_expiration.py:27]
- `test_checkout_lines_update_invalidate_prices` (function) — [saleor/graphql/checkout/tests/test_checkout_price_expiration.py:73]
- `test_checkout_lines_delete_invalidate_prices` (function) — [saleor/graphql/checkout/tests/test_checkout_price_expiration.py:121]
- `test_checkout_shipping_address_update_invalidate_prices` (function) — [saleor/graphql/checkout/tests/test_checkout_price_expiration.py:166]
- `test_checkout_billing_address_update_invalidate_prices` (function) — [saleor/graphql/checkout/tests/test_checkout_price_expiration.py:212]
- `test_checkout_shipping_method_update_invalidate_prices` (function) — [saleor/graphql/checkout/tests/test_checkout_price_expiration.py:256]
- `test_checkout_delivery_method_update_invalidate_prices` (function) — [saleor/graphql/checkout/tests/test_checkout_price_expiration.py:299]
- `test_invalidate_checkout_with_save` (function) — [saleor/graphql/checkout/tests/test_checkout_price_expiration.py:327]
- `test_invalidate_checkout_without_save` (function) — [saleor/graphql/checkout/tests/test_checkout_price_expiration.py:351]

**`saleor/graphql/checkout/tests/test_checkout_problems.py`**

- `test_checkout_without_problems` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:49]
- `test_checkout_without_shipping` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:64]
- `test_checkout_with_out_of_stock_when_stocks_dont_exist` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:80]
- `test_checkout_problem_out_of_stock_without_available_quantity` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:112]
- `test_checkout_problems_with_reservation` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:148]
- `test_checkout_with_out_of_stock_with_allocations_and_not_enough_items` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:179]
- `test_checkout_out_of_stock_without_tracking_inventory` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:228]
- `test_checkout_with_multiple_same_variant_and_out_of_stock` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:251]
- `test_checkout_problems_when_product_is_not_published` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:291]
- `test_checkout_problems_when_product_doesnt_have_channel_listing` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:320]
- `test_checkout_problems_when_product_is_not_available_to_purchase` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:350]
- `test_checkout_problems_when_product_variant_doesnt_have_channel_listing` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:379]
- `test_checkout_problems_when_variant_channel_listing_doesnt_have_price_amount` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:408]
- `test_checkout_problems_delivery_method_stale` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:440]
- `test_checkout_problems_delivery_method_invalid` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:464]
- `test_checkout_problems_delivery_method_invalid_when_active_set_to_false` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:488]
- `test_checkout_problems_delivery_method_stale_and_invalid` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:512]
- `test_checkout_problems_without_delivery_method` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:547]
- `test_checkout_problem_insufficient_stock_warehouse_without_shipping_zones` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:568]
- `test_checkout_problem_no_insufficient_stock_warehouse_without_shipping_zones_excluded_from_stock_calculations` (function) — [saleor/graphql/checkout/tests/test_checkout_problems.py:594]

**`saleor/graphql/checkout/tests/test_checkout_promo_codes.py`**

- `test_checkout_totals_use_discounts` (function) — [saleor/graphql/checkout/tests/test_checkout_promo_codes.py:8]
- `test_checkout_get_gift_card_code` (function) — [saleor/graphql/checkout/tests/test_checkout_promo_codes.py:87]
- `test_checkout_get_gift_card_codes` (function) — [saleor/graphql/checkout/tests/test_checkout_promo_codes.py:99]
- `test_checkout_get_gift_card_code_without_gift_card` (function) — [saleor/graphql/checkout/tests/test_checkout_promo_codes.py:131]

**`saleor/graphql/checkout/tests/test_checkout.py`**

- `expected_dummy_gateway` (function) — [saleor/graphql/checkout/tests/test_checkout.py:69]
- `expected_gift_card_payment_gateway` (function) — [saleor/graphql/checkout/tests/test_checkout.py:79]
- `subscription_shipping_list_methods_for_checkout_webhook` (function) — [saleor/graphql/checkout/tests/test_checkout.py:108]
- `test_checkout_available_payment_gateways` (function) — [saleor/graphql/checkout/tests/test_checkout.py:134]
- `test_checkout_available_payment_gateways_valid_info_sent` (function) — [saleor/graphql/checkout/tests/test_checkout.py:153]
- `test_checkout_available_payment_gateways_currency_specified_USD` (function) — [saleor/graphql/checkout/tests/test_checkout.py:182]
- `test_checkout_available_payment_gateways_currency_specified_EUR` (function) — [saleor/graphql/checkout/tests/test_checkout.py:206]
- `test_checkout_selected_shipping_method` (function) — [saleor/graphql/checkout/tests/test_checkout.py:270]
- `test_checkout_selected_shipping_method_as_staff` (function) — [saleor/graphql/checkout/tests/test_checkout.py:340]
- `test_checkout_available_shipping_methods` (function) — [saleor/graphql/checkout/tests/test_checkout.py:423]
- `test_query_checkout_empty_address_with_shipping_method_without_exclude_webhook` (function) — [saleor/graphql/checkout/tests/test_checkout.py:488]
- `test_query_checkout_with_address_with_shipping_method_without_exclude_webhook` (function) — [saleor/graphql/checkout/tests/test_checkout.py:514]
- `test_preventing_circular_payload_generation_when_listing_shipping_methods_for_checkout` (function) — [saleor/graphql/checkout/tests/test_checkout.py:539]
- `test_checkout_available_shipping_methods_with_weight_based_shipping_method` (function) — [saleor/graphql/checkout/tests/test_checkout.py:600]
- `test_checkout_available_shipping_methods_weight_method_with_higher_minimal_weigh` (function) — [saleor/graphql/checkout/tests/test_checkout.py:632]
- `test_checkout_deliveries_with_price_based_shipping_method_and_discount` (function) — [saleor/graphql/checkout/tests/test_checkout.py:660]
- `test_checkout_deliveries_with_price_based_shipping_and_shipping_discount` (function) — [saleor/graphql/checkout/tests/test_checkout.py:699]
- `test_checkout_deliveries_with_price_based_method_and_product_voucher` (function) — [saleor/graphql/checkout/tests/test_checkout.py:743]
- `test_checkout_available_shipping_methods_shipping_zone_without_channels` (function) — [saleor/graphql/checkout/tests/test_checkout.py:804]
- `test_checkout_available_shipping_methods_excluded_postal_codes` (function) — [saleor/graphql/checkout/tests/test_checkout.py:820]
- `test_checkout_available_shipping_methods_with_price_displayed` (function) — [saleor/graphql/checkout/tests/test_checkout.py:840]
- `test_checkout_no_available_shipping_methods_without_address` (function) — [saleor/graphql/checkout/tests/test_checkout.py:884]
- `test_checkout_no_available_shipping_methods_without_lines` (function) — [saleor/graphql/checkout/tests/test_checkout.py:896]
- `test_available_collection_points_for_preorders_variants_in_checkout` (function) — [saleor/graphql/checkout/tests/test_checkout.py:931]
- `test_available_collection_points_for_preorders_and_regular_variants_in_checkout` (function) — [saleor/graphql/checkout/tests/test_checkout.py:957]
- `test_checkout_available_collection_points_with_lines_avail_in_1_local_and_1_all` (function) — [saleor/graphql/checkout/tests/test_checkout.py:989]
- `test_checkout_available_collection_points_with_line_avail_in_2_local_and_1_all` (function) — [saleor/graphql/checkout/tests/test_checkout.py:1014]
- `test_checkout_available_collection_points_two_lines_for_same_checkout` (function) — [saleor/graphql/checkout/tests/test_checkout.py:1035]
- `test_checkout_avail_collect_points_only_all_warehouse_quantity_collected` (function) — [saleor/graphql/checkout/tests/test_checkout.py:1065]
- `test_checkout_avail_collect_points_all_warehouse_quantity_from_disabled_warehouse` (function) — [saleor/graphql/checkout/tests/test_checkout.py:1104]
- `test_checkout_avail_collect_points_returns_empty_list_when_no_channels` (function) — [saleor/graphql/checkout/tests/test_checkout.py:1139]
- `test_checkout_avail_collect_fallbacks_to_channel_country_when_no_shipping_address` (function) — [saleor/graphql/checkout/tests/test_checkout.py:1153]
- `test_checkout_reservation_date_for_stock_reservation` (function) — [saleor/graphql/checkout/tests/test_checkout.py:1182]
- `test_checkout_reservation_date_for_preorder_reservation` (function) — [saleor/graphql/checkout/tests/test_checkout.py:1198]
- `test_checkout_reservation_date_for_multiple_reservations` (function) — [saleor/graphql/checkout/tests/test_checkout.py:1214]
- `test_checkout_reservation_date_for_multiple_reservations_types` (function) — [saleor/graphql/checkout/tests/test_checkout.py:1231]
- `test_checkout_reservation_date_for_expired_reservations` (function) — [saleor/graphql/checkout/tests/test_checkout.py:1255]
- `test_checkout_reservation_date_for_no_reservations` (function) — [saleor/graphql/checkout/tests/test_checkout.py:1278]
- `test_checkout_reservation_date_for_disabled_reservations` (function) — [saleor/graphql/checkout/tests/test_checkout.py:1297]
- `test_anonymous_client_can_fetch_anonymous_checkout_user` (function) — [saleor/graphql/checkout/tests/test_checkout.py:1323]
- _…and 97 more in this file_

**`saleor/graphql/checkout/tests/test_checkouts_query.py`**

- `test_query_checkouts_do_not_trigger_external_shipping_webhook_with_flat_rates` (function) — [saleor/graphql/checkout/tests/test_checkouts_query.py:69]
- `test_query_checkouts_do_not_trigger_external_shipping_webhook_with_tax_app` (function) — [saleor/graphql/checkout/tests/test_checkouts_query.py:126]
- `test_query_checkouts_do_not_trigger_exclude_shipping_webhooks_with_flat_rates` (function) — [saleor/graphql/checkout/tests/test_checkouts_query.py:184]
- `test_query_checkouts_do_not_trigger_exclude_shipping_webhooks_with_tax_app` (function) — [saleor/graphql/checkout/tests/test_checkouts_query.py:240]

**`saleor/graphql/checkout/tests/test_utils.py`**

- `test_apply_gift_reward_if_applicable` (function) — [saleor/graphql/checkout/tests/test_utils.py:4]
- `test_apply_gift_reward_if_applicable_no_gift_promotion_rules` (function) — [saleor/graphql/checkout/tests/test_utils.py:22]
- `test_apply_gift_reward_if_applicable_no_gift_promotion_rules_for_checkout_channel` (function) — [saleor/graphql/checkout/tests/test_utils.py:37]

**`saleor/graphql/checkout/tests/utils.py`**

- `assert_address_data` (function) — [saleor/graphql/checkout/tests/utils.py:1]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/checkout/tests/__init__.py` (1 lines)
- `saleor/graphql/checkout/tests/test_checkout_discount_expiration.py` (658 lines)
- `saleor/graphql/checkout/tests/test_checkout_filters.py` (1039 lines)
- `saleor/graphql/checkout/tests/test_checkout_line_problems.py` (774 lines)
- `saleor/graphql/checkout/tests/test_checkout_no_shipping_needed.py` (59 lines)
- `saleor/graphql/checkout/tests/test_checkout_price_expiration.py` (373 lines)
- `saleor/graphql/checkout/tests/test_checkout_problems.py` (615 lines)
- `saleor/graphql/checkout/tests/test_checkout_promo_codes.py` (138 lines)
- `saleor/graphql/checkout/tests/test_checkout.py` (5406 lines)
- `saleor/graphql/checkout/tests/test_checkouts_query.py` (292 lines)
- `saleor/graphql/checkout/tests/test_utils.py` (50 lines)
- `saleor/graphql/checkout/tests/utils.py` (13 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/checkout/webhooks`, `saleor/graphql/checkout/mutations`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....account.models.User`
- `....checkout.base_calculations`
- `....checkout.calculations`
- `....checkout.calculations._fetch_checkout_prices_if_expired`
- `....checkout.error_codes.CheckoutErrorCode`
- `....checkout.fetch.fetch_checkout_info`
- `....checkout.fetch.fetch_checkout_lines`
- `....checkout.models.Checkout`
- `....checkout.payment_utils.update_checkout_payment_statuses`
- `....checkout.search.indexing.update_checkouts_search_vector`
- `....checkout.tests.utils.add_variant_to_checkout`
- `....checkout.utils.invalidate_checkout`
- `....core.db.connection.allow_writer`
- `....core.prices.quantize_price`
- `....discount.DiscountValueType`
- `....discount.VoucherType`
- `....payment.TransactionAction`
- `....payment.models.ChargeStatus`
- `....payment.models.Payment`
- `....plugins.manager.get_plugins_manager`
- `....plugins.tests.sample_plugins.ActiveDummyPaymentGateway`
- `....product.models.ProductChannelListing`
- `....product.models.ProductVariantChannelListing`
- `....shipping.models.ShippingMethod`
- `....shipping.models.ShippingMethodTranslation`
- `....tests.race_condition`
- `....tests.utils.dummy_editorjs`
- `....warehouse.WarehouseClickAndCollectOption`
- `....warehouse.models.Allocation`
- `....warehouse.models.PreorderReservation`
- `....warehouse.models.Reservation`
- `....warehouse.models.Stock`
- `....warehouse.models.Warehouse`
- `....webhook.event_types.WebhookEventSyncType`
- `...core.connection.where_filter_qs`
- `...core.utils.to_global_id_or_none`
- `...payment.enums.TokenizedPaymentFlowEnum`
- `...tests.utils.assert_no_permission`
- `...tests.utils.get_graphql_content`
- `..enums.CheckoutAuthorizeStatusEnum`
- `..enums.CheckoutChargeStatusEnum`
- `..filters.CheckoutDiscountedObjectWhere`
- `..mutations.utils.apply_gift_reward_if_applicable_on_checkout_creation`
- `..mutations.utils.mark_checkout_deliveries_as_stale_if_needed`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `772a217964b5` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
