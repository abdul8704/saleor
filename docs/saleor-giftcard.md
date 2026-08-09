## Purpose

`saleor/giftcard` (`saleor/giftcard`) groups 11 source file(s) exposing 72 top-level declaration(s).

## Public surface

**`saleor/giftcard/__init__.py`**

- `GiftCardEvents` (class) — [saleor/giftcard/__init__.py:9]
- `GiftCardLineData` (class) — [saleor/giftcard/__init__.py:50]

**`saleor/giftcard/error_codes.py`**

- `GiftCardErrorCode` (class) — [saleor/giftcard/error_codes.py:4]

**`saleor/giftcard/events.py`**

- `gift_card_issued_event` (function) — [saleor/giftcard/events.py:14]
- `gift_card_balance_adjusted_event` (function) — [saleor/giftcard/events.py:33]
- `gift_card_assigned_event` (function) — [saleor/giftcard/events.py:57]
- `gift_card_unassigned_event` (function) — [saleor/giftcard/events.py:78]
- `gift_cards_issued_event` (function) — [saleor/giftcard/events.py:97]
- `gift_card_sent_event` (function) — [saleor/giftcard/events.py:121]
- `gift_card_resent_event` (function) — [saleor/giftcard/events.py:133]
- `gift_card_balance_reset_event` (function) — [saleor/giftcard/events.py:145]
- `gift_card_expiry_date_updated_event` (function) — [saleor/giftcard/events.py:168]
- `gift_card_tags_updated_event` (function) — [saleor/giftcard/events.py:186]
- `gift_card_activated_event` (function) — [saleor/giftcard/events.py:206]
- `gift_card_deactivated_event` (function) — [saleor/giftcard/events.py:219]
- `gift_cards_activated_event` (function) — [saleor/giftcard/events.py:232]
- `gift_cards_deactivated_event` (function) — [saleor/giftcard/events.py:249]
- `gift_card_note_added_event` (function) — [saleor/giftcard/events.py:266]
- `gift_cards_used_in_order_event` (function) — [saleor/giftcard/events.py:278]
- `gift_card_refunded_in_order_event` (function) — [saleor/giftcard/events.py:304]
- `gift_cards_bought_event` (function) — [saleor/giftcard/events.py:328]

**`saleor/giftcard/gateway.py`**

- `GiftCardPaymentGatewayDataSchema` (class) — [saleor/giftcard/gateway.py:37]
- `GiftCardPaymentGatewayException` (class) — [saleor/giftcard/gateway.py:48]
- `transaction_initialize_session_with_gift_card_payment_method` (function) — [saleor/giftcard/gateway.py:55]
- `attach_app_identifier_to_transaction` (function) — [saleor/giftcard/gateway.py:98]
- `validate_transaction_session_data` (function) — [saleor/giftcard/gateway.py:106]
- `validate_and_get_gift_card` (function) — [saleor/giftcard/gateway.py:126]
- `attach_gift_card_to_transaction` (function) — [saleor/giftcard/gateway.py:154]
- `detach_gift_card_from_previous_checkout_transactions` (function) — [saleor/giftcard/gateway.py:179]
- `charge_gift_card` (function) — [saleor/giftcard/gateway.py:227]
- `charge_gift_card_transactions` (function) — [saleor/giftcard/gateway.py:249]
- `cancel_gift_card_transaction` (function) — [saleor/giftcard/gateway.py:348]
- `refund_gift_card_transaction` (function) — [saleor/giftcard/gateway.py:384]

**`saleor/giftcard/lock_objects.py`**

- `gift_card_qs_select_for_update` (function) — [saleor/giftcard/lock_objects.py:6]

**`saleor/giftcard/models.py`**

- `GiftCardTag` (class) — [saleor/giftcard/models.py:19]
- `Meta` (class) — [saleor/giftcard/models.py:22]
- `GiftCardQueryset` (class) — [saleor/giftcard/models.py:34]
- `active` (function) — [saleor/giftcard/models.py:35]
- `GiftCard` (class) — [saleor/giftcard/models.py:45]
- `Meta` (class) — [saleor/giftcard/models.py:131]
- `display_code` (function) — [saleor/giftcard/models.py:151]
- `GiftCardEvent` (class) — [saleor/giftcard/models.py:155]
- `Meta` (class) — [saleor/giftcard/models.py:173]

**`saleor/giftcard/notifications.py`**

- `send_gift_card_notification` (function) — [saleor/giftcard/notifications.py:13]
- `get_default_gift_card_payload` (function) — [saleor/giftcard/notifications.py:49]

**`saleor/giftcard/search.py`**

- `prepare_gift_card_search_vector_value` (function) — [saleor/giftcard/search.py:19]
- `mark_gift_cards_search_index_as_dirty` (function) — [saleor/giftcard/search.py:43]
- `mark_gift_cards_search_index_as_dirty_by_users` (function) — [saleor/giftcard/search.py:49]
- `update_gift_cards_search_vector` (function) — [saleor/giftcard/search.py:61]

**`saleor/giftcard/tasks.py`**

- `deactivate_expired_cards_task` (function) — [saleor/giftcard/tasks.py:17]
- `update_gift_cards_search_vector_task` (function) — [saleor/giftcard/tasks.py:32]

**`saleor/giftcard/utils.py`**

- `add_gift_card_code_to_checkout` (function) — [saleor/giftcard/utils.py:42]
- `remove_gift_card_code_from_checkout_or_error` (function) — [saleor/giftcard/utils.py:87]
- `GiftCardCannotAssign` (class) — [saleor/giftcard/utils.py:102]
- `assign_gift_card_to_user` (function) — [saleor/giftcard/utils.py:106]
- `deactivate_assigned_gift_cards` (function) — [saleor/giftcard/utils.py:146]
- `deactivate_gift_card` (function) — [saleor/giftcard/utils.py:185]
- `activate_gift_card` (function) — [saleor/giftcard/utils.py:192]
- `fulfill_non_shippable_gift_cards` (function) — [saleor/giftcard/utils.py:199]
- `get_non_shippable_gift_card_lines` (function) — [saleor/giftcard/utils.py:215]
- `get_gift_card_lines` (function) — [saleor/giftcard/utils.py:223]
- `fulfill_gift_card_lines` (function) — [saleor/giftcard/utils.py:228]
- `gift_cards_create` (function) — [saleor/giftcard/utils.py:275]
- `calculate_expiry_date` (function) — [saleor/giftcard/utils.py:331]
- `send_gift_cards_to_customer` (function) — [saleor/giftcard/utils.py:342]
- `deactivate_order_gift_cards` (function) — [saleor/giftcard/utils.py:364]
- `order_has_gift_card_lines` (function) — [saleor/giftcard/utils.py:379]
- `assign_user_gift_cards` (function) — [saleor/giftcard/utils.py:383]
- `is_gift_card_expired` (function) — [saleor/giftcard/utils.py:388]
- `get_user_gift_cards` (function) — [saleor/giftcard/utils.py:394]
- `project_remaining_balance` (function) — [saleor/giftcard/utils.py:404]
- `sweep_expired_gift_cards` (function) — [saleor/giftcard/utils.py:409]

## How it works

The module's files, as provided to this run:

- `saleor/giftcard/__init__.py` (54 lines)
- `saleor/giftcard/models.py` (174 lines)
- `saleor/giftcard/search.py` (69 lines)
- `saleor/giftcard/const.py` (4 lines)
- `saleor/giftcard/error_codes.py` (13 lines)
- `saleor/giftcard/events.py` (345 lines)
- `saleor/giftcard/gateway.py` (448 lines)
- `saleor/giftcard/lock_objects.py` (11 lines)
- `saleor/giftcard/notifications.py` (55 lines)
- `saleor/giftcard/tasks.py` (39 lines)
- `saleor/giftcard/utils.py` (411 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core`, `saleor/plugins/openid_connect`, `saleor/core/db`
- Imported by: `saleor/giftcard/tests`, `saleor/graphql/giftcard/tests/queries`

Internal dependencies named in the source:

- `..account.models.User`
- `..account.notifications.get_default_user_payload`
- `..app.models.App`
- `..celeryconf.app`
- `..checkout.error_codes.CheckoutErrorCode`
- `..checkout.models.Checkout`
- `..core.db.connection.allow_writer`
- `..core.db.fields.MoneyField`
- `..core.exceptions.GiftCardNotApplicable`
- `..core.models.ModelWithMetadata`
- `..core.notification.utils.get_site_context`
- `..core.notify.NotifyEventType`
- `..core.notify.NotifyHandler`
- `..core.postgres.FlatConcatSearchVector`
- `..core.postgres.NoValidationSearchVector`
- `..core.prices.quantize_price`
- `..core.tracing.traced_atomic_transaction`
- `..core.utils.events.call_event`
- `..core.utils.json_serializer.CustomJsonEncoder`
- `..core.utils.promo_code.generate_promo_code`
- `..core.utils.promo_code.InvalidPromoCode`
- `..events`
- `..GiftCardEvents`
- `..GiftCardLineData`
- `..graphql.core.utils.to_global_id_or_none`
- `..order.actions.create_fulfillments`
- `..order.actions.OrderFulfillmentLineInfo`
- `..order.models.FulfillmentLine`
- `..order.models.Order`
- `..order.models.OrderLine`
- `..payment.models.Payment`
- `..payment.models.TransactionEvent`
- `..payment.models.TransactionItem`
- `..payment.PaymentMethodType`
- `..payment.TransactionAction`
- `..payment.TransactionEventType`
- `..permission.enums.GiftcardPermissions`
- `..plugins.manager.PluginsManager`
- `..product.models.ProductVariant`
- `..site.GiftCardSettingsExpiryType`
- `..site.models.SiteSettings`
- `.events.gift_card_refunded_in_order_event`
- `.events.gift_cards_deactivated_event`
- `.events.gift_cards_used_in_order_event`
- `.lock_objects.gift_card_qs_select_for_update`
- `.models.GiftCard`
- `.models.GiftCardEvent`
- `.notifications.send_gift_card_notification`
- `.search.mark_gift_cards_search_index_as_dirty`
- `.search.update_gift_cards_search_vector`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `623886ea231b` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
