## Purpose

`saleor/checkout/search` (`saleor/checkout/search`) groups 3 source file(s) exposing 10 top-level declaration(s).

## Public surface

**`saleor/checkout/search/indexing.py`**

- `update_checkouts_search_vector` (function) — [saleor/checkout/search/indexing.py:27]
- `set_search_index_dirty` (function) — [saleor/checkout/search/indexing.py:60]
- `prepare_checkout_search_vector_value` (function) — [saleor/checkout/search/indexing.py:75]
- `generate_checkout_transactions_search_vector_value` (function) — [saleor/checkout/search/indexing.py:118]
- `generate_checkout_payments_search_vector_value` (function) — [saleor/checkout/search/indexing.py:156]
- `generate_checkout_lines_search_vector_value` (function) — [saleor/checkout/search/indexing.py:180]

**`saleor/checkout/search/loaders.py`**

- `CheckoutLineData` (class) — [saleor/checkout/search/loaders.py:27]
- `TransactionData` (class) — [saleor/checkout/search/loaders.py:33]
- `CheckoutData` (class) — [saleor/checkout/search/loaders.py:38]
- `load_checkout_data` (function) — [saleor/checkout/search/loaders.py:47]

## How it works

The module's files, as provided to this run:

- `saleor/checkout/search/__init__.py` (1 lines)
- `saleor/checkout/search/indexing.py` (217 lines)
- `saleor/checkout/search/loaders.py` (176 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...account.models.Address`
- `...account.models.User`
- `...core.context.with_promise_context`
- `...core.db.connection.allow_writer`
- `...core.postgres.FlatConcatSearchVector`
- `...core.postgres.NoValidationSearchVector`
- `...graphql.account.dataloaders.AddressByIdLoader`
- `...graphql.account.dataloaders.UserByUserIdLoader`
- `...graphql.core.context.SaleorContext`
- `...payment.models.Payment`
- `...payment.models.TransactionEvent`
- `...payment.models.TransactionItem`
- `...product.models.Product`
- `...product.models.ProductVariant`
- `..lock_objects.checkout_qs_select_for_update`
- `..models.Checkout`
- `..models.CheckoutLine`
- `.loaders.CheckoutData`
- `.loaders.CheckoutLineData`
- `.loaders.TransactionData`
- `.loaders.load_checkout_data`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `ed0f25dc52fb` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
