## Purpose

`saleor/webhook/migrations` (`saleor/webhook/migrations`) groups 15 source file(s) exposing 16 top-level declaration(s).

## Public surface

**`saleor/webhook/migrations/0001_initial.py`**

- `Migration` (class) — [saleor/webhook/migrations/0001_initial.py:7]

**`saleor/webhook/migrations/0002_webhook_name.py`**

- `Migration` (class) — [saleor/webhook/migrations/0002_webhook_name.py:6]

**`saleor/webhook/migrations/0003_unmount_service_account.py`**

- `Migration` (class) — [saleor/webhook/migrations/0003_unmount_service_account.py:6]

**`saleor/webhook/migrations/0004_mount_app.py`**

- `Migration` (class) — [saleor/webhook/migrations/0004_mount_app.py:4]

**`saleor/webhook/migrations/0005_drop_manage_webhooks_permission.py`**

- `change_webhook_permission_to_app_permission` (function) — [saleor/webhook/migrations/0005_drop_manage_webhooks_permission.py:6]
- `Migration` (class) — [saleor/webhook/migrations/0005_drop_manage_webhooks_permission.py:40]

**`saleor/webhook/migrations/0006_auto_20200731_1440.py`**

- `Migration` (class) — [saleor/webhook/migrations/0006_auto_20200731_1440.py:8]

**`saleor/webhook/migrations/0007_auto_20210319_0945.py`**

- `Migration` (class) — [saleor/webhook/migrations/0007_auto_20210319_0945.py:6]

**`saleor/webhook/migrations/0008_webhook_subscription_query.py`**

- `Migration` (class) — [saleor/webhook/migrations/0008_webhook_subscription_query.py:6]

**`saleor/webhook/migrations/0009_webhook_custom_headers.py`**

- `Migration` (class) — [saleor/webhook/migrations/0009_webhook_custom_headers.py:9]

**`saleor/webhook/migrations/0010_drop_transaction_request_action_event.py`**

- `drop_transaction_action_request` (function) — [saleor/webhook/migrations/0010_drop_transaction_request_action_event.py:4]
- `Migration` (class) — [saleor/webhook/migrations/0010_drop_transaction_request_action_event.py:12]

**`saleor/webhook/migrations/0011_webhook_filterable_channel_slugs.py`**

- `Migration` (class) — [saleor/webhook/migrations/0011_webhook_filterable_channel_slugs.py:7]

**`saleor/webhook/migrations/0012_webhook_filterable_channel_slugs_idx.py`**

- `Migration` (class) — [saleor/webhook/migrations/0012_webhook_filterable_channel_slugs_idx.py:8]

**`saleor/webhook/migrations/0013_webhook_identifier_and_more.py`**

- `Migration` (class) — [saleor/webhook/migrations/0013_webhook_identifier_and_more.py:4]

**`saleor/webhook/migrations/0014_webhook_identifier_unique_constraint.py`**

- `Migration` (class) — [saleor/webhook/migrations/0014_webhook_identifier_unique_constraint.py:4]

## How it works

The module's files, as provided to this run:

- `saleor/webhook/migrations/__init__.py` (1 lines)
- `saleor/webhook/migrations/0001_initial.py` (67 lines)
- `saleor/webhook/migrations/0002_webhook_name.py` (15 lines)
- `saleor/webhook/migrations/0003_unmount_service_account.py` (24 lines)
- `saleor/webhook/migrations/0004_mount_app.py` (24 lines)
- `saleor/webhook/migrations/0005_drop_manage_webhooks_permission.py` (56 lines)
- `saleor/webhook/migrations/0006_auto_20200731_1440.py` (19 lines)
- `saleor/webhook/migrations/0007_auto_20210319_0945.py` (16 lines)
- `saleor/webhook/migrations/0008_webhook_subscription_query.py` (17 lines)
- `saleor/webhook/migrations/0009_webhook_custom_headers.py` (26 lines)
- `saleor/webhook/migrations/0010_drop_transaction_request_action_event.py` (21 lines)
- `saleor/webhook/migrations/0011_webhook_filterable_channel_slugs.py` (31 lines)
- `saleor/webhook/migrations/0012_webhook_filterable_channel_slugs_idx.py` (23 lines)
- `saleor/webhook/migrations/0013_webhook_identifier_and_more.py` (22 lines)
- `saleor/webhook/migrations/0014_webhook_identifier_unique_constraint.py` (49 lines)

## Interactions

- Imports from: `saleor/webhook`, `saleor/core`, `saleor/core/utils`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `saleor.core.utils.json_serializer`
- `saleor.webhook.models`
- `saleor.webhook.validators`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `238fbd1cd886` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
