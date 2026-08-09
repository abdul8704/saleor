## Purpose

`saleor/order/webhooks` (`saleor/order/webhooks`) groups 3 source file(s) exposing 4 top-level declaration(s).

## Public surface

**`saleor/order/webhooks/exclude_shipping.py`**

- `generate_excluded_shipping_methods_for_order_payload` (function) — [saleor/order/webhooks/exclude_shipping.py:33]
- `excluded_shipping_methods_for_order` (function) — [saleor/order/webhooks/exclude_shipping.py:48]

**`saleor/order/webhooks/order_calculate_taxes.py`**

- `generate_order_payload_for_tax_calculation` (function) — [saleor/order/webhooks/order_calculate_taxes.py:72]
- `get_taxes` (function) — [saleor/order/webhooks/order_calculate_taxes.py:144]

## How it works

The module's files, as provided to this run:

- `saleor/order/webhooks/exclude_shipping.py` (129 lines)
- `saleor/order/webhooks/order_calculate_taxes.py` (157 lines)
- `saleor/order/webhooks/__init__.py` (1 lines)

## Interactions

- Imports from: `saleor/graphql`, `saleor/core`, `saleor/graphql/product/types`
- Imported by: `saleor/order/tests/webhooks`, `saleor/graphql/order/tests/queries`

Internal dependencies named in the source:

- `...account.models.User`
- `...app.models.App`
- `...core.db.connection.allow_writer`
- `...core.prices.quantize_price`
- `...core.prices.quantize_price_fields`
- `...core.taxes.TaxData`
- `...core.utils.json_serializer.CustomJsonEncoder`
- `...discount.utils.shared.is_order_level_discount`
- `...order.models.Order`
- `...shipping.interface.ExcludedShippingMethod`
- `...shipping.interface.ShippingMethodData`
- `...tax.utils.get_charge_taxes_for_order`
- `...tax.webhooks.shared`
- `...webhook.event_types.WebhookEventSyncType`
- `...webhook.payload_serializers.PayloadSerializer`
- `...webhook.serializers.serialize_variant_full_name`
- `...webhook.traced_payload_generator`
- `...webhook.utils.get_webhooks_for_event`
- `..models.Order`
- `..models.OrderLine`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `f8092c0f34ad` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
