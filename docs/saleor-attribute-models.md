## Purpose

`saleor/attribute/models` (`saleor/attribute/models`) groups 5 source file(s) exposing 60 top-level declaration(s).

## Public surface

**`saleor/attribute/models/base.py`**

- `BaseAssignedAttribute` (class) — [saleor/attribute/models/base.py:23]
- `Meta` (class) — [saleor/attribute/models/base.py:26]
- `attribute` (function) — [saleor/attribute/models/base.py:30]
- `BaseAttributeQuerySet` (class) — [saleor/attribute/models/base.py:37]
- `get_public_attributes` (function) — [saleor/attribute/models/base.py:38]
- `get_visible_to_user` (function) — [saleor/attribute/models/base.py:41]
- `AssociatedAttributeQuerySet` (class) — [saleor/attribute/models/base.py:53]
- `get_public_attributes` (function) — [saleor/attribute/models/base.py:54]
- `AttributeQuerySet` (class) — [saleor/attribute/models/base.py:62]
- `get_unassigned_product_type_attributes` (function) — [saleor/attribute/models/base.py:63]
- `get_unassigned_page_type_attributes` (function) — [saleor/attribute/models/base.py:69]
- `get_assigned_product_type_attributes` (function) — [saleor/attribute/models/base.py:74]
- `get_assigned_page_type_attributes` (function) — [saleor/attribute/models/base.py:80]
- `get_public_attributes` (function) — [saleor/attribute/models/base.py:85]
- `product_attributes_sorted` (function) — [saleor/attribute/models/base.py:100]
- `variant_attributes_sorted` (function) — [saleor/attribute/models/base.py:103]
- `product_type_attributes` (function) — [saleor/attribute/models/base.py:106]
- `page_type_attributes` (function) — [saleor/attribute/models/base.py:109]
- `Attribute` (class) — [saleor/attribute/models/base.py:116]
- `Meta` (class) — [saleor/attribute/models/base.py:188]
- `has_values` (function) — [saleor/attribute/models/base.py:203]
- `AttributeTranslation` (class) — [saleor/attribute/models/base.py:207]
- `Meta` (class) — [saleor/attribute/models/base.py:213]
- `get_translated_object_id` (function) — [saleor/attribute/models/base.py:223]
- `get_translated_keys` (function) — [saleor/attribute/models/base.py:226]
- `AttributeValueManager` (class) — [saleor/attribute/models/base.py:230]
- `bulk_get_or_create` (function) — [saleor/attribute/models/base.py:249]
- `bulk_update_or_create` (function) — [saleor/attribute/models/base.py:290]
- `AttributeValue` (class) — [saleor/attribute/models/base.py:365]
- `Meta` (class) — [saleor/attribute/models/base.py:424]
- `input_type` (function) — [saleor/attribute/models/base.py:444]
- `get_ordering_queryset` (function) — [saleor/attribute/models/base.py:447]
- `save` (function) — [saleor/attribute/models/base.py:451]
- `delete` (function) — [saleor/attribute/models/base.py:458]
- `set_current_sorting_order` (function) — [saleor/attribute/models/base.py:491]
- `AttributeValueTranslation` (class) — [saleor/attribute/models/base.py:503]
- `Meta` (class) — [saleor/attribute/models/base.py:514]
- `get_translated_object_id` (function) — [saleor/attribute/models/base.py:524]
- `get_translated_keys` (function) — [saleor/attribute/models/base.py:527]
- `get_translation_context` (function) — [saleor/attribute/models/base.py:530]

**`saleor/attribute/models/page.py`**

- `AssignedPageAttributeValue` (class) — [saleor/attribute/models/page.py:9]
- `Meta` (class) — [saleor/attribute/models/page.py:24]
- `get_ordering_queryset` (function) — [saleor/attribute/models/page.py:29]
- `AttributePage` (class) — [saleor/attribute/models/page.py:33]
- `Meta` (class) — [saleor/attribute/models/page.py:43]
- `get_ordering_queryset` (function) — [saleor/attribute/models/page.py:47]

**`saleor/attribute/models/product_variant.py`**

- `AssignedVariantAttributeValue` (class) — [saleor/attribute/models/product_variant.py:8]
- `Meta` (class) — [saleor/attribute/models/product_variant.py:27]
- `get_ordering_queryset` (function) — [saleor/attribute/models/product_variant.py:31]
- `AssignedVariantAttribute` (class) — [saleor/attribute/models/product_variant.py:35]
- `Meta` (class) — [saleor/attribute/models/product_variant.py:51]
- `AttributeVariant` (class) — [saleor/attribute/models/product_variant.py:55]
- `Meta` (class) — [saleor/attribute/models/product_variant.py:73]
- `get_ordering_queryset` (function) — [saleor/attribute/models/product_variant.py:77]

**`saleor/attribute/models/product.py`**

- `AssignedProductAttributeValue` (class) — [saleor/attribute/models/product.py:9]
- `Meta` (class) — [saleor/attribute/models/product.py:24]
- `get_ordering_queryset` (function) — [saleor/attribute/models/product.py:31]
- `AttributeProduct` (class) — [saleor/attribute/models/product.py:35]
- `Meta` (class) — [saleor/attribute/models/product.py:45]
- `get_ordering_queryset` (function) — [saleor/attribute/models/product.py:49]

## How it works

The module's files, as provided to this run:

- `saleor/attribute/models/__init__.py` (27 lines)
- `saleor/attribute/models/base.py` (556 lines)
- `saleor/attribute/models/page.py` (48 lines)
- `saleor/attribute/models/product_variant.py` (78 lines)
- `saleor/attribute/models/product.py` (50 lines)

## Interactions

- Imports from: `saleor/core`, `saleor/attribute`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `...AttributeEntityType`
- `...AttributeInputType`
- `...AttributeType`
- `...account.models.User`
- `...app.models.App`
- `...core.db.fields.SanitizedJSONField`
- `...core.editorjs.clean_editorjs`
- `...core.models.ModelWithExternalReference`
- `...core.models.ModelWithMetadata`
- `...core.models.SortableModel`
- `...core.units.MeasurementUnits`
- `...core.utils.translations.Translation`
- `...page.models.Page`
- `...page.models.PageType`
- `...permission.enums.PageTypePermissions`
- `...permission.enums.ProductTypePermissions`
- `...permission.utils.has_one_of_permissions`
- `...product.models.Category`
- `...product.models.Collection`
- `...product.models.Product`
- `...product.models.ProductType`
- `...product.models.ProductVariant`
- `..lock_objects.attribute_value_qs_select_for_update`
- `.base.AssociatedAttributeManager`
- `.base.AttributeValue`
- `.base.BaseAssignedAttribute`
- `.page.AssignedPageAttributeValue`
- `.page.AttributePage`
- `.product.AssignedProductAttributeValue`
- `.product.AttributeProduct`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `5f042f7eb42d` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
