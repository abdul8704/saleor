## Purpose

`saleor/webhook/tests/circuit_breaker` (`saleor/webhook/tests/circuit_breaker`) groups 6 source file(s) exposing 25 top-level declaration(s).

## Public surface

**`saleor/webhook/tests/circuit_breaker/fixtures.py`**

- `breaker_storage` (function) — [saleor/webhook/tests/circuit_breaker/fixtures.py:11]
- `breaker_not_connected_storage` (function) — [saleor/webhook/tests/circuit_breaker/fixtures.py:19]
- `app_with_webhook` (function) — [saleor/webhook/tests/circuit_breaker/fixtures.py:27]

**`saleor/webhook/tests/circuit_breaker/test_breaker_board_decorator.py`**

- `test_breaker_board_for_promise_handler` (function) — [saleor/webhook/tests/circuit_breaker/test_breaker_board_decorator.py:14]
- `test_breaker_board_trip_for_promise_handler` (function) — [saleor/webhook/tests/circuit_breaker/test_breaker_board_decorator.py:47]
- `test_breaker_board_enter_half_open_for_promise_handler` (function) — [saleor/webhook/tests/circuit_breaker/test_breaker_board_decorator.py:78]
- `test_breaker_board_closes_on_half_open_for_promise_handler` (function) — [saleor/webhook/tests/circuit_breaker/test_breaker_board_decorator.py:109]
- `test_breaker_board_closes_stays_half_open_below_threshold_for_promise_handler` (function) — [saleor/webhook/tests/circuit_breaker/test_breaker_board_decorator.py:140]
- `test_breaker_board_reopens_on_half_open_for_promise_handler` (function) — [saleor/webhook/tests/circuit_breaker/test_breaker_board_decorator.py:171]

**`saleor/webhook/tests/circuit_breaker/test_breaker_board.py`**

- `test_breaker_board_failure_for_promise_wrapper` (function) — [saleor/webhook/tests/circuit_breaker/test_breaker_board.py:12]
- `test_breaker_board_failure_ignored_webhook_event_type_for_promise_func_wrapper` (function) — [saleor/webhook/tests/circuit_breaker/test_breaker_board.py:46]
- `test_breaker_board_success_for_promise_func_wrapper` (function) — [saleor/webhook/tests/circuit_breaker/test_breaker_board.py:80]
- `test_breaker_board_threshold` (function) — [saleor/webhook/tests/circuit_breaker/test_breaker_board.py:123]
- `test_breaker_board_clear_state_for_app` (function) — [saleor/webhook/tests/circuit_breaker/test_breaker_board.py:167]
- `test_breaker_board_configuration_invalid_events` (function) — [saleor/webhook/tests/circuit_breaker/test_breaker_board.py:202]
- `test_breaker_board_configuration_empty_event` (function) — [saleor/webhook/tests/circuit_breaker/test_breaker_board.py:217]
- `test_breaker_board_configuration_mixed_events` (function) — [saleor/webhook/tests/circuit_breaker/test_breaker_board.py:229]
- `test_breaker_board_configuration_unexpected_dry_run_event` (function) — [saleor/webhook/tests/circuit_breaker/test_breaker_board.py:249]

**`saleor/webhook/tests/circuit_breaker/test_redis_storage.py`**

- `test_get_app_state` (function) — [saleor/webhook/tests/circuit_breaker/test_redis_storage.py:13]
- `test_manually_clear_state_for_app` (function) — [saleor/webhook/tests/circuit_breaker/test_redis_storage.py:27]
- `test_register_event` (function) — [saleor/webhook/tests/circuit_breaker/test_redis_storage.py:43]
- `test_get_app_state_does_not_crash_on_redis_error` (function) — [saleor/webhook/tests/circuit_breaker/test_redis_storage.py:61]
- `test_set_app_state_does_not_crash_on_redis_error` (function) — [saleor/webhook/tests/circuit_breaker/test_redis_storage.py:67]
- `test_register_event_does_not_crash_on_redis_error` (function) — [saleor/webhook/tests/circuit_breaker/test_redis_storage.py:76]

**`saleor/webhook/tests/circuit_breaker/utils.py`**

- `create_breaker_board` (function) — [saleor/webhook/tests/circuit_breaker/utils.py:4]

## How it works

The module's files, as provided to this run:

- `saleor/webhook/tests/circuit_breaker/__init__.py` (1 lines)
- `saleor/webhook/tests/circuit_breaker/fixtures.py` (46 lines)
- `saleor/webhook/tests/circuit_breaker/test_breaker_board_decorator.py` (204 lines)
- `saleor/webhook/tests/circuit_breaker/test_breaker_board.py` (265 lines)
- `saleor/webhook/tests/circuit_breaker/test_redis_storage.py` (79 lines)
- `saleor/webhook/tests/circuit_breaker/utils.py` (23 lines)

## Interactions

- Imports from: `saleor/graphql`, `saleor/webhook`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....app.models.App`
- `....graphql.app.enums.CircuitBreakerState`
- `....webhook.circuit_breaker.storage.RedisStorage`
- `....webhook.event_types.WebhookEventSyncType`
- `....webhook.models.Webhook`
- `....webhook.models.WebhookEvent`
- `....webhook.transport.synchronous.transport`
- `.utils.create_breaker_board`
- `saleor.webhook.circuit_breaker.breaker_board.BreakerBoard`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `69a3927a5c50` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
