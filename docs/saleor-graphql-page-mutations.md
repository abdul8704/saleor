## Purpose

`saleor/graphql/page/mutations` (`saleor/graphql/page/mutations`) groups 11 source file(s) exposing 67 top-level declaration(s).

## Public surface

**`saleor/graphql/page/mutations/page_attribute_assign.py`**

- `PageAttributeAssign` (class) — [saleor/graphql/page/mutations/page_attribute_assign.py:19]
- `Arguments` (class) — [saleor/graphql/page/mutations/page_attribute_assign.py:22]
- `Meta` (class) — [saleor/graphql/page/mutations/page_attribute_assign.py:33]
- `clean_attributes` (function) — [saleor/graphql/page/mutations/page_attribute_assign.py:41]
- `perform_mutation` (function) — [saleor/graphql/page/mutations/page_attribute_assign.py:101]

**`saleor/graphql/page/mutations/page_attribute_unassign.py`**

- `PageAttributeUnassign` (class) — [saleor/graphql/page/mutations/page_attribute_unassign.py:15]
- `Arguments` (class) — [saleor/graphql/page/mutations/page_attribute_unassign.py:18]
- `Meta` (class) — [saleor/graphql/page/mutations/page_attribute_unassign.py:31]
- `perform_mutation` (function) — [saleor/graphql/page/mutations/page_attribute_unassign.py:39]

**`saleor/graphql/page/mutations/page_create.py`**

- `PageInput` (class) — [saleor/graphql/page/mutations/page_create.py:27]
- `Meta` (class) — [saleor/graphql/page/mutations/page_create.py:44]
- `PageCreateInput` (class) — [saleor/graphql/page/mutations/page_create.py:48]
- `Meta` (class) — [saleor/graphql/page/mutations/page_create.py:53]
- `PageCreate` (class) — [saleor/graphql/page/mutations/page_create.py:57]
- `Arguments` (class) — [saleor/graphql/page/mutations/page_create.py:58]
- `Meta` (class) — [saleor/graphql/page/mutations/page_create.py:63]
- `clean_attributes` (function) — [saleor/graphql/page/mutations/page_create.py:72]
- `clean_input` (function) — [saleor/graphql/page/mutations/page_create.py:81]
- `save` (function) — [saleor/graphql/page/mutations/page_create.py:137]
- `success_response` (function) — [saleor/graphql/page/mutations/page_create.py:143]

**`saleor/graphql/page/mutations/page_delete.py`**

- `PageDelete` (class) — [saleor/graphql/page/mutations/page_delete.py:21]
- `Arguments` (class) — [saleor/graphql/page/mutations/page_delete.py:22]
- `Meta` (class) — [saleor/graphql/page/mutations/page_delete.py:25]
- `perform_mutation` (function) — [saleor/graphql/page/mutations/page_delete.py:34]
- `update_products_search_index` (function) — [saleor/graphql/page/mutations/page_delete.py:48]
- `delete_assigned_attribute_values` (function) — [saleor/graphql/page/mutations/page_delete.py:65]

**`saleor/graphql/page/mutations/page_reorder_attribute_values.py`**

- `PageReorderAttributeValues` (class) — [saleor/graphql/page/mutations/page_reorder_attribute_values.py:19]
- `Meta` (class) — [saleor/graphql/page/mutations/page_reorder_attribute_values.py:24]
- `Arguments` (class) — [saleor/graphql/page/mutations/page_reorder_attribute_values.py:31]
- `perform_mutation` (function) — [saleor/graphql/page/mutations/page_reorder_attribute_values.py:45]
- `perform` (function) — [saleor/graphql/page/mutations/page_reorder_attribute_values.py:51]
- `get_instance` (function) — [saleor/graphql/page/mutations/page_reorder_attribute_values.py:80]
- `validate_attribute_assignment` (function) — [saleor/graphql/page/mutations/page_reorder_attribute_values.py:97]

**`saleor/graphql/page/mutations/page_type_create.py`**

- `PageTypeCreateInput` (class) — [saleor/graphql/page/mutations/page_type_create.py:23]
- `Meta` (class) — [saleor/graphql/page/mutations/page_type_create.py:31]
- `PageTypeMixin` (class) — [saleor/graphql/page/mutations/page_type_create.py:35]
- `validate_attributes` (function) — [saleor/graphql/page/mutations/page_type_create.py:37]
- `PageTypeCreate` (class) — [saleor/graphql/page/mutations/page_type_create.py:62]
- `Arguments` (class) — [saleor/graphql/page/mutations/page_type_create.py:63]
- `Meta` (class) — [saleor/graphql/page/mutations/page_type_create.py:68]
- `clean_input` (function) — [saleor/graphql/page/mutations/page_type_create.py:77]
- `post_save_action` (function) — [saleor/graphql/page/mutations/page_type_create.py:105]

**`saleor/graphql/page/mutations/page_type_delete.py`**

- `PageTypeDelete` (class) — [saleor/graphql/page/mutations/page_type_delete.py:20]
- `Arguments` (class) — [saleor/graphql/page/mutations/page_type_delete.py:21]
- `Meta` (class) — [saleor/graphql/page/mutations/page_type_delete.py:24]
- `perform_mutation` (function) — [saleor/graphql/page/mutations/page_type_delete.py:33]
- `update_products_search_index` (function) — [saleor/graphql/page/mutations/page_type_delete.py:43]
- `delete_assigned_attribute_values` (function) — [saleor/graphql/page/mutations/page_type_delete.py:63]
- `post_save_action` (function) — [saleor/graphql/page/mutations/page_type_delete.py:77]

**`saleor/graphql/page/mutations/page_type_reorder_attributes.py`**

- `PageTypeReorderAttributes` (class) — [saleor/graphql/page/mutations/page_type_reorder_attributes.py:17]
- `Arguments` (class) — [saleor/graphql/page/mutations/page_type_reorder_attributes.py:22]
- `Meta` (class) — [saleor/graphql/page/mutations/page_type_reorder_attributes.py:32]
- `perform_mutation` (function) — [saleor/graphql/page/mutations/page_type_reorder_attributes.py:40]

**`saleor/graphql/page/mutations/page_type_update.py`**

- `PageTypeUpdateInput` (class) — [saleor/graphql/page/mutations/page_type_update.py:21]
- `Meta` (class) — [saleor/graphql/page/mutations/page_type_update.py:27]
- `PageTypeUpdate` (class) — [saleor/graphql/page/mutations/page_type_update.py:31]
- `Arguments` (class) — [saleor/graphql/page/mutations/page_type_update.py:32]
- `Meta` (class) — [saleor/graphql/page/mutations/page_type_update.py:38]
- `clean_input` (function) — [saleor/graphql/page/mutations/page_type_update.py:47]
- `post_save_action` (function) — [saleor/graphql/page/mutations/page_type_update.py:87]

**`saleor/graphql/page/mutations/page_update.py`**

- `PageUpdate` (class) — [saleor/graphql/page/mutations/page_update.py:23]
- `Arguments` (class) — [saleor/graphql/page/mutations/page_update.py:24]
- `Meta` (class) — [saleor/graphql/page/mutations/page_update.py:30]
- `clean_attributes` (function) — [saleor/graphql/page/mutations/page_update.py:40]
- `save` (function) — [saleor/graphql/page/mutations/page_update.py:49]
- `update_products_search_index` (function) — [saleor/graphql/page/mutations/page_update.py:70]
- `success_response` (function) — [saleor/graphql/page/mutations/page_update.py:87]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/page/mutations/__init__.py` (23 lines)
- `saleor/graphql/page/mutations/page_attribute_assign.py` (134 lines)
- `saleor/graphql/page/mutations/page_attribute_unassign.py` (56 lines)
- `saleor/graphql/page/mutations/page_create.py` (146 lines)
- `saleor/graphql/page/mutations/page_delete.py` (76 lines)
- `saleor/graphql/page/mutations/page_reorder_attribute_values.py` (119 lines)
- `saleor/graphql/page/mutations/page_type_create.py` (107 lines)
- `saleor/graphql/page/mutations/page_type_delete.py` (79 lines)
- `saleor/graphql/page/mutations/page_type_reorder_attributes.py` (70 lines)
- `saleor/graphql/page/mutations/page_type_update.py` (103 lines)
- `saleor/graphql/page/mutations/page_update.py` (90 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core/db`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....attribute.AttributeInputType`
- `....attribute.AttributeType`
- `....attribute.models`
- `....attribute.models.Attribute`
- `....core.tracing.traced_atomic_transaction`
- `....core.utils.update_mutation_manager.InstanceTracker`
- `....page.error_codes.PageErrorCode`
- `....page.models`
- `....page.utils.mark_pages_search_vector_as_dirty_in_batches`
- `....permission.enums.PagePermissions`
- `....permission.enums.PageTypePermissions`
- `....product.models.Product`
- `...attribute.mutations.BaseReorderAttributeValuesMutation`
- `...attribute.mutations.BaseReorderAttributesMutation`
- `...attribute.types.Attribute`
- `...attribute.types.AttributeValueInput`
- `...attribute.utils.attribute_assignment.AttributeAssignmentMixin`
- `...core.ResolveInfo`
- `...core.context.ChannelContext`
- `...core.descriptions.DEPRECATED_IN_3X_INPUT`
- `...core.descriptions.RICH_CONTENT`
- `...core.doc_category.DOC_CATEGORY_PAGES`
- `...core.fields.JSONString`
- `...core.inputs.ReorderInput`
- `...core.mutations.BaseMutation`
- `...core.mutations.DeprecatedModelMutation`
- `...core.mutations.ModelDeleteMutation`
- `...core.scalars.DateTime`
- `...core.types.BaseInputObjectType`
- `...core.types.NonNullList`
- `...core.types.PageError`
- `...core.types.SeoInput`
- `...core.utils.reordering.perform_reordering`
- `...core.validators.clean_seo_fields`
- `...core.validators.validate_slug_and_generate_if_needed`
- `...page.types.Page`
- `...page.types.PageType`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `...utils.resolve_global_ids_to_primary_keys`
- `...utils.validators.check_for_duplicates`
- `..types.Page`
- `..types.PageType`
- `.page_attribute_assign.PageAttributeAssign`
- `.page_attribute_unassign.PageAttributeUnassign`
- `.page_create.PageCreate`
- `.page_create.PageInput`
- `.page_delete.PageDelete`
- `.page_reorder_attribute_values.PageReorderAttributeValues`
- `.page_type_create.PageTypeCreate`
- `.page_type_create.PageTypeCreateInput`
- `.page_type_create.PageTypeMixin`
- `.page_type_delete.PageTypeDelete`
- `.page_type_reorder_attributes.PageTypeReorderAttributes`
- `.page_type_update.PageTypeUpdate`
- `.page_update.PageUpdate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `0d603d6a3977` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
