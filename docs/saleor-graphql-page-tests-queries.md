## Purpose

`saleor/graphql/page/tests/queries` (`saleor/graphql/page/tests/queries`) groups 6 source file(s) exposing 61 top-level declaration(s).

## Public surface

**`saleor/graphql/page/tests/queries/test_page_type.py`**

- `test_page_type_query_by_staff` (function) — [saleor/graphql/page/tests/queries/test_page_type.py:35]
- `test_page_type_query_by_staff_with_page_type_permission` (function) — [saleor/graphql/page/tests/queries/test_page_type.py:67]
- `test_page_type_query_by_staff_no_perm` (function) — [saleor/graphql/page/tests/queries/test_page_type.py:99]
- `test_page_type_query_by_app` (function) — [saleor/graphql/page/tests/queries/test_page_type.py:112]
- `test_page_type_query_by_app_no_perm` (function) — [saleor/graphql/page/tests/queries/test_page_type.py:142]
- `test_staff_query_page_type_by_invalid_id` (function) — [saleor/graphql/page/tests/queries/test_page_type.py:158]
- `test_staff_query_page_type_with_invalid_object_type` (function) — [saleor/graphql/page/tests/queries/test_page_type.py:168]
- `test_page_type_query_filter_unassigned_attributes` (function) — [saleor/graphql/page/tests/queries/test_page_type.py:175]
- `test_page_type_query_where_filter_unassigned_attributes` (function) — [saleor/graphql/page/tests/queries/test_page_type.py:209]
- `test_page_type_query_search_unassigned_attributes` (function) — [saleor/graphql/page/tests/queries/test_page_type.py:243]
- `test_page_type_query_no_pages` (function) — [saleor/graphql/page/tests/queries/test_page_type.py:275]
- `test_query_page_types_for_federation` (function) — [saleor/graphql/page/tests/queries/test_page_type.py:306]
- `test_page_type_attribute_not_visible_in_storefront_for_customer_is_not_returned` (function) — [saleor/graphql/page/tests/queries/test_page_type.py:351]
- `test_page_type_attribute_visible_in_storefront_for_customer_is_returned` (function) — [saleor/graphql/page/tests/queries/test_page_type.py:381]
- `test_page_type_attribute_visible_in_storefront_for_staff_is_always_returned` (function) — [saleor/graphql/page/tests/queries/test_page_type.py:408]

**`saleor/graphql/page/tests/queries/test_page_types_sorting_and_filtering.py`**

- `test_filter_page_types` (function) — [saleor/graphql/page/tests/queries/test_page_types_sorting_and_filtering.py:24]
- `test_filter_page_types_filtering` (function) — [saleor/graphql/page/tests/queries/test_page_types_sorting_and_filtering.py:50]
- `test_sort_page_types_by_name` (function) — [saleor/graphql/page/tests/queries/test_page_types_sorting_and_filtering.py:72]
- `test_sort_page_types_by_slug` (function) — [saleor/graphql/page/tests/queries/test_page_types_sorting_and_filtering.py:95]
- `test_filter_and_sort_by_slug_page_types` (function) — [saleor/graphql/page/tests/queries/test_page_types_sorting_and_filtering.py:118]

**`saleor/graphql/page/tests/queries/test_page.py`**

- `test_query_published_page` (function) — [saleor/graphql/page/tests/queries/test_page.py:58]
- `test_customer_query_unpublished_page` (function) — [saleor/graphql/page/tests/queries/test_page.py:128]
- `test_staff_query_unpublished_page_by_id` (function) — [saleor/graphql/page/tests/queries/test_page.py:145]
- `test_staff_query_unpublished_page_by_id_without_required_permission` (function) — [saleor/graphql/page/tests/queries/test_page.py:163]
- `test_app_query_unpublished_page_by_id` (function) — [saleor/graphql/page/tests/queries/test_page.py:177]
- `test_app_query_unpublished_page_by_id_without_required_permission` (function) — [saleor/graphql/page/tests/queries/test_page.py:199]
- `test_app_query_unpublished_page_by_slug` (function) — [saleor/graphql/page/tests/queries/test_page.py:217]
- `test_app_query_unpublished_page_by_slug_without_required_permission` (function) — [saleor/graphql/page/tests/queries/test_page.py:239]
- `test_staff_query_unpublished_page_by_slug` (function) — [saleor/graphql/page/tests/queries/test_page.py:256]
- `test_staff_query_unpublished_page_by_slug_without_required_permission` (function) — [saleor/graphql/page/tests/queries/test_page.py:274]
- `test_staff_query_page_by_invalid_id` (function) — [saleor/graphql/page/tests/queries/test_page.py:288]
- `test_staff_query_page_with_invalid_object_type` (function) — [saleor/graphql/page/tests/queries/test_page.py:298]
- `test_get_page_with_sorted_attribute_values` (function) — [saleor/graphql/page/tests/queries/test_page.py:305]
- `test_page_attributes_not_visible_in_storefront_for_customer_is_not_returned` (function) — [saleor/graphql/page/tests/queries/test_page.py:369]
- `test_page_attributes_visible_in_storefront_for_customer_is_returned` (function) — [saleor/graphql/page/tests/queries/test_page.py:405]
- `test_page_attributes_visible_in_storefront_for_staff_is_always_returned` (function) — [saleor/graphql/page/tests/queries/test_page.py:438]
- `test_page_query_by_translated_slug` (function) — [saleor/graphql/page/tests/queries/test_page.py:474]
- `test_page_attribute_field_filtering` (function) — [saleor/graphql/page/tests/queries/test_page.py:548]
- `test_page_attribute_field_filtering_not_found` (function) — [saleor/graphql/page/tests/queries/test_page.py:574]
- `test_page_attribute_not_visible_in_storefront_for_customer_is_not_returned` (function) — [saleor/graphql/page/tests/queries/test_page.py:595]
- `test_page_attribute_visible_in_storefront_for_customer_is_returned` (function) — [saleor/graphql/page/tests/queries/test_page.py:634]
- `test_page_attribute_visible_in_storefront_for_staff_is_always_returned` (function) — [saleor/graphql/page/tests/queries/test_page.py:661]
- `test_page_channel_not_found` (function) — [saleor/graphql/page/tests/queries/test_page.py:691]
- `test_applies_limit_on_page_assigned_attributes` (function) — [saleor/graphql/page/tests/queries/test_page.py:715]

**`saleor/graphql/page/tests/queries/test_pages_search.py`**

- `test_pages_query_with_search_by_title` (function) — [saleor/graphql/page/tests/queries/test_pages_search.py:32]
- `test_pages_query_with_search_by_slug` (function) — [saleor/graphql/page/tests/queries/test_pages_search.py:79]
- `test_pages_query_with_search_by_content` (function) — [saleor/graphql/page/tests/queries/test_pages_search.py:125]
- `test_pages_query_with_search_by_page_type` (function) — [saleor/graphql/page/tests/queries/test_pages_search.py:173]
- `test_pages_query_with_search_by_attributes` (function) — [saleor/graphql/page/tests/queries/test_pages_search.py:223]
- `test_pages_query_with_filter` (function) — [saleor/graphql/page/tests/queries/test_pages_search.py:307]
- `test_pages_search_sorted_by_rank_exact_match_prioritized` (function) — [saleor/graphql/page/tests/queries/test_pages_search.py:346]

**`saleor/graphql/page/tests/queries/test_pages.py`**

- `test_pages_query_with_filter_by_page_type` (function) — [saleor/graphql/page/tests/queries/test_pages.py:24]
- `test_pages_with_filtering` (function) — [saleor/graphql/page/tests/queries/test_pages.py:48]
- `test_pages_query_with_filter_by_ids` (function) — [saleor/graphql/page/tests/queries/test_pages.py:64]
- `test_query_pages_with_sort` (function) — [saleor/graphql/page/tests/queries/test_pages.py:116]
- `test_query_pages_by_staff` (function) — [saleor/graphql/page/tests/queries/test_pages.py:309]
- `test_query_pages_by_app` (function) — [saleor/graphql/page/tests/queries/test_pages.py:330]
- `test_query_pages_by_staff_no_perm` (function) — [saleor/graphql/page/tests/queries/test_pages.py:349]
- `test_query_pages_by_app_no_perm` (function) — [saleor/graphql/page/tests/queries/test_pages.py:366]
- `test_query_pages_by_customer` (function) — [saleor/graphql/page/tests/queries/test_pages.py:384]
- `test_pages_attribute_with_incorrect_channel_slug` (function) — [saleor/graphql/page/tests/queries/test_pages.py:431]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/page/tests/queries/__init__.py` (1 lines)
- `saleor/graphql/page/tests/queries/test_page_type.py` (435 lines)
- `saleor/graphql/page/tests/queries/test_page_types_sorting_and_filtering.py` (137 lines)
- `saleor/graphql/page/tests/queries/test_page.py` (759 lines)
- `saleor/graphql/page/tests/queries/test_pages_search.py` (406 lines)
- `saleor/graphql/page/tests/queries/test_pages.py` (453 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....attribute.models.AttributeValue`
- `.....attribute.utils.associate_attribute_values_to_instance`
- `.....page.models.Page`
- `.....page.models.PageTranslation`
- `.....page.models.PageType`
- `.....page.search.update_pages_search_vector`
- `.....tests.utils.dummy_editorjs`
- `....core.enums.LanguageCodeEnum`
- `....tests.utils.get_graphql_content`
- `....tests.utils.get_graphql_content_from_response`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `fa070ae51e84` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
