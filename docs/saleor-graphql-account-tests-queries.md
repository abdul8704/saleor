## Purpose

`saleor/graphql/account/tests/queries` (`saleor/graphql/account/tests/queries`) groups 17 source file(s) exposing 154 top-level declaration(s).

## Public surface

**`saleor/graphql/account/tests/queries/test_account_events.py`**

- `test_account_events_are_properly_restricted` (function) — [saleor/graphql/account/tests/queries/test_account_events.py:32]
- `test_account_event_customer_account_was_created` (function) — [saleor/graphql/account/tests/queries/test_account_events.py:76]
- `test_account_event_customer_account_was_activated` (function) — [saleor/graphql/account/tests/queries/test_account_events.py:99]
- `test_account_event_customer_account_was_deactivated` (function) — [saleor/graphql/account/tests/queries/test_account_events.py:122]
- `test_account_event_sent_password_reset_email_to_customer_event` (function) — [saleor/graphql/account/tests/queries/test_account_events.py:145]
- `test_account_event_customer_reset_password_from_link_event` (function) — [saleor/graphql/account/tests/queries/test_account_events.py:170]
- `test_account_event_customer_placed_order_event_resolves_properly` (function) — [saleor/graphql/account/tests/queries/test_account_events.py:193]
- `test_account_event_customer_added_to_note_order_event_resolves_properly` (function) — [saleor/graphql/account/tests/queries/test_account_events.py:221]
- `test_account_event_customer_deleted_event_resolves_properly` (function) — [saleor/graphql/account/tests/queries/test_account_events.py:251]
- `test_event_staff_user_assigned_new_name_to_customer_event_resolves_properly` (function) — [saleor/graphql/account/tests/queries/test_account_events.py:274]
- `test_account_event_staff_user_assigned_email_to_customer_event_resolves_properly` (function) — [saleor/graphql/account/tests/queries/test_account_events.py:297]
- `test_account_event_created_by_removed_app` (function) — [saleor/graphql/account/tests/queries/test_account_events.py:320]

**`saleor/graphql/account/tests/queries/test_address_validation_rules.py`**

- `test_address_validation_rules` (function) — [saleor/graphql/account/tests/queries/test_address_validation_rules.py:43]
- `test_address_validation_rules_with_country_area` (function) — [saleor/graphql/account/tests/queries/test_address_validation_rules.py:75]
- `test_address_validation_rules_for_EU` (function) — [saleor/graphql/account/tests/queries/test_address_validation_rules.py:116]
- `test_address_validation_rules_fields_in_camel_case` (function) — [saleor/graphql/account/tests/queries/test_address_validation_rules.py:130]

**`saleor/graphql/account/tests/queries/test_address.py`**

- `test_address_query_as_owner` (function) — [saleor/graphql/account/tests/queries/test_address.py:24]
- `test_address_query_as_not_owner` (function) — [saleor/graphql/account/tests/queries/test_address.py:33]
- `test_address_query_as_app_with_permission` (function) — [saleor/graphql/account/tests/queries/test_address.py:43]
- `test_address_query_as_app_without_permission` (function) — [saleor/graphql/account/tests/queries/test_address.py:57]
- `test_address_query_as_anonymous_user` (function) — [saleor/graphql/account/tests/queries/test_address.py:65]
- `test_address_query_invalid_id` (function) — [saleor/graphql/account/tests/queries/test_address.py:71]
- `test_address_query_with_invalid_object_type` (function) — [saleor/graphql/account/tests/queries/test_address.py:84]
- `test_customer_query_address_federation` (function) — [saleor/graphql/account/tests/queries/test_address.py:107]
- `test_customer_query_other_user_address_federation` (function) — [saleor/graphql/account/tests/queries/test_address.py:131]
- `test_staff_query_other_user_address_federation` (function) — [saleor/graphql/account/tests/queries/test_address.py:151]
- `test_staff_query_other_user_address_with_permission_federation` (function) — [saleor/graphql/account/tests/queries/test_address.py:171]
- `test_app_query_address_federation` (function) — [saleor/graphql/account/tests/queries/test_address.py:196]
- `test_app_no_permission_query_address_federation` (function) — [saleor/graphql/account/tests/queries/test_address.py:223]
- `test_unauthenticated_query_address_federation` (function) — [saleor/graphql/account/tests/queries/test_address.py:239]

**`saleor/graphql/account/tests/queries/test_customers_filtering.py`**

- `query_customer_with_filter` (function) — [saleor/graphql/account/tests/queries/test_customers_filtering.py:12]
- `test_query_customer_members_with_filter_search` (function) — [saleor/graphql/account/tests/queries/test_customers_filtering.py:48]
- `test_customers_search_sorted_by_rank_exact_match_prioritized` (function) — [saleor/graphql/account/tests/queries/test_customers_filtering.py:87]
- `test_query_customers_with_filter_by_one_id` (function) — [saleor/graphql/account/tests/queries/test_customers_filtering.py:162]
- `test_query_customers_with_filter_by_multiple_ids` (function) — [saleor/graphql/account/tests/queries/test_customers_filtering.py:189]
- `test_query_customers_with_filter_by_empty_list` (function) — [saleor/graphql/account/tests/queries/test_customers_filtering.py:219]
- `test_query_customers_with_filter_by_not_existing_id` (function) — [saleor/graphql/account/tests/queries/test_customers_filtering.py:244]
- `test_query_customers_with_filter_placed_orders` (function) — [saleor/graphql/account/tests/queries/test_customers_filtering.py:276]
- `test_query_customers_with_filter_date_joined_and_updated_at` (function) — [saleor/graphql/account/tests/queries/test_customers_filtering.py:322]
- `test_query_customers_with_filter_placed_orders_` (function) — [saleor/graphql/account/tests/queries/test_customers_filtering.py:350]
- `test_query_customers_with_filter_metadata` (function) — [saleor/graphql/account/tests/queries/test_customers_filtering.py:379]
- `test_query_customers_search_without_duplications` (function) — [saleor/graphql/account/tests/queries/test_customers_filtering.py:402]
- `test_query_customers_with_permission_manage_orders` (function) — [saleor/graphql/account/tests/queries/test_customers_filtering.py:432]
- `test_query_customer_members_pagination_with_filter_search` (function) — [saleor/graphql/account/tests/queries/test_customers_filtering.py:475]

**`saleor/graphql/account/tests/queries/test_customers_sorting.py`**

- `test_query_customers_with_sort` (function) — [saleor/graphql/account/tests/queries/test_customers_sorting.py:37]
- `customers_for_pagination` (function) — [saleor/graphql/account/tests/queries/test_customers_sorting.py:112]
- `test_query_customers_pagination_with_sort` (function) — [saleor/graphql/account/tests/queries/test_customers_sorting.py:153]

**`saleor/graphql/account/tests/queries/test_customers_where_filtering.py`**

- `test_customers_filter_by_ids` (function) — [saleor/graphql/account/tests/queries/test_customers_where_filtering.py:30]
- `test_customers_filter_by_date_joined` (function) — [saleor/graphql/account/tests/queries/test_customers_where_filtering.py:89]
- `test_customers_filter_by_updated_at` (function) — [saleor/graphql/account/tests/queries/test_customers_where_filtering.py:164]
- `test_customers_filter_by_metadata` (function) — [saleor/graphql/account/tests/queries/test_customers_where_filtering.py:213]
- `test_customers_filter_by_placed_orders_at` (function) — [saleor/graphql/account/tests/queries/test_customers_where_filtering.py:280]
- `test_customers_filter_by_email` (function) — [saleor/graphql/account/tests/queries/test_customers_where_filtering.py:334]
- `test_customers_filter_by_is_active` (function) — [saleor/graphql/account/tests/queries/test_customers_where_filtering.py:374]
- `test_customers_filter_by_addresses` (function) — [saleor/graphql/account/tests/queries/test_customers_where_filtering.py:433]
- `test_customers_filter_by_number_of_orders` (function) — [saleor/graphql/account/tests/queries/test_customers_where_filtering.py:496]
- `test_customers_filter_by_first_name` (function) — [saleor/graphql/account/tests/queries/test_customers_where_filtering.py:537]
- `test_customers_filter_by_last_name` (function) — [saleor/graphql/account/tests/queries/test_customers_where_filtering.py:582]

**`saleor/graphql/account/tests/queries/test_customers.py`**

- `customers_for_pagination` (function) — [saleor/graphql/account/tests/queries/test_customers.py:34]
- `test_query_customers_pagination_with_sort` (function) — [saleor/graphql/account/tests/queries/test_customers.py:75]
- `test_query_customers_root_level_filter` (function) — [saleor/graphql/account/tests/queries/test_customers.py:120]

**`saleor/graphql/account/tests/queries/test_me.py`**

- `test_me_query` (function) — [saleor/graphql/account/tests/queries/test_me.py:47]
- `test_me_user_permissions_query` (function) — [saleor/graphql/account/tests/queries/test_me.py:54]
- `test_me_query_anonymous_client` (function) — [saleor/graphql/account/tests/queries/test_me.py:68]
- `test_me_query_customer_can_not_see_note` (function) — [saleor/graphql/account/tests/queries/test_me.py:74]
- `test_me_query_checkout` (function) — [saleor/graphql/account/tests/queries/test_me.py:100]
- `test_me_query_checkouts_do_not_trigger_sync_tax_webhooks` (function) — [saleor/graphql/account/tests/queries/test_me.py:171]
- `test_me_query_checkouts_calculate_flat_taxes` (function) — [saleor/graphql/account/tests/queries/test_me.py:217]
- `test_me_query_orders_do_not_trigger_sync_tax_webhooks` (function) — [saleor/graphql/account/tests/queries/test_me.py:313]
- `test_me_query_orders_calculate_flat_taxes` (function) — [saleor/graphql/account/tests/queries/test_me.py:355]
- `test_me_query_checkout_with_inactive_channel` (function) — [saleor/graphql/account/tests/queries/test_me.py:389]
- `test_me_query_checkouts_with_channel` (function) — [saleor/graphql/account/tests/queries/test_me.py:404]
- `test_me_checkout_tokens_without_channel_param` (function) — [saleor/graphql/account/tests/queries/test_me.py:448]
- `test_me_checkout_tokens_without_channel_param_inactive_channel` (function) — [saleor/graphql/account/tests/queries/test_me.py:465]
- `test_me_checkout_tokens_with_channel` (function) — [saleor/graphql/account/tests/queries/test_me.py:483]
- `test_me_checkout_tokens_with_inactive_channel` (function) — [saleor/graphql/account/tests/queries/test_me.py:501]
- `test_me_checkout_tokens_with_not_existing_channel` (function) — [saleor/graphql/account/tests/queries/test_me.py:519]
- `test_me_with_cancelled_fulfillments` (function) — [saleor/graphql/account/tests/queries/test_me.py:535]
- `test_me_query_stored_payment_methods` (function) — [saleor/graphql/account/tests/queries/test_me.py:600]
- `test_me_orders_pagination_has_previous_page` (function) — [saleor/graphql/account/tests/queries/test_me.py:711]
- `test_me_orders_where_filter_by_ids` (function) — [saleor/graphql/account/tests/queries/test_me.py:749]
- `test_me_orders_where_filter_by_status` (function) — [saleor/graphql/account/tests/queries/test_me.py:773]
- `test_me_orders_where_filter_excludes_draft_orders` (function) — [saleor/graphql/account/tests/queries/test_me.py:798]
- `test_me_orders_where_filter_by_number` (function) — [saleor/graphql/account/tests/queries/test_me.py:819]
- `test_me_orders_where_filter_by_metadata` (function) — [saleor/graphql/account/tests/queries/test_me.py:839]

**`saleor/graphql/account/tests/queries/test_permission_group.py`**

- `test_staff_query_group_federation` (function) — [saleor/graphql/account/tests/queries/test_permission_group.py:19]
- `test_app_query_group_federation` (function) — [saleor/graphql/account/tests/queries/test_permission_group.py:47]
- `test_app_no_permission_query_group_federation` (function) — [saleor/graphql/account/tests/queries/test_permission_group.py:75]
- `test_client_query_group_federation` (function) — [saleor/graphql/account/tests/queries/test_permission_group.py:92]
- `test_unauthenticated_query_group_federation` (function) — [saleor/graphql/account/tests/queries/test_permission_group.py:110]

**`saleor/graphql/account/tests/queries/test_permission_groups_filtering.py`**

- `test_permission_groups_query` (function) — [saleor/graphql/account/tests/queries/test_permission_groups_filtering.py:33]
- `test_permission_groups_query_with_filter_by_ids` (function) — [saleor/graphql/account/tests/queries/test_permission_groups_filtering.py:56]
- `test_permission_groups_no_permission_to_perform` (function) — [saleor/graphql/account/tests/queries/test_permission_groups_filtering.py:82]

**`saleor/graphql/account/tests/queries/test_permission_groups_sorting.py`**

- `test_permission_group_with_sort` (function) — [saleor/graphql/account/tests/queries/test_permission_groups_sorting.py:32]

**`saleor/graphql/account/tests/queries/test_permission_groups.py`**

- `permission_groups_for_pagination` (function) — [saleor/graphql/account/tests/queries/test_permission_groups.py:8]
- `test_permission_groups_pagination_with_sorting` (function) — [saleor/graphql/account/tests/queries/test_permission_groups.py:58]
- `test_permission_groups_pagination_with_filtering` (function) — [saleor/graphql/account/tests/queries/test_permission_groups.py:81]

**`saleor/graphql/account/tests/queries/test_staff_users_filtering.py`**

- `query_staff_users_with_filter` (function) — [saleor/graphql/account/tests/queries/test_staff_users_filtering.py:10]
- `test_query_staff_members_with_filter_status` (function) — [saleor/graphql/account/tests/queries/test_staff_users_filtering.py:32]
- `test_query_staff_members_with_filter_by_ids` (function) — [saleor/graphql/account/tests/queries/test_staff_users_filtering.py:57]
- `test_query_staff_members_with_filter_search` (function) — [saleor/graphql/account/tests/queries/test_staff_users_filtering.py:98]
- `staff_for_search` (function) — [saleor/graphql/account/tests/queries/test_staff_users_filtering.py:146]
- `test_query_staff_members_pagination_with_filter_search` (function) — [saleor/graphql/account/tests/queries/test_staff_users_filtering.py:230]

**`saleor/graphql/account/tests/queries/test_staff_users_sorting.py`**

- `test_query_staff_members_with_sort` (function) — [saleor/graphql/account/tests/queries/test_staff_users_sorting.py:34]

**`saleor/graphql/account/tests/queries/test_user.py`**

- `test_query_customer_user` (function) — [saleor/graphql/account/tests/queries/test_user.py:124]
- `test_query_customer_user_with_orders` (function) — [saleor/graphql/account/tests/queries/test_user.py:227]
- `test_query_customer_user_with_orders_no_manage_orders_perm` (function) — [saleor/graphql/account/tests/queries/test_user.py:269]
- `test_query_customer_user_app` (function) — [saleor/graphql/account/tests/queries/test_user.py:304]
- `test_query_customer_user_with_orders_by_app_no_manage_orders_perm` (function) — [saleor/graphql/account/tests/queries/test_user.py:339]
- `test_query_customer_user_with_orders_restricted_access_to_channel` (function) — [saleor/graphql/account/tests/queries/test_user.py:374]
- `test_query_staff_user` (function) — [saleor/graphql/account/tests/queries/test_user.py:421]
- `test_query_staff_user_with_order_and_without_manage_orders_perm` (function) — [saleor/graphql/account/tests/queries/test_user.py:501]
- `test_query_staff_user_with_orders_and_manage_orders_perm` (function) — [saleor/graphql/account/tests/queries/test_user.py:542]
- `test_query_user_by_email_address` (function) — [saleor/graphql/account/tests/queries/test_user.py:594]
- `test_query_user_by_email_address_case_insensitive` (function) — [saleor/graphql/account/tests/queries/test_user.py:607]
- `test_query_user_by_external_reference` (function) — [saleor/graphql/account/tests/queries/test_user.py:620]
- `test_query_user_by_id_and_email` (function) — [saleor/graphql/account/tests/queries/test_user.py:641]
- `test_customer_can_not_see_other_users_data` (function) — [saleor/graphql/account/tests/queries/test_user.py:658]
- `test_user_query_anonymous_user` (function) — [saleor/graphql/account/tests/queries/test_user.py:665]
- `test_user_query_permission_manage_users_get_customer` (function) — [saleor/graphql/account/tests/queries/test_user.py:671]
- `test_user_query_as_app` (function) — [saleor/graphql/account/tests/queries/test_user.py:684]
- `test_user_query_permission_manage_users_get_staff` (function) — [saleor/graphql/account/tests/queries/test_user.py:695]
- `test_user_query_permission_manage_staff_get_customer` (function) — [saleor/graphql/account/tests/queries/test_user.py:707]
- `test_user_query_permission_manage_staff_get_staff` (function) — [saleor/graphql/account/tests/queries/test_user.py:719]
- `test_user_query_invalid_id` (function) — [saleor/graphql/account/tests/queries/test_user.py:733]
- `test_user_query_object_with_given_id_does_not_exist` (function) — [saleor/graphql/account/tests/queries/test_user.py:747]
- `test_user_query_object_with_invalid_object_type` (function) — [saleor/graphql/account/tests/queries/test_user.py:760]
- `test_query_user_avatar_with_size_and_format_proxy_url_returned` (function) — [saleor/graphql/account/tests/queries/test_user.py:786]
- `test_query_user_avatar_with_size_proxy_url_returned` (function) — [saleor/graphql/account/tests/queries/test_user.py:816]
- `test_query_user_avatar_with_size_thumbnail_url_returned` (function) — [saleor/graphql/account/tests/queries/test_user.py:841]
- `test_query_user_avatar_original_size_custom_format_provided_original_image_returned` (function) — [saleor/graphql/account/tests/queries/test_user.py:872]
- `test_query_user_avatar_no_size_value` (function) — [saleor/graphql/account/tests/queries/test_user.py:901]
- `test_query_user_avatar_no_image` (function) — [saleor/graphql/account/tests/queries/test_user.py:927]
- `test_query_user_channel_accessibility_restricted_access_to_channels` (function) — [saleor/graphql/account/tests/queries/test_user.py:959]
- `test_query_user_channel_accessibility_not_restricted_access` (function) — [saleor/graphql/account/tests/queries/test_user.py:986]
- `test_user_with_cancelled_fulfillments` (function) — [saleor/graphql/account/tests/queries/test_user.py:1016]
- `test_staff_query_user_by_id_for_federation` (function) — [saleor/graphql/account/tests/queries/test_user.py:1070]
- `test_staff_query_user_by_email_for_federation` (function) — [saleor/graphql/account/tests/queries/test_user.py:1099]
- `test_staff_query_user_by_id_without_permission_for_federation` (function) — [saleor/graphql/account/tests/queries/test_user.py:1128]
- `test_staff_query_user_by_email_without_permission_for_federation` (function) — [saleor/graphql/account/tests/queries/test_user.py:1146]
- `test_customer_query_self_by_id_for_federation` (function) — [saleor/graphql/account/tests/queries/test_user.py:1163]
- `test_customer_query_self_by_email_for_federation` (function) — [saleor/graphql/account/tests/queries/test_user.py:1188]
- `test_customer_query_user_by_id_for_federation` (function) — [saleor/graphql/account/tests/queries/test_user.py:1213]
- `test_customer_query_user_by_email_for_federation` (function) — [saleor/graphql/account/tests/queries/test_user.py:1234]
- _…and 6 more in this file_

**`saleor/graphql/account/tests/queries/test_users.py`**

- `test_query_customers` (function) — [saleor/graphql/account/tests/queries/test_users.py:8]
- `test_query_staff` (function) — [saleor/graphql/account/tests/queries/test_users.py:35]
- `test_who_can_see_user` (function) — [saleor/graphql/account/tests/queries/test_users.py:77]
- `test_user_orders_where_filter_and_unfiltered_in_single_query` (function) — [saleor/graphql/account/tests/queries/test_users.py:134]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/account/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/account/tests/queries/test_account_events.py` (340 lines)
- `saleor/graphql/account/tests/queries/test_address_validation_rules.py` (149 lines)
- `saleor/graphql/account/tests/queries/test_address.py` (252 lines)
- `saleor/graphql/account/tests/queries/test_customers_filtering.py` (544 lines)
- `saleor/graphql/account/tests/queries/test_customers_sorting.py` (177 lines)
- `saleor/graphql/account/tests/queries/test_customers_where_filtering.py` (611 lines)
- `saleor/graphql/account/tests/queries/test_customers.py` (147 lines)
- `saleor/graphql/account/tests/queries/test_me.py` (861 lines)
- `saleor/graphql/account/tests/queries/test_permission_group.py` (125 lines)
- `saleor/graphql/account/tests/queries/test_permission_groups_filtering.py` (91 lines)
- `saleor/graphql/account/tests/queries/test_permission_groups_sorting.py` (51 lines)
- `saleor/graphql/account/tests/queries/test_permission_groups.py` (98 lines)
- `saleor/graphql/account/tests/queries/test_staff_users_filtering.py` (253 lines)
- `saleor/graphql/account/tests/queries/test_staff_users_sorting.py` (74 lines)
- `saleor/graphql/account/tests/queries/test_user.py` (1459 lines)
- `saleor/graphql/account/tests/queries/test_users.py` (174 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....account.events`
- `.....account.models.Address`
- `.....account.models.Group`
- `.....account.models.User`
- `.....account.search.update_user_search_vector`
- `.....account.tests.fixtures.user.dangerously_create_test_user`
- `.....channel.models.Channel`
- `.....checkout.calculations._fetch_checkout_prices_if_expired`
- `.....checkout.fetch.fetch_checkout_lines`
- `.....order.OrderOrigin`
- `.....order.OrderStatus`
- `.....order.models.FulfillmentStatus`
- `.....order.models.Order`
- `.....tax.calculations.order.update_order_prices_with_flat_rates`
- `.....thumbnail.models.Thumbnail`
- `....core.enums.ThumbnailFormatEnum`
- `....core.utils.to_global_id_or_none`
- `....payment.enums.TokenizedPaymentFlowEnum`
- `....tests.utils.assert_graphql_error_with_message`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `1adc125b699f` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
