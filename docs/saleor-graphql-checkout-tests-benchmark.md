## Purpose

`saleor/graphql/checkout/tests/benchmark` (`saleor/graphql/checkout/tests/benchmark`) groups 5 source file(s) exposing 34 top-level declaration(s).

## Public surface

**`saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py`**

- `test_create_checkout` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:291]
- `test_create_checkout_with_reservations` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:351]
- `test_create_checkout_with_gift_promotion` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:448]
- `test_create_checkout_with_order_promotion` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:512]
- `test_add_shipping_to_checkout` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:584]
- `test_add_delivery_to_checkout` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:620]
- `test_add_billing_address_to_checkout` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:656]
- `test_update_checkout_lines` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:717]
- `test_update_checkout_lines_with_reservations` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:773]
- `test_add_checkout_lines` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:885]
- `test_add_checkout_lines_with_external_shipping` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:958]
- `test_add_checkout_lines_with_reservations` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1059]
- `test_add_checkout_lines_catalogue_discount_applies` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1130]
- `test_add_checkout_lines_multiple_catalogue_discount_applies` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1180]
- `test_add_checkout_lines_order_discount_applies` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1266]
- `test_add_checkout_lines_gift_discount_applies` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1301]
- `test_checkout_shipping_address_update` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1336]
- `test_checkout_email_update` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1369]
- `test_checkout_voucher_code` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1398]
- `test_checkout_payment_charge` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1432]
- `test_complete_checkout` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1630]
- `test_complete_checkout_with_out_of_stock_webhook` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1644]
- `test_complete_checkout_with_single_line` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1665]
- `test_customer_complete_checkout` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1683]
- `test_customer_complete_checkout_for_cc` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1700]
- `test_complete_checkout_preorder` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1717]
- `test_checkout_create_from_order` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1757]
- `test_checkout_gift_cards` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1776]
- `test_checkout_customer_note_update` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py:1807]

**`saleor/graphql/checkout/tests/benchmark/test_checkout.py`**

- `test_user_checkout_details` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkout.py:57]

**`saleor/graphql/checkout/tests/benchmark/test_checkouts.py`**

- `test_staff_multiple_checkouts` (function) — [saleor/graphql/checkout/tests/benchmark/test_checkouts.py:24]

**`saleor/graphql/checkout/tests/benchmark/test_homepage.py`**

- `test_user_checkout_details` (function) — [saleor/graphql/checkout/tests/benchmark/test_homepage.py:15]
- `test_user_checkout_details_with_external_shipping_method` (function) — [saleor/graphql/checkout/tests/benchmark/test_homepage.py:152]
- `test_user_checkout_details_with_tax_app` (function) — [saleor/graphql/checkout/tests/benchmark/test_homepage.py:222]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/checkout/tests/benchmark/__init__.py` (1 lines)
- `saleor/graphql/checkout/tests/benchmark/test_checkout_mutations.py` (1833 lines)
- `saleor/graphql/checkout/tests/benchmark/test_checkout.py` (74 lines)
- `saleor/graphql/checkout/tests/benchmark/test_checkouts.py` (42 lines)
- `saleor/graphql/checkout/tests/benchmark/test_homepage.py` (290 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....checkout.calculations`
- `.....checkout.delivery_context.assign_shipping_method_to_checkout`
- `.....checkout.fetch.fetch_checkout_info`
- `.....checkout.fetch.fetch_checkout_lines`
- `.....checkout.models.Checkout`
- `.....checkout.models.CheckoutDelivery`
- `.....discount.RewardValueType`
- `.....discount.models.CheckoutLineDiscount`
- `.....discount.models.PromotionRule`
- `.....plugins.manager.get_plugins_manager`
- `.....product.models.Product`
- `.....product.models.ProductVariant`
- `.....product.models.ProductVariantChannelListing`
- `.....product.utils.variant_prices.update_discounted_prices_for_promotion`
- `.....product.utils.variants.fetch_variants_for_promotion_rules`
- `.....warehouse.models.Stock`
- `.....webhook.transport.shipping_helpers.to_shipping_app_id`
- `....core.utils.to_global_id_or_none`
- `....tests.utils.get_graphql_content`
- `...mutations.utils.CheckoutLineData`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `48cdc7ba84f8` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
