## Purpose

`saleor/graphql/order/tests` (`saleor/graphql/order/tests`) groups 10 source file(s) exposing 64 top-level declaration(s).

## Public surface

**`saleor/graphql/order/tests/dataloaders/test_order_shipping_methods.py`**

- `test_batch_load_single_order` (function) — [saleor/graphql/order/tests/dataloaders/test_order_shipping_methods.py:16]
- `test_batch_load_missing_order_returns_empty_list` (function) — [saleor/graphql/order/tests/dataloaders/test_order_shipping_methods.py:31]
- `test_batch_load_mixed_existing_and_missing_orders` (function) — [saleor/graphql/order/tests/dataloaders/test_order_shipping_methods.py:47]

**`saleor/graphql/order/tests/test_draft_order_validate.py`**

- `test_validate_draft_order` (function) — [saleor/graphql/order/tests/test_draft_order_validate.py:13]
- `test_validate_draft_order_without_sku` (function) — [saleor/graphql/order/tests/test_draft_order_validate.py:27]
- `test_validate_draft_order_wrong_shipping` (function) — [saleor/graphql/order/tests/test_draft_order_validate.py:43]
- `test_validate_draft_order_no_order_lines` (function) — [saleor/graphql/order/tests/test_draft_order_validate.py:61]
- `test_validate_draft_order_non_existing_variant` (function) — [saleor/graphql/order/tests/test_draft_order_validate.py:75]
- `test_validate_draft_order_with_unpublished_product` (function) — [saleor/graphql/order/tests/test_draft_order_validate.py:95]
- `test_validate_draft_order_with_unavailable_for_purchase_product` (function) — [saleor/graphql/order/tests/test_draft_order_validate.py:119]
- `test_validate_draft_order_with_product_available_for_purchase_in_future` (function) — [saleor/graphql/order/tests/test_draft_order_validate.py:141]
- `test_validate_draft_order_out_of_stock_variant` (function) — [saleor/graphql/order/tests/test_draft_order_validate.py:168]
- `test_validate_draft_order_no_shipping_address` (function) — [saleor/graphql/order/tests/test_draft_order_validate.py:189]
- `test_validate_draft_order_no_billing_address` (function) — [saleor/graphql/order/tests/test_draft_order_validate.py:206]
- `test_validate_draft_order_no_shipping_method` (function) — [saleor/graphql/order/tests/test_draft_order_validate.py:223]
- `test_validate_draft_order_no_shipping_method_shipping_not_required` (function) — [saleor/graphql/order/tests/test_draft_order_validate.py:241]
- `test_validate_draft_order_no_shipping_address_no_method_shipping_not_required` (function) — [saleor/graphql/order/tests/test_draft_order_validate.py:261]
- `test_validate_draft_order_voucher` (function) — [saleor/graphql/order/tests/test_draft_order_validate.py:282]

**`saleor/graphql/order/tests/test_filters.py`**

- `similar_customers_with_orders` (function) — [saleor/graphql/order/tests/test_filters.py:14]
- `test_filter_customer_by_email` (function) — [saleor/graphql/order/tests/test_filters.py:39]
- `test_filter_customer_by_first_name` (function) — [saleor/graphql/order/tests/test_filters.py:67]
- `test_filter_customer_by_last_name` (function) — [saleor/graphql/order/tests/test_filters.py:96]
- `test_filter_customer_by_full_name_first_last_name` (function) — [saleor/graphql/order/tests/test_filters.py:125]
- `test_filter_customer_by_full_name_last_first_name` (function) — [saleor/graphql/order/tests/test_filters.py:153]
- `test_filter_customer_by_email_domain` (function) — [saleor/graphql/order/tests/test_filters.py:181]

**`saleor/graphql/order/tests/test_homepage.py`**

- `order_events_from_different_channels` (function) — [saleor/graphql/order/tests/test_homepage.py:27]
- `test_homepage_events` (function) — [saleor/graphql/order/tests/test_homepage.py:57]
- `test_query_homepage_events_by_user_with_restricted_access_to_channels` (function) — [saleor/graphql/order/tests/test_homepage.py:86]
- `test_query_homepage_by_user_with_restricted_access_to_channels_no_acc_channels` (function) — [saleor/graphql/order/tests/test_homepage.py:115]
- `test_query_homepage_by_app` (function) — [saleor/graphql/order/tests/test_homepage.py:133]
- `test_query_homepage_by_customer` (function) — [saleor/graphql/order/tests/test_homepage.py:155]
- `test_orders_total` (function) — [saleor/graphql/order/tests/test_homepage.py:183]
- `test_orders_total_channel_pln` (function) — [saleor/graphql/order/tests/test_homepage.py:204]
- `test_orders_total_not_existing_channel` (function) — [saleor/graphql/order/tests/test_homepage.py:225]
- `test_orders_total_as_staff` (function) — [saleor/graphql/order/tests/test_homepage.py:243]
- `test_orders_total_no_access_to_channel` (function) — [saleor/graphql/order/tests/test_homepage.py:264]
- `test_orders_total_as_app` (function) — [saleor/graphql/order/tests/test_homepage.py:280]
- `test_orders_total_as_customer` (function) — [saleor/graphql/order/tests/test_homepage.py:302]
- `test_orders_total_as_anonymous` (function) — [saleor/graphql/order/tests/test_homepage.py:318]
- `test_orders_total_count_without_channel` (function) — [saleor/graphql/order/tests/test_homepage.py:343]
- `test_orders_total_count_channel_USD` (function) — [saleor/graphql/order/tests/test_homepage.py:370]
- `test_orders_total_count_channel_PLN` (function) — [saleor/graphql/order/tests/test_homepage.py:398]
- `test_orders_total_count_as_staff` (function) — [saleor/graphql/order/tests/test_homepage.py:426]
- `test_orders_total_count_as_app` (function) — [saleor/graphql/order/tests/test_homepage.py:454]
- `test_orders_total_count_as_customer` (function) — [saleor/graphql/order/tests/test_homepage.py:483]
- `test_orders_total_count_as_anonymous` (function) — [saleor/graphql/order/tests/test_homepage.py:508]

**`saleor/graphql/order/tests/test_order_clean.py`**

- `test_clean_order_refund_payment` (function) — [saleor/graphql/order/tests/test_order_clean.py:14]
- `test_clean_order_capture` (function) — [saleor/graphql/order/tests/test_order_clean.py:22]
- `test_clean_order_cancel` (function) — [saleor/graphql/order/tests/test_order_clean.py:39]
- `test_clean_order_cancel_draft_order` (function) — [saleor/graphql/order/tests/test_order_clean.py:47]
- `test_clean_order_cancel_expired_order` (function) — [saleor/graphql/order/tests/test_order_clean.py:62]
- `test_clean_order_cancel_canceled_order` (function) — [saleor/graphql/order/tests/test_order_clean.py:77]
- `test_clean_order_cancel_order_with_fulfillment` (function) — [saleor/graphql/order/tests/test_order_clean.py:92]

**`saleor/graphql/order/tests/test_order_payment.py`**

- `test_clean_payment_without_payment_associated_to_order` (function) — [saleor/graphql/order/tests/test_order_payment.py:16]
- `test_try_payment_action_generates_event` (function) — [saleor/graphql/order/tests/test_order_payment.py:50]
- `test_try_payment_action_generates_app_event` (function) — [saleor/graphql/order/tests/test_order_payment.py:79]

**`saleor/graphql/order/tests/test_utils.py`**

- `test_invalidate_order_prices_status` (function) — [saleor/graphql/order/tests/test_utils.py:17]
- `test_invalidate_order_prices_save` (function) — [saleor/graphql/order/tests/test_utils.py:36]
- `test_save_addresses_both_addresses` (function) — [saleor/graphql/order/tests/test_utils.py:51]
- `test_save_addresses_only_billing_address` (function) — [saleor/graphql/order/tests/test_utils.py:67]
- `test_save_addresses_only_shipping_address` (function) — [saleor/graphql/order/tests/test_utils.py:82]
- `test_save_addresses_empty` (function) — [saleor/graphql/order/tests/test_utils.py:97]

**`saleor/graphql/order/tests/utils.py`**

- `assert_order_and_payment_ids` (function) — [saleor/graphql/order/tests/utils.py:6]
- `assert_proper_webhook_called_once` (function) — [saleor/graphql/order/tests/utils.py:15]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/order/tests/__init__.py` (1 lines)
- `saleor/graphql/order/tests/dataloaders/__init__.py` (1 lines)
- `saleor/graphql/order/tests/dataloaders/test_order_shipping_methods.py` (61 lines)
- `saleor/graphql/order/tests/test_draft_order_validate.py` (298 lines)
- `saleor/graphql/order/tests/test_filters.py` (199 lines)
- `saleor/graphql/order/tests/test_homepage.py` (530 lines)
- `saleor/graphql/order/tests/test_order_clean.py` (104 lines)
- `saleor/graphql/order/tests/test_order_payment.py` (101 lines)
- `saleor/graphql/order/tests/test_utils.py` (107 lines)
- `saleor/graphql/order/tests/utils.py` (21 lines)

## Interactions

- Imports from: `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....shipping.interface.ShippingMethodData`
- `....account.models.Address`
- `....context.SaleorContext`
- `....order.FulfillmentStatus`
- `....order.OrderEvents`
- `....order.OrderStatus`
- `....order.error_codes.OrderErrorCode`
- `....order.events`
- `....order.models.Order`
- `....order.models.OrderEvent`
- `....order.utils.invalidate_order_prices`
- `....payment.PaymentError`
- `....payment.models.Payment`
- `....plugins.manager.get_plugins_manager`
- `....product.models.ProductVariant`
- `...core.enums.ReportingPeriod`
- `...dataloaders.OrderShippingMethodsByOrderIdAndWebhookSyncLoader`
- `...tests.utils.assert_no_permission`
- `...tests.utils.get_graphql_content`
- `..mutations.order_cancel.clean_order_cancel`
- `..mutations.order_capture.clean_order_capture`
- `..mutations.order_refund.clean_refund_payment`
- `..mutations.utils.save_addresses`
- `..mutations.utils.try_payment_action`
- `..utils.validate_draft_order`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `7c960503f13e` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
