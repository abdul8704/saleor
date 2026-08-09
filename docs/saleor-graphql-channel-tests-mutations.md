## Purpose

`saleor/graphql/channel/tests/mutations` (`saleor/graphql/channel/tests/mutations`) groups 8 source file(s) exposing 122 top-level declaration(s).

## Public surface

**`saleor/graphql/channel/tests/mutations/test_base_channel_listing.py`**

- `test_validate_duplicated_channel_ids` (function) — [saleor/graphql/channel/tests/mutations/test_base_channel_listing.py:11]
- `test_validate_duplicated_channel_ids_with_duplicates` (function) — [saleor/graphql/channel/tests/mutations/test_base_channel_listing.py:30]
- `test_validate_duplicated_channel_values` (function) — [saleor/graphql/channel/tests/mutations/test_base_channel_listing.py:47]
- `test_validate_duplicated_channel_values_with_duplicates` (function) — [saleor/graphql/channel/tests/mutations/test_base_channel_listing.py:65]
- `test_clean_channels_add_channels` (function) — [saleor/graphql/channel/tests/mutations/test_base_channel_listing.py:83]
- `test_clean_channels_remove_channels` (function) — [saleor/graphql/channel/tests/mutations/test_base_channel_listing.py:102]
- `test_clean_channels_remove_channels_is_null` (function) — [saleor/graphql/channel/tests/mutations/test_base_channel_listing.py:118]
- `test_test_clean_channels_with_errors` (function) — [saleor/graphql/channel/tests/mutations/test_base_channel_listing.py:134]
- `test_test_clean_channels_invalid_object_type` (function) — [saleor/graphql/channel/tests/mutations/test_base_channel_listing.py:150]

**`saleor/graphql/channel/tests/mutations/test_channel_activate.py`**

- `test_channel_activate_mutation` (function) — [saleor/graphql/channel/tests/mutations/test_channel_activate.py:32]
- `test_channel_activate_mutation_trigger_webhook` (function) — [saleor/graphql/channel/tests/mutations/test_channel_activate.py:59]
- `test_channel_activate_mutation_on_activated_channel` (function) — [saleor/graphql/channel/tests/mutations/test_channel_activate.py:108]

**`saleor/graphql/channel/tests/mutations/test_channel_create.py`**

- `test_channel_create_mutation_as_staff_user` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:83]
- `test_channel_create_mutation_as_app` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:149]
- `test_channel_create_mutation_as_customer` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:219]
- `test_channel_create_mutation_negative_expire_orders` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:251]
- `test_channel_create_draft_order_line_price_freeze_period_negative_value` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:292]
- `test_channel_create_mutation_disabled_expire_orders` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:334]
- `test_channel_create_mutation_as_anonymous` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:372]
- `test_channel_create_mutation_slugify_slug_field` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:398]
- `test_channel_create_mutation_with_duplicated_slug` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:429]
- `test_channel_create_mutation_with_shipping_zones` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:462]
- `test_channel_create_mutation_with_warehouses` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:510]
- `test_channel_create_mutation_trigger_webhook` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:563]
- `test_channel_create_creates_tax_configuration` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:625]
- `test_channel_create_set_order_mark_as_paid` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:651]
- `test_channel_create_set_default_transaction_flow_strategy` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:695]
- `test_channel_create_set_checkout_release_settings` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:741]
- `test_channel_create_set_incorect_checkout_ttl_before_releasing_funds` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:797]
- `test_channel_create_set_delete_expired_orders_after` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:835]
- `test_channel_create_mutation_negative_delete_expired_orders_after` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:877]
- `test_channel_create_mutation_set_incorrect_delete_expired_orders_after` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:915]
- `test_channel_create_set_checkout_use_legacy_error_flow` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:947]
- `test_channel_create_set_automatic_checkout_completion` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:984]
- `test_channel_create_set_automatic_checkout_completion_false` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:1039]
- `test_channel_create_with_automatic_completion_delay_value_below_0` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:1077]
- `test_channel_create_with_delay_exceeding_threshold` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:1119]
- `test_channel_create_with_new_automatic_completion_enabled_with_default_delay` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:1163]
- `test_channel_create_with_new_automatic_completion_enabled_with_custom_delay_and_cut_off` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:1210]
- `test_channel_create_with_automatic_completion_disabled` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:1264]
- `test_channel_create_with_automatic_completion_disabled_and_delay` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:1304]
- `test_channel_create_with_automatic_completion_disabled_and_cutoff` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:1342]
- `test_channel_create_with_both_old_and_new_automatic_completion_fields` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:1381]
- `test_channel_create_with_cutoff_later_than_threshold` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:1421]
- `test_channel_create_set_allow_unpaid_orders` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:1467]
- `test_channel_create_set_use_legacy_line_discount_propagation` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:1513]
- `test_channel_create_allow_legacy_gift_card_use` (function) — [saleor/graphql/channel/tests/mutations/test_channel_create.py:1555]

**`saleor/graphql/channel/tests/mutations/test_channel_deactivate.py`**

- `test_channel_deactivate_mutation` (function) — [saleor/graphql/channel/tests/mutations/test_channel_deactivate.py:32]
- `test_channel_deactivate_mutation_trigger_webhook` (function) — [saleor/graphql/channel/tests/mutations/test_channel_deactivate.py:57]
- `test_channel_deactivate_mutation_on_deactivated_channel` (function) — [saleor/graphql/channel/tests/mutations/test_channel_deactivate.py:104]

**`saleor/graphql/channel/tests/mutations/test_channel_delete.py`**

- `test_channel_delete_mutation_as_staff_user` (function) — [saleor/graphql/channel/tests/mutations/test_channel_delete.py:36]
- `test_channel_delete_mutation_with_the_same_channel_and_target_channel_id` (function) — [saleor/graphql/channel/tests/mutations/test_channel_delete.py:68]
- `test_channel_delete_mutation_without_migration_channel_with_orders` (function) — [saleor/graphql/channel/tests/mutations/test_channel_delete.py:88]
- `test_channel_delete_mutation_without_orders_in_channel` (function) — [saleor/graphql/channel/tests/mutations/test_channel_delete.py:117]
- `test_channel_delete_mutation_with_different_currency` (function) — [saleor/graphql/channel/tests/mutations/test_channel_delete.py:144]
- `test_channel_delete_mutation_as_app` (function) — [saleor/graphql/channel/tests/mutations/test_channel_delete.py:165]
- `test_channel_delete_mutation_as_customer` (function) — [saleor/graphql/channel/tests/mutations/test_channel_delete.py:198]
- `test_channel_delete_mutation_as_anonymous` (function) — [saleor/graphql/channel/tests/mutations/test_channel_delete.py:218]
- `test_channel_delete_mutation_trigger_webhook` (function) — [saleor/graphql/channel/tests/mutations/test_channel_delete.py:241]
- `test_channel_delete_mutation_deletes_invalid_warehouse_to_zone_relations` (function) — [saleor/graphql/channel/tests/mutations/test_channel_delete.py:293]
- `test_channel_delete_with_empty_id_returns_validation_error` (function) — [saleor/graphql/channel/tests/mutations/test_channel_delete.py:360]

**`saleor/graphql/channel/tests/mutations/test_channel_reorder_warehouses.py`**

- `test_sort_warehouses_with_channel` (function) — [saleor/graphql/channel/tests/mutations/test_channel_reorder_warehouses.py:41]
- `test_sort_warehouses_with_channel_invalid_channel_id` (function) — [saleor/graphql/channel/tests/mutations/test_channel_reorder_warehouses.py:102]
- `test_sort_warehouses_with_channel_not_existing_warehouse_ids` (function) — [saleor/graphql/channel/tests/mutations/test_channel_reorder_warehouses.py:131]
- `test_sort_warehouses_with_channel_not_invalid_warehouse_ids` (function) — [saleor/graphql/channel/tests/mutations/test_channel_reorder_warehouses.py:167]

**`saleor/graphql/channel/tests/mutations/test_channel_update.py`**

- `test_channel_update_mutation_as_staff_user` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:74]
- `test_channel_update_mutation_as_app` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:140]
- `test_channel_update_mutation_as_customer` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:173]
- `test_channel_update_mutation_as_anonymous` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:199]
- `test_channel_update_order_settings_anonymous_is_denied` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:255]
- `test_channel_update_mutation_slugify_slug_field` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:293]
- `test_channel_update_mutation_with_duplicated_slug` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:315]
- `test_channel_update_mutation_only_name` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:340]
- `test_channel_update_mutation_only_slug` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:375]
- `test_channel_update_mutation_add_shipping_zone` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:410]
- `test_channel_update_mutation_remove_shipping_zone` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:457]
- `test_channel_update_mutation_add_and_remove_shipping_zone` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:530]
- `test_channel_update_mutation_duplicated_shipping_zone` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:576]
- `test_channel_update_mutation_trigger_webhook` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:623]
- `test_channel_update_mutation_add_warehouse` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:692]
- `test_channel_update_mutation_remove_warehouse` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:737]
- `test_channel_update_mutation_add_and_remove_warehouse` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:820]
- `test_channel_update_mutation_duplicated_warehouses` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:870]
- `test_channel_update_mutation_disable_expire_orders` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:913]
- `test_channel_update_mutation_negative_expire_orders` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:948]
- `test_channel_update_order_settings_manage_orders` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:983]
- `test_channel_update_order_settings_empty_order_settings` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1027]
- `test_channel_update_order_settings_manage_orders_as_app` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1069]
- `test_channel_update_order_settings_manage_orders_permission_denied` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1105]
- `test_channel_update_order_settings_manage_orders_as_app_permission_denied` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1157]
- `test_channel_update_order_mark_as_paid_strategy` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1209]
- `test_channel_update_delete_expired_orders_after` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1250]
- `test_channel_update_mutation_negative_delete_expired_orders_after` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1292]
- `test_channel_update_set_incorrect_delete_expired_orders_after` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1326]
- `test_channel_update_order_settings_voucher_usage_disable` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1360]
- `test_channel_update_order_settings_voucher_usage_enable` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1424]
- `test_channel_update_draft_order_line_price_freeze_period` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1461]
- `test_channel_update_draft_order_line_price_freeze_period_negative_value` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1499]
- `test_channel_update_channel_settings` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1566]
- `test_channel_update_set_automatic_checkout_completion` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1629]
- `test_channel_update_set_automatic_checkout_completion_change_to_false` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1678]
- `test_channel_update_set_automatic_checkout_completion_false` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1726]
- `test_channel_update_with_automatic_completion_delay_below_0` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1768]
- `test_channel_update_with_delay_exceeding_threshold` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1805]
- `test_channel_update_with_new_automatic_completion_enabled_with_default_delay` (function) — [saleor/graphql/channel/tests/mutations/test_channel_update.py:1844]
- _…and 17 more in this file_

## How it works

The module's files, as provided to this run:

- `saleor/graphql/channel/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/channel/tests/mutations/test_base_channel_listing.py` (166 lines)
- `saleor/graphql/channel/tests/mutations/test_channel_activate.py` (126 lines)
- `saleor/graphql/channel/tests/mutations/test_channel_create.py` (1592 lines)
- `saleor/graphql/channel/tests/mutations/test_channel_deactivate.py` (124 lines)
- `saleor/graphql/channel/tests/mutations/test_channel_delete.py` (378 lines)
- `saleor/graphql/channel/tests/mutations/test_channel_reorder_warehouses.py` (194 lines)
- `saleor/graphql/channel/tests/mutations/test_channel_update.py` (2652 lines)

## Interactions

- Imports from: `saleor/core/utils`, `saleor/graphql/product/types`, `saleor/graphql/channel/mutations`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....channel.error_codes.ChannelErrorCode`
- `.....channel.models.Channel`
- `.....checkout.models.Checkout`
- `.....core.utils.json_serializer.CustomJsonEncoder`
- `.....discount.models.VoucherCode`
- `.....order.models.Order`
- `.....shipping.error_codes.ShippingErrorCode`
- `.....tax.models.TaxConfiguration`
- `.....warehouse.models.ChannelWarehouse`
- `.....webhook.event_types.WebhookEventAsyncType`
- `.....webhook.payloads.generate_meta`
- `.....webhook.payloads.generate_requestor`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `...mutations.BaseChannelListingMutation`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `d97b95b03e79` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
