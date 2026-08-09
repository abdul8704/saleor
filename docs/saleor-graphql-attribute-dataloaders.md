## Purpose

`saleor/graphql/attribute/dataloaders` (`saleor/graphql/attribute/dataloaders`) groups 4 source file(s) exposing 53 top-level declaration(s).

## Public surface

**`saleor/graphql/attribute/dataloaders/assigned_attributes.py`**

- `AttributesByProductIdAndLimitLoader` (class) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:39]
- `get_attribute_product_qs` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:44]
- `batch_load` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:51]
- `with_products` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:53]
- `get_attributes_for_products` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:81]
- `AttributesVisibleToCustomerByProductIdAndLimitLoader` (class) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:114]
- `get_attribute_product_qs` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:119]
- `AttributeByProductIdAndAttributeSlugLoader` (class) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:128]
- `batch_load` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:133]
- `with_attributes_and_products` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:137]
- `AttributeByProductVariantIdAndAttributeSlugLoader` (class) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:191]
- `batch_load` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:196]
- `with_attributes_and_products` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:200]
- `AttributesByProductVariantIdAndSelectionAndLimitLoader` (class) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:255]
- `get_attribute_variant_qs` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:260]
- `batch_load` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:267]
- `with_products` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:269]
- `get_attributes_for_variants` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:319]
- `AttributesVisibleToCustomerByProductVariantIdAndSelectionAndLimitLoader` (class) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:369]
- `get_attribute_variant_qs` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:374]
- `AttributesByPageIdAndLimitLoader` (class) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:382]
- `get_attribute_page_qs` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:387]
- `batch_load` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:392]
- `with_pages` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:394]
- `get_attributes_for_pages` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:420]
- `AttributesVisibleToCustomerByPageIdAndLimitLoader` (class) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:451]
- `get_attribute_page_qs` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:456]
- `AttributeByPageIdAndAttributeSlugLoader` (class) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:463]
- `batch_load` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:468]
- `with_pages_and_attributes` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:472]
- `AttributeValuesByProductIdAndAttributeIdAndLimitLoader` (class) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:522]
- `batch_load` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:527]
- `with_attribute_values` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:566]
- `AttributeValuesByPageIdAndAttributeIdAndLimitLoader` (class) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:590]
- `batch_load` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:595]
- `with_attribute_values` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:633]
- `AttributeValuesByVariantIdAndAttributeIdAndLimitLoader` (class) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:657]
- `batch_load` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:662]
- `with_attribute_values` (function) — [saleor/graphql/attribute/dataloaders/assigned_attributes.py:719]

**`saleor/graphql/attribute/dataloaders/attributes.py`**

- `AttributeValuesByAttributeIdLoader` (class) — [saleor/graphql/attribute/dataloaders/attributes.py:7]
- `batch_load` (function) — [saleor/graphql/attribute/dataloaders/attributes.py:10]
- `AttributesByAttributeId` (class) — [saleor/graphql/attribute/dataloaders/attributes.py:22]
- `batch_load` (function) — [saleor/graphql/attribute/dataloaders/attributes.py:25]
- `AttributesBySlugLoader` (class) — [saleor/graphql/attribute/dataloaders/attributes.py:32]
- `batch_load` (function) — [saleor/graphql/attribute/dataloaders/attributes.py:35]
- `AttributeValueByIdLoader` (class) — [saleor/graphql/attribute/dataloaders/attributes.py:42]
- `batch_load` (function) — [saleor/graphql/attribute/dataloaders/attributes.py:45]

**`saleor/graphql/attribute/dataloaders/reference_types.py`**

- `AttributeReferenceProductTypesByAttributeIdAndLimitLoader` (class) — [saleor/graphql/attribute/dataloaders/reference_types.py:16]
- `batch_load` (function) — [saleor/graphql/attribute/dataloaders/reference_types.py:21]
- `get_reference_types` (function) — [saleor/graphql/attribute/dataloaders/reference_types.py:40]
- `AttributeReferencePageTypesByAttributeIdAndLimitLoader` (class) — [saleor/graphql/attribute/dataloaders/reference_types.py:63]
- `batch_load` (function) — [saleor/graphql/attribute/dataloaders/reference_types.py:68]
- `get_reference_types` (function) — [saleor/graphql/attribute/dataloaders/reference_types.py:87]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/attribute/dataloaders/__init__.py` (1 lines)
- `saleor/graphql/attribute/dataloaders/assigned_attributes.py` (740 lines)
- `saleor/graphql/attribute/dataloaders/attributes.py` (49 lines)
- `saleor/graphql/attribute/dataloaders/reference_types.py` (105 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/graphql`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....attribute.models.Attribute`
- `....attribute.models.AttributeValue`
- `....attribute.models.page.AssignedPageAttributeValue`
- `....attribute.models.page.AttributePage`
- `....attribute.models.product.AssignedProductAttributeValue`
- `....attribute.models.product.AttributeProduct`
- `....core.db.connection.allow_writer_in_context`
- `....page.models`
- `....page.models.PageType`
- `....product.models`
- `....product.models.ProductType`
- `...core.dataloaders.DataLoader`
- `...page.dataloaders.PageByIdLoader`
- `...page.dataloaders.PageTypeByIdLoader`
- `...product.dataloaders.ProductTypeByIdLoader`
- `...product.dataloaders.products.ProductByIdLoader`
- `...product.dataloaders.products.ProductByVariantIdLoader`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c2beadb81637` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
