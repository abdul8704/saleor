## Purpose

`saleor/graphql/payment/mutations` (`saleor/graphql/payment/mutations`) groups 2 source file(s) exposing 4 top-level declaration(s).

## Public surface

**`saleor/graphql/payment/mutations/base.py`**

- `TransactionSessionBase` (class) — [saleor/graphql/payment/mutations/base.py:22]
- `Meta` (class) — [saleor/graphql/payment/mutations/base.py:23]
- `clean_source_object` (function) — [saleor/graphql/payment/mutations/base.py:27]
- `get_amount` (function) — [saleor/graphql/payment/mutations/base.py:104]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/payment/mutations/__init__.py` (45 lines)
- `saleor/graphql/payment/mutations/base.py` (122 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....checkout.calculations.fetch_checkout_data`
- `....checkout.fetch.fetch_checkout_info`
- `....checkout.fetch.fetch_checkout_lines`
- `....checkout.models`
- `....core.prices.quantize_price`
- `....order.models`
- `....plugins.manager.PluginsManager`
- `...core.enums.TransactionInitializeErrorCode`
- `...core.mutations.BaseMutation`
- `...core.utils.from_global_id_or_error`
- `...utils.get_user_or_app_from_context`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `61ea48fcb389` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
