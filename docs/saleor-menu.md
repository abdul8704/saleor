## Purpose

`saleor/menu` (`saleor/menu`) groups 3 source file(s) exposing 11 top-level declaration(s).

## Public surface

**`saleor/menu/error_codes.py`**

- `MenuErrorCode` (class) — [saleor/menu/error_codes.py:4]

**`saleor/menu/models.py`**

- `Menu` (class) — [saleor/menu/models.py:12]
- `Meta` (class) — [saleor/menu/models.py:16]
- `MenuItem` (class) — [saleor/menu/models.py:24]
- `Meta` (class) — [saleor/menu/models.py:44]
- `get_ordering_queryset` (function) — [saleor/menu/models.py:51]
- `linked_object` (function) — [saleor/menu/models.py:59]
- `MenuItemTranslation` (class) — [saleor/menu/models.py:63]
- `Meta` (class) — [saleor/menu/models.py:69]
- `get_translated_object_id` (function) — [saleor/menu/models.py:80]
- `get_translated_keys` (function) — [saleor/menu/models.py:83]

## How it works

The module's files, as provided to this run:

- `saleor/menu/__init__.py` (1 lines)
- `saleor/menu/error_codes.py` (13 lines)
- `saleor/menu/models.py` (86 lines)

## Interactions

- Imports from: `saleor/product`
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `..core.models.ModelWithMetadata`
- `..core.models.SortableModel`
- `..core.utils.translations.Translation`
- `..page.models.Page`
- `..permission.enums.MenuPermissions`
- `..product.models.Category`
- `..product.models.Collection`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `c0263e95d0ce` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
