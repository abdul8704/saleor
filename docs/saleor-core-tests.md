## Purpose

`saleor/core/tests` (`saleor/core/tests`) groups 28 source file(s) exposing 258 top-level declaration(s).

## Public surface

**`saleor/core/tests/test_anonymize.py`**

- `test_obfuscate_email` (function) — [saleor/core/tests/test_anonymize.py:4]
- `test_obfuscate_email_example_email` (function) — [saleor/core/tests/test_anonymize.py:15]
- `test_obfuscate_email_no_at_in_email` (function) — [saleor/core/tests/test_anonymize.py:26]
- `test_obfuscate_string` (function) — [saleor/core/tests/test_anonymize.py:37]
- `test_obfuscate_string_empty_string` (function) — [saleor/core/tests/test_anonymize.py:48]
- `test_obfuscate_string_phone_string` (function) — [saleor/core/tests/test_anonymize.py:59]
- `test_obfuscate_address` (function) — [saleor/core/tests/test_anonymize.py:70]
- `test_obfuscate_address_no_address` (function) — [saleor/core/tests/test_anonymize.py:92]

**`saleor/core/tests/test_auth_backend_default_header.py`**

- `test_use_default_header_as_a_fallback` (function) — [saleor/core/tests/test_auth_backend_default_header.py:20]
- `test_user_authenticated` (function) — [saleor/core/tests/test_auth_backend_default_header.py:32]
- `test_user_deactivated` (function) — [saleor/core/tests/test_auth_backend_default_header.py:41]
- `test_incorect_type_of_token` (function) — [saleor/core/tests/test_auth_backend_default_header.py:52]
- `test_saleor_is_not_owner_of_token` (function) — [saleor/core/tests/test_auth_backend_default_header.py:61]
- `test_owner_field_is_missing` (function) — [saleor/core/tests/test_auth_backend_default_header.py:76]
- `test_incorrect_token` (function) — [saleor/core/tests/test_auth_backend_default_header.py:90]
- `test_missing_token` (function) — [saleor/core/tests/test_auth_backend_default_header.py:108]
- `test_missing_header` (function) — [saleor/core/tests/test_auth_backend_default_header.py:114]
- `test_token_expired` (function) — [saleor/core/tests/test_auth_backend_default_header.py:121]
- `test_user_doesnt_exist` (function) — [saleor/core/tests/test_auth_backend_default_header.py:131]
- `test_user_deactivated_token` (function) — [saleor/core/tests/test_auth_backend_default_header.py:141]
- `test_user_doesnt_have_permissions_from_token` (function) — [saleor/core/tests/test_auth_backend_default_header.py:152]
- `test_user_with_limited_permissions` (function) — [saleor/core/tests/test_auth_backend_default_header.py:192]
- `test_user_payload_doesnt_have_user_token` (function) — [saleor/core/tests/test_auth_backend_default_header.py:210]
- `test_staff_user_customers_only_mode` (function) — [saleor/core/tests/test_auth_backend_default_header.py:224]
- `test_customer_user_customers_only_mode` (function) — [saleor/core/tests/test_auth_backend_default_header.py:245]
- `test_staff_user_disabled_mode` (function) — [saleor/core/tests/test_auth_backend_default_header.py:262]
- `test_staff_user_app_access_token_customers_only_mode` (function) — [saleor/core/tests/test_auth_backend_default_header.py:278]
- `test_staff_user_app_access_token_disabled_mode` (function) — [saleor/core/tests/test_auth_backend_default_header.py:306]

**`saleor/core/tests/test_auth_backend_saleor_header.py`**

- `test_use_authorization_bearer_header_when_authorization_is_provided` (function) — [saleor/core/tests/test_auth_backend_saleor_header.py:20]
- `test_use_saleor_header_as_a_first_try` (function) — [saleor/core/tests/test_auth_backend_saleor_header.py:33]
- `test_user_authenticated` (function) — [saleor/core/tests/test_auth_backend_saleor_header.py:46]
- `test_user_deactivated` (function) — [saleor/core/tests/test_auth_backend_saleor_header.py:54]
- `test_incorect_type_of_token` (function) — [saleor/core/tests/test_auth_backend_saleor_header.py:64]
- `test_saleor_is_not_owner_of_token` (function) — [saleor/core/tests/test_auth_backend_saleor_header.py:72]
- `test_incorrect_token` (function) — [saleor/core/tests/test_auth_backend_saleor_header.py:86]
- `test_missing_token` (function) — [saleor/core/tests/test_auth_backend_saleor_header.py:103]
- `test_missing_header` (function) — [saleor/core/tests/test_auth_backend_saleor_header.py:109]
- `test_token_expired` (function) — [saleor/core/tests/test_auth_backend_saleor_header.py:115]
- `test_user_doesnt_exist` (function) — [saleor/core/tests/test_auth_backend_saleor_header.py:124]
- `test_user_deactivated_token` (function) — [saleor/core/tests/test_auth_backend_saleor_header.py:133]
- `test_user_doesnt_have_permissions_from_token` (function) — [saleor/core/tests/test_auth_backend_saleor_header.py:143]
- `test_user_with_limited_permissions` (function) — [saleor/core/tests/test_auth_backend_saleor_header.py:183]
- `test_user_payload_doesnt_have_user_token` (function) — [saleor/core/tests/test_auth_backend_saleor_header.py:200]

**`saleor/core/tests/test_core.py`**

- `test_get_client_ip` (function) — [saleor/core/tests/test_core.py:64]
- `test_create_superuser` (function) — [saleor/core/tests/test_core.py:71]
- `test_create_shipping_zones` (function) — [saleor/core/tests/test_core.py:88]
- `test_create_channels` (function) — [saleor/core/tests/test_core.py:95]
- `test_create_channels_with_default_channel_slug` (function) — [saleor/core/tests/test_core.py:104]
- `test_create_fake_user` (function) — [saleor/core/tests/test_core.py:112]
- `test_create_fake_users` (function) — [saleor/core/tests/test_core.py:120]
- `test_create_address` (function) — [saleor/core/tests/test_core.py:127]
- `test_create_fake_order` (function) — [saleor/core/tests/test_core.py:133]
- `test_create_catalogue_promotions` (function) — [saleor/core/tests/test_core.py:155]
- `test_create_order_promotions` (function) — [saleor/core/tests/test_core.py:166]
- `test_create_vouchers` (function) — [saleor/core/tests/test_core.py:177]
- `test_create_gift_card` (function) — [saleor/core/tests/test_core.py:190]
- `test_storages_set_s3_bucket_domain` (function) — [saleor/core/tests/test_core.py:207]
- `test_storages_not_setting_s3_bucket_domain` (function) — [saleor/core/tests/test_core.py:216]
- `test_build_absolute_uri` (function) — [saleor/core/tests/test_core.py:224]
- `test_build_absolute_uri_with_host` (function) — [saleor/core/tests/test_core.py:237]
- `test_build_absolute_uri_with_public_url` (function) — [saleor/core/tests/test_core.py:256]
- `test_build_absolute_uri_with_public_url_and_absolute_location` (function) — [saleor/core/tests/test_core.py:267]
- `test_is_ssl_enabled` (function) — [saleor/core/tests/test_core.py:278]
- `test_is_ssl_enabled_with_public_url` (function) — [saleor/core/tests/test_core.py:291]
- `test_get_domain` (function) — [saleor/core/tests/test_core.py:299]
- `test_get_domain_with_public_url` (function) — [saleor/core/tests/test_core.py:304]
- `test_delete_sort_order_with_null_value` (function) — [saleor/core/tests/test_core.py:311]
- `test_generate_unique_slug_with_slugable_field` (function) — [saleor/core/tests/test_core.py:333]
- `test_generate_unique_slug_for_slug_with_max_characters_number` (function) — [saleor/core/tests/test_core.py:357]
- `test_generate_unique_slug_with_additional_lookup_slug_not_changed` (function) — [saleor/core/tests/test_core.py:365]
- `test_generate_unique_slug_with_additional_lookup_slug_changed` (function) — [saleor/core/tests/test_core.py:384]
- `test_cleardb_exits_with_debug_off` (function) — [saleor/core/tests/test_core.py:402]
- `test_cleardb_passes_with_force_flag_in_debug_off` (function) — [saleor/core/tests/test_core.py:408]
- `test_cleardb_delete_staff_parameter` (function) — [saleor/core/tests/test_core.py:413]
- `test_cleardb_preserves_data` (function) — [saleor/core/tests/test_core.py:425]
- `test_cleardb_remove_orders_and_transactions` (function) — [saleor/core/tests/test_core.py:435]
- `test_prepare_unique_attribute_value_slug` (function) — [saleor/core/tests/test_core.py:445]
- `test_prepare_unique_attribute_value_slug_non_existing_slug` (function) — [saleor/core/tests/test_core.py:460]

**`saleor/core/tests/test_dataloaders.py`**

- `test_plugins_manager_loader_loads_requestor_in_plugin` (function) — [saleor/core/tests/test_dataloaders.py:6]
- `test_plugins_manager_loader_requestor_in_plugin_when_no_app_and_user_in_req_is_none` (function) — [saleor/core/tests/test_dataloaders.py:23]

**`saleor/core/tests/test_event_payload.py`**

- `payload_data` (function) — [saleor/core/tests/test_event_payload.py:10]
- `test_reading_event_payload` (function) — [saleor/core/tests/test_event_payload.py:14]
- `test_reading_event_payload_saved_as_string` (function) — [saleor/core/tests/test_event_payload.py:26]

**`saleor/core/tests/test_hashers.py`**

- `test_encode_and_verify_sha512_base64_pbkdf2` (function) — [saleor/core/tests/test_hashers.py:4]

**`saleor/core/tests/test_http_client.py`**

- `test_user_agent_override` (function) — [saleor/core/tests/test_http_client.py:10]
- `test_http_client_disallows_private_ip_ranges` (function) — [saleor/core/tests/test_http_client.py:26]

**`saleor/core/tests/test_jwt_manager.py`**

- `test_get_jwt_manager` (function) — [saleor/core/tests/test_jwt_manager.py:12]
- `test_jwt_manager_validate_missing_rsa_private_key` (function) — [saleor/core/tests/test_jwt_manager.py:24]
- `test_jwt_manager_validate_incorrect_format_of_rsa_private_key` (function) — [saleor/core/tests/test_jwt_manager.py:34]
- `test_jwt_manager_encode` (function) — [saleor/core/tests/test_jwt_manager.py:43]
- `test_jwt_manager_jws_encode` (function) — [saleor/core/tests/test_jwt_manager.py:66]
- `test_jwt_manager_decode_token_signed_with_rs256` (function) — [saleor/core/tests/test_jwt_manager.py:96]
- `test_jwt_manager_decode_token_signed_with_hs256` (function) — [saleor/core/tests/test_jwt_manager.py:112]

**`saleor/core/tests/test_jwt.py`**

- `test_create_access_token_for_app` (function) — [saleor/core/tests/test_jwt.py:18]
- `test_create_access_token_for_app_extension_staff_user_with_more_permissions` (function) — [saleor/core/tests/test_jwt.py:46]
- `test_create_access_token_for_app_extension_with_more_permissions` (function) — [saleor/core/tests/test_jwt.py:91]
- `test_jwt_decode_accepts_token_signed_with_hs256` (function) — [saleor/core/tests/test_jwt.py:132]
- `test_jwt_decode_accepts_token_signed_with_rs256` (function) — [saleor/core/tests/test_jwt.py:144]
- `test_jwt_decode_accepts_app_token_rs256_with_audience` (function) — [saleor/core/tests/test_jwt.py:159]
- `test_jwt_decode_accepts_app_token_hs256_with_audience` (function) — [saleor/core/tests/test_jwt.py:172]
- `test_jwt_encode_creates_token_signed_with_rs256` (function) — [saleor/core/tests/test_jwt.py:182]
- `test_get_user_from_access_payload_with_is_staff_true` (function) — [saleor/core/tests/test_jwt.py:194]
- `test_get_user_from_access_payload_for_customer` (function) — [saleor/core/tests/test_jwt.py:211]

**`saleor/core/tests/test_metadata_manager.py`**

- `valid_metadata_input` (function) — [saleor/core/tests/test_metadata_manager.py:17]
- `invalid_metadata_input` (function) — [saleor/core/tests/test_metadata_manager.py:28]
- `valid_metadata_input_list` (function) — [saleor/core/tests/test_metadata_manager.py:39]
- `invalid_metadata_input_list` (function) — [saleor/core/tests/test_metadata_manager.py:44]
- `invalid_metadata_input_list_with_one_valid` (function) — [saleor/core/tests/test_metadata_manager.py:49]
- `test_create_collection_empty` (function) — [saleor/core/tests/test_metadata_manager.py:55]
- `test_create_collection_valid` (function) — [saleor/core/tests/test_metadata_manager.py:61]
- `test_create_collection` (function) — [saleor/core/tests/test_metadata_manager.py:74]
- `test_testing_model_is_inheriting_metadata` (function) — [saleor/core/tests/test_metadata_manager.py:81]
- `test_write_on_model_public` (function) — [saleor/core/tests/test_metadata_manager.py:90]
- `test_write_on_model_private` (function) — [saleor/core/tests/test_metadata_manager.py:103]
- `test_throw_on_empty_key` (function) — [saleor/core/tests/test_metadata_manager.py:116]
- `test_throw_on_empty_key_with_whitespaces` (function) — [saleor/core/tests/test_metadata_manager.py:121]
- `test_store_multiple_keys` (function) — [saleor/core/tests/test_metadata_manager.py:130]
- `test_throws_for_invalid_metadata_target` (function) — [saleor/core/tests/test_metadata_manager.py:152]

**`saleor/core/tests/test_middleware.py`**

- `test_jwt_refresh_token_middleware` (function) — [saleor/core/tests/test_middleware.py:14]
- `test_jwt_refresh_token_middleware_token_without_expire` (function) — [saleor/core/tests/test_middleware.py:29]
- `test_jwt_refresh_token_middleware_samesite_debug_mode` (function) — [saleor/core/tests/test_middleware.py:51]
- `test_jwt_refresh_token_middleware_samesite_none` (function) — [saleor/core/tests/test_middleware.py:67]

**`saleor/core/tests/test_notification.py`**

- `test_validate_and_get_channel_for_non_existing_slug` (function) — [saleor/core/tests/test_notification.py:8]
- `test_validate_and_get_channel_for_inactive_channel` (function) — [saleor/core/tests/test_notification.py:15]
- `test_validate_and_get_channel_for_lack_of_input` (function) — [saleor/core/tests/test_notification.py:25]
- `test_validate_and_get_channel` (function) — [saleor/core/tests/test_notification.py:30]

**`saleor/core/tests/test_postgresql_search.py`**

- `named_products` (function) — [saleor/core/tests/test_postgresql_search.py:20]
- `gen_product` (function) — [saleor/core/tests/test_postgresql_search.py:21]
- `execute_search` (function) — [saleor/core/tests/test_postgresql_search.py:45]
- `test_storefront_product_fuzzy_name_search` (function) — [saleor/core/tests/test_postgresql_search.py:57]
- `gen_address_for_user` (function) — [saleor/core/tests/test_postgresql_search.py:72]
- `test_combined_flat_search_vector` (function) — [saleor/core/tests/test_postgresql_search.py:84]
- `test_flat_concat_drop_exceeding_count_no_silently_fail` (function) — [saleor/core/tests/test_postgresql_search.py:103]
- `LimitedFlatConcat` (class) — [saleor/core/tests/test_postgresql_search.py:104]
- `test_flat_concat_drop_exceeding_count_silently_truncate` (function) — [saleor/core/tests/test_postgresql_search.py:118]
- `LimitedFlatConcat` (class) — [saleor/core/tests/test_postgresql_search.py:119]

**`saleor/core/tests/test_rlimit.py`**

- `test_limit_passed_as_string` (function) — [saleor/core/tests/test_rlimit.py:11]
- `test_limit_passed_as_int` (function) — [saleor/core/tests/test_rlimit.py:29]
- `test_no_limits` (function) — [saleor/core/tests/test_rlimit.py:47]
- `test_only_soft_limit_set` (function) — [saleor/core/tests/test_rlimit.py:65]
- `test_only_hard_limit_set` (function) — [saleor/core/tests/test_rlimit.py:79]
- `test_negative_soft_limit` (function) — [saleor/core/tests/test_rlimit.py:93]
- `test_negative_hard_limit` (function) — [saleor/core/tests/test_rlimit.py:107]
- `test_invalid_soft_limit` (function) — [saleor/core/tests/test_rlimit.py:121]
- `test_invalid_hard_limit` (function) — [saleor/core/tests/test_rlimit.py:135]
- `test_soft_limit_greater_than_hard_limit` (function) — [saleor/core/tests/test_rlimit.py:149]

**`saleor/core/tests/test_schedules.py`**

- `test_search_update_schedule_remaining_estimate_initial_state` (function) — [saleor/core/tests/test_schedules.py:31]
- `test_search_update_schedule_remaining_estimate` (function) — [saleor/core/tests/test_schedules.py:48]
- `test_gift_card_search_update_schedule_are_dirty` (function) — [saleor/core/tests/test_schedules.py:59]
- `test_page_search_update_schedule_are_dirty` (function) — [saleor/core/tests/test_schedules.py:73]
- `test_product_search_update_schedule_are_dirty` (function) — [saleor/core/tests/test_schedules.py:87]
- `test_promotion_webhook_schedule_remaining_estimate_initial_state` (function) — [saleor/core/tests/test_schedules.py:102]
- `test_promotion_webhook_schedule_remaining_estimate` (function) — [saleor/core/tests/test_schedules.py:114]
- `test_is_due_not_promotion_to_notify_about_not_upcoming_promotion` (function) — [saleor/core/tests/test_schedules.py:126]
- `test_is_due_promotion_started_to_notify_and_not_upcoming_promotion` (function) — [saleor/core/tests/test_schedules.py:152]
- `test_is_due_promotion_ended_to_notify_and_not_upcoming_promotion` (function) — [saleor/core/tests/test_schedules.py:179]
- `test_is_due_promotion_started_to_notify_and_upcoming_promotion` (function) — [saleor/core/tests/test_schedules.py:212]
- `test_is_due_no_promotion_to_notify_about_and_upcoming_promotion_exists` (function) — [saleor/core/tests/test_schedules.py:246]
- `test_is_due_no_promo_to_notify_about_upcoming_promo_exists_initial_time_returned` (function) — [saleor/core/tests/test_schedules.py:278]
- `test_promotion_webhook_schedule_import_path` (function) — [saleor/core/tests/test_schedules.py:309]
- `test_automatic_completion_update_schedule_remaining_estimate_initial_state` (function) — [saleor/core/tests/test_schedules.py:321]
- `test_automatic_completion_schedule_remaining_estimate` (function) — [saleor/core/tests/test_schedules.py:333]
- `test_automatic_completion_schedule_are_dirty` (function) — [saleor/core/tests/test_schedules.py:345]
- `test_automatic_completion_schedule_are_dirty_checkout_too_old` (function) — [saleor/core/tests/test_schedules.py:369]
- `test_automatic_completion_schedule_are_dirty_checkout_not_in_cut_off_date` (function) — [saleor/core/tests/test_schedules.py:395]
- `test_automatic_completion_schedule_are_dirty_checkout_in_cut_off_date` (function) — [saleor/core/tests/test_schedules.py:425]
- `test_automatic_completion_schedule_missing_billing_address` (function) — [saleor/core/tests/test_schedules.py:455]
- `test_automatic_completion_schedule_missing_user_or_email` (function) — [saleor/core/tests/test_schedules.py:482]
- `test_automatic_completion_schedule_zero_total` (function) — [saleor/core/tests/test_schedules.py:510]
- `test_checkout_search_update_schedule_are_dirty` (function) — [saleor/core/tests/test_schedules.py:535]
- `test_checkout_search_update_schedule_remaining_estimate_initial_state` (function) — [saleor/core/tests/test_schedules.py:550]
- `test_checkout_search_update_schedule_remaining_estimate` (function) — [saleor/core/tests/test_schedules.py:562]
- `test_checkout_search_update_schedule_not_dirty` (function) — [saleor/core/tests/test_schedules.py:574]

**`saleor/core/tests/test_search_tasks.py`**

- `test_set_user_search_document_values` (function) — [saleor/core/tests/test_search_tasks.py:9]
- `test_set_order_search_document_values_already_present` (function) — [saleor/core/tests/test_search_tasks.py:29]
- `test_set_order_search_document_values_no_vector` (function) — [saleor/core/tests/test_search_tasks.py:45]

**`saleor/core/tests/test_search.py`**

- `test_sanitize_word_removes_tsquery_metacharacters` (function) — [saleor/core/tests/test_search.py:13]
- `test_sanitize_word_preserves_safe_characters` (function) — [saleor/core/tests/test_search.py:24]
- `test_sanitize_word_handles_empty_string` (function) — [saleor/core/tests/test_search.py:35]
- `test_sanitize_word_handles_only_metacharacters` (function) — [saleor/core/tests/test_search.py:46]
- `test_parse_search_query_single_word` (function) — [saleor/core/tests/test_search.py:57]
- `test_parse_search_query_multiple_words_implicit_and` (function) — [saleor/core/tests/test_search.py:61]
- `test_parse_search_query_or_operator` (function) — [saleor/core/tests/test_search.py:65]
- `test_parse_search_query_negation` (function) — [saleor/core/tests/test_search.py:69]
- `test_parse_search_query_quoted_phrase` (function) — [saleor/core/tests/test_search.py:73]
- `test_parse_search_query_quoted_phrase_with_other_terms` (function) — [saleor/core/tests/test_search.py:77]
- `test_parse_search_query_negated_quoted_phrase` (function) — [saleor/core/tests/test_search.py:81]
- `test_parse_search_query_or_with_negation` (function) — [saleor/core/tests/test_search.py:85]
- `test_parse_search_query_with_email` (function) — [saleor/core/tests/test_search.py:89]
- `test_parse_search_query_empty_string` (function) — [saleor/core/tests/test_search.py:93]
- `test_parse_search_query_whitespace_normalization` (function) — [saleor/core/tests/test_search.py:97]
- `test_parse_search_query_preserves_case` (function) — [saleor/core/tests/test_search.py:101]
- `test_parse_search_query_single_word_in_quotes` (function) — [saleor/core/tests/test_search.py:105]
- `test_parse_search_query_quoted_word_with_or` (function) — [saleor/core/tests/test_search.py:110]
- `test_parse_search_query_or_two_plain_words` (function) — [saleor/core/tests/test_search.py:114]
- `test_parse_search_query_or_between_phrases` (function) — [saleor/core/tests/test_search.py:118]
- `test_parse_search_query_negated_word_with_or` (function) — [saleor/core/tests/test_search.py:125]
- `test_parse_search_query_phrase_and_prefix_and_negation` (function) — [saleor/core/tests/test_search.py:131]
- `test_parse_search_query_multiple_or_operators` (function) — [saleor/core/tests/test_search.py:137]
- `test_parse_search_query_or_with_negated_phrase` (function) — [saleor/core/tests/test_search.py:143]
- `test_parse_search_query_quoted_exact_and_prefix_mixed` (function) — [saleor/core/tests/test_search.py:149]
- `test_parse_search_query_multiple_phrases_with_words` (function) — [saleor/core/tests/test_search.py:153]
- `test_parse_search_query_or_chain_with_phrase_in_middle` (function) — [saleor/core/tests/test_search.py:159]
- `test_parse_search_query_negation_before_or` (function) — [saleor/core/tests/test_search.py:165]
- `test_parse_search_query_parentheses_are_stripped` (function) — [saleor/core/tests/test_search.py:170]
- `test_parse_search_query_lowercase_or_is_regular_word` (function) — [saleor/core/tests/test_search.py:177]
- `test_parse_search_query_lowercase_and_is_regular_word` (function) — [saleor/core/tests/test_search.py:182]
- `test_parse_search_query_mixed_case_or_is_regular_word` (function) — [saleor/core/tests/test_search.py:186]
- `test_parse_search_query_unclosed_quote` (function) — [saleor/core/tests/test_search.py:190]
- `test_parse_search_query_whitespace_only_returns_none` (function) — [saleor/core/tests/test_search.py:195]
- `test_parse_search_query_hyphenated_words_preserved` (function) — [saleor/core/tests/test_search.py:199]
- `test_parse_search_query_quoted_phrase_with_metacharacters` (function) — [saleor/core/tests/test_search.py:203]
- `products_for_search` (function) — [saleor/core/tests/test_search.py:208]
- `test_prefix_search_returns_prefix_matches` (function) — [saleor/core/tests/test_search.py:237]
- `test_prefix_search_perfect_match_scores_higher` (function) — [saleor/core/tests/test_search.py:250]
- `test_prefix_search_empty_value_returns_all` (function) — [saleor/core/tests/test_search.py:262]
- _…and 17 more in this file_

**`saleor/core/tests/test_sqs.py`**

- `test_sqs_channel_put_delay_seconds` (function) — [saleor/core/tests/test_sqs.py:22]
- `test_sqs_channel_skips_delay_seconds_for_fifo` (function) — [saleor/core/tests/test_sqs.py:56]

**`saleor/core/tests/test_tasks.py`**

- `test_delete_from_storage_task` (function) — [saleor/core/tests/test_tasks.py:17]
- `test_delete_from_storage_task_file_that_not_exists` (function) — [saleor/core/tests/test_tasks.py:29]
- `test_delete_event_payloads_task` (function) — [saleor/core/tests/test_tasks.py:39]
- `test_delete_files_from_storage_task` (function) — [saleor/core/tests/test_tasks.py:68]
- `test_delete_files_from_storage_task_files_not_existing_files` (function) — [saleor/core/tests/test_tasks.py:85]

**`saleor/core/tests/test_taxes.py`**

- `app_factory` (function) — [saleor/core/tests/test_taxes.py:14]
- `factory` (function) — [saleor/core/tests/test_taxes.py:15]
- `tax_app_factory` (function) — [saleor/core/tests/test_taxes.py:38]
- `factory` (function) — [saleor/core/tests/test_taxes.py:39]
- `tax_app` (function) — [saleor/core/tests/test_taxes.py:58]

**`saleor/core/tests/test_text.py`**

- `test_strip_accents_removes_diacritics` (function) — [saleor/core/tests/test_text.py:4]
- `test_strip_accents_removes_multiple_diacritics` (function) — [saleor/core/tests/test_text.py:8]
- `test_strip_accents_removes_diaeresis` (function) — [saleor/core/tests/test_text.py:12]
- `test_strip_accents_preserves_ascii` (function) — [saleor/core/tests/test_text.py:16]
- `test_strip_accents_empty_string` (function) — [saleor/core/tests/test_text.py:20]

**`saleor/core/tests/test_view.py`**

- `dummy_media_file_request` (function) — [saleor/core/tests/test_view.py:15]
- `test_jwks_can_be_used_to_decode_saleor_token` (function) — [saleor/core/tests/test_view.py:27]
- `test_serve_media_view_serves_as_attachment` (function) — [saleor/core/tests/test_view.py:41]
- `test_serve_media_view_serves_only_when_debug_mode` (function) — [saleor/core/tests/test_view.py:63]

**`saleor/core/tests/test_weight.py`**

- `test_convert_weight` (function) — [saleor/core/tests/test_weight.py:12]
- `test_get_default_weight_unit` (function) — [saleor/core/tests/test_weight.py:24]
- `test_convert_weight_to_default_weight_unit` (function) — [saleor/core/tests/test_weight.py:41]

**`saleor/core/tests/utils.py`**

- `get_site_context_payload` (function) — [saleor/core/tests/utils.py:6]

## How it works

The module's files, as provided to this run:

- `saleor/core/tests/__init__.py` (1 lines)
- `saleor/core/tests/cassettes/test_http_client/test_http_client_disallows_private_ip_ranges[http].yaml` (56 lines)
- `saleor/core/tests/cassettes/test_http_client/test_http_client_disallows_private_ip_ranges[https].yaml` (59 lines)
- `saleor/core/tests/test_anonymize.py` (97 lines)
- `saleor/core/tests/test_auth_backend_default_header.py` (324 lines)
- `saleor/core/tests/test_auth_backend_saleor_header.py` (210 lines)
- `saleor/core/tests/test_core.py` (467 lines)
- `saleor/core/tests/test_dataloaders.py` (38 lines)
- `saleor/core/tests/test_event_payload.py` (39 lines)
- `saleor/core/tests/test_hashers.py` (9 lines)
- `saleor/core/tests/test_http_client.py` (44 lines)
- `saleor/core/tests/test_jwt_manager.py` (122 lines)
- `saleor/core/tests/test_jwt.py` (224 lines)
- `saleor/core/tests/test_metadata_manager.py` (161 lines)
- `saleor/core/tests/test_middleware.py` (79 lines)
- `saleor/core/tests/test_notification.py` (34 lines)
- `saleor/core/tests/test_postgresql_search.py` (128 lines)
- `saleor/core/tests/test_rlimit.py` (159 lines)
- `saleor/core/tests/test_schedules.py` (585 lines)
- `saleor/core/tests/test_search_tasks.py` (55 lines)
- `saleor/core/tests/test_search.py` (512 lines)
- `saleor/core/tests/test_sqs.py` (85 lines)
- `saleor/core/tests/test_tasks.py` (94 lines)
- `saleor/core/tests/test_taxes.py` (62 lines)
- `saleor/core/tests/test_text.py` (21 lines)
- `saleor/core/tests/test_view.py` (84 lines)
- `saleor/core/tests/test_weight.py` (52 lines)
- `saleor/core/tests/utils.py` (11 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/core/utils`, `saleor/webhook`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....user_agent_version`
- `...account.models.Address`
- `...account.models.User`
- `...account.search.update_user_search_vector`
- `...account.tests.fixtures.user.dangerously_get_or_create_superuser`
- `...app.models.App`
- `...attribute.models.AttributeValue`
- `...channel.models.Channel`
- `...checkout.CheckoutAuthorizeStatus`
- `...checkout.models.Checkout`
- `...checkout.search.indexing.update_checkouts_search_vector`
- `...core.notification.validation.validate_and_get_channel`
- `...core.postgres.FlatConcatSearchVector`
- `...discount.models.Promotion`
- `...giftcard.models.GiftCard`
- `...giftcard.models.GiftCardEvent`
- `...graphql.meta.inputs.MetadataInput`
- `...graphql.notifications.error_codes.ExternalNotificationErrorCodes`
- `...graphql.plugins.dataloaders.get_plugin_manager_promise`
- `...order.models.Order`
- `...payment.models.TransactionItem`
- `...permission.enums.get_permissions_from_names`
- `...permission.models.Permission`
- `...private_storage`
- `...product.ProductTypeKind`
- `...product.models.Product`
- `...product.models.ProductChannelListing`
- `...product.models.ProductType`
- `...shipping.models.ShippingZone`
- `...site.PasswordLoginMode`
- `...tests.utils.dummy_editorjs`
- `...webhook.event_types.WebhookEventAsyncType`
- `...webhook.event_types.WebhookEventSyncType`
- `...webhook.models.Webhook`
- `...webhook.models.WebhookEvent`
- `..anonymize.obfuscate_address`
- `..anonymize.obfuscate_email`
- `..anonymize.obfuscate_string`
- `..auth_backend.JSONWebTokenBackend`
- `..hashers.SHA512Base64PBKDF2PasswordHasher`
- `..http_client.HTTPClient`
- `..http_client.HTTPConfig`
- `..jwt_manager.JWTManager`
- `..jwt_manager.get_jwt_manager`
- `..models.EventDelivery`
- `..models.EventDeliveryAttempt`
- `..models.EventPayload`
- `..models.ModelWithMetadata`
- `..notification.utils.LOGO_URL`
- `..postgres.FlatConcat`
- `..postgres.NoValidationSearchVector`
- `..rlimit.RLIMIT_TYPE`
- `..rlimit.validate_and_set_rlimit`
- `..search._sanitize_word`
- `..search.parse_search_query`
- `..search.prefix_search`
- `..sqs.Channel`
- `..storages.S3MediaStorage`
- `..units.WeightUnits`
- `..utils.build_absolute_uri`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `fccd18c33d1c` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
