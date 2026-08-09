## Purpose

`saleor/webhook/tests/fixtures` (`saleor/webhook/tests/fixtures`) groups 7 source file(s) exposing 199 top-level declaration(s).

## Public surface

**`saleor/webhook/tests/fixtures/subscription_webhooks.py`**

- `subscription_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:9]
- `fun` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:10]
- `subscription_account_confirmation_requested_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:24]
- `subscription_account_confirmed_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:32]
- `subscription_account_change_email_requested_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:40]
- `subscription_account_email_changed_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:48]
- `subscription_account_delete_requested_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:56]
- `subscription_account_set_password_requested_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:64]
- `subscription_account_deleted_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:72]
- `subscription_address_created_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:80]
- `subscription_address_updated_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:87]
- `subscription_address_deleted_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:94]
- `subscription_app_installed_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:101]
- `subscription_app_updated_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:108]
- `subscription_app_deleted_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:113]
- `subscription_app_status_changed_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:118]
- `subscription_attribute_created_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:126]
- `subscription_attribute_updated_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:133]
- `subscription_attribute_deleted_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:140]
- `subscription_attribute_value_created_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:147]
- `subscription_attribute_value_updated_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:155]
- `subscription_attribute_value_deleted_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:163]
- `subscription_category_created_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:171]
- `subscription_category_updated_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:178]
- `subscription_category_deleted_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:185]
- `subscription_channel_created_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:192]
- `subscription_channel_updated_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:199]
- `subscription_channel_deleted_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:206]
- `subscription_channel_status_changed_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:213]
- `subscription_gift_card_created_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:221]
- `subscription_gift_card_updated_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:228]
- `subscription_gift_card_deleted_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:235]
- `subscription_gift_card_sent_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:242]
- `subscription_gift_card_status_changed_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:249]
- `subscription_gift_card_metadata_updated_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:257]
- `subscription_gift_card_export_completed_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:265]
- `subscription_menu_created_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:273]
- `subscription_menu_updated_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:280]
- `subscription_menu_deleted_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:287]
- `subscription_menu_item_created_webhook` (function) — [saleor/webhook/tests/fixtures/subscription_webhooks.py:294]
- _…and 143 more in this file_

**`saleor/webhook/tests/fixtures/utils.py`**

- `prepare_async_and_sync_events` (function) — [saleor/webhook/tests/fixtures/utils.py:5]
- `prepare_sync_event` (function) — [saleor/webhook/tests/fixtures/utils.py:14]
- `prepare_async_event` (function) — [saleor/webhook/tests/fixtures/utils.py:23]

**`saleor/webhook/tests/fixtures/webhook_data.py`**

- `observability_webhook_data` (function) — [saleor/webhook/tests/fixtures/webhook_data.py:7]

**`saleor/webhook/tests/fixtures/webhook_event.py`**

- `events_cycle` (function) — [saleor/webhook/tests/fixtures/webhook_event.py:14]
- `webhook_events` (function) — [saleor/webhook/tests/fixtures/webhook_event.py:27]

**`saleor/webhook/tests/fixtures/webhook_response.py`**

- `webhook_response` (function) — [saleor/webhook/tests/fixtures/webhook_response.py:8]
- `webhook_response_failed` (function) — [saleor/webhook/tests/fixtures/webhook_response.py:20]

**`saleor/webhook/tests/fixtures/webhook.py`**

- `webhook` (function) — [saleor/webhook/tests/fixtures/webhook.py:9]
- `webhook_without_name` (function) — [saleor/webhook/tests/fixtures/webhook.py:18]
- `webhook_removed_app` (function) — [saleor/webhook/tests/fixtures/webhook.py:25]
- `any_webhook` (function) — [saleor/webhook/tests/fixtures/webhook.py:36]
- `observability_webhook` (function) — [saleor/webhook/tests/fixtures/webhook.py:45]
- `webhooks_without_events` (function) — [saleor/webhook/tests/fixtures/webhook.py:60]
- `setup_checkout_webhooks` (function) — [saleor/webhook/tests/fixtures/webhook.py:78]
- `setup_order_webhooks` (function) — [saleor/webhook/tests/fixtures/webhook.py:249]

## How it works

The module's files, as provided to this run:

- `saleor/webhook/tests/fixtures/__init__.py` (5 lines)
- `saleor/webhook/tests/fixtures/subscription_webhooks.py` (1370 lines)
- `saleor/webhook/tests/fixtures/utils.py` (26 lines)
- `saleor/webhook/tests/fixtures/webhook_data.py` (13 lines)
- `saleor/webhook/tests/fixtures/webhook_event.py` (33 lines)
- `saleor/webhook/tests/fixtures/webhook_response.py` (28 lines)
- `saleor/webhook/tests/fixtures/webhook.py` (433 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....app.models.App`
- `....core.EventDeliveryStatus`
- `....webhook.event_types.WebhookEventAsyncType`
- `....webhook.event_types.WebhookEventSyncType`
- `....webhook.models.Webhook`
- `....webhook.models.WebhookEvent`
- `....webhook.observability.WebhookData`
- `....webhook.transport.utils.WebhookResponse`
- `...event_types.WebhookEventAsyncType`
- `...event_types.WebhookEventSyncType`
- `...models.Webhook`
- `..subscription_webhooks.subscription_queries`
- `.subscription_webhooks.*  # noqa: F403`
- `.webhook.*  # noqa: F403`
- `.webhook_data.*  # noqa: F403`
- `.webhook_event.*  # noqa: F403`
- `.webhook_response.*  # noqa: F403`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `6c9642846397` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
