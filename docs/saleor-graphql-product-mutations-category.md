## Purpose

`saleor/graphql/product/mutations/category` (`saleor/graphql/product/mutations/category`) groups 4 source file(s) exposing 17 top-level declaration(s).

## Public surface

**`saleor/graphql/product/mutations/category/category_create.py`**

- `CategoryInput` (class) — [saleor/graphql/product/mutations/category/category_create.py:27]
- `Meta` (class) — [saleor/graphql/product/mutations/category/category_create.py:47]
- `CategoryCreate` (class) — [saleor/graphql/product/mutations/category/category_create.py:51]
- `Arguments` (class) — [saleor/graphql/product/mutations/category/category_create.py:52]
- `Meta` (class) — [saleor/graphql/product/mutations/category/category_create.py:64]
- `clean_input` (function) — [saleor/graphql/product/mutations/category/category_create.py:75]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/category/category_create.py:100]
- `post_save_action` (function) — [saleor/graphql/product/mutations/category/category_create.py:106]

**`saleor/graphql/product/mutations/category/category_delete.py`**

- `CategoryDelete` (class) — [saleor/graphql/product/mutations/category/category_delete.py:13]
- `Arguments` (class) — [saleor/graphql/product/mutations/category/category_delete.py:14]
- `Meta` (class) — [saleor/graphql/product/mutations/category/category_delete.py:17]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/category/category_delete.py:26]

**`saleor/graphql/product/mutations/category/category_update.py`**

- `CategoryUpdate` (class) — [saleor/graphql/product/mutations/category/category_update.py:15]
- `Arguments` (class) — [saleor/graphql/product/mutations/category/category_update.py:16]
- `Meta` (class) — [saleor/graphql/product/mutations/category/category_update.py:22]
- `construct_instance` (function) — [saleor/graphql/product/mutations/category/category_update.py:33]
- `post_save_action` (function) — [saleor/graphql/product/mutations/category/category_update.py:41]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/product/mutations/category/__init__.py` (5 lines)
- `saleor/graphql/product/mutations/category/category_create.py` (108 lines)
- `saleor/graphql/product/mutations/category/category_delete.py` (36 lines)
- `saleor/graphql/product/mutations/category/category_update.py` (52 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....core.editorjs.editorjs_to_text`
- `.....discount.utils.promotion.mark_active_catalogue_promotion_rules_as_dirty`
- `.....permission.enums.ProductPermissions`
- `.....product.error_codes.ProductErrorCode`
- `.....product.models`
- `.....product.utils.delete_categories`
- `.....thumbnail.models`
- `....core.ResolveInfo`
- `....core.descriptions.RICH_CONTENT`
- `....core.doc_category.DOC_CATEGORY_PRODUCTS`
- `....core.fields.JSONString`
- `....core.mutations.DeprecatedModelMutation`
- `....core.mutations.ModelDeleteMutation`
- `....core.types.ProductError`
- `....core.validators.clean_seo_fields`
- `....core.validators.file.clean_image_file`
- `....core.validators.validate_slug_and_generate_if_needed`
- `....meta.inputs.MetadataInput`
- `....meta.inputs.MetadataInputDescription`
- `....plugins.dataloaders.get_plugin_manager_promise`
- `...types.Category`
- `.category_create.CategoryCreate`
- `.category_create.CategoryInput`
- `.category_delete.CategoryDelete`
- `.category_update.CategoryUpdate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `2283c701720c` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
