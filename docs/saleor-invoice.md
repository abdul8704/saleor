## Purpose

`saleor/invoice` (`saleor/invoice`) groups 7 source file(s) exposing 19 top-level declaration(s).

## Public surface

**`saleor/invoice/__init__.py`**

- `InvoiceEvents` (class) — [saleor/invoice/__init__.py:1]

**`saleor/invoice/error_codes.py`**

- `InvoiceErrorCode` (class) — [saleor/invoice/error_codes.py:4]

**`saleor/invoice/events.py`**

- `invoice_requested_event` (function) — [saleor/invoice/events.py:7]
- `invoice_requested_deletion_event` (function) — [saleor/invoice/events.py:19]
- `invoice_created_event` (function) — [saleor/invoice/events.py:31]
- `invoice_deleted_event` (function) — [saleor/invoice/events.py:44]
- `notification_invoice_sent_event` (function) — [saleor/invoice/events.py:55]

**`saleor/invoice/models.py`**

- `InvoiceQueryset` (class) — [saleor/invoice/models.py:16]
- `ready` (function) — [saleor/invoice/models.py:17]
- `Invoice` (class) — [saleor/invoice/models.py:24]
- `url` (function) — [saleor/invoice/models.py:39]
- `url` (function) — [saleor/invoice/models.py:45]
- `update_invoice` (function) — [saleor/invoice/models.py:48]
- `Meta` (class) — [saleor/invoice/models.py:54]
- `InvoiceEvent` (class) — [saleor/invoice/models.py:62]
- `Meta` (class) — [saleor/invoice/models.py:86]

**`saleor/invoice/notifications.py`**

- `get_invoice_payload` (function) — [saleor/invoice/notifications.py:14]
- `send_invoice` (function) — [saleor/invoice/notifications.py:23]

**`saleor/invoice/tests/test_notifications.py`**

- `test_collect_invoice_data_for_email` (function) — [saleor/invoice/tests/test_notifications.py:6]

## How it works

The module's files, as provided to this run:

- `saleor/invoice/__init__.py` (14 lines)
- `saleor/invoice/error_codes.py` (12 lines)
- `saleor/invoice/events.py` (68 lines)
- `saleor/invoice/models.py` (90 lines)
- `saleor/invoice/notifications.py` (51 lines)
- `saleor/invoice/tests/__init__.py` (1 lines)
- `saleor/invoice/tests/test_notifications.py` (13 lines)

## Interactions

- Imports from: `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...graphql.core.utils.to_global_id_or_none`
- `..InvoiceEvents`
- `..account.models.User`
- `..app.models.App`
- `..core.JobStatus`
- `..core.models.Job`
- `..core.models.ModelWithMetadata`
- `..core.notification.utils.get_site_context`
- `..core.notify.NotifyEventType`
- `..core.notify.NotifyHandler`
- `..core.utils.build_absolute_uri`
- `..core.utils.json_serializer.CustomJsonEncoder`
- `..graphql.core.utils.to_global_id_or_none`
- `..models.Invoice`
- `..notifications.get_invoice_payload`
- `..order.models.Order`
- `..plugins.manager.PluginsManager`
- `.models.Invoice`
- `.models.InvoiceEvent`
- `.models.InvoiceEvents`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `3a2d3967dce9` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
