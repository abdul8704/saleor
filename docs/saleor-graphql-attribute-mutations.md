## Purpose

`saleor/graphql/attribute/mutations` (`saleor/graphql/attribute/mutations`) groups 15 source file(s) exposing 113 top-level declaration(s).

## Public surface

**`saleor/graphql/attribute/mutations/attribute_bulk_create.py`**

- `validate_value` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_create.py:43]
- `clean_values` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_create.py:86]
- `AttributeBulkCreateResult` (class) — [saleor/graphql/attribute/mutations/attribute_bulk_create.py:192]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_bulk_create.py:200]
- `get_results` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_create.py:204]
- `AttributeBulkCreate` (class) — [saleor/graphql/attribute/mutations/attribute_bulk_create.py:224]
- `Arguments` (class) — [saleor/graphql/attribute/mutations/attribute_bulk_create.py:236]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_bulk_create.py:248]
- `clean_attributes` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_create.py:260]
- `clean_attribute_input` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_create.py:370]
- `create_attributes` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_create.py:486]
- `create_values` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_create.py:551]
- `create_reference_types` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_create.py:579]
- `save` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_create.py:605]
- `post_save_actions` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_create.py:641]
- `perform_mutation` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_create.py:649]

**`saleor/graphql/attribute/mutations/attribute_bulk_update.py`**

- `ReferenceTypeUpdateData` (class) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:57]
- `AttributeBulkUpdateResult` (class) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:64]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:72]
- `get_results` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:76]
- `AttributeBulkUpdateInput` (class) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:96]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:103]
- `AttributeBulkUpdate` (class) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:107]
- `Arguments` (class) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:119]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:131]
- `clean_attributes` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:155]
- `get_existing_reference_types` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:332]
- `clean_attribute_input` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:352]
- `clean_remove_values` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:446]
- `update_attributes` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:484]
- `create_values` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:553]
- `create_reference_types` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:582]
- `get_attributes` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:614]
- `find_attribute` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:651]
- `save` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:677]
- `post_save_actions` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:838]
- `perform_mutation` (function) — [saleor/graphql/attribute/mutations/attribute_bulk_update.py:858]

**`saleor/graphql/attribute/mutations/attribute_create.py`**

- `AttributeValueInput` (class) — [saleor/graphql/attribute/mutations/attribute_create.py:25]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_create.py:49]
- `AttributeValueCreateInput` (class) — [saleor/graphql/attribute/mutations/attribute_create.py:53]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_create.py:56]
- `AttributeCreateInput` (class) — [saleor/graphql/attribute/mutations/attribute_create.py:60]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_create.py:112]
- `AttributeCreate` (class) — [saleor/graphql/attribute/mutations/attribute_create.py:122]
- `Arguments` (class) — [saleor/graphql/attribute/mutations/attribute_create.py:129]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_create.py:134]
- `clean_input` (function) — [saleor/graphql/attribute/mutations/attribute_create.py:148]
- `perform_mutation` (function) — [saleor/graphql/attribute/mutations/attribute_create.py:166]
- `post_save_action` (function) — [saleor/graphql/attribute/mutations/attribute_create.py:192]

**`saleor/graphql/attribute/mutations/attribute_delete.py`**

- `AttributeDelete` (class) — [saleor/graphql/attribute/mutations/attribute_delete.py:27]
- `Arguments` (class) — [saleor/graphql/attribute/mutations/attribute_delete.py:28]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_delete.py:35]
- `success_response` (function) — [saleor/graphql/attribute/mutations/attribute_delete.py:54]
- `post_save_action` (function) — [saleor/graphql/attribute/mutations/attribute_delete.py:60]
- `perform_mutation` (function) — [saleor/graphql/attribute/mutations/attribute_delete.py:65]
- `get_product_ids_to_search_index_update` (function) — [saleor/graphql/attribute/mutations/attribute_delete.py:95]
- `get_page_ids_to_search_index_update` (function) — [saleor/graphql/attribute/mutations/attribute_delete.py:108]

**`saleor/graphql/attribute/mutations/attribute_reorder_values.py`**

- `AttributeReorderValues` (class) — [saleor/graphql/attribute/mutations/attribute_reorder_values.py:24]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_reorder_values.py:29]
- `Arguments` (class) — [saleor/graphql/attribute/mutations/attribute_reorder_values.py:50]
- `perform_mutation` (function) — [saleor/graphql/attribute/mutations/attribute_reorder_values.py:61]

**`saleor/graphql/attribute/mutations/attribute_update.py`**

- `AttributeValueUpdateInput` (class) — [saleor/graphql/attribute/mutations/attribute_update.py:34]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_update.py:37]
- `AttributeUpdateInput` (class) — [saleor/graphql/attribute/mutations/attribute_update.py:41]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_update.py:97]
- `AttributeUpdate` (class) — [saleor/graphql/attribute/mutations/attribute_update.py:107]
- `Arguments` (class) — [saleor/graphql/attribute/mutations/attribute_update.py:114]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_update.py:124]
- `clean_remove_values` (function) — [saleor/graphql/attribute/mutations/attribute_update.py:143]
- `perform_mutation` (function) — [saleor/graphql/attribute/mutations/attribute_update.py:165]
- `post_save_action` (function) — [saleor/graphql/attribute/mutations/attribute_update.py:202]

**`saleor/graphql/attribute/mutations/attribute_value_create.py`**

- `AttributeValueCreate` (class) — [saleor/graphql/attribute/mutations/attribute_value_create.py:25]
- `Arguments` (class) — [saleor/graphql/attribute/mutations/attribute_value_create.py:30]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_value_create.py:40]
- `clean_input` (function) — [saleor/graphql/attribute/mutations/attribute_value_create.py:63]
- `clean_instance` (function) — [saleor/graphql/attribute/mutations/attribute_value_create.py:97]
- `perform_mutation` (function) — [saleor/graphql/attribute/mutations/attribute_value_create.py:102]
- `post_save_action` (function) — [saleor/graphql/attribute/mutations/attribute_value_create.py:123]

**`saleor/graphql/attribute/mutations/attribute_value_delete.py`**

- `AttributeValueDelete` (class) — [saleor/graphql/attribute/mutations/attribute_value_delete.py:28]
- `Arguments` (class) — [saleor/graphql/attribute/mutations/attribute_value_delete.py:31]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_value_delete.py:38]
- `perform_mutation` (function) — [saleor/graphql/attribute/mutations/attribute_value_delete.py:61]
- `success_response` (function) — [saleor/graphql/attribute/mutations/attribute_value_delete.py:84]

**`saleor/graphql/attribute/mutations/attribute_value_update.py`**

- `AttributeValueUpdate` (class) — [saleor/graphql/attribute/mutations/attribute_value_update.py:27]
- `Arguments` (class) — [saleor/graphql/attribute/mutations/attribute_value_update.py:30]
- `Meta` (class) — [saleor/graphql/attribute/mutations/attribute_value_update.py:42]
- `clean_input` (function) — [saleor/graphql/attribute/mutations/attribute_value_update.py:65]
- `perform_mutation` (function) — [saleor/graphql/attribute/mutations/attribute_value_update.py:75]
- `success_response` (function) — [saleor/graphql/attribute/mutations/attribute_value_update.py:87]
- `post_save_action` (function) — [saleor/graphql/attribute/mutations/attribute_value_update.py:94]
- `mark_search_index_dirty` (function) — [saleor/graphql/attribute/mutations/attribute_value_update.py:101]

**`saleor/graphql/attribute/mutations/base_reorder_attributes.py`**

- `BaseReorderAttributesMutation` (class) — [saleor/graphql/attribute/mutations/base_reorder_attributes.py:16]
- `Meta` (class) — [saleor/graphql/attribute/mutations/base_reorder_attributes.py:17]
- `prepare_operations` (function) — [saleor/graphql/attribute/mutations/base_reorder_attributes.py:21]
- `BaseReorderAttributeValuesMutation` (class) — [saleor/graphql/attribute/mutations/base_reorder_attributes.py:66]
- `Meta` (class) — [saleor/graphql/attribute/mutations/base_reorder_attributes.py:67]
- `perform` (function) — [saleor/graphql/attribute/mutations/base_reorder_attributes.py:71]
- `get_instance` (function) — [saleor/graphql/attribute/mutations/base_reorder_attributes.py:100]
- `get_attribute_assignment` (function) — [saleor/graphql/attribute/mutations/base_reorder_attributes.py:104]
- `prepare_operations` (function) — [saleor/graphql/attribute/mutations/base_reorder_attributes.py:128]

**`saleor/graphql/attribute/mutations/mixins.py`**

- `AttributeMixin` (class) — [saleor/graphql/attribute/mutations/mixins.py:28]
- `clean_values` (function) — [saleor/graphql/attribute/mutations/mixins.py:34]
- `validate_non_swatch_attr_value` (function) — [saleor/graphql/attribute/mutations/mixins.py:115]
- `validate_swatch_attr_value` (function) — [saleor/graphql/attribute/mutations/mixins.py:128]
- `check_values_are_unique` (function) — [saleor/graphql/attribute/mutations/mixins.py:140]
- `validate_reference_types_limit` (function) — [saleor/graphql/attribute/mutations/mixins.py:172]
- `clean_attribute` (function) — [saleor/graphql/attribute/mutations/mixins.py:188]
- `clean_reference_types` (function) — [saleor/graphql/attribute/mutations/mixins.py:225]

**`saleor/graphql/attribute/mutations/permissions.py`**

- `check_any_attribute_type_permission` (function) — [saleor/graphql/attribute/mutations/permissions.py:20]
- `check_attribute_type_permissions` (function) — [saleor/graphql/attribute/mutations/permissions.py:35]

**`saleor/graphql/attribute/mutations/utils.py`**

- `get_product_ids_to_search_index_update_for_attribute_values` (function) — [saleor/graphql/attribute/mutations/utils.py:8]
- `get_page_ids_to_search_index_update_for_attribute_values` (function) — [saleor/graphql/attribute/mutations/utils.py:37]

**`saleor/graphql/attribute/mutations/validators.py`**

- `validate_value_is_unique` (function) — [saleor/graphql/attribute/mutations/validators.py:7]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/attribute/mutations/attribute_bulk_create.py` (680 lines)
- `saleor/graphql/attribute/mutations/attribute_bulk_update.py` (904 lines)
- `saleor/graphql/attribute/mutations/__init__.py` (27 lines)
- `saleor/graphql/attribute/mutations/attribute_create.py` (194 lines)
- `saleor/graphql/attribute/mutations/attribute_delete.py` (117 lines)
- `saleor/graphql/attribute/mutations/attribute_reorder_values.py` (115 lines)
- `saleor/graphql/attribute/mutations/attribute_update.py` (204 lines)
- `saleor/graphql/attribute/mutations/attribute_value_create.py` (126 lines)
- `saleor/graphql/attribute/mutations/attribute_value_delete.py` (88 lines)
- `saleor/graphql/attribute/mutations/attribute_value_update.py` (134 lines)
- `saleor/graphql/attribute/mutations/base_reorder_attributes.py` (170 lines)
- `saleor/graphql/attribute/mutations/mixins.py` (313 lines)
- `saleor/graphql/attribute/mutations/permissions.py` (58 lines)
- `saleor/graphql/attribute/mutations/utils.py` (52 lines)
- `saleor/graphql/attribute/mutations/validators.py` (18 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core/utils`, `saleor/plugins/openid_connect`, `saleor/graphql`
- Imported by: `saleor/graphql/attribute/tests/mutations`

Internal dependencies named in the source:

- `....attribute.AttributeEntityType`
- `....attribute.AttributeInputType`
- `....attribute.AttributeType`
- `....attribute.error_codes.AttributeBulkCreateErrorCode`
- `....attribute.error_codes.AttributeBulkUpdateErrorCode`
- `....attribute.error_codes.AttributeErrorCode`
- `....attribute.lock_objects.attribute_value_qs_select_for_update`
- `....attribute.models`
- `....core.exceptions.PermissionDenied`
- `....core.tracing.traced_atomic_transaction`
- `....core.utils.generate_unique_slug`
- `....core.utils.prepare_unique_slug`
- `....page.models`
- `....page.utils.mark_pages_search_vector_as_dirty_in_batches`
- `....product.models`
- `....webhook.event_types.WebhookEventAsyncType`
- `....webhook.utils.get_webhooks_for_event`
- `...core.ResolveInfo`
- `...core.context.ChannelContext`
- `...core.descriptions.ADDED_IN_322`
- `...core.descriptions.DEPRECATED_IN_3X_INPUT`
- `...core.doc_category.DOC_CATEGORY_ATTRIBUTES`
- `...core.enums.ErrorPolicyEnum`
- `...core.enums.MeasurementUnitsEnum`
- `...core.fields.JSONString`
- `...core.inputs.ReorderInput`
- `...core.mutations.BaseMutation`
- `...core.mutations.DeprecatedModelMutation`
- `...core.mutations.ModelDeleteMutation`
- `...core.mutations.ModelWithExtRefMutation`
- `...core.types.AttributeBulkCreateError`
- `...core.types.AttributeError`
- `...core.types.BaseInputObjectType`
- `...core.types.BaseObjectType`
- `...core.types.NonNullList`
- `...core.utils.WebhookEventInfo`
- `...core.utils.get_duplicated_values`
- `...core.utils.reordering.perform_reordering`
- `...core.validators.validate_one_of_args_is_in_mutation`
- `...plugins.dataloaders.get_plugin_manager_promise`
- `..descriptions.AttributeDescriptions`
- `..descriptions.AttributeValueDescriptions`
- `..enums.AttributeEntityTypeEnum`
- `..enums.AttributeInputTypeEnum`
- `..enums.AttributeTypeEnum`
- `..mutations.attribute_create.AttributeCreateInput`
- `..mutations.attribute_create.AttributeValueCreateInput`
- `..types.Attribute`
- `..types.AttributeValue`
- `.attribute_bulk_create.AttributeBulkCreate`
- `.attribute_bulk_create.DEPRECATED_ATTR_FIELDS`
- `.attribute_bulk_create.clean_values`
- `.attribute_bulk_update.AttributeBulkUpdate`
- `.attribute_create.AttributeCreate`
- `.attribute_create.AttributeValueCreateInput`
- `.attribute_create.AttributeValueInput`
- `.attribute_delete.AttributeDelete`
- `.attribute_reorder_values.AttributeReorderValues`
- `.attribute_update.AttributeUpdate`
- `.attribute_update.AttributeUpdateInput`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `8573e9994d06` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
