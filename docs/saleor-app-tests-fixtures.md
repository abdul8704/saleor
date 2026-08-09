## Purpose

`saleor/app/tests/fixtures` (`saleor/app/tests/fixtures`) groups 8 source file(s) exposing 32 top-level declaration(s).

## Public surface

**`saleor/app/tests/fixtures/app_extension.py`**

- `app_with_extensions` (function) — [saleor/app/tests/fixtures/app_extension.py:7]
- `removed_app_with_extensions` (function) — [saleor/app/tests/fixtures/app_extension.py:30]

**`saleor/app/tests/fixtures/app_installation.py`**

- `app_installation` (function) — [saleor/app/tests/fixtures/app_installation.py:7]

**`saleor/app/tests/fixtures/app_problem.py`**

- `app_problem_generator` (function) — [saleor/app/tests/fixtures/app_problem.py:11]
- `create_problem` (function) — [saleor/app/tests/fixtures/app_problem.py:12]

**`saleor/app/tests/fixtures/app.py`**

- `app` (function) — [saleor/app/tests/fixtures/app.py:11]
- `app_marked_to_be_removed` (function) — [saleor/app/tests/fixtures/app.py:22]
- `webhook_app` (function) — [saleor/app/tests/fixtures/app.py:34]
- `app_with_token` (function) — [saleor/app/tests/fixtures/app.py:60]
- `removed_app` (function) — [saleor/app/tests/fixtures/app.py:67]
- `external_app` (function) — [saleor/app/tests/fixtures/app.py:77]
- `apps_without_webhooks` (function) — [saleor/app/tests/fixtures/app.py:96]
- `app_exclude_shipping_for_order` (function) — [saleor/app/tests/fixtures/app.py:108]
- `app_exclude_shipping_for_checkout` (function) — [saleor/app/tests/fixtures/app.py:135]
- `second_app_exclude_shipping_for_checkout` (function) — [saleor/app/tests/fixtures/app.py:162]
- `second_app_exclude_shipping_for_order` (function) — [saleor/app/tests/fixtures/app.py:189]

**`saleor/app/tests/fixtures/webhooks/payment_app.py`**

- `payment_app` (function) — [saleor/app/tests/fixtures/webhooks/payment_app.py:10]
- `payment_app_with_subscription_webhooks` (function) — [saleor/app/tests/fixtures/webhooks/payment_app.py:32]
- `list_stored_payment_methods_app` (function) — [saleor/app/tests/fixtures/webhooks/payment_app.py:55]
- `stored_payment_method_request_delete_app` (function) — [saleor/app/tests/fixtures/webhooks/payment_app.py:76]
- `payment_gateway_initialize_tokenization_app` (function) — [saleor/app/tests/fixtures/webhooks/payment_app.py:97]
- `payment_method_initialize_tokenization_app` (function) — [saleor/app/tests/fixtures/webhooks/payment_app.py:118]
- `payment_method_process_tokenization_app` (function) — [saleor/app/tests/fixtures/webhooks/payment_app.py:139]
- `payment_gateway_initialize_session_app` (function) — [saleor/app/tests/fixtures/webhooks/payment_app.py:160]
- `transaction_process_session_app` (function) — [saleor/app/tests/fixtures/webhooks/payment_app.py:181]
- `transaction_initialize_session_app` (function) — [saleor/app/tests/fixtures/webhooks/payment_app.py:251]

**`saleor/app/tests/fixtures/webhooks/shipping_app.py`**

- `shipping_app` (function) — [saleor/app/tests/fixtures/webhooks/shipping_app.py:9]
- `shipping_app_with_subscription` (function) — [saleor/app/tests/fixtures/webhooks/shipping_app.py:32]
- `exclude_shipping_app_without_subscription` (function) — [saleor/app/tests/fixtures/webhooks/shipping_app.py:65]
- `exclude_shipping_app_with_subscription` (function) — [saleor/app/tests/fixtures/webhooks/shipping_app.py:83]

**`saleor/app/tests/fixtures/webhooks/tax_app.py`**

- `tax_app` (function) — [saleor/app/tests/fixtures/webhooks/tax_app.py:130]
- `external_tax_app` (function) — [saleor/app/tests/fixtures/webhooks/tax_app.py:156]

## How it works

The module's files, as provided to this run:

- `saleor/app/tests/fixtures/__init__.py` (7 lines)
- `saleor/app/tests/fixtures/app_extension.py` (49 lines)
- `saleor/app/tests/fixtures/app_installation.py` (12 lines)
- `saleor/app/tests/fixtures/app_problem.py` (46 lines)
- `saleor/app/tests/fixtures/app.py` (212 lines)
- `saleor/app/tests/fixtures/webhooks/payment_app.py` (302 lines)
- `saleor/app/tests/fixtures/webhooks/shipping_app.py` (109 lines)
- `saleor/app/tests/fixtures/webhooks/tax_app.py` (188 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....app.models.App`
- `.....app.types.AppType`
- `.....graphql.core.utils.to_global_id_or_none`
- `.....webhook.event_types.WebhookEventAsyncType`
- `.....webhook.event_types.WebhookEventSyncType`
- `.....webhook.models.Webhook`
- `.....webhook.models.WebhookEvent`
- `.....webhook.tests.subscription_webhooks.subscription_queries`
- `....account.models.User`
- `....app.models.App`
- `....app.models.AppExtension`
- `....app.models.AppInstallation`
- `....app.types.AppType`
- `....webhook.event_types.WebhookEventSyncType`
- `....webhook.models.Webhook`
- `....webhook.models.WebhookEvent`
- `...models.App`
- `...models.AppProblem`
- `.app.*  # noqa: F403`
- `.app_extension.*  # noqa: F403`
- `.app_installation.*  # noqa: F403`
- `.app_problem.*  # noqa: F403`
- `.webhooks.payment_app.*  # noqa: F403`
- `.webhooks.shipping_app.*  # noqa: F403`
- `.webhooks.tax_app.*  # noqa: F403`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `6dbea5ffe56d` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
