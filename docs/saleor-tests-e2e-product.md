## Purpose

`saleor/tests/e2e/product` (`saleor/tests/e2e/product`) groups 6 source file(s) exposing 7 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/product/test_create_product_with_all_attributes_types.py`**

- `test_create_product_with_attributes_created_in_bulk_core_0704` (function) — [saleor/tests/e2e/product/test_create_product_with_all_attributes_types.py:19]

**`saleor/tests/e2e/product/test_create_product_with_restricted_reference_attributes.py`**

- `test_product_with_restricted_reference_attribute` (function) — [saleor/tests/e2e/product/test_create_product_with_restricted_reference_attributes.py:17]

**`saleor/tests/e2e/product/test_create_simple_product.py`**

- `prepare_attributes_and_product_type` (function) — [saleor/tests/e2e/product/test_create_simple_product.py:17]
- `test_should_create_simple_product_core_0302` (function) — [saleor/tests/e2e/product/test_create_simple_product.py:39]

**`saleor/tests/e2e/product/test_product_no_longer_on_promotion_when_promotion_is_removed.py`**

- `test_product_no_longer_on_promotion_when_promotion_is_removed_CORE_2114` (function) — [saleor/tests/e2e/product/test_product_no_longer_on_promotion_when_promotion_is_removed.py:17]

**`saleor/tests/e2e/product/test_should_create_variants_in_bulk.py`**

- `prepare_attributes_and_product_type` (function) — [saleor/tests/e2e/product/test_should_create_variants_in_bulk.py:17]
- `test_should_create_product_with_few_variants_core_0301` (function) — [saleor/tests/e2e/product/test_should_create_variants_in_bulk.py:63]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/product/__init__.py` (1 lines)
- `saleor/tests/e2e/product/test_create_product_with_all_attributes_types.py` (113 lines)
- `saleor/tests/e2e/product/test_create_product_with_restricted_reference_attributes.py` (208 lines)
- `saleor/tests/e2e/product/test_create_simple_product.py` (109 lines)
- `saleor/tests/e2e/product/test_product_no_longer_on_promotion_when_promotion_is_removed.py` (102 lines)
- `saleor/tests/e2e/product/test_should_create_variants_in_bulk.py` (162 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....product.tasks.recalculate_discounted_price_for_products_task`
- `....tests.utils.dummy_editorjs`
- `..attributes.utils.attribute_create`
- `..attributes.utils.attribute_update`
- `..attributes.utils.prepare_all_attributes_in_bulk`
- `..pages.utils.create_page`
- `..pages.utils.create_page_type`
- `..shop.utils.preparing_shop.prepare_default_shop`
- `..utils.assign_permissions`
- `.utils.preparing_product.prepare_product`
- `.utils.product_query.get_product`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `5ad152dc9611` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
