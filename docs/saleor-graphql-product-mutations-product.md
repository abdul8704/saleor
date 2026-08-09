## Purpose

`saleor/graphql/product/mutations/product` (`saleor/graphql/product/mutations/product`) groups 9 source file(s) exposing 56 top-level declaration(s).

## Public surface

**`saleor/graphql/product/mutations/product/product_cleaner.py`**

- `clean_weight` (function) — [saleor/graphql/product/mutations/product/product_cleaner.py:8]
- `clean_slug` (function) — [saleor/graphql/product/mutations/product/product_cleaner.py:21]
- `clean_description` (function) — [saleor/graphql/product/mutations/product/product_cleaner.py:29]

**`saleor/graphql/product/mutations/product/product_create.py`**

- `ProductInput` (class) — [saleor/graphql/product/mutations/product/product_create.py:30]
- `Meta` (class) — [saleor/graphql/product/mutations/product/product_create.py:83]
- `StockInput` (class) — [saleor/graphql/product/mutations/product/product_create.py:87]
- `Meta` (class) — [saleor/graphql/product/mutations/product/product_create.py:95]
- `StockUpdateInput` (class) — [saleor/graphql/product/mutations/product/product_create.py:99]
- `Meta` (class) — [saleor/graphql/product/mutations/product/product_create.py:105]
- `ProductCreateInput` (class) — [saleor/graphql/product/mutations/product/product_create.py:109]
- `Meta` (class) — [saleor/graphql/product/mutations/product/product_create.py:116]
- `ProductCreate` (class) — [saleor/graphql/product/mutations/product/product_create.py:123]
- `Arguments` (class) — [saleor/graphql/product/mutations/product/product_create.py:124]
- `Meta` (class) — [saleor/graphql/product/mutations/product/product_create.py:129]
- `clean_input` (function) — [saleor/graphql/product/mutations/product/product_create.py:140]
- `clean_attributes` (function) — [saleor/graphql/product/mutations/product/product_create.py:153]
- `save` (function) — [saleor/graphql/product/mutations/product/product_create.py:170]
- `post_save_action` (function) — [saleor/graphql/product/mutations/product/product_create.py:185]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/product/product_create.py:191]

**`saleor/graphql/product/mutations/product/product_delete.py`**

- `ProductDelete` (class) — [saleor/graphql/product/mutations/product/product_delete.py:24]
- `Arguments` (class) — [saleor/graphql/product/mutations/product/product_delete.py:25]
- `Meta` (class) — [saleor/graphql/product/mutations/product/product_delete.py:32]
- `success_response` (function) — [saleor/graphql/product/mutations/product/product_delete.py:41]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/product/product_delete.py:46]
- `delete_assigned_attribute_values` (function) — [saleor/graphql/product/mutations/product/product_delete.py:94]

**`saleor/graphql/product/mutations/product/product_media_create.py`**

- `ProductMediaCreateInput` (class) — [saleor/graphql/product/mutations/product/product_media_create.py:19]
- `Meta` (class) — [saleor/graphql/product/mutations/product/product_media_create.py:31]
- `ProductMediaCreate` (class) — [saleor/graphql/product/mutations/product/product_media_create.py:35]
- `Arguments` (class) — [saleor/graphql/product/mutations/product/product_media_create.py:39]
- `Meta` (class) — [saleor/graphql/product/mutations/product/product_media_create.py:44]
- `validate_input` (function) — [saleor/graphql/product/mutations/product/product_media_create.py:57]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/product/product_media_create.py:69]

**`saleor/graphql/product/mutations/product/product_media_delete.py`**

- `ProductMediaDelete` (class) — [saleor/graphql/product/mutations/product/product_media_delete.py:14]
- `Arguments` (class) — [saleor/graphql/product/mutations/product/product_media_delete.py:18]
- `Meta` (class) — [saleor/graphql/product/mutations/product/product_media_delete.py:21]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/product/product_media_delete.py:29]

**`saleor/graphql/product/mutations/product/product_media_reorder.py`**

- `ProductMediaReorder` (class) — [saleor/graphql/product/mutations/product/product_media_reorder.py:17]
- `Arguments` (class) — [saleor/graphql/product/mutations/product/product_media_reorder.py:21]
- `Meta` (class) — [saleor/graphql/product/mutations/product/product_media_reorder.py:32]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/product/product_media_reorder.py:40]

**`saleor/graphql/product/mutations/product/product_media_update.py`**

- `ProductMediaUpdateInput` (class) — [saleor/graphql/product/mutations/product/product_media_update.py:17]
- `Meta` (class) — [saleor/graphql/product/mutations/product/product_media_update.py:20]
- `ProductMediaUpdate` (class) — [saleor/graphql/product/mutations/product/product_media_update.py:24]
- `Arguments` (class) — [saleor/graphql/product/mutations/product/product_media_update.py:28]
- `Meta` (class) — [saleor/graphql/product/mutations/product/product_media_update.py:34]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/product/product_media_update.py:42]

**`saleor/graphql/product/mutations/product/product_update.py`**

- `ProductUpdate` (class) — [saleor/graphql/product/mutations/product/product_update.py:26]
- `Arguments` (class) — [saleor/graphql/product/mutations/product/product_update.py:27]
- `Meta` (class) — [saleor/graphql/product/mutations/product/product_update.py:37]
- `get_instance` (function) — [saleor/graphql/product/mutations/product/product_update.py:48]
- `clean_input` (function) — [saleor/graphql/product/mutations/product/product_update.py:65]
- `clean_attributes` (function) — [saleor/graphql/product/mutations/product/product_update.py:78]
- `handle_metadata` (function) — [saleor/graphql/product/mutations/product/product_update.py:95]
- `save` (function) — [saleor/graphql/product/mutations/product/product_update.py:111]
- `success_response` (function) — [saleor/graphql/product/mutations/product/product_update.py:137]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/product/product_update.py:142]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/product/mutations/product/__init__.py` (17 lines)
- `saleor/graphql/product/mutations/product/product_media_reorder.py` (82 lines)
- `saleor/graphql/product/mutations/product/product_cleaner.py` (34 lines)
- `saleor/graphql/product/mutations/product/product_create.py` (201 lines)
- `saleor/graphql/product/mutations/product/product_delete.py` (113 lines)
- `saleor/graphql/product/mutations/product/product_media_create.py` (128 lines)
- `saleor/graphql/product/mutations/product/product_media_delete.py` (41 lines)
- `saleor/graphql/product/mutations/product/product_media_update.py` (65 lines)
- `saleor/graphql/product/mutations/product/product_update.py` (156 lines)

## Interactions

- Imports from: `saleor/core/db`
- Imported by: `saleor/graphql/product/tests/mutations`

Internal dependencies named in the source:

- `.....attribute.AttributeInputType`
- `.....attribute.lock_objects.attribute_value_qs_select_for_update`
- `.....attribute.models`
- `.....core.editorjs.editorjs_to_text`
- `.....core.tracing.traced_atomic_transaction`
- `.....discount.utils.promotion.mark_active_catalogue_promotion_rules_as_dirty`
- `.....order.events`
- `.....order.models`
- `.....order.tasks.recalculate_orders_task`
- `.....permission.enums.ProductPermissions`
- `.....product.ProductMediaTypes`
- `.....product.error_codes.ProductErrorCode`
- `.....product.models`
- `.....product.tasks.fetch_product_media_image_task`
- `....app.dataloaders.get_app_promise`
- `....attribute.types.AttributeValueInput`
- `....attribute.utils.attribute_assignment.AttributeAssignmentMixin`
- `....attribute.utils.shared.AttrValuesInput`
- `....core.ResolveInfo`
- `....core.context.ChannelContext`
- `....core.doc_category.DOC_CATEGORY_PRODUCTS`
- `....core.fields.JSONString`
- `....core.mutations.BaseMutation`
- `....core.mutations.DeprecatedModelMutation`
- `....core.mutations.ModelDeleteMutation`
- `....core.mutations.ModelWithExtRefMutation`
- `....core.scalars.WeightScalar`
- `....core.types.BaseInputObjectType`
- `....core.types.NonNullList`
- `....core.types.ProductError`
- `....core.types.SeoInput`
- `....core.types.Upload`
- `....core.types.common.ProductError`
- `....core.validators.clean_seo_fields`
- `....core.validators.file.clean_image_file`
- `....core.validators.validate_slug_and_generate_if_needed`
- `....meta.inputs.MetadataInput`
- `....meta.inputs.MetadataInputDescription`
- `....plugins.dataloaders.get_plugin_manager_promise`
- `...types.Product`
- `...types.ProductMedia`
- `...utils.ALT_CHAR_LIMIT`
- `...utils.get_draft_order_lines_data_for_variants`
- `...utils.probe_media_url`
- `...utils.update_ordered_media`
- `...utils.validate_media_input`
- `..product_cleaner`
- `..utils.clean_tax_code`
- `.product_create.ProductCreate`
- `.product_create.ProductInput`
- `.product_delete.ProductDelete`
- `.product_media_create.ProductMediaCreate`
- `.product_media_delete.ProductMediaDelete`
- `.product_media_reorder.ProductMediaReorder`
- `.product_media_update.ProductMediaUpdate`
- `.product_update.ProductUpdate`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `902705b4211f` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
