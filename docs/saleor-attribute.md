## Purpose

`saleor/attribute` (`saleor/attribute`) groups 5 source file(s) exposing 13 top-level declaration(s).

## Public surface

**`saleor/attribute/__init__.py`**

- `AttributeInputType` (class) — [saleor/attribute/__init__.py:1]
- `AttributeType` (class) — [saleor/attribute/__init__.py:97]
- `AttributeEntityType` (class) — [saleor/attribute/__init__.py:104]

**`saleor/attribute/error_codes.py`**

- `AttributeErrorCode` (class) — [saleor/attribute/error_codes.py:4]
- `AttributeBulkCreateErrorCode` (class) — [saleor/attribute/error_codes.py:13]
- `AttributeBulkUpdateErrorCode` (class) — [saleor/attribute/error_codes.py:25]

**`saleor/attribute/lock_objects.py`**

- `attribute_value_qs_select_for_update` (function) — [saleor/attribute/lock_objects.py:6]
- `attribute_reference_product_types_qs_select_for_update` (function) — [saleor/attribute/lock_objects.py:12]
- `attribute_reference_page_types_qs_select_for_update` (function) — [saleor/attribute/lock_objects.py:18]

**`saleor/attribute/search.py`**

- `get_search_vectors_for_attribute_values` (function) — [saleor/attribute/search.py:11]
- `get_reference_attribute_search_value` (function) — [saleor/attribute/search.py:81]

**`saleor/attribute/utils.py`**

- `associate_attribute_values_to_instance` (function) — [saleor/attribute/utils.py:32]
- `validate_attribute_owns_values` (function) — [saleor/attribute/utils.py:48]

## How it works

The module's files, as provided to this run:

- `saleor/attribute/__init__.py` (123 lines)
- `saleor/attribute/error_codes.py` (34 lines)
- `saleor/attribute/lock_objects.py` (21 lines)
- `saleor/attribute/search.py` (93 lines)
- `saleor/attribute/utils.py` (261 lines)

## Interactions

- Imports from: `saleor/graphql/product/types`
- Imported by: `saleor/attribute/models`, `saleor/attribute/tests`

Internal dependencies named in the source:

- `..attribute.AttributeInputType`
- `..core.editorjs.editorjs_to_text`
- `..core.postgres.NoValidationSearchVector`
- `..page.models.Page`
- `..product.models.Product`
- `..product.models.ProductVariant`
- `.models.Attribute`
- `.models.AttributeValue`
- `.models.base.Attribute`
- `.models.base.AttributeValue`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `8d287fd05b6f` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
