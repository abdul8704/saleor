## Purpose

`saleor/core/tests/commands` (`saleor/core/tests/commands`) groups 3 source file(s) exposing 9 top-level declaration(s).

## Public surface

**`saleor/core/tests/commands/test_clean_editorjs_fields.py`**

- `dirty` (function) — [saleor/core/tests/commands/test_clean_editorjs_fields.py:20]
- `cleaned` (function) — [saleor/core/tests/commands/test_clean_editorjs_fields.py:27]
- `create_dirty_category` (function) — [saleor/core/tests/commands/test_clean_editorjs_fields.py:32]
- `test_handles_errors` (function) — [saleor/core/tests/commands/test_clean_editorjs_fields.py:51]
- `test_detects_dirty_rows` (function) — [saleor/core/tests/commands/test_clean_editorjs_fields.py:72]
- `test_track_progress` (function) — [saleor/core/tests/commands/test_clean_editorjs_fields.py:108]
- `test_filter_models` (function) — [saleor/core/tests/commands/test_clean_editorjs_fields.py:168]
- `test_can_clean_all_models` (function) — [saleor/core/tests/commands/test_clean_editorjs_fields.py:225]

**`saleor/core/tests/commands/test_clearorders.py`**

- `test_delete_checkouts_with_checkout_delivery` (function) — [saleor/core/tests/commands/test_clearorders.py:19]

## How it works

The module's files, as provided to this run:

- `saleor/core/tests/commands/__init__.py` (1 lines)
- `saleor/core/tests/commands/test_clean_editorjs_fields.py` (250 lines)
- `saleor/core/tests/commands/test_clearorders.py` (36 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....attribute.models.base.AttributeValue`
- `....checkout.models.Checkout`
- `....checkout.models.CheckoutDelivery`
- `....page.models.Page`
- `....product.models.Category`
- `....product.models.Collection`
- `...management.commands.clean_editorjs_fields.MODELS`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `3e5ce1b4f05c` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
