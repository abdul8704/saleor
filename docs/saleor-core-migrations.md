## Purpose

`saleor/core/migrations` (`saleor/core/migrations`) groups 12 source file(s) exposing 26 top-level declaration(s).

## Public surface

**`saleor/core/migrations/0001_migrate_metadata.py`**

- `flatten_model_metadata` (function) — [saleor/core/migrations/0001_migrate_metadata.py:6]
- `flatten_metadata` (function) — [saleor/core/migrations/0001_migrate_metadata.py:20]
- `flatten_attributes_metadata` (function) — [saleor/core/migrations/0001_migrate_metadata.py:32]
- `flatten_categories_metadata` (function) — [saleor/core/migrations/0001_migrate_metadata.py:38]
- `flatten_checkouts_metadata` (function) — [saleor/core/migrations/0001_migrate_metadata.py:44]
- `flatten_collections_metadata` (function) — [saleor/core/migrations/0001_migrate_metadata.py:50]
- `flatten_digital_contents_metadata` (function) — [saleor/core/migrations/0001_migrate_metadata.py:56]
- `flatten_fulfillments_metadata` (function) — [saleor/core/migrations/0001_migrate_metadata.py:62]
- `flatten_orders_metadata` (function) — [saleor/core/migrations/0001_migrate_metadata.py:68]
- `flatten_products_metadata` (function) — [saleor/core/migrations/0001_migrate_metadata.py:74]
- `flatten_product_types_metadata` (function) — [saleor/core/migrations/0001_migrate_metadata.py:80]
- `flatten_product_variants_metadata` (function) — [saleor/core/migrations/0001_migrate_metadata.py:86]
- `flatten_service_accounts_metadata` (function) — [saleor/core/migrations/0001_migrate_metadata.py:92]
- `flatten_users_metadata` (function) — [saleor/core/migrations/0001_migrate_metadata.py:98]
- `Migration` (class) — [saleor/core/migrations/0001_migrate_metadata.py:104]

**`saleor/core/migrations/0002_initial.py`**

- `Migration` (class) — [saleor/core/migrations/0002_initial.py:7]

**`saleor/core/migrations/0003_eventdeliveryattempt_response_status_code.py`**

- `Migration` (class) — [saleor/core/migrations/0003_eventdeliveryattempt_response_status_code.py:6]

**`saleor/core/migrations/0004_delete_delivery_without_webhook.py`**

- `remove_event_deliveries_without_webhook` (function) — [saleor/core/migrations/0004_delete_delivery_without_webhook.py:4]
- `Migration` (class) — [saleor/core/migrations/0004_delete_delivery_without_webhook.py:11]

**`saleor/core/migrations/0005_alter_eventdelivery_webhook.py`**

- `Migration` (class) — [saleor/core/migrations/0005_alter_eventdelivery_webhook.py:7]

**`saleor/core/migrations/0006_celerytask.py`**

- `Migration` (class) — [saleor/core/migrations/0006_celerytask.py:4]

**`saleor/core/migrations/0007_delete_celerytask.py`**

- `Migration` (class) — [saleor/core/migrations/0007_delete_celerytask.py:8]

**`saleor/core/migrations/0008_drop_openexchangerates_table.py`**

- `Migration` (class) — [saleor/core/migrations/0008_drop_openexchangerates_table.py:9]

**`saleor/core/migrations/0009_add_temporary_vatlayer_tables.py`**

- `Migration` (class) — [saleor/core/migrations/0009_add_temporary_vatlayer_tables.py:13]

**`saleor/core/migrations/0010_drop_vatlayer_tables.py`**

- `Migration` (class) — [saleor/core/migrations/0010_drop_vatlayer_tables.py:9]

**`saleor/core/migrations/0011_eventpayload_payload_file.py`**

- `Migration` (class) — [saleor/core/migrations/0011_eventpayload_payload_file.py:8]

## How it works

The module's files, as provided to this run:

- `saleor/core/migrations/__init__.py` (1 lines)
- `saleor/core/migrations/0001_migrate_metadata.py` (127 lines)
- `saleor/core/migrations/0002_initial.py` (126 lines)
- `saleor/core/migrations/0003_eventdeliveryattempt_response_status_code.py` (17 lines)
- `saleor/core/migrations/0004_delete_delivery_without_webhook.py` (21 lines)
- `saleor/core/migrations/0005_alter_eventdelivery_webhook.py` (21 lines)
- `saleor/core/migrations/0006_celerytask.py` (44 lines)
- `saleor/core/migrations/0007_delete_celerytask.py` (17 lines)
- `saleor/core/migrations/0008_drop_openexchangerates_table.py` (19 lines)
- `saleor/core/migrations/0009_add_temporary_vatlayer_tables.py` (38 lines)
- `saleor/core/migrations/0010_drop_vatlayer_tables.py` (24 lines)
- `saleor/core/migrations/0011_eventpayload_payload_file.py` (34 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `saleor.core.private_storage`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `a5cc3b108456` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
