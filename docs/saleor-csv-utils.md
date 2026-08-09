## Purpose

`saleor/csv/utils` (`saleor/csv/utils`) groups 4 source file(s) exposing 33 top-level declaration(s).

## Public surface

**`saleor/csv/utils/__init__.py`**

- `ProductExportFields` (class) — [saleor/csv/utils/__init__.py:1]

**`saleor/csv/utils/export.py`**

- `export_products` (function) — [saleor/csv/utils/export.py:29]
- `export_gift_cards` (function) — [saleor/csv/utils/export.py:64]
- `export_voucher_codes` (function) — [saleor/csv/utils/export.py:94]
- `get_filename` (function) — [saleor/csv/utils/export.py:129]
- `get_queryset` (function) — [saleor/csv/utils/export.py:136]
- `parse_input` (function) — [saleor/csv/utils/export.py:150]
- `create_file_with_headers` (function) — [saleor/csv/utils/export.py:179]
- `export_products_in_batches` (function) — [saleor/csv/utils/export.py:192]
- `export_gift_cards_in_batches` (function) — [saleor/csv/utils/export.py:225]
- `export_voucher_codes_in_batches` (function) — [saleor/csv/utils/export.py:242]
- `append_to_file` (function) — [saleor/csv/utils/export.py:259]
- `save_csv_file_in_export_file` (function) — [saleor/csv/utils/export.py:275]

**`saleor/csv/utils/product_headers.py`**

- `get_product_export_fields_and_headers_info` (function) — [saleor/csv/utils/product_headers.py:13]
- `get_product_export_fields_and_headers` (function) — [saleor/csv/utils/product_headers.py:34]
- `get_attributes_headers` (function) — [saleor/csv/utils/product_headers.py:61]
- `get_warehouses_headers` (function) — [saleor/csv/utils/product_headers.py:98]
- `get_channels_headers` (function) — [saleor/csv/utils/product_headers.py:118]

**`saleor/csv/utils/products_data.py`**

- `get_products_data` (function) — [saleor/csv/utils/products_data.py:32]
- `get_products_relations_data` (function) — [saleor/csv/utils/products_data.py:113]
- `prepare_products_relations_data` (function) — [saleor/csv/utils/products_data.py:137]
- `get_variants_relations_data` (function) — [saleor/csv/utils/products_data.py:218]
- `prepare_variants_relations_data` (function) — [saleor/csv/utils/products_data.py:243]
- `add_collection_info_to_data` (function) — [saleor/csv/utils/products_data.py:328]
- `add_image_uris_to_data` (function) — [saleor/csv/utils/products_data.py:348]
- `AttributeData` (class) — [saleor/csv/utils/products_data.py:367]
- `handle_attribute_data` (function) — [saleor/csv/utils/products_data.py:386]
- `handle_channel_data` (function) — [saleor/csv/utils/products_data.py:411]
- `handle_warehouse_data` (function) — [saleor/csv/utils/products_data.py:430]
- `add_attribute_info_to_data` (function) — [saleor/csv/utils/products_data.py:451]
- `prepare_attribute_value` (function) — [saleor/csv/utils/products_data.py:481]
- `add_warehouse_info_to_data` (function) — [saleor/csv/utils/products_data.py:547]
- `add_channel_info_to_data` (function) — [saleor/csv/utils/products_data.py:567]

## How it works

The module's files, as provided to this run:

- `saleor/csv/utils/export.py` (278 lines)
- `saleor/csv/utils/__init__.py` (93 lines)
- `saleor/csv/utils/product_headers.py` (154 lines)
- `saleor/csv/utils/products_data.py` (584 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/csv`, `saleor/plugins/openid_connect`
- Imported by: `saleor/core/telemetry`, `saleor/tests`

Internal dependencies named in the source:

- `...FileTypes`
- `...attribute.AttributeInputType`
- `...attribute.models.Attribute`
- `...channel.models.Channel`
- `...core.db.connection.allow_writer`
- `...core.editorjs.editorjs_to_text`
- `...core.utils.batches.queryset_in_batches`
- `...core.utils.build_absolute_uri`
- `...discount.models.VoucherCode`
- `...giftcard.models.GiftCard`
- `...graphql.giftcard.filters.GiftCardFilter`
- `...graphql.product.filters.product.ProductFilter`
- `...product.models.Product`
- `...warehouse.models.Warehouse`
- `..ProductExportFields`
- `..models.ExportFile`
- `..notifications.send_export_download_link_notification`
- `.product_headers.get_product_export_fields_and_headers_info`
- `.products_data.get_products_data`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `69473a953b1a` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
