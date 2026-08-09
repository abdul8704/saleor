## Purpose

`saleor/giftcard/tests` (`saleor/giftcard/tests`) groups 12 source file(s) exposing 71 top-level declaration(s).

## Public surface

**`saleor/giftcard/tests/fixtures/giftcard_event.py`**

- `gift_card_event` (function) — [saleor/giftcard/tests/fixtures/giftcard_event.py:11]

**`saleor/giftcard/tests/fixtures/giftcard_tag.py`**

- `gift_card_tag_list` (function) — [saleor/giftcard/tests/fixtures/giftcard_tag.py:7]

**`saleor/giftcard/tests/fixtures/giftcard.py`**

- `gift_card` (function) — [saleor/giftcard/tests/fixtures/giftcard.py:13]
- `gift_card_with_metadata` (function) — [saleor/giftcard/tests/fixtures/giftcard.py:27]
- `gift_card_expiry_date` (function) — [saleor/giftcard/tests/fixtures/giftcard.py:39]
- `gift_card_used` (function) — [saleor/giftcard/tests/fixtures/giftcard.py:55]
- `gift_card_created_by_staff` (function) — [saleor/giftcard/tests/fixtures/giftcard.py:71]
- `gift_card_list` (function) — [saleor/giftcard/tests/fixtures/giftcard.py:85]
- `gift_cards_for_benchmarks` (function) — [saleor/giftcard/tests/fixtures/giftcard.py:111]

**`saleor/giftcard/tests/test_events.py`**

- `test_gift_card_balance_adjusted_event` (function) — [saleor/giftcard/tests/test_events.py:11]
- `test_gift_card_assigned_event_records_prev_and_new` (function) — [saleor/giftcard/tests/test_events.py:31]
- `test_gift_card_unassigned_event_records_prev` (function) — [saleor/giftcard/tests/test_events.py:49]

**`saleor/giftcard/tests/test_gateway.py`**

- `test_charge_creates_used_in_order_event` (function) — [saleor/giftcard/tests/test_gateway.py:17]
- `test_charge_does_not_create_event_on_insufficient_funds` (function) — [saleor/giftcard/tests/test_gateway.py:60]
- `test_refund_creates_refunded_in_order_event` (function) — [saleor/giftcard/tests/test_gateway.py:86]

**`saleor/giftcard/tests/test_lock_objects.py`**

- `test_gift_card_qs_select_for_update_returns_giftcard_queryset` (function) — [saleor/giftcard/tests/test_lock_objects.py:5]

**`saleor/giftcard/tests/test_models.py`**

- `test_gift_card_can_be_assigned_to_customer` (function) — [saleor/giftcard/tests/test_models.py:10]
- `test_deleting_assigned_customer_is_protected` (function) — [saleor/giftcard/tests/test_models.py:24]
- `test_current_balance_cannot_be_negative` (function) — [saleor/giftcard/tests/test_models.py:37]

**`saleor/giftcard/tests/test_notifications.py`**

- `test_get_default_gift_card_payload` (function) — [saleor/giftcard/tests/test_notifications.py:11]
- `test_send_gift_card_notification` (function) — [saleor/giftcard/tests/test_notifications.py:22]

**`saleor/giftcard/tests/test_tasks.py`**

- `test_update_gift_cards_search_vector_task` (function) — [saleor/giftcard/tests/test_tasks.py:11]
- `test_deactivate_expired_cards_task` (function) — [saleor/giftcard/tests/test_tasks.py:24]
- `test_deactivate_expired_cards_task_cards_not_deactivated` (function) — [saleor/giftcard/tests/test_tasks.py:68]

**`saleor/giftcard/tests/test_utils.py`**

- `test_add_gift_card_code_to_checkout` (function) — [saleor/giftcard/tests/test_utils.py:45]
- `test_add_gift_card_code_to_checkout_without_email` (function) — [saleor/giftcard/tests/test_utils.py:58]
- `test_add_gift_card_code_to_checkout_inactive_card` (function) — [saleor/giftcard/tests/test_utils.py:69]
- `test_add_gift_card_code_to_checkout_expired_card` (function) — [saleor/giftcard/tests/test_utils.py:84]
- `test_add_gift_card_code_to_checkout_invalid_currency` (function) — [saleor/giftcard/tests/test_utils.py:101]
- `test_add_gift_card_code_to_checkout_used_gift_card` (function) — [saleor/giftcard/tests/test_utils.py:116]
- `test_remove_gift_card_code_from_checkout` (function) — [saleor/giftcard/tests/test_utils.py:133]
- `test_remove_gift_card_code_from_checkout_no_checkout_gift_cards` (function) — [saleor/giftcard/tests/test_utils.py:145]
- `test_calculate_expiry_settings` (function) — [saleor/giftcard/tests/test_utils.py:167]
- `test_calculate_expiry_settings_for_never_expire_settings` (function) — [saleor/giftcard/tests/test_utils.py:187]
- `test_gift_cards_create` (function) — [saleor/giftcard/tests/test_utils.py:199]
- `test_gift_cards_create_expiry_date_set` (function) — [saleor/giftcard/tests/test_utils.py:299]
- `test_gift_cards_create_multiple_quantity` (function) — [saleor/giftcard/tests/test_utils.py:376]
- `test_gift_cards_create_trigger_webhook` (function) — [saleor/giftcard/tests/test_utils.py:425]
- `test_get_gift_card_lines` (function) — [saleor/giftcard/tests/test_utils.py:504]
- `test_get_gift_card_lines_no_gift_card_lines` (function) — [saleor/giftcard/tests/test_utils.py:524]
- `test_get_non_shippable_gift_card_lines` (function) — [saleor/giftcard/tests/test_utils.py:537]
- `test_get_non_shippable_gift_card_lines_no_gift_card_lines` (function) — [saleor/giftcard/tests/test_utils.py:554]
- `test_fulfill_non_shippable_gift_cards` (function) — [saleor/giftcard/tests/test_utils.py:568]
- `test_fulfill_non_shippable_gift_cards_line_with_allocation` (function) — [saleor/giftcard/tests/test_utils.py:608]
- `test_fulfill_gift_card_lines` (function) — [saleor/giftcard/tests/test_utils.py:653]
- `test_fulfill_gift_card_lines_lack_of_stock` (function) — [saleor/giftcard/tests/test_utils.py:709]
- `test_deactivate_order_gift_cards` (function) — [saleor/giftcard/tests/test_utils.py:732]
- `test_deactivate_order_gift_cards_no_order_gift_cards` (function) — [saleor/giftcard/tests/test_utils.py:755]
- `test_order_has_gift_card_lines_true` (function) — [saleor/giftcard/tests/test_utils.py:772]
- `test_order_has_gift_card_lines_false` (function) — [saleor/giftcard/tests/test_utils.py:777]
- `test_assign_user_gift_cards` (function) — [saleor/giftcard/tests/test_utils.py:781]
- `test_assign_user_gift_cards_no_gift_cards_to_assign` (function) — [saleor/giftcard/tests/test_utils.py:816]
- `test_is_gift_card_expired_never_expired_gift_card` (function) — [saleor/giftcard/tests/test_utils.py:831]
- `test_is_gift_card_expired_true` (function) — [saleor/giftcard/tests/test_utils.py:842]
- `test_is_gift_card_expired_false` (function) — [saleor/giftcard/tests/test_utils.py:860]
- `test_assign_sets_user_and_email` (function) — [saleor/giftcard/tests/test_utils.py:872]
- `test_assign_blocked_when_used_in_order` (function) — [saleor/giftcard/tests/test_utils.py:886]
- `test_assign_detaches_clean_checkout` (function) — [saleor/giftcard/tests/test_utils.py:896]
- `test_assign_bumps_last_change_of_detached_checkout` (function) — [saleor/giftcard/tests/test_utils.py:912]
- `test_assign_blocked_when_checkout_has_transaction` (function) — [saleor/giftcard/tests/test_utils.py:931]
- `test_deactivate_assigned_gift_cards_detaches_and_deactivates` (function) — [saleor/giftcard/tests/test_utils.py:944]
- `test_deactivate_assigned_gift_cards_ignores_other_users` (function) — [saleor/giftcard/tests/test_utils.py:967]
- `test_deactivate_assigned_gift_cards_no_event_for_already_inactive` (function) — [saleor/giftcard/tests/test_utils.py:988]
- `test_deactivate_assigned_gift_cards_deactivates_card_activated_before_detach` (function) — [saleor/giftcard/tests/test_utils.py:1009]
- _…and 7 more in this file_

## How it works

The module's files, as provided to this run:

- `saleor/giftcard/tests/__init__.py` (1 lines)
- `saleor/giftcard/tests/fixtures/__init__.py` (3 lines)
- `saleor/giftcard/tests/fixtures/giftcard_event.py` (35 lines)
- `saleor/giftcard/tests/fixtures/giftcard_tag.py` (9 lines)
- `saleor/giftcard/tests/fixtures/giftcard.py` (147 lines)
- `saleor/giftcard/tests/test_events.py` (58 lines)
- `saleor/giftcard/tests/test_gateway.py` (132 lines)
- `saleor/giftcard/tests/test_lock_objects.py` (11 lines)
- `saleor/giftcard/tests/test_models.py` (43 lines)
- `saleor/giftcard/tests/test_notifications.py` (64 lines)
- `saleor/giftcard/tests/test_tasks.py` (89 lines)
- `saleor/giftcard/tests/test_utils.py` (1164 lines)

## Interactions

- Imports from: `saleor/giftcard`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....GiftCardEvents`
- `....core.prices.Money`
- `....graphql.giftcard.tests.benchmark.GIFT_CARD_COUNT_IN_BENCHMARKS`
- `...GiftCardEvents`
- `...GiftCardLineData`
- `...account.notifications.get_default_user_payload`
- `...checkout.error_codes.CheckoutErrorCode`
- `...core.TimePeriodType`
- `...core.exceptions.GiftCardNotApplicable`
- `...core.notify.NotifyEventType`
- `...core.tests.utils.get_site_context_payload`
- `...core.utils.json_serializer.CustomJsonEncoder`
- `...core.utils.promo_code.InvalidPromoCode`
- `...events`
- `...giftcard.GiftCardEvents`
- `...giftcard.const.GIFT_CARD_PAYMENT_GATEWAY_ID`
- `...giftcard.models.GiftCardEvent`
- `...graphql.core.utils.to_global_id_or_none`
- `...models.GiftCard`
- `...models.GiftCardEvent`
- `...models.GiftCardTag`
- `...order.OrderEvents`
- `...order.models.OrderLine`
- `...payment.TransactionAction`
- `...payment.TransactionEventType`
- `...payment.models.TransactionEvent`
- `...plugins.manager.get_plugins_manager`
- `...site.GiftCardSettingsExpiryType`
- `...webhook.event_types.WebhookEventAsyncType`
- `...webhook.payloads.generate_meta`
- `...webhook.payloads.generate_requestor`
- `..lock_objects.gift_card_qs_select_for_update`
- `..models.GiftCard`
- `..models.GiftCardEvent`
- `..notifications.get_default_gift_card_payload`
- `..notifications.send_gift_card_notification`
- `..tasks.deactivate_expired_cards_task`
- `..tasks.update_gift_cards_search_vector_task`
- `.giftcard.*  # noqa: F403`
- `.giftcard_event.*  # noqa: F403`
- `.giftcard_tag.*  # noqa: F403`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `aa56ad176337` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
