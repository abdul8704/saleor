## Purpose

`saleor/graphql/csv/tests` (`saleor/graphql/csv/tests`) groups 8 source file(s) exposing 48 top-level declaration(s).

## Public surface

**`saleor/graphql/csv/tests/mutations/test_export_gift_cards.py`**

- `test_export_gift_cards_mutation` (function) — [saleor/graphql/csv/tests/mutations/test_export_gift_cards.py:59]
- `test_export_gift_cards_mutation_ids_scope` (function) — [saleor/graphql/csv/tests/mutations/test_export_gift_cards.py:101]
- `test_export_gift_cards_mutation_ids_scope_invalid_object_type` (function) — [saleor/graphql/csv/tests/mutations/test_export_gift_cards.py:163]
- `test_export_gift_cards_mutation_failed` (function) — [saleor/graphql/csv/tests/mutations/test_export_gift_cards.py:237]
- `test_export_gift_cards_mutation_by_app` (function) — [saleor/graphql/csv/tests/mutations/test_export_gift_cards.py:306]
- `test_export_gift_cards_webhooks` (function) — [saleor/graphql/csv/tests/mutations/test_export_gift_cards.py:354]

**`saleor/graphql/csv/tests/mutations/test_export_products.py`**

- `test_export_products_mutation_all_scope` (function) — [saleor/graphql/csv/tests/mutations/test_export_products.py:64]
- `test_export_products_mutation_filter_scope_with_channel` (function) — [saleor/graphql/csv/tests/mutations/test_export_products.py:109]
- `test_export_products_mutation_by_app` (function) — [saleor/graphql/csv/tests/mutations/test_export_products.py:160]
- `test_export_products_mutation_ids_scope` (function) — [saleor/graphql/csv/tests/mutations/test_export_products.py:207]
- `test_export_products_mutation_ids_scope_invalid_object_type` (function) — [saleor/graphql/csv/tests/mutations/test_export_products.py:272]
- `test_export_products_mutation_with_warehouse_and_attribute_ids` (function) — [saleor/graphql/csv/tests/mutations/test_export_products.py:321]
- `test_export_products_mutation_with_warehouse_ids_invalid_object_type` (function) — [saleor/graphql/csv/tests/mutations/test_export_products.py:406]
- `test_export_products_mutation_with_attribute_ids_invalid_object_type` (function) — [saleor/graphql/csv/tests/mutations/test_export_products.py:466]
- `test_export_products_mutation_with_channel_ids_invalid_object_type` (function) — [saleor/graphql/csv/tests/mutations/test_export_products.py:526]
- `test_export_products_mutation_failed` (function) — [saleor/graphql/csv/tests/mutations/test_export_products.py:607]
- `test_export_products_webhooks` (function) — [saleor/graphql/csv/tests/mutations/test_export_products.py:640]
- `test_export_products_with_channel_dependent_filter_requires_channel` (function) — [saleor/graphql/csv/tests/mutations/test_export_products.py:685]
- `test_export_products_with_channel_dependent_filter_no_channel_returns_error` (function) — [saleor/graphql/csv/tests/mutations/test_export_products.py:740]
- `test_export_products_with_channel_dependent_filter_multiple_channels_returns_error` (function) — [saleor/graphql/csv/tests/mutations/test_export_products.py:780]
- `test_export_products_with_non_channel_filter_does_not_require_channel` (function) — [saleor/graphql/csv/tests/mutations/test_export_products.py:825]
- `test_export_products_with_channel_dependent_filter_invalid_channel_returns_error` (function) — [saleor/graphql/csv/tests/mutations/test_export_products.py:867]

**`saleor/graphql/csv/tests/mutations/test_export_voucher_codes.py`**

- `test_export_voucher_codes_by_voucher_id` (function) — [saleor/graphql/csv/tests/mutations/test_export_voucher_codes.py:40]
- `test_export_voucher_codes_by_voucher_code_ids` (function) — [saleor/graphql/csv/tests/mutations/test_export_voucher_codes.py:83]
- `test_export_voucher_codes_by_app` (function) — [saleor/graphql/csv/tests/mutations/test_export_voucher_codes.py:129]
- `test_export_voucher_codes_by_staff_no_permission` (function) — [saleor/graphql/csv/tests/mutations/test_export_voucher_codes.py:190]
- `test_export_voucher_codes_by_app_no_permission` (function) — [saleor/graphql/csv/tests/mutations/test_export_voucher_codes.py:213]
- `test_export_voucher_codes_error_too_many_arguments` (function) — [saleor/graphql/csv/tests/mutations/test_export_voucher_codes.py:236]
- `test_export_voucher_codes_error_lack_of_required_argument` (function) — [saleor/graphql/csv/tests/mutations/test_export_voucher_codes.py:272]
- `test_export_voucher_codes_error_invalid_voucher_id` (function) — [saleor/graphql/csv/tests/mutations/test_export_voucher_codes.py:296]
- `test_export_voucher_codes_error_invalid_voucher_code_ids` (function) — [saleor/graphql/csv/tests/mutations/test_export_voucher_codes.py:327]
- `test_export_voucher_webhooks` (function) — [saleor/graphql/csv/tests/mutations/test_export_voucher_codes.py:362]

**`saleor/graphql/csv/tests/queries/test_export_file.py`**

- `test_query_export_file` (function) — [saleor/graphql/csv/tests/queries/test_export_file.py:60]
- `test_query_export_file_by_app` (function) — [saleor/graphql/csv/tests/queries/test_export_file.py:97]
- `test_query_export_file_export_file_with_app` (function) — [saleor/graphql/csv/tests/queries/test_export_file.py:135]
- `test_query_export_file_export_file_with_removed_app` (function) — [saleor/graphql/csv/tests/queries/test_export_file.py:175]
- `test_query_export_file_as_app` (function) — [saleor/graphql/csv/tests/queries/test_export_file.py:217]
- `test_query_export_file_by_invalid_id` (function) — [saleor/graphql/csv/tests/queries/test_export_file.py:256]
- `test_query_export_file_with_invalid_object_type` (function) — [saleor/graphql/csv/tests/queries/test_export_file.py:270]
- `test_query_export_file_user_field_denied_for_app_with_only_manage_staff` (function) — [saleor/graphql/csv/tests/queries/test_export_file.py:281]

**`saleor/graphql/csv/tests/queries/test_export_files.py`**

- `test_filter_export_files_by_status` (function) — [saleor/graphql/csv/tests/queries/test_export_files.py:66]
- `test_filter_export_files_by_created_at_date` (function) — [saleor/graphql/csv/tests/queries/test_export_files.py:95]
- `test_filter_export_files_by_ended_at_date` (function) — [saleor/graphql/csv/tests/queries/test_export_files.py:124]
- `test_filter_export_files_by_user` (function) — [saleor/graphql/csv/tests/queries/test_export_files.py:146]
- `test_filter_export_files_by_app` (function) — [saleor/graphql/csv/tests/queries/test_export_files.py:177]
- `test_sort_export_files_query_by_created_at_date` (function) — [saleor/graphql/csv/tests/queries/test_export_files.py:217]
- `test_sort_export_files_query_by_updated_at_date` (function) — [saleor/graphql/csv/tests/queries/test_export_files.py:248]
- `test_sort_export_files_query_by_status` (function) — [saleor/graphql/csv/tests/queries/test_export_files.py:282]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/csv/tests/__init__.py` (1 lines)
- `saleor/graphql/csv/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/csv/tests/mutations/test_export_gift_cards.py` (380 lines)
- `saleor/graphql/csv/tests/mutations/test_export_products.py` (903 lines)
- `saleor/graphql/csv/tests/mutations/test_export_voucher_codes.py` (386 lines)
- `saleor/graphql/csv/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/csv/tests/queries/test_export_file.py` (319 lines)
- `saleor/graphql/csv/tests/queries/test_export_files.py` (302 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....account.tests.fixtures.user.dangerously_create_test_user`
- `.....app.models.App`
- `.....attribute.models.Attribute`
- `.....channel.models.Channel`
- `.....core.JobStatus`
- `.....csv.ExportEvents`
- `.....csv.error_codes.ExportErrorCode`
- `.....csv.models.ExportEvent`
- `.....csv.models.ExportFile`
- `.....warehouse.models.Warehouse`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `....tests.utils.get_graphql_content_from_response`
- `...enums.ExportScope`
- `...enums.FileTypeEnum`
- `...enums.ProductFieldEnum`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `7e366ed2c5db` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
