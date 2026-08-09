## Purpose

`saleor/graphql/webhook/tests` (`saleor/graphql/webhook/tests`) groups 8 source file(s) exposing 34 top-level declaration(s).

## Public surface

**`saleor/graphql/webhook/tests/benchmark/test_webhook_events.py`**

- `test_webhooks` (function) — [saleor/graphql/webhook/tests/benchmark/test_webhook_events.py:34]

**`saleor/graphql/webhook/tests/deprecated/test_webhook.py`**

- `test_webhook_create_by_app` (function) — [saleor/graphql/webhook/tests/deprecated/test_webhook.py:24]
- `test_webhook_create_inactive_app` (function) — [saleor/graphql/webhook/tests/deprecated/test_webhook.py:49]
- `test_webhook_create_without_app` (function) — [saleor/graphql/webhook/tests/deprecated/test_webhook.py:65]
- `test_webhook_create_app_doesnt_exist` (function) — [saleor/graphql/webhook/tests/deprecated/test_webhook.py:78]
- `test_webhook_create_by_staff` (function) — [saleor/graphql/webhook/tests/deprecated/test_webhook.py:108]
- `test_webhook_create_by_staff_with_inactive_app` (function) — [saleor/graphql/webhook/tests/deprecated/test_webhook.py:133]
- `test_webhook_create_by_staff_without_permission` (function) — [saleor/graphql/webhook/tests/deprecated/test_webhook.py:147]
- `test_webhook_update_by_staff` (function) — [saleor/graphql/webhook/tests/deprecated/test_webhook.py:179]
- `test_webhook_update_by_staff_without_permission` (function) — [saleor/graphql/webhook/tests/deprecated/test_webhook.py:202]
- `test_query_webhook_by_staff` (function) — [saleor/graphql/webhook/tests/deprecated/test_webhook.py:230]
- `test_query_webhook_events` (function) — [saleor/graphql/webhook/tests/deprecated/test_webhook.py:257]
- `test_query_webhook_events_without_permissions` (function) — [saleor/graphql/webhook/tests/deprecated/test_webhook.py:266]

**`saleor/graphql/webhook/tests/test_pagination.py`**

- `webhooks_for_pagination` (function) — [saleor/graphql/webhook/tests/test_pagination.py:8]

**`saleor/graphql/webhook/tests/test_subscription_payload.py`**

- `test_initialize_request` (function) — [saleor/graphql/webhook/tests/test_subscription_payload.py:16]
- `test_initialize_request_pass_params` (function) — [saleor/graphql/webhook/tests/test_subscription_payload.py:25]
- `test_generate_pre_save_payloads_disabled_with_env` (function) — [saleor/graphql/webhook/tests/test_subscription_payload.py:54]
- `test_generate_pre_save_payloads_no_subscription_query` (function) — [saleor/graphql/webhook/tests/test_subscription_payload.py:78]
- `test_generate_pre_save_payloads` (function) — [saleor/graphql/webhook/tests/test_subscription_payload.py:102]
- `test_generate_payload_from_subscription` (function) — [saleor/graphql/webhook/tests/test_subscription_payload.py:127]
- `test_generate_payload_from_subscription_missing_permissions` (function) — [saleor/graphql/webhook/tests/test_subscription_payload.py:164]
- `test_generate_payload_from_subscription_circular_call` (function) — [saleor/graphql/webhook/tests/test_subscription_payload.py:190]
- `test_generate_payload_from_subscription_unable_to_build_payload` (function) — [saleor/graphql/webhook/tests/test_subscription_payload.py:238]
- `test_generate_payload_promise_from_subscription` (function) — [saleor/graphql/webhook/tests/test_subscription_payload.py:280]
- `test_generate_payload_promise_from_subscription_missing_permissions` (function) — [saleor/graphql/webhook/tests/test_subscription_payload.py:321]
- `test_generate_payload_promise_from_subscription_circular_call` (function) — [saleor/graphql/webhook/tests/test_subscription_payload.py:348]
- `test_generate_payload_promise_from_subscription_unable_to_build_payload` (function) — [saleor/graphql/webhook/tests/test_subscription_payload.py:397]

**`saleor/graphql/webhook/tests/test_subscription_query.py`**

- `test_subscription_query` (function) — [saleor/graphql/webhook/tests/test_subscription_query.py:11]
- `test_get_event_type_from_subscription` (function) — [saleor/graphql/webhook/tests/test_subscription_query.py:304]
- `test_query_validation` (function) — [saleor/graphql/webhook/tests/test_subscription_query.py:579]
- `test_get_events_from_field` (function) — [saleor/graphql/webhook/tests/test_subscription_query.py:588]
- `test_get_filterable_channel_slugs_for_query_with_filters` (function) — [saleor/graphql/webhook/tests/test_subscription_query.py:633]
- `test_get_filterable_channel_slugs_with_empty_filters` (function) — [saleor/graphql/webhook/tests/test_subscription_query.py:660]
- `test_get_filterable_channel_slugs_for_non_filterable_query` (function) — [saleor/graphql/webhook/tests/test_subscription_query.py:687]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/webhook/tests/__init__.py` (1 lines)
- `saleor/graphql/webhook/tests/benchmark/__init__.py` (1 lines)
- `saleor/graphql/webhook/tests/benchmark/test_webhook_events.py` (44 lines)
- `saleor/graphql/webhook/tests/deprecated/__init__.py` (1 lines)
- `saleor/graphql/webhook/tests/deprecated/test_webhook.py` (269 lines)
- `saleor/graphql/webhook/tests/test_pagination.py` (43 lines)
- `saleor/graphql/webhook/tests/test_subscription_payload.py` (437 lines)
- `saleor/graphql/webhook/tests/test_subscription_query.py` (721 lines)

## Interactions

- Imports from: `saleor/graphql`, `saleor/webhook`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....webhook.deprecated_event_types.WebhookEventType`
- `.....webhook.models.Webhook`
- `....app.models.App`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `....webhook.event_types.WebhookEventAsyncType`
- `....webhook.event_types.WebhookEventSyncType`
- `....webhook.models.Webhook`
- `...enums.WebhookEventTypeEnum`
- `..subscription_query.IsFragment`
- `..subscription_query.SubscriptionQuery`
- `saleor.webhook.error_codes.WebhookErrorCode`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `017c39a016a0` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
