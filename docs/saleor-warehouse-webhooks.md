## Purpose

`saleor/warehouse/webhooks` (`saleor/warehouse/webhooks`) groups 4 source file(s) exposing 8 top-level declaration(s).

## Public surface

**`saleor/warehouse/webhooks/channel_stock_events.py`**

- `trigger_product_variant_out_of_stock_in_channel` (function) — [saleor/warehouse/webhooks/channel_stock_events.py:77]
- `trigger_product_variant_back_in_stock_in_channel` (function) — [saleor/warehouse/webhooks/channel_stock_events.py:92]
- `trigger_product_variant_out_of_stock_for_click_and_collect` (function) — [saleor/warehouse/webhooks/channel_stock_events.py:107]
- `trigger_product_variant_back_in_stock_for_click_and_collect` (function) — [saleor/warehouse/webhooks/channel_stock_events.py:122]

**`saleor/warehouse/webhooks/payloads.py`**

- `generate_product_variant_with_stock_payload` (function) — [saleor/warehouse/webhooks/payloads.py:18]

**`saleor/warehouse/webhooks/stock_events.py`**

- `trigger_product_variant_out_of_stock` (function) — [saleor/warehouse/webhooks/stock_events.py:26]
- `trigger_product_variant_back_in_stock` (function) — [saleor/warehouse/webhooks/stock_events.py:49]
- `trigger_product_variant_stocks_updated` (function) — [saleor/warehouse/webhooks/stock_events.py:72]

## How it works

The module's files, as provided to this run:

- `saleor/warehouse/webhooks/stock_events.py` (97 lines)
- `saleor/warehouse/webhooks/channel_stock_events.py` (134 lines)
- `saleor/warehouse/webhooks/__init__.py` (1 lines)
- `saleor/warehouse/webhooks/payloads.py` (35 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: `saleor/warehouse/tests/webhooks`, `saleor/warehouse/tests`

Internal dependencies named in the source:

- `...account.models.User`
- `...app.models.App`
- `...core.db.connection.allow_writer`
- `...plugins.base_plugin.RequestorOrLazyObject`
- `...site.models.SiteSettings`
- `...webhook.event_types.WebhookEventAsyncType`
- `...webhook.models.Webhook`
- `...webhook.payload_helpers.generate_meta`
- `...webhook.payload_helpers.generate_requestor`
- `...webhook.payload_serializers.PayloadSerializer`
- `...webhook.traced_payload_generator`
- `...webhook.utils.filter_webhooks_for_channel`
- `...webhook.utils.get_webhooks_for_event`
- `..interface.VariantChannelStockInfo`
- `..models.Stock`
- `.payloads.generate_product_variant_with_stock_payload`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `7734d12b9bcf` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
