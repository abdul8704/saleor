## Purpose

`saleor/attribute/tests` (`saleor/attribute/tests`) groups 7 source file(s) exposing 81 top-level declaration(s).

## Public surface

**`saleor/attribute/tests/fixtures/attribute.py`**

- `attribute_generator` (function) — [saleor/attribute/tests/fixtures/attribute.py:14]
- `create_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:15]
- `attribute_value_generator` (function) — [saleor/attribute/tests/fixtures/attribute.py:42]
- `create_attribute_value` (function) — [saleor/attribute/tests/fixtures/attribute.py:43]
- `attribute_values_generator` (function) — [saleor/attribute/tests/fixtures/attribute.py:66]
- `create_attribute_values` (function) — [saleor/attribute/tests/fixtures/attribute.py:67]
- `color_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:111]
- `color_attribute_with_translations` (function) — [saleor/attribute/tests/fixtures/attribute.py:138]
- `second_color_attribute_with_translations` (function) — [saleor/attribute/tests/fixtures/attribute.py:158]
- `attribute_without_values` (function) — [saleor/attribute/tests/fixtures/attribute.py:178]
- `multiselect_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:192]
- `date_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:214]
- `date_time_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:243]
- `attribute_choices_for_sorting` (function) — [saleor/attribute/tests/fixtures/attribute.py:273]
- `boolean_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:289]
- `rich_text_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:315]
- `rich_text_attribute_page_type` (function) — [saleor/attribute/tests/fixtures/attribute.py:336]
- `rich_text_attribute_with_many_values` (function) — [saleor/attribute/tests/fixtures/attribute.py:357]
- `plain_text_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:375]
- `plain_text_attribute_page_type` (function) — [saleor/attribute/tests/fixtures/attribute.py:396]
- `color_attribute_without_values` (function) — [saleor/attribute/tests/fixtures/attribute.py:417]
- `pink_attribute_value` (function) — [saleor/attribute/tests/fixtures/attribute.py:429]
- `size_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:437]
- `weight_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:460]
- `numeric_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:477]
- `numeric_attribute_without_unit` (function) — [saleor/attribute/tests/fixtures/attribute.py:498]
- `file_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:514]
- `file_attribute_with_file_input_type_without_values` (function) — [saleor/attribute/tests/fixtures/attribute.py:539]
- `swatch_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:549]
- `product_type_page_reference_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:576]
- `page_type_page_reference_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:587]
- `product_type_product_reference_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:598]
- `page_type_product_reference_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:609]
- `product_type_variant_reference_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:620]
- `page_type_variant_reference_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:631]
- `product_type_category_reference_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:642]
- `page_type_category_reference_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:653]
- `product_type_collection_reference_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:664]
- `page_type_collection_reference_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:675]
- `product_type_page_single_reference_attribute` (function) — [saleor/attribute/tests/fixtures/attribute.py:686]
- _…and 15 more in this file_

**`saleor/attribute/tests/fixtures/translation.py`**

- `translated_attribute` (function) — [saleor/attribute/tests/fixtures/translation.py:9]
- `translated_attribute_value` (function) — [saleor/attribute/tests/fixtures/translation.py:17]
- `translated_page_unique_attribute_value` (function) — [saleor/attribute/tests/fixtures/translation.py:26]
- `translated_product_unique_attribute_value` (function) — [saleor/attribute/tests/fixtures/translation.py:41]
- `translated_variant_unique_attribute_value` (function) — [saleor/attribute/tests/fixtures/translation.py:56]

**`saleor/attribute/tests/model_helpers.py`**

- `get_page_attributes` (function) — [saleor/attribute/tests/model_helpers.py:15]
- `get_page_attribute_values` (function) — [saleor/attribute/tests/model_helpers.py:23]
- `get_product_attributes` (function) — [saleor/attribute/tests/model_helpers.py:32]
- `get_product_attribute_values` (function) — [saleor/attribute/tests/model_helpers.py:47]

**`saleor/attribute/tests/models/test_base.py`**

- `test_attribute_value_setting_up_max_sort_order` (function) — [saleor/attribute/tests/models/test_base.py:5]
- `test_attribute_value_using_max_sort_order_from_parent` (function) — [saleor/attribute/tests/models/test_base.py:24]
- `test_attribute_value_sort_order_when_attribute_has_other_values` (function) — [saleor/attribute/tests/models/test_base.py:44]
- `test_max_sort_order_when_deleting_attribute_value` (function) — [saleor/attribute/tests/models/test_base.py:66]
- `test_max_sort_order_none_when_deleting_attribute_value_with_sort_order_0` (function) — [saleor/attribute/tests/models/test_base.py:91]
- `test_max_sort_order_0_when_deleting_attribute_value_with_sort_order_0` (function) — [saleor/attribute/tests/models/test_base.py:121]

**`saleor/attribute/tests/test_utils.py`**

- `test_associate_attribute_to_non_product_instance` (function) — [saleor/attribute/tests/test_utils.py:19]
- `test_associate_attribute_to_product_instance_from_different_attribute` (function) — [saleor/attribute/tests/test_utils.py:33]
- `test_associate_attribute_to_product_instance_without_values` (function) — [saleor/attribute/tests/test_utils.py:49]
- `test_disassociate_attributes_from_instance` (function) — [saleor/attribute/tests/test_utils.py:64]
- `test_associate_attribute_to_product_instance_multiple_values` (function) — [saleor/attribute/tests/test_utils.py:81]
- `test_associate_attribute_to_page_instance_multiple_values` (function) — [saleor/attribute/tests/test_utils.py:109]
- `test_associate_attribute_to_variant_instance_multiple_values` (function) — [saleor/attribute/tests/test_utils.py:135]
- `test_associate_attribute_to_product_copies_data_over_to_new_field` (function) — [saleor/attribute/tests/test_utils.py:159]
- `test_associate_attribute_to_instance_duplicated_values` (function) — [saleor/attribute/tests/test_utils.py:183]
- `test_validate_attribute_owns_values` (function) — [saleor/attribute/tests/test_utils.py:220]
- `test_associate_attribute_to_variant_copies_data_over_to_new_field` (function) — [saleor/attribute/tests/test_utils.py:260]

## How it works

The module's files, as provided to this run:

- `saleor/attribute/tests/fixtures/attribute.py` (895 lines)
- `saleor/attribute/tests/fixtures/translation.py` (67 lines)
- `saleor/attribute/tests/__init__.py` (1 lines)
- `saleor/attribute/tests/fixtures/__init__.py` (2 lines)
- `saleor/attribute/tests/model_helpers.py` (62 lines)
- `saleor/attribute/tests/models/test_base.py` (148 lines)
- `saleor/attribute/tests/test_utils.py` (287 lines)

## Interactions

- Imports from: `saleor/core/db`, `saleor/attribute`
- Imported by: `.semgrep`, `saleor/graphql/core/tests`, `saleor/graphql/translations/tests`, `saleor/permission`

Internal dependencies named in the source:

- `....AttributeEntityType`
- `....AttributeInputType`
- `....AttributeType`
- `....core.editorjs.editorjs_to_text`
- `....core.units.MeasurementUnits`
- `....core.utils.text.safe_truncate`
- `....tests.utils.dummy_editorjs`
- `...AttributeInputType`
- `...AttributeType`
- `...attribute.models.AssignedPageAttributeValue`
- `...models.Attribute`
- `...models.AttributeTranslation`
- `...models.AttributeValue`
- `...models.AttributeValueTranslation`
- `...page.models.Page`
- `...product.models.Product`
- `...product.models.ProductType`
- `...utils.associate_attribute_values_to_instance`
- `..models.Attribute`
- `..models.AttributeValue`
- `.attribute.*  # noqa: F403`
- `.translation.*  # noqa: F403`
- `saleor.attribute.AttributeType`
- `saleor.attribute.models.Attribute`
- `saleor.attribute.models.AttributeValue`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `de90ba83ef00` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
