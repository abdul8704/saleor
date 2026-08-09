## Purpose

`saleor/warehouse/tests/webhooks` (`saleor/warehouse/tests/webhooks`) groups 6 source file(s) exposing 25 top-level declaration(s).

## Public surface

**`saleor/warehouse/tests/webhooks/subscriptions/test_channel_stock_events.py`**

- `subscription_product_variant_out_of_stock_in_channel_webhook` (function) — [saleor/warehouse/tests/webhooks/subscriptions/test_channel_stock_events.py:58]
- `subscription_product_variant_back_in_stock_in_channel_webhook` (function) — [saleor/warehouse/tests/webhooks/subscriptions/test_channel_stock_events.py:66]
- `subscription_product_variant_out_of_stock_for_click_and_collect_webhook` (function) — [saleor/warehouse/tests/webhooks/subscriptions/test_channel_stock_events.py:74]
- `subscription_product_variant_back_in_stock_for_click_and_collect_webhook` (function) — [saleor/warehouse/tests/webhooks/subscriptions/test_channel_stock_events.py:84]
- `test_product_variant_out_of_stock_in_channel` (function) — [saleor/warehouse/tests/webhooks/subscriptions/test_channel_stock_events.py:93]
- `test_product_variant_back_in_stock_in_channel` (function) — [saleor/warehouse/tests/webhooks/subscriptions/test_channel_stock_events.py:119]
- `test_product_variant_out_of_stock_for_click_and_collect` (function) — [saleor/warehouse/tests/webhooks/subscriptions/test_channel_stock_events.py:145]
- `test_product_variant_back_in_stock_for_click_and_collect` (function) — [saleor/warehouse/tests/webhooks/subscriptions/test_channel_stock_events.py:173]

**`saleor/warehouse/tests/webhooks/test_channel_stock_events.py`**

- `stock_info` (function) — [saleor/warehouse/tests/webhooks/test_channel_stock_events.py:27]
- `test_trigger_dispatches` (function) — [saleor/warehouse/tests/webhooks/test_channel_stock_events.py:54]
- `test_trigger_skipped_when_legacy_flag_on` (function) — [saleor/warehouse/tests/webhooks/test_channel_stock_events.py:91]
- `test_trigger_empty_stock_infos_skips` (function) — [saleor/warehouse/tests/webhooks/test_channel_stock_events.py:113]
- `test_trigger_no_webhooks_skips` (function) — [saleor/warehouse/tests/webhooks/test_channel_stock_events.py:135]
- `test_trigger_uses_passed_webhooks` (function) — [saleor/warehouse/tests/webhooks/test_channel_stock_events.py:157]
- `test_trigger_filters_webhooks_by_channel_slug` (function) — [saleor/warehouse/tests/webhooks/test_channel_stock_events.py:183]
- `test_trigger_passes_through_when_subscription_has_no_channel_filter` (function) — [saleor/warehouse/tests/webhooks/test_channel_stock_events.py:208]
- `test_trigger_groups_multiple_channels_into_separate_calls` (function) — [saleor/warehouse/tests/webhooks/test_channel_stock_events.py:234]
- `test_trigger_batches_multiple_variants_in_same_channel` (function) — [saleor/warehouse/tests/webhooks/test_channel_stock_events.py:266]

**`saleor/warehouse/tests/webhooks/test_payloads.py`**

- `test_generate_base_product_variant_payload` (function) — [saleor/warehouse/tests/webhooks/test_payloads.py:12]

**`saleor/warehouse/tests/webhooks/test_stock_events.py`**

- `test_trigger_product_variant_out_of_stock_dispatches` (function) — [saleor/warehouse/tests/webhooks/test_stock_events.py:15]
- `test_trigger_product_variant_out_of_stock_no_webhooks_skips` (function) — [saleor/warehouse/tests/webhooks/test_stock_events.py:39]
- `test_trigger_product_variant_out_of_stock_uses_passed_webhooks` (function) — [saleor/warehouse/tests/webhooks/test_stock_events.py:54]
- `test_trigger_product_variant_back_in_stock_dispatches` (function) — [saleor/warehouse/tests/webhooks/test_stock_events.py:68]
- `test_trigger_product_variant_stocks_updated_dispatches` (function) — [saleor/warehouse/tests/webhooks/test_stock_events.py:92]
- `test_trigger_product_variant_stocks_updated_no_webhooks_skips` (function) — [saleor/warehouse/tests/webhooks/test_stock_events.py:119]

## How it works

The module's files, as provided to this run:

- `saleor/warehouse/tests/webhooks/__init__.py` (1 lines)
- `saleor/warehouse/tests/webhooks/subscriptions/__init__.py` (1 lines)
- `saleor/warehouse/tests/webhooks/subscriptions/test_channel_stock_events.py` (200 lines)
- `saleor/warehouse/tests/webhooks/test_channel_stock_events.py` (287 lines)
- `saleor/warehouse/tests/webhooks/test_payloads.py` (60 lines)
- `saleor/warehouse/tests/webhooks/test_stock_events.py` (129 lines)

## Interactions

- Imports from: `saleor/warehouse/webhooks`, `saleor/webhook`, `saleor/webhook/transport/asynchronous`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....__version__`
- `.....webhook.event_types.WebhookEventAsyncType`
- `....interface.VariantChannelStockInfo`
- `....webhook.event_types.WebhookEventAsyncType`
- `...interface.VariantChannelStockInfo`
- `saleor.webhook.event_types.WebhookEventAsyncType`
- `saleor.webhook.transport.asynchronous.transport.WebhookPayloadData`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `adebb5aa2a9a` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
