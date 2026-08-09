## Purpose

`saleor/graphql/csv/mutations` (`saleor/graphql/csv/mutations`) groups 5 source file(s) exposing 29 top-level declaration(s).

## Public surface

**`saleor/graphql/csv/mutations/base_export.py`**

- `BaseExportMutation` (class) — [saleor/graphql/csv/mutations/base_export.py:12]
- `Meta` (class) — [saleor/graphql/csv/mutations/base_export.py:20]
- `get_scope` (function) — [saleor/graphql/csv/mutations/base_export.py:24]
- `clean_ids` (function) — [saleor/graphql/csv/mutations/base_export.py:33]
- `clean_filter` (function) — [saleor/graphql/csv/mutations/base_export.py:48]

**`saleor/graphql/csv/mutations/export_gift_cards.py`**

- `ExportGiftCardsInput` (class) — [saleor/graphql/csv/mutations/export_gift_cards.py:19]
- `Meta` (class) — [saleor/graphql/csv/mutations/export_gift_cards.py:33]
- `ExportGiftCards` (class) — [saleor/graphql/csv/mutations/export_gift_cards.py:37]
- `Arguments` (class) — [saleor/graphql/csv/mutations/export_gift_cards.py:38]
- `Meta` (class) — [saleor/graphql/csv/mutations/export_gift_cards.py:43]
- `perform_mutation` (function) — [saleor/graphql/csv/mutations/export_gift_cards.py:60]

**`saleor/graphql/csv/mutations/export_products.py`**

- `ExportInfoInput` (class) — [saleor/graphql/csv/mutations/export_products.py:41]
- `Meta` (class) — [saleor/graphql/csv/mutations/export_products.py:59]
- `ExportProductsInput` (class) — [saleor/graphql/csv/mutations/export_products.py:63]
- `Meta` (class) — [saleor/graphql/csv/mutations/export_products.py:81]
- `ExportProducts` (class) — [saleor/graphql/csv/mutations/export_products.py:85]
- `Arguments` (class) — [saleor/graphql/csv/mutations/export_products.py:86]
- `Meta` (class) — [saleor/graphql/csv/mutations/export_products.py:91]
- `perform_mutation` (function) — [saleor/graphql/csv/mutations/export_products.py:109]
- `add_channel_to_filter_scope` (function) — [saleor/graphql/csv/mutations/export_products.py:135]
- `get_export_info` (function) — [saleor/graphql/csv/mutations/export_products.py:178]
- `get_items_pks` (function) — [saleor/graphql/csv/mutations/export_products.py:196]

**`saleor/graphql/csv/mutations/export_voucher_codes.py`**

- `ExportVoucherCodesInput` (class) — [saleor/graphql/csv/mutations/export_voucher_codes.py:20]
- `Meta` (class) — [saleor/graphql/csv/mutations/export_voucher_codes.py:35]
- `ExportVoucherCodes` (class) — [saleor/graphql/csv/mutations/export_voucher_codes.py:39]
- `Arguments` (class) — [saleor/graphql/csv/mutations/export_voucher_codes.py:40]
- `Meta` (class) — [saleor/graphql/csv/mutations/export_voucher_codes.py:45]
- `clean_input` (function) — [saleor/graphql/csv/mutations/export_voucher_codes.py:58]
- `perform_mutation` (function) — [saleor/graphql/csv/mutations/export_voucher_codes.py:89]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/csv/mutations/__init__.py` (5 lines)
- `saleor/graphql/csv/mutations/base_export.py` (59 lines)
- `saleor/graphql/csv/mutations/export_gift_cards.py` (75 lines)
- `saleor/graphql/csv/mutations/export_products.py` (201 lines)
- `saleor/graphql/csv/mutations/export_voucher_codes.py` (108 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....channel.models`
- `....csv.error_codes.ExportErrorCode`
- `....csv.events.export_started_event`
- `....csv.models`
- `....csv.tasks.export_gift_cards_task`
- `....csv.tasks.export_products_task`
- `....csv.tasks.export_voucher_codes_task`
- `....permission.enums.DiscountPermissions`
- `....permission.enums.GiftcardPermissions`
- `....permission.enums.ProductPermissions`
- `....webhook.event_types.WebhookEventAsyncType`
- `...app.dataloaders.get_app_promise`
- `...attribute.types.Attribute`
- `...channel.types.Channel`
- `...core.ResolveInfo`
- `...core.doc_category.DOC_CATEGORY_DISCOUNTS`
- `...core.doc_category.DOC_CATEGORY_GIFT_CARDS`
- `...core.doc_category.DOC_CATEGORY_PRODUCTS`
- `...core.enums.ExportErrorCode`
- `...core.mutations.BaseMutation`
- `...core.types.BaseInputObjectType`
- `...core.types.ExportError`
- `...core.types.NonNullList`
- `...core.utils.WebhookEventInfo`
- `...core.utils.raise_validation_error`
- `...core.validators.validate_one_of_args_is_in_mutation`
- `...giftcard.filters.GiftCardFilterInput`
- `...giftcard.types.GiftCard`
- `...product.filters.product.ProductFilterInput`
- `...product.types.Product`
- `...warehouse.types.Warehouse`
- `..enums.ExportScope`
- `..enums.FileTypeEnum`
- `..enums.ProductFieldEnum`
- `..types.ExportFile`
- `.base_export.BaseExportMutation`
- `.export_gift_cards.ExportGiftCards`
- `.export_products.ExportProducts`
- `.export_voucher_codes.ExportVoucherCodes`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `5542ff831286` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
