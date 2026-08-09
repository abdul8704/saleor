## Purpose

`saleor/tests/e2e/checkout/shipping` (`saleor/tests/e2e/checkout/shipping`) groups 4 source file(s) exposing 3 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/checkout/shipping/test_checkout_invalidate_price_based_shipping_on_voucher_add.py`**

- `prepare_entire_order_voucher` (function) — [saleor/tests/e2e/checkout/shipping/test_checkout_invalidate_price_based_shipping_on_voucher_add.py:17]
- `test_checkout_should_invalidate_shipping_methods_when_adding_entire_order_voucher_0116` (function) — [saleor/tests/e2e/checkout/shipping/test_checkout_invalidate_price_based_shipping_on_voucher_add.py:51]

**`saleor/tests/e2e/checkout/shipping/test_use_external_shipping_methods_in_checkout.py`**

- `test_use_external_shipping_methods_in_checkout_core_1652` (function) — [saleor/tests/e2e/checkout/shipping/test_use_external_shipping_methods_in_checkout.py:19]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/checkout/shipping/__init__.py` (1 lines)
- `saleor/tests/e2e/checkout/shipping/cassettes/test_use_external_shipping_methods_in_checkout/test_use_external_shipping_methods_in_checkout_core_1652.yaml` (100 lines)
- `saleor/tests/e2e/checkout/shipping/test_checkout_invalidate_price_based_shipping_on_voucher_add.py` (195 lines)
- `saleor/tests/e2e/checkout/shipping/test_use_external_shipping_methods_in_checkout.py` (143 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...apps.utils.add_app`
- `...product.utils.preparing_product.prepare_product`
- `...shop.utils.preparing_shop.prepare_default_shop`
- `...shop.utils.preparing_shop.prepare_shop`
- `...utils.assign_permissions`
- `...utils.request_matcher`
- `...vouchers.utils.create_voucher`
- `...vouchers.utils.create_voucher_channel_listing`
- `...webhooks.utils.create_webhook`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c13d68a47dc3` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
