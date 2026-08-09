## Purpose

`saleor/graphql/shipping/bulk_mutations` (`saleor/graphql/shipping/bulk_mutations`) groups 3 source file(s) exposing 9 top-level declaration(s).

## Public surface

**`saleor/graphql/shipping/bulk_mutations/shipping_price_bulk_delete.py`**

- `ShippingPriceBulkDelete` (class) — [saleor/graphql/shipping/bulk_mutations/shipping_price_bulk_delete.py:15]
- `Arguments` (class) — [saleor/graphql/shipping/bulk_mutations/shipping_price_bulk_delete.py:16]
- `Meta` (class) — [saleor/graphql/shipping/bulk_mutations/shipping_price_bulk_delete.py:26]
- `get_nodes_or_error` (function) — [saleor/graphql/shipping/bulk_mutations/shipping_price_bulk_delete.py:36]
- `bulk_action` (function) — [saleor/graphql/shipping/bulk_mutations/shipping_price_bulk_delete.py:53]

**`saleor/graphql/shipping/bulk_mutations/shipping_zone_bulk_delete.py`**

- `ShippingZoneBulkDelete` (class) — [saleor/graphql/shipping/bulk_mutations/shipping_zone_bulk_delete.py:15]
- `Arguments` (class) — [saleor/graphql/shipping/bulk_mutations/shipping_zone_bulk_delete.py:16]
- `Meta` (class) — [saleor/graphql/shipping/bulk_mutations/shipping_zone_bulk_delete.py:26]
- `bulk_action` (function) — [saleor/graphql/shipping/bulk_mutations/shipping_zone_bulk_delete.py:36]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/shipping/bulk_mutations/shipping_price_bulk_delete.py` (59 lines)
- `saleor/graphql/shipping/bulk_mutations/shipping_zone_bulk_delete.py` (42 lines)
- `saleor/graphql/shipping/bulk_mutations/__init__.py` (4 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: `saleor/graphql/shipping/tests/mutations`

Internal dependencies named in the source:

- `....permission.enums.ShippingPermissions`
- `....shipping.models`
- `....webhook.event_types.WebhookEventAsyncType`
- `....webhook.utils.get_webhooks_for_event`
- `...core.ResolveInfo`
- `...core.mutations.ModelBulkDeleteMutation`
- `...core.types.NonNullList`
- `...core.types.ShippingError`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `..types.ShippingMethod`
- `..types.ShippingZone`
- `.shipping_price_bulk_delete.ShippingPriceBulkDelete`
- `.shipping_zone_bulk_delete.ShippingZoneBulkDelete`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `fb8a6964c4f7` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
