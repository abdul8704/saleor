## Purpose

`saleor/graphql/discount/tests/benchmark` (`saleor/graphql/discount/tests/benchmark`) groups 11 source file(s) exposing 15 top-level declaration(s).

## Public surface

**`saleor/graphql/discount/tests/benchmark/test_promotion_create.py`**

- `test_promotion_create` (function) — [saleor/graphql/discount/tests/benchmark/test_promotion_create.py:32]
- `test_promotion_create_order_promotion` (function) — [saleor/graphql/discount/tests/benchmark/test_promotion_create.py:130]

**`saleor/graphql/discount/tests/benchmark/test_promotion_delete.py`**

- `test_promotion_delete` (function) — [saleor/graphql/discount/tests/benchmark/test_promotion_delete.py:10]
- `test_gift_promotion_delete` (function) — [saleor/graphql/discount/tests/benchmark/test_promotion_delete.py:38]

**`saleor/graphql/discount/tests/benchmark/test_promotion_rule_create.py`**

- `test_promotion_rule_create` (function) — [saleor/graphql/discount/tests/benchmark/test_promotion_rule_create.py:27]
- `test_promotion_rule_create_gift` (function) — [saleor/graphql/discount/tests/benchmark/test_promotion_rule_create.py:102]

**`saleor/graphql/discount/tests/benchmark/test_promotion_rule_delete.py`**

- `test_promotion_rule_delete` (function) — [saleor/graphql/discount/tests/benchmark/test_promotion_rule_delete.py:10]

**`saleor/graphql/discount/tests/benchmark/test_promotion_rule_update.py`**

- `test_promotion_rule_update` (function) — [saleor/graphql/discount/tests/benchmark/test_promotion_rule_update.py:13]

**`saleor/graphql/discount/tests/benchmark/test_promotion_update.py`**

- `test_promotion_update` (function) — [saleor/graphql/discount/tests/benchmark/test_promotion_update.py:13]

**`saleor/graphql/discount/tests/benchmark/test_promotions.py`**

- `test_promotions_querytest_promotions_query` (function) — [saleor/graphql/discount/tests/benchmark/test_promotions.py:44]

**`saleor/graphql/discount/tests/benchmark/test_sales.py`**

- `test_sales_query_with_channel_slug` (function) — [saleor/graphql/discount/tests/benchmark/test_sales.py:66]
- `test_sales_query_without_channel_slug` (function) — [saleor/graphql/discount/tests/benchmark/test_sales.py:86]

**`saleor/graphql/discount/tests/benchmark/test_voucher_code_bulk_delete.py`**

- `test_voucher_code_bulk_delete_queries` (function) — [saleor/graphql/discount/tests/benchmark/test_voucher_code_bulk_delete.py:17]

**`saleor/graphql/discount/tests/benchmark/test_vouchers.py`**

- `test_vouchers_query_with_channel_slug` (function) — [saleor/graphql/discount/tests/benchmark/test_vouchers.py:84]
- `test_vouchers_query_withot_channel_slug` (function) — [saleor/graphql/discount/tests/benchmark/test_vouchers.py:104]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/discount/tests/benchmark/__init__.py` (1 lines)
- `saleor/graphql/discount/tests/benchmark/test_promotion_create.py` (206 lines)
- `saleor/graphql/discount/tests/benchmark/test_promotion_delete.py` (61 lines)
- `saleor/graphql/discount/tests/benchmark/test_promotion_rule_create.py` (145 lines)
- `saleor/graphql/discount/tests/benchmark/test_promotion_rule_delete.py` (31 lines)
- `saleor/graphql/discount/tests/benchmark/test_promotion_rule_update.py` (78 lines)
- `saleor/graphql/discount/tests/benchmark/test_promotion_update.py` (45 lines)
- `saleor/graphql/discount/tests/benchmark/test_promotions.py` (63 lines)
- `saleor/graphql/discount/tests/benchmark/test_sales.py` (99 lines)
- `saleor/graphql/discount/tests/benchmark/test_voucher_code_bulk_delete.py` (47 lines)
- `saleor/graphql/discount/tests/benchmark/test_vouchers.py` (117 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....tests.utils.get_graphql_content`
- `...enums.PromotionTypeEnum`
- `...enums.RewardTypeEnum`
- `...enums.RewardValueTypeEnum`
- `..mutations.test_promotion_delete.PROMOTION_DELETE_MUTATION`
- `..mutations.test_promotion_rule_delete.PROMOTION_RULE_DELETE_MUTATION`
- `..mutations.test_promotion_rule_update.PROMOTION_RULE_UPDATE_MUTATION`
- `..mutations.test_promotion_update.PROMOTION_UPDATE_MUTATION`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `385b6d1adc43` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
