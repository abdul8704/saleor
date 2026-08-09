## Purpose

`saleor/graphql/invoice` (`saleor/graphql/invoice`) groups 4 source file(s) exposing 6 top-level declaration(s).

## Public surface

**`saleor/graphql/invoice/dataloaders.py`**

- `InvoicesByOrderIdLoader` (class) — [saleor/graphql/invoice/dataloaders.py:7]
- `batch_load` (function) — [saleor/graphql/invoice/dataloaders.py:10]

**`saleor/graphql/invoice/schema.py`**

- `InvoiceMutations` (class) — [saleor/graphql/invoice/schema.py:13]

**`saleor/graphql/invoice/types.py`**

- `Invoice` (class) — [saleor/graphql/invoice/types.py:11]
- `Meta` (class) — [saleor/graphql/invoice/types.py:31]
- `resolve_order` (function) — [saleor/graphql/invoice/types.py:37]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/invoice/__init__.py` (1 lines)
- `saleor/graphql/invoice/dataloaders.py` (19 lines)
- `saleor/graphql/invoice/schema.py` (19 lines)
- `saleor/graphql/invoice/types.py` (45 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...invoice.models`
- `...invoice.models.Invoice`
- `..core.context.SyncWebhookControlContext`
- `..core.dataloaders.DataLoader`
- `..core.scalars.DateTime`
- `..core.types.Job`
- `..core.types.ModelObjectType`
- `..meta.types.ObjectWithMetadata`
- `..order.dataloaders.OrderByIdLoader`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `575752d2e9bc` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
