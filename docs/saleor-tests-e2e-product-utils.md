## Purpose

`saleor/tests/e2e/product/utils` (`saleor/tests/e2e/product/utils`) groups 17 source file(s) exposing 21 top-level declaration(s).

## Public surface

**`saleor/tests/e2e/product/utils/category.py`**

- `create_category` (function) — [saleor/tests/e2e/product/utils/category.py:20]

**`saleor/tests/e2e/product/utils/collection_add_products.py`**

- `add_product_to_collection` (function) — [saleor/tests/e2e/product/utils/collection_add_products.py:26]

**`saleor/tests/e2e/product/utils/collection_listing_update.py`**

- `create_collection_channel_listing` (function) — [saleor/tests/e2e/product/utils/collection_listing_update.py:28]

**`saleor/tests/e2e/product/utils/collection.py`**

- `create_collection` (function) — [saleor/tests/e2e/product/utils/collection.py:21]

**`saleor/tests/e2e/product/utils/preparing_product.py`**

- `prepare_product` (function) — [saleor/tests/e2e/product/utils/preparing_product.py:11]
- `prepare_products` (function) — [saleor/tests/e2e/product/utils/preparing_product.py:68]

**`saleor/tests/e2e/product/utils/product_attribute_assignment_update.py`**

- `update_product_type_assignment_attribute` (function) — [saleor/tests/e2e/product/utils/product_attribute_assignment_update.py:30]

**`saleor/tests/e2e/product/utils/product_channel_listing.py`**

- `raw_create_product_channel_listing` (function) — [saleor/tests/e2e/product/utils/product_channel_listing.py:34]
- `create_product_channel_listing` (function) — [saleor/tests/e2e/product/utils/product_channel_listing.py:72]

**`saleor/tests/e2e/product/utils/product_query.py`**

- `get_product` (function) — [saleor/tests/e2e/product/utils/product_query.py:69]

**`saleor/tests/e2e/product/utils/product_type_update.py`**

- `update_product_type` (function) — [saleor/tests/e2e/product/utils/product_type_update.py:38]

**`saleor/tests/e2e/product/utils/product_type.py`**

- `create_product_type` (function) — [saleor/tests/e2e/product/utils/product_type.py:33]

**`saleor/tests/e2e/product/utils/product_update.py`**

- `update_product` (function) — [saleor/tests/e2e/product/utils/product_update.py:41]

**`saleor/tests/e2e/product/utils/product_variant_bulk_create.py`**

- `create_variants_in_bulk` (function) — [saleor/tests/e2e/product/utils/product_variant_bulk_create.py:49]

**`saleor/tests/e2e/product/utils/product_variant_channel_listing.py`**

- `raw_create_product_variant_channel_listing` (function) — [saleor/tests/e2e/product/utils/product_variant_channel_listing.py:30]
- `create_product_variant_channel_listing` (function) — [saleor/tests/e2e/product/utils/product_variant_channel_listing.py:59]

**`saleor/tests/e2e/product/utils/product_variant_stock_update.py`**

- `product_variant_stock_update` (function) — [saleor/tests/e2e/product/utils/product_variant_stock_update.py:24]

**`saleor/tests/e2e/product/utils/product_variant.py`**

- `raw_create_product_variant` (function) — [saleor/tests/e2e/product/utils/product_variant.py:24]
- `create_product_variant` (function) — [saleor/tests/e2e/product/utils/product_variant.py:56]

**`saleor/tests/e2e/product/utils/product.py`**

- `create_product` (function) — [saleor/tests/e2e/product/utils/product.py:38]
- `raw_create_product` (function) — [saleor/tests/e2e/product/utils/product.py:66]

## How it works

The module's files, as provided to this run:

- `saleor/tests/e2e/product/utils/__init__.py` (46 lines)
- `saleor/tests/e2e/product/utils/category.py` (43 lines)
- `saleor/tests/e2e/product/utils/collection_add_products.py` (43 lines)
- `saleor/tests/e2e/product/utils/collection_listing_update.py` (60 lines)
- `saleor/tests/e2e/product/utils/collection.py` (44 lines)
- `saleor/tests/e2e/product/utils/preparing_product.py` (91 lines)
- `saleor/tests/e2e/product/utils/product_attribute_assignment_update.py` (50 lines)
- `saleor/tests/e2e/product/utils/product_channel_listing.py` (107 lines)
- `saleor/tests/e2e/product/utils/product_query.py` (89 lines)
- `saleor/tests/e2e/product/utils/product_type_update.py` (53 lines)
- `saleor/tests/e2e/product/utils/product_type.py` (72 lines)
- `saleor/tests/e2e/product/utils/product_update.py` (60 lines)
- `saleor/tests/e2e/product/utils/product_variant_bulk_create.py` (64 lines)
- `saleor/tests/e2e/product/utils/product_variant_channel_listing.py` (78 lines)
- `saleor/tests/e2e/product/utils/product_variant_stock_update.py` (45 lines)
- `saleor/tests/e2e/product/utils/product_variant.py` (78 lines)
- `saleor/tests/e2e/product/utils/product.py` (97 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...utils.get_graphql_content`
- `.category.create_category`
- `.collection.create_collection`
- `.collection_add_products.add_product_to_collection`
- `.collection_listing_update.create_collection_channel_listing`
- `.product.create_product`
- `.product.raw_create_product`
- `.product_query.get_product`
- `.product_type.create_product_type`
- `.product_type_update.update_product_type`
- `.product_update.update_product`
- `.product_variant.create_product_variant`
- `.product_variant.raw_create_product_variant`
- `.product_variant_bulk_create.create_variants_in_bulk`
- `.product_variant_stock_update.product_variant_stock_update`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `1b846186df5a` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
