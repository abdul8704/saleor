## Purpose

`saleor/graphql/page/tests/mutations` (`saleor/graphql/page/tests/mutations`) groups 14 source file(s) exposing 132 top-level declaration(s).

## Public surface

**`saleor/graphql/page/tests/mutations/test_page_attribute_assign.py`**

- `test_assign_attributes_to_page_type_by_staff` (function) — [saleor/graphql/page/tests/mutations/test_page_attribute_assign.py:34]
- `test_assign_attributes_to_page_type_by_app` (function) — [saleor/graphql/page/tests/mutations/test_page_attribute_assign.py:74]
- `test_assign_attributes_to_page_type_by_staff_no_perm` (function) — [saleor/graphql/page/tests/mutations/test_page_attribute_assign.py:114]
- `test_assign_attributes_to_page_type_by_app_no_perm` (function) — [saleor/graphql/page/tests/mutations/test_page_attribute_assign.py:137]
- `test_assign_attributes_to_page_type_invalid_object_type_as_page_type_id` (function) — [saleor/graphql/page/tests/mutations/test_page_attribute_assign.py:160]
- `test_assign_attributes_to_page_type_invalid_object_for_attributes` (function) — [saleor/graphql/page/tests/mutations/test_page_attribute_assign.py:193]
- `test_assign_attributes_to_page_type_not_page_attribute` (function) — [saleor/graphql/page/tests/mutations/test_page_attribute_assign.py:224]
- `test_assign_attributes_to_page_type_nonexistent_attribute` (function) — [saleor/graphql/page/tests/mutations/test_page_attribute_assign.py:265]
- `test_assign_attributes_to_page_type_nonexistent_and_valid_attribute` (function) — [saleor/graphql/page/tests/mutations/test_page_attribute_assign.py:301]
- `test_assign_attributes_to_page_type_attribute_already_assigned` (function) — [saleor/graphql/page/tests/mutations/test_page_attribute_assign.py:342]
- `test_assign_attributes_to_page_type_multiple_error_returned` (function) — [saleor/graphql/page/tests/mutations/test_page_attribute_assign.py:383]

**`saleor/graphql/page/tests/mutations/test_page_attribute_unassign.py`**

- `test_unassign_attributes_from_page_type_by_staff` (function) — [saleor/graphql/page/tests/mutations/test_page_attribute_unassign.py:29]
- `test_unassign_attributes_from_page_type_by_staff_no_perm` (function) — [saleor/graphql/page/tests/mutations/test_page_attribute_unassign.py:63]
- `test_unassign_attributes_from_page_type_by_app` (function) — [saleor/graphql/page/tests/mutations/test_page_attribute_unassign.py:82]
- `test_unassign_attributes_from_page_type_by_app_no_perm` (function) — [saleor/graphql/page/tests/mutations/test_page_attribute_unassign.py:116]

**`saleor/graphql/page/tests/mutations/test_page_bulk_delete.py`**

- `test_delete_pages` (function) — [saleor/graphql/page/tests/mutations/test_page_bulk_delete.py:24]
- `test_page_bulk_delete_with_file_attribute` (function) — [saleor/graphql/page/tests/mutations/test_page_bulk_delete.py:39]
- `test_page_delete_removes_reference_to_product` (function) — [saleor/graphql/page/tests/mutations/test_page_bulk_delete.py:77]
- `test_page_delete_removes_reference_to_product_variant` (function) — [saleor/graphql/page/tests/mutations/test_page_bulk_delete.py:117]
- `test_page_delete_removes_reference_to_page` (function) — [saleor/graphql/page/tests/mutations/test_page_bulk_delete.py:157]
- `test_bulk_delete_page_with_invalid_ids` (function) — [saleor/graphql/page/tests/mutations/test_page_bulk_delete.py:200]
- `test_page_bulk_delete_reference_attribute_sets_search_index_dirty_in_product` (function) — [saleor/graphql/page/tests/mutations/test_page_bulk_delete.py:218]

**`saleor/graphql/page/tests/mutations/test_page_bulk_publish.py`**

- `test_bulk_publish` (function) — [saleor/graphql/page/tests/mutations/test_page_bulk_publish.py:15]
- `test_bulk_unpublish` (function) — [saleor/graphql/page/tests/mutations/test_page_bulk_publish.py:33]

**`saleor/graphql/page/tests/mutations/test_page_create.py`**

- `test_page_create_mutation` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:144]
- `test_page_create_mutation_with_published_at_date` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:238]
- `test_page_create_trigger_page_webhook` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:316]
- `test_page_create_required_fields` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:371]
- `test_create_default_slug` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:388]
- `test_page_create_mutation_missing_required_attributes` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:407]
- `test_page_create_mutation_empty_attribute_value` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:458]
- `test_create_page_with_file_attribute` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:503]
- `test_create_page_with_file_attribute_new_attribute_value` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:588]
- `test_create_page_with_file_attribute_not_required_no_file_url_given` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:680]
- `test_create_page_with_file_attribute_required_no_file_url_given` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:735]
- `test_create_page_with_page_reference_attribute` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:781]
- `test_create_page_with_reference_attributes_and_reference_types_defined` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:864]
- `test_create_page_with_date_attribute` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:1002]
- `test_create_page_with_date_time_attribute` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:1068]
- `test_create_page_with_plain_text_attribute` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:1134]
- `test_create_page_with_page_reference_attribute_not_required_no_references_given` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:1200]
- `test_create_page_with_page_reference_attribute_required_no_references_given` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:1260]
- `test_create_page_with_reference_attributes_ref_not_in_available_choices` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:1315]
- `test_create_page_with_product_reference_attribute` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:1396]
- `test_create_page_with_product_reference_attribute_not_required_no_references_given` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:1479]
- `test_create_page_with_product_reference_attribute_required_no_references_given` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:1539]
- `test_create_page_with_variant_reference_attribute` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:1590]
- `test_create_page_with_category_reference_attribute` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:1673]
- `test_create_page_with_collection_reference_attribute` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:1755]
- `test_create_page_with_single_reference_attributes` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:1836]
- `test_page_create_mutation_with_numeric_attribue` (function) — [saleor/graphql/page/tests/mutations/test_page_create.py:1978]

**`saleor/graphql/page/tests/mutations/test_page_delete.py`**

- `test_page_delete_mutation` (function) — [saleor/graphql/page/tests/mutations/test_page_delete.py:32]
- `test_page_delete_trigger_webhook` (function) — [saleor/graphql/page/tests/mutations/test_page_delete.py:46]
- `test_page_delete_trigger_webhook_with_page_type` (function) — [saleor/graphql/page/tests/mutations/test_page_delete.py:82]
- `test_page_delete_with_file_attribute` (function) — [saleor/graphql/page/tests/mutations/test_page_delete.py:109]
- `test_page_delete_removes_reference_to_product` (function) — [saleor/graphql/page/tests/mutations/test_page_delete.py:140]
- `test_page_delete_removes_reference_to_product_variant` (function) — [saleor/graphql/page/tests/mutations/test_page_delete.py:180]
- `test_page_delete_removes_reference_to_page` (function) — [saleor/graphql/page/tests/mutations/test_page_delete.py:220]
- `test_page_delete_reference_attribute_sets_search_index_dirty_in_product` (function) — [saleor/graphql/page/tests/mutations/test_page_delete.py:263]

**`saleor/graphql/page/tests/mutations/test_page_reorder_attribute_values.py`**

- `test_sort_page_attribute_values` (function) — [saleor/graphql/page/tests/mutations/test_page_reorder_attribute_values.py:44]
- `test_sort_page_attribute_values_invalid_attribute_id` (function) — [saleor/graphql/page/tests/mutations/test_page_reorder_attribute_values.py:121]
- `test_sort_page_attribute_values_invalid_value_id` (function) — [saleor/graphql/page/tests/mutations/test_page_reorder_attribute_values.py:174]

**`saleor/graphql/page/tests/mutations/test_page_type_create.py`**

- `test_page_type_create_as_staff` (function) — [saleor/graphql/page/tests/mutations/test_page_type_create.py:39]
- `test_page_type_create_trigger_webhook` (function) — [saleor/graphql/page/tests/mutations/test_page_type_create.py:83]
- `test_page_type_create_as_staff_no_perm` (function) — [saleor/graphql/page/tests/mutations/test_page_type_create.py:145]
- `test_page_type_create_as_app` (function) — [saleor/graphql/page/tests/mutations/test_page_type_create.py:169]
- `test_page_type_create_as_app_no_perm` (function) — [saleor/graphql/page/tests/mutations/test_page_type_create.py:203]
- `test_page_type_create_unique_slug_generated` (function) — [saleor/graphql/page/tests/mutations/test_page_type_create.py:223]
- `test_page_type_create_duplicated_slug` (function) — [saleor/graphql/page/tests/mutations/test_page_type_create.py:270]
- `test_page_type_create_not_valid_attributes` (function) — [saleor/graphql/page/tests/mutations/test_page_type_create.py:313]

**`saleor/graphql/page/tests/mutations/test_page_type_delete.py`**

- `test_page_type_delete_by_staff` (function) — [saleor/graphql/page/tests/mutations/test_page_type_delete.py:36]
- `test_page_type_delete_trigger_webhook` (function) — [saleor/graphql/page/tests/mutations/test_page_type_delete.py:72]
- `test_page_type_delete_by_staff_no_perm` (function) — [saleor/graphql/page/tests/mutations/test_page_type_delete.py:124]
- `test_page_type_delete_by_app` (function) — [saleor/graphql/page/tests/mutations/test_page_type_delete.py:139]
- `test_page_type_delete_by_app_no_perm` (function) — [saleor/graphql/page/tests/mutations/test_page_type_delete.py:170]
- `test_page_type_delete_with_file_attributes` (function) — [saleor/graphql/page/tests/mutations/test_page_type_delete.py:185]
- `test_page_type_delete_sets_search_index_dirty_in_product_with_page_reference` (function) — [saleor/graphql/page/tests/mutations/test_page_type_delete.py:221]

**`saleor/graphql/page/tests/mutations/test_page_type_reorder_attributes.py`**

- `test_reorder_page_type_attributes_by_staff` (function) — [saleor/graphql/page/tests/mutations/test_page_type_reorder_attributes.py:34]
- `test_reorder_page_type_attributes_by_staff_no_perm` (function) — [saleor/graphql/page/tests/mutations/test_page_type_reorder_attributes.py:96]
- `test_reorder_page_type_attributes_by_app` (function) — [saleor/graphql/page/tests/mutations/test_page_type_reorder_attributes.py:133]
- `test_reorder_page_type_attributes_by_app_no_perm` (function) — [saleor/graphql/page/tests/mutations/test_page_type_reorder_attributes.py:193]
- `test_reorder_page_type_attributes_invalid_page_type` (function) — [saleor/graphql/page/tests/mutations/test_page_type_reorder_attributes.py:230]
- `test_reorder_page_type_attributes_invalid_attribute_id` (function) — [saleor/graphql/page/tests/mutations/test_page_type_reorder_attributes.py:267]

**`saleor/graphql/page/tests/mutations/test_page_type_update.py`**

- `test_page_type_update_as_staff` (function) — [saleor/graphql/page/tests/mutations/test_page_type_update.py:39]
- `test_page_type_update_trigger_webhook` (function) — [saleor/graphql/page/tests/mutations/test_page_type_update.py:94]
- `test_page_type_update_as_staff_no_perm` (function) — [saleor/graphql/page/tests/mutations/test_page_type_update.py:157]
- `test_page_type_update_as_app` (function) — [saleor/graphql/page/tests/mutations/test_page_type_update.py:171]
- `test_page_type_update_as_app_no_perm` (function) — [saleor/graphql/page/tests/mutations/test_page_type_update.py:223]
- `test_page_type_update_duplicated_attributes` (function) — [saleor/graphql/page/tests/mutations/test_page_type_update.py:237]
- `test_page_type_update_not_valid_attributes` (function) — [saleor/graphql/page/tests/mutations/test_page_type_update.py:277]
- `test_page_type_update_empty_slug` (function) — [saleor/graphql/page/tests/mutations/test_page_type_update.py:337]
- `test_page_type_update_duplicated_slug` (function) — [saleor/graphql/page/tests/mutations/test_page_type_update.py:364]
- `test_page_type_update_multiple_errors` (function) — [saleor/graphql/page/tests/mutations/test_page_type_update.py:394]
- `test_page_type_update_only_name` (function) — [saleor/graphql/page/tests/mutations/test_page_type_update.py:439]
- `test_page_type_update_only_add_attributes` (function) — [saleor/graphql/page/tests/mutations/test_page_type_update.py:475]
- `test_page_type_update_only_remove_attributes` (function) — [saleor/graphql/page/tests/mutations/test_page_type_update.py:521]

**`saleor/graphql/page/tests/mutations/test_page_types_bulk_delete.py`**

- `test_page_type_bulk_delete_by_staff` (function) — [saleor/graphql/page/tests/mutations/test_page_types_bulk_delete.py:26]
- `test_page_type_bulk_delete_trigger_webhooks` (function) — [saleor/graphql/page/tests/mutations/test_page_types_bulk_delete.py:62]
- `test_page_type_bulk_delete_by_staff_no_perm` (function) — [saleor/graphql/page/tests/mutations/test_page_types_bulk_delete.py:99]
- `test_page_type_bulk_delete_by_app` (function) — [saleor/graphql/page/tests/mutations/test_page_types_bulk_delete.py:117]
- `test_page_type_bulk_delete_by_app_no_perm` (function) — [saleor/graphql/page/tests/mutations/test_page_types_bulk_delete.py:149]
- `test_page_type_bulk_delete_with_file_attribute` (function) — [saleor/graphql/page/tests/mutations/test_page_types_bulk_delete.py:167]
- `test_page_type_bulk_delete_by_app_with_invalid_ids` (function) — [saleor/graphql/page/tests/mutations/test_page_types_bulk_delete.py:214]
- `test_page_type_bulk_delete_sets_search_index_dirty_in_product_with_page_reference` (function) — [saleor/graphql/page/tests/mutations/test_page_types_bulk_delete.py:240]

**`saleor/graphql/page/tests/mutations/test_page_update.py`**

- `test_update_page` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:145]
- `test_update_page_trigger_webhook` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:242]
- `test_update_page_only_title` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:297]
- `test_update_page_with_file_attribute_value` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:376]
- `test_update_page_with_file_attribute_new_value_is_not_created` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:441]
- `test_update_page_clear_file_attribute_values` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:504]
- `test_update_page_with_page_reference_attribute_new_value` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:559]
- `test_update_page_with_page_reference_attribute_existing_value` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:622]
- `test_update_page_with_plain_text_attribute_new_value` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:695]
- `test_update_page_with_reference_attributes_and_reference_types_defined` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:757]
- `test_update_page_with_plain_text_attribute_existing_value` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:895]
- `test_update_page_with_required_plain_text_attribute_empty_value` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:962]
- `test_update_page_with_product_reference_attribute_new_value` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:1009]
- `test_update_page_with_product_reference_attribute_existing_value` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:1071]
- `test_update_page_with_variant_reference_attribute_new_value` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:1144]
- `test_update_page_with_variant_reference_attribute_existing_value` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:1206]
- `test_update_page_with_category_reference_attribute_new_value` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:1279]
- `test_update_page_with_collection_reference_attribute_new_value` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:1339]
- `test_update_page_with_reference_attributes_ref_not_in_available_choices` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:1399]
- `test_public_page_sets_publication_date` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:1482]
- `test_update_page_publication_date` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:1509]
- `test_update_page_blank_slug_value` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:1548]
- `test_update_page_with_title_value_and_without_slug_value` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:1568]
- `test_update_page_change_attribute_values_ordering` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:1696]
- `test_paginate_pages` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:1808]
- `test_update_page_with_single_reference_attributes` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:1845]
- `test_update_page_with_numeric_attribute` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:1971]
- `test_page_update_reference_attribute_sets_search_index_dirty_in_product` (function) — [saleor/graphql/page/tests/mutations/test_page_update.py:2028]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/page/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/page/tests/mutations/test_page_attribute_assign.py` (437 lines)
- `saleor/graphql/page/tests/mutations/test_page_attribute_unassign.py` (130 lines)
- `saleor/graphql/page/tests/mutations/test_page_bulk_delete.py` (276 lines)
- `saleor/graphql/page/tests/mutations/test_page_bulk_publish.py` (46 lines)
- `saleor/graphql/page/tests/mutations/test_page_create.py` (2039 lines)
- `saleor/graphql/page/tests/mutations/test_page_delete.py` (321 lines)
- `saleor/graphql/page/tests/mutations/test_page_reorder_attribute_values.py` (238 lines)
- `saleor/graphql/page/tests/mutations/test_page_type_create.py` (353 lines)
- `saleor/graphql/page/tests/mutations/test_page_type_delete.py` (286 lines)
- `saleor/graphql/page/tests/mutations/test_page_type_reorder_attributes.py` (310 lines)
- `saleor/graphql/page/tests/mutations/test_page_type_update.py` (558 lines)
- `saleor/graphql/page/tests/mutations/test_page_types_bulk_delete.py` (313 lines)
- `saleor/graphql/page/tests/mutations/test_page_update.py` (2088 lines)

## Interactions

- Imports from: `saleor/core/utils`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....attribute.models.AttributeValue`
- `.....attribute.utils.associate_attribute_values_to_instance`
- `.....core.utils.json_serializer.CustomJsonEncoder`
- `.....page.error_codes.PageErrorCode`
- `.....page.models.Page`
- `.....page.models.PageType`
- `.....product.search.update_products_search_vector`
- `.....tests.utils.dummy_editorjs`
- `.....webhook.event_types.WebhookEventAsyncType`
- `.....webhook.payloads.generate_meta`
- `.....webhook.payloads.generate_requestor`
- `....core.utils.to_global_id_or_none`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `dcfc1732db0b` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
