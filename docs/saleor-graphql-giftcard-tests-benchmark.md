## Purpose

`saleor/graphql/giftcard/tests/benchmark` (`saleor/graphql/giftcard/tests/benchmark`) groups 3 source file(s) exposing 9 top-level declaration(s).

## Public surface

**`saleor/graphql/giftcard/tests/benchmark/test_gift_card_mutations.py`**

- `test_create_never_expiry_gift_card` (function) — [saleor/graphql/giftcard/tests/benchmark/test_gift_card_mutations.py:38]
- `test_update_gift_card` (function) — [saleor/graphql/giftcard/tests/benchmark/test_gift_card_mutations.py:105]
- `test_gift_card_bulk_activate_by_staff` (function) — [saleor/graphql/giftcard/tests/benchmark/test_gift_card_mutations.py:162]
- `test_bulk_create_gift_cards` (function) — [saleor/graphql/giftcard/tests/benchmark/test_gift_card_mutations.py:210]

**`saleor/graphql/giftcard/tests/benchmark/test_gift_card_queries.py`**

- `test_query_gift_card_details` (function) — [saleor/graphql/giftcard/tests/benchmark/test_gift_card_queries.py:94]
- `test_query_gift_cards` (function) — [saleor/graphql/giftcard/tests/benchmark/test_gift_card_queries.py:133]
- `test_filter_gift_cards_by_tags` (function) — [saleor/graphql/giftcard/tests/benchmark/test_gift_card_queries.py:173]
- `test_filter_gift_cards_by_used_by_user` (function) — [saleor/graphql/giftcard/tests/benchmark/test_gift_card_queries.py:213]
- `test_filter_gift_cards_by_products` (function) — [saleor/graphql/giftcard/tests/benchmark/test_gift_card_queries.py:263]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/giftcard/tests/benchmark/__init__.py` (1 lines)
- `saleor/graphql/giftcard/tests/benchmark/test_gift_card_mutations.py` (247 lines)
- `saleor/graphql/giftcard/tests/benchmark/test_gift_card_queries.py` (311 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....giftcard.models.GiftCard`
- `....tests.utils.get_graphql_content`
- `.test_gift_card_queries.FRAGMENT_GIFT_CARD_DETAILS`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `19aa43ce2583` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
