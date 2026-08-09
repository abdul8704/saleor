## Purpose

`saleor/csv/tests` (`saleor/csv/tests`) groups 10 source file(s) exposing 115 top-level declaration(s).

## Public surface

**`saleor/csv/tests/export/products_data/test_get_products_data.py`**

- `test_get_products_data` (function) — [saleor/csv/tests/export/products_data/test_get_products_data.py:24]
- `test_get_products_data_for_specified_attributes` (function) — [saleor/csv/tests/export/products_data/test_get_products_data.py:138]
- `test_get_products_data_for_specified_warehouses` (function) — [saleor/csv/tests/export/products_data/test_get_products_data.py:176]
- `test_get_products_data_for_product_without_channel` (function) — [saleor/csv/tests/export/products_data/test_get_products_data.py:210]
- `test_get_products_data_for_specified_warehouses_channels_and_attributes` (function) — [saleor/csv/tests/export/products_data/test_get_products_data.py:246]

**`saleor/csv/tests/export/products_data/test_handle_relations_data.py`**

- `test_get_products_relations_data` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:35]
- `test_get_products_relations_data_no_relations_fields` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:64]
- `test_get_products_relations_data_attribute_ids` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:81]
- `test_get_products_relations_data_channel_ids` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:159]
- `test_prepare_products_relations_data` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:180]
- `test_prepare_products_relations_data_ignores_unassigned_attribute_values` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:249]
- `test_prepare_products_relations_data_only_fields` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:277]
- `test_prepare_products_relations_data_only_attributes_ids` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:301]
- `test_prepare_products_relations_data_only_channel_ids` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:328]
- `test_prepare_products_relations_data_sets_published_dates` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:357]
- `test_get_variants_relations_data` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:405]
- `test_get_variants_relations_data_no_relations_fields` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:437]
- `test_get_variants_relations_data_attribute_ids` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:457]
- `test_get_variants_relations_data_warehouse_ids` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:519]
- `test_get_variants_relations_data_channel_ids` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:544]
- `test_get_variants_relations_data_attributes_warehouses_and_channels_ids` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:569]
- `test_prepare_variants_relations_data` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:593]
- `test_prepare_variants_relations_data_only_fields` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:682]
- `test_prepare_variants_relations_data_attributes_ids` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:716]
- `test_prepare_variants_relations_data_warehouse_ids` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:748]
- `test_prepare_variants_relations_data_channel_ids` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:776]
- `test_add_collection_info_to_data` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:803]
- `test_add_collection_info_to_data_update_collections` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:816]
- `test_add_collection_info_to_data_no_collection` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:830]
- `test_add_image_uris_to_data` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:843]
- `test_add_image_uris_to_data_update_images` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:857]
- `test_add_image_uris_to_data_no_image_path` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:872]
- `test_add_attribute_info_to_data` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:885]
- `test_add_attribute_info_to_data_update_attribute_data` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:918]
- `test_add_attribute_info_to_data_no_slug` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:951]
- `test_add_attribute_info_when_no_value` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:980]
- `test_add_file_attribute_info_to_data` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:1011]
- `test_add_rich_text_attribute_info_to_data` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:1043]
- `test_add_boolean_attribute_info_to_data` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:1074]
- `test_add_reference_attribute_info_to_data` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:1105]
- `test_add_reference_info_to_data_update_attribute_data` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:1137]
- `test_add_date_time_attribute_info_to_data` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:1172]
- `test_add_date_attribute_info_to_data` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:1203]
- `test_add_numeric_attribute_info_to_data` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:1234]
- `test_add_numeric_attribute_info_to_data_no_unit` (function) — [saleor/csv/tests/export/products_data/test_handle_relations_data.py:1266]
- _…and 12 more in this file_

**`saleor/csv/tests/export/products_data/test_prepare_headers.py`**

- `test_get_export_fields_and_headers_fields_without_price` (function) — [saleor/csv/tests/export/products_data/test_prepare_headers.py:13]
- `test_get_export_fields_and_headers_no_fields` (function) — [saleor/csv/tests/export/products_data/test_prepare_headers.py:39]
- `test_get_attributes_headers` (function) — [saleor/csv/tests/export/products_data/test_prepare_headers.py:46]
- `test_get_attributes_headers_lack_of_attributes_ids` (function) — [saleor/csv/tests/export/products_data/test_prepare_headers.py:80]
- `test_get_warehouses_headers` (function) — [saleor/csv/tests/export/products_data/test_prepare_headers.py:91]
- `test_get_warehouses_headers_lack_of_warehouse_ids` (function) — [saleor/csv/tests/export/products_data/test_prepare_headers.py:103]
- `test_get_channels_headers` (function) — [saleor/csv/tests/export/products_data/test_prepare_headers.py:114]
- `test_get_channels_headers_lack_of_channel_ids` (function) — [saleor/csv/tests/export/products_data/test_prepare_headers.py:144]
- `test_get_product_export_fields_and_headers_info` (function) — [saleor/csv/tests/export/products_data/test_prepare_headers.py:155]

**`saleor/csv/tests/export/products_data/utils.py`**

- `add_product_attribute_data_to_expected_data` (function) — [saleor/csv/tests/export/products_data/utils.py:15]
- `add_variant_attribute_data_to_expected_data` (function) — [saleor/csv/tests/export/products_data/utils.py:48]
- `get_attribute_value` (function) — [saleor/csv/tests/export/products_data/utils.py:63]
- `add_stocks_to_expected_data` (function) — [saleor/csv/tests/export/products_data/utils.py:92]
- `add_channel_to_expected_product_data` (function) — [saleor/csv/tests/export/products_data/utils.py:107]
- `add_channel_to_expected_variant_data` (function) — [saleor/csv/tests/export/products_data/utils.py:132]

**`saleor/csv/tests/export/test_export.py`**

- `test_export_products` (function) — [saleor/csv/tests/export/test_export.py:47]
- `test_export_products_ids` (function) — [saleor/csv/tests/export/test_export.py:105]
- `test_export_products_filter_is_published` (function) — [saleor/csv/tests/export/test_export.py:152]
- `test_export_products_filter_collections` (function) — [saleor/csv/tests/export/test_export.py:209]
- `test_export_products_by_app` (function) — [saleor/csv/tests/export/test_export.py:258]
- `test_export_products_webhook` (function) — [saleor/csv/tests/export/test_export.py:306]
- `test_export_gift_cards` (function) — [saleor/csv/tests/export/test_export.py:326]
- `test_export_gift_cards_by_app` (function) — [saleor/csv/tests/export/test_export.py:369]
- `test_export_gift_cards_ids` (function) — [saleor/csv/tests/export/test_export.py:411]
- `test_export_gift_cards_with_filter` (function) — [saleor/csv/tests/export/test_export.py:452]
- `test_export_gift_cards_webhook` (function) — [saleor/csv/tests/export/test_export.py:506]
- `test_get_filename_csv` (function) — [saleor/csv/tests/export/test_export.py:524]
- `test_get_filename_xlsx` (function) — [saleor/csv/tests/export/test_export.py:532]
- `test_get_product_queryset_all` (function) — [saleor/csv/tests/export/test_export.py:540]
- `test_get_product_queryset_ids` (function) — [saleor/csv/tests/export/test_export.py:546]
- `get_product_queryset_filter` (function) — [saleor/csv/tests/export/test_export.py:553]
- `test_get_product_queryset_filter_stock_availability` (function) — [saleor/csv/tests/export/test_export.py:563]
- `test_create_file_with_headers_csv` (function) — [saleor/csv/tests/export/test_export.py:592]
- `test_create_file_with_headers_xlsx` (function) — [saleor/csv/tests/export/test_export.py:611]
- `test_save_csv_file_in_export_file` (function) — [saleor/csv/tests/export/test_export.py:634]
- `test_append_to_file_for_csv` (function) — [saleor/csv/tests/export/test_export.py:649]
- `test_append_to_file_for_xlsx` (function) — [saleor/csv/tests/export/test_export.py:678]
- `test_export_products_in_batches_for_csv` (function) — [saleor/csv/tests/export/test_export.py:717]
- `test_export_products_in_batches_for_xlsx` (function) — [saleor/csv/tests/export/test_export.py:779]
- `test_export_gift_cards_in_batches_to_csv` (function) — [saleor/csv/tests/export/test_export.py:858]
- `test_export_gift_cards_in_batches_to_xlsx` (function) — [saleor/csv/tests/export/test_export.py:893]
- `test_parse_input` (function) — [saleor/csv/tests/export/test_export.py:936]
- `test_export_voucher_codes_by_voucher_id` (function) — [saleor/csv/tests/export/test_export.py:979]
- `test_export_voucher_codes_by_ids` (function) — [saleor/csv/tests/export/test_export.py:1020]
- `test_export_voucher_codes_by_app` (function) — [saleor/csv/tests/export/test_export.py:1062]
- `test_export_voucher_codes_webhooks` (function) — [saleor/csv/tests/export/test_export.py:1099]
- `test_export_voucher_codes_in_batches_to_csv` (function) — [saleor/csv/tests/export/test_export.py:1116]
- `test_export_voucher_codes_in_batches_to_xlsx` (function) — [saleor/csv/tests/export/test_export.py:1149]

**`saleor/csv/tests/test_notifications.py`**

- `test_send_export_download_link_notification` (function) — [saleor/csv/tests/test_notifications.py:17]
- `test_send_export_failed_info` (function) — [saleor/csv/tests/test_notifications.py:62]

**`saleor/csv/tests/test_tasks.py`**

- `test_export_products_task` (function) — [saleor/csv/tests/test_tasks.py:21]
- `test_export_products_task_failed` (function) — [saleor/csv/tests/test_tasks.py:39]
- `test_export_gift_cards_task` (function) — [saleor/csv/tests/test_tasks.py:61]
- `test_export_gift_cards_task_failed` (function) — [saleor/csv/tests/test_tasks.py:78]
- `test_on_task_failure` (function) — [saleor/csv/tests/test_tasks.py:97]
- `test_on_task_failure_for_app` (function) — [saleor/csv/tests/test_tasks.py:137]
- `test_on_task_success` (function) — [saleor/csv/tests/test_tasks.py:176]
- `test_delete_old_export_files` (function) — [saleor/csv/tests/test_tasks.py:207]

## How it works

The module's files, as provided to this run:

- `saleor/csv/tests/__init__.py` (1 lines)
- `saleor/csv/tests/export/__init__.py` (1 lines)
- `saleor/csv/tests/export/products_data/__init__.py` (1 lines)
- `saleor/csv/tests/export/products_data/test_get_products_data.py` (524 lines)
- `saleor/csv/tests/export/products_data/test_handle_relations_data.py` (1606 lines)
- `saleor/csv/tests/export/products_data/test_prepare_headers.py` (232 lines)
- `saleor/csv/tests/export/products_data/utils.py` (156 lines)
- `saleor/csv/tests/export/test_export.py` (1187 lines)
- `saleor/csv/tests/test_notifications.py` (99 lines)
- `saleor/csv/tests/test_tasks.py` (305 lines)

## Interactions

- Imports from: `saleor/csv`, `saleor/graphql/product/types`, `saleor/core/db`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....attribute.AttributeInputType`
- `.....attribute.models.Attribute`
- `.....attribute.models.AttributeValue`
- `.....attribute.tests.model_helpers.get_product_attributes`
- `.....attribute.utils.associate_attribute_values_to_instance`
- `.....channel.models.Channel`
- `.....core.editorjs.editorjs_to_text`
- `.....graphql.csv.enums.ProductFieldEnum`
- `.....product.models.Product`
- `.....product.models.ProductMedia`
- `.....product.models.ProductVariant`
- `.....product.models.VariantMedia`
- `.....tests.utils.dummy_editorjs`
- `.....warehouse.models.Warehouse`
- `....FileTypes`
- `....core.JobStatus`
- `....discount.models.VoucherCode`
- `....giftcard.models.GiftCard`
- `....graphql.csv.enums.ProductFieldEnum`
- `....graphql.product.enums.StockAvailability`
- `....graphql.product.filters.product.ProductFilter`
- `....product.models.Product`
- `....product.models.ProductChannelListing`
- `....utils.ProductExportFields`
- `....utils.products_data.get_products_data`
- `....warehouse.models.Allocation`
- `...ExportEvents`
- `...FileTypes`
- `...core.JobStatus`
- `...core.notification.utils.get_site_context`
- `...core.notify.AdminNotifyEvent`
- `...core.utils.build_absolute_uri`
- `...notifications`
- `..models.ExportEvent`
- `..models.ExportFile`
- `..notifications.get_default_export_payload`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `42ce9fd1d6af` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
