## Purpose

`saleor/graphql/attribute/tests` (`saleor/graphql/attribute/tests`) groups 8 source file(s) exposing 122 top-level declaration(s).

## Public surface

**`saleor/graphql/attribute/tests/benchmark/test_attribute.py`**

- `test_query_attribute` (function) — [saleor/graphql/attribute/tests/benchmark/test_attribute.py:11]
- `test_query_attributes` (function) — [saleor/graphql/attribute/tests/benchmark/test_attribute.py:53]
- `test_attribute_translation` (function) — [saleor/graphql/attribute/tests/benchmark/test_attribute.py:101]
- `test_attribute_value_translation` (function) — [saleor/graphql/attribute/tests/benchmark/test_attribute.py:138]

**`saleor/graphql/attribute/tests/deprecated/test_attributes.py`**

- `test_attributes_query_with_filter` (function) — [saleor/graphql/attribute/tests/deprecated/test_attributes.py:28]

**`saleor/graphql/attribute/tests/test_utils.py`**

- `test_clean_input_for_product` (function) — [saleor/graphql/attribute/tests/test_utils.py:30]
- `test_clean_attribute_input_for_product_no_values_given` (function) — [saleor/graphql/attribute/tests/test_utils.py:64]
- `test_clean_attribute_input_for_product_too_many_values_given` (function) — [saleor/graphql/attribute/tests/test_utils.py:105]
- `test_clean_attribute_input_for_product_empty_values_given` (function) — [saleor/graphql/attribute/tests/test_utils.py:149]
- `test_clean_attribute_input_for_product_lack_of_required_attribute` (function) — [saleor/graphql/attribute/tests/test_utils.py:193]
- `test_clean_attribute_input_for_product_creation_multiple_errors` (function) — [saleor/graphql/attribute/tests/test_utils.py:231]
- `test_clean_attribute_input_for_page` (function) — [saleor/graphql/attribute/tests/test_utils.py:282]
- `test_clean_attribute_input_for_page_no_values_given` (function) — [saleor/graphql/attribute/tests/test_utils.py:316]
- `test_clean_attribute_input_for_page_too_many_values_given` (function) — [saleor/graphql/attribute/tests/test_utils.py:357]
- `test_clean_attribute_input_for_page_empty_values_given` (function) — [saleor/graphql/attribute/tests/test_utils.py:401]
- `test_clean_attribute_input_for_page_lack_of_required_attribute` (function) — [saleor/graphql/attribute/tests/test_utils.py:445]
- `test_clean_attribute_input_for_page_multiple_errors` (function) — [saleor/graphql/attribute/tests/test_utils.py:481]
- `test_clean_variant_attribute_input` (function) — [saleor/graphql/attribute/tests/test_utils.py:531]
- `test_clean_variant_attribute_input_no_values_given` (function) — [saleor/graphql/attribute/tests/test_utils.py:565]
- `test_clean_variant_attribute_duplicated_values_given` (function) — [saleor/graphql/attribute/tests/test_utils.py:606]
- `test_clean_variant_attribute_input_empty_values_given` (function) — [saleor/graphql/attribute/tests/test_utils.py:651]
- `test_clean_variant_attribute_too_many_values_given` (function) — [saleor/graphql/attribute/tests/test_utils.py:685]
- `test_clean_variant_attribute_empty_values_given` (function) — [saleor/graphql/attribute/tests/test_utils.py:727]
- `test_clean_variant_attribute_input_multiple_errors` (function) — [saleor/graphql/attribute/tests/test_utils.py:769]
- `test_clean_attributes_with_file_input_type_for_product` (function) — [saleor/graphql/attribute/tests/test_utils.py:820]
- `test_clean_attributes_with_file_input_type_for_product_no_file_given` (function) — [saleor/graphql/attribute/tests/test_utils.py:855]
- `test_clean_not_required_attrs_with_file_input_type_for_product_no_file_given` (function) — [saleor/graphql/attribute/tests/test_utils.py:896]
- `test_clean_attributes_with_file_input_type_for_product_empty_file_value` (function) — [saleor/graphql/attribute/tests/test_utils.py:929]
- `test_clean_numeric_attributes_input_for_product` (function) — [saleor/graphql/attribute/tests/test_utils.py:971]
- `test_clean_numeric_attributes_input_for_product_not_numeric_value_given` (function) — [saleor/graphql/attribute/tests/test_utils.py:999]
- `test_validate_numeric_attributes_input_for_product_blank_value` (function) — [saleor/graphql/attribute/tests/test_utils.py:1034]
- `test_validate_numeric_attributes_input_none_as_values` (function) — [saleor/graphql/attribute/tests/test_utils.py:1069]
- `test_validate_numeric_attributes_input_for_product_more_than_one_value_given` (function) — [saleor/graphql/attribute/tests/test_utils.py:1103]
- `test_validate_selectable_attributes_by_value` (function) — [saleor/graphql/attribute/tests/test_utils.py:1138]
- `test_validate_selectable_attributes_by_id` (function) — [saleor/graphql/attribute/tests/test_utils.py:1177]
- `test_clean_selectable_attributes_pass_null_value` (function) — [saleor/graphql/attribute/tests/test_utils.py:1216]
- `test_clean_selectable_attribute_by_id_and_value` (function) — [saleor/graphql/attribute/tests/test_utils.py:1250]
- `test_clean_selectable_attribute_by_external_reference` (function) — [saleor/graphql/attribute/tests/test_utils.py:1289]
- `test_clean_selectable_attribute_by_id_and_external_reference` (function) — [saleor/graphql/attribute/tests/test_utils.py:1320]
- `test_clean_selectable_attribute_by_value_and_external_reference` (function) — [saleor/graphql/attribute/tests/test_utils.py:1359]
- `test_clean_multiselect_attribute_by_id_and_value` (function) — [saleor/graphql/attribute/tests/test_utils.py:1390]
- `test_clean_multiselect_attribute_duplicated_values` (function) — [saleor/graphql/attribute/tests/test_utils.py:1429]
- `test_clean_multiselect_attribute_duplicated_ids` (function) — [saleor/graphql/attribute/tests/test_utils.py:1469]
- `test_clean_multiselect_attribute_duplicated_external_refs` (function) — [saleor/graphql/attribute/tests/test_utils.py:1509]
- `test_clean_selectable_attribute_max_length_exceeded` (function) — [saleor/graphql/attribute/tests/test_utils.py:1549]
- _…and 49 more in this file_

**`saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py`**

- `test_reference_handler_clean_and_validate_product_reference` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:12]
- `test_reference_handler_clean_and_validate_page_reference` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:33]
- `test_reference_handler_clean_and_validate_variant_reference` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:54]
- `test_reference_handler_clean_and_validate_product_reference_with_reference_types` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:77]
- `test_reference_handler_clean_and_validate_page_reference_with_reference_types` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:99]
- `test_reference_handler_clean_and_validate_variant_reference_with_reference_types` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:121]
- `test_reference_handler_clean_and_validate_category_reference` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:145]
- `test_reference_handler_clean_and_validate_collection_reference` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:166]
- `test_reference_handler_clean_and_validate_invalid_product_reference_type` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:189]
- `test_reference_handler_clean_and_validate_invalid_product_variant_ref_type` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:213]
- `test_reference_handler_clean_and_validate_invalid_page_reference_type` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:237]
- `test_single_reference_handler_clean_and_validate_page_reference` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:257]
- `test_single_reference_handler_clean_and_validate_variant_reference` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:276]
- `test_single_reference_handler_clean_and_validate_category_reference` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:295]
- `test_single_reference_handler_clean_and_validate_collection_reference` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:314]
- `test_single_reference_handler_clean_and_validate_product_ref_with_reference_types` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:333]
- `test_single_reference_handler_clean_and_validate_page_ref_with_reference_types` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:356]
- `test_single_reference_handler_clean_and_validate_variant_ref_with_reference_types` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:377]
- `test_single_reference_handler_clean_and_validate_success` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:400]
- `test_reference_handler_clean_and_validate_value_required` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:419]
- `test_single_reference_handlers_clean_and_validate_value_required` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:439]
- `test_reference_handler_clean_and_validate_invalid_reference` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:459]
- `test_single_reference_handler_clean_and_validate_invalid_reference` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:482]
- `test_single_reference_handler_clean_and_validate_invalid_product_reference_type` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:501]
- `test_single_reference_handler_clean_and_validate_invalid_product_variant_ref_type` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:525]
- `test_single_reference_handler_clean_and_validate_invalid_page_reference_type` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:549]
- `test_reference_handler_pre_save_value` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:571]
- `test_single_reference_handler_pre_save_value` (function) — [saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py:599]

## How it works

The module's files, as provided to this run:

- `saleor/graphql/attribute/tests/__init__.py` (1 lines)
- `saleor/graphql/attribute/tests/benchmark/__init__.py` (1 lines)
- `saleor/graphql/attribute/tests/benchmark/test_attribute.py` (178 lines)
- `saleor/graphql/attribute/tests/deprecated/__init__.py` (1 lines)
- `saleor/graphql/attribute/tests/deprecated/test_attributes.py` (71 lines)
- `saleor/graphql/attribute/tests/test_utils.py` (3014 lines)
- `saleor/graphql/attribute/tests/type_handlers/__init__.py` (1 lines)
- `saleor/graphql/attribute/tests/type_handlers/test_reference_handler.py` (624 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`, `saleor/core/utils`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `.....attribute.models.Attribute`
- `.....attribute.models.AttributeTranslation`
- `.....attribute.models.AttributeValueTranslation`
- `.....attribute.utils.associate_attribute_values_to_instance`
- `.....channel.models.Channel`
- `.....channel.utils.DEPRECATION_WARNING_MESSAGE`
- `.....product.ProductTypeKind`
- `.....product.models.Category`
- `.....product.models.Product`
- `.....product.models.ProductType`
- `....attribute.AttributeInputType`
- `....attribute.models.AttributeValue`
- `....attribute.utils.associate_attribute_values_to_instance`
- `....product.error_codes.ProductErrorCode`
- `....tests.utils.get_graphql_content`
- `...enums.AttributeValueBulkActionEnum`
- `...utils.shared.AttrValuesInput`
- `...utils.type_handlers.AttributeInputErrors`
- `...utils.type_handlers.ReferenceAttributeHandler`
- `..enums.AttributeValueBulkActionEnum`
- `..shared_filters.validate_attribute_value_input`
- `..utils.attribute_assignment.AttributeAssignmentMixin`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `63dba8272167` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
