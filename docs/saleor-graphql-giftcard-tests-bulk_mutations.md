## Purpose

`saleor/graphql/giftcard/tests/bulk_mutations` (`saleor/graphql/giftcard/tests/bulk_mutations`) groups 5 source file(s) exposing 23 top-level declaration(s).

## Public surface

**`saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_activate.py`**

- `test_gift_card_bulk_activate_by_staff` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_activate.py:24]
- `test_gift_card_bulk_activate_by_app` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_activate.py:59]
- `test_gift_card_bulk_activate_all_cards_already_active` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_activate.py:92]
- `test_gift_card_bulk_activate_by_customer` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_activate.py:121]
- `test_gift_card_bulk_activate_expired_cards` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_activate.py:143]
- `test_gift_card_bulk_activate_trigger_webhook` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_activate.py:195]

**`saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_create.py`**

- `test_create_never_expiry_gift_cards` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_create.py:85]
- `test_create_gift_cards_trigger_webhooks` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_create.py:170]
- `test_create_gift_cards_with_expiry_date_by_app` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_create.py:223]
- `test_create_gift_cards_by_cutomer` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_create.py:307]
- `test_create_gift_cards_invalid_count_value` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_create.py:337]
- `test_create_gift_cards_too_many_decimal_places_in_balance_amount` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_create.py:388]
- `test_create_gift_cards_zero_balance_amount` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_create.py:438]
- `test_create_gift_cards_invalid_expiry_date` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_create.py:492]

**`saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_deactivate.py`**

- `test_gift_card_bulk_deactivate_by_staff` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_deactivate.py:22]
- `test_gift_card_bulk_deactivate_by_app` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_deactivate.py:62]
- `test_gift_card_bulk_deactivate_all_cards_already_inactive` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_deactivate.py:99]
- `test_gift_card_bulk_deactivate_by_customer` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_deactivate.py:130]
- `test_gift_card_bulk_deactivate_trigger_webhook` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_deactivate.py:154]

**`saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_delete.py`**

- `test_gift_card_bulk_delete_by_staff` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_delete.py:22]
- `test_gift_card_bulk_delete_by_app` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_delete.py:49]
- `test_gift_card_bulk_delete_by_customer` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_delete.py:76]
- `test_gift_card_bulk_delete_trigger_webhook` (function) — [saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_delete.py:96]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/giftcard/tests/bulk_mutations/__init__.py` (1 lines)
- `saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_activate.py` (229 lines)
- `saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_create.py` (537 lines)
- `saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_deactivate.py` (185 lines)
- `saleor/graphql/giftcard/tests/bulk_mutations/test_gift_card_bulk_delete.py` (127 lines)

## Interactions

- Imports from: `saleor/graphql/giftcard/bulk_mutations`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....giftcard.GiftCardEvents`
- `.....giftcard.error_codes.GiftCardErrorCode`
- `.....giftcard.models.GiftCard`
- `.....giftcard.models.GiftCardEvent`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `0269d6ff233b` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
