## Purpose

`saleor/page/tests` (`saleor/page/tests`) groups 8 source file(s) exposing 16 top-level declaration(s).

## Public surface

**`saleor/page/tests/fixtures/page_translation.py`**

- `page_translation_fr` (function) — [saleor/page/tests/fixtures/page_translation.py:8]

**`saleor/page/tests/fixtures/page_type.py`**

- `page_type` (function) — [saleor/page/tests/fixtures/page_type.py:7]
- `page_type_with_rich_text_attribute` (function) — [saleor/page/tests/fixtures/page_type.py:16]
- `page_type_list` (function) — [saleor/page/tests/fixtures/page_type.py:25]

**`saleor/page/tests/fixtures/page.py`**

- `page` (function) — [saleor/page/tests/fixtures/page.py:10]
- `page_with_rich_text_attribute` (function) — [saleor/page/tests/fixtures/page.py:32]
- `page_list` (function) — [saleor/page/tests/fixtures/page.py:54]
- `page_list_unpublished` (function) — [saleor/page/tests/fixtures/page.py:90]

**`saleor/page/tests/test_search.py`**

- `test_update_pages_search_vector_multiple_pages` (function) — [saleor/page/tests/test_search.py:11]
- `test_update_pages_search_vector_empty_list` (function) — [saleor/page/tests/test_search.py:26]
- `page_list_with_attributes` (function) — [saleor/page/tests/test_search.py:36]
- `test_update_pages_search_vector_constant_queries` (function) — [saleor/page/tests/test_search.py:89]

**`saleor/page/tests/test_tasks.py`**

- `test_update_pages_search_vector` (function) — [saleor/page/tests/test_tasks.py:8]
- `test_update_pages_search_vector_nothing_to_update` (function) — [saleor/page/tests/test_tasks.py:21]
- `test_mark_pages_search_vector_as_dirty` (function) — [saleor/page/tests/test_tasks.py:35]

**`saleor/page/tests/test_utils.py`**

- `test_mark_pages_search_vector_as_dirty_in_batches` (function) — [saleor/page/tests/test_utils.py:8]

## How it works

The module's files, as provided to this run:

- `saleor/page/tests/__init__.py` (1 lines)
- `saleor/page/tests/fixtures/__init__.py` (3 lines)
- `saleor/page/tests/fixtures/page_translation.py` (14 lines)
- `saleor/page/tests/fixtures/page_type.py` (45 lines)
- `saleor/page/tests/fixtures/page.py` (104 lines)
- `saleor/page/tests/test_search.py` (115 lines)
- `saleor/page/tests/test_tasks.py` (48 lines)
- `saleor/page/tests/test_utils.py` (21 lines)

## Interactions

- Imports from: _no measured outgoing edges_
- Imported by: _no measured incoming edges_

Internal dependencies named in the source:

- `....attribute.utils.associate_attribute_values_to_instance`
- `....tests.utils.dummy_editorjs`
- `...attribute.models.AttributeValue`
- `...attribute.utils.associate_attribute_values_to_instance`
- `...models.Page`
- `...models.PageTranslation`
- `...models.PageType`
- `...search.update_pages_search_vector`
- `..models.Page`
- `..tasks.mark_pages_search_vector_as_dirty`
- `..tasks.update_pages_search_vector_task`
- `..utils.mark_pages_search_vector_as_dirty_in_batches`
- `.page.*  # noqa: F403`
- `.page_translation.*  # noqa: F403`
- `.page_type.*  # noqa: F403`

## Gotchas

Documentation for this module was produced by the simulated provider. Source
fingerprint `9a94b95e76d2` — it changes whenever any file above changes, which
is what makes doc propagation testable without a paid model.
