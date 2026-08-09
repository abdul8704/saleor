## Purpose

`saleor/graphql/warehouse/tests/mutations` (`saleor/graphql/warehouse/tests/mutations`) groups 6 source file(s) exposing 39 top-level declaration(s).

## Public surface

**`saleor/graphql/warehouse/tests/mutations/test_warehouse_create.py`**

- `test_mutation_create_warehouse` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_create.py:52]
- `test_mutation_create_warehouse_shipping_zone_provided` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_create.py:99]
- `test_mutation_create_warehouse_trigger_webhook` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_create.py:140]
- `test_mutation_create_warehouse_does_not_create_when_name_is_empty_string` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_create.py:195]
- `test_create_warehouse_creates_address` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_create.py:234]
- `test_create_warehouse_with_given_slug` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_create.py:282]
- `test_create_warehouse_with_non_unique_external_reference` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_create.py:314]
- `test_create_warehouse_with_address_item_from_valid_address_extension_map` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_create.py:350]
- `test_create_warehouse_invalid_address_skip_validation` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_create.py:396]

**`saleor/graphql/warehouse/tests/mutations/test_warehouse_delete.py`**

- `test_delete_warehouse_mutation` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_delete.py:32]
- `test_delete_warehouse_mutation_trigger_webhook` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_delete.py:55]
- `test_delete_warehouse_mutation_with_webhooks` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_delete.py:100]
- `test_delete_warehouse_mutation_with_webhooks_for_many_product_variants` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_delete.py:135]
- `test_delete_warehouse_deletes_associated_address` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_delete.py:163]
- `test_delete_warehouse_triggers_channel_out_of_stock_events` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_delete.py:185]
- `test_delete_warehouse_skips_channel_events_when_legacy_flag_enabled` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_delete.py:216]
- `test_delete_warehouse_skips_channel_events_when_no_stocks` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_delete.py:244]
- `test_delete_warehouse_fires_out_of_stock_in_channel_per_variant` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_delete.py:272]
- `test_delete_warehouse_does_not_fire_channel_event_when_another_warehouse_covers` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_delete.py:311]

**`saleor/graphql/warehouse/tests/mutations/test_warehouse_shipping_zone_assign.py`**

- `test_shipping_zone_can_be_assigned_only_to_one_warehouse` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_shipping_zone_assign.py:21]
- `test_shipping_zone_assign_to_warehouse` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_shipping_zone_assign.py:53]
- `test_shipping_zone_assign_to_warehouse_no_common_channel` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_shipping_zone_assign.py:80]
- `test_shipping_zone_assign_to_warehouse_no_zone_channels` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_shipping_zone_assign.py:117]
- `test_empty_shipping_zone_assign_to_warehouse` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_shipping_zone_assign.py:156]

**`saleor/graphql/warehouse/tests/mutations/test_warehouse_shipping_zone_unassign.py`**

- `test_shipping_zone_unassign_from_warehouse` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_shipping_zone_unassign.py:17]

**`saleor/graphql/warehouse/tests/mutations/test_warehouse_update.py`**

- `test_mutation_update_warehouse` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_update.py:47]
- `test_mutation_update_warehouse_with_non_unique_external_reference` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_update.py:87]
- `test_mutation_update_warehouse_trigger_webhook` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_update.py:118]
- `test_mutation_update_warehouse_can_update_address` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_update.py:164]
- `test_mutation_update_warehouse_to_country_with_different_validation_rules` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_update.py:202]
- `test_update_warehouse_slug` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_update.py:246]
- `test_update_warehouse_slug_exists` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_update.py:281]
- `test_update_warehouse_slug_and_name` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_update.py:339]
- `test_update_click_and_collect_option` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_update.py:395]
- `test_update_click_and_collect_option_invalid_input` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_update.py:437]
- `test_mutation_update_warehouse_by_external_reference` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_update.py:498]
- `test_update_warehouse_by_both_id_and_external_reference` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_update.py:529]
- `test_update_product_external_reference_not_existing` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_update.py:558]
- `test_update_warehouse_invalid_address_skip_validation` (function) — [saleor/graphql/warehouse/tests/mutations/test_warehouse_update.py:585]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/warehouse/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/warehouse/tests/mutations/test_warehouse_create.py` (428 lines)
- `saleor/graphql/warehouse/tests/mutations/test_warehouse_delete.py` (353 lines)
- `saleor/graphql/warehouse/tests/mutations/test_warehouse_shipping_zone_assign.py` (183 lines)
- `saleor/graphql/warehouse/tests/mutations/test_warehouse_shipping_zone_unassign.py` (38 lines)
- `saleor/graphql/warehouse/tests/mutations/test_warehouse_update.py` (619 lines)

## Interactions

- Imports from: `saleor/graphql/warehouse/mutations`, `saleor/warehouse`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....account.i18n_valid_address_extension.VALID_ADDRESS_EXTENSION_MAP`
- `.....account.models.Address`
- `.....core.utils.json_serializer.CustomJsonEncoder`
- `.....warehouse.WarehouseClickAndCollectOption`
- `.....warehouse.error_codes.WarehouseErrorCode`
- `.....warehouse.models.Stock`
- `.....warehouse.models.Warehouse`
- `.....webhook.event_types.WebhookEventAsyncType`
- `....tests.utils.get_graphql_content`
- `...enums.WarehouseClickAndCollectOptionEnum`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `dceab622b2b8` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
