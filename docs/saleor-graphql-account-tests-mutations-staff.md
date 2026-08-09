## Purpose

`saleor/graphql/account/tests/mutations/staff` (`saleor/graphql/account/tests/mutations/staff`) groups 13 source file(s) exposing 100 top-level declaration(s).

## Public surface

**`saleor/graphql/account/tests/mutations/staff/test_address_create.py`**

- `test_create_address_mutation` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_create.py:43]
- `test_create_address_mutation_trigger_webhook` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_create.py:76]
- `test_create_address_mutation_the_oldest_address_is_deleted` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_create.py:116]
- `test_create_address_validation_fails` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_create.py:155]
- `test_create_address_skip_validation` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_create.py:182]
- `test_create_address_country_area_cleared_by_default` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_create.py:212]
- `test_create_address_country_area_preserved_when_flag_enabled` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_create.py:243]

**`saleor/graphql/account/tests/mutations/staff/test_address_delete.py`**

- `test_address_delete_mutation` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_delete.py:25]
- `test_address_delete_mutation_trigger_webhook` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_delete.py:48]
- `test_address_delete_mutation_as_app` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_delete.py:83]
- `test_customer_delete_address_for_other` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_delete.py:100]

**`saleor/graphql/account/tests/mutations/staff/test_address_set_default.py`**

- `test_set_default_address` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_set_default.py:26]

**`saleor/graphql/account/tests/mutations/staff/test_address_update.py`**

- `test_address_update_mutation` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_update.py:32]
- `test_address_update_mutation_trigger_webhook` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_update.py:59]
- `test_address_update_mutation_no_user_assigned` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_update.py:101]
- `test_customer_update_address_for_other` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_update.py:128]
- `test_address_update_skip_validation` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_update.py:143]
- `test_address_update_address_with_skipped_validation` (function) — [saleor/graphql/account/tests/mutations/staff/test_address_update.py:175]

**`saleor/graphql/account/tests/mutations/staff/test_customer_create.py`**

- `test_customer_create` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_create.py:87]
- `test_customer_create_as_app` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_create.py:202]
- `test_customer_create_send_password_with_url` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_create.py:320]
- `test_customer_create_empty_metadata_key` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_create.py:367]
- `test_customer_create_without_send_password` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_create.py:414]
- `test_customer_create_with_invalid_url` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_create.py:428]
- `test_customer_create_with_not_allowed_url` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_create.py:445]
- `test_customer_create_with_upper_case_email` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_create.py:464]
- `test_customer_create_with_non_unique_external_reference` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_create.py:483]
- `test_customer_create_webhook_event_triggered` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_create.py:508]
- `test_customer_create_race_condition` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_create.py:550]
- `create_existing_customer` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_create.py:579]

**`saleor/graphql/account/tests/mutations/staff/test_customer_delete.py`**

- `test_customer_delete` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_delete.py:32]
- `test_customer_delete_trigger_webhook` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_delete.py:66]
- `test_customer_delete_by_app` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_delete.py:109]
- `test_customer_delete_errors` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_delete.py:142]
- `test_customer_delete_by_external_reference` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_delete.py:154]
- `test_delete_customer_by_both_id_and_external_reference` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_delete.py:180]
- `test_delete_customer_by_external_reference_not_existing` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_delete.py:201]

**`saleor/graphql/account/tests/mutations/staff/test_customer_update.py`**

- `test_customer_update` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:66]
- `test_customer_data_update_sends_customer_updated_webhook` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:181]
- `test_metadata_update_with_changed_legacy_webhook_on` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:224]
- `test_metadata_update_with_changed_legacy_webhook_off` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:269]
- `test_metadata_and_customer_data_update_sends_both_webhooks` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:311]
- `test_customer_update_by_external_reference` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:376]
- `test_update_customer_by_both_id_and_external_reference` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:407]
- `test_update_customer_by_external_reference_not_existing` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:429]
- `test_update_customer_with_non_unique_external_reference` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:453]
- `test_customer_update_generates_event_when_changing_email` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:497]
- `test_customer_update_generates_event_when_deactivating` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:540]
- `test_customer_update_generates_event_when_activating` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:561]
- `test_customer_update_generates_event_when_deactivating_as_app` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:584]
- `test_customer_update_generates_event_when_activating_as_app` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:604]
- `test_customer_update_without_any_changes_generates_no_event` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:626]
- `test_customer_update_generates_event_when_changing_email_by_app` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:651]
- `test_customer_update_existing_user_does_not_merge_with_existing_account` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:677]
- `test_customer_update_assign_gift_cards_and_orders` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:761]
- `test_customer_update_trigger_gift_card_search_vector_update` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:811]
- `test_customer_confirm_assign_gift_cards_and_orders` (function) — [saleor/graphql/account/tests/mutations/staff/test_customer_update.py:871]

**`saleor/graphql/account/tests/mutations/staff/test_staff_create.py`**

- `test_staff_create` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_create.py:67]
- `test_promote_customer_to_staff_user` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_create.py:148]
- `test_staff_create_trigger_webhook` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_create.py:204]
- `test_staff_create_app_no_permission` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_create.py:267]
- `test_staff_create_out_of_scope_group` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_create.py:297]
- `test_staff_create_send_password_with_url` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_create.py:402]
- `test_staff_create_without_send_password` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_create.py:441]
- `test_staff_create_with_invalid_url` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_create.py:455]
- `test_staff_create_with_not_allowed_url` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_create.py:475]
- `test_staff_create_with_upper_case_email` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_create.py:495]

**`saleor/graphql/account/tests/mutations/staff/test_staff_delete.py`**

- `test_staff_delete` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_delete.py:38]
- `test_staff_delete_with_orders` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_delete.py:53]
- `test_staff_delete_trigger_webhook` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_delete.py:77]
- `test_staff_delete_with_avatar` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_delete.py:124]
- `test_staff_delete_app_no_permission` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_delete.py:148]
- `test_staff_delete_out_of_scope_user` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_delete.py:161]
- `test_staff_delete_left_not_manageable_permissions` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_delete.py:193]
- `test_staff_delete_all_permissions_manageable` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_delete.py:252]
- `test_user_delete_errors` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_delete.py:293]
- `test_staff_delete_errors` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_delete.py:309]
- `test_staff_update_errors` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_delete.py:321]

**`saleor/graphql/account/tests/mutations/staff/test_staff_update.py`**

- `test_staff_update` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_update.py:56]
- `test_staff_update_metadata` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_update.py:76]
- `test_staff_update_private_metadata` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_update.py:100]
- `test_staff_update_trigger_webhook` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_update.py:127]
- `test_staff_update_email` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_update.py:176]
- `test_staff_update_name_field` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_update.py:198]
- `test_staff_update_app_no_permission` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_update.py:222]
- `test_staff_update_groups_and_permissions` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_update.py:237]
- `test_staff_update_out_of_scope_user` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_update.py:286]
- `test_staff_update_out_of_scope_groups` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_update.py:319]
- `test_staff_update_duplicated_input_items` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_update.py:398]
- `test_staff_update_doesnt_change_existing_avatar` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_update.py:449]
- `test_staff_update_deactivate_with_manage_staff_left_not_manageable_perms` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_update.py:475]
- `test_staff_update_deactivate_with_manage_staff_all_perms_manageable` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_update.py:536]
- `test_staff_update_update_email_assign_gift_cards_and_orders` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_update.py:579]
- `test_staff_update_trigger_gift_card_search_vector_update` (function) — [saleor/graphql/account/tests/mutations/staff/test_staff_update.py:618]

**`saleor/graphql/account/tests/mutations/staff/test_user_avatar_delete.py`**

- `test_user_avatar_delete_mutation_permission` (function) — [saleor/graphql/account/tests/mutations/staff/test_user_avatar_delete.py:17]
- `test_user_avatar_delete_mutation` (function) — [saleor/graphql/account/tests/mutations/staff/test_user_avatar_delete.py:27]

**`saleor/graphql/account/tests/mutations/staff/test_user_avatar_update.py`**

- `test_user_avatar_update_mutation_permission` (function) — [saleor/graphql/account/tests/mutations/staff/test_user_avatar_update.py:33]
- `test_user_avatar_update_mutation` (function) — [saleor/graphql/account/tests/mutations/staff/test_user_avatar_update.py:46]
- `test_user_avatar_update_mutation_image_exists` (function) — [saleor/graphql/account/tests/mutations/staff/test_user_avatar_update.py:75]
- `test_user_avatar_update_mutation_file_size_exceeds_limit` (function) — [saleor/graphql/account/tests/mutations/staff/test_user_avatar_update.py:108]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/account/tests/mutations/staff/__init__.py` (1 lines)
- `saleor/graphql/account/tests/mutations/staff/test_address_create.py` (274 lines)
- `saleor/graphql/account/tests/mutations/staff/test_address_delete.py` (108 lines)
- `saleor/graphql/account/tests/mutations/staff/test_address_set_default.py` (57 lines)
- `saleor/graphql/account/tests/mutations/staff/test_address_update.py` (207 lines)
- `saleor/graphql/account/tests/mutations/staff/test_customer_create.py` (598 lines)
- `saleor/graphql/account/tests/mutations/staff/test_customer_delete.py` (217 lines)
- `saleor/graphql/account/tests/mutations/staff/test_customer_update.py` (913 lines)
- `saleor/graphql/account/tests/mutations/staff/test_staff_create.py` (511 lines)
- `saleor/graphql/account/tests/mutations/staff/test_staff_delete.py` (346 lines)
- `saleor/graphql/account/tests/mutations/staff/test_staff_update.py` (654 lines)
- `saleor/graphql/account/tests/mutations/staff/test_user_avatar_delete.py` (44 lines)
- `saleor/graphql/account/tests/mutations/staff/test_user_avatar_update.py` (130 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `......account.error_codes.AccountErrorCode`
- `......account.events`
- `......account.models`
- `......account.models.Address`
- `......account.models.Group`
- `......account.models.User`
- `......account.notifications.get_default_user_payload`
- `......checkout.AddressType`
- `......core.notify.NotifyEventType`
- `......core.tests.utils.get_site_context_payload`
- `......core.tokens.password_reset_token_generator`
- `......core.utils.json_serializer.CustomJsonEncoder`
- `......core.utils.url.prepare_url`
- `......giftcard.models.GiftCard`
- `......giftcard.search.update_gift_cards_search_vector`
- `......permission.enums.AccountPermissions`
- `......permission.enums.OrderPermissions`
- `......product.tests.utils.create_image`
- `......tests.race_condition`
- `......thumbnail.models.Thumbnail`
- `......webhook.event_types.WebhookEventAsyncType`
- `......webhook.payloads.generate_meta`
- `......webhook.payloads.generate_requestor`
- `.....tests.utils.assert_no_permission`
- `.....tests.utils.get_graphql_content`
- `....mutations.staff.CustomerDelete`
- `....mutations.staff.StaffDelete`
- `....mutations.staff.StaffUpdate`
- `....mutations.staff.base.UserDelete`
- `....tests.utils.convert_dict_keys_to_camel_case`
- `..utils.generate_address_webhook_call_args`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `b38a4d284280` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
