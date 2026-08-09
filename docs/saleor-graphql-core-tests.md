## Purpose

`saleor/graphql/core/tests` (`saleor/graphql/core/tests`) groups 24 source file(s) exposing 263 top-level declaration(s).

## Public surface

**`saleor/graphql/core/tests/__init__.py`**

- `ErrorCodeTest` (class) — [saleor/graphql/core/tests/__init__.py:8]
- `ErrorTest` (class) — [saleor/graphql/core/tests/__init__.py:15]

**`saleor/graphql/core/tests/test_base_mutation.py`**

- `Mutation` (class) — [saleor/graphql/core/tests/test_base_mutation.py:19]
- `Arguments` (class) — [saleor/graphql/core/tests/test_base_mutation.py:22]
- `Meta` (class) — [saleor/graphql/core/tests/test_base_mutation.py:26]
- `perform_mutation` (function) — [saleor/graphql/core/tests/test_base_mutation.py:31]
- `MutationWithCustomErrors` (class) — [saleor/graphql/core/tests/test_base_mutation.py:41]
- `Meta` (class) — [saleor/graphql/core/tests/test_base_mutation.py:42]
- `RestrictedMutation` (class) — [saleor/graphql/core/tests/test_base_mutation.py:48]
- `Meta` (class) — [saleor/graphql/core/tests/test_base_mutation.py:55]
- `OrderMutation` (class) — [saleor/graphql/core/tests/test_base_mutation.py:61]
- `Arguments` (class) — [saleor/graphql/core/tests/test_base_mutation.py:64]
- `Meta` (class) — [saleor/graphql/core/tests/test_base_mutation.py:68]
- `perform_mutation` (function) — [saleor/graphql/core/tests/test_base_mutation.py:73]
- `Mutations` (class) — [saleor/graphql/core/tests/test_base_mutation.py:81]
- `test_mutation_without_description_raises_error` (function) — [saleor/graphql/core/tests/test_base_mutation.py:94]
- `MutationNoDescription` (class) — [saleor/graphql/core/tests/test_base_mutation.py:97]
- `Arguments` (class) — [saleor/graphql/core/tests/test_base_mutation.py:100]
- `test_mutation_without_error_type_class_raises_error` (function) — [saleor/graphql/core/tests/test_base_mutation.py:104]
- `MutationNoDescription` (class) — [saleor/graphql/core/tests/test_base_mutation.py:107]
- `Arguments` (class) — [saleor/graphql/core/tests/test_base_mutation.py:111]
- `test_resolve_id` (function) — [saleor/graphql/core/tests/test_base_mutation.py:128]
- `test_user_error_nonexistent_id` (function) — [saleor/graphql/core/tests/test_base_mutation.py:138]
- `test_order_mutation_resolve_uuid_id` (function) — [saleor/graphql/core/tests/test_base_mutation.py:163]
- `test_order_mutation_for_old_int_id` (function) — [saleor/graphql/core/tests/test_base_mutation.py:173]
- `test_mutation_custom_errors_default_value` (function) — [saleor/graphql/core/tests/test_base_mutation.py:186]
- `test_user_error_id_of_different_type` (function) — [saleor/graphql/core/tests/test_base_mutation.py:209]
- `test_get_node_or_error_returns_null_for_empty_id` (function) — [saleor/graphql/core/tests/test_base_mutation.py:230]
- `test_base_mutation_get_node_by_pk_with_order_qs_and_old_int_id` (function) — [saleor/graphql/core/tests/test_base_mutation.py:236]
- `test_base_mutation_get_node_by_pk_with_order_qs_and_new_uuid_id` (function) — [saleor/graphql/core/tests/test_base_mutation.py:250]
- `test_base_mutation_get_node_by_pk_with_order_qs_and_int_id_use_old_id_set_to_false` (function) — [saleor/graphql/core/tests/test_base_mutation.py:260]
- `test_base_mutation_get_node_by_pk_with_qs_for_product` (function) — [saleor/graphql/core/tests/test_base_mutation.py:276]
- `test_expired_token_error` (function) — [saleor/graphql/core/tests/test_base_mutation.py:286]

**`saleor/graphql/core/tests/test_context.py`**

- `test_app_middleware_accepts_app_requests` (function) — [saleor/graphql/core/tests/test_context.py:7]
- `test_app_middleware_accepts_saleors_header` (function) — [saleor/graphql/core/tests/test_context.py:21]
- `test_app_middleware_skips_when_token_length_is_different_than_30` (function) — [saleor/graphql/core/tests/test_context.py:34]
- `test_saleor_context_init_dataloaders` (function) — [saleor/graphql/core/tests/test_context.py:48]

**`saleor/graphql/core/tests/test_converters.py`**

- `mockfield` (function) — [saleor/graphql/core/tests/test_converters.py:11]
- `Field` (class) — [saleor/graphql/core/tests/test_converters.py:12]
- `test_get_form_field_description_empty_help_text` (function) — [saleor/graphql/core/tests/test_converters.py:18]
- `test_get_form_field_description_nonempty_help_text` (function) — [saleor/graphql/core/tests/test_converters.py:29]
- `test_get_form_field_description_empty_extra_help_text` (function) — [saleor/graphql/core/tests/test_converters.py:40]
- `test_get_form_field_description_nonempty_extra_help_text` (function) — [saleor/graphql/core/tests/test_converters.py:51]
- `test_conversion` (function) — [saleor/graphql/core/tests/test_converters.py:80]

**`saleor/graphql/core/tests/test_core_reordering.py`**

- `dummy_attribute` (function) — [saleor/graphql/core/tests/test_core_reordering.py:20]
- `sorted_entries_seq` (function) — [saleor/graphql/core/tests/test_core_reordering.py:25]
- `sorted_entries_gaps` (function) — [saleor/graphql/core/tests/test_core_reordering.py:39]
- `test_reordering_sequential` (function) — [saleor/graphql/core/tests/test_core_reordering.py:52]
- `test_reordering_non_sequential` (function) — [saleor/graphql/core/tests/test_core_reordering.py:75]
- `test_inserting_at_the_edges` (function) — [saleor/graphql/core/tests/test_core_reordering.py:102]
- `test_reordering_out_of_bound` (function) — [saleor/graphql/core/tests/test_core_reordering.py:124]
- `test_reordering_null_sort_orders` (function) — [saleor/graphql/core/tests/test_core_reordering.py:147]
- `test_reordering_nothing` (function) — [saleor/graphql/core/tests/test_core_reordering.py:187]
- `test_giving_no_operation_does_no_query` (function) — [saleor/graphql/core/tests/test_core_reordering.py:198]
- `test_reordering_concurrently` (function) — [saleor/graphql/core/tests/test_core_reordering.py:207]
- `test_reordering_deleted_node_from_concurrent_update` (function) — [saleor/graphql/core/tests/test_core_reordering.py:245]

**`saleor/graphql/core/tests/test_core.py`**

- `test_user_error_field_name_for_related_object` (function) — [saleor/graphql/core/tests/test_core.py:34]
- `test_snake_to_camel_case` (function) — [saleor/graphql/core/tests/test_core.py:60]
- `test_reporting_period_to_date` (function) — [saleor/graphql/core/tests/test_core.py:66]
- `test_require_pagination` (function) — [saleor/graphql/core/tests/test_core.py:84]
- `test_total_count_query` (function) — [saleor/graphql/core/tests/test_core.py:105]
- `test_filter_input` (function) — [saleor/graphql/core/tests/test_core.py:118]
- `CreatedEnum` (class) — [saleor/graphql/core/tests/test_core.py:119]
- `TestProductFilter` (class) — [saleor/graphql/core/tests/test_core.py:123]
- `Meta` (class) — [saleor/graphql/core/tests/test_core.py:127]
- `created_filter` (function) — [saleor/graphql/core/tests/test_core.py:131]
- `TestFilter` (class) — [saleor/graphql/core/tests/test_core.py:138]
- `Meta` (class) — [saleor/graphql/core/tests/test_core.py:139]
- `PermissionEnumForTests` (class) — [saleor/graphql/core/tests/test_core.py:161]
- `test_mutation_invalid_permission_in_meta` (function) — [saleor/graphql/core/tests/test_core.py:175]
- `test_filter_range_field` (function) — [saleor/graphql/core/tests/test_core.py:200]
- `test_filter_products_with_zero_discount` (function) — [saleor/graphql/core/tests/test_core.py:211]
- `test_get_duplicated_values` (function) — [saleor/graphql/core/tests/test_core.py:223]
- `test_requestor_is_superuser_for_staff_user` (function) — [saleor/graphql/core/tests/test_core.py:231]
- `test_requestor_is_superuser_for_superuser` (function) — [saleor/graphql/core/tests/test_core.py:236]
- `test_requestor_is_superuser_for_app` (function) — [saleor/graphql/core/tests/test_core.py:241]
- `test_get_oembed_data` (function) — [saleor/graphql/core/tests/test_core.py:272]
- `test_get_oembed_data_unsupported_media_provider` (function) — [saleor/graphql/core/tests/test_core.py:290]
- `test_add_hash_to_file_name` (function) — [saleor/graphql/core/tests/test_core.py:299]
- `test_short_file_name_is_not_trimmed` (function) — [saleor/graphql/core/tests/test_core.py:310]
- `test_long_file_name_is_trimmed` (function) — [saleor/graphql/core/tests/test_core.py:324]
- `test_external_reference_to_global_id` (function) — [saleor/graphql/core/tests/test_core.py:339]
- `test_external_reference_to_global_id_non_existing` (function) — [saleor/graphql/core/tests/test_core.py:350]
- `test_get_instance_by_both_id_and_external_reference` (function) — [saleor/graphql/core/tests/test_core.py:363]

**`saleor/graphql/core/tests/test_deprecated_field_monitoring.py`**

- `test_deprecated_field_query_triggers_monitoring` (function) — [saleor/graphql/core/tests/test_deprecated_field_monitoring.py:133]
- `test_non_deprecated_field_query_does_not_trigger_monitoring` (function) — [saleor/graphql/core/tests/test_deprecated_field_monitoring.py:150]
- `test_deprecated_field_mutation_triggers_monitoring` (function) — [saleor/graphql/core/tests/test_deprecated_field_monitoring.py:167]
- `test_non_deprecated_field_mutation_does_not_trigger_monitoring` (function) — [saleor/graphql/core/tests/test_deprecated_field_monitoring.py:184]
- `test_deprecated_field_subscription_payload_triggers_monitoring` (function) — [saleor/graphql/core/tests/test_deprecated_field_monitoring.py:203]
- `test_deprecated_field_subscription_promise_payload_triggers_monitoring` (function) — [saleor/graphql/core/tests/test_deprecated_field_monitoring.py:226]
- `test_non_deprecated_field_subscription_payload_does_not_trigger_monitoring` (function) — [saleor/graphql/core/tests/test_deprecated_field_monitoring.py:250]
- `test_monitor_usage_field_subscription_payload_triggers_monitoring` (function) — [saleor/graphql/core/tests/test_deprecated_field_monitoring.py:273]

**`saleor/graphql/core/tests/test_federation.py`**

- `user_representation_by_id` (function) — [saleor/graphql/core/tests/test_federation.py:8]
- `user_representation_by_email` (function) — [saleor/graphql/core/tests/test_federation.py:14]
- `test_get_user_data_through_federated_query_by_id` (function) — [saleor/graphql/core/tests/test_federation.py:31]
- `test_get_user_data_through_federated_query_by_email` (function) — [saleor/graphql/core/tests/test_federation.py:41]

**`saleor/graphql/core/tests/test_file_upload.py`**

- `test_file_upload_by_staff` (function) — [saleor/graphql/core/tests/test_file_upload.py:33]
- `test_file_upload_by_customer` (function) — [saleor/graphql/core/tests/test_file_upload.py:63]
- `test_file_upload_by_app` (function) — [saleor/graphql/core/tests/test_file_upload.py:80]
- `test_file_upload_by_superuser` (function) — [saleor/graphql/core/tests/test_file_upload.py:108]
- `test_file_upload_file_with_the_same_name_already_exists` (function) — [saleor/graphql/core/tests/test_file_upload.py:136]
- `test_file_upload_file_name_with_space` (function) — [saleor/graphql/core/tests/test_file_upload.py:171]
- `test_file_upload_file_name_with_encoded_value` (function) — [saleor/graphql/core/tests/test_file_upload.py:202]
- `test_file_upload_invalid_mime_type` (function) — [saleor/graphql/core/tests/test_file_upload.py:232]
- `test_file_upload_invalid_extension` (function) — [saleor/graphql/core/tests/test_file_upload.py:260]

**`saleor/graphql/core/tests/test_file_validation.py`**

- `test_is_supported_image_mimetype_valid_mimetype` (function) — [saleor/graphql/core/tests/test_file_validation.py:20]
- `test_is_supported_image_mimetype_invalid_mimetype` (function) — [saleor/graphql/core/tests/test_file_validation.py:31]
- `test_clean_image_file` (function) — [saleor/graphql/core/tests/test_file_validation.py:42]
- `test_clean_image_file_file_size_exceeds_limit` (function) — [saleor/graphql/core/tests/test_file_validation.py:56]
- `test_clean_image_file_file_size_within_limit` (function) — [saleor/graphql/core/tests/test_file_validation.py:76]
- `test_clean_image_file_invalid_content_type` (function) — [saleor/graphql/core/tests/test_file_validation.py:88]
- `test_clean_image_file_no_file` (function) — [saleor/graphql/core/tests/test_file_validation.py:104]
- `test_clean_image_file_no_file_extension` (function) — [saleor/graphql/core/tests/test_file_validation.py:116]
- `test_clean_image_file_invalid_file_extension` (function) — [saleor/graphql/core/tests/test_file_validation.py:132]
- `test_clean_image_file_file_extension_not_supported_by_thumbnails` (function) — [saleor/graphql/core/tests/test_file_validation.py:151]
- `test_clean_image_file_issue_with_file_opening` (function) — [saleor/graphql/core/tests/test_file_validation.py:170]
- `test_clean_image_file_exif_validation_raising_error` (function) — [saleor/graphql/core/tests/test_file_validation.py:192]
- `test_clean_image_file_invalid_image_mime_type` (function) — [saleor/graphql/core/tests/test_file_validation.py:215]
- `test_clean_image_file_with_captialized_extension` (function) — [saleor/graphql/core/tests/test_file_validation.py:235]
- `test_clean_image_file_in_avif_format` (function) — [saleor/graphql/core/tests/test_file_validation.py:248]
- `test_validate_upload_file_valid_files` (function) — [saleor/graphql/core/tests/test_file_validation.py:279]
- `test_validate_upload_file_unsupported_mime_type` (function) — [saleor/graphql/core/tests/test_file_validation.py:302]
- `test_validate_upload_file_invalid_file_type` (function) — [saleor/graphql/core/tests/test_file_validation.py:330]
- `test_validate_upload_file_detects_spoofed_content_type` (function) — [saleor/graphql/core/tests/test_file_validation.py:346]
- `test_detect_mime_type_success` (function) — [saleor/graphql/core/tests/test_file_validation.py:369]
- `test_detect_mime_type_reads_file_content` (function) — [saleor/graphql/core/tests/test_file_validation.py:383]

**`saleor/graphql/core/tests/test_graphql.py`**

- `test_middleware_dont_generate_sql_requests` (function) — [saleor/graphql/core/tests/test_graphql.py:19]
- `test_jwt_middleware` (function) — [saleor/graphql/core/tests/test_graphql.py:31]
- `test_real_query` (function) — [saleor/graphql/core/tests/test_graphql.py:78]
- `test_get_nodes` (function) — [saleor/graphql/core/tests/test_graphql.py:226]
- `test_get_nodes_for_order_with_int_id` (function) — [saleor/graphql/core/tests/test_graphql.py:274]
- `test_get_nodes_for_order_with_uuid_id` (function) — [saleor/graphql/core/tests/test_graphql.py:290]
- `test_get_nodes_for_order_with_int_id_and_use_old_id_set_to_false` (function) — [saleor/graphql/core/tests/test_graphql.py:304]
- `test_get_nodes_for_order_with_uuid_and_int_id` (function) — [saleor/graphql/core/tests/test_graphql.py:317]
- `test_from_global_id_or_error` (function) — [saleor/graphql/core/tests/test_graphql.py:331]
- `test_from_global_id_or_error_wth_invalid_type` (function) — [saleor/graphql/core/tests/test_graphql.py:341]
- `test_from_global_id_or_error_wth_type` (function) — [saleor/graphql/core/tests/test_graphql.py:351]
- `test_query_allow_replica` (function) — [saleor/graphql/core/tests/test_graphql.py:366]

**`saleor/graphql/core/tests/test_json_string_scalar.py`**

- `test_parse_value_valid_string` (function) — [saleor/graphql/core/tests/test_json_string_scalar.py:16]
- `test_parse_value_invalid_returns_none` (function) — [saleor/graphql/core/tests/test_json_string_scalar.py:30]
- `test_parse_literal_valid_string` (function) — [saleor/graphql/core/tests/test_json_string_scalar.py:34]
- `test_parse_literal_invalid_returns_none` (function) — [saleor/graphql/core/tests/test_json_string_scalar.py:47]

**`saleor/graphql/core/tests/test_pagination.py`**

- `BookType` (class) — [saleor/graphql/core/tests/test_pagination.py:13]
- `BookTypeCountableConnection` (class) — [saleor/graphql/core/tests/test_pagination.py:17]
- `Meta` (class) — [saleor/graphql/core/tests/test_pagination.py:18]
- `Query` (class) — [saleor/graphql/core/tests/test_pagination.py:22]
- `resolve_books` (function) — [saleor/graphql/core/tests/test_pagination.py:26]
- `ListQuery` (class) — [saleor/graphql/core/tests/test_pagination.py:34]
- `resolve_books` (function) — [saleor/graphql/core/tests/test_pagination.py:40]
- `books` (function) — [saleor/graphql/core/tests/test_pagination.py:49]
- `test_pagination_forward` (function) — [saleor/graphql/core/tests/test_pagination.py:74]
- `test_pagination_backward` (function) — [saleor/graphql/core/tests/test_pagination.py:94]
- `test_pagination_order` (function) — [saleor/graphql/core/tests/test_pagination.py:113]
- `test_pagination_previous_page_using_last` (function) — [saleor/graphql/core/tests/test_pagination.py:131]
- `test_pagination_forward_first_page_info` (function) — [saleor/graphql/core/tests/test_pagination.py:156]
- `test_pagination_forward_middle_page_info` (function) — [saleor/graphql/core/tests/test_pagination.py:166]
- `test_pagination_forward_last_page_info` (function) — [saleor/graphql/core/tests/test_pagination.py:184]
- `test_pagination_backward_first_page_info` (function) — [saleor/graphql/core/tests/test_pagination.py:202]
- `test_pagination_backward_middle_page_info` (function) — [saleor/graphql/core/tests/test_pagination.py:212]
- `test_pagination_backward_last_page_info` (function) — [saleor/graphql/core/tests/test_pagination.py:230]
- `test_pagination_invalid_cursor` (function) — [saleor/graphql/core/tests/test_pagination.py:248]
- `test_pagination_invalid_cursor_and_valid_base64` (function) — [saleor/graphql/core/tests/test_pagination.py:259]
- `test_pagination_cursor_decodes_to_non_list` (function) — [saleor/graphql/core/tests/test_pagination.py:269]
- `test_query_with_pagination_and_fragments` (function) — [saleor/graphql/core/tests/test_pagination.py:317]
- `test_query_with_pagination_and_fragments_no_first_or_last_raises_an_error` (function) — [saleor/graphql/core/tests/test_pagination.py:328]
- `test_query_with_pagination_and_inline_fragments` (function) — [saleor/graphql/core/tests/test_pagination.py:372]
- `test_list_pagination_forward_first_page_info` (function) — [saleor/graphql/core/tests/test_pagination.py:386]
- `test_list_pagination_forward_middle_page_info` (function) — [saleor/graphql/core/tests/test_pagination.py:401]
- `test_list_pagination_forward_last_page_info` (function) — [saleor/graphql/core/tests/test_pagination.py:420]
- `test_list_pagination_backward_first_page_info` (function) — [saleor/graphql/core/tests/test_pagination.py:439]
- `test_list_pagination_backward_middle_page_info` (function) — [saleor/graphql/core/tests/test_pagination.py:454]
- `test_list_pagination_backward_last_page_info` (function) — [saleor/graphql/core/tests/test_pagination.py:473]

**`saleor/graphql/core/tests/test_query_cost_validation.py`**

- `test_query_exceeding_cost_limit_fails_validation` (function) — [saleor/graphql/core/tests/test_query_cost_validation.py:10]
- `test_query_below_cost_limit_passes_validation` (function) — [saleor/graphql/core/tests/test_query_cost_validation.py:44]
- `test_query_exceeding_cost_limit_due_to_multiplied_complexity_fails_validation` (function) — [saleor/graphql/core/tests/test_query_cost_validation.py:88]
- `test_query_below_cost_limit_with_multiplied_complexity_passes_validation` (function) — [saleor/graphql/core/tests/test_query_cost_validation.py:113]
- `test_query_with_fragments_have_same_multiplied_complexity_cost` (function) — [saleor/graphql/core/tests/test_query_cost_validation.py:213]
- `test_query_cost_for_inline_fragments_on_interface` (function) — [saleor/graphql/core/tests/test_query_cost_validation.py:268]
- `test_query_cost_for_spread_fragments_on_interface` (function) — [saleor/graphql/core/tests/test_query_cost_validation.py:346]
- `test_query_cost_for_spread_and_inline_fragments_on_interface` (function) — [saleor/graphql/core/tests/test_query_cost_validation.py:429]
- `test_query_with_empty_not_required_limit_argument` (function) — [saleor/graphql/core/tests/test_query_cost_validation.py:494]
- `test_query_with_not_required_limit_argument_not_provided` (function) — [saleor/graphql/core/tests/test_query_cost_validation.py:524]

**`saleor/graphql/core/tests/test_scalars_decimals.py`**

- `test_decimal_scalar_invalid_value` (function) — [saleor/graphql/core/tests/test_scalars_decimals.py:12]
- `test_decimal_scalar_valid_literal` (function) — [saleor/graphql/core/tests/test_scalars_decimals.py:26]
- `test_decimal_scalar_invalid_literal` (function) — [saleor/graphql/core/tests/test_scalars_decimals.py:38]
- `test_positive_decimal_scalar_valid_literal` (function) — [saleor/graphql/core/tests/test_scalars_decimals.py:53]
- `test_positive_decimal_scalar_valid_literal_zero` (function) — [saleor/graphql/core/tests/test_scalars_decimals.py:66]
- `test_positive_decimal_scalar_invalid_value` (function) — [saleor/graphql/core/tests/test_scalars_decimals.py:73]
- `test_positive_decimal_scalar_valid_value_zero` (function) — [saleor/graphql/core/tests/test_scalars_decimals.py:78]
- `test_positive_decimal_scalar_invalid_literal` (function) — [saleor/graphql/core/tests/test_scalars_decimals.py:91]
- `test_positive_int_scalar_valid_literal` (function) — [saleor/graphql/core/tests/test_scalars_decimals.py:108]
- `test_positive_int_scalar_invalid_literal` (function) — [saleor/graphql/core/tests/test_scalars_decimals.py:123]
- `test_positive_int_scalar_valid_value` (function) — [saleor/graphql/core/tests/test_scalars_decimals.py:132]
- `test_positive_int_scalar_invalid_value` (function) — [saleor/graphql/core/tests/test_scalars_decimals.py:141]

**`saleor/graphql/core/tests/test_scalars_weight.py`**

- `test_weight_scalar_parse_value_with_none_value` (function) — [saleor/graphql/core/tests/test_scalars_weight.py:15]

**`saleor/graphql/core/tests/test_scalars.py`**

- `test_uuid_scalar_value_passed_as_variable` (function) — [saleor/graphql/core/tests/test_scalars.py:19]
- `test_uuid_scalar_wrong_value_passed_as_variable` (function) — [saleor/graphql/core/tests/test_scalars.py:26]
- `test_uuid_scalar_value_passed_in_input` (function) — [saleor/graphql/core/tests/test_scalars.py:33]
- `test_uuid_scalar_wrong_value_passed_in_input` (function) — [saleor/graphql/core/tests/test_scalars.py:48]
- `test_order_query_with_filter_created_str_as_date_value` (function) — [saleor/graphql/core/tests/test_scalars.py:71]
- `test_json_scalar_as_correct_variable` (function) — [saleor/graphql/core/tests/test_scalars.py:144]
- `test_json_scalar_as_incorrect_variable` (function) — [saleor/graphql/core/tests/test_scalars.py:170]
- `test_json_scalar_as_incorrect_value` (function) — [saleor/graphql/core/tests/test_scalars.py:215]
- `test_json_scalar_as_correct_value` (function) — [saleor/graphql/core/tests/test_scalars.py:257]
- `test_incorrect_date_time_as_variable` (function) — [saleor/graphql/core/tests/test_scalars.py:305]
- `test_correct_date_time_as_variable` (function) — [saleor/graphql/core/tests/test_scalars.py:331]
- `test_incorrect_date_time_as_input` (function) — [saleor/graphql/core/tests/test_scalars.py:356]
- `test_correct_date_time_as_input` (function) — [saleor/graphql/core/tests/test_scalars.py:396]

**`saleor/graphql/core/tests/test_validators.py`**

- `test_validate_price_precision` (function) — [saleor/graphql/core/tests/test_validators.py:31]
- `test_validate_price_precision_raise_error` (function) — [saleor/graphql/core/tests/test_validators.py:49]
- `test_validate_end_is_after_start_raise_error` (function) — [saleor/graphql/core/tests/test_validators.py:54]
- `test_validate_end_is_after_start` (function) — [saleor/graphql/core/tests/test_validators.py:73]
- `test_validate_one_of_args_is_in_query` (function) — [saleor/graphql/core/tests/test_validators.py:77]
- `test_validate_one_of_args_is_in_query_false_args` (function) — [saleor/graphql/core/tests/test_validators.py:81]
- `test_validate_one_of_args_is_in_query_more_than_one_true` (function) — [saleor/graphql/core/tests/test_validators.py:89]
- `test_validate_one_of_args_is_in_query_single_arg` (function) — [saleor/graphql/core/tests/test_validators.py:99]
- `test_validate_one_of_args_is_in_query_single_arg_absent` (function) — [saleor/graphql/core/tests/test_validators.py:103]
- `test_clean_seo_fields` (function) — [saleor/graphql/core/tests/test_validators.py:109]
- `test_clean_seo_fields_accepts_null` (function) — [saleor/graphql/core/tests/test_validators.py:118]
- `test_validate_slug_and_generate_if_needed_raises_errors` (function) — [saleor/graphql/core/tests/test_validators.py:133]
- `test_validate_slug_and_generate_if_needed_not_raises_errors` (function) — [saleor/graphql/core/tests/test_validators.py:141]
- `test_validate_slug_and_generate_if_needed_generate_slug` (function) — [saleor/graphql/core/tests/test_validators.py:154]
- `test_validate_slug_and_generate_if_needed_slug_not_changed` (function) — [saleor/graphql/core/tests/test_validators.py:176]

**`saleor/graphql/core/tests/test_view.py`**

- `test_batch_queries` (function) — [saleor/graphql/core/tests/test_view.py:30]
- `test_rejects_based_on_number_batch_queries` (function) — [saleor/graphql/core/tests/test_view.py:78]
- `test_batch_query_size_metric_is_recorded` (function) — [saleor/graphql/core/tests/test_view.py:133]
- `test_graphql_view_query_with_invalid_object_type` (function) — [saleor/graphql/core/tests/test_view.py:156]
- `test_graphql_view_get_enabled_or_disabled` (function) — [saleor/graphql/core/tests/test_view.py:176]
- `test_graphql_view_not_allowed` (function) — [saleor/graphql/core/tests/test_view.py:183]
- `test_invalid_request_body_non_debug` (function) — [saleor/graphql/core/tests/test_view.py:190]
- `test_invalid_request_body_with_debug` (function) — [saleor/graphql/core/tests/test_view.py:203]
- `test_invalid_request_body_error_is_not_logged` (function) — [saleor/graphql/core/tests/test_view.py:216]
- `test_unexpected_types_in_json_request_body` (function) — [saleor/graphql/core/tests/test_view.py:240]
- `test_request_body_too_big` (function) — [saleor/graphql/core/tests/test_view.py:252]
- `test_invalid_query` (function) — [saleor/graphql/core/tests/test_view.py:268]
- `test_no_query` (function) — [saleor/graphql/core/tests/test_view.py:276]
- `test_query_is_dict` (function) — [saleor/graphql/core/tests/test_view.py:283]
- `test_graphql_execution_exception` (function) — [saleor/graphql/core/tests/test_view.py:291]
- `mocked_execute` (function) — [saleor/graphql/core/tests/test_view.py:292]
- `test_invalid_query_graphql_errors_are_logged_in_another_logger` (function) — [saleor/graphql/core/tests/test_view.py:302]
- `test_invalid_syntax_graphql_errors_are_logged_in_another_logger` (function) — [saleor/graphql/core/tests/test_view.py:319]
- `test_permission_denied_query_graphql_errors_are_logged_in_another_logger` (function) — [saleor/graphql/core/tests/test_view.py:336]
- `test_validation_errors_query_do_not_get_logged` (function) — [saleor/graphql/core/tests/test_view.py:363]
- `test_unexpected_exceptions_are_logged_in_their_own_logger` (function) — [saleor/graphql/core/tests/test_view.py:383]
- `bad_mocked_resolve_collection_by_id` (function) — [saleor/graphql/core/tests/test_view.py:391]
- `test_query_contains_not_only_schema_raise_error` (function) — [saleor/graphql/core/tests/test_view.py:421]
- `test_introspection_query_is_cached` (function) — [saleor/graphql/core/tests/test_view.py:466]
- `test_introspection_query_is_cached_only_once` (function) — [saleor/graphql/core/tests/test_view.py:480]
- `test_introspection_query_is_not_cached_in_debug_mode` (function) — [saleor/graphql/core/tests/test_view.py:492]
- `test_generate_cache_key_use_saleor_version` (function) — [saleor/graphql/core/tests/test_view.py:500]
- `test_graphql_view_clears_context` (function) — [saleor/graphql/core/tests/test_view.py:505]
- `test_playground_is_rendered_with_proper_api_url_if_public_url_is_set` (function) — [saleor/graphql/core/tests/test_view.py:536]
- `test_marks_slow_queries` (function) — [saleor/graphql/core/tests/test_view.py:562]
- `set_allow_storefront_traffic` (function) — [saleor/graphql/core/tests/test_view.py:609]
- `set_flag` (function) — [saleor/graphql/core/tests/test_view.py:612]
- `storefront_traffic_disabled` (function) — [saleor/graphql/core/tests/test_view.py:623]
- `test_storefront_traffic_allowed_by_default` (function) — [saleor/graphql/core/tests/test_view.py:627]
- `test_request_per_principal` (function) — [saleor/graphql/core/tests/test_view.py:644]
- `test_unusable_authorization_header_blocked_when_disabled` (function) — [saleor/graphql/core/tests/test_view.py:677]
- `test_anonymous_batch_rejected_when_disabled` (function) — [saleor/graphql/core/tests/test_view.py:691]
- `test_anonymous_introspection_blocked_when_disabled` (function) — [saleor/graphql/core/tests/test_view.py:706]
- `test_real_public_query_blocked_when_disabled` (function) — [saleor/graphql/core/tests/test_view.py:718]
- `test_real_public_mutation_blocked_when_disabled` (function) — [saleor/graphql/core/tests/test_view.py:738]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/core/tests/__init__.py` (16 lines)
- `saleor/graphql/core/tests/cassettes/test_core/test_get_oembed_data[http---www.youtube.com-watch-v=dQw4w9WgXcQ-VIDEO].yaml` (50 lines)
- `saleor/graphql/core/tests/cassettes/test_core/test_get_oembed_data[https---vimeo.com-148751763-VIDEO].yaml` (82 lines)
- `saleor/graphql/core/tests/cassettes/test_core/test_get_oembed_data[https---www.flickr.com-photos-megane_wakui-31740618232--IMAGE].yaml` (110 lines)
- `saleor/graphql/core/tests/cassettes/test_core/test_get_oembed_data[https---www.youtube.com-watch-v=dQw4w9WgXcQ-VIDEO].yaml` (50 lines)
- `saleor/graphql/core/tests/cassettes/test_core/test_get_oembed_data[https---www.youtube.com-watch-v=dQw4w9WgXcQ&ab_channel=TestingChannel-VIDEO].yaml` (50 lines)
- `saleor/graphql/core/tests/test_base_mutation.py` (316 lines)
- `saleor/graphql/core/tests/test_context.py` (56 lines)
- `saleor/graphql/core/tests/test_converters.py` (92 lines)
- `saleor/graphql/core/tests/test_core_reordering.py` (272 lines)
- `saleor/graphql/core/tests/test_core.py` (373 lines)
- `saleor/graphql/core/tests/test_deprecated_field_monitoring.py` (304 lines)
- `saleor/graphql/core/tests/test_federation.py` (50 lines)
- `saleor/graphql/core/tests/test_file_upload.py` (282 lines)
- `saleor/graphql/core/tests/test_file_validation.py` (396 lines)
- `saleor/graphql/core/tests/test_graphql.py` (386 lines)
- `saleor/graphql/core/tests/test_json_string_scalar.py` (48 lines)
- `saleor/graphql/core/tests/test_pagination.py` (489 lines)
- `saleor/graphql/core/tests/test_query_cost_validation.py` (550 lines)
- `saleor/graphql/core/tests/test_scalars_decimals.py` (143 lines)
- `saleor/graphql/core/tests/test_scalars_weight.py` (17 lines)
- `saleor/graphql/core/tests/test_scalars.py` (421 lines)
- `saleor/graphql/core/tests/test_validators.py` (185 lines)
- `saleor/graphql/core/tests/test_view.py` (759 lines)

## Interactions

- Imports from: `saleor/graphql`, `saleor/webhook`, `saleor/graphql/order`, `saleor/attribute/tests`, `saleor/core/telemetry`, `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....__version__`
- `....attribute.models`
- `....core.error_codes.UploadErrorCode`
- `....core.exceptions.UnsupportedMediaProviderException`
- `....core.jwt.create_access_token`
- `....core.telemetry.Scope`
- `....core.telemetry.Unit`
- `....core.utils.validators.get_oembed_data`
- `....graphql.tests.utils.get_graphql_content`
- `....order.models`
- `....order.models.Order`
- `....payment.interface.PaymentGatewayData`
- `....permission.enums.ProductPermissions`
- `....product.ProductMediaTypes`
- `....product.error_codes.ProductErrorCode`
- `....product.models.Category`
- `....product.models.Product`
- `....product.models.ProductChannelListing`
- `....product.tests.utils.create_image`
- `....shipping.utils.convert_to_shipping_method_data`
- `....tests.models.Book`
- `....tests.utils.get_metric_data`
- `....tests.utils.get_span_by_name`
- `....thumbnail.FILE_NAME_MAX_LENGTH`
- `....webhook.event_types.WebhookEventAsyncType`
- `....webhook.event_types.WebhookEventSyncType`
- `...api.backend`
- `...api.schema`
- `...context.set_app_on_context`
- `...core.utils.from_global_id_or_error`
- `...metrics.METRIC_GRAPHQL_BATCH_SIZE`
- `...order.types`
- `...order.types.Order`
- `...product.types`
- `...product.types.Product`
- `...query_cost_map.COST_MAP`
- `...tests.fixtures.API_PATH`
- `...tests.utils.get_graphql_content`
- `...tests.utils.get_graphql_content_from_response`
- `...utils.INTERNAL_ERROR_MESSAGE`
- `...utils.filters.filter_range_field`
- `...utils.filters.reporting_period_to_date`
- `...utils.get_nodes`
- `...utils.requestor_is_superuser`
- `...views.GraphQLView`
- `...views.generate_cache_key`
- `...webhook.tests.test_subscription_payload.initialize_request`
- `..ErrorTest`
- `..connection.CountableConnection`
- `..connection.create_connection_slice`
- `..const.DEFAULT_NESTED_LIST_LIMIT`
- `..context.SaleorContext`
- `..enums.ReportingPeriod`
- `..fields.ConnectionField`
- `..fields.JSONString`
- `..filters.EnumFilter`
- `..filters.filter_input.FilterInputObjectType`
- `..mutations.BaseMutation`
- `..mutations.ModelWithExtRefMutation`
- `..scalars.Decimal`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `554fe9aad862` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
