## Purpose

`saleor/graphql/giftcard/tests/queries` (`saleor/graphql/giftcard/tests/queries`) groups 9 source file(s) exposing 61 top-level declaration(s).

## Public surface

**`saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py`**

- `test_query_filter_gift_cards_by_tags` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py:40]
- `test_query_filter_gift_cards_by_products` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py:73]
- `test_query_filter_gift_cards_by_used_by_user` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py:114]
- `test_query_filter_gift_cards_by_assigned_to_user` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py:144]
- `test_query_filter_gift_cards_by_currency` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py:179]
- `test_query_filter_gift_cards_by_is_active` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py:224]
- `test_query_filter_gift_cards_used` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py:269]
- `test_query_filter_gift_cards_by_current_balance_no_currency_given` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py:303]
- `test_query_filter_gift_cards_by_current_balance` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py:346]
- `test_query_filter_gift_cards_by_initial_balance_no_currency_given` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py:383]
- `test_query_filter_gift_cards_by_initial_balance` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py:426]
- `test_query_filter_gift_cards_by_code` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py:463]
- `test_query_filter_gift_cards_by_code_no_gift_card` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py:487]
- `test_query_filter_gift_cards_by_metadata` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py:510]
- `test_query_filter_gift_cards_by_created_by_email` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py:532]

**`saleor/graphql/giftcard/tests/queries/test_gift_card_search.py`**

- `test_query_gift_cards_with_search` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_search.py:51]
- `test_gift_cards_search_sorted_by_rank_exact_match_prioritized` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_search.py:79]

**`saleor/graphql/giftcard/tests/queries/test_gift_card_sorting.py`**

- `test_sorting_gift_cards_by_current_balance` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_sorting.py:30]
- `test_sorting_gift_cards_by_current_balance_no_currency_in_filter` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_sorting.py:67]
- `test_sorting_gift_cards_by_product` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_sorting.py:100]
- `test_sorting_gift_cards_by_used_by` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_sorting.py:145]
- `test_sorting_gift_cards_by_created_at` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_sorting.py:187]

**`saleor/graphql/giftcard/tests/queries/test_gift_card_tags_filtering.py`**

- `test_filter_gift_card_tags_by_name` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_tags_filtering.py:30]

**`saleor/graphql/giftcard/tests/queries/test_gift_card_tags.py`**

- `test_query_gift_card_tags_by_staff` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_tags.py:18]
- `test_query_gift_card_tags_by_app` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_tags.py:38]
- `test_query_gift_card_tags_by_customer` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card_tags.py:58]

**`saleor/graphql/giftcard/tests/queries/test_gift_card.py`**

- `test_query_gift_card_with_permissions` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:59]
- `test_query_gift_card_no_permissions` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:106]
- `test_query_gift_card_by_app` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:119]
- `test_query_gift_card_by_removed_app` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:170]
- `test_query_gift_card_by_app_no_premissions` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:202]
- `test_query_gift_card_with_expiry_date` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:217]
- `test_query_gift_card_by_customer` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:249]
- `test_query_used_gift_card_by_owner` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:265]
- `test_query_gift_card_only_users_emails` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:298]
- `test_staff_query_gift_card_by_invalid_id` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:336]
- `test_staff_query_gift_card_with_invalid_object_type` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:357]
- `test_query_gift_card_events` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:422]
- `test_query_gift_card_event_user_field_denied_for_app_with_only_manage_staff` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:522]
- `test_query_gift_card_event_with_removed_app` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:565]
- `test_query_gift_card_expiry_date_set_event` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:603]
- `test_query_gift_card_used_in_order_event` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:639]
- `test_query_gift_card_bought_event` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:683]
- `test_query_gift_card_events_filter_by_type` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:730]
- `test_query_gift_card_events_filter_by_orders` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:779]
- `test_query_gift_card_events_filter_by_orders_no_events` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:834]
- `test_assigned_field_visible_with_manage_users` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:902]
- `test_assigned_to_requires_manage_users` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_card.py:932]

**`saleor/graphql/giftcard/tests/queries/test_gift_cards_currencies.py`**

- `test_fetch_gift_card_currencies` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_cards_currencies.py:11]
- `test_fetch_gift_card_currencies_by_app` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_cards_currencies.py:37]
- `test_fetch_gift_card_currencies_no_permission` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_cards_currencies.py:62]
- `test_fetch_gift_card_currencies_no_gift_cards` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_cards_currencies.py:72]

**`saleor/graphql/giftcard/tests/queries/test_gift_cards.py`**

- `test_query_gift_cards_by_staff` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_cards.py:22]
- `test_query_gift_cards_by_app` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_cards.py:47]
- `test_query_own_gift_cards` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_cards.py:72]
- `test_me_gift_cards_includes_assigned` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_cards.py:106]
- `test_me_gift_cards_assigned_field_visible_to_owner` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_cards.py:140]
- `test_me_gift_cards_assigned_to_email_requires_manage_gift_card_for_non_owner` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_cards.py:160]
- `test_assigned_customer_can_read_code` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_cards.py:192]
- `test_filter_by_assigned_to` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_cards.py:218]
- `test_filter_by_assigned_to_does_not_require_manage_users` (function) — [saleor/graphql/giftcard/tests/queries/test_gift_cards.py:247]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/giftcard/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/giftcard/tests/queries/test_gift_card_filtering.py` (551 lines)
- `saleor/graphql/giftcard/tests/queries/test_gift_card_search.py` (146 lines)
- `saleor/graphql/giftcard/tests/queries/test_gift_card_sorting.py` (213 lines)
- `saleor/graphql/giftcard/tests/queries/test_gift_card_tags_filtering.py` (52 lines)
- `saleor/graphql/giftcard/tests/queries/test_gift_card_tags.py` (66 lines)
- `saleor/graphql/giftcard/tests/queries/test_gift_card.py` (956 lines)
- `saleor/graphql/giftcard/tests/queries/test_gift_cards_currencies.py` (86 lines)
- `saleor/graphql/giftcard/tests/queries/test_gift_cards.py` (268 lines)

## Interactions

- Imports from: `saleor/giftcard`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....account.models.User`
- `.....core.anonymize.obfuscate_email`
- `.....giftcard.GiftCardEvents`
- `.....giftcard.events`
- `.....giftcard.models.GiftCard`
- `.....giftcard.models.GiftCardEvent`
- `.....permission.enums.AccountPermissions`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `....tests.utils.get_graphql_content_from_response`
- `...enums.GiftCardEventsEnum`
- `saleor.giftcard.models.GiftCard`
- `saleor.giftcard.search.update_gift_cards_search_vector`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `25581f9235ec` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
