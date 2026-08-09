## Purpose

`saleor/tests/e2e/transactions` (`saleor/tests/e2e/transactions`) groups 5 source file(s) exposing 4 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/transactions/utils/transaction_create.py`**

- `create_transaction` (function) — [saleor/tests/e2e/transactions/utils/transaction_create.py:32]

**`saleor/tests/e2e/transactions/utils/transaction_event_report.py`**

- `transaction_event_report` (function) — [saleor/tests/e2e/transactions/utils/transaction_event_report.py:70]

**`saleor/tests/e2e/transactions/utils/transaction_initialize.py`**

- `transaction_initialize` (function) — [saleor/tests/e2e/transactions/utils/transaction_initialize.py:69]
- `transaction_initialize_for_gift_card_payment_gateway` (function) — [saleor/tests/e2e/transactions/utils/transaction_initialize.py:116]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/transactions/__init__.py` (1 lines)
- `saleor/tests/e2e/transactions/utils/__init__.py` (9 lines)
- `saleor/tests/e2e/transactions/utils/transaction_create.py` (79 lines)
- `saleor/tests/e2e/transactions/utils/transaction_event_report.py` (103 lines)
- `saleor/tests/e2e/transactions/utils/transaction_initialize.py` (139 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....giftcard.const.GIFT_CARD_PAYMENT_GATEWAY_ID`
- `.....payment.interface.TransactionSessionResult`
- `...utils.get_graphql_content`
- `.transaction_create.create_transaction`
- `.transaction_event_report.transaction_event_report`
- `.transaction_initialize.transaction_initialize`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `7804aa8016ec` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
