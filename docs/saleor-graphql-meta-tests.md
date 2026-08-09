## Purpose

`saleor/graphql/meta/tests` (`saleor/graphql/meta/tests`) groups 3 source file(s) exposing 187 top-level declaration(s).

## Public surface

**`saleor/graphql/meta/tests/conftest.py`**

- `payment_with_public_metadata` (function) — [saleor/graphql/meta/tests/conftest.py:11]
- `payment_with_private_metadata` (function) — [saleor/graphql/meta/tests/conftest.py:18]

**`saleor/graphql/meta/tests/test_meta_queries.py`**

- `execute_query` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:19]
- `assert_model_contains_metadata` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:34]
- `assert_model_contains_private_metadata` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:41]
- `test_query_public_meta_for_me_as_customer` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:62]
- `test_query_public_meta_for_me_as_staff` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:82]
- `test_query_public_meta_for_customer_as_staff` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:114]
- `test_query_public_meta_for_customer_as_app` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:134]
- `test_query_public_meta_for_staff_as_other_staff` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:154]
- `test_query_public_meta_for_checkout_as_anonymous_user` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:186]
- `test_query_public_meta_for_other_customer_checkout_as_anonymous_user` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:202]
- `test_query_public_meta_for_checkout_as_customer` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:220]
- `test_query_public_meta_for_checkout_as_staff` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:238]
- `test_query_public_meta_for_checkout_as_app` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:263]
- `test_query_public_meta_for_order_by_token_as_anonymous_user` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:300]
- `test_query_public_meta_for_order_by_token_as_customer` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:316]
- `test_query_public_meta_for_order_by_token_as_staff` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:333]
- `test_query_public_meta_for_order_by_token_as_app` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:357]
- `test_query_public_meta_for_order_as_anonymous_user` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:393]
- `test_query_public_meta_for_order_as_customer` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:409]
- `test_query_public_meta_for_order_as_staff` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:426]
- `test_query_public_meta_for_order_as_app` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:450]
- `test_query_public_meta_for_draft_order_as_anonymous_user` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:486]
- `test_query_public_meta_for_draft_order_as_customer` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:502]
- `test_query_public_meta_for_draft_order_as_staff` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:519]
- `test_query_public_meta_for_draft_order_as_app` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:543]
- `test_query_public_meta_for_fulfillment_as_anonymous_user` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:581]
- `test_query_public_meta_for_fulfillment_as_customer` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:600]
- `test_query_public_meta_for_fulfillment_as_staff` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:621]
- `test_query_public_meta_for_fulfillment_as_app` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:647]
- `test_query_public_meta_for_attribute_as_anonymous_user` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:685]
- `test_query_public_meta_for_attribute_as_customer` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:701]
- `test_query_public_meta_for_attribute_as_staff` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:717]
- `test_query_public_meta_for_attribute_as_app` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:740]
- `test_query_public_meta_for_category_as_anonymous_user` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:775]
- `test_query_public_meta_for_category_as_customer` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:791]
- `test_query_public_meta_for_category_as_staff` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:807]
- `test_query_public_meta_for_category_as_app` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:830]
- `test_query_public_meta_for_collection_as_anonymous_user` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:865]
- `test_query_public_meta_for_collection_as_customer` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:886]
- `test_query_public_meta_for_collection_as_staff` (function) — [saleor/graphql/meta/tests/test_meta_queries.py:908]
- _…and 145 more in this file_

## How it works

The module's files, as provided to this run:

- `saleor/graphql/meta/tests/__init__.py` (1 lines)
- `saleor/graphql/meta/tests/conftest.py` (21 lines)
- `saleor/graphql/meta/tests/test_meta_queries.py` (3976 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....core.models.ModelWithMetadata`
- `....order.models.Order`
- `....payment.models.Payment`
- `....payment.utils.payment_owned_by_user`
- `....permission.models.Permission`
- `...tests.fixtures.ApiClient`
- `...tests.utils.assert_no_permission`
- `...tests.utils.get_graphql_content`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `b80f9cea349a` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
