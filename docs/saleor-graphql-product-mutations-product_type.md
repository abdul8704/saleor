## Purpose

`saleor/graphql/product/mutations/product_type` (`saleor/graphql/product/mutations/product_type`) groups 4 source file(s) exposing 21 top-level declaration(s).

## Public surface

**`saleor/graphql/product/mutations/product_type/product_type_create.py`**

- `ProductTypeInput` (class) — [saleor/graphql/product/mutations/product_type/product_type_create.py:21]
- `Meta` (class) — [saleor/graphql/product/mutations/product_type/product_type_create.py:70]
- `ProductTypeCreate` (class) — [saleor/graphql/product/mutations/product_type/product_type_create.py:74]
- `Arguments` (class) — [saleor/graphql/product/mutations/product_type/product_type_create.py:75]
- `Meta` (class) — [saleor/graphql/product/mutations/product_type/product_type_create.py:80]
- `clean_product_kind` (function) — [saleor/graphql/product/mutations/product_type/product_type_create.py:89]
- `clean_input` (function) — [saleor/graphql/product/mutations/product_type/product_type_create.py:97]
- `validate_attributes` (function) — [saleor/graphql/product/mutations/product_type/product_type_create.py:126]
- `post_save_action` (function) — [saleor/graphql/product/mutations/product_type/product_type_create.py:157]

**`saleor/graphql/product/mutations/product_type/product_type_delete.py`**

- `ProductTypeDelete` (class) — [saleor/graphql/product/mutations/product_type/product_type_delete.py:20]
- `Arguments` (class) — [saleor/graphql/product/mutations/product_type/product_type_delete.py:21]
- `Meta` (class) — [saleor/graphql/product/mutations/product_type/product_type_delete.py:24]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/product_type/product_type_delete.py:35]
- `delete_assigned_attribute_values` (function) — [saleor/graphql/product/mutations/product_type/product_type_delete.py:60]
- `post_save_action` (function) — [saleor/graphql/product/mutations/product_type/product_type_delete.py:76]

**`saleor/graphql/product/mutations/product_type/product_type_update.py`**

- `ProductTypeUpdate` (class) — [saleor/graphql/product/mutations/product_type/product_type_update.py:16]
- `Arguments` (class) — [saleor/graphql/product/mutations/product_type/product_type_update.py:17]
- `Meta` (class) — [saleor/graphql/product/mutations/product_type/product_type_update.py:23]
- `clean_product_kind` (function) — [saleor/graphql/product/mutations/product_type/product_type_update.py:32]
- `save` (function) — [saleor/graphql/product/mutations/product_type/product_type_update.py:36]
- `post_save_action` (function) — [saleor/graphql/product/mutations/product_type/product_type_update.py:45]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/product/mutations/product_type/__init__.py` (5 lines)
- `saleor/graphql/product/mutations/product_type/product_type_create.py` (159 lines)
- `saleor/graphql/product/mutations/product_type/product_type_delete.py` (78 lines)
- `saleor/graphql/product/mutations/product_type/product_type_update.py` (58 lines)

## Interactions

- Imports from: `saleor/core/db`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....attribute.AttributeInputType`
- `.....attribute.AttributeType`
- `.....attribute.models`
- `.....core.tracing.traced_atomic_transaction`
- `.....order.OrderStatus`
- `.....order.models`
- `.....permission.enums.ProductTypePermissions`
- `.....product.ProductTypeKind`
- `.....product.error_codes.ProductErrorCode`
- `.....product.models`
- `.....product.tasks.update_variants_names`
- `....core.ResolveInfo`
- `....core.descriptions.DEPRECATED_IN_3X_INPUT`
- `....core.doc_category.DOC_CATEGORY_PRODUCTS`
- `....core.mutations.DeprecatedModelMutation`
- `....core.mutations.ModelDeleteMutation`
- `....core.scalars.WeightScalar`
- `....core.types.BaseInputObjectType`
- `....core.types.NonNullList`
- `....core.types.ProductError`
- `....core.validators.validate_slug_and_generate_if_needed`
- `....plugins.dataloaders.get_plugin_manager_promise`
- `...enums.ProductTypeKindEnum`
- `...types.ProductType`
- `..utils.clean_tax_code`
- `.product_type_create.ProductTypeCreate`
- `.product_type_create.ProductTypeInput`
- `.product_type_delete.ProductTypeDelete`
- `.product_type_update.ProductTypeUpdate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `f17b099bcb03` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
