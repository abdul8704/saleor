## Purpose

`saleor/graphql/giftcard/tests` (`saleor/graphql/giftcard/tests`) groups 2 source file(s) exposing 5 top-level declaration(s).

## Public surface

**`saleor/graphql/giftcard/tests/test_user_delete_deactivates_assigned_cards.py`**

- `test_customer_delete_deactivates_assigned_gift_card` (function) — [saleor/graphql/giftcard/tests/test_user_delete_deactivates_assigned_cards.py:66]
- `test_account_delete_deactivates_assigned_gift_card` (function) — [saleor/graphql/giftcard/tests/test_user_delete_deactivates_assigned_cards.py:86]
- `test_staff_delete_deactivates_assigned_gift_card` (function) — [saleor/graphql/giftcard/tests/test_user_delete_deactivates_assigned_cards.py:103]
- `test_customer_bulk_delete_deactivates_assigned_gift_card` (function) — [saleor/graphql/giftcard/tests/test_user_delete_deactivates_assigned_cards.py:124]
- `test_staff_bulk_delete_deactivates_assigned_gift_card` (function) — [saleor/graphql/giftcard/tests/test_user_delete_deactivates_assigned_cards.py:143]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/giftcard/tests/__init__.py` (1 lines)
- `saleor/graphql/giftcard/tests/test_user_delete_deactivates_assigned_cards.py` (160 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....account.models.User`
- `....core.tokens.account_delete_token_generator`
- `....giftcard.GiftCardEvents`
- `....giftcard.models.GiftCardEvent`
- `...tests.utils.get_graphql_content`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `6b13b1c3954c` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
