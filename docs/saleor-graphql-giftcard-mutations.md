## Purpose

`saleor/graphql/giftcard/mutations` (`saleor/graphql/giftcard/mutations`) groups 12 source file(s) exposing 64 top-level declaration(s).

## Public surface

**`saleor/graphql/giftcard/mutations/gift_card_activate.py`**

- `GiftCardActivate` (class) — [saleor/graphql/giftcard/mutations/gift_card_activate.py:18]
- `Arguments` (class) — [saleor/graphql/giftcard/mutations/gift_card_activate.py:21]
- `Meta` (class) — [saleor/graphql/giftcard/mutations/gift_card_activate.py:24]
- `perform_mutation` (function) — [saleor/graphql/giftcard/mutations/gift_card_activate.py:38]

**`saleor/graphql/giftcard/mutations/gift_card_add_note.py`**

- `GiftCardAddNoteInput` (class) — [saleor/graphql/giftcard/mutations/gift_card_add_note.py:19]
- `Meta` (class) — [saleor/graphql/giftcard/mutations/gift_card_add_note.py:22]
- `GiftCardAddNote` (class) — [saleor/graphql/giftcard/mutations/gift_card_add_note.py:26]
- `Arguments` (class) — [saleor/graphql/giftcard/mutations/gift_card_add_note.py:30]
- `Meta` (class) — [saleor/graphql/giftcard/mutations/gift_card_add_note.py:39]
- `clean_input` (function) — [saleor/graphql/giftcard/mutations/gift_card_add_note.py:52]
- `perform_mutation` (function) — [saleor/graphql/giftcard/mutations/gift_card_add_note.py:67]

**`saleor/graphql/giftcard/mutations/gift_card_assign_user.py`**

- `GiftCardAssignUser` (class) — [saleor/graphql/giftcard/mutations/gift_card_assign_user.py:24]
- `Arguments` (class) — [saleor/graphql/giftcard/mutations/gift_card_assign_user.py:27]
- `Meta` (class) — [saleor/graphql/giftcard/mutations/gift_card_assign_user.py:34]
- `perform_mutation` (function) — [saleor/graphql/giftcard/mutations/gift_card_assign_user.py:51]

**`saleor/graphql/giftcard/mutations/gift_card_balance_adjust.py`**

- `GiftCardBalanceAdjust` (class) — [saleor/graphql/giftcard/mutations/gift_card_balance_adjust.py:26]
- `Arguments` (class) — [saleor/graphql/giftcard/mutations/gift_card_balance_adjust.py:29]
- `Meta` (class) — [saleor/graphql/giftcard/mutations/gift_card_balance_adjust.py:41]
- `perform_mutation` (function) — [saleor/graphql/giftcard/mutations/gift_card_balance_adjust.py:55]

**`saleor/graphql/giftcard/mutations/gift_card_create.py`**

- `GiftCardInput` (class) — [saleor/graphql/giftcard/mutations/gift_card_create.py:31]
- `Meta` (class) — [saleor/graphql/giftcard/mutations/gift_card_create.py:66]
- `GiftCardCreateInput` (class) — [saleor/graphql/giftcard/mutations/gift_card_create.py:70]
- `Meta` (class) — [saleor/graphql/giftcard/mutations/gift_card_create.py:100]
- `GiftCardCreate` (class) — [saleor/graphql/giftcard/mutations/gift_card_create.py:104]
- `Arguments` (class) — [saleor/graphql/giftcard/mutations/gift_card_create.py:105]
- `Meta` (class) — [saleor/graphql/giftcard/mutations/gift_card_create.py:110]
- `clean_input` (function) — [saleor/graphql/giftcard/mutations/gift_card_create.py:131]
- `set_created_by_user` (function) — [saleor/graphql/giftcard/mutations/gift_card_create.py:191]
- `clean_expiry_date` (function) — [saleor/graphql/giftcard/mutations/gift_card_create.py:199]
- `clean_balance` (function) — [saleor/graphql/giftcard/mutations/gift_card_create.py:212]
- `post_save_action` (function) — [saleor/graphql/giftcard/mutations/gift_card_create.py:246]
- `assign_gift_card_tags` (function) — [saleor/graphql/giftcard/mutations/gift_card_create.py:281]

**`saleor/graphql/giftcard/mutations/gift_card_deactivate.py`**

- `GiftCardDeactivate` (class) — [saleor/graphql/giftcard/mutations/gift_card_deactivate.py:17]
- `Arguments` (class) — [saleor/graphql/giftcard/mutations/gift_card_deactivate.py:20]
- `Meta` (class) — [saleor/graphql/giftcard/mutations/gift_card_deactivate.py:23]
- `perform_mutation` (function) — [saleor/graphql/giftcard/mutations/gift_card_deactivate.py:37]

**`saleor/graphql/giftcard/mutations/gift_card_delete.py`**

- `GiftCardDelete` (class) — [saleor/graphql/giftcard/mutations/gift_card_delete.py:14]
- `Arguments` (class) — [saleor/graphql/giftcard/mutations/gift_card_delete.py:15]
- `Meta` (class) — [saleor/graphql/giftcard/mutations/gift_card_delete.py:18]
- `post_save_action` (function) — [saleor/graphql/giftcard/mutations/gift_card_delete.py:33]

**`saleor/graphql/giftcard/mutations/gift_card_resend.py`**

- `GiftCardResendInput` (class) — [saleor/graphql/giftcard/mutations/gift_card_resend.py:21]
- `Meta` (class) — [saleor/graphql/giftcard/mutations/gift_card_resend.py:31]
- `GiftCardResend` (class) — [saleor/graphql/giftcard/mutations/gift_card_resend.py:35]
- `Arguments` (class) — [saleor/graphql/giftcard/mutations/gift_card_resend.py:38]
- `Meta` (class) — [saleor/graphql/giftcard/mutations/gift_card_resend.py:43]
- `clean_input` (function) — [saleor/graphql/giftcard/mutations/gift_card_resend.py:56]
- `get_target_email` (function) — [saleor/graphql/giftcard/mutations/gift_card_resend.py:73]
- `get_customer_user` (function) — [saleor/graphql/giftcard/mutations/gift_card_resend.py:79]
- `perform_mutation` (function) — [saleor/graphql/giftcard/mutations/gift_card_resend.py:83]

**`saleor/graphql/giftcard/mutations/gift_card_unassign_user.py`**

- `GiftCardUnassignUser` (class) — [saleor/graphql/giftcard/mutations/gift_card_unassign_user.py:21]
- `Arguments` (class) — [saleor/graphql/giftcard/mutations/gift_card_unassign_user.py:24]
- `Meta` (class) — [saleor/graphql/giftcard/mutations/gift_card_unassign_user.py:27]
- `perform_mutation` (function) — [saleor/graphql/giftcard/mutations/gift_card_unassign_user.py:41]

**`saleor/graphql/giftcard/mutations/gift_card_update.py`**

- `GiftCardUpdateInput` (class) — [saleor/graphql/giftcard/mutations/gift_card_update.py:25]
- `Meta` (class) — [saleor/graphql/giftcard/mutations/gift_card_update.py:35]
- `GiftCardUpdate` (class) — [saleor/graphql/giftcard/mutations/gift_card_update.py:39]
- `Arguments` (class) — [saleor/graphql/giftcard/mutations/gift_card_update.py:40]
- `Meta` (class) — [saleor/graphql/giftcard/mutations/gift_card_update.py:46]
- `clean_expiry_date` (function) — [saleor/graphql/giftcard/mutations/gift_card_update.py:63]
- `clean_balance` (function) — [saleor/graphql/giftcard/mutations/gift_card_update.py:70]
- `clean_tags` (function) — [saleor/graphql/giftcard/mutations/gift_card_update.py:86]
- `perform_mutation` (function) — [saleor/graphql/giftcard/mutations/gift_card_update.py:93]
- `clean_input` (function) — [saleor/graphql/giftcard/mutations/gift_card_update.py:149]

**`saleor/graphql/giftcard/mutations/utils.py`**

- `clean_gift_card` (function) — [saleor/graphql/giftcard/mutations/utils.py:8]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/giftcard/mutations/gift_card_create.py` (298 lines)
- `saleor/graphql/giftcard/mutations/gift_card_resend.py` (108 lines)
- `saleor/graphql/giftcard/mutations/__init__.py` (23 lines)
- `saleor/graphql/giftcard/mutations/gift_card_activate.py` (57 lines)
- `saleor/graphql/giftcard/mutations/gift_card_add_note.py` (81 lines)
- `saleor/graphql/giftcard/mutations/gift_card_assign_user.py` (104 lines)
- `saleor/graphql/giftcard/mutations/gift_card_balance_adjust.py` (109 lines)
- `saleor/graphql/giftcard/mutations/gift_card_deactivate.py` (55 lines)
- `saleor/graphql/giftcard/mutations/gift_card_delete.py` (35 lines)
- `saleor/graphql/giftcard/mutations/gift_card_unassign_user.py` (70 lines)
- `saleor/graphql/giftcard/mutations/gift_card_update.py` (166 lines)
- `saleor/graphql/giftcard/mutations/utils.py` (18 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: `saleor/graphql/giftcard/tests/mutations`

Internal dependencies named in the source:

- `....account.models.User`
- `....core.tracing.traced_atomic_transaction`
- `....core.utils.events.call_event`
- `....core.utils.promo_code.generate_promo_code`
- `....core.utils.promo_code.is_available_promo_code`
- `....core.utils.validators.is_date_in_future`
- `....giftcard.error_codes.GiftCardErrorCode`
- `....giftcard.events`
- `....giftcard.lock_objects.gift_card_qs_select_for_update`
- `....giftcard.models`
- `....giftcard.notifications.send_gift_card_notification`
- `....giftcard.utils.GiftCardCannotAssign`
- `....giftcard.utils.activate_gift_card`
- `....giftcard.utils.assign_gift_card_to_user`
- `....giftcard.utils.deactivate_gift_card`
- `....giftcard.utils.is_gift_card_expired`
- `....permission.enums.GiftcardPermissions`
- `....webhook.event_types.WebhookEventAsyncType`
- `...account.types.User`
- `...app.dataloaders.get_app_promise`
- `...core.ResolveInfo`
- `...core.descriptions.ADDED_IN_323`
- `...core.descriptions.DEPRECATED_IN_3X_INPUT`
- `...core.doc_category.DOC_CATEGORY_GIFT_CARDS`
- `...core.mutations.BaseMutation`
- `...core.mutations.DeprecatedModelMutation`
- `...core.mutations.ModelDeleteMutation`
- `...core.scalars.Date`
- `...core.scalars.Decimal`
- `...core.scalars.PositiveDecimal`
- `...core.types.BaseInputObjectType`
- `...core.types.GiftCardError`
- `...core.types.NonNullList`
- `...core.types.PriceInput`
- `...core.utils.WebhookEventInfo`
- `...core.validators.validate_price_precision`
- `...core.validators.validate_required_string_field`
- `...meta.inputs.MetadataInput`
- `...meta.inputs.MetadataInputDescription`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `...utils.validators.check_for_duplicates`
- `..types.GiftCard`
- `..types.GiftCardEvent`
- `.gift_card_activate.GiftCardActivate`
- `.gift_card_add_note.GiftCardAddNote`
- `.gift_card_assign_user.GiftCardAssignUser`
- `.gift_card_balance_adjust.GiftCardBalanceAdjust`
- `.gift_card_create.GiftCardCreate`
- `.gift_card_create.GiftCardInput`
- `.gift_card_deactivate.GiftCardDeactivate`
- `.gift_card_delete.GiftCardDelete`
- `.gift_card_resend.GiftCardResend`
- `.gift_card_unassign_user.GiftCardUnassignUser`
- `.gift_card_update.GiftCardUpdate`
- `.utils.clean_gift_card`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `613825357890` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
