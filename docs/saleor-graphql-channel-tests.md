## Purpose

`saleor/graphql/channel/tests` (`saleor/graphql/channel/tests`) groups 5 source file(s) exposing 11 top-level declaration(s).

## Public surface

**`saleor/graphql/channel/tests/benchmark/test_channel.py`**

- `test_channels_query` (function) — [saleor/graphql/channel/tests/benchmark/test_channel.py:25]

**`saleor/graphql/channel/tests/dataloaders/test_by_transaction.py`**

- `test_batch_load_with_order_transactions` (function) — [saleor/graphql/channel/tests/dataloaders/test_by_transaction.py:6]
- `test_batch_load_with_checkout_transactions` (function) — [saleor/graphql/channel/tests/dataloaders/test_by_transaction.py:26]
- `test_batch_load_with_mixed_transactions` (function) — [saleor/graphql/channel/tests/dataloaders/test_by_transaction.py:43]
- `test_batch_load_with_nonexistent_transaction_ids` (function) — [saleor/graphql/channel/tests/dataloaders/test_by_transaction.py:64]
- `test_batch_load_with_transaction_without_order_or_checkout` (function) — [saleor/graphql/channel/tests/dataloaders/test_by_transaction.py:79]
- `test_batch_load_empty_keys` (function) — [saleor/graphql/channel/tests/dataloaders/test_by_transaction.py:95]
- `test_batch_load_with_deleted_order` (function) — [saleor/graphql/channel/tests/dataloaders/test_by_transaction.py:105]
- `test_batch_load_with_deleted_checkout` (function) — [saleor/graphql/channel/tests/dataloaders/test_by_transaction.py:124]
- `test_batch_load_maintains_order` (function) — [saleor/graphql/channel/tests/dataloaders/test_by_transaction.py:139]
- `test_batch_load_handles_duplicate_transaction_ids` (function) — [saleor/graphql/channel/tests/dataloaders/test_by_transaction.py:164]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/channel/tests/__init__.py` (1 lines)
- `saleor/graphql/channel/tests/benchmark/__init__.py` (1 lines)
- `saleor/graphql/channel/tests/benchmark/test_channel.py` (36 lines)
- `saleor/graphql/channel/tests/dataloaders/__init__.py` (1 lines)
- `saleor/graphql/channel/tests/dataloaders/test_by_transaction.py` (179 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....channel.models.Channel`
- `....context.SaleorContext`
- `....tests.utils.get_graphql_content`
- `...dataloaders.by_transaction.ChannelByTransactionIdLoader`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `b75ec17cfe9a` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
