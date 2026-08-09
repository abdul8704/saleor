## Purpose

`saleor/graphql/product/mutations/product_variant` (`saleor/graphql/product/mutations/product_variant`) groups 10 source file(s) exposing 60 top-level declaration(s).

## Public surface

**`saleor/graphql/product/mutations/product_variant/product_variant_cleaner.py`**

- `clean_weight` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_cleaner.py:14]
- `clean_quantity_limit` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_cleaner.py:27]
- `clean_preorder_settings` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_cleaner.py:43]
- `clean_variant_attributes` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_cleaner.py:53]

**`saleor/graphql/product/mutations/product_variant/product_variant_create.py`**

- `PreorderSettingsInput` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:38]
- `Meta` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:44]
- `ProductVariantInput` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:48]
- `Meta` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:91]
- `ProductVariantCreateInput` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:95]
- `Meta` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:112]
- `ProductVariantCreate` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:116]
- `Arguments` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:117]
- `Meta` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:122]
- `clean_input` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:134]
- `clean_attributes` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:155]
- `get_product` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:186]
- `check_for_duplicates_in_stocks` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:200]
- `set_track_inventory` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:214]
- `save` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:225]
- `post_save_action` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:257]
- `create_variant_stocks` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:265]
- `success_response` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_create.py:273]

**`saleor/graphql/product/mutations/product_variant/product_variant_delete.py`**

- `ProductVariantDelete` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_delete.py:28]
- `Arguments` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_delete.py:29]
- `Meta` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_delete.py:42]
- `success_response` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_delete.py:51]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_delete.py:63]
- `delete_assigned_attribute_values` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_delete.py:146]
- `delete_product_channel_listings_without_available_variants` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_delete.py:157]

**`saleor/graphql/product/mutations/product_variant/product_variant_preorder_deactivate.py`**

- `ProductVariantPreorderDeactivate` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_preorder_deactivate.py:19]
- `Arguments` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_preorder_deactivate.py:24]
- `Meta` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_preorder_deactivate.py:30]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_preorder_deactivate.py:40]

**`saleor/graphql/product/mutations/product_variant/product_variant_reorder.py`**

- `ProductVariantReorder` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_reorder.py:19]
- `Arguments` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_reorder.py:22]
- `Meta` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_reorder.py:33]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_reorder.py:45]

**`saleor/graphql/product/mutations/product_variant/product_variant_set_default.py`**

- `ProductVariantSetDefault` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_set_default.py:16]
- `Arguments` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_set_default.py:19]
- `Meta` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_set_default.py:29]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_set_default.py:40]

**`saleor/graphql/product/mutations/product_variant/product_variant_update.py`**

- `ProductVariantUpdate` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_update.py:39]
- `Arguments` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_update.py:40]
- `Meta` (class) — [saleor/graphql/product/mutations/product_variant/product_variant_update.py:54]
- `get_instance` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_update.py:68]
- `clean_input` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_update.py:111]
- `clean_attributes` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_update.py:130]
- `set_track_inventory` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_update.py:175]
- `construct_instance` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_update.py:254]
- `handle_metadata` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_update.py:291]
- `success_response` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_update.py:307]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/product_variant/product_variant_update.py:312]

**`saleor/graphql/product/mutations/product_variant/variant_media_assign.py`**

- `VariantMediaAssign` (class) — [saleor/graphql/product/mutations/product_variant/variant_media_assign.py:17]
- `Arguments` (class) — [saleor/graphql/product/mutations/product_variant/variant_media_assign.py:21]
- `Meta` (class) — [saleor/graphql/product/mutations/product_variant/variant_media_assign.py:27]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/product_variant/variant_media_assign.py:35]

**`saleor/graphql/product/mutations/product_variant/variant_media_unassign.py`**

- `VariantMediaUnassign` (class) — [saleor/graphql/product/mutations/product_variant/variant_media_unassign.py:16]
- `Arguments` (class) — [saleor/graphql/product/mutations/product_variant/variant_media_unassign.py:20]
- `Meta` (class) — [saleor/graphql/product/mutations/product_variant/variant_media_unassign.py:27]
- `perform_mutation` (function) — [saleor/graphql/product/mutations/product_variant/variant_media_unassign.py:35]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/product/mutations/product_variant/__init__.py` (19 lines)
- `saleor/graphql/product/mutations/product_variant/product_variant_cleaner.py` (76 lines)
- `saleor/graphql/product/mutations/product_variant/product_variant_create.py` (275 lines)
- `saleor/graphql/product/mutations/product_variant/product_variant_delete.py` (183 lines)
- `saleor/graphql/product/mutations/product_variant/product_variant_preorder_deactivate.py` (68 lines)
- `saleor/graphql/product/mutations/product_variant/product_variant_reorder.py` (88 lines)
- `saleor/graphql/product/mutations/product_variant/product_variant_set_default.py` (68 lines)
- `saleor/graphql/product/mutations/product_variant/product_variant_update.py` (359 lines)
- `saleor/graphql/product/mutations/product_variant/variant_media_assign.py` (74 lines)
- `saleor/graphql/product/mutations/product_variant/variant_media_unassign.py` (65 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....attribute.AttributeInputType`
- `.....attribute.lock_objects.attribute_value_qs_select_for_update`
- `.....attribute.models`
- `.....core.exceptions.PreorderAllocationError`
- `.....core.tracing.traced_atomic_transaction`
- `.....core.utils.update_mutation_manager.InstanceTracker`
- `.....discount.utils.promotion.mark_active_catalogue_promotion_rules_as_dirty`
- `.....order.events`
- `.....order.models`
- `.....order.tasks.recalculate_orders_task`
- `.....permission.enums.ProductPermissions`
- `.....product.error_codes.ProductErrorCode`
- `.....product.models`
- `.....product.models.ProductType`
- `.....product.utils.variants.generate_and_set_variant_name`
- `.....warehouse.management.deactivate_preorder_for_variant`
- `....app.dataloaders.get_app_promise`
- `....attribute.types.AttributeValueInput`
- `....attribute.utils.shared.AttrValuesInput`
- `....core.ResolveInfo`
- `....core.context.ChannelContext`
- `....core.doc_category.DOC_CATEGORY_PRODUCTS`
- `....core.inputs.ReorderInput`
- `....core.mutations.BaseMutation`
- `....core.mutations.DeprecatedModelMutation`
- `....core.mutations.ModelDeleteMutation`
- `....core.mutations.ModelWithExtRefMutation`
- `....core.scalars.DateTime`
- `....core.scalars.WeightScalar`
- `....core.types.BaseInputObjectType`
- `....core.types.NonNullList`
- `....core.types.ProductError`
- `....core.utils.ext_ref_to_global_id_or_error`
- `....core.utils.get_duplicated_values`
- `....core.utils.reordering.perform_reordering`
- `....core.validators.validate_one_of_args_is_in_mutation`
- `....meta.inputs.MetadataInput`
- `....meta.inputs.MetadataInputDescription`
- `....plugins.dataloaders.get_plugin_manager_promise`
- `....shop.utils.get_track_inventory_by_default`
- `....site.dataloaders.get_site_promise`
- `....warehouse.types.Warehouse`
- `...types.Product`
- `...types.ProductMedia`
- `...types.ProductVariant`
- `...utils.clean_variant_sku`
- `...utils.get_draft_order_lines_data_for_variants`
- `..product.product_create.StockInput`
- `..product_variant_cleaner`
- `..utils.PRODUCT_VARIANT_UPDATE_FIELDS`
- `.product_variant_create.ProductVariantCreate`
- `.product_variant_create.ProductVariantInput`
- `.product_variant_delete.ProductVariantDelete`
- `.product_variant_preorder_deactivate.ProductVariantPreorderDeactivate`
- `.product_variant_reorder.ProductVariantReorder`
- `.product_variant_set_default.ProductVariantSetDefault`
- `.product_variant_update.ProductVariantUpdate`
- `.variant_media_assign.VariantMediaAssign`
- `.variant_media_unassign.VariantMediaUnassign`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `affb03688351` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
