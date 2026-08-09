## Purpose

`saleor/core/management` (`saleor/core/management`) groups 10 source file(s) exposing 38 top-level declaration(s).

## Public surface

**`saleor/core/management/commands/clean_editorjs_fields.py`**

- `Command` (class) — [saleor/core/management/commands/clean_editorjs_fields.py:54]
- `add_arguments` (function) — [saleor/core/management/commands/clean_editorjs_fields.py:57]
- `handle` (function) — [saleor/core/management/commands/clean_editorjs_fields.py:119]
- `clean_model` (function) — [saleor/core/management/commands/clean_editorjs_fields.py:162]

**`saleor/core/management/commands/cleardb.py`**

- `Command` (class) — [saleor/core/management/commands/cleardb.py:26]
- `add_arguments` (function) — [saleor/core/management/commands/cleardb.py:29]
- `handle` (function) — [saleor/core/management/commands/cleardb.py:41]

**`saleor/core/management/commands/clearorders.py`**

- `Command` (class) — [saleor/core/management/commands/clearorders.py:44]
- `add_arguments` (function) — [saleor/core/management/commands/clearorders.py:47]
- `handle` (function) — [saleor/core/management/commands/clearorders.py:54]
- `delete_allocations` (function) — [saleor/core/management/commands/clearorders.py:68]
- `delete_reservations` (function) — [saleor/core/management/commands/clearorders.py:77]
- `delete_checkouts` (function) — [saleor/core/management/commands/clearorders.py:86]
- `delete_payments` (function) — [saleor/core/management/commands/clearorders.py:115]
- `delete_invoices` (function) — [saleor/core/management/commands/clearorders.py:135]
- `delete_gift_cards` (function) — [saleor/core/management/commands/clearorders.py:143]
- `delete_orders` (function) — [saleor/core/management/commands/clearorders.py:160]
- `delete_unassigned_addresses` (function) — [saleor/core/management/commands/clearorders.py:186]
- `delete_customers` (function) — [saleor/core/management/commands/clearorders.py:195]

**`saleor/core/management/commands/delete_event_payloads.py`**

- `Command` (class) — [saleor/core/management/commands/delete_event_payloads.py:6]
- `handle` (function) — [saleor/core/management/commands/delete_event_payloads.py:13]

**`saleor/core/management/commands/generate_json_schemas.py`**

- `Command` (class) — [saleor/core/management/commands/generate_json_schemas.py:14]
- `handle` (function) — [saleor/core/management/commands/generate_json_schemas.py:17]
- `export_single_schemas` (function) — [saleor/core/management/commands/generate_json_schemas.py:23]
- `export_combined_schemas` (function) — [saleor/core/management/commands/generate_json_schemas.py:32]
- `get_schemas` (function) — [saleor/core/management/commands/generate_json_schemas.py:46]
- `get_schema_title` (function) — [saleor/core/management/commands/generate_json_schemas.py:60]
- `write_schema_to_file` (function) — [saleor/core/management/commands/generate_json_schemas.py:67]
- `clear_dir` (function) — [saleor/core/management/commands/generate_json_schemas.py:76]

**`saleor/core/management/commands/populatedb.py`**

- `Command` (class) — [saleor/core/management/commands/populatedb.py:34]
- `add_arguments` (function) — [saleor/core/management/commands/populatedb.py:38]
- `sequence_reset` (function) — [saleor/core/management/commands/populatedb.py:64]
- `handle` (function) — [saleor/core/management/commands/populatedb.py:80]

**`saleor/core/management/commands/remove_invalid_files.py`**

- `Command` (class) — [saleor/core/management/commands/remove_invalid_files.py:17]
- `add_arguments` (function) — [saleor/core/management/commands/remove_invalid_files.py:25]
- `handle` (function) — [saleor/core/management/commands/remove_invalid_files.py:35]

**`saleor/core/management/commands/update_search_indexes.py`**

- `Command` (class) — [saleor/core/management/commands/update_search_indexes.py:10]
- `handle` (function) — [saleor/core/management/commands/update_search_indexes.py:13]

## How it works

The module's files, as provided to this run:

- `saleor/core/management/__init__.py` (1 lines)
- `saleor/core/management/commands/__init__.py` (1 lines)
- `saleor/core/management/commands/clean_editorjs_fields.py` (242 lines)
- `saleor/core/management/commands/cleardb.py` (118 lines)
- `saleor/core/management/commands/clearorders.py` (207 lines)
- `saleor/core/management/commands/delete_event_payloads.py` (14 lines)
- `saleor/core/management/commands/generate_json_schemas.py` (78 lines)
- `saleor/core/management/commands/populatedb.py` (147 lines)
- `saleor/core/management/commands/remove_invalid_files.py` (197 lines)
- `saleor/core/management/commands/update_search_indexes.py` (24 lines)

## Interactions

- Imports from: `saleor/webhook`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....account.models.Address`
- `....account.models.CustomerEvent`
- `....account.models.CustomerNote`
- `....account.models.User`
- `....account.tests.fixtures.user.dangerously_get_or_create_superuser`
- `....attribute.models.Attribute`
- `....attribute.models.AttributeValue`
- `....attribute.models.AttributeValueTranslation`
- `....checkout.models.Checkout`
- `....discount.models.Promotion`
- `....discount.models.Voucher`
- `....giftcard.models.GiftCard`
- `....giftcard.models.GiftCardEvent`
- `....giftcard.models.GiftCardTag`
- `....graphql.core.validators.file.detect_mime_type`
- `....invoice.models.Invoice`
- `....invoice.models.InvoiceEvent`
- `....order.models.Order`
- `....page.models.Page`
- `....page.models.PageTranslation`
- `....page.models.PageType`
- `....payment.models.Payment`
- `....payment.models.Transaction`
- `....payment.models.TransactionEvent`
- `....payment.models.TransactionItem`
- `....product.models.Category`
- `....product.models.Collection`
- `....product.models.Product`
- `....product.models.ProductType`
- `....shipping.models.ShippingMethod`
- `....shipping.models.ShippingMethodTranslation`
- `....shipping.models.ShippingZone`
- `....warehouse.models.Warehouse`
- `....webhook.models.Webhook`
- `....webhook.response_schemas.COMBINED_SCHEMAS_TO_EXPORT`
- `....webhook.response_schemas.SCHEMAS_TO_EXPORT`
- `...editorjs.clean_editorjs`
- `...tasks.delete_event_payloads_task`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `17cda1c64519` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
