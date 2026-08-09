## Purpose

`saleor/graphql/discount/tests/queries` (`saleor/graphql/discount/tests/queries`) groups 15 source file(s) exposing 82 top-level declaration(s).

## Public surface

**`saleor/graphql/discount/tests/queries/test_promotion.py`**

- `test_query_promotion_by_id_by_staff_user` (function) — [saleor/graphql/discount/tests/queries/test_promotion.py:70]
- `test_query_promotion_by_id_by_app` (function) — [saleor/graphql/discount/tests/queries/test_promotion.py:88]
- `test_query_promotion_by_id_by_customer` (function) — [saleor/graphql/discount/tests/queries/test_promotion.py:105]
- `test_query_promotion_without_rules_by_id` (function) — [saleor/graphql/discount/tests/queries/test_promotion.py:117]
- `test_query_promotion_with_complex_rule_2` (function) — [saleor/graphql/discount/tests/queries/test_promotion.py:135]
- `test_query_order_promotion_with_gift_rule` (function) — [saleor/graphql/discount/tests/queries/test_promotion.py:177]
- `test_query_order_promotion_with_gift_rule_variant_removed_in_meantime` (function) — [saleor/graphql/discount/tests/queries/test_promotion.py:221]
- `test_query_promotion_translation` (function) — [saleor/graphql/discount/tests/queries/test_promotion.py:264]
- `test_query_promotion_rule_translation` (function) — [saleor/graphql/discount/tests/queries/test_promotion.py:305]
- `test_query_promotion_events` (function) — [saleor/graphql/discount/tests/queries/test_promotion.py:374]
- `test_query_promotion_event_created_by_hidden_for_app_with_only_manage_staff` (function) — [saleor/graphql/discount/tests/queries/test_promotion.py:412]

**`saleor/graphql/discount/tests/queries/test_promotions_filtering.py`**

- `test_query_promotions_filter_by_id` (function) — [saleor/graphql/discount/tests/queries/test_promotions_filtering.py:30]
- `test_query_promotions_filter_by_ids_empty_values` (function) — [saleor/graphql/discount/tests/queries/test_promotions_filtering.py:54]
- `test_query_promotions_filter_by_name` (function) — [saleor/graphql/discount/tests/queries/test_promotions_filtering.py:85]
- `test_query_promotions_filter_by_end_date` (function) — [saleor/graphql/discount/tests/queries/test_promotions_filtering.py:149]
- `test_query_promotions_filter_by_start_date` (function) — [saleor/graphql/discount/tests/queries/test_promotions_filtering.py:217]
- `test_query_promotions_filter_by_is_old_sale` (function) — [saleor/graphql/discount/tests/queries/test_promotions_filtering.py:239]
- `test_query_promotions_filter_type_eq` (function) — [saleor/graphql/discount/tests/queries/test_promotions_filtering.py:268]
- `test_query_promotions_filter_type_one_of` (function) — [saleor/graphql/discount/tests/queries/test_promotions_filtering.py:304]

**`saleor/graphql/discount/tests/queries/test_promotions_sorting.py`**

- `test_sorting_promotions_by_name` (function) — [saleor/graphql/discount/tests/queries/test_promotions_sorting.py:28]
- `test_sorting_promotions_by_end_date` (function) — [saleor/graphql/discount/tests/queries/test_promotions_sorting.py:62]
- `test_sorting_promotions_by_start_date` (function) — [saleor/graphql/discount/tests/queries/test_promotions_sorting.py:96]
- `test_sorting_promotions_by_created_at` (function) — [saleor/graphql/discount/tests/queries/test_promotions_sorting.py:132]

**`saleor/graphql/discount/tests/queries/test_promotions.py`**

- `test_query_promotions_by_staff_user` (function) — [saleor/graphql/discount/tests/queries/test_promotions.py:26]
- `test_query_promotions_by_app` (function) — [saleor/graphql/discount/tests/queries/test_promotions.py:49]
- `test_query_promotions_by_customer` (function) — [saleor/graphql/discount/tests/queries/test_promotions.py:72]
- `test_query_promotions_pagination` (function) — [saleor/graphql/discount/tests/queries/test_promotions.py:111]

**`saleor/graphql/discount/tests/queries/test_sale.py`**

- `test_staff_query_sale` (function) — [saleor/graphql/discount/tests/queries/test_sale.py:60]
- `test_query_sale_by_app` (function) — [saleor/graphql/discount/tests/queries/test_sale.py:105]
- `test_query_sale_by_customer` (function) — [saleor/graphql/discount/tests/queries/test_sale.py:126]
- `test_staff_query_sale_by_invalid_id` (function) — [saleor/graphql/discount/tests/queries/test_sale.py:136]
- `test_staff_query_sale_with_invalid_object_type` (function) — [saleor/graphql/discount/tests/queries/test_sale.py:155]
- `test_staff_query_sale_no_channel_provided` (function) — [saleor/graphql/discount/tests/queries/test_sale.py:172]
- `test_query_sale_when_type_is_not_provided` (function) — [saleor/graphql/discount/tests/queries/test_sale.py:195]

**`saleor/graphql/discount/tests/queries/test_sales_filtering.py`**

- `test_query_sales_with_filter_status` (function) — [saleor/graphql/discount/tests/queries/test_sales_filtering.py:48]
- `test_query_sales_with_filter_discount_type` (function) — [saleor/graphql/discount/tests/queries/test_sales_filtering.py:87]
- `test_query_sales_with_filter_started` (function) — [saleor/graphql/discount/tests/queries/test_sales_filtering.py:144]
- `test_query_sales_with_filter_updated_at` (function) — [saleor/graphql/discount/tests/queries/test_sales_filtering.py:197]
- `test_query_sales_with_filter_search` (function) — [saleor/graphql/discount/tests/queries/test_sales_filtering.py:240]

**`saleor/graphql/discount/tests/queries/test_sales_pagination.py`**

- `sales_for_pagination` (function) — [saleor/graphql/discount/tests/queries/test_sales_pagination.py:14]
- `test_sales_pagination_with_sorting` (function) — [saleor/graphql/discount/tests/queries/test_sales_pagination.py:100]
- `test_sales_pagination_with_sorting_and_channel` (function) — [saleor/graphql/discount/tests/queries/test_sales_pagination.py:124]
- `test_sales_pagination_with_filtering` (function) — [saleor/graphql/discount/tests/queries/test_sales_pagination.py:166]

**`saleor/graphql/discount/tests/queries/test_sales_sorting.py`**

- `sales_for_sorting_with_channels` (function) — [saleor/graphql/discount/tests/queries/test_sales_sorting.py:10]
- `test_sales_with_sorting_and_without_channel` (function) — [saleor/graphql/discount/tests/queries/test_sales_sorting.py:97]
- `test_sales_with_sorting_and_channel_USD` (function) — [saleor/graphql/discount/tests/queries/test_sales_sorting.py:145]
- `test_sales_with_sorting_and_channel_PLN` (function) — [saleor/graphql/discount/tests/queries/test_sales_sorting.py:200]
- `test_vouchers_with_sorting_and_not_existing_channel_asc` (function) — [saleor/graphql/discount/tests/queries/test_sales_sorting.py:226]
- `test_query_sales_with_sort` (function) — [saleor/graphql/discount/tests/queries/test_sales_sorting.py:277]

**`saleor/graphql/discount/tests/queries/test_sales.py`**

- `test_sale_query` (function) — [saleor/graphql/discount/tests/queries/test_sales.py:4]
- `test_sale_query_with_channel_slug` (function) — [saleor/graphql/discount/tests/queries/test_sales.py:66]
- `test_sales_query` (function) — [saleor/graphql/discount/tests/queries/test_sales.py:118]
- `test_sales_query_with_channel_slug` (function) — [saleor/graphql/discount/tests/queries/test_sales.py:146]
- `test_sales_query_channel_listing` (function) — [saleor/graphql/discount/tests/queries/test_sales.py:176]

**`saleor/graphql/discount/tests/queries/test_voucher.py`**

- `test_staff_query_voucher` (function) — [saleor/graphql/discount/tests/queries/test_voucher.py:33]
- `test_query_voucher_by_app` (function) — [saleor/graphql/discount/tests/queries/test_voucher.py:49]
- `test_query_voucher_by_customer` (function) — [saleor/graphql/discount/tests/queries/test_voucher.py:65]
- `test_staff_query_voucher_by_invalid_id` (function) — [saleor/graphql/discount/tests/queries/test_voucher.py:76]
- `test_staff_query_voucher_with_invalid_object_type` (function) — [saleor/graphql/discount/tests/queries/test_voucher.py:95]

**`saleor/graphql/discount/tests/queries/test_vouchers_filtering.py`**

- `test_query_vouchers_with_filter_status` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_filtering.py:49]
- `test_query_vouchers_with_filter_times_used` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_filtering.py:93]
- `test_query_vouchers_with_filter_started` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_filtering.py:137]
- `test_query_vouchers_with_filter_discount_type` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_filtering.py:175]
- `test_query_vouchers_with_filter_search` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_filtering.py:212]
- `test_query_vouchers_with_filter_status_expired` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_filtering.py:281]

**`saleor/graphql/discount/tests/queries/test_vouchers_pagination.py`**

- `vouchers_for_pagination` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_pagination.py:12]
- `test_vouchers_pagination_with_sorting` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_pagination.py:149]
- `test_vouchers_pagination_with_sorting_and_channel` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_pagination.py:183]
- `test_vouchers_pagination_with_filtering` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_pagination.py:227]

**`saleor/graphql/discount/tests/queries/test_vouchers_sorting.py`**

- `vouchers_for_sorting_with_channels` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_sorting.py:11]
- `test_voucher_with_sorting_and_without_channel` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_sorting.py:136]
- `test_vouchers_with_sorting_and_channel_USD` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_sorting.py:177]
- `test_vouchers_with_sorting_and_channel_PLN` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_sorting.py:224]
- `test_vouchers_with_sorting_and_not_existing_channel_asc` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_sorting.py:257]
- `test_vouchers_with_filter_and_channel_USD` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_sorting.py:294]
- `test_vouchers_with_filter_by_ids_and_channel_USD` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_sorting.py:319]
- `test_query_vouchers_with_sort` (function) — [saleor/graphql/discount/tests/queries/test_vouchers_sorting.py:411]

**`saleor/graphql/discount/tests/queries/test_vouchers.py`**

- `test_voucher_query` (function) — [saleor/graphql/discount/tests/queries/test_vouchers.py:44]
- `test_voucher_query_no_codes` (function) — [saleor/graphql/discount/tests/queries/test_vouchers.py:83]
- `test_voucher_query_with_channel_slug` (function) — [saleor/graphql/discount/tests/queries/test_vouchers.py:113]
- `test_vouchers_query_with_channel_slug` (function) — [saleor/graphql/discount/tests/queries/test_vouchers.py:155]
- `test_vouchers_query` (function) — [saleor/graphql/discount/tests/queries/test_vouchers.py:183]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/discount/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/discount/tests/queries/test_promotion.py` (438 lines)
- `saleor/graphql/discount/tests/queries/test_promotions_filtering.py` (329 lines)
- `saleor/graphql/discount/tests/queries/test_promotions_sorting.py` (159 lines)
- `saleor/graphql/discount/tests/queries/test_promotions.py` (159 lines)
- `saleor/graphql/discount/tests/queries/test_sale.py` (219 lines)
- `saleor/graphql/discount/tests/queries/test_sales_filtering.py` (288 lines)
- `saleor/graphql/discount/tests/queries/test_sales_pagination.py` (186 lines)
- `saleor/graphql/discount/tests/queries/test_sales_sorting.py` (323 lines)
- `saleor/graphql/discount/tests/queries/test_sales.py` (219 lines)
- `saleor/graphql/discount/tests/queries/test_voucher.py` (108 lines)
- `saleor/graphql/discount/tests/queries/test_vouchers_filtering.py` (329 lines)
- `saleor/graphql/discount/tests/queries/test_vouchers_pagination.py` (247 lines)
- `saleor/graphql/discount/tests/queries/test_vouchers_sorting.py` (454 lines)
- `saleor/graphql/discount/tests/queries/test_vouchers.py` (207 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....discount.DiscountValueType`
- `.....discount.PromotionEvents`
- `.....discount.RewardType`
- `.....discount.RewardValueType`
- `.....discount.VoucherType`
- `.....discount.models.Promotion`
- `.....discount.models.PromotionRule`
- `.....discount.models.Voucher`
- `.....discount.models.VoucherChannelListing`
- `.....discount.models.VoucherCode`
- `.....tests.utils.dummy_editorjs`
- `....tests.utils.assert_graphql_error_with_message`
- `....tests.utils.assert_no_permission`
- `....tests.utils.get_graphql_content`
- `...enums.PromotionTypeEnum`
- `saleor.discount.DiscountValueType`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `6415e199a32e` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
