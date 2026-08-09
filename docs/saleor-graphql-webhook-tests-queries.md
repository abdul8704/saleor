## Purpose

`saleor/graphql/webhook/tests/queries` (`saleor/graphql/webhook/tests/queries`) groups 6 source file(s) exposing 25 top-level declaration(s).

## Public surface

**`saleor/graphql/webhook/tests/queries/test_event_delivery_filter.py`**

- `test_delivery_status_filter` (function) — [saleor/graphql/webhook/tests/queries/test_event_delivery_filter.py:30]
- `test_delivery_status_filter_no_results` (function) — [saleor/graphql/webhook/tests/queries/test_event_delivery_filter.py:54]

**`saleor/graphql/webhook/tests/queries/test_event_delivery_query.py`**

- `test_event_deliveries_pagination_with_shared_created_at` (function) — [saleor/graphql/webhook/tests/queries/test_event_delivery_query.py:73]
- `test_webhook_delivery_attempt_query` (function) — [saleor/graphql/webhook/tests/queries/test_event_delivery_query.py:125]
- `test_webhook_delivery_attempt_query_deprecated_payload_in_database` (function) — [saleor/graphql/webhook/tests/queries/test_event_delivery_query.py:166]

**`saleor/graphql/webhook/tests/queries/test_event_delivery_sort.py`**

- `test_webhook_delivery_query_sort_asc` (function) — [saleor/graphql/webhook/tests/queries/test_event_delivery_sort.py:25]
- `test_webhook_delivery_query_sort_dsc` (function) — [saleor/graphql/webhook/tests/queries/test_event_delivery_sort.py:52]
- `test_webhook_delivery_attempt_query_sort_asc` (function) — [saleor/graphql/webhook/tests/queries/test_event_delivery_sort.py:111]
- `test_webhook_delivery_attempt_query_sort_desc` (function) — [saleor/graphql/webhook/tests/queries/test_event_delivery_sort.py:137]

**`saleor/graphql/webhook/tests/queries/test_sample_payload.py`**

- `test_sample_payload_query_by_app` (function) — [saleor/graphql/webhook/tests/queries/test_sample_payload.py:36]
- `test_sample_payload_query_by_staff` (function) — [saleor/graphql/webhook/tests/queries/test_sample_payload.py:78]

**`saleor/graphql/webhook/tests/queries/test_webhook.py`**

- `test_query_webhook_by_staff` (function) — [saleor/graphql/webhook/tests/queries/test_webhook.py:31]
- `test_query_webhook_identifier_by_staff` (function) — [saleor/graphql/webhook/tests/queries/test_webhook.py:50]
- `test_query_webhook_with_subscription_query_by_staff` (function) — [saleor/graphql/webhook/tests/queries/test_webhook.py:70]
- `test_query_webhook_by_staff_without_permission` (function) — [saleor/graphql/webhook/tests/queries/test_webhook.py:90]
- `test_query_webhook_removed_app` (function) — [saleor/graphql/webhook/tests/queries/test_webhook.py:98]
- `test_query_webhook_by_app` (function) — [saleor/graphql/webhook/tests/queries/test_webhook.py:116]
- `test_query_webhook_identifier_by_app` (function) — [saleor/graphql/webhook/tests/queries/test_webhook.py:132]
- `test_query_webhook_by_app_without_permission` (function) — [saleor/graphql/webhook/tests/queries/test_webhook.py:149]
- `test_query_webhook_by_anonymnous_client` (function) — [saleor/graphql/webhook/tests/queries/test_webhook.py:165]
- `test_query_webhook_sync_and_async_events` (function) — [saleor/graphql/webhook/tests/queries/test_webhook.py:180]
- `test_webhook_query_invalid_id` (function) — [saleor/graphql/webhook/tests/queries/test_webhook.py:210]
- `test_webhook_query_object_with_given_id_does_not_exist` (function) — [saleor/graphql/webhook/tests/queries/test_webhook.py:226]
- `test_webhook_with_invalid_object_type` (function) — [saleor/graphql/webhook/tests/queries/test_webhook.py:237]
- `test_webhook_without_name` (function) — [saleor/graphql/webhook/tests/queries/test_webhook.py:248]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/webhook/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/webhook/tests/queries/test_event_delivery_filter.py` (72 lines)
- `saleor/graphql/webhook/tests/queries/test_event_delivery_query.py` (209 lines)
- `saleor/graphql/webhook/tests/queries/test_event_delivery_sort.py` (159 lines)
- `saleor/graphql/webhook/tests/queries/test_sample_payload.py` (101 lines)
- `saleor/graphql/webhook/tests/queries/test_webhook.py` (260 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....app.models.App`
- `.....core.EventDeliveryStatus`
- `.....core.models.EventDelivery`
- `.....webhook.event_types.WebhookEventAsyncType`
- `.....webhook.models.Webhook`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `...enums.WebhookEventTypeAsyncEnum`
- `...enums.WebhookEventTypeSyncEnum`
- `...enums.WebhookSampleEventTypeEnum`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `d139f3baa3d6` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
