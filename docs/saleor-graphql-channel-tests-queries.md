## Purpose

`saleor/graphql/channel/tests/queries` (`saleor/graphql/channel/tests/queries`) groups 3 source file(s) exposing 31 top-level declaration(s).

## Public surface

**`saleor/graphql/channel/tests/queries/test_channel.py`**

- `test_query_channel_as_staff_user` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:32]
- `test_query_channel_as_app` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:58]
- `test_query_channel_as_customer` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:85]
- `test_query_channel_as_anonymous` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:97]
- `test_query_channel_by_invalid_id` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:109]
- `test_query_channel_with_invalid_object_type` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:119]
- `test_query_channel_return_public_data_as_anonymous` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:162]
- `test_query_channel_missing_id_and_slug_in_query` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:174]
- `test_query_channel_returns_countries_attached_to_shipping_zone` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:192]
- `test_query_channel_returns_supported_shipping_methods` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:220]
- `test_query_channel_returns_supported_shipping_methods_with_countries_input` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:260]
- `test_query_channel_order_settings_as_staff_user` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:322]
- `test_query_channel_order_settings_as_app` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:383]
- `test_query_channel_order_settings_as_staff_user_no_permission` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:437]
- `test_query_channel_order_settings_as_app_no_permission` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:454]
- `test_query_channel_checkout_settings_as_staff_user` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:486]
- `test_query_channel_checkout_settings_as_app` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:529]
- `test_query_channel_checkout_settings_as_staff_user_no_permission` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:559]
- `test_query_channel_checkout_settings_as_app_no_permission` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:576]
- `test_query_channel_checkout_settings_with_manage_checkouts` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:594]
- `test_query_channel_payment_settings_as_staff_user` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:642]
- `test_query_channel_payment_settings_as_app` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:670]
- `test_query_channel_payment_settings_as_staff_user_no_permission` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:696]
- `test_query_channel_payment_settings_as_app_no_permission` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:713]
- `test_query_channel_payment_settings_with_handle_payments` (function) — [saleor/graphql/channel/tests/queries/test_channel.py:731]

**`saleor/graphql/channel/tests/queries/test_channels.py`**

- `test_query_channels_as_staff_user` (function) — [saleor/graphql/channel/tests/queries/test_channels.py:18]
- `test_query_channels_as_app` (function) — [saleor/graphql/channel/tests/queries/test_channels.py:48]
- `test_query_channels_as_customer` (function) — [saleor/graphql/channel/tests/queries/test_channels.py:78]
- `test_query_channels_as_anonymous` (function) — [saleor/graphql/channel/tests/queries/test_channels.py:88]
- `test_query_channels_with_has_orders_order` (function) — [saleor/graphql/channel/tests/queries/test_channels.py:110]
- `test_query_channels_with_has_orders_without_permission` (function) — [saleor/graphql/channel/tests/queries/test_channels.py:140]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/channel/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/channel/tests/queries/test_channel.py` (756 lines)
- `saleor/graphql/channel/tests/queries/test_channels.py` (149 lines)

## Interactions

- Imports from: `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....channel.TransactionFlowStrategy`
- `.....shipping.models.ShippingMethodChannelListing`
- `.....shipping.models.ShippingZone`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `...enums.AllocationStrategyEnum`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `8dc7b3d3fc2d` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
