## Purpose

`saleor/discount/tests/fixtures` (`saleor/discount/tests/fixtures`) groups 5 source file(s) exposing 33 top-level declaration(s).

## Public surface

**`saleor/discount/tests/fixtures/benchmark.py`**

- `promotion_list_for_benchmark` (function) — [saleor/discount/tests/fixtures/benchmark.py:16]
- `promotion_converted_from_sale_list_for_benchmark` (function) — [saleor/discount/tests/fixtures/benchmark.py:68]

**`saleor/discount/tests/fixtures/promotion_rule.py`**

- `promotion_rule` (function) — [saleor/discount/tests/fixtures/promotion_rule.py:13]
- `order_promotion_rule` (function) — [saleor/discount/tests/fixtures/promotion_rule.py:31]
- `gift_promotion_rule` (function) — [saleor/discount/tests/fixtures/promotion_rule.py:47]
- `rule_info` (function) — [saleor/discount/tests/fixtures/promotion_rule.py:62]
- `catalogue_predicate` (function) — [saleor/discount/tests/fixtures/promotion_rule.py:85]

**`saleor/discount/tests/fixtures/promotion.py`**

- `catalogue_promotion` (function) — [saleor/discount/tests/fixtures/promotion.py:15]
- `catalogue_promotion_without_rules` (function) — [saleor/discount/tests/fixtures/promotion.py:61]
- `order_promotion_without_rules` (function) — [saleor/discount/tests/fixtures/promotion.py:72]
- `catalogue_promotion_with_single_rule` (function) — [saleor/discount/tests/fixtures/promotion.py:83]
- `order_promotion_with_rule` (function) — [saleor/discount/tests/fixtures/promotion.py:99]
- `promotion_list` (function) — [saleor/discount/tests/fixtures/promotion.py:118]
- `promotion_10_percentage` (function) — [saleor/discount/tests/fixtures/promotion.py:212]
- `promotion_converted_from_sale` (function) — [saleor/discount/tests/fixtures/promotion.py:235]
- `promotion_converted_from_sale_with_many_channels` (function) — [saleor/discount/tests/fixtures/promotion.py:253]
- `promotion_converted_from_sale_with_empty_predicate` (function) — [saleor/discount/tests/fixtures/promotion.py:271]
- `promotion_converted_from_sale_list` (function) — [saleor/discount/tests/fixtures/promotion.py:289]

**`saleor/discount/tests/fixtures/voucher.py`**

- `voucher_without_channel` (function) — [saleor/discount/tests/fixtures/voucher.py:10]
- `voucher` (function) — [saleor/discount/tests/fixtures/voucher.py:17]
- `voucher_with_many_codes` (function) — [saleor/discount/tests/fixtures/voucher.py:27]
- `voucher_with_many_channels` (function) — [saleor/discount/tests/fixtures/voucher.py:40]
- `voucher_percentage` (function) — [saleor/discount/tests/fixtures/voucher.py:50]
- `voucher_specific_product_type` (function) — [saleor/discount/tests/fixtures/voucher.py:65]
- `voucher_with_high_min_spent_amount` (function) — [saleor/discount/tests/fixtures/voucher.py:73]
- `voucher_shipping_type` (function) — [saleor/discount/tests/fixtures/voucher.py:86]
- `voucher_free_shipping` (function) — [saleor/discount/tests/fixtures/voucher.py:98]
- `voucher_customer` (function) — [saleor/discount/tests/fixtures/voucher.py:109]
- `voucher_multiple_use` (function) — [saleor/discount/tests/fixtures/voucher.py:116]
- `voucher_single_use` (function) — [saleor/discount/tests/fixtures/voucher.py:129]
- `voucher_with_many_channels_and_countries` (function) — [saleor/discount/tests/fixtures/voucher.py:137]
- `voucher_list` (function) — [saleor/discount/tests/fixtures/voucher.py:144]
- `vouchers_list` (function) — [saleor/discount/tests/fixtures/voucher.py:186]

## How it works

The module's files, as provided to this run:

- `saleor/discount/tests/fixtures/__init__.py` (4 lines)
- `saleor/discount/tests/fixtures/benchmark.py` (106 lines)
- `saleor/discount/tests/fixtures/promotion_rule.py` (97 lines)
- `saleor/discount/tests/fixtures/promotion.py` (335 lines)
- `saleor/discount/tests/fixtures/voucher.py` (221 lines)

## Interactions

- Imports from: `saleor/core`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....DiscountValueType`
- `....PromotionType`
- `....RewardType`
- `....RewardValueType`
- `....VoucherType`
- `....discount.RewardValueType`
- `....product.utils.variants.fetch_variants_for_promotion_rules`
- `....tests.utils.dummy_editorjs`
- `...interface.VariantPromotionRuleInfo`
- `...models.Promotion`
- `...models.PromotionRule`
- `...models.Voucher`
- `...models.VoucherChannelListing`
- `...models.VoucherCode`
- `...models.VoucherCustomer`
- `.benchmark.*  # noqa: F403`
- `.promotion.*  # noqa: F403`
- `.promotion_rule.*  # noqa: F403`
- `.voucher.*  # noqa: F403`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `446818c082a5` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
