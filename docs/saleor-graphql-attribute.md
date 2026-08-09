## Purpose

`saleor/graphql/attribute` (`saleor/graphql/attribute`) groups 11 source file(s) exposing 239 top-level declaration(s).

## Public surface

**`saleor/graphql/attribute/bulk_mutations.py`**

- `AttributeBulkDelete` (class) — [saleor/graphql/attribute/bulk_mutations.py:27]
- `Arguments` (class) — [saleor/graphql/attribute/bulk_mutations.py:28]
- `Meta` (class) — [saleor/graphql/attribute/bulk_mutations.py:38]
- `perform_mutation` (function) — [saleor/graphql/attribute/bulk_mutations.py:58]
- `get_product_ids_to_update` (function) — [saleor/graphql/attribute/bulk_mutations.py:80]
- `bulk_action` (function) — [saleor/graphql/attribute/bulk_mutations.py:104]
- `AttributeValueBulkDelete` (class) — [saleor/graphql/attribute/bulk_mutations.py:113]
- `Arguments` (class) — [saleor/graphql/attribute/bulk_mutations.py:114]
- `Meta` (class) — [saleor/graphql/attribute/bulk_mutations.py:124]
- `perform_mutation` (function) — [saleor/graphql/attribute/bulk_mutations.py:148]
- `bulk_action` (function) — [saleor/graphql/attribute/bulk_mutations.py:170]
- `get_product_ids_to_update` (function) — [saleor/graphql/attribute/bulk_mutations.py:187]

**`saleor/graphql/attribute/descriptions.py`**

- `AttributeDescriptions` (class) — [saleor/graphql/attribute/descriptions.py:4]
- `AttributeValueDescriptions` (class) — [saleor/graphql/attribute/descriptions.py:29]

**`saleor/graphql/attribute/enums.py`**

- `AttributeValueBulkActionEnum` (class) — [saleor/graphql/attribute/enums.py:24]

**`saleor/graphql/attribute/filters.py`**

- `filter_attributes_by_product_types` (function) — [saleor/graphql/attribute/filters.py:44]
- `filter_attribute_search` (function) — [saleor/graphql/attribute/filters.py:97]
- `filter_by_attribute_type` (function) — [saleor/graphql/attribute/filters.py:103]
- `search_attribute_values` (function) — [saleor/graphql/attribute/filters.py:109]
- `AttributeValueFilter` (class) — [saleor/graphql/attribute/filters.py:114]
- `Meta` (class) — [saleor/graphql/attribute/filters.py:119]
- `filter_search` (function) — [saleor/graphql/attribute/filters.py:124]
- `AttributeFilter` (class) — [saleor/graphql/attribute/filters.py:131]
- `Meta` (class) — [saleor/graphql/attribute/filters.py:140]
- `filter_in_collection` (function) — [saleor/graphql/attribute/filters.py:151]
- `filter_in_category` (function) — [saleor/graphql/attribute/filters.py:158]
- `AttributeFilterInput` (class) — [saleor/graphql/attribute/filters.py:166]
- `Meta` (class) — [saleor/graphql/attribute/filters.py:167]
- `AttributeValueFilterInput` (class) — [saleor/graphql/attribute/filters.py:172]
- `Meta` (class) — [saleor/graphql/attribute/filters.py:173]
- `AttributeInputTypeEnumFilterInput` (class) — [saleor/graphql/attribute/filters.py:178]
- `Meta` (class) — [saleor/graphql/attribute/filters.py:186]
- `AttributeEntityTypeEnumFilterInput` (class) — [saleor/graphql/attribute/filters.py:190]
- `Meta` (class) — [saleor/graphql/attribute/filters.py:198]
- `AttributeTypeEnumFilterInput` (class) — [saleor/graphql/attribute/filters.py:202]
- `Meta` (class) — [saleor/graphql/attribute/filters.py:210]
- `MeasurementUnitsEnumFilterInput` (class) — [saleor/graphql/attribute/filters.py:214]
- `Meta` (class) — [saleor/graphql/attribute/filters.py:222]
- `filter_attribute_name` (function) — [saleor/graphql/attribute/filters.py:226]
- `filter_attribute_slug` (function) — [saleor/graphql/attribute/filters.py:230]
- `filter_with_choices` (function) — [saleor/graphql/attribute/filters.py:234]
- `filter_attribute_input_type` (function) — [saleor/graphql/attribute/filters.py:243]
- `filter_attribute_entity_type` (function) — [saleor/graphql/attribute/filters.py:247]
- `filter_attribute_type` (function) — [saleor/graphql/attribute/filters.py:251]
- `filter_attribute_unit` (function) — [saleor/graphql/attribute/filters.py:255]
- `where_filter_attributes_by_product_types` (function) — [saleor/graphql/attribute/filters.py:259]
- `AttributeWhere` (class) — [saleor/graphql/attribute/filters.py:266]
- `Meta` (class) — [saleor/graphql/attribute/filters.py:293]
- `filter_in_collection` (function) — [saleor/graphql/attribute/filters.py:297]
- `filter_in_category` (function) — [saleor/graphql/attribute/filters.py:304]
- `AttributeWhereInput` (class) — [saleor/graphql/attribute/filters.py:312]
- `Meta` (class) — [saleor/graphql/attribute/filters.py:313]
- `AttributeValueWhere` (class) — [saleor/graphql/attribute/filters.py:319]
- `Meta` (class) — [saleor/graphql/attribute/filters.py:328]
- `filter_by_name` (function) — [saleor/graphql/attribute/filters.py:333]
- _…and 3 more in this file_

**`saleor/graphql/attribute/resolvers.py`**

- `resolve_attributes` (function) — [saleor/graphql/attribute/resolvers.py:6]

**`saleor/graphql/attribute/schema.py`**

- `AttributeQueries` (class) — [saleor/graphql/attribute/schema.py:35]
- `resolve_attributes` (function) — [saleor/graphql/attribute/schema.py:66]
- `resolve_attribute` (function) — [saleor/graphql/attribute/schema.py:76]
- `AttributeMutations` (class) — [saleor/graphql/attribute/schema.py:87]

**`saleor/graphql/attribute/shared_filters.py`**

- `AssignedAttributeReferenceInput` (class) — [saleor/graphql/attribute/shared_filters.py:29]
- `AssignedAttributeValueInput` (class) — [saleor/graphql/attribute/shared_filters.py:61]
- `AssignedAttributeWhereInput` (class) — [saleor/graphql/attribute/shared_filters.py:90]
- `SharedContainsFilterParams` (class) — [saleor/graphql/attribute/shared_filters.py:104]
- `get_attribute_values_by_slug_or_name_value` (function) — [saleor/graphql/attribute/shared_filters.py:114]
- `get_attribute_values_by_numeric_value` (function) — [saleor/graphql/attribute/shared_filters.py:133]
- `get_attribute_values_by_boolean_value` (function) — [saleor/graphql/attribute/shared_filters.py:150]
- `get_attribute_values_by_date_value` (function) — [saleor/graphql/attribute/shared_filters.py:162]
- `get_attribute_values_by_date_time_value` (function) — [saleor/graphql/attribute/shared_filters.py:178]
- `get_attribute_values_by_referenced_page_slugs` (function) — [saleor/graphql/attribute/shared_filters.py:207]
- `get_attribute_values_by_referenced_page_ids` (function) — [saleor/graphql/attribute/shared_filters.py:215]
- `get_attribute_values_by_referenced_category_slugs` (function) — [saleor/graphql/attribute/shared_filters.py:236]
- `get_attribute_values_by_referenced_category_ids` (function) — [saleor/graphql/attribute/shared_filters.py:244]
- `get_attribute_values_by_referenced_collection_slugs` (function) — [saleor/graphql/attribute/shared_filters.py:265]
- `get_attribute_values_by_referenced_collection_ids` (function) — [saleor/graphql/attribute/shared_filters.py:273]
- `get_attribute_values_by_referenced_product_slugs` (function) — [saleor/graphql/attribute/shared_filters.py:294]
- `get_attribute_values_by_referenced_product_ids` (function) — [saleor/graphql/attribute/shared_filters.py:302]
- `get_attribute_values_by_referenced_variant_skus` (function) — [saleor/graphql/attribute/shared_filters.py:323]
- `get_attribute_values_by_referenced_variant_ids` (function) — [saleor/graphql/attribute/shared_filters.py:331]
- `clean_up_referenced_global_ids` (function) — [saleor/graphql/attribute/shared_filters.py:339]
- `validate_attribute_value_reference_input` (function) — [saleor/graphql/attribute/shared_filters.py:384]
- `validate_attribute_value_input` (function) — [saleor/graphql/attribute/shared_filters.py:474]

**`saleor/graphql/attribute/sorters.py`**

- `AttributeSortField` (class) — [saleor/graphql/attribute/sorters.py:5]
- `Meta` (class) — [saleor/graphql/attribute/sorters.py:16]
- `description` (function) — [saleor/graphql/attribute/sorters.py:20]
- `AttributeSortingInput` (class) — [saleor/graphql/attribute/sorters.py:53]
- `Meta` (class) — [saleor/graphql/attribute/sorters.py:54]
- `AttributeChoicesSortField` (class) — [saleor/graphql/attribute/sorters.py:60]
- `Meta` (class) — [saleor/graphql/attribute/sorters.py:64]
- `description` (function) — [saleor/graphql/attribute/sorters.py:68]
- `AttributeChoicesSortingInput` (class) — [saleor/graphql/attribute/sorters.py:78]
- `Meta` (class) — [saleor/graphql/attribute/sorters.py:79]

**`saleor/graphql/attribute/types.py`**

- `get_reference_pk` (function) — [saleor/graphql/attribute/types.py:87]
- `resolve_variant_name` (function) — [saleor/graphql/attribute/types.py:118]
- `AttributeValue` (class) — [saleor/graphql/attribute/types.py:144]
- `Meta` (class) — [saleor/graphql/attribute/types.py:178]
- `resolve_name` (function) — [saleor/graphql/attribute/types.py:185]
- `resolve_input_type` (function) — [saleor/graphql/attribute/types.py:201]
- `resolve_file` (function) — [saleor/graphql/attribute/types.py:212]
- `resolve_reference` (function) — [saleor/graphql/attribute/types.py:221]
- `prepare_reference` (function) — [saleor/graphql/attribute/types.py:226]
- `resolve_date_time` (function) — [saleor/graphql/attribute/types.py:239]
- `resolve_date` (function) — [saleor/graphql/attribute/types.py:256]
- `AttributeValueCountableConnection` (class) — [saleor/graphql/attribute/types.py:271]
- `Meta` (class) — [saleor/graphql/attribute/types.py:272]
- `Attribute` (class) — [saleor/graphql/attribute/types.py:277]
- `Meta` (class) — [saleor/graphql/attribute/types.py:410]
- `resolve_reference_types` (function) — [saleor/graphql/attribute/types.py:420]
- `resolve_choices` (function) — [saleor/graphql/attribute/types.py:438]
- `resolve_value_required` (function) — [saleor/graphql/attribute/types.py:460]
- `resolve_visible_in_storefront` (function) — [saleor/graphql/attribute/types.py:467]
- `resolve_filterable_in_storefront` (function) — [saleor/graphql/attribute/types.py:474]
- `resolve_filterable_in_dashboard` (function) — [saleor/graphql/attribute/types.py:481]
- `resolve_storefront_search_position` (function) — [saleor/graphql/attribute/types.py:488]
- `resolve_available_in_grid` (function) — [saleor/graphql/attribute/types.py:495]
- `resolve_with_choices` (function) — [saleor/graphql/attribute/types.py:501]
- `resolve_product_types` (function) — [saleor/graphql/attribute/types.py:507]
- `resolve_product_variant_types` (function) — [saleor/graphql/attribute/types.py:518]
- `AttributeCountableConnection` (class) — [saleor/graphql/attribute/types.py:529]
- `Meta` (class) — [saleor/graphql/attribute/types.py:530]
- `AssignedVariantAttribute` (class) — [saleor/graphql/attribute/types.py:535]
- `Meta` (class) — [saleor/graphql/attribute/types.py:549]
- `AttributeInput` (class) — [saleor/graphql/attribute/types.py:556]
- `Meta` (class) — [saleor/graphql/attribute/types.py:610]
- `AttributeValueSelectableTypeInput` (class) — [saleor/graphql/attribute/types.py:614]
- `Meta` (class) — [saleor/graphql/attribute/types.py:627]
- `AttributeValueInput` (class) — [saleor/graphql/attribute/types.py:641]
- `Meta` (class) — [saleor/graphql/attribute/types.py:698]
- `get_attribute_values` (function) — [saleor/graphql/attribute/types.py:702]
- `SelectedAttribute` (class) — [saleor/graphql/attribute/types.py:720]
- `Meta` (class) — [saleor/graphql/attribute/types.py:731]
- `resolve_attribute` (function) — [saleor/graphql/attribute/types.py:736]
- _…and 101 more in this file_

**`saleor/graphql/attribute/unions.py`**

- `ReferenceType` (class) — [saleor/graphql/attribute/unions.py:10]
- `Meta` (class) — [saleor/graphql/attribute/unions.py:11]
- `resolve_type` (function) — [saleor/graphql/attribute/unions.py:22]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/attribute/__init__.py` (1 lines)
- `saleor/graphql/attribute/bulk_mutations.py` (206 lines)
- `saleor/graphql/attribute/descriptions.py` (54 lines)
- `saleor/graphql/attribute/enums.py` (28 lines)
- `saleor/graphql/attribute/filters.py` (345 lines)
- `saleor/graphql/attribute/resolvers.py` (11 lines)
- `saleor/graphql/attribute/schema.py` (105 lines)
- `saleor/graphql/attribute/shared_filters.py` (568 lines)
- `saleor/graphql/attribute/sorters.py` (82 lines)
- `saleor/graphql/attribute/types.py` (1699 lines)
- `saleor/graphql/attribute/unions.py` (28 lines)

## Interactions

- Imports from: `saleor/graphql`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...attribute.AttributeEntityType`
- `...attribute.AttributeInputType`
- `...attribute.AttributeType`
- `...attribute.lock_objects.attribute_value_qs_select_for_update`
- `...attribute.models`
- `...attribute.models.Attribute`
- `...attribute.models.AttributeValue`
- `...attribute.models.product.AttributeProduct`
- `...attribute.models.product_variant.AttributeVariant`
- `...channel.models.Channel`
- `...page.models`
- `...permission.utils.has_one_of_permissions`
- `...product.models`
- `...product.models.ALL_PRODUCTS_PERMISSIONS`
- `...webhook.event_types.WebhookEventAsyncType`
- `...webhook.utils.get_webhooks_for_event`
- `..channel.filters.get_channel_slug_from_filter_data`
- `..core.ResolveInfo`
- `..core.connection.create_connection_slice`
- `..core.connection.filter_connection_queryset`
- `..core.const.DEFAULT_NESTED_LIST_LIMIT`
- `..core.context.ChannelContext`
- `..core.context.ChannelQsContext`
- `..core.context.get_database_connection_name`
- `..core.descriptions.DEPRECATED_IN_3X_INPUT`
- `..core.descriptions.RICH_CONTENT`
- `..core.doc_category.DOC_CATEGORY_ATTRIBUTES`
- `..core.enums.LanguageCodeEnum`
- `..core.enums.MeasurementUnitsEnum`
- `..core.enums.to_enum`
- `..core.fields.BaseField`
- `..core.fields.ConnectionField`
- `..core.fields.FilterConnectionField`
- `..core.fields.JSONString`
- `..core.filters.DecimalFilterInput`
- `..core.filters.where_input.ContainsFilterInput`
- `..core.filters.where_input.StringFilterInput`
- `..core.mutations.ModelBulkDeleteMutation`
- `..core.scalars.Date`
- `..core.scalars.DateTime`
- `..core.scalars.JSON`
- `..core.scalars.PositiveInt`
- `..core.types.AttributeError`
- `..core.types.BaseEnum`
- `..core.types.DateRangeInput`
- `..core.types.DateTimeRangeInput`
- `..core.types.NonNullList`
- `..core.types.SortInputObjectType`
- `..core.types.base.BaseInputObjectType`
- `..core.types.common.NonNullList`
- `..core.types.context.ChannelContextType`
- `..core.types.context.ChannelContextTypeForObjectType`
- `..core.utils.WebhookEventInfo`
- `..core.utils.from_global_id_or_error`
- `..core.utils.resolvers.resolve_by_global_id_slug_or_ext_ref`
- `..core.utils.str_to_enum`
- `..decorators.check_attribute_required_permissions`
- `..meta.types.ObjectWithMetadata`
- `..page.dataloaders.PageByIdLoader`
- `..page.types.PageType`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `87c6d52233f8` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
