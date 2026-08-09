## Purpose

`saleor/graphql/giftcard/tests/mutations` (`saleor/graphql/giftcard/tests/mutations`) groups 11 source file(s) exposing 79 top-level declaration(s).

## Public surface

**`saleor/graphql/giftcard/tests/mutations/test_gift_card_activate.py`**

- `test_activate_gift_card_by_staff` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_activate.py:41]
- `test_activate_gift_card_by_app` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_activate.py:76]
- `test_activate_gift_card_by_customer` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_activate.py:103]
- `test_activate_gift_card_without_premissions` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_activate.py:123]
- `test_activate_active_gift_card` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_activate.py:134]
- `test_activate_expired_gift_card` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_activate.py:155]
- `test_activate_gift_card_trigger_webhook` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_activate.py:196]

**`saleor/graphql/giftcard/tests/mutations/test_gift_card_add_note.py`**

- `test_gift_card_add_note_as_staff_user` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_add_note.py:42]
- `test_gift_card_add_note_as_app` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_add_note.py:82]
- `test_gift_card_add_note_fail_on_empty_message` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_add_note.py:130]
- `test_gift_card_add_note_expired_card` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_add_note.py:160]
- `test_gift_card_add_note_trigger_webhook` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_add_note.py:208]

**`saleor/graphql/giftcard/tests/mutations/test_gift_card_assign_user.py`**

- `test_assign_user` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_assign_user.py:45]
- `test_reassign_records_previous` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_assign_user.py:74]
- `test_assigned_to_user_fields_require_manage_users` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_assign_user.py:106]
- `test_assign_blocked_when_used` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_assign_user.py:132]
- `test_requires_permission` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_assign_user.py:152]
- `test_empty_gift_card_id_is_rejected` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_assign_user.py:163]
- `test_empty_user_id_is_rejected` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_assign_user.py:189]

**`saleor/graphql/giftcard/tests/mutations/test_gift_card_balance_adjust.py`**

- `test_increase_balance` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_balance_adjust.py:34]
- `test_increase_above_initial_bumps_initial` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_balance_adjust.py:56]
- `test_decrease_clamps_to_zero` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_balance_adjust.py:75]
- `test_zero_amount_is_rejected` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_balance_adjust.py:94]
- `test_requires_permission` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_balance_adjust.py:117]
- `test_empty_id_is_rejected` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_balance_adjust.py:130]

**`saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py`**

- `test_create_never_expiry_gift_card` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:96]
- `test_create_gift_card_by_app` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:193]
- `test_create_gift_card_by_customer` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:266]
- `test_create_gift_card_no_premissions` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:296]
- `test_create_gift_card_with_too_many_decimal_places_in_balance_amount` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:324]
- `test_create_gift_card_with_malformed_email` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:370]
- `test_create_gift_card_lack_of_channel` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:416]
- `test_create_gift_card_with_zero_balance_amount` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:463]
- `test_create_gift_card_with_expiry_date` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:511]
- `test_create_gift_card_with_expiry_date_type_invalid` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:592]
- `test_create_gift_card_trigger_webhook` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:643]
- `test_create_gift_card_with_email_triggers_gift_card_sent_webhook` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:714]
- `test_create_gift_card_with_code` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:792]
- `test_create_gift_card_with_to_short_code` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:831]
- `test_create_gift_card_with_public_metadata` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:890]
- `test_create_gift_card_with_private_metadata` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:930]
- `test_create_gift_card_with_private_and_public_metadata` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:970]
- `test_create_with_assigned_to` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:1013]
- `test_create_with_assigned_to_not_found` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py:1049]

**`saleor/graphql/giftcard/tests/mutations/test_gift_card_deactivate.py`**

- `test_deactivate_gift_card_by_staff` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_deactivate.py:38]
- `test_deactivate_gift_card_by_app` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_deactivate.py:71]
- `test_deactivate_gift_card_by_customer` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_deactivate.py:104]
- `test_deactivate_gift_card_without_premissions` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_deactivate.py:124]
- `test_deactivate_inactive_gift_card` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_deactivate.py:135]
- `test_deactivate_gift_card_trigger_webhook` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_deactivate.py:171]

**`saleor/graphql/giftcard/tests/mutations/test_gift_card_delete.py`**

- `test_delete_gift_card_by_staff` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_delete.py:25]
- `test_delete_gift_card_by_staff_no_permission` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_delete.py:47]
- `test_delete_gift_card_by_app` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_delete.py:58]
- `test_delete_gift_card_by_customer` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_delete.py:80]
- `test_delete_gift_card_trigger_webhook` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_delete.py:94]

**`saleor/graphql/giftcard/tests/mutations/test_gift_card_resend.py`**

- `test_resend_gift_card` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_resend.py:56]
- `test_resend_gift_card_as_app` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_resend.py:109]
- `test_update_gift_card_no_permission` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_resend.py:159]
- `test_resend_gift_card_malformed_email` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_resend.py:189]
- `test_resend_gift_card_triggers_gift_card_sent_event` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_resend.py:236]
- `test_resend_gift_card_expired_card` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_resend.py:307]

**`saleor/graphql/giftcard/tests/mutations/test_gift_card_unassign_user.py`**

- `test_unassign_clears_fields` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_unassign_user.py:38]
- `test_requires_permission` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_unassign_user.py:73]
- `test_assigned_to_user_fields_require_manage_users` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_unassign_user.py:90]
- `test_empty_id_is_rejected` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_unassign_user.py:115]

**`saleor/graphql/giftcard/tests/mutations/test_gift_card_update.py`**

- `test_update_gift_card` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_update.py:97]
- `test_update_gift_card_by_app` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_update.py:218]
- `test_update_gift_card_by_customer` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_update.py:344]
- `test_update_gift_card_balance` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_update.py:367]
- `test_update_gift_card_change_to_never_expire` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_update.py:451]
- `test_update_used_gift_card_to_expiry_date` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_update.py:516]
- `test_update_used_gift_card_to_never_expired` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_update.py:561]
- `test_update_gift_card_date_in_past` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_update.py:599]
- `test_update_gift_card_expired_card` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_update.py:639]
- `test_update_gift_card_expiry_date_not_changed` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_update.py:687]
- `test_update_gift_card_duplicated_tags_item` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_update.py:732]
- `test_update_gift_card_trigger_webhook` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_update.py:772]
- `test_update_gift_card_metadata_empty` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_update.py:861]
- `test_update_gift_card_metadata_existed` (function) — [saleor/graphql/giftcard/tests/mutations/test_gift_card_update.py:913]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/giftcard/tests/mutations/__init__.py` (1 lines)
- `saleor/graphql/giftcard/tests/mutations/test_gift_card_activate.py` (250 lines)
- `saleor/graphql/giftcard/tests/mutations/test_gift_card_add_note.py` (262 lines)
- `saleor/graphql/giftcard/tests/mutations/test_gift_card_assign_user.py` (211 lines)
- `saleor/graphql/giftcard/tests/mutations/test_gift_card_balance_adjust.py` (143 lines)
- `saleor/graphql/giftcard/tests/mutations/test_gift_card_create.py` (1081 lines)
- `saleor/graphql/giftcard/tests/mutations/test_gift_card_deactivate.py` (223 lines)
- `saleor/graphql/giftcard/tests/mutations/test_gift_card_delete.py` (139 lines)
- `saleor/graphql/giftcard/tests/mutations/test_gift_card_resend.py` (350 lines)
- `saleor/graphql/giftcard/tests/mutations/test_gift_card_unassign_user.py` (132 lines)
- `saleor/graphql/giftcard/tests/mutations/test_gift_card_update.py` (963 lines)

## Interactions

- Imports from: `saleor/graphql/giftcard/mutations`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....core.utils.json_serializer.CustomJsonEncoder`
- `.....giftcard.GiftCardEvents`
- `.....giftcard.error_codes.GiftCardErrorCode`
- `.....giftcard.models.GiftCard`
- `.....giftcard.models.GiftCardEvent`
- `.....giftcard.models.GiftCardTag`
- `.....giftcard.utils.assign_gift_card_to_user`
- `.....permission.enums.AccountPermissions`
- `.....webhook.event_types.WebhookEventAsyncType`
- `.....webhook.payloads.generate_meta`
- `.....webhook.payloads.generate_requestor`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `7304a707390e` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
