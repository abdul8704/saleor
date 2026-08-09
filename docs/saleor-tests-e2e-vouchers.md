## Purpose

`saleor/tests/e2e/vouchers` (`saleor/tests/e2e/vouchers`) groups 15 source file(s) exposing 23 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/vouchers/test_export_voucher_codes.py`**

- `create_vouchers_with_multiple_codes` (function) — [saleor/tests/e2e/vouchers/test_export_voucher_codes.py:15]
- `test_export_valid_voucher_ids_CORE_0925` (function) — [saleor/tests/e2e/vouchers/test_export_voucher_codes.py:59]
- `test_export_voucher_ids_and_codes_CORE_0925` (function) — [saleor/tests/e2e/vouchers/test_export_voucher_codes.py:115]
- `test_export_valid_voucher_code_ids_CORE_0925` (function) — [saleor/tests/e2e/vouchers/test_export_voucher_codes.py:165]
- `test_export_voucher_codes_with_invalid_voucher_id_CORE_0925` (function) — [saleor/tests/e2e/vouchers/test_export_voucher_codes.py:212]
- `test_export_voucher_codes_with_invalid_voucher_codes_CORE_0925` (function) — [saleor/tests/e2e/vouchers/test_export_voucher_codes.py:248]
- `test_export_voucher_codes_without_voucher_id_nor_codes_CORE_0925` (function) — [saleor/tests/e2e/vouchers/test_export_voucher_codes.py:283]
- `test_export_voucher_codes_with_invalid_file_type_CORE_0925` (function) — [saleor/tests/e2e/vouchers/test_export_voucher_codes.py:325]

**`saleor/tests/e2e/vouchers/test_staff_can_delete_vouchers_in_bulk.py`**

- `create_multiple_vouchers` (function) — [saleor/tests/e2e/vouchers/test_staff_can_delete_vouchers_in_bulk.py:13]
- `test_staff_can_delete_vouchers_in_bulk_CORE_0924` (function) — [saleor/tests/e2e/vouchers/test_staff_can_delete_vouchers_in_bulk.py:43]

**`saleor/tests/e2e/vouchers/utils/prepare_voucher.py`**

- `prepare_voucher` (function) — [saleor/tests/e2e/vouchers/utils/prepare_voucher.py:4]

**`saleor/tests/e2e/vouchers/utils/query_voucher.py`**

- `get_voucher` (function) — [saleor/tests/e2e/vouchers/utils/query_voucher.py:31]

**`saleor/tests/e2e/vouchers/utils/query_vouchers.py`**

- `get_vouchers` (function) — [saleor/tests/e2e/vouchers/utils/query_vouchers.py:16]

**`saleor/tests/e2e/vouchers/utils/voucher_bulk_delete.py`**

- `voucher_bulk_delete` (function) — [saleor/tests/e2e/vouchers/utils/voucher_bulk_delete.py:18]

**`saleor/tests/e2e/vouchers/utils/voucher_catalogues_add.py`**

- `add_catalogue_to_voucher` (function) — [saleor/tests/e2e/vouchers/utils/voucher_catalogues_add.py:29]

**`saleor/tests/e2e/vouchers/utils/voucher_channel_listing.py`**

- `create_voucher_channel_listing` (function) — [saleor/tests/e2e/vouchers/utils/voucher_channel_listing.py:33]

**`saleor/tests/e2e/vouchers/utils/voucher_code_bulk_delete.py`**

- `voucher_code_bulk_delete` (function) — [saleor/tests/e2e/vouchers/utils/voucher_code_bulk_delete.py:16]

**`saleor/tests/e2e/vouchers/utils/voucher_codes_export.py`**

- `raw_export_voucher_codes` (function) — [saleor/tests/e2e/vouchers/utils/voucher_codes_export.py:20]
- `export_voucher_codes` (function) — [saleor/tests/e2e/vouchers/utils/voucher_codes_export.py:35]

**`saleor/tests/e2e/vouchers/utils/voucher_create.py`**

- `create_voucher` (function) — [saleor/tests/e2e/vouchers/utils/voucher_create.py:33]

**`saleor/tests/e2e/vouchers/utils/voucher_delete.py`**

- `voucher_delete` (function) — [saleor/tests/e2e/vouchers/utils/voucher_delete.py:20]

**`saleor/tests/e2e/vouchers/utils/voucher_update.py`**

- `raw_update_voucher` (function) — [saleor/tests/e2e/vouchers/utils/voucher_update.py:34]
- `update_voucher` (function) — [saleor/tests/e2e/vouchers/utils/voucher_update.py:52]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/vouchers/__init__.py` (1 lines)
- `saleor/tests/e2e/vouchers/test_export_voucher_codes.py` (370 lines)
- `saleor/tests/e2e/vouchers/test_staff_can_delete_vouchers_in_bulk.py` (80 lines)
- `saleor/tests/e2e/vouchers/utils/__init__.py` (25 lines)
- `saleor/tests/e2e/vouchers/utils/prepare_voucher.py` (40 lines)
- `saleor/tests/e2e/vouchers/utils/query_voucher.py` (40 lines)
- `saleor/tests/e2e/vouchers/utils/query_vouchers.py` (22 lines)
- `saleor/tests/e2e/vouchers/utils/voucher_bulk_delete.py` (32 lines)
- `saleor/tests/e2e/vouchers/utils/voucher_catalogues_add.py` (58 lines)
- `saleor/tests/e2e/vouchers/utils/voucher_channel_listing.py` (63 lines)
- `saleor/tests/e2e/vouchers/utils/voucher_code_bulk_delete.py` (30 lines)
- `saleor/tests/e2e/vouchers/utils/voucher_codes_export.py` (43 lines)
- `saleor/tests/e2e/vouchers/utils/voucher_create.py` (50 lines)
- `saleor/tests/e2e/vouchers/utils/voucher_delete.py` (34 lines)
- `saleor/tests/e2e/vouchers/utils/voucher_update.py` (59 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...utils.get_graphql_content`
- `...vouchers.utils.create_voucher`
- `...vouchers.utils.create_voucher_channel_listing`
- `..shop.utils.preparing_shop.prepare_default_shop`
- `..utils.assign_permissions`
- `.query_voucher.get_voucher`
- `.query_vouchers.get_vouchers`
- `.voucher_bulk_delete.voucher_bulk_delete`
- `.voucher_catalogues_add.add_catalogue_to_voucher`
- `.voucher_channel_listing.create_voucher_channel_listing`
- `.voucher_code_bulk_delete.voucher_code_bulk_delete`
- `.voucher_codes_export.export_voucher_codes`
- `.voucher_codes_export.raw_export_voucher_codes`
- `.voucher_create.create_voucher`
- `.voucher_delete.voucher_delete`
- `.voucher_update.raw_update_voucher`
- `.voucher_update.update_voucher`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c1b01453c3d9` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
