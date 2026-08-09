## Purpose

`saleor/graphql/attribute/utils` (`saleor/graphql/attribute/utils`) groups 4 source file(s) exposing 55 top-level declaration(s).

## Public surface

**`saleor/graphql/attribute/utils/attribute_assignment.py`**

- `AttributeAssignmentMixin` (class) — [saleor/graphql/attribute/utils/attribute_assignment.py:52]
- `clean_input` (function) — [saleor/graphql/attribute/utils/attribute_assignment.py:123]
- `prepare_error_list_from_error_attribute_mapping` (function) — [saleor/graphql/attribute/utils/attribute_assignment.py:260]
- `pre_save_values` (function) — [saleor/graphql/attribute/utils/attribute_assignment.py:300]
- `save` (function) — [saleor/graphql/attribute/utils/attribute_assignment.py:399]

**`saleor/graphql/attribute/utils/shared.py`**

- `AssignedAttributeData` (class) — [saleor/graphql/attribute/utils/shared.py:31]
- `AttrValuesForSelectableFieldInput` (class) — [saleor/graphql/attribute/utils/shared.py:40]
- `AttrValuesInput` (class) — [saleor/graphql/attribute/utils/shared.py:47]
- `EntityTypeData` (class) — [saleor/graphql/attribute/utils/shared.py:67]
- `get_assignment_model_and_fk` (function) — [saleor/graphql/attribute/utils/shared.py:94]
- `get_assigned_attribute_value_if_exists` (function) — [saleor/graphql/attribute/utils/shared.py:132]
- `get_assigned_attribute_values_map` (function) — [saleor/graphql/attribute/utils/shared.py:143]
- `has_input_modified_attribute_values` (function) — [saleor/graphql/attribute/utils/shared.py:153]
- `get_attribute_to_values_map_for_variant` (function) — [saleor/graphql/attribute/utils/shared.py:175]
- `get_values_from_pre_save_bulk_data` (function) — [saleor/graphql/attribute/utils/shared.py:213]

**`saleor/graphql/attribute/utils/type_handlers.py`**

- `AttributeInputErrors` (class) — [saleor/graphql/attribute/utils/type_handlers.py:39]
- `AttributeTypeHandler` (class) — [saleor/graphql/attribute/utils/type_handlers.py:85]
- `clean_and_validate` (function) — [saleor/graphql/attribute/utils/type_handlers.py:101]
- `pre_save_value` (function) — [saleor/graphql/attribute/utils/type_handlers.py:107]
- `prepare_attribute_values` (function) — [saleor/graphql/attribute/utils/type_handlers.py:144]
- `prepare_attribute_values_with_external_reference` (function) — [saleor/graphql/attribute/utils/type_handlers.py:182]
- `get_existing_slugs` (function) — [saleor/graphql/attribute/utils/type_handlers.py:204]
- `SelectableAttributeHandler` (class) — [saleor/graphql/attribute/utils/type_handlers.py:215]
- `get_selectable_input` (function) — [saleor/graphql/attribute/utils/type_handlers.py:218]
- `clean_and_validate` (function) — [saleor/graphql/attribute/utils/type_handlers.py:227]
- `pre_save_value` (function) — [saleor/graphql/attribute/utils/type_handlers.py:290]
- `MultiSelectableAttributeHandler` (class) — [saleor/graphql/attribute/utils/type_handlers.py:356]
- `clean_and_validate` (function) — [saleor/graphql/attribute/utils/type_handlers.py:359]
- `pre_save_value` (function) — [saleor/graphql/attribute/utils/type_handlers.py:405]
- `FileAttributeHandler` (class) — [saleor/graphql/attribute/utils/type_handlers.py:495]
- `clean_and_validate` (function) — [saleor/graphql/attribute/utils/type_handlers.py:498]
- `pre_save_value` (function) — [saleor/graphql/attribute/utils/type_handlers.py:515]
- `ReferenceAttributeHandler` (class) — [saleor/graphql/attribute/utils/type_handlers.py:538]
- `get_references` (function) — [saleor/graphql/attribute/utils/type_handlers.py:541]
- `clean_and_validate` (function) — [saleor/graphql/attribute/utils/type_handlers.py:546]
- `get_references_with_invalid_reference_types` (function) — [saleor/graphql/attribute/utils/type_handlers.py:596]
- `pre_save_value` (function) — [saleor/graphql/attribute/utils/type_handlers.py:629]
- `PlainTextAttributeHandler` (class) — [saleor/graphql/attribute/utils/type_handlers.py:655]
- `clean_and_validate` (function) — [saleor/graphql/attribute/utils/type_handlers.py:658]
- `pre_save_value` (function) — [saleor/graphql/attribute/utils/type_handlers.py:665]
- `RichTextAttributeHandler` (class) — [saleor/graphql/attribute/utils/type_handlers.py:677]
- `clean_and_validate` (function) — [saleor/graphql/attribute/utils/type_handlers.py:680]
- `pre_save_value` (function) — [saleor/graphql/attribute/utils/type_handlers.py:688]
- `NumericAttributeHandler` (class) — [saleor/graphql/attribute/utils/type_handlers.py:700]
- `clean_and_validate` (function) — [saleor/graphql/attribute/utils/type_handlers.py:703]
- `pre_save_value` (function) — [saleor/graphql/attribute/utils/type_handlers.py:723]
- `DateTimeAttributeHandler` (class) — [saleor/graphql/attribute/utils/type_handlers.py:734]
- `clean_and_validate` (function) — [saleor/graphql/attribute/utils/type_handlers.py:737]
- `pre_save_value` (function) — [saleor/graphql/attribute/utils/type_handlers.py:745]
- `BooleanAttributeHandler` (class) — [saleor/graphql/attribute/utils/type_handlers.py:760]
- `clean_and_validate` (function) — [saleor/graphql/attribute/utils/type_handlers.py:763]
- `pre_save_value` (function) — [saleor/graphql/attribute/utils/type_handlers.py:769]
- `LegacyValuesHandler` (class) — [saleor/graphql/attribute/utils/type_handlers.py:786]
- `clean_and_validate` (function) — [saleor/graphql/attribute/utils/type_handlers.py:792]
- `pre_save_value` (function) — [saleor/graphql/attribute/utils/type_handlers.py:834]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/attribute/utils/__init__.py` (1 lines)
- `saleor/graphql/attribute/utils/attribute_assignment.py` (477 lines)
- `saleor/graphql/attribute/utils/shared.py` (250 lines)
- `saleor/graphql/attribute/utils/type_handlers.py` (846 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core/db`, `saleor/graphql`, `saleor/plugins/openid_connect`, `saleor/core/utils`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....attribute.AttributeEntityType`
- `....attribute.AttributeInputType`
- `....attribute.models`
- `....attribute.models.Attribute`
- `....attribute.models.AttributeValue`
- `....attribute.utils.associate_attribute_values_to_instance`
- `....core.editorjs.editorjs_to_text`
- `....core.utils.text.safe_truncate`
- `....core.utils.url.get_default_storage_root_url`
- `....page.error_codes.PageErrorCode`
- `....page.models`
- `....product.error_codes.ProductErrorCode`
- `....product.models`
- `...core.utils.from_global_id_or_error`
- `...core.utils.get_duplicated_values`
- `...core.validators.validate_one_of_args_is_in_mutation`
- `...utils.get_nodes`
- `..enums.AttributeValueBulkActionEnum`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `143e15b3724a` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
