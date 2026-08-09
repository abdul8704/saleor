## Purpose

`saleor/checkout/webhooks` (`saleor/checkout/webhooks`) groups 4 source file(s) exposing 6 top-level declaration(s).

## Public surface

**`saleor/checkout/webhooks/calculate_taxes.py`**

- `serialize_checkout_lines_for_tax_calculation` (function) — [saleor/checkout/webhooks/calculate_taxes.py:62]
- `generate_checkout_payload_for_tax_calculation` (function) — [saleor/checkout/webhooks/calculate_taxes.py:86]
- `get_taxes` (function) — [saleor/checkout/webhooks/calculate_taxes.py:173]

**`saleor/checkout/webhooks/exclude_shipping.py`**

- `excluded_shipping_methods_for_checkout` (function) — [saleor/checkout/webhooks/exclude_shipping.py:29]

**`saleor/checkout/webhooks/list_shipping_methods.py`**

- `list_shipping_methods_for_checkout` (function) — [saleor/checkout/webhooks/list_shipping_methods.py:23]
- `process_responses` (function) — [saleor/checkout/webhooks/list_shipping_methods.py:50]

## How it works

The module's files, as provided to this run:

- `saleor/checkout/webhooks/exclude_shipping.py` (76 lines)
- `saleor/checkout/webhooks/list_shipping_methods.py` (91 lines)
- `saleor/checkout/webhooks/calculate_taxes.py` (188 lines)
- `saleor/checkout/webhooks/__init__.py` (1 lines)

## Interactions

- Imports from: `saleor/graphql`, `saleor/core`, `saleor/checkout`
- Imported by: `saleor/checkout/tests/webhooks`, `saleor/checkout/tests`, `saleor/graphql/checkout/tests/mutations`, `saleor/graphql/checkout/tests`, `saleor/graphql/shipping/tests/mutations`

Internal dependencies named in the source:

- `...account.models.User`
- `...app.models.App`
- `...base_calculations`
- `...checkout.fetch.CheckoutInfo`
- `...checkout.fetch.CheckoutLineInfo`
- `...core.db.connection.allow_writer`
- `...core.prices.quantize_price`
- `...core.taxes.TaxData`
- `...core.utils.json_serializer.CustomJsonEncoder`
- `...discount.utils.voucher.is_order_level_voucher`
- `...shipping.interface.ExcludedShippingMethod`
- `...shipping.interface.ShippingMethodData`
- `...tax.utils.get_charge_taxes_for_checkout`
- `...tax.webhooks.shared`
- `...webhook.event_types.WebhookEventSyncType`
- `...webhook.payload_serializers.PayloadSerializer`
- `...webhook.payloads.generate_checkout_payload`
- `...webhook.response_schemas.shipping.ListShippingMethodsSchema`
- `...webhook.traced_payload_generator`
- `...webhook.transport.synchronous.transport.trigger_webhook_sync_promise`
- `...webhook.utils.get_webhooks_for_event`
- `..models.Checkout`
- `..utils.get_checkout_metadata`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c7a976068a8d` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
