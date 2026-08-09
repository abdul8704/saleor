## Purpose

`saleor/tests/e2e/checkout/utils` (`saleor/tests/e2e/checkout/utils`) groups 15 source file(s) exposing 19 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/checkout/utils/checkout_add_promo_code.py`**

- `raw_checkout_add_promo_code` (function) — [saleor/tests/e2e/checkout/utils/checkout_add_promo_code.py:73]
- `checkout_add_promo_code` (function) — [saleor/tests/e2e/checkout/utils/checkout_add_promo_code.py:93]

**`saleor/tests/e2e/checkout/utils/checkout_billing_address_update.py`**

- `checkout_billing_address_update` (function) — [saleor/tests/e2e/checkout/utils/checkout_billing_address_update.py:34]

**`saleor/tests/e2e/checkout/utils/checkout_complete.py`**

- `raw_checkout_complete` (function) — [saleor/tests/e2e/checkout/utils/checkout_complete.py:141]
- `checkout_complete` (function) — [saleor/tests/e2e/checkout/utils/checkout_complete.py:156]

**`saleor/tests/e2e/checkout/utils/checkout_create_from_order.py`**

- `checkout_create_from_order` (function) — [saleor/tests/e2e/checkout/utils/checkout_create_from_order.py:114]

**`saleor/tests/e2e/checkout/utils/checkout_create.py`**

- `raw_checkout_create` (function) — [saleor/tests/e2e/checkout/utils/checkout_create.py:122]
- `checkout_create` (function) — [saleor/tests/e2e/checkout/utils/checkout_create.py:163]

**`saleor/tests/e2e/checkout/utils/checkout_delivery_method_update.py`**

- `checkout_delivery_method_update` (function) — [saleor/tests/e2e/checkout/utils/checkout_delivery_method_update.py:78]

**`saleor/tests/e2e/checkout/utils/checkout_email_update.py`**

- `checkout_update_email` (function) — [saleor/tests/e2e/checkout/utils/checkout_email_update.py:21]

**`saleor/tests/e2e/checkout/utils/checkout_lines_add.py`**

- `checkout_lines_add` (function) — [saleor/tests/e2e/checkout/utils/checkout_lines_add.py:66]

**`saleor/tests/e2e/checkout/utils/checkout_lines_delete.py`**

- `checkout_lines_delete` (function) — [saleor/tests/e2e/checkout/utils/checkout_lines_delete.py:58]

**`saleor/tests/e2e/checkout/utils/checkout_lines_update.py`**

- `checkout_lines_update` (function) — [saleor/tests/e2e/checkout/utils/checkout_lines_update.py:62]

**`saleor/tests/e2e/checkout/utils/checkout_payment_create.py`**

- `raw_checkout_dummy_payment_create` (function) — [saleor/tests/e2e/checkout/utils/checkout_payment_create.py:22]
- `checkout_dummy_payment_create` (function) — [saleor/tests/e2e/checkout/utils/checkout_payment_create.py:45]

**`saleor/tests/e2e/checkout/utils/checkout_remove_promo_code.py`**

- `checkout_remove_promo_code` (function) — [saleor/tests/e2e/checkout/utils/checkout_remove_promo_code.py:28]

**`saleor/tests/e2e/checkout/utils/checkout_shipping_address_update.py`**

- `raw_checkout_shipping_address_update` (function) — [saleor/tests/e2e/checkout/utils/checkout_shipping_address_update.py:41]
- `checkout_shipping_address_update` (function) — [saleor/tests/e2e/checkout/utils/checkout_shipping_address_update.py:59]

**`saleor/tests/e2e/checkout/utils/query_checkout.py`**

- `get_checkout` (function) — [saleor/tests/e2e/checkout/utils/query_checkout.py:62]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/checkout/utils/__init__.py` (51 lines)
- `saleor/tests/e2e/checkout/utils/checkout_add_promo_code.py` (106 lines)
- `saleor/tests/e2e/checkout/utils/checkout_billing_address_update.py` (50 lines)
- `saleor/tests/e2e/checkout/utils/checkout_complete.py` (165 lines)
- `saleor/tests/e2e/checkout/utils/checkout_create_from_order.py` (125 lines)
- `saleor/tests/e2e/checkout/utils/checkout_create.py` (189 lines)
- `saleor/tests/e2e/checkout/utils/checkout_delivery_method_update.py` (98 lines)
- `saleor/tests/e2e/checkout/utils/checkout_email_update.py` (36 lines)
- `saleor/tests/e2e/checkout/utils/checkout_lines_add.py` (81 lines)
- `saleor/tests/e2e/checkout/utils/checkout_lines_delete.py` (72 lines)
- `saleor/tests/e2e/checkout/utils/checkout_lines_update.py` (75 lines)
- `saleor/tests/e2e/checkout/utils/checkout_payment_create.py` (60 lines)
- `saleor/tests/e2e/checkout/utils/checkout_remove_promo_code.py` (43 lines)
- `saleor/tests/e2e/checkout/utils/checkout_shipping_address_update.py` (71 lines)
- `saleor/tests/e2e/checkout/utils/query_checkout.py` (71 lines)

## Interactions

- Imports from: `saleor/graphql/tests`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....DEFAULT_ADDRESS`
- `...account.utils.fragments.ADDRESS_FRAGMENT`
- `...orders.utils.draft_order_create.draft_order_create`
- `...orders.utils.order_lines_create.order_lines_create`
- `...product.utils.product_channel_listing.raw_create_product_channel_listing`
- `...utils.assert_address_data`
- `...utils.get_graphql_content`
- `.checkout_billing_address_update.checkout_billing_address_update`
- `.checkout_complete.checkout_complete`
- `.checkout_complete.raw_checkout_complete`
- `.checkout_create.checkout_create`
- `.checkout_create.raw_checkout_create`
- `.checkout_create_from_order.checkout_create_from_order`
- `.checkout_delivery_method_update.checkout_delivery_method_update`
- `.checkout_email_update.checkout_update_email`
- `.checkout_lines_add.checkout_lines_add`
- `.checkout_lines_delete.checkout_lines_delete`
- `.checkout_lines_update.checkout_lines_update`
- `.checkout_remove_promo_code.checkout_remove_promo_code`
- `.query_checkout.get_checkout`
- `saleor.graphql.tests.utils.get_graphql_content`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `a08b10cef86d` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
