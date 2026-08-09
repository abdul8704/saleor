## Purpose

`saleor/graphql/invoice/mutations` (`saleor/graphql/invoice/mutations`) groups 7 source file(s) exposing 33 top-level declaration(s).

## Public surface

**`saleor/graphql/invoice/mutations/invoice_create.py`**

- `InvoiceCreateInput` (class) — [saleor/graphql/invoice/mutations/invoice_create.py:20]
- `Meta` (class) — [saleor/graphql/invoice/mutations/invoice_create.py:36]
- `InvoiceCreate` (class) — [saleor/graphql/invoice/mutations/invoice_create.py:40]
- `Arguments` (class) — [saleor/graphql/invoice/mutations/invoice_create.py:41]
- `Meta` (class) — [saleor/graphql/invoice/mutations/invoice_create.py:49]
- `clean_input` (function) — [saleor/graphql/invoice/mutations/invoice_create.py:60]
- `clean_order` (function) — [saleor/graphql/invoice/mutations/invoice_create.py:73]
- `perform_mutation` (function) — [saleor/graphql/invoice/mutations/invoice_create.py:96]

**`saleor/graphql/invoice/mutations/invoice_delete.py`**

- `InvoiceDelete` (class) — [saleor/graphql/invoice/mutations/invoice_delete.py:13]
- `Arguments` (class) — [saleor/graphql/invoice/mutations/invoice_delete.py:14]
- `Meta` (class) — [saleor/graphql/invoice/mutations/invoice_delete.py:17]
- `perform_mutation` (function) — [saleor/graphql/invoice/mutations/invoice_delete.py:26]

**`saleor/graphql/invoice/mutations/invoice_request_delete.py`**

- `InvoiceRequestDelete` (class) — [saleor/graphql/invoice/mutations/invoice_request_delete.py:16]
- `Arguments` (class) — [saleor/graphql/invoice/mutations/invoice_request_delete.py:17]
- `Meta` (class) — [saleor/graphql/invoice/mutations/invoice_request_delete.py:22]
- `perform_mutation` (function) — [saleor/graphql/invoice/mutations/invoice_request_delete.py:37]

**`saleor/graphql/invoice/mutations/invoice_request.py`**

- `InvoiceRequest` (class) — [saleor/graphql/invoice/mutations/invoice_request.py:22]
- `Meta` (class) — [saleor/graphql/invoice/mutations/invoice_request.py:25]
- `Arguments` (class) — [saleor/graphql/invoice/mutations/invoice_request.py:39]
- `clean_order` (function) — [saleor/graphql/invoice/mutations/invoice_request.py:49]
- `perform_mutation` (function) — [saleor/graphql/invoice/mutations/invoice_request.py:72]

**`saleor/graphql/invoice/mutations/invoice_send_notification.py`**

- `InvoiceSendNotification` (class) — [saleor/graphql/invoice/mutations/invoice_send_notification.py:22]
- `Arguments` (class) — [saleor/graphql/invoice/mutations/invoice_send_notification.py:23]
- `Meta` (class) — [saleor/graphql/invoice/mutations/invoice_send_notification.py:26]
- `clean_instance` (function) — [saleor/graphql/invoice/mutations/invoice_send_notification.py:45]
- `perform_mutation` (function) — [saleor/graphql/invoice/mutations/invoice_send_notification.py:72]

**`saleor/graphql/invoice/mutations/invoice_update.py`**

- `UpdateInvoiceInput` (class) — [saleor/graphql/invoice/mutations/invoice_update.py:18]
- `Meta` (class) — [saleor/graphql/invoice/mutations/invoice_update.py:34]
- `InvoiceUpdate` (class) — [saleor/graphql/invoice/mutations/invoice_update.py:38]
- `Arguments` (class) — [saleor/graphql/invoice/mutations/invoice_update.py:39]
- `Meta` (class) — [saleor/graphql/invoice/mutations/invoice_update.py:45]
- `clean_input` (function) — [saleor/graphql/invoice/mutations/invoice_update.py:56]
- `perform_mutation` (function) — [saleor/graphql/invoice/mutations/invoice_update.py:78]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/invoice/mutations/__init__.py` (15 lines)
- `saleor/graphql/invoice/mutations/invoice_create.py` (139 lines)
- `saleor/graphql/invoice/mutations/invoice_delete.py` (36 lines)
- `saleor/graphql/invoice/mutations/invoice_request_delete.py` (50 lines)
- `saleor/graphql/invoice/mutations/invoice_request.py` (120 lines)
- `saleor/graphql/invoice/mutations/invoice_send_notification.py` (88 lines)
- `saleor/graphql/invoice/mutations/invoice_update.py` (122 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....account.models.User`
- `....core.JobStatus`
- `....invoice.error_codes.InvoiceErrorCode`
- `....invoice.events`
- `....invoice.models`
- `....invoice.notifications.send_invoice`
- `....order.events`
- `....order.search.update_order_search_vector`
- `....permission.enums.OrderPermissions`
- `....webhook.event_types.WebhookEventAsyncType`
- `...app.dataloaders.get_app_promise`
- `...core.ResolveInfo`
- `...core.context.SyncWebhookControlContext`
- `...core.doc_category.DOC_CATEGORY_ORDERS`
- `...core.mutations.DeprecatedModelMutation`
- `...core.mutations.ModelDeleteMutation`
- `...core.types.BaseInputObjectType`
- `...core.types.InvoiceError`
- `...core.types.NonNullList`
- `...core.utils.WebhookEventInfo`
- `...meta.inputs.MetadataInput`
- `...meta.inputs.MetadataInputDescription`
- `...order.types.Order`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `..types.Invoice`
- `.invoice_create.InvoiceCreate`
- `.invoice_delete.InvoiceDelete`
- `.invoice_request.InvoiceRequest`
- `.invoice_request_delete.InvoiceRequestDelete`
- `.invoice_send_notification.InvoiceSendNotification`
- `.invoice_update.InvoiceUpdate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `a2dd9aae2acd` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
