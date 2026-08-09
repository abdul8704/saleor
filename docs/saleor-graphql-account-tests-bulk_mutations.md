## Purpose

`saleor/graphql/account/tests/bulk_mutations` (`saleor/graphql/account/tests/bulk_mutations`) groups 5 source file(s) exposing 39 top-level declaration(s).

## Public surface

**`saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_delete.py`**

- `test_delete_customers` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_delete.py:18]
- `test_delete_customers_trigger_webhooks` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_delete.py:62]
- `test_delete_customers_by_app` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_delete.py:92]

**`saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py`**

- `test_customers_bulk_update_using_ids` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:54]
- `test_stocks_bulk_update_send_stock_updated_event` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:113]
- `test_customers_bulk_update_generate_events_when_deactivating` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:159]
- `test_customers_bulk_update_generate_events_when_name_change` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:207]
- `test_customers_bulk_update_generate_events_when_email_change` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:258]
- `test_customers_bulk_update_match_orders_and_gift_card_when_confirmed` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:310]
- `test_customers_bulk_update_using_external_refs` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:361]
- `test_customers_bulk_update_when_no_id_or_external_ref_provided` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:406]
- `test_customers_bulk_update_when_invalid_id_provided` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:435]
- `test_customers_bulk_update_when_customer_not_exists` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:464]
- `test_customers_bulk_update_correct_fields_validation` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:494]
- `test_customers_bulk_update_with_address` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:526]
- `test_customers_bulk_update_with_address_when_no_default` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:582]
- `test_customers_bulk_update_with_invalid_address` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:632]
- `test_customers_bulk_update_with_duplicated_external_ref` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:683]
- `test_customers_bulk_update_metadata` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:725]
- `test_customers_bulk_update_metadata_empty_key_in_one_input` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:788]
- `test_customers_bulk_update_trigger_gift_card_search_vector_update` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:859]
- `test_customers_bulk_update_skip_address_validation` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:920]
- `test_bulk_metadata_update_with_changed_legacy_webhook_on` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:977]
- `test_bulk_metadata_update_with_changed_legacy_webhook_off` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:1032]
- `test_bulk_metadata_and_customer_data_update_sends_both_webhooks` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:1084]
- `test_customer_update_existing_user_does_not_merge_with_existing_account` (function) — [saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py:1150]

**`saleor/graphql/account/tests/bulk_mutations/test_staff_bulk_delete.py`**

- `test_delete_staff_members` (function) — [saleor/graphql/account/tests/bulk_mutations/test_staff_bulk_delete.py:26]
- `test_delete_staff_members_exceeding_max_input_size` (function) — [saleor/graphql/account/tests/bulk_mutations/test_staff_bulk_delete.py:52]
- `test_delete_staff_members_trigger_webhook` (function) — [saleor/graphql/account/tests/bulk_mutations/test_staff_bulk_delete.py:80]
- `test_delete_staff_members_app_no_permission` (function) — [saleor/graphql/account/tests/bulk_mutations/test_staff_bulk_delete.py:112]
- `test_delete_staff_members_left_not_manageable_permissions` (function) — [saleor/graphql/account/tests/bulk_mutations/test_staff_bulk_delete.py:132]
- `test_delete_staff_members_superuser_can_delete_when_delete_left_notmanageable_perms` (function) — [saleor/graphql/account/tests/bulk_mutations/test_staff_bulk_delete.py:187]
- `test_delete_staff_members_all_permissions_manageable` (function) — [saleor/graphql/account/tests/bulk_mutations/test_staff_bulk_delete.py:232]
- `test_delete_staff_members_out_of_scope_users` (function) — [saleor/graphql/account/tests/bulk_mutations/test_staff_bulk_delete.py:281]
- `test_delete_staff_members_superuser_can_delete__out_of_scope_users` (function) — [saleor/graphql/account/tests/bulk_mutations/test_staff_bulk_delete.py:340]

**`saleor/graphql/account/tests/bulk_mutations/test_user_bulk_set_active.py`**

- `test_staff_bulk_set_active` (function) — [saleor/graphql/account/tests/bulk_mutations/test_user_bulk_set_active.py:19]
- `test_staff_bulk_set_not_active` (function) — [saleor/graphql/account/tests/bulk_mutations/test_user_bulk_set_active.py:40]
- `test_change_active_status_for_superuser` (function) — [saleor/graphql/account/tests/bulk_mutations/test_user_bulk_set_active.py:61]
- `test_change_active_status_for_himself` (function) — [saleor/graphql/account/tests/bulk_mutations/test_user_bulk_set_active.py:85]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/account/tests/bulk_mutations/__init__.py` (1 lines)
- `saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_delete.py` (131 lines)
- `saleor/graphql/account/tests/bulk_mutations/test_customer_bulk_update.py` (1251 lines)
- `saleor/graphql/account/tests/bulk_mutations/test_staff_bulk_delete.py` (389 lines)
- `saleor/graphql/account/tests/bulk_mutations/test_user_bulk_set_active.py` (104 lines)

## Interactions

- Imports from: `saleor/graphql/account/bulk_mutations`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....account.error_codes.AccountErrorCode`
- `.....account.error_codes.CustomerBulkUpdateErrorCode`
- `.....account.events.CustomerEvents`
- `.....account.models`
- `.....account.models.Group`
- `.....account.models.User`
- `.....giftcard.models.GiftCard`
- `.....giftcard.search.update_gift_cards_search_vector`
- `.....permission.enums.AccountPermissions`
- `.....permission.enums.OrderPermissions`
- `....core.enums.ErrorPolicyEnum`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `..utils.convert_dict_keys_to_camel_case`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `74b242a1348f` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
