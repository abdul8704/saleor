## Purpose

`saleor/graphql/discount/tests` (`saleor/graphql/discount/tests`) groups 3 source file(s) exposing 40 top-level declaration(s).

## Public surface

**`saleor/graphql/discount/tests/test_utils.py`**

- `test_get_variants_for_catalogue_predicate_with_or` (function) — [saleor/graphql/discount/tests/test_utils.py:17]
- `test_get_variants_for_catalogue_predicate_with_and` (function) — [saleor/graphql/discount/tests/test_utils.py:49]
- `test_get_variants_for_product_predicate` (function) — [saleor/graphql/discount/tests/test_utils.py:80]
- `test_get_variants_for_variant_predicate` (function) — [saleor/graphql/discount/tests/test_utils.py:98]
- `test_get_variants_for_category_predicate` (function) — [saleor/graphql/discount/tests/test_utils.py:119]
- `test_get_variants_for_collection_predicate` (function) — [saleor/graphql/discount/tests/test_utils.py:143]
- `test_get_variants_for_variant_and_empty_list_of_other_predicates` (function) — [saleor/graphql/discount/tests/test_utils.py:165]
- `test_get_variants_for_variant_or_operator_and_empty_list_of_other_predicates` (function) — [saleor/graphql/discount/tests/test_utils.py:188]
- `test_get_variants_for_catalogue_predicate_with_nested_conditions` (function) — [saleor/graphql/discount/tests/test_utils.py:222]
- `test_get_variants_for_variant_predicate_empty_predicate_data` (function) — [saleor/graphql/discount/tests/test_utils.py:267]
- `test_get_variants_for_promotion` (function) — [saleor/graphql/discount/tests/test_utils.py:280]
- `test_convert_migrated_sale_predicate_to_catalogue_info` (function) — [saleor/graphql/discount/tests/test_utils.py:331]
- `test_predicate_to_snake_case` (function) — [saleor/graphql/discount/tests/test_utils.py:352]
- `test_promotion_rule_should_be_marked_with_dirty_variants` (function) — [saleor/graphql/discount/tests/test_utils.py:440]
- `test_promotion_rule_should_be_marked_with_dirty_variants_incorrect_promotion_type` (function) — [saleor/graphql/discount/tests/test_utils.py:455]
- `test_promotion_rule_should_be_marked_with_dirty_variants_missing_channels` (function) — [saleor/graphql/discount/tests/test_utils.py:470]
- `test_get_variants_for_catalogue_predicate_with_inner_or_operator` (function) — [saleor/graphql/discount/tests/test_utils.py:485]

**`saleor/graphql/discount/tests/test_validators.py`**

- `test_clean_predicate` (function) — [saleor/graphql/discount/tests/test_validators.py:20]
- `test_clean_predicate_invalid_predicate` (function) — [saleor/graphql/discount/tests/test_validators.py:60]
- `test_clean_predicates_invalid_order_predicate` (function) — [saleor/graphql/discount/tests/test_validators.py:69]
- `test_clean_predicates_invalid_catalogue_predicate` (function) — [saleor/graphql/discount/tests/test_validators.py:97]
- `test_clean_predicates_missing_catalogue_predicate` (function) — [saleor/graphql/discount/tests/test_validators.py:127]
- `test_clean_predicates_missing_order_predicate` (function) — [saleor/graphql/discount/tests/test_validators.py:149]
- `test_clean_predicates_mixed_promotion_predicates_invalid_catalogue_predicate` (function) — [saleor/graphql/discount/tests/test_validators.py:169]
- `test_clean_predicates_mixed_promotion_predicates_invalid_order` (function) — [saleor/graphql/discount/tests/test_validators.py:198]
- `test_clean_catalogue_predicate_reward_type_provided` (function) — [saleor/graphql/discount/tests/test_validators.py:223]
- `test_clean_order_predicate_missing_reward_type` (function) — [saleor/graphql/discount/tests/test_validators.py:251]
- `test_clean_order_predicate_reward_type_in_instance` (function) — [saleor/graphql/discount/tests/test_validators.py:279]
- `test_clean_order_predicate_price_based_predicate_mixed_currencies` (function) — [saleor/graphql/discount/tests/test_validators.py:308]
- `test_clean_order_mixed_currencies_instance_given_invalid_predicate` (function) — [saleor/graphql/discount/tests/test_validators.py:341]
- `test_clean_order_mixed_currencies_instance_given_invalid_channels` (function) — [saleor/graphql/discount/tests/test_validators.py:376]
- `test_clean_reward_lack_of_reward_value_type` (function) — [saleor/graphql/discount/tests/test_validators.py:411]
- `test_clean_reward_no_reward_value` (function) — [saleor/graphql/discount/tests/test_validators.py:442]
- `test_clean_reward_lack_of_reward_value_and_reward_value_type` (function) — [saleor/graphql/discount/tests/test_validators.py:471]
- `test_clean_reward_value_missing_channels` (function) — [saleor/graphql/discount/tests/test_validators.py:503]
- `test_clean_reward_value_multiple_currencies` (function) — [saleor/graphql/discount/tests/test_validators.py:534]
- `test_clean_reward_value_multiple_currencies_error_not_raised_for_percentage_disc` (function) — [saleor/graphql/discount/tests/test_validators.py:568]
- `test_clean_gift_rule` (function) — [saleor/graphql/discount/tests/test_validators.py:597]
- `test_clean_gift_rule_no_gifts` (function) — [saleor/graphql/discount/tests/test_validators.py:620]
- `test_clean_gift_rule_invalid_gift_type` (function) — [saleor/graphql/discount/tests/test_validators.py:644]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/discount/tests/__init__.py` (1 lines)
- `saleor/graphql/discount/tests/test_utils.py` (507 lines)
- `saleor/graphql/discount/tests/test_validators.py` (669 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....discount.PromotionType`
- `....discount.RewardType`
- `....discount.RewardValueType`
- `....discount.models.Promotion`
- `....discount.models.PromotionRule`
- `..enums.PromotionCreateErrorCode`
- `..mutations.utils.promotion_rule_should_be_marked_with_dirty_variants`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `4a9b66bfbbee` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
