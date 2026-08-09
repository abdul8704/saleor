## Purpose

`saleor/graphql/invoice/tests` (`saleor/graphql/invoice/tests`) groups 7 source file(s) exposing 38 top-level declaration(s).

## Public surface

**`saleor/graphql/invoice/tests/test_invoice_create.py`**

- `test_create_invoice` (function) — [saleor/graphql/invoice/tests/test_invoice_create.py:43]
- `test_create_invoice_by_user_no_channel_access` (function) — [saleor/graphql/invoice/tests/test_invoice_create.py:96]
- `test_create_invoice_by_app` (function) — [saleor/graphql/invoice/tests/test_invoice_create.py:123]
- `test_create_invoice_no_billing_address` (function) — [saleor/graphql/invoice/tests/test_invoice_create.py:170]
- `test_create_invoice_invalid_order_status` (function) — [saleor/graphql/invoice/tests/test_invoice_create.py:202]
- `test_create_invoice_invalid_id` (function) — [saleor/graphql/invoice/tests/test_invoice_create.py:231]
- `test_create_invoice_empty_params` (function) — [saleor/graphql/invoice/tests/test_invoice_create.py:252]

**`saleor/graphql/invoice/tests/test_invoice_delete.py`**

- `test_invoice_delete` (function) — [saleor/graphql/invoice/tests/test_invoice_delete.py:23]
- `test_invoice_delete_by_user_no_channel_access` (function) — [saleor/graphql/invoice/tests/test_invoice_delete.py:45]
- `test_invoice_delete_by_app` (function) — [saleor/graphql/invoice/tests/test_invoice_delete.py:64]
- `test_invoice_delete_invalid_id` (function) — [saleor/graphql/invoice/tests/test_invoice_delete.py:89]

**`saleor/graphql/invoice/tests/test_invoice_request_delete.py`**

- `setup_dummy_gateways` (function) — [saleor/graphql/invoice/tests/test_invoice_request_delete.py:25]
- `test_invoice_request_delete` (function) — [saleor/graphql/invoice/tests/test_invoice_request_delete.py:33]
- `test_invoice_request_delete_by_user_no_channel_access` (function) — [saleor/graphql/invoice/tests/test_invoice_request_delete.py:55]
- `test_invoice_request_delete_by_app` (function) — [saleor/graphql/invoice/tests/test_invoice_request_delete.py:74]
- `test_invoice_request_delete_invalid_id` (function) — [saleor/graphql/invoice/tests/test_invoice_request_delete.py:101]
- `test_invoice_request_delete_no_permission` (function) — [saleor/graphql/invoice/tests/test_invoice_request_delete.py:120]

**`saleor/graphql/invoice/tests/test_invoice_request.py`**

- `setup_dummy_gateways` (function) — [saleor/graphql/invoice/tests/test_invoice_request.py:37]
- `test_invoice_request` (function) — [saleor/graphql/invoice/tests/test_invoice_request.py:49]
- `test_invoice_request_by_user_no_channel_access` (function) — [saleor/graphql/invoice/tests/test_invoice_request.py:97]
- `test_invoice_request_by_app` (function) — [saleor/graphql/invoice/tests/test_invoice_request.py:129]
- `test_invoice_request_invalid_order_status` (function) — [saleor/graphql/invoice/tests/test_invoice_request.py:181]
- `test_invoice_request_no_billing_address` (function) — [saleor/graphql/invoice/tests/test_invoice_request.py:206]
- `test_invoice_request_no_number` (function) — [saleor/graphql/invoice/tests/test_invoice_request.py:235]
- `test_invoice_request_invalid_id` (function) — [saleor/graphql/invoice/tests/test_invoice_request.py:251]
- `test_invoice_request_no_invoice_plugin` (function) — [saleor/graphql/invoice/tests/test_invoice_request.py:273]

**`saleor/graphql/invoice/tests/test_invoice_update.py`**

- `test_invoice_update` (function) — [saleor/graphql/invoice/tests/test_invoice_update.py:36]
- `test_invoice_update_by_user_no_channel_access` (function) — [saleor/graphql/invoice/tests/test_invoice_update.py:68]
- `test_invoice_update_by_app` (function) — [saleor/graphql/invoice/tests/test_invoice_update.py:98]
- `test_invoice_update_single_value` (function) — [saleor/graphql/invoice/tests/test_invoice_update.py:137]
- `test_invoice_update_missing_number` (function) — [saleor/graphql/invoice/tests/test_invoice_update.py:163]
- `test_invoice_update_invalid_id` (function) — [saleor/graphql/invoice/tests/test_invoice_update.py:188]

**`saleor/graphql/invoice/tests/test_send_invoice_notification.py`**

- `test_invoice_send_notification_by_user` (function) — [saleor/graphql/invoice/tests/test_send_invoice_notification.py:29]
- `test_invoice_send_notification_by_user_no_channel_access` (function) — [saleor/graphql/invoice/tests/test_send_invoice_notification.py:66]
- `test_invoice_send_notification_by_app` (function) — [saleor/graphql/invoice/tests/test_send_invoice_notification.py:90]
- `test_invoice_send_notification_pending` (function) — [saleor/graphql/invoice/tests/test_send_invoice_notification.py:129]
- `test_invoice_send_notification_without_url_and_number` (function) — [saleor/graphql/invoice/tests/test_send_invoice_notification.py:155]
- `test_invoice_send_email_without_email` (function) — [saleor/graphql/invoice/tests/test_send_invoice_notification.py:181]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/invoice/tests/__init__.py` (1 lines)
- `saleor/graphql/invoice/tests/test_invoice_create.py` (283 lines)
- `saleor/graphql/invoice/tests/test_invoice_delete.py` (104 lines)
- `saleor/graphql/invoice/tests/test_invoice_request_delete.py` (132 lines)
- `saleor/graphql/invoice/tests/test_invoice_request.py` (293 lines)
- `saleor/graphql/invoice/tests/test_invoice_update.py` (200 lines)
- `saleor/graphql/invoice/tests/test_send_invoice_notification.py` (204 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....core.JobStatus`
- `....core.notify.NotifyEventType`
- `....core.tests.utils.get_site_context_payload`
- `....graphql.tests.utils.assert_no_permission`
- `....graphql.tests.utils.get_graphql_content`
- `....invoice.error_codes.InvoiceErrorCode`
- `....invoice.models.Invoice`
- `....invoice.models.InvoiceEvent`
- `....invoice.models.InvoiceEvents`
- `....invoice.notifications.get_invoice_payload`
- `....order.OrderEvents`
- `....order.OrderStatus`
- `....order.models.OrderEvent`
- `...core.utils.to_global_id_or_none`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `4e72ff941feb` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
