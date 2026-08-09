## Purpose

`saleor/graphql/product/mutations/collection` (`saleor/graphql/product/mutations/collection`) groups 7 source file(s) exposing 35 top-level declaration(s).

## Public surface

**`saleor/graphql/product/mutations/collection/collection_add_products.py`**

- `CollectionAddProducts` (class) — [saleor/graphql/product/mutations/collection/collection_add_products.py:16]
- `Arguments` (class) — [saleor/graphql/product/mutations/collection/collection_add_products.py:21]
- `Meta` (class) — [saleor/graphql/product/mutations/collection/collection_add_products.py:29]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/collection/collection_add_products.py:37]

**`saleor/graphql/product/mutations/collection/collection_create.py`**

- `CollectionInput` (class) — [saleor/graphql/product/mutations/collection/collection_create.py:37]
- `Meta` (class) — [saleor/graphql/product/mutations/collection/collection_create.py:65]
- `CollectionCreateInput` (class) — [saleor/graphql/product/mutations/collection/collection_create.py:69]
- `Meta` (class) — [saleor/graphql/product/mutations/collection/collection_create.py:76]
- `CollectionCreate` (class) — [saleor/graphql/product/mutations/collection/collection_create.py:80]
- `Arguments` (class) — [saleor/graphql/product/mutations/collection/collection_create.py:81]
- `Meta` (class) — [saleor/graphql/product/mutations/collection/collection_create.py:86]
- `clean_input` (function) — [saleor/graphql/product/mutations/collection/collection_create.py:97]
- `batch_product_ids` (function) — [saleor/graphql/product/mutations/collection/collection_create.py:118]
- `post_save_action` (function) — [saleor/graphql/product/mutations/collection/collection_create.py:124]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/collection/collection_create.py:139]

**`saleor/graphql/product/mutations/collection/collection_delete.py`**

- `CollectionDelete` (class) — [saleor/graphql/product/mutations/collection/collection_delete.py:19]
- `Arguments` (class) — [saleor/graphql/product/mutations/collection/collection_delete.py:20]
- `Meta` (class) — [saleor/graphql/product/mutations/collection/collection_delete.py:23]
- `batch_product_ids` (function) — [saleor/graphql/product/mutations/collection/collection_delete.py:32]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/collection/collection_delete.py:38]

**`saleor/graphql/product/mutations/collection/collection_remove_products.py`**

- `CollectionRemoveProducts` (class) — [saleor/graphql/product/mutations/collection/collection_remove_products.py:15]
- `Arguments` (class) — [saleor/graphql/product/mutations/collection/collection_remove_products.py:20]
- `Meta` (class) — [saleor/graphql/product/mutations/collection/collection_remove_products.py:28]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/collection/collection_remove_products.py:36]

**`saleor/graphql/product/mutations/collection/collection_reorder_products.py`**

- `MoveProductInput` (class) — [saleor/graphql/product/mutations/collection/collection_reorder_products.py:17]
- `Meta` (class) — [saleor/graphql/product/mutations/collection/collection_reorder_products.py:30]
- `CollectionReorderProducts` (class) — [saleor/graphql/product/mutations/collection/collection_reorder_products.py:34]
- `Meta` (class) — [saleor/graphql/product/mutations/collection/collection_reorder_products.py:39]
- `Arguments` (class) — [saleor/graphql/product/mutations/collection/collection_reorder_products.py:46]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/collection/collection_reorder_products.py:57]

**`saleor/graphql/product/mutations/collection/collection_update.py`**

- `CollectionUpdate` (class) — [saleor/graphql/product/mutations/collection/collection_update.py:15]
- `Arguments` (class) — [saleor/graphql/product/mutations/collection/collection_update.py:16]
- `Meta` (class) — [saleor/graphql/product/mutations/collection/collection_update.py:22]
- `construct_instance` (function) — [saleor/graphql/product/mutations/collection/collection_update.py:33]
- `post_save_action` (function) — [saleor/graphql/product/mutations/collection/collection_update.py:43]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/product/mutations/collection/__init__.py` (15 lines)
- `saleor/graphql/product/mutations/collection/collection_add_products.py` (64 lines)
- `saleor/graphql/product/mutations/collection/collection_create.py` (143 lines)
- `saleor/graphql/product/mutations/collection/collection_delete.py` (61 lines)
- `saleor/graphql/product/mutations/collection/collection_remove_products.py` (62 lines)
- `saleor/graphql/product/mutations/collection/collection_reorder_products.py` (106 lines)
- `saleor/graphql/product/mutations/collection/collection_update.py` (59 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....core.tracing.traced_atomic_transaction`
- `.....core.utils.date_time.convert_to_utc_date_time`
- `.....discount.utils.promotion.mark_active_catalogue_promotion_rules_as_dirty`
- `.....permission.enums.ProductPermissions`
- `.....product.error_codes.CollectionErrorCode`
- `.....product.error_codes.ProductErrorCode`
- `.....product.models`
- `.....product.tasks.collection_product_updated_task`
- `.....thumbnail.models`
- `....core.ResolveInfo`
- `....core.context.ChannelContext`
- `....core.descriptions.DEPRECATED_IN_3X_INPUT`
- `....core.descriptions.RICH_CONTENT`
- `....core.doc_category.DOC_CATEGORY_PRODUCTS`
- `....core.fields.JSONString`
- `....core.mutations.BaseMutation`
- `....core.mutations.DeprecatedModelMutation`
- `....core.mutations.ModelDeleteMutation`
- `....core.scalars.Date`
- `....core.types.BaseInputObjectType`
- `....core.types.CollectionError`
- `....core.types.NonNullList`
- `....core.utils.reordering.perform_reordering`
- `....core.validators.clean_seo_fields`
- `....core.validators.file.clean_image_file`
- `....core.validators.validate_slug_and_generate_if_needed`
- `....meta.inputs.MetadataInput`
- `....meta.inputs.MetadataInputDescription`
- `....plugins.dataloaders.get_plugin_manager_promise`
- `...types.Collection`
- `...types.Product`
- `.collection_add_products.CollectionAddProducts`
- `.collection_create.CollectionCreate`
- `.collection_create.CollectionInput`
- `.collection_delete.CollectionDelete`
- `.collection_remove_products.CollectionRemoveProducts`
- `.collection_reorder_products.CollectionReorderProducts`
- `.collection_update.CollectionUpdate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `74fe78331405` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
