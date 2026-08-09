## Purpose

`saleor/graphql/attribute/tests/mutations` (`saleor/graphql/attribute/tests/mutations`) groups 11 source file(s) exposing 180 top-level declaration(s).

## Public surface

**`saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py`**

- `test_attribute_bulk_create_with_base_data` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py:59]
- `test_attribute_bulk_create_trigger_webhook` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py:104]
- `test_attribute_bulk_create_without_permission` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py:148]
- `test_attribute_bulk_create_with_deprecated_field` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py:185]
- `test_attribute_bulk_create_with_file_input_type_and_invalid_settings` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py:223]
- `test_attribute_bulk_create_with_duplicated_external_ref` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py:280]
- `test_attribute_bulk_create_with_to_long_name` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py:332]
- `test_attribute_bulk_create_with_existing_external_ref` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py:371]
- `test_attribute_bulk_create_dropdown_with_values` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py:405]
- `test_attribute_bulk_create_with_duplicated_external_reference_in_values` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py:453]
- `test_attribute_bulk_create_with_existing_external_reference_in_values` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py:520]
- `test_attribute_bulk_create_dropdown_with_one_invalid_value_and_ignore_failed` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py:559]
- `test_attribute_bulk_create_dropdown_with_invalid_row_and_reject_failed_rows` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py:607]
- `test_attribute_bulk_create_with_reference_types` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py:664]
- `test_attribute_bulk_create_with_invalid_reference_types` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py:729]
- `test_attribute_type_without_mapped_permission_returns_error` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py:814]

**`saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py`**

- `test_attribute_bulk_update_with_base_data` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:62]
- `test_attribute_bulk_update_trigger_webhook` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:106]
- `test_attribute_bulk_update_without_permission` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:144]
- `test_attribute_bulk_update_with_deprecated_fields` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:172]
- `test_attribute_bulk_update_with_duplicated_external_ref` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:206]
- `test_attribute_bulk_update_with_existing_external_ref` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:254]
- `test_attribute_bulk_update_with_invalid_type_id` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:290]
- `test_attribute_bulk_update_without_id_and_external_ref` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:319]
- `test_attribute_bulk_update_with_id_and_external_ref` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:347]
- `test_attribute_bulk_update_removes_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:386]
- `test_attribute_bulk_update_removes_value_trigger_webhook` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:424]
- `test_attribute_bulk_update_removes_invalid_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:462]
- `test_attribute_bulk_update_removes_value_mark_product_search_index_dirty` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:510]
- `test_attribute_bulk_update_removes_value_mark_page_search_index_dirty` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:544]
- `test_attribute_bulk_update_add_new_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:578]
- `test_attribute_bulk_update_add_value_with_existing_name` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:636]
- `test_attribute_bulk_update_with_duplicated_external_reference_in_values` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:678]
- `test_attribute_bulk_update_add_value_with_to_long_name_and_reject_failed_rows` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:745]
- `test_attribute_bulk_update_add_value_with_to_long_name_and_ignore_failed` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:796]
- `test_attribute_bulk_update_add_value_with_existing_external_ref` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:844]
- `test_attribute_bulk_update_removes_value_with_invalid_id` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:889]
- `test_attribute_bulk_update_add_value_missing_name` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:923]
- `test_attribute_bulk_update_reference_types` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:968]
- `test_attribute_bulk_update_invalid_reference_types` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:1073]
- `test_attribute_type_without_mapped_permission_returns_error` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py:1158]

**`saleor/graphql/attribute/tests/mutations/test_attribute_create.py`**

- `test_create_attribute_and_attribute_values` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:77]
- `test_create_attribute_trigger_webhook` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:132]
- `test_create_numeric_attribute_and_attribute_values` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:194]
- `test_create_numeric_attribute_and_attribute_values_not_numeric_value_provided` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:235]
- `test_create_swatch_attribute_and_attribute_values_only_name_provided` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:279]
- `test_create_swatch_attribute_and_attribute_values_with_file` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:338]
- `test_create_swatch_attribute_and_attribute_values_with_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:405]
- `test_create_swatch_attribute_and_attribute_values_file_and_value_provided` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:467]
- `test_create_not_swatch_attribute_provide_not_valid_data` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:514]
- `test_create_attribute_with_file_input_type` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:558]
- `test_create_attribute_with_reference_input_type` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:614]
- `test_create_attribute_with_reference_input_type_entity_type_not_given` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:664]
- `test_create_attribute_with_single_reference_input_type` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:711]
- `test_create_attribute_with_single_reference_input_type_entity_type_not_given` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:763]
- `test_create_attribute_with_plain_text_input_type` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:801]
- `test_create_page_attribute_and_attribute_values` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:848]
- `test_create_attribute_with_file_input_type_and_values` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:901]
- `test_create_attribute_with_file_input_type_correct_attribute_settings` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:941]
- `test_create_attribute_with_file_input_type_and_invalid_settings` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:992]
- `test_create_attribute_with_reference_input_type_invalid_settings` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1043]
- `test_create_attribute_with_file_input_type_and_invalid_one_settings_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1101]
- `test_create_attribute_with_reference_input_type_invalid_one_settings_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1151]
- `test_create_attribute_with_reference_input_type_values_given` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1197]
- `test_create_attribute_with_given_slug` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1247]
- `test_create_attribute_value_name_and_slug_with_unicode` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1289]
- `test_create_attribute_and_attribute_values_errors` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1341]
- `test_create_attribute_with_non_unique_external_reference` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1380]
- `test_create_attribute_similar_names` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1419]
- `test_create_product_reference_attribute_with_reference_types` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1466]
- `test_create_variant_reference_attribute_with_reference_types` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1526]
- `test_create_page_reference_attribute_with_reference_types` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1589]
- `test_create_reference_attribute_with_reference_types_not_valid_entity_type` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1651]
- `test_create_attribute_with_reference_types_invalid_input_type` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1696]
- `test_create_attribute_with_reference_types_limit_exceeded` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1739]
- `test_create_attribute_with_reference_types_page_types_provided_for_variant_ref` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1784]
- `test_create_attribute_with_reference_types_product_types_provided_for_page_ref` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_create.py:1828]

**`saleor/graphql/attribute/tests/mutations/test_attribute_delete.py`**

- `test_delete_attribute` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_delete.py:32]
- `test_delete_attribute_trigger_webhook` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_delete.py:60]
- `test_delete_file_attribute` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_delete.py:111]
- `test_delete_attribute_update_search_index_dirty_in_product` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_delete.py:136]
- `test_delete_attribute_update_search_index_dirty_in_page` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_delete.py:158]
- `test_delete_attribute_by_external_reference` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_delete.py:197]
- `test_delete_attribute_by_both_id_and_external_reference` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_delete.py:226]
- `test_delete_attribute_by_external_reference_not_existing` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_delete.py:247]
- `test_delete_page_attribute_with_page_type_permission` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_delete.py:266]
- `test_delete_page_attribute_without_page_type_permission` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_delete.py:291]
- `test_delete_product_attribute_without_product_type_permission` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_delete.py:313]
- `test_attribute_type_without_mapped_permission_is_denied` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_delete.py:335]

**`saleor/graphql/attribute/tests/mutations/test_attribute_reorder_values.py`**

- `test_sort_values_within_attribute_invalid_product_type` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_reorder_values.py:38]
- `test_sort_values_within_attribute_invalid_id` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_reorder_values.py:67]
- `test_sort_values_within_attribute` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_reorder_values.py:97]
- `test_sort_values_trigger_webhook` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_reorder_values.py:156]
- `generate_attribute_value_update_call` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_reorder_values.py:226]
- `test_authorization` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_reorder_values.py:316]

**`saleor/graphql/attribute/tests/mutations/test_attribute_update.py`**

- `test_update_attribute` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:71]
- `test_update_attribute_trigger_webhook` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:113]
- `test_update_attribute_remove_and_add_values` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:168]
- `test_update_empty_attribute_and_add_values` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:203]
- `test_update_empty_attribute_and_add_values_name_not_given` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:235]
- `test_update_attribute_with_file_input_type` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:266]
- `test_update_attribute_with_numeric_input_type` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:295]
- `test_update_attribute_with_file_input_type_and_values` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:328]
- `test_update_attribute_with_file_input_type_invalid_settings` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:365]
- `test_update_attribute_provide_existing_value_name` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:410]
- `test_update_attribute_slug` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:464]
- `test_update_attribute_slug_exists` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:504]
- `test_update_attribute_slug_and_name` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:555]
- `test_update_attribute_and_add_attribute_values_errors` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:638]
- `test_update_attribute_and_remove_others_attribute_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:674]
- `test_update_attribute_by_external_reference` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:728]
- `test_update_attribute_by_both_id_and_external_reference` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:761]
- `test_update_attribute_by_external_reference_not_existing` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:783]
- `test_update_attribute_with_non_unique_external_reference` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:807]
- `test_update_attribute_name_similar_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:840]
- `test_update_attribute_reference_types` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:879]
- `test_update_attribute_clear_reference_types` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:916]
- `test_update_reference_attribute_with_reference_types_not_valid_entity_type` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:957]
- `test_update_attribute_with_reference_types_invalid_input_type` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:997]
- `test_update_attribute_with_reference_types_limit_exceeded` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:1037]
- `test_update_attribute_with_reference_types_page_types_provided_for_variant_ref` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:1078]
- `test_update_attribute_with_reference_types_product_types_provided_for_page_ref` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:1116]
- `test_update_attribute_remove_value_marks_product_search_index_dirty` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:1151]
- `test_update_attribute_add_value_does_not_mark_product_search_index_dirty` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:1185]
- `test_update_attribute_remove_value_marks_page_search_index_dirty` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:1216]
- `test_update_attribute_add_value_does_not_mark_page_search_index_dirty` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:1251]
- `test_update_page_attribute_with_page_type_permission` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:1283]
- `test_update_page_attribute_without_page_type_permission` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:1308]
- `test_update_product_attribute_without_product_type_permission` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_update.py:1330]

**`saleor/graphql/attribute/tests/mutations/test_attribute_value_create.py`**

- `test_validate_value_is_unique` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_create.py:20]
- `test_create_attribute_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_create.py:75]
- `test_create_attribute_value_trigger_webhooks` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_create.py:112]
- `test_create_attribute_value_with_the_same_name_as_different_attribute_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_create.py:187]
- `test_create_swatch_attribute_value_with_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_create.py:221]
- `test_create_swatch_attribute_value_with_file` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_create.py:253]
- `test_create_swatch_attribute_value_with_value_and_file` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_create.py:291]
- `test_create_attribute_value_provide_not_allowed_input_data` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_create.py:333]
- `test_create_attribute_value_not_unique_name` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_create.py:362]
- `test_create_attribute_value_capitalized_name` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_create.py:384]
- `test_create_attribute_value_with_non_unique_external_reference` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_create.py:406]
- `test_authorization` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_create.py:507]

**`saleor/graphql/attribute/tests/mutations/test_attribute_value_delete.py`**

- `test_delete_attribute_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_delete.py:31]
- `test_delete_attribute_value_update_search_index_dirty_in_product` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_delete.py:53]
- `test_delete_attribute_value_update_search_index_dirty_in_page` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_delete.py:75]
- `test_delete_attribute_value_trigger_webhooks` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_delete.py:100]
- `test_delete_file_attribute_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_delete.py:172]
- `test_delete_attribute_value_product_search_document_updated` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_delete.py:193]
- `test_delete_attribute_value_product_search_document_updated_variant_attribute` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_delete.py:223]
- `test_delete_attribute_value_by_external_reference` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_delete.py:270]
- `test_delete_attribute_value_by_both_id_and_external_reference` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_delete.py:300]
- `test_delete_attribute_value_by_external_reference_not_existing` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_delete.py:323]
- `test_authorization` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_delete.py:404]

**`saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py`**

- `test_update_attribute_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:53]
- `test_update_attribute_value_update_search_index_dirty_in_product` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:93]
- `test_update_attribute_value_update_search_index_dirty_in_page` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:118]
- `test_update_attribute_value_trigger_webhooks` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:145]
- `test_update_attribute_value_name_not_unique` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:222]
- `test_update_attribute_value_the_same_name_as_different_attribute_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:247]
- `test_update_attribute_value_product_search_document_updated` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:279]
- `test_update_attribute_value_product_search_document_updated_variant_attribute` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:315]
- `test_update_swatch_attribute_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:352]
- `test_update_swatch_attribute_value_clear_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:383]
- `test_update_swatch_attribute_value_clear_file_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:415]
- `test_update_attribute_value_invalid_input_data` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:453]
- `test_update_attribute_value_swatch_attr_value` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:482]
- `test_update_attribute_value_by_external_reference` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:530]
- `test_update_attribute_value_by_both_id_and_external_reference` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:565]
- `test_update_attribute_value_by_external_reference_not_existing` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:589]
- `test_update_attribute_value_with_non_unique_external_reference` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:615]
- `test_authorization` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:711]
- `test_invalid_id_returns_error` (function) — [saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py:743]

**`saleor/graphql/attribute/tests/mutations/test_bulk_delete.py`**

- `attribute_value_list` (function) — [saleor/graphql/attribute/tests/mutations/test_bulk_delete.py:20]
- `test_delete_attributes` (function) — [saleor/graphql/attribute/tests/mutations/test_bulk_delete.py:33]
- `test_delete_attributes_trigger_webhooks` (function) — [saleor/graphql/attribute/tests/mutations/test_bulk_delete.py:59]
- `test_delete_attributes_products_search_document_updated` (function) — [saleor/graphql/attribute/tests/mutations/test_bulk_delete.py:91]
- `test_delete_attribute_values` (function) — [saleor/graphql/attribute/tests/mutations/test_bulk_delete.py:159]
- `test_delete_attribute_values_trigger_webhook` (function) — [saleor/graphql/attribute/tests/mutations/test_bulk_delete.py:185]
- `test_delete_attribute_values_search_document_updated` (function) — [saleor/graphql/attribute/tests/mutations/test_bulk_delete.py:220]
- `test_delete_attributes_authorization` (function) — [saleor/graphql/attribute/tests/mutations/test_bulk_delete.py:368]
- `test_delete_attribute_values_authorization` (function) — [saleor/graphql/attribute/tests/mutations/test_bulk_delete.py:494]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/attribute/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/attribute/tests/mutations/test_attribute_bulk_create.py` (855 lines)
- `saleor/graphql/attribute/tests/mutations/test_attribute_bulk_update.py` (1200 lines)
- `saleor/graphql/attribute/tests/mutations/test_attribute_create.py` (1866 lines)
- `saleor/graphql/attribute/tests/mutations/test_attribute_delete.py` (361 lines)
- `saleor/graphql/attribute/tests/mutations/test_attribute_reorder_values.py` (350 lines)
- `saleor/graphql/attribute/tests/mutations/test_attribute_update.py` (1347 lines)
- `saleor/graphql/attribute/tests/mutations/test_attribute_value_create.py` (534 lines)
- `saleor/graphql/attribute/tests/mutations/test_attribute_value_delete.py` (426 lines)
- `saleor/graphql/attribute/tests/mutations/test_attribute_value_update.py` (765 lines)
- `saleor/graphql/attribute/tests/mutations/test_bulk_delete.py` (525 lines)

## Interactions

- Imports from: `saleor/core/utils`, `saleor/graphql/attribute/mutations`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....attribute.AttributeEntityType`
- `.....attribute.AttributeInputType`
- `.....attribute.error_codes.AttributeBulkCreateErrorCode`
- `.....attribute.error_codes.AttributeBulkUpdateErrorCode`
- `.....attribute.error_codes.AttributeErrorCode`
- `.....attribute.models.Attribute`
- `.....attribute.models.AttributeValue`
- `.....attribute.utils.associate_attribute_values_to_instance`
- `.....core.utils.json_serializer.CustomJsonEncoder`
- `.....webhook.event_types.WebhookEventAsyncType`
- `.....webhook.payloads.generate_meta`
- `.....webhook.payloads.generate_requestor`
- `....core.enums.ErrorPolicyEnum`
- `....core.enums.MeasurementUnitsEnum`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `...enums.AttributeEntityTypeEnum`
- `...enums.AttributeInputTypeEnum`
- `...enums.AttributeTypeEnum`
- `...mutations.validators.validate_value_is_unique`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `46c65981e4f4` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
