## Purpose

`saleor/tests/e2e/gift_cards` (`saleor/tests/e2e/gift_cards`) groups 7 source file(s) exposing 11 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/gift_cards/test_gift_cards.py`**

- `test_gift_card_added_via_add_promo_code_and_transaction_does_not_use_the_same_funds_twice` (function) — [saleor/tests/e2e/gift_cards/test_gift_cards.py:74]
- `test_gift_card_detach_gift_card_from_checkout_as_gift_card_transactions_are_about_to_get_charged` (function) — [saleor/tests/e2e/gift_cards/test_gift_cards.py:145]
- `attach_gift_card_to_another_checkout` (function) — [saleor/tests/e2e/gift_cards/test_gift_cards.py:192]
- `test_gift_card_detach_gift_card_from_checkout_as_checkout_gets_completed` (function) — [saleor/tests/e2e/gift_cards/test_gift_cards.py:231]
- `attach_gift_card_to_another_checkout` (function) — [saleor/tests/e2e/gift_cards/test_gift_cards.py:278]
- `test_gift_card_simultaneous_complete_checkout_of_two_checkouts_using_gift_card_differently` (function) — [saleor/tests/e2e/gift_cards/test_gift_cards.py:314]
- `do_complete_checkout` (function) — [saleor/tests/e2e/gift_cards/test_gift_cards.py:378]

**`saleor/tests/e2e/gift_cards/utils/gift_card_bulk_create.py`**

- `bulk_create_gift_card` (function) — [saleor/tests/e2e/gift_cards/utils/gift_card_bulk_create.py:23]

**`saleor/tests/e2e/gift_cards/utils/gift_card_create.py`**

- `create_gift_card` (function) — [saleor/tests/e2e/gift_cards/utils/gift_card_create.py:23]

**`saleor/tests/e2e/gift_cards/utils/gift_card_query.py`**

- `get_gift_card` (function) — [saleor/tests/e2e/gift_cards/utils/gift_card_query.py:21]

**`saleor/tests/e2e/gift_cards/utils/gift_cards_query.py`**

- `get_gift_cards` (function) — [saleor/tests/e2e/gift_cards/utils/gift_cards_query.py:20]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/gift_cards/__init__.py` (1 lines)
- `saleor/tests/e2e/gift_cards/test_gift_cards.py` (407 lines)
- `saleor/tests/e2e/gift_cards/utils/__init__.py` (9 lines)
- `saleor/tests/e2e/gift_cards/utils/gift_card_bulk_create.py` (49 lines)
- `saleor/tests/e2e/gift_cards/utils/gift_card_create.py` (54 lines)
- `saleor/tests/e2e/gift_cards/utils/gift_card_query.py` (34 lines)
- `saleor/tests/e2e/gift_cards/utils/gift_cards_query.py` (34 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....graphql.order.enums.OrderChargeStatusEnum`
- `....tests.race_condition`
- `...e2e.utils.assign_permissions`
- `...utils.get_graphql_content`
- `..checkout.utils.checkout_add_promo_code.checkout_add_promo_code`
- `..checkout.utils.checkout_complete.checkout_complete`
- `..checkout.utils.checkout_create.checkout_create`
- `..orders.utils.order_query.order_query`
- `..product.utils.preparing_product.prepare_product`
- `..shop.utils.prepare_shop`
- `.gift_card_bulk_create.bulk_create_gift_card`
- `.gift_card_create.create_gift_card`
- `.gift_cards_query.get_gift_cards`
- `.utils.gift_card_create.create_gift_card`
- `.utils.gift_card_query.get_gift_card`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `dce0f419535f` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
