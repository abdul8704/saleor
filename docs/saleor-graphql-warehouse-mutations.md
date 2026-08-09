## Purpose

`saleor/graphql/warehouse/mutations` (`saleor/graphql/warehouse/mutations`) groups 7 source file(s) exposing 29 top-level declaration(s).

## Public surface

**`saleor/graphql/warehouse/mutations/base.py`**

- `WarehouseMixin` (class) — [saleor/graphql/warehouse/mutations/base.py:12]
- `clean_input` (function) — [saleor/graphql/warehouse/mutations/base.py:14]

**`saleor/graphql/warehouse/mutations/warehouse_create.py`**

- `WarehouseCreate` (class) — [saleor/graphql/warehouse/mutations/warehouse_create.py:13]
- `Arguments` (class) — [saleor/graphql/warehouse/mutations/warehouse_create.py:16]
- `Meta` (class) — [saleor/graphql/warehouse/mutations/warehouse_create.py:21]
- `prepare_address` (function) — [saleor/graphql/warehouse/mutations/warehouse_create.py:30]
- `post_save_action` (function) — [saleor/graphql/warehouse/mutations/warehouse_create.py:37]
- `perform_mutation` (function) — [saleor/graphql/warehouse/mutations/warehouse_create.py:42]

**`saleor/graphql/warehouse/mutations/warehouse_delete.py`**

- `WarehouseDelete` (class) — [saleor/graphql/warehouse/mutations/warehouse_delete.py:25]
- `Meta` (class) — [saleor/graphql/warehouse/mutations/warehouse_delete.py:26]
- `Arguments` (class) — [saleor/graphql/warehouse/mutations/warehouse_delete.py:69]
- `perform_mutation` (function) — [saleor/graphql/warehouse/mutations/warehouse_delete.py:73]
- `post_save_action` (function) — [saleor/graphql/warehouse/mutations/warehouse_delete.py:132]

**`saleor/graphql/warehouse/mutations/warehouse_shipping_zone_assign.py`**

- `WarehouseShippingZoneAssign` (class) — [saleor/graphql/warehouse/mutations/warehouse_shipping_zone_assign.py:19]
- `Meta` (class) — [saleor/graphql/warehouse/mutations/warehouse_shipping_zone_assign.py:20]
- `Arguments` (class) — [saleor/graphql/warehouse/mutations/warehouse_shipping_zone_assign.py:28]
- `perform_mutation` (function) — [saleor/graphql/warehouse/mutations/warehouse_shipping_zone_assign.py:37]
- `clean_shipping_zones` (function) — [saleor/graphql/warehouse/mutations/warehouse_shipping_zone_assign.py:49]
- `check_if_zones_can_be_assigned` (function) — [saleor/graphql/warehouse/mutations/warehouse_shipping_zone_assign.py:59]

**`saleor/graphql/warehouse/mutations/warehouse_shipping_zone_unassign.py`**

- `WarehouseShippingZoneUnassign` (class) — [saleor/graphql/warehouse/mutations/warehouse_shipping_zone_unassign.py:14]
- `Meta` (class) — [saleor/graphql/warehouse/mutations/warehouse_shipping_zone_unassign.py:15]
- `Arguments` (class) — [saleor/graphql/warehouse/mutations/warehouse_shipping_zone_unassign.py:23]
- `perform_mutation` (function) — [saleor/graphql/warehouse/mutations/warehouse_shipping_zone_unassign.py:32]

**`saleor/graphql/warehouse/mutations/warehouse_update.py`**

- `WarehouseUpdate` (class) — [saleor/graphql/warehouse/mutations/warehouse_update.py:15]
- `Meta` (class) — [saleor/graphql/warehouse/mutations/warehouse_update.py:18]
- `Arguments` (class) — [saleor/graphql/warehouse/mutations/warehouse_update.py:26]
- `prepare_address` (function) — [saleor/graphql/warehouse/mutations/warehouse_update.py:37]
- `post_save_action` (function) — [saleor/graphql/warehouse/mutations/warehouse_update.py:49]
- `perform_mutation` (function) — [saleor/graphql/warehouse/mutations/warehouse_update.py:54]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/warehouse/mutations/warehouse_delete.py` (134 lines)
- `saleor/graphql/warehouse/mutations/__init__.py` (13 lines)
- `saleor/graphql/warehouse/mutations/base.py` (61 lines)
- `saleor/graphql/warehouse/mutations/warehouse_create.py` (51 lines)
- `saleor/graphql/warehouse/mutations/warehouse_shipping_zone_assign.py` (122 lines)
- `saleor/graphql/warehouse/mutations/warehouse_shipping_zone_unassign.py` (40 lines)
- `saleor/graphql/warehouse/mutations/warehouse_update.py` (63 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: `saleor/graphql/warehouse/tests/mutations`

Internal dependencies named in the source:

- `....channel.models`
- `....core.tracing.traced_atomic_transaction`
- `....core.utils.events.call_event`
- `....permission.enums.ProductPermissions`
- `....warehouse.WarehouseClickAndCollectOption`
- `....warehouse.error_codes.WarehouseErrorCode`
- `....warehouse.models`
- `....warehouse.validation.validate_warehouse_count`
- `....webhook.event_types.WebhookEventAsyncType`
- `...account.i18n.I18nMixin`
- `...account.mixins.AddressMetadataMixin`
- `...core.ResolveInfo`
- `...core.mutations.DeprecatedModelMutation`
- `...core.mutations.ModelDeleteMutation`
- `...core.mutations.ModelWithExtRefMutation`
- `...core.types.NonNullList`
- `...core.types.WarehouseError`
- `...core.utils.WebhookEventInfo`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `...shipping.types.ShippingZone`
- `...site.dataloaders.get_site_promise`
- `...utils.get_user_or_app_from_context`
- `..types.Warehouse`
- `..types.WarehouseCreateInput`
- `..types.WarehouseUpdateInput`
- `.base.WarehouseMixin`
- `.warehouse_create.WarehouseCreate`
- `.warehouse_delete.WarehouseDelete`
- `.warehouse_shipping_zone_assign.WarehouseShippingZoneAssign`
- `.warehouse_shipping_zone_unassign.WarehouseShippingZoneUnassign`
- `.warehouse_update.WarehouseUpdate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `15a0ff88dbee` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
