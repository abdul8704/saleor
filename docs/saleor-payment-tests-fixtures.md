## Purpose

`saleor/payment/tests/fixtures` (`saleor/payment/tests/fixtures`) groups 7 source file(s) exposing 22 top-level declaration(s).

## Public surface

**`saleor/payment/tests/fixtures/gateway_config.py`**

- `dummy_gateway_config` (function) — [saleor/payment/tests/fixtures/gateway_config.py:7]

**`saleor/payment/tests/fixtures/gateway_response.py`**

- `action_required_gateway_response` (function) — [saleor/payment/tests/fixtures/gateway_response.py:10]
- `success_gateway_response` (function) — [saleor/payment/tests/fixtures/gateway_response.py:35]

**`saleor/payment/tests/fixtures/payment_data.py`**

- `dummy_payment_data` (function) — [saleor/payment/tests/fixtures/payment_data.py:10]

**`saleor/payment/tests/fixtures/payment.py`**

- `payment_dummy` (function) — [saleor/payment/tests/fixtures/payment.py:9]
- `payment_not_authorized` (function) — [saleor/payment/tests/fixtures/payment.py:35]
- `payments_dummy` (function) — [saleor/payment/tests/fixtures/payment.py:42]
- `payment` (function) — [saleor/payment/tests/fixtures/payment.py:73]
- `payment_cancelled` (function) — [saleor/payment/tests/fixtures/payment.py:82]
- `payment_dummy_fully_charged` (function) — [saleor/payment/tests/fixtures/payment.py:89]
- `payment_txn_preauth` (function) — [saleor/payment/tests/fixtures/payment.py:97]
- `payment_txn_captured` (function) — [saleor/payment/tests/fixtures/payment.py:114]
- `payment_txn_capture_failed` (function) — [saleor/payment/tests/fixtures/payment.py:133]
- `payment_txn_to_confirm` (function) — [saleor/payment/tests/fixtures/payment.py:157]
- `payment_txn_refunded` (function) — [saleor/payment/tests/fixtures/payment.py:176]

**`saleor/payment/tests/fixtures/transaction_event.py`**

- `transaction_events_generator` (function) — [saleor/payment/tests/fixtures/transaction_event.py:10]
- `factory` (function) — [saleor/payment/tests/fixtures/transaction_event.py:13]

**`saleor/payment/tests/fixtures/transaction_item.py`**

- `transaction_item_generator` (function) — [saleor/payment/tests/fixtures/transaction_item.py:12]
- `create_transaction` (function) — [saleor/payment/tests/fixtures/transaction_item.py:13]
- `transaction_item_created_by_app` (function) — [saleor/payment/tests/fixtures/transaction_item.py:86]
- `transaction_item_created_by_user` (function) — [saleor/payment/tests/fixtures/transaction_item.py:98]
- `transaction_item` (function) — [saleor/payment/tests/fixtures/transaction_item.py:110]

## How it works

The module's files, as provided to this run:

- `saleor/payment/tests/fixtures/__init__.py` (6 lines)
- `saleor/payment/tests/fixtures/gateway_config.py` (13 lines)
- `saleor/payment/tests/fixtures/gateway_response.py` (45 lines)
- `saleor/payment/tests/fixtures/payment_data.py` (22 lines)
- `saleor/payment/tests/fixtures/payment.py` (191 lines)
- `saleor/payment/tests/fixtures/transaction_event.py` (33 lines)
- `saleor/payment/tests/fixtures/transaction_item.py` (113 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....payment.ChargeStatus`
- `....payment.TransactionKind`
- `....payment.interface.GatewayConfig`
- `....payment.interface.GatewayResponse`
- `....payment.interface.PaymentData`
- `....payment.models.Payment`
- `....payment.models.TransactionEvent`
- `....payment.models.TransactionItem`
- `....webhook.transport.utils.to_payment_app_id`
- `...models.TransactionItem`
- `...transaction_item_calculations.recalculate_transaction_amounts`
- `...utils.create_manual_adjustment_events`
- `.gateway_config.*  # noqa: F403`
- `.gateway_response.*  # noqa: F403`
- `.payment.*  # noqa: F403`
- `.payment_data.*  # noqa: F403`
- `.transaction_event.*  # noqa: F403`
- `.transaction_item.*  # noqa: F403`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `dfccb7e892de` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
