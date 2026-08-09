## Purpose

`saleor/csv` (`saleor/csv`) groups 6 source file(s) exposing 21 top-level declaration(s).

## Public surface

**`saleor/csv/__init__.py`**

- `ExportEvents` (class) — [saleor/csv/__init__.py:1]
- `FileTypes` (class) — [saleor/csv/__init__.py:27]

**`saleor/csv/error_codes.py`**

- `ExportErrorCode` (class) — [saleor/csv/error_codes.py:4]

**`saleor/csv/events.py`**

- `export_started_event` (function) — [saleor/csv/events.py:14]
- `export_success_event` (function) — [saleor/csv/events.py:26]
- `export_failed_event` (function) — [saleor/csv/events.py:38]
- `export_deleted_event` (function) — [saleor/csv/events.py:56]
- `export_file_sent_event` (function) — [saleor/csv/events.py:68]
- `export_failed_info_sent_event` (function) — [saleor/csv/events.py:77]

**`saleor/csv/models.py`**

- `ExportFile` (class) — [saleor/csv/models.py:12]
- `ExportEvent` (class) — [saleor/csv/models.py:22]

**`saleor/csv/notifications.py`**

- `get_default_export_payload` (function) — [saleor/csv/notifications.py:13]
- `send_export_download_link_notification` (function) — [saleor/csv/notifications.py:29]
- `send_export_failed_info` (function) — [saleor/csv/notifications.py:53]

**`saleor/csv/tasks.py`**

- `ExportTask` (class) — [saleor/csv/tasks.py:20]
- `on_failure` (function) — [saleor/csv/tasks.py:28]
- `on_success` (function) — [saleor/csv/tasks.py:49]
- `export_products_task` (function) — [saleor/csv/tasks.py:61]
- `export_gift_cards_task` (function) — [saleor/csv/tasks.py:78]
- `export_voucher_codes_task` (function) — [saleor/csv/tasks.py:94]
- `delete_old_export_files` (function) — [saleor/csv/tasks.py:111]

## How it works

The module's files, as provided to this run:

- `saleor/csv/__init__.py` (34 lines)
- `saleor/csv/error_codes.py` (8 lines)
- `saleor/csv/events.py` (82 lines)
- `saleor/csv/models.py` (36 lines)
- `saleor/csv/notifications.py` (73 lines)
- `saleor/csv/tasks.py` (134 lines)

## Interactions

- Imports from: `saleor/webhook`, `saleor/core/db`
- Imported by: `saleor/csv/tests`, `saleor/csv/utils`

Internal dependencies named in the source:

- `..ExportEvents`
- `..account.models.User`
- `..app.models.App`
- `..celeryconf.app`
- `..core.JobStatus`
- `..core.db.connection.allow_writer`
- `..core.models.Job`
- `..core.notification.utils.get_site_context`
- `..core.notify.NotifyEventType`
- `..core.notify.NotifyHandler`
- `..core.tasks.RestrictWriterDBTask`
- `..core.utils.build_absolute_uri`
- `..core.utils.json_serializer.CustomJsonEncoder`
- `..events`
- `..graphql.core.utils.to_global_id_or_none`
- `..plugins.manager.get_plugins_manager`
- `.models.ExportEvent`
- `.models.ExportFile`
- `.notifications.send_export_failed_info`
- `.utils.export.export_gift_cards`
- `.utils.export.export_products`
- `.utils.export.export_voucher_codes`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `1f9ecafdbac2` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
