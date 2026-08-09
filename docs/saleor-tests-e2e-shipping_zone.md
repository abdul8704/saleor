## Purpose

`saleor/tests/e2e/shipping_zone` (`saleor/tests/e2e/shipping_zone`) groups 6 source file(s) exposing 5 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/shipping_zone/utils/shipping_method_channel_listing.py`**

- `create_shipping_method_channel_listing` (function) — [saleor/tests/e2e/shipping_zone/utils/shipping_method_channel_listing.py:35]

**`saleor/tests/e2e/shipping_zone/utils/shipping_method.py`**

- `decode_and_modify_base64_descriptor` (function) — [saleor/tests/e2e/shipping_zone/utils/shipping_method.py:38]
- `create_shipping_method` (function) — [saleor/tests/e2e/shipping_zone/utils/shipping_method.py:57]

**`saleor/tests/e2e/shipping_zone/utils/shipping_price_update.py`**

- `update_shipping_price` (function) — [saleor/tests/e2e/shipping_zone/utils/shipping_price_update.py:53]

**`saleor/tests/e2e/shipping_zone/utils/shipping_zone.py`**

- `create_shipping_zone` (function) — [saleor/tests/e2e/shipping_zone/utils/shipping_zone.py:49]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/shipping_zone/__init__.py` (1 lines)
- `saleor/tests/e2e/shipping_zone/utils/__init__.py` (11 lines)
- `saleor/tests/e2e/shipping_zone/utils/shipping_method_channel_listing.py` (64 lines)
- `saleor/tests/e2e/shipping_zone/utils/shipping_method.py` (84 lines)
- `saleor/tests/e2e/shipping_zone/utils/shipping_price_update.py` (71 lines)
- `saleor/tests/e2e/shipping_zone/utils/shipping_zone.py` (86 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...utils.get_graphql_content`
- `.shipping_method.create_shipping_method`
- `.shipping_method_channel_listing.create_shipping_method_channel_listing`
- `.shipping_price_update.update_shipping_price`
- `.shipping_zone.create_shipping_zone`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `b9290325947d` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
